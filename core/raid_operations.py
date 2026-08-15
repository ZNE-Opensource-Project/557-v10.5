import discord


async def raid_http(interaction: discord.Interaction, message: str):
    webhook = discord.Webhook.partial(
        interaction.client.user.id,
        interaction.token,
        session=interaction.client.http._HTTPClient__session,
    )
    for _ in range(5):
        await webhook.send(message)
