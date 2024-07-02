import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Remplacez par votre clé API Telegram réelle
TELEGRAM_API_KEY = '7263112829:AAEEmqWJTFAuLhRsinRXtXoTbnktTG8CM-U'
bot = telebot.TeleBot(TELEGRAM_API_KEY)

# ID du chat de groupe où le bot est autorisé à répondre
ALLOWED_GROUP_CHAT_ID = -1002136444842 
ADMIN_CHAT_ID = 6631613512

user_language = {}
user_player_id = {}

def get_player_info(player_id):
    url = f'https://www.public.freefireinfo.site/api/info/sg/{player_id}?key=Ryz'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

messages = {
    'en': {
        'enter_id': "🆔 Please enter the player ID:",
        'choose_language': "🌐 Please choose your language:",
        'language_set': "🇬🇧 Language set to English.",
        'player_info': (
            "ℹ️ Account Information:\n"
            "- 📛 Name: {Account Name}\n"
            "- 🆔 UID: {Account UID}\n"
            "- 📈 Level: {Account Level}\n"
            "- 👍 Likes: {Account Likes}\n"
            "- 🌍 Region: {Account Region}\n"
            "- 📝 Bio: {Account Signature}\n"
            "- 🕰️ Last Login: {Account Last Login}\n"
            "- 🎟️ Booyah Pass: {Account Booyah Pass}\n"
            "- 🏅 Booyah Pass Badges: {Account Booyah Pass Badges}\n"
            "- 📅 Create Time: {Account Create Time}\n"
            "- 💯 Honor Score: {Account Honor Score}\n"
            "- 🌐 Language: {Account Language}\n"
            "🐾 Pet Info:\n"
            "- 📈 Pet Level: {Pet Level}\n"
            "- 🐾 Pet Name: {Pet Name}\n"
            "- 🐶 Pet Type: {Pet Type}\n"
            "- 🔝 Pet XP: {Pet XP}\n"
            "🛡️ Guild Info:\n"
            "- 🏰 Guild Capacity: {Guild Capacity}\n"
            "- 👥 Guild Members: {Guild Current Members}\n"
            "- 🆔 Guild ID: {Guild ID}\n"
            "- 📈 Guild Level: {Guild Level}\n"
            "- 📛 Guild Name: {Guild Name}\n"
            "- 🆔 Guild Leader ID: {Leader ID}\n"
            "- 🎖️ Guild Leader Title: {Leader Title}\n"
            "- 📍 Guild Leader Pin: {Leader Pin}\n"
            "- 🔝 Guild Leader XP: {Leader XP}\n"
        )
    },
    'ar': {
        'enter_id': "🆔 يرجى إدخال معرف اللاعب:",
        'choose_language': "🌐 يرجى اختيار لغتك:",
        'language_set': "🇸🇦 تم تعيين اللغة إلى العربية.",
        'player_info': (
            "ℹ️ معلومات الحساب:\n"
            "- 📛 الاسم: {Account Name}\n"
            "- 🆔 UID: {Account UID}\n"
            "- 📈 المستوى: {Account Level}\n"
            "- 👍 الإعجابات: {Account Likes}\n"
            "- 🌍 المنطقة: {Account Region}\n"
            "- 📝 السيرة الذاتية: {Account Signature}\n"
            "- 🕰️ آخر تسجيل دخول: {Account Last Login}\n"
            "- 🎟️ Booyah Pass: {Account Booyah Pass}\n"
            "- 🏅 شارات Booyah Pass: {Account Booyah Pass Badges}\n"
            "- 📅 وقت الإنشاء: {Account Create Time}\n"
            "- 💯 درجة الشرف: {Account Honor Score}\n"
            "- 🌐 اللغة: {Account Language}\n"
            "🐾 معلومات الحيوان الأليف:\n"
            "- 📈 مستوى الحيوان الأليف: {Pet Level}\n"
            "- 🐾 اسم الحيوان الأليف: {Pet Name}\n"
            "- 🐶 نوع الحيوان الأليف: {Pet Type}\n"
            "- 🔝 XP الحيوان الأليف: {Pet XP}\n"
            "🛡️ معلومات قائد النقابة:\n"
            "- 🏰 سعة النقابة: {Guild Capacity}\n"
            "- 👥 الأعضاء الحاليين للنقابة: {Guild Current Members}\n"
            "- 🆔 معرف النقابة: {Guild ID}\n"
            "- 📈 مستوى النقابة: {Guild Level}\n"
            "- 📛 اسم النقابة: {Guild Name}\n"
            "- 🆔 معرف قائد النقابة: {Leader ID}\n"
            "- 🎖️ لقب قائد النقابة: {Leader Title}\n"
            "- 📍 رمز قائد النقابة: {Leader Pin}\n"
            "- 🔝 XP قائد النقابة: {Leader XP}\n"
        )
    },
    'fr': {
        'enter_id': "🆔 Veuillez entrer l'ID du joueur:",
        'choose_language': "🌐 Veuillez choisir votre langue:",
        'language_set': "🇫🇷 La langue a été définie sur le français.",
        'player_info': (
            "ℹ️ Informations sur le compte :\n"
            "- 📛 Nom : {Account Name}\n"
            "- 🆔 UID : {Account UID}\n"
            "- 📈 Niveau : {Account Level}\n"
            "- 👍 Likes : {Account Likes}\n"
            "- 🌍 Région : {Account Region}\n"
            "- 📝 Bio : {Account Signature}\n"
            "- 🕰️ Dernière connexion : {Account Last Login}\n"
            "- 🎟️ Booyah Pass : {Account Booyah Pass}\n"
            "- 🏅 Badges Booyah Pass : {Account Booyah Pass Badges}\n"
            "- 📅 Date de création : {Account Create Time}\n"
            "- 💯 Score d'honneur : {Account Honor Score}\n"
            "- 🌐 Langue : {Account Language}\n"
            "🐾 Informations sur l'animal de compagnie :\n"
            "- 📈 Niveau de l'animal : {Pet Level}\n"
            "- 🐾 Nom de l'animal : {Pet Name}\n"
            "- 🐶 Type de l'animal : {Pet Type}\n"
            "- 🔝 XP de l'animal : {Pet XP}\n"
            "🛡️ Informations sur la guilde :\n"
            "- 🏰 Capacité de la guilde : {Guild Capacity}\n"
            "- 👥 Membres de la guilde : {Guild Current Members}\n"
            "- 🆔 ID de la guilde : {Guild ID}\n"
            "- 📈 Niveau de la guilde : {Guild Level}\n"
            "- 📛 Nom de la guilde : {Guild Name}\n"
            "- 🆔 ID du chef de guilde : {Leader ID}\n"
            "- 🎖️ Titre du chef de guilde : {Leader Title}\n"
            "- 📍 Insigne du chef de guilde : {Leader Pin}\n"
            "- 🔝 XP du chef de guilde : {Leader XP}\n"
        )
    }
}

