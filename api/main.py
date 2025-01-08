import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from webscraper import webscraper

# Automation Libraries


# Load environment variables
load_dotenv()
TOKEN = os.getenv('BOT_API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def sendTemplate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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


if __name__ == "__main__":
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("sendTemplate", sendTemplate))

    # Set up the scheduler
    


    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
