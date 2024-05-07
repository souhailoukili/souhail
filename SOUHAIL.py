import telebot
from telebot import types
import requests
import datetime

TOKEN = "6713438442:AAEB4tiquU_M0LGtNiA-ikAIQZ9RYDBgXgg"
DEVELOPER_ID = "6631613512"
USER_FILE = "users.txt"
SECOND_BOT_TOKEN = "6901062644:AAEbWucUfzcjnWoCHgjBAr-35ojHv8ryBGk"

bot = telebot.TeleBot(TOKEN)
second_bot = telebot.TeleBot(SECOND_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
        bot.reply_to(message, "مرحبًا بك مطور الروبوت 👋")
        save_user_info(message.from_user)
    elif message.chat.type == 'group' or message.chat.type == 'supergroup':
        bot.reply_to(message, "مرحبًا بك في مجموعة الروبوت 👋\nللحصول على معلومات حول اللاعب ++\n قم بكتابة ++تعرفة اللاعب")
    else:
        pass

def save_user_info(user):
    with open(USER_FILE, 'a', encoding='utf-8') as f:
        f.write(f"معرف المستخدم: {user.id}, اسم المستخدم: {user.username}, الاسم الأول: {user.first_name}, الاسم الأخير: {user.last_name}\n")

@second_bot.message_handler(commands=['show_users'])
def show_users(message):
    if str(message.from_user.id) == DEVELOPER_ID:
        with open(USER_FILE, 'r', encoding='utf-8') as f:
            users_info = f.read()
        second_bot.reply_to(message, "قائمة المستخدمين:\n" + users_info)
    else:
        second_bot.reply_to(message, "لا تمتلك صلاحيات للوصول إلى هذا الأمر.")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        get_player_info(message)
    elif message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
        get_player_info(message)

def get_player_info(message):
    if '++' in message.text:
        if message.chat.type == 'group' or message.chat.type == 'supergroup':
            sent = bot.send_message(message.chat.id, "يرجى الانتظار بينما أبحث عن المعلومات...⏳")
        elif message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
            bot.reply_to(message, "يرجى الانتظار بينما أبحث عن المعلومات...⏳")
        player_id = message.text.split('++')[1]
        id = player_id
        region = "me"

        url = 'https://freefireapi.com.br/api/search_id?id={}&region={}'.format(player_id, region)
        response = requests.get(url)
        if response.status_code == 200:
            player_data = response.json()
            basic_info = player_data.get('basicInfo', {})
            profile_info = player_data.get('profileInfo', {})
            history_ep_info = player_data.get('historyEpInfo', [])
            clan_basic_info = player_data.get('clanBasicInfo', {})
            captain_basic_info = player_data.get('captainBasicInfo', {})
            social_info = player_data.get('socialInfo', {})

            # Extracting additional player information
            name = basic_info.get('nickname', 'الاسم غير متوفر')
            level = basic_info.get('level', 'المستوى غير متوفر')
            player_id = basic_info.get('accountId', 'معرف اللاعب غير متوفر')
            exp = basic_info.get('exp', 'الخبرة غير متوفرة')
            liked = basic_info.get('liked', 'الإعجابات غير متوفرة')
            last_login = datetime.datetime.utcfromtimestamp(int(basic_info.get('lastLoginAt', 0)))
            creation_date = datetime.datetime.utcfromtimestamp(int(basic_info.get('createAt', 0)))
            rank_token = basic_info.get('rankingPoints', 'نقاط التصنيف غير متوفرة')
            rank_number = basic_info.get('rank', 'رقم التصنيف غير متوفر')
            language = social_info.get('language', 'اللغة غير متوفرة')
            bio = social_info.get('signature', 'السيرة الذاتية غير متوفرة')
            guild_id = clan_basic_info.get('clanId', 'معرف النقابة غير متوفر')
            admin_id = captain_basic_info.get('accountId', 'معرف الإداري غير متوفر')
            admin_name = captain_basic_info.get('nickname', 'اسم الإداري غير متوفر')
            clan_level = clan_basic_info.get('clanLevel', 'مستوى النقابة غير متوفر')
            clan_capacity = clan_basic_info.get('capacity', 'سعة النقابة غير متوفرة')
            clan_max_capacity = clan_basic_info.get('memberNum', 'الحد الأقصى لسعة النقابة غير متوفر')

            # Constructing the message with styling
            Answer_message = f"➪ اسم اللاعب: {name} 😊\n➪ المستوى: {level} ⭐️\n➪ معرف اللاعب: #{player_id} 🔍\n➪ الخبرة: {exp} 📊\n➪ الإعجابات: {liked} ❤️\n➪ آخر تسجيل دخول: {last_login} 🕒\n➪ تاريخ الإنشاء: {creation_date} 📅\n➪ نقاط التصنيف: {rank_token} 🏅\n➪ رقم التصنيف: {rank_number} #️⃣\n➪ اللغة: {language} 🌐\n➪ السيرة الذاتية: {bio} ℹ️\n=========================\n\n➪ معرف النقابة: {guild_id} 🛡️\n➪ معرف الإداري: {admin_id} 👮\n➪ اسم الإداري: {admin_name} 👤\n➪ مستوى النقابة: {clan_level} 🏰\n➪ سعة النقابة: {clan_capacity} 🧩\n➪ الحد الأقصى لسعة النقابة: {clan_max_capacity} 🧩\n\n تطوير الروبوت\n @lion_souhail\n @MRX3SKR🤖"

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="—͟͞͞  ＬＩＯＮ👀", url="https://www.instagram.com/blrx__souhail?igsh=bXhwd2FuMXd2cXh4")
            keyboard.add(url_button)

            if message.chat.type == 'group' or message.chat.type == 'supergroup':
                bot.delete_message(message.chat.id, sent.message_id)  # Supprimer le message de chargement précédent
                bot.send_message(message.chat.id, Answer_message, reply_markup=keyboard)
                # Envoyer les informations de l'utilisateur au deuxième robot
                send_user_info_to_second_bot(Answer_message)
        else:
            if message.chat.type == 'group' or message.chat.type == 'supergroup':
                bot.delete_message(message.chat.id, sent.message_id)  # Supprimer le message de chargement précédent
                bot.reply_to(message, "حدث خطأ أثناء جلب معلومات اللاعب. يرجى المحاولة مرة أخرى في وقت لاحق.")
            elif message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
                bot.reply_to(message, "حدث خطأ أثناء جلب معلومات اللاعب. يرجى المحاولة مرة أخرى في وقت لاحق.")

def send_user_info_to_second_bot(info):
    second_bot.send_message(DEVELOPER_ID, info)

try:
    bot.polling()
except Exception as e:
    print(f"حدث خطأ: {str(e)}")

try:
    second_bot.polling()
except Exception as e:
    print(f"حدث خطأ: {str(e)}")
