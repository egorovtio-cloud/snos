from hikka import loader, utils
import aiohttp
import os
import asyncio
from telethon.tl.types import MessageMediaDocument, DocumentAttributeFilename

class AdvancedWhisperMod(loader.Module):
    """Whisper модуль для распознавания голосовых и видео сообщений"""
    strings = {"name": "AdvancedWhisper"}

    async def client_ready(self, client, db):
        self.client = client

    async def wcmd(self, message):
        """Автоматическое распознавание голосовых/видео сообщений"""
        API_KEY = "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"
        
        reply = await message.get_reply_message()
        if not reply or not reply.media:
            return await utils.answer(message, "❌ Ответьте на голосовое или видео сообщение")

        if isinstance(reply.media, MessageMediaDocument):
            attributes = reply.media.document.attributes
            filename = next((attr.file_name for attr in attributes if isinstance(attr, DocumentAttributeFilename)), None)
            
            if filename and any(x in filename.lower() for x in ['.ogg', '.mp3', '.wav', '.m4a', '.mp4']):
                await utils.answer(message, "🔍 Начинаю обработку медиа...")
                
                file = await self.client.download_media(reply.media, bytes)
                
                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "audio/mpeg"  # Или соответствующий MIME-тип
                }
                
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.post(
                            "https://api.openai.com/v1/audio/transcriptions",
                            headers=headers,
                            data={"file": file, "model": "whisper-1"}
                        ) as resp:
                            data = await resp.json()
                            if resp.status == 200:
                                text = data.get("text", "Не удалось распознать текст")
                                await utils.answer(message, f"📝 Распознанный текст:\n\n{text}")
                            else:
                                await utils.answer(message, f"❌ Ошибка API: {data.get('error', 'Unknown error')}")
                except Exception as e:
                    await utils.answer(message, f"⚠️ Ошибка: {str(e)}")
            else:
                await utils.answer(message, "❌ Формат файла не поддерживается")
        else:
            await utils.answer(message, "❌ Это не голосовое/видео сообщение")