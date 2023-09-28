import asyncio
import telegram

from constants import TOKEN

# async def main():
#     bot= telegram.Bot(TOKEN)
#     async with bot:
#         print(await bot.get_me())

# async def main():
#     bot= telegram.Bot(TOKEN)
#     async with bot:
#         print((await bot.get_updates()))  # this results a tuple each updata is numbered

async def main():
    bot= telegram.Bot(TOKEN)
    async with bot:
        await bot.send_message(text="first message", chat_id=821915079)




if __name__=="__main__":
    asyncio.run(main())