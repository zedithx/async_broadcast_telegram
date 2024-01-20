import asyncio
import os
from dotenv import load_dotenv

from telebot.async_telebot import AsyncTeleBot
TOKEN = os.environ.get('TOKEN')
bot = AsyncTeleBot(TOKEN)
userID_database = {}


async def announce_luckydraw():
    tasks = []
    for userID in userID_database:
        tasks.append(asyncio.create_task(
            bot.send_message(userID, "The LCC lucky draw is ending soon. Please make your way down to the "
                                     "Campus Centre by 5.30pm for the reveal of the results! \n\n")
        ))
    await asyncio.gather(*tasks)

asyncio.run(announce_luckydraw())

