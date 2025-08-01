import discord
from discord.ext import commands
import glob


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="/", intents=intents)

    async def on_ready(self):
        if self.user:
            print(f"Logged in as @{self.user.name}")

    async def setup_hook(self):
        cogs = glob.glob("src/cogs/**/*.py", recursive=True)

        for path in cogs:
            cog = path.replace("/", ".").replace("\\", ".").removesuffix(".py")
            await self.load_extension(cog)
            print(f"Loaded {path} ({cog})")

        await self.tree.sync()
