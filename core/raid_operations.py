import json
from urllib.parse import quote

import aiohttp


async def _send(application_id: str, token: str, content: str):
    url = f"https://discord.com/api/v10/webhooks/{application_id}/{quote(token, safe='')}"
    payload = json.dumps({"content": content}).encode()
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
        ) as resp:
            resp.raise_for_status()


async def raid_http(interaction, message: str):
    app_id = str(interaction.client.user.id)
    token = interaction.token
    tasks = [_send(app_id, token, message) for _ in range(5)]
    await asyncio.gather(*tasks)
