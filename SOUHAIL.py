import telebot
import requests
import datetime
from telebot import types

TOKEN = "6713438442:AAEB4tiquU_M0LGtNiA-ikAIQZ9RYDBgXgg"
DEVELOPER_CHAT_ID = "6631613512,1480248962"
GROUP_CHAT_ID = "-1002136444842"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if str(message.chat.id) in [GROUP_CHAT_ID, DEVELOPER_CHAT_ID]:
        bot.send_message(message.chat.id, "𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐮𝐞 𝐝𝐚𝐧𝐬 𝐥𝐞 𝐠𝐫𝐨𝐮𝐩𝐞 𝐝𝐞 𝐫𝐨𝐛𝐨𝐭𝐬 👋\n𝐏𝐨𝐮𝐫 𝐨𝐛𝐭𝐞𝐧𝐢𝐫 𝐝𝐞𝐬 𝐢𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧𝐬 𝐬𝐮𝐫 𝐥𝐞 𝐣𝐨𝐮𝐞𝐮𝐫 ++𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖\n 𝐜𝐡𝐨𝐮𝐡𝐫𝐚\n𝐒𝐇 𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖 𝐬𝐠 𝟏𝟎𝟎 ")
    else:
        activate_user(message)

@bot.message_handler(func=lambda message: '++' in message.text)
def get_player_info(message):
    if str(message.chat.id) in [GROUP_CHAT_ID, DEVELOPER_CHAT_ID]:
        if str(message.chat.id) == GROUP_CHAT_ID:
            if str(message.from_user.id) != DEVELOPER_CHAT_ID:
                bot.reply_to(message, "Ce bot est destiné à être utilisé uniquement par le développeur dans un groupe spécifique.")
                return
        player_id = message.text.split('++')[1]
        region = "me"
        msg = bot.reply_to(message, "𝙍𝙚𝙘𝙝𝙚𝙧𝙘𝙝𝙚 𝙙𝙪 𝙟𝙤𝙪𝙚𝙪𝙧...⏳")
        url = 'https://freefireapi.com.br/api/search_id?id={}&region={}'.format(player_id, region)
        response = requests.get(url)
        if response.status_code == 200:
            player_data = response.json()
            info_message = format_player_info(player_data)
            send_message_with_keyboard(message, info_message)
            bot.delete_message(message.chat.id, msg.message_id)  # Supprime le message en attente
        else:
            bot.reply_to(message, "Une erreur s'est produite lors de la récupération des informations du joueur. Veuillez réessayer ultérieurement.")
    else:
        bot.reply_to(message, "Ce bot est destiné à être utilisé uniquement dans un groupe spécifique.")