def generate_player_info_message(player_info, lang):
    lang_messages = messages[lang]

    formatted_player_info = {k: player_info.get(k, 'N/A') for k in [
        'Account Name', 'Account UID', 'Account Level', 'Account Likes', 'Account Region',
        'Account Signature', 'Account Last Login', 'Account Booyah Pass', 'Account Booyah Pass Badges',
        'Account Create Time', 'Account Honor Score', 'Account Language',
    ]}

    formatted_pet_info = {k: player_info.get(k, 'N/A') for k in [
        'Pet Level', 'Pet Name', 'Pet Type', 'Pet XP',
    ]}

    formatted_guild_info = {k: player_info.get(k, 'N/A') for k in [
        'Guild Capacity', 'Guild Current Members', 'Guild ID', 'Guild Level',
        'Guild Name', 'Leader ID', 'Leader Title', 'Leader Pin', 'Leader XP',
    ]}

    return lang_messages['player_info'].format(**formatted_player_info, **formatted_pet_info, **formatted_guild_info)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id == ALLOWED_GROUP_CHAT_ID or message.chat.id == ADMIN_CHAT_ID:
        bot.reply_to(message, "👋 Welcome! Please send your player ID with the format 'SH [player_id]' to get started.")
    else:
        bot.reply_to(message, f"❌ This bot is only allowed to be used in the designated group. Join our group here: [HRIGA BOT](https://t.me/hriga_bot_v1)")

@bot.message_handler(func=lambda message: message.text and message.text.startswith('SH'))
def get_player_id(message):
    if message.chat.id == ALLOWED_GROUP_CHAT_ID or message.chat.id == ADMIN_CHAT_ID:
        try:
            player_id = message.text.split()[1]
            user_player_id[message.chat.id] = player_id
            
            markup = InlineKeyboardMarkup()
            markup.add(
                InlineKeyboardButton("English 🇬🇧", callback_data="language_en"),
                InlineKeyboardButton("العربية 🇸🇦", callback_data="language_ar"),
                InlineKeyboardButton("Français 🇫🇷", callback_data="language_fr")
            )
            
            bot.reply_to(message, messages['en']['choose_language'], reply_markup=markup)
        except IndexError:
            bot.reply_to(message, "⚠️ Please provide a valid player ID. Example: SH 123456789")
    else:
        bot.reply_to(message, f"❌ This bot is only allowed to be used in the designated group. Join our group here: [HRIGA BOT](https://t.me/hriga_bot_v1)")

@bot.callback_query_handler(func=lambda call: call.data.startswith("language_"))
def callback_language(call):
    if call.message.chat.id == ALLOWED_GROUP_CHAT_ID or call.message.chat.id == ADMIN_CHAT_ID:
        lang = call.data.split("_")[1]
        user_language[call.message.chat.id] = lang

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

        if lang == 'en':
            bot.send_message(call.message.chat.id, messages['en']['language_set'])
        elif lang == 'ar':
            bot.send_message(call.message.chat.id, messages['ar']['language_set'])
        elif lang == 'fr':
            bot.send_message(call.message.chat.id, messages['fr']['language_set'])

        player_id = user_player_id[call.message.chat.id]
        player_info = get_player_info(player_id)
        
        if player_info:
            player_info_message = generate_player_info_message(player_info, lang)
            bot.send_message(call.message.chat.id, player_info_message)
        else:
            bot.send_message(call.message.chat.id, "❌ Player information not found.")
    else:
        bot.send_message(call.message.chat.id, f"❌ This bot is only allowed to be used in the designated group. Join our group here: [HRIGA BOT](https://t.me/hriga_bot_v1)")

bot.polling()
