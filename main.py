```python
import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)


# ==========================================
# Bot Token
# ==========================================

BOT_TOKEN = os.getenv("BOT_TOKEN")


# ==========================================
# Language Data
# ==========================================
# غيّر النصوص والروابط هنا حسب موقعك.

LANGUAGES = {
    "lang_ar": {
        "name": "العربية 🇪🇬",
        "message": "🔗 هذا هو الرابط الرسمي للموقع باللغة العربية:",
        "button": "فتح الموقع 🇪🇬",
        "url": "https://example.com/ar",
    },

    "lang_en": {
        "name": "English 🇬🇧",
        "message": "🔗 Here is the official website in English:",
        "button": "Open Website 🇬🇧",
        "url": "https://example.com/en",
    },

    "lang_fr": {
        "name": "Français 🇫🇷",
        "message": "🔗 Voici le site officiel en français :",
        "button": "Ouvrir le site 🇫🇷",
        "url": "https://example.com/fr",
    },

    "lang_de": {
        "name": "Deutsch 🇩🇪",
        "message": "🔗 Hier ist die offizielle Website auf Deutsch:",
        "button": "Website öffnen 🇩🇪",
        "url": "https://example.com/de",
    },

    "lang_pt": {
        "name": "Português 🇵🇹",
        "message": "🔗 Aqui está o site oficial em português:",
        "button": "Abrir o site 🇵🇹",
        "url": "https://example.com/pt",
    },

    "lang_it": {
        "name": "Italiano 🇮🇹",
        "message": "🔗 Ecco il sito ufficiale in italiano:",
        "button": "Apri il sito 🇮🇹",
        "url": "https://example.com/it",
    },

    "lang_tr": {
        "name": "Türkçe 🇹🇷",
        "message": "🔗 Türkçe resmi web sitesi:",
        "button": "Web sitesini aç 🇹🇷",
        "url": "https://example.com/tr",
    },

    "lang_fa": {
        "name": "فارسی 🇮🇷",
        "message": "🔗 این لینک رسمی وب‌سایت به زبان فارسی است:",
        "button": "باز کردن وب‌سایت 🇮🇷",
        "url": "https://example.com/fa",
    },
}


# ==========================================
# /start
# ==========================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [
        [
            InlineKeyboardButton(
                "🇪🇬 العربية",
                callback_data="lang_ar"
            ),
            InlineKeyboardButton(
                "🇬🇧 English",
                callback_data="lang_en"
            ),
        ],

        [
            InlineKeyboardButton(
                "🇫🇷 Français",
                callback_data="lang_fr"
            ),
            InlineKeyboardButton(
                "🇩🇪 Deutsch",
                callback_data="lang_de"
            ),
        ],

        [
            InlineKeyboardButton(
                "🇵🇹 Português",
                callback_data="lang_pt"
            ),
            InlineKeyboardButton(
                "🇮🇹 Italiano",
                callback_data="lang_it"
            ),
        ],

        [
            InlineKeyboardButton(
                "🇹🇷 Türkçe",
                callback_data="lang_tr"
            ),
            InlineKeyboardButton(
                "🇮🇷 فارسی",
                callback_data="lang_fa"
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🌍 اختر لغتك / Choose your language:",
        reply_markup=reply_markup,
    )


# ==========================================
# Language Selected
# ==========================================

async def language_selected(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    # إيقاف حالة تحميل الزر
    await query.answer()

    language_code = query.data

    # التأكد أن اللغة موجودة
    language = LANGUAGES.get(language_code)

    if not language:
        return

    # حفظ اللغة للمستخدم
    context.user_data["language"] = language_code

    # إنشاء زر الموقع
    website_button = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                language["button"],
                url=language["url"]
            )
        ]
    ])

    # حذف رسالة اختيار اللغة وإظهار الرسالة الجديدة
    await query.edit_message_text(
        text=language["message"],
        reply_markup=website_button
    )


# ==========================================
# Main
# ==========================================

def main():

    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN غير موجود في Environment Variables."
        )

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # /start
    application.add_handler(
        CommandHandler("start", start)
    )

    # اختيار اللغة
    application.add_handler(
        CallbackQueryHandler(
            language_selected,
            pattern=r"^lang_"
        )
    )

    print("🤖 Bot is running...")

    application.run_polling()


# ==========================================
# Run Bot
# ==========================================

if __name__ == "__main__":
    main()
```

### `requirements.txt`

```text
python-telegram-bot==22.5
```
