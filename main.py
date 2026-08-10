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
        "message": """**مرحبًا بك في بوت المعلومات الرسمي لـ 1XBET! 🌍**

1XBET هي منصة دولية للمراهنات والألعاب عبر الإنترنت، وتوفر الوصول إلى مجموعة واسعة من الأسواق الرياضية والفعاليات المباشرة وغيرها من الخدمات الترفيهية عبر منصاتها الرقمية.

توفر المنصة أسواقًا رياضية متنوعة تشمل العديد من الرياضات والمسابقات، مع اختلاف الخدمات ومدى توفرها حسب بلد المستخدم واللوائح المحلية المعمول بها.

تم تصميم هذا البوت لتوفير وصول سهل إلى موارد 1XBET الرسمية والمعلومات الخاصة بمنطقتك بلغتك المفضلة.

**متاح على مدار الساعة عبر هذا البوت:**

• روابط الوصول الرسمية إلى 1XBET لمنطقتك
• معلومات حول الخدمات والميزات المتاحة
• أدلة ومعلومات عامة مفيدة
• التحديثات والإعلانات
• معلومات وموارد خاصة بكل منطقة
• الوصول إلى القنوات والمواقع الرسمية لـ 1XBET

**موارد 1XBET الرسمية:**""",
        "button": "فتح الموقع 🇪🇬",
        "url": "https://example.com/ar",
    },


    "lang_en": {
        "name": "English 🇬🇧",
        "message": """**Welcome to the official 1XBET information bot! 🌍**

1XBET is an international online betting and gaming platform offering access to a wide range of sports markets, live events, and other entertainment products through its digital services.

The platform provides sports betting markets across numerous sports and competitions, with available services varying depending on the user's country and applicable local regulations.

This bot is designed to provide convenient access to official 1XBET resources and region-specific information in your preferred language.

**Available 24/7 through this bot:**

• Official 1XBET access links for your region
• Information about available services and features
• Useful guides and general platform information
• Updates and announcements
• Region-specific information and resources
• Access to official 1XBET channels and websites

**Official 1XBET resources:**""",
        "button": "Open Website 🇬🇧",
        "url": "https://example.com/en",
    },


    "lang_fr": {
        "name": "Français 🇫🇷",
        "message": """**Bienvenue sur le bot d'information officiel de 1XBET ! 🌍**

1XBET est une plateforme internationale de paris et de jeux en ligne proposant un large choix de marchés sportifs, d'événements en direct et d'autres services de divertissement via ses plateformes numériques.

La plateforme propose des marchés sportifs couvrant de nombreux sports et compétitions. Les services disponibles peuvent varier selon le pays de l'utilisateur et la réglementation locale applicable.

Ce bot a été conçu pour faciliter l'accès aux ressources officielles de 1XBET ainsi qu'aux informations spécifiques à votre région dans votre langue préférée.

**Disponible 24h/24 et 7j/7 via ce bot :**

• Liens officiels 1XBET disponibles dans votre région
• Informations sur les services et fonctionnalités disponibles
• Guides utiles et informations générales
• Actualités et annonces
• Informations et ressources spécifiques à chaque région
• Accès aux sites et canaux officiels de 1XBET

**Ressources officielles de 1XBET :**""",
        "button": "Ouvrir le site 🇫🇷",
        "url": "https://example.com/fr",
    },


    "lang_de": {
        "name": "Deutsch 🇩🇪",
        "message": """**Willkommen beim offiziellen 1XBET-Informationsbot! 🌍**

1XBET ist eine internationale Online-Plattform für Sportwetten und Gaming. Über ihre digitalen Dienste bietet sie Zugang zu zahlreichen Sportmärkten, Live-Events und weiteren Unterhaltungsangeboten.

Die Plattform bietet Sportwettenmärkte für zahlreiche Sportarten und Wettbewerbe. Die verfügbaren Dienste können je nach Land des Nutzers und den geltenden lokalen Vorschriften unterschiedlich sein.

Dieser Bot wurde entwickelt, um einen einfachen Zugang zu offiziellen 1XBET-Ressourcen und regionalen Informationen in Ihrer bevorzugten Sprache zu ermöglichen.

**Rund um die Uhr über diesen Bot verfügbar:**

• Offizielle 1XBET-Zugangslinks für Ihre Region
• Informationen zu verfügbaren Diensten und Funktionen
• Nützliche Anleitungen und allgemeine Informationen
• Aktualisierungen und Ankündigungen
• Regionale Informationen und Ressourcen
• Zugang zu offiziellen 1XBET-Websites und -Kanälen

**Offizielle 1XBET-Ressourcen:**""",
        "button": "Website öffnen 🇩🇪",
        "url": "https://example.com/de",
    },


    "lang_pt": {
        "name": "Português 🇵🇹",
        "message": """**Bem-vindo ao bot oficial de informações da 1XBET! 🌍**

A 1XBET é uma plataforma internacional de apostas e jogos online que oferece acesso a uma ampla variedade de mercados esportivos, eventos ao vivo e outros serviços de entretenimento através das suas plataformas digitais.

A plataforma disponibiliza mercados esportivos em diversas modalidades e competições. Os serviços disponíveis podem variar de acordo com o país do utilizador e a regulamentação local aplicável.

Este bot foi criado para facilitar o acesso aos recursos oficiais da 1XBET e às informações específicas da sua região no idioma da sua preferência.

**Disponível 24 horas por dia através deste bot:**

• Links oficiais da 1XBET para a sua região
• Informações sobre serviços e funcionalidades disponíveis
• Guias úteis e informações gerais
• Atualizações e anúncios
• Informações e recursos específicos de cada região
• Acesso aos sites e canais oficiais da 1XBET

**Recursos oficiais da 1XBET:**""",
        "button": "Abrir o site 🇵🇹",
        "url": "https://example.com/pt",
    },


    "lang_it": {
        "name": "Italiano 🇮🇹",
        "message": """**Benvenuto nel bot informativo ufficiale di 1XBET! 🌍**

1XBET è una piattaforma internazionale di scommesse e giochi online che offre accesso a un'ampia varietà di mercati sportivi, eventi dal vivo e altri servizi di intrattenimento attraverso le sue piattaforme digitali.

La piattaforma offre mercati sportivi relativi a numerosi sport e competizioni. I servizi disponibili possono variare in base al Paese dell'utente e alle normative locali applicabili.

Questo bot è stato progettato per facilitare l'accesso alle risorse ufficiali di 1XBET e alle informazioni specifiche della propria regione nella lingua preferita.

**Disponibile 24 ore su 24 tramite questo bot:**

• Link ufficiali 1XBET disponibili nella tua regione
• Informazioni sui servizi e sulle funzionalità disponibili
• Guide utili e informazioni generali
• Aggiornamenti e comunicazioni
• Informazioni e risorse specifiche per regione
• Accesso ai siti e ai canali ufficiali di 1XBET

**Risorse ufficiali di 1XBET:**""",
        "button": "Apri il sito 🇮🇹",
        "url": "https://example.com/it",
    },


    "lang_tr": {
        "name": "Türkçe 🇹🇷",
        "message": """**Resmi 1XBET bilgi botuna hoş geldiniz! 🌍**

1XBET, dijital hizmetleri üzerinden çok çeşitli spor bahisleri, canlı etkinlikler ve diğer eğlence hizmetlerine erişim sunan uluslararası bir çevrim içi bahis ve oyun platformudur.

Platform, birçok spor dalı ve müsabaka için çeşitli spor bahis piyasaları sunmaktadır. Kullanılabilir hizmetler, kullanıcının bulunduğu ülkeye ve geçerli yerel düzenlemelere göre değişiklik gösterebilir.

Bu bot, resmi 1XBET kaynaklarına ve bölgenize özel bilgilere tercih ettiğiniz dilde kolay erişim sağlamak amacıyla tasarlanmıştır.

**Bu bot üzerinden 7/24 erişilebilir:**

• Bölgeniz için resmi 1XBET erişim bağlantıları
• Mevcut hizmetler ve özellikler hakkında bilgiler
• Yararlı rehberler ve genel platform bilgileri
• Güncellemeler ve duyurular
• Bölgeye özel bilgiler ve kaynaklar
• Resmi 1XBET web sitelerine ve kanallarına erişim

**Resmi 1XBET kaynakları:**""",
        "button": "Web sitesini aç 🇹🇷",
        "url": "https://example.com/tr",
    },


    "lang_fa": {
        "name": "فارسی 🇮🇷",
        "message": """**به ربات اطلاعات رسمی 1XBET خوش آمدید! 🌍**

1XBET یک پلتفرم بین‌المللی شرط‌بندی و بازی آنلاین است که از طریق خدمات دیجیتال خود دسترسی به طیف گسترده‌ای از بازارهای ورزشی، رویدادهای زنده و سایر خدمات سرگرمی را ارائه می‌دهد.

این پلتفرم بازارهای ورزشی مختلفی را برای ورزش‌ها و مسابقات متعدد ارائه می‌کند. خدمات قابل دسترس ممکن است بسته به کشور کاربر و مقررات محلی مربوطه متفاوت باشد.

این ربات برای فراهم کردن دسترسی آسان به منابع رسمی 1XBET و اطلاعات مربوط به منطقه شما به زبان موردنظر شما طراحی شده است.

**به صورت ۲۴ ساعته از طریق این ربات در دسترس است:**

• لینک‌های رسمی دسترسی به 1XBET برای منطقه شما
• اطلاعات مربوط به خدمات و امکانات موجود
• راهنماها و اطلاعات عمومی مفید
• به‌روزرسانی‌ها و اطلاعیه‌ها
• اطلاعات و منابع ویژه هر منطقه
• دسترسی به وب‌سایت‌ها و کانال‌های رسمی 1XBET

**منابع رسمی 1XBET:**""",
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
