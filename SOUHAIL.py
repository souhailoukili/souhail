import telebot
from telebot import types
import requests
import datetime

TOKEN = "6713438442:AAEB4tiquU_M0LGtNiA-ikAIQZ9RYDBgXgg"
DEVELOPER_ID = "6927323442"
USER_FILE = "users.txt"
SECOND_BOT_TOKEN = "6901062644:AAEbWucUfzcjnWoCHgjBAr-35ojHv8ryBGk"

bot = telebot.TeleBot(TOKEN)
second_bot = telebot.TeleBot(SECOND_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
        bot.reply_to(message, "𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 👋")
        save_user_info(message.from_user)
    elif message.chat.type == 'group' or message.chat.type == 'supergroup':
        bot.reply_to(message, "𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗚𝗥𝗢𝗨𝗣 𝗠𝗘𝗠𝗕𝗘𝗥 👋\n𝗙𝗢𝗥 𝗚𝗘𝗧 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗔𝗕𝗢𝗨𝗧 𝗜𝗗 ℹ 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 ++")
    else:
        pass

def save_user_info(user):
    with open(USER_FILE, 'a') as f:
        f.write(f"User ID: {user.id}, Username: {user.username}, First Name: {user.first_name}, Last Name: {user.last_name}\n")

@second_bot.message_handler(commands=['show_users'])
def show_users(message):
    if str(message.from_user.id) == DEVELOPER_ID:
        with open(USER_FILE, 'r') as f:
            users_info = f.read()
        second_bot.reply_to(message, "List of Users:\n" + users_info)
    else:
        second_bot.reply_to(message, "You are not authorized to access this command.")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        get_player_info(message)
    elif message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
        get_player_info(message)

def get_player_info(message):
    if '++' in message.text:
        if message.chat.type == 'group' or message.chat.type == 'supergroup':
            sent = bot.send_message(message.chat.id, "𝙍𝙚𝙘𝙝𝙚𝙧𝙘𝙝𝙚 𝙙𝙪 𝙟𝙤𝙪𝙚𝙪𝙧...⏳")
        elif message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
            bot.reply_to(message, "𝙍𝙚𝙘𝙝𝙚𝙧𝙘𝙝𝙚 𝙙𝙪 𝙟𝙤𝙪𝙚𝙪𝙧...⏳")
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

            name = basic_info.get('nickname', 'Nom introuvable')
            level = basic_info.get('level', 'Niveau introuvable')
            player_id = basic_info.get('accountId', 'ID joueur introuvable')
            exp = basic_info.get('exp', 'Expérience introuvable')
            liked = basic_info.get('liked', 'Likes introuvables')
            last_login = datetime.datetime.utcfromtimestamp(int(basic_info.get('lastLoginAt', 0)))
            creation_date = datetime.datetime.utcfromtimestamp(int(basic_info.get('createAt', 0)))
            rank_token = basic_info.get('rankingPoints', 'Token de classement introuvable')
            rank_number = basic_info.get('rank', 'Numéro de classement introuvable')
            language = social_info.get('language', 'Langue introuvable')
            bio = social_info.get('signature', 'Biographie introuvable')
            guild_id = clan_basic_info.get('clanId', 'ID de guilde introuvable')
            admin_id = captain_basic_info.get('accountId', 'ID administrateur introuvable')
            admin_name = captain_basic_info.get('nickname', 'Nom administrateur introuvable')
            clan_level = clan_basic_info.get('clanLevel', 'Niveau de guilde introuvable')
            clan_capacity = clan_basic_info.get('capacity', 'Capacité de guilde introuvable')
            clan_max_capacity = clan_basic_info.get('memberNum', 'Capacité maximale de guilde introuvable')

            Answer_message = f"Nom du joueur: {name} 😊\nNiveau du joueur: {level} ⭐️\nID du joueur: #{player_id} 🔍\nExpérience: {exp} 📊\nLikes: {liked} ❤️\nDernière connexion: {last_login} 🕒\nDate de création: {creation_date} 📅\nToken de classement: {rank_token} 🏅\nNuméro de classement: {rank_number} #️⃣\nLangue: {language} 🌐\nBiographie: {bio} ℹ️\nID de guilde: {guild_id} 🛡️\nID administrateur: {admin_id} 👮\nNom administrateur: {admin_name} 👤\nNiveau de guilde : {clan_level} 🏰\nCapacité de guilde: {clan_capacity} 🧩\nCapacité maximale de guilde: {clan_max_capacity} 🧩\n\n Développeur du bot \n @lion_souhail🤖"

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_button = types.InlineKeyboardButton(text="—͟͞͞  ＬＩＯＮ👀", url="https://www.instagram.com/blrx__souhail?igsh=bXhwd2FuMXd2cXh4")
            keyboard.add(url_button)

            if message.chat.type == 'group' or message.chat.type == 'supergroup':
                bot.delete_message(message.chat.id, sent.message_id)  # Supprimer le message de chargement précédent
                bot.send_message(message.chat.id, Answer_message, reply_markup=keyboard)
                # Send user info to the second bot
                send_user_info_to_second_bot(Answer_message)
        else:
            if message.chat.type == 'group' or message.chat.type == 'supergroup':
                bot.delete_message(message.chat.id, sent.message_id)  # Supprimer le message de chargement précédent
                bot.reply_to(message, "Une erreur s'est produite lors de la recherche des informations du joueur. Veuillez réessayer plus tard.")
            elif message.chat.type == 'private' and str(message.from_user.id) == DEVELOPER_ID:
                bot.reply_to(message, "Une erreur s'est produite lors de la recherche des informations du joueur. Veuillez réessayer plus tard.")

def send_user_info_to_second_bot(info):
    second_bot.send_message(DEVELOPER_ID, info)

try:
    bot.polling()
except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")

try:
    second_bot.polling()
except Exception as e:
    print(f"An error occurred: {str(e)}")
