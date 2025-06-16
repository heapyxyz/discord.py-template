from src import Bot
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()
    token = os.environ.get("BOT_TOKEN")

    if not token:
        raise Exception("BOT_TOKEN variable isn't set")

    bot = Bot()
    bot.run(token)
