from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ربات افق رویداد فعال است."
    )

def main():
    print("Ofogh Roydad Bot Started")

if __name__ == "__main__":
    main()
