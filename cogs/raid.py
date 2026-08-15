import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import View, Button
from pathlib import Path


class RaidView(View):
    def __init__(self, message: str):
        super().__init__(timeout=None)
        self.message = message

    @discord.ui.button(
        style=discord.ButtonStyle.success,
        label="ad r4id",
        emoji="☣️"
    )
    async def raid_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        for _ in range(5):
            await interaction.followup.send(self.message)


class Raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.raid_message = (
            Path(__file__).parent.parent / "messages" / "ad.txt"
        ).read_text(encoding="utf-8").strip()

    @app_commands.command(name="ad-r4id", description="spam the ad r4id")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def raid(self, interaction: discord.Interaction):
        embed = discord.Embed(
            color=25600,
            description="click the button below to start the ad r4id!\nalso u can click on it multiple times",
        )
        await interaction.response.send_message(embed=embed, view=RaidView(self.raid_message), ephemeral=True)


async def setup(bot):
    await bot.add_cog(Raid(bot))
