import asyncio
import telegram

from constants import TOKEN

async def main():
    bot= telegram.Bot(TOKEN)
    async with bot:
        print(await bot.get_me())


if __name__=="__main__":
    asyncio.run(main())