def format_player_info(player_data):
    basic_info = player_data.get('basicInfo', {})
    clan_basic_info = player_data.get('clanBasicInfo', {})
    captain_basic_info = player_data.get('captainBasicInfo', {})
    social_info = player_data.get('socialInfo', {})
    pet_info = player_data.get('petInfo', {})

    last_login_date = datetime.datetime.utcfromtimestamp(int(basic_info.get('lastLoginAt', 0)))
    creation_date = datetime.datetime.utcfromtimestamp(int(basic_info.get('createAt', 0)))

    pet_equipped = "نعم" if pet_info.get('equipped', False) else "لا"
    pet_name = pet_info.get('petName', 'لا يوجد')
    pet_type = pet_info.get('petType', 'لا يوجد')
    pet_experience = pet_info.get('petExp', 'لا يوجد')
    pet_level = pet_info.get('petLevel', 'لا يوجد')

    info_message =f"⇯⇢⇢⇢🌐 معلومات اللاعب 🌐⇠⇠⇠⇯\n\n" \
                   f"♠ رقم اللاعب ➩ {basic_info.get('accountId', 'لا يوجد')}\n" \
                   f"♠ الاسم ➩ {basic_info.get('nickname', 'لا يوجد')}\n" \
                   f"♠ المستوى ➩ {basic_info.get('level', 'لا يوجد')}\n" \
                   f"♠ الخبرة ➩ {basic_info.get('exp', 'لا يوجد')}\n" \
                   f"♠ عدد الإعجابات ➩ {basic_info.get('liked', 'لا يوجد')}\n" \
                   f"♠ البنر ID ➩ {basic_info.get('bannerId', 'لا يوجد')}\n" \
                   f"♠ الصورة الرمزية ➩ {basic_info.get('headPic', 'لا يوجد')}\n" \
                   f"♠ الرتبة ➩ {basic_info.get('rank', 'لا يوجد')}\n" \
                   f"♠ نقاط التصنيف ➩ {basic_info.get('rankingPoints', 'لا يوجد')}\n" \
                   f"♠ يملك باس النخبة ➩ {basic_info.get('hasElitePass', 'لا يوجد')}\n" \
                   f"♠ عدد الشارات ➩ {basic_info.get('badgeCnt', 'لا يوجد')}\n" \
                   f"♠ هوية الشارة ➩ {basic_info.get('badgeId', 'لا يوجد')}\n" \
                   f"♠ موسم ➩ {basic_info.get('seasonId', 'لا يوجد')}\n" \
                   f"♠ تظهر الرتبة ➩ {basic_info.get('showRank', 'لا يوجد')}\n" \
                   f"♠ آخر تسجيل دخول ➩ {last_login_date.strftime('%Y-%m-%d %H:%M:%S')}\n" \
                   f"♠ تم الإنشاء في ➩ {creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n\n" \
                   f"⇯⇢⇢⇢🏛️ معلومات النقابة 🏛️⇠⇠⇠⇯\n\n" \
                   f"♠ رقم النقابة ➩ {clan_basic_info.get('clanId', 'لا يوجد')}\n" \
                   f"♠ رقم القائد ➩ {clan_basic_info.get('captainId', 'لا يوجد')}\n" \
                   f"♠ مستوى النقابة ➩ {clan_basic_info.get('clanLevel', 'لا يوجد')}\n" \
                   f"♠ السعة ➩ {clan_basic_info.get('capacity', 'لا يوجد')}\n" \
                   f"♠ عدد الأعضاء ➩ {clan_basic_info.get('memberNum', 'لا يوجد')}\n\n" \
                   f"⇯⇢⇢⇢🎖️ معلومات القائد 🎖️⇠⇠⇠⇯\n\n" \
                   f"♠ رقم اللاعب ➩ {captain_basic_info.get('accountId', 'لا يوجد')}\n" \
                   f"♠ الاسم ➩ {captain_basic_info.get('nickname', 'لا يوجد')}\n" \
                   f"♠ المستوى ➩ {captain_basic_info.get('level', 'لا يوجد')}\n" \
                   f"♠ الخبرة ➩ {captain_basic_info.get('exp', 'لا يوجد')}\n" \
                   f"♠ الرتبة ➩ {captain_basic_info.get('rank', 'لا يوجد')}\n" \
                   f"♠ نقاط التصنيف ➩ {captain_basic_info.get('rankingPoints', 'لا يوجد')}\n" \
                   f"♠ يملك باس النخبة ➩ {captain_basic_info.get('hasElitePass', 'لا يوجد')}\n" \
                   f"♠ عدد الشارات ➩ {captain_basic_info.get('badgeCnt', 'لا يوجد')}\n" \
                   f"♠ هوية الشارة ➩ {captain_basic_info.get('badgeId', 'لا يوجد')}\n" \
                   f"♠ موسم ➩ {captain_basic_info.get('seasonId', 'لا يوجد')}\n" \
                   f"♠ عدد الإعجابات ➩ {captain_basic_info.get('liked', 'لا يوجد')}\n" \
                   f"♠ آخر تسجيل دخول ➩ {last_login_date.strftime('%Y-%m-%d %H:%M:%S')}\n\n" \
                   f"⇯⇢⇢⇢📊 معلومات اجتماعية 📊⇠⇠⇠⇯\n\n" \
                   f"♠ لغة ➩ {social_info.get('language', 'لا يوجد')}\n" \
                   f"♠ التوقيع ➩ {social_info.get('signature', 'لا يوجد')}\n\n"\
                   f"💻 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧:\n@lion_souhail☠\n@MRX3SKR☠"
    return info_message

def send_message_with_keyboard(message, text):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton(text="𝐕𝐨𝐢𝐫 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 ❤️", url="https://www.instagram.com/blrx__souhail?igsh=bXhwd2FuMXd2cXh4")
    keyboard.add(url_button)
    bot.reply_to(message, text, reply_markup=keyboard)

def activate_user(message):
    user_id = str(message.from_user.id)

try:
    bot.polling()
except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")
