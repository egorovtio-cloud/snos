from hikka import loader, utils
import aiohttp
import json

class WhisperMod(loader.Module):
    """Whisper модуль для Hikka"""
    strings = {"name": "WhisperMod"}

    async def whispercmd(self, message):
        """Отправка whisper сообщения"""
        args = utils.get_args_raw(message)
        if not args:
            return await utils.answer(message, "❌ Укажите текст сообщения")

        API_KEY = "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"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "text": args,
            "language": "ru"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://api.openai.com/v1/whisper",
                    headers=headers,
                    json=payload
                ) as resp:
                    data = await resp.json()
                    if resp.status == 200:
                        await utils.answer(message, f"✅ Сообщение отправлено: {data['response']}")
                    else:
                        await utils.answer(message, f"❌ Ошибка: {data.get('error', 'Unknown error')}")
        except Exception as e:
            await utils.answer(message, f"⚠️ Критическая ошибка: {str(e)}")