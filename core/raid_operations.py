import asyncio

import aiohttp


async def send_message_http(session: aiohttp.ClientSession, application_id: int, interaction_token: str, content: str):
    url = f"https://discord.com/api/v10/webhooks/{application_id}/{interaction_token}"
    payload = {"content": content, "allowed_mentions": {"parse": ["everyone", "users", "roles"]}}
    async with session.post(url, json=payload) as resp:
        resp.raise_for_status()


async def raid_http(interaction, message: str):
    app_id = interaction.client.user.id
    token = interaction.token
    async with aiohttp.ClientSession() as session:
        tasks = [send_message_http(session, app_id, token, message) for _ in range(5)]
        await asyncio.gather(*tasks)
