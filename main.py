import asyncio

from telebot.async_telebot import AsyncTeleBot
userID_database = []
TOKEN = '5631416352:AAGNTPtHwtzZi3dEpywSRDLSzD7e9vJBYVA'
bot = AsyncTeleBot(TOKEN)
# temp_db = []
# temp_db = []
# First broadcast message to everyone

# async def hype_message():
#     tasks = []
#     for userID in userID_database:
#         tasks.append(asyncio.create_task(
#             bot.send_message(userID, "Have u signed up for Echo@Cove yet? We are only 3 days away from it! "
#                                      "Sign up now to not miss out!")
#         ))
#     await asyncio.gather(*tasks)
#
# asyncio.run(hype_message())

async def hype_message():
    tasks = []
    for userID in userID_database:
        tasks.append(asyncio.create_task(
            bot.send_message(userID, "We are only 3 days away from Echo@Cove! Have u signed up for Echo@Cove yet? \n\n"
                                     "Here are some things you can look forward to on the day itself! \n\n"
                                     "1. Themed music will be played and the songs you've requested will be played on the night! \n\n"
                                     "2. You will be wearing the same coloured glowsticks as those that chose the same theme as you! \n\n"
                                     "3. Free drinks will be available on a first come first serve basis \n\n"
                                     "4. There will be board games on level 2 for you to go chill with your friends with! \n\n"
                                     "5. There will even be a unique photobooth for you to capture all the memories of this event! \n\n"
                                     "/start to sign up now and not miss out!!!!!")
        ))
    await asyncio.gather(*tasks)

async def reminder_message():
    tasks = []
    for userID in userID_database:
        tasks.append(asyncio.create_task(
            bot.send_message(userID, "ECHO @COVE will be starting soon at 7pm at the Root Cove (2.311A). See you there!")
        ))
    await asyncio.gather(*tasks)

asyncio.run(reminder_message())

# TODO - update to let them know what popular artists are being played. eg. One direction. Monday + last 3 days

# TODO - Time and location on the day itself

