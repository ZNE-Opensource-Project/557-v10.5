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
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="v10.5 | /r4id (FLASH)",
            ),
            status=discord.Status.dnd,
            allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True),
        )

    async def setup_hook(self):
        await self.load_extension("cogs.raid")
        await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user}")

def is_blacklisted_guild(interaction: discord.Interaction) -> bool:
    if interaction.guild:
        bl_guild = interaction.client.config.get("bl_guild")
        if bl_guild and interaction.guild.id == int(bl_guild):
            raise app_commands.CheckFailure("this server is whitelisted nigga")
    return True

def start():
    bot = Bot()
    bot.run(Bot().config["token"])
