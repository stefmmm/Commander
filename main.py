import os, discord, discord.ext, logging
from dotenv import load_dotenv
from discord.ext import commands
from requests import get, post

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_GUILD = os.getenv('BOT_GUILD')
MCSS_KEY = os.getenv('MCSS_KEY')
MCSS_API = os.getenv('MCSS_API')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix='$%')

logger = logging.getLogger("discord.bot")

headers = {"apiKey": f"{MCSS_KEY}"}
url1 = f"{MCSS_API}/api/v2/servers?filter=0"


@client.event
async def on_ready():
    await client.tree.sync(guild=None)
    # await client.tree.sync(guild=discord.Object(BOT_GUILD)) #uncomment to only sync to 1 guild
    logger.info(f"We have logged in as {client.user}")
    for guild in client.guilds:
        logger.info(f"In Guild: {guild.id} {guild.name}")


@client.hybrid_group(name="server", with_app_command=True)
async def server(ctx):
    return


@server.command(name="start", with_app_command=True, description="start a server")
@commands.is_owner()
async def server_start(ctx, name: str):
    serverinfo = ''
    sAction = {"action":"start"}
    req = get(url=url1, headers=headers)
    result = req.json()
    logger.info(result)
    for server in result:
        if name == server["name"]:
            serverinfo = [server['name'], server['serverId'], server['status']]
        else:
            await ctx.send("Server not found.")
    url2 = f"{MCSS_API}/api/v2/servers/{serverinfo[1]}/execute/action"
    if serverinfo[2] == 0:
        req2 = post(url=url2, headers=headers, json=sAction)
        logger.info(req2.status_code)
        await ctx.send(f"Started server: {serverinfo[0]}")
    else:
        await ctx.send(f"Server {serverinfo[0]} is already running.")


@server.command(name="stop", with_app_command=True, description="stop a server")
@commands.is_owner()
async def server_stop(ctx, name: str):
    serverinfo = ''
    sAction = {"action":"stop"}
    req = get(url=url1, headers=headers)
    result = req.json()
    logger.info(result)
    for server in result:
        if name == server["name"]:
            serverinfo = [server['name'], server['serverId'], server['status']]
        else:
            await ctx.send("Server not found.")
    url2 = f"{MCSS_API}/api/v2/servers/{serverinfo[1]}/execute/action"
    if serverinfo[2] == 1:
        req2 = post(url=url2, headers=headers, json=sAction)
        logger.info(req2.status_code)
        await ctx.send(f"Stopping server: {serverinfo[0]}")
    else:
        await ctx.send(f"Server {serverinfo[0]} is already stopped.")

client.run(BOT_TOKEN)
