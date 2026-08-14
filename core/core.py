import discord
from discord import app_commands
from discord.ext import commands
import json
from pathlib import Path


class Bot(commands.Bot):
    def __init__(self):
        with open(Path(__file__).parent.parent / "config.json") as f:
            self.config = json.load(f)
        super().__init__(
            command_prefix=self.config["prefix"],
            intents=discord.Intents.default(),
        )

    async def setup_hook(self):
        await self.load_extension("cogs.raid")
        await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user}")


def start():
    bot = Bot()
    bot.run(Bot().config["token"])
