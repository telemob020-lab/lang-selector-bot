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
        "message": """**مرحبًا بك في البوت الرسمي! 🌍**

هذا البوت يوفر لك الوصول إلى الموقع الرسمي والمعلومات المتاحة لمنطقتك.

متاح على مدار الساعة:

• روابط الموقع الرسمية لمنطقتك
• أدلة ومعلومات مفيدة
• آخر التحديثات والمعلومات العامة

**الروابط الرسمية:**""",
        "button": "فتح الموقع 🇪🇬",
        "url": "https://example.com/ar",
    },

    "lang_en": {
        "name": "English 🇬🇧",
        "message": """**Welcome to the official bot! 🌍**

This bot provides access to the official website and information available for your region.

Available 24/7:

• Official website links for your region
• Useful guides and information
• Latest updates and general information

**Official resources:**""",
        "button": "Open Website 🇬🇧",
        "url": "https://example.com/en",
    },

    "lang_fr": {
        "name": "Français 🇫🇷",
        "message": """**Bienvenue sur le bot officiel ! 🌍**

Ce bot vous permet d'accéder au site officiel et aux informations disponibles dans votre région.

Disponible 24h/24 et 7j/7 :

• Liens officiels pour votre région
• Guides et informations utiles
• Dernières mises à jour et informations générales

**Ressources officielles :**""",
        "button": "Ouvrir le site 🇫🇷",
        "url": "https://example.com/fr",
    },

    "lang_de": {
        "name": "Deutsch 🇩🇪",
        "message": """**Willkommen beim offiziellen Bot! 🌍**

Dieser Bot bietet Ihnen Zugriff auf die offizielle Website und Informationen für Ihre Region.

Rund um die Uhr verfügbar:

• Offizielle Links für Ihre Region
• Nützliche Anleitungen und Informationen
• Aktuelle Updates und allgemeine Informationen

**Offizielle Ressourcen:**""",
        "button": "Website öffnen 🇩🇪",
        "url": "https://example.com/de",
    },

    "lang_pt": {
        "name": "Português 🇵🇹",
        "message": """**Bem-vindo ao bot oficial! 🌍**

Este bot fornece acesso ao site oficial e às informações disponíveis para a sua região.

Disponível 24 horas por dia:

• Links oficiais para a sua região
• Guias e informações úteis
• Atualizações e informações gerais

**Recursos oficiais:**""",
        "button": "Abrir o site 🇵🇹",
        "url": "https://example.com/pt",
    },

    "lang_it": {
        "name": "Italiano 🇮🇹",
        "message": """**Benvenuto nel bot ufficiale! 🌍**

Questo bot offre accesso al sito ufficiale e alle informazioni disponibili nella tua regione.

Disponibile 24 ore su 24:

• Link ufficiali per la tua regione
• Guide e informazioni utili
• Aggiornamenti e informazioni generali

**Risorse ufficiali:**""",
        "button": "Apri il sito 🇮🇹",
        "url": "https://example.com/it",
    },

    "lang_tr": {
        "name": "Türkçe 🇹🇷",
        "message": """**Resmi bota hoş geldiniz! 🌍**

Bu bot, resmi web sitesine ve bölgenizde mevcut olan bilgilere erişim sağlar.

7/24 kullanılabilir:

• Bölgeniz için resmi bağlantılar
• Yararlı rehberler ve bilgiler
• Güncel ve genel bilgiler

**Resmi kaynaklar:**""",
        "button": "Web sitesini aç 🇹🇷",
        "url": "https://example.com/tr",
    },

    "lang_fa": {
        "name": "فارسی 🇮🇷",
        "message": """**به ربات رسمی خوش آمدید! 🌍**

این ربات دسترسی به وب‌سایت رسمی و اطلاعات موجود برای منطقه شما را فراهم می‌کند.

به صورت ۲۴ ساعته در دسترس است:

• لینک‌های رسمی برای منطقه شما
• راهنماها و اطلاعات مفید
• آخرین به‌روزرسانی‌ها و اطلاعات عمومی

**منابع رسمی:**""",
        "button": "باز کردن وب‌سایت 🇮🇷",
        "url": "https://example.com/fa",
    },
}
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
        "🌍 Choose your language:",
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
requirements.txt
python-telegram-bot==22.5
