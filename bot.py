import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)

from content import Article


TOKEN = os.getenv("BOT_TOKEN")

TITLE, TEXT = range(2)

article = Article()


async def new_article(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "عنوان مقاله را ارسال کن."
    )
    return TITLE


async def get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    article.title = update.message.text

    await update.message.reply_text(
        "متن مقاله را ارسال کن."
    )

    return TEXT


async def get_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    article.text = update.message.text

    await update.message.reply_text(
        "مقاله دریافت شد."
    )

    return ConversationHandler.END


def main():

    app = Application.builder().token(TOKEN).build()

    conversation = ConversationHandler(
        entry_points=[
            CommandHandler("new", new_article)
        ],

        states={
            TITLE: [
                MessageHandler(
                    filters.TEXT,
                    get_title
                )
            ],

            TEXT: [
                MessageHandler(
                    filters.TEXT,
                    get_text
                )
            ]
        },

        fallbacks=[]
    )

    app.add_handler(conversation)

    print("Ofogh Roydad Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
