import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 FX Trading AI Bot Online!\n\n"
        "Commands:\n"
        "/analyze - Market Analysis\n"
        "/strategy - Strategy Test"
    )


async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 FX Trading AI Analysis\n\n"
        "Market: Checking...\n"
        "Trend: Waiting for data..."
    )


async def strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 Send your trading strategy.\n"
        "Example:\n"
        "EMA 20 cross EMA 50 + RSI"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analyze", analyze))
app.add_handler(CommandHandler("strategy", strategy))


print("FX Trading AI Bot Running...")

app.run_polling()
