import asyncio
import random
from hikka import utils, loader

class SnosMod(loader.Module):
    """Модуль для массового сноса через жалобы"""
    strings = {"name": "SnosSystem"}

    async def snoscmd(self, message):
        """Запустить процесс сноса"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "❌ Укажи цель для сноса, дебил.")
            return

        target = args
        progress_msg = await utils.answer(message, "🔥 Снос начинается, отправка жалоб...\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 0%")
        
        progress = 0
        progress_bar = ["⬜️"] * 10
        
        while progress <= 100:
            await asyncio.sleep(0.6)
            progress += 2
            
            # Заменяем кубик каждые 10%
            if progress % 10 == 0 and progress > 0:
                progress_bar[progress//10 - 1] = "🟩"
            
            bar = "".join(progress_bar)
            await utils.answer(progress_msg, f"🔥 Снос начинается, отправка жалоб...\n{bar} {progress}%")
        
        complaints = random.randint(200, 400)
        result_text = (
            f"✅ Отправка жалоб закончена\n\n"
            f"📊 Жалоб: {complaints}\n"
            f"🎯 Цель: {target}\n"
            f"💀 Статус: Скорее всего, уже снесено"
        )
        
        await utils.answer(progress_msg, result_text)