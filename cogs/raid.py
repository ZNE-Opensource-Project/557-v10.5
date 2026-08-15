"""
the raid cog.

command status: 
/ad-r4id = complete
/avatar = complete
"""

import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import View, Button
from pathlib import Path
from core.raid_operations import raid_http


class RaidView(View):
    def __init__(self, message: str, instant: bool = False):
        super().__init__(timeout=None)
        self.message = message
        self.instant = instant

    @discord.ui.button(
        style=discord.ButtonStyle.success,
        label="ad r4id",
        emoji="☣️"
    )
    async def raid_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.defer()
        if self.instant:
            await raid_http(interaction, self.message)
        else: # doesnt really speed it up though
            tasks = [
                asyncio.create_task(interaction.followup.send(self.message))
                for _ in range(5)
            ]
            await asyncio.gather(*tasks)


class Raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.raid_message = (
            Path(__file__).parent.parent / "messages" / "ad.txt"
        ).read_text(encoding="utf-8").strip()

    @app_commands.command(name="ad-r4id", description="spam the ad r4id")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.describe(instant="sends r4id messages instantly")
    async def raid(self, interaction: discord.Interaction, instant: bool = False):
        embed = discord.Embed(
            color=25600,
            description="click the button below to start the ad r4id!\nalso u can click on it multiple times",
        )
        await interaction.response.send_message(
            embed=embed,
            view=RaidView(self.raid_message, instant=instant),
            ephemeral=True,
        )


    @app_commands.command(name="avatar", description="fetch user profile picture")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    @app_commands.describe(user="user to get avatar from")
    async def avatar(self, interaction: discord.Interaction, user: discord.User = None):
        target = user or interaction.user
        embed = discord.Embed(
            color=2449420,
            title=f"{target}'s Avatar",
        )
        embed.set_image(url=target.display_avatar.url)
        embed.add_field(
            name="Link",
            value="[Click here](https://link.com/)",
            inline=False,
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Raid(bot))
