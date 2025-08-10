from hikka import loader, utils
import asyncio
from time import time

class MusicLyricsMod(loader.Module):
    """Анимированные текст песни Rock Your Body"""
    strings = {"name": "RockYourBody"}

    async def rockyourbodycmd(self, message):
        """Анимированный вывод текста песни"""
        lyrics = [
            ("I wanna da-", 0.06),
            ("I wanna dance in the lights", 0.05),
            ("I wanna ro-", 0.07),
            ("I wanna rock your body", 0.08),
            ("I wanna go", 0.08),
            ("I wanna go for a ride", 0.068),
            ("Hop in the music and", 0.07),
            ("Rock your body", 0.08),
            ("Rock that body", 0.069),
            ("Come on, come on", 0.035),
            ("(Rock your body)", 0.05),
            ("Rock that body", 0.03),
            ("Rock that body", 0.049),
            ("Come on, come on", 0.035),
            ("Rock that body", 0.08),
        ]

        msg = await utils.answer(message, "🎵 Rock Your Body Lyrics 🎵\n(инициализация...)")
        text = ""
        
        for line, delay in lyrics:
            text += f"{line}\n"
            start_time = time()
            await utils.answer(msg, f"🎵 Rock Your Body Lyrics 🎵\n\n{text}")
            elapsed = time() - start_time
            remaining = max(0, delay - elapsed)
            await asyncio.sleep(remaining)
