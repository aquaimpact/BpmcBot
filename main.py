import os

import logging
from dotenv import load_dotenv

from telegram import Update, Bot
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler

from webscraper import webscraper

# Automation Libraries


# Load environment variables
load_dotenv()
TOKEN = os.getenv('BOT_API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def sendTemplate(update, context):
    """Send a message and photo when the command /start is issued."""
    chat_id = -4634623504  # Get chat ID of the user
                           # -2287006194
    data = webscraper()  # Fetch data from the webscraper function
    try:
        caption = (
            f"<b>{data['Title:']}</b>\n\n"
            f"<b>SCRIPTURE:</b>\n{data['Verse:']}\n\n"
            f"<b>READ:</b>\n{data['Read']}\n\n"
            f"{data['URL']}"
        )

        await context.bot.send_photo(
            chat_id=chat_id,
            photo=data['Image'],
            caption=caption,
            parse_mode=ParseMode.HTML
        )
    except Exception as e:
        logger.error(f"Error sending photo: {e}")
        await context.bot.send_message(chat_id=chat_id, text="Failed to send the photo. Please try again later.")   

def register_handlers(app: Application) -> None:
    sendTemplate_handler = CommandHandler("sendTemplate", sendTemplate)
    app.add_handler(sendTemplate_handler)


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    register_handlers(application)

    logger.info("Starting polling...")
    application.run_polling()
    

if __name__ == "__main__":
    main()
