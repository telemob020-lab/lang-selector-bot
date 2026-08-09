from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# =========================
# Bot Token
# =========================
# لا تضع الـ Token الحقيقي هنا عند رفع المشروع.
# سنضعه لاحقًا في Railway كـ Environment Variable.
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")


# =========================
# /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇪🇬 العربية", callback_data="lang_ar"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        ],
        [
            InlineKeyboardButton("🇫🇷 Français", callback_data="lang_fr"),
            InlineKeyboardButton("🇩🇪 Deutsch", callback_data="lang_de"),
        ],
        [
            InlineKeyboardButton("🇵🇹 Português", callback_data="lang_pt"),
            InlineKeyboardButton("🇮🇹 Italiano", callback_data="lang_it"),
        ],
        [
            InlineKeyboardButton("🇹🇷 Türkçe", callback_data="lang_tr"),
            InlineKeyboardButton("🇮🇷 فارسی", callback_data="lang_fa"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
    "🌍  Choose your language:",
        reply_markup=reply_markup,
    )


# =========================
# Language Selection
# =========================
async def language_selected(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query

    # إبلاغ Telegram أن الزر تم الضغط عليه
    await query.answer()

    languages = {
        "lang_ar": "العربية 🇪🇬",
        "lang_en": "English 🇬🇧",
        "lang_fr": "Français 🇫🇷",
        "lang_de": "Deutsch 🇩🇪",
        "lang_pt": "Português 🇵🇹",
        "lang_it": "Italiano 🇮🇹",
        "lang_tr": "Türkçe 🇹🇷",
        "lang_fa": "فارسی 🇮🇷",
    }

    selected_language = languages.get(query.data)

    if not selected_language:
        return

    # نحفظ اختيار اللغة مؤقتًا في بيانات المستخدم
    context.user_data["language"] = query.data

    await query.edit_message_text(
        f"✅ تم اختيار اللغة: {selected_language}\n\n"
        "نكمل إعداد البوت..."
    )


# =========================
# Main
# =========================
def main():
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN غير موجود. أضفه في Environment Variables."
        )

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        CallbackQueryHandler(language_selected, pattern=r"^lang_")
    )

    print("🤖 Bot is running...")

    application.run_polling()


if __name__ == "__main__":
    main()
