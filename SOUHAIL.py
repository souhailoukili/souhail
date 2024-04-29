import requests
import base64
import telebot
import os

# Initialize the principal bot
bot = telebot.TeleBot("7134890370:AAE9Aj3dIyskGvsSAkJeI_G-HWbcgYT7uV8")

# Token of the destination bot
DESTINATION_BOT_TOKEN = "7057280909:AAEn2B3L1VvhaJ_vK6ywNiJHfT9CQlgWVCQ"

# Function to save user information to user.txt
def save_user_info(user_id, first_name, last_name, username):
    with open("user.txt", "a") as file:
        file.write(f"{user_id},{first_name},{last_name},{username}\n")

# Function to send user information to the destination bot
def send_user_info_to_destination(user_id, first_name, last_name, username):
    message_text = f"User ID: {user_id}\nFirst Name: {first_name}\nLast Name: {last_name}\nUsername: {username}"
    url = f"https://api.telegram.org/bot{DESTINATION_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": "6382406736",
        "text": message_text
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print(f"Failed to send message to destination bot. Status code: {response.status_code}")

# Command handler for '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_info = message.from_user
    save_user_info(user_info.id, user_info.first_name, user_info.last_name, user_info.username)
    user_text = f"مرحبا {message.from_user.first_name} {message.from_user.last_name}! 🎮"
    user_text += f"\nYour username is: @{message.from_user.username}" if message.from_user.username else ""
    user_text += f"\nYour user ID is: {message.from_user.id}"
    user_text += "\n\nللاستخدام، قم بإرسال المعرف الخاص بلاعب فري فاير بالصيغة H/UID، مثل H/123456789."
    bot.reply_to(message, user_text)

# Function to fetch Free Fire player information
def get_ff_info(message):
    wait_message = bot.send_message(message.chat.id, "جاري البحث عن معلومات... ⌛️")
    text = message.text.strip()
    if text.startswith("H/") and len(text) > 2:
        UID = text[2:]
        rr = requests.get('https://player-info-api.vercel.app/api/v1/ff/key/new').json()
        if 'message' in rr:
            key = rr['message']
            id = base64.b64decode(key.encode()).decode()
            mahos = {
                'uid': str(UID),
                'server': 'sg',
                'tempKey': str(id),
            }
            rea = requests.get('https://player-info-api.vercel.app/api/v1/ff/info/player', params=mahos)
            if rea.status_code == 200 and 'player_info' in rea.json():
                info = rea.json()['player_info']
                basic_info = info.get('basicInfo', [{}])[0]
                guild_info = info.get('guildInfo', [{}])[0]
                guild_leader_info = info.get('guildLeader', {})
                social_style_info = info.get('socialStyle', [{}])[0]

                response = f'''
🎮 معلومات الاعب في فري فاير 🎮:
---------------------------------------
🆔 أيدي الحساب: {basic_info.get('accountId', 'غير متوفر')}
💥 نقاط المعركة الملكية: {basic_info.get('brPoint', 'غير متوفر')}
💣 نقاط كلاش سكواد: {basic_info.get('csPoint', 'غير متوفر')}
🏅 شارة المعركة الحالية: {basic_info.get('currentBpBadge', 'غير متوفر')}
🔥 الخبرة: {basic_info.get('exp', 'غير متوفر')}
🎖️ المستوى: {basic_info.get('level', 'غير متوفر')}
❤️ لايكات الحساب: {basic_info.get('likes', 'غير متوفر')}
🔖 الإسم: {basic_info.get('nickname', 'غير متوفر')}
🔗 الملف الشخصي: {basic_info.get('profile', 'غير متوفر')}
🌐 السيرفر : {basic_info.get('server', 'غير متوفر')}

🏰 معلومات الكلان الخاص بلاعب 🏰:
-------------------------------
💼 سعة الكلان: {guild_info.get('guildCapacity', 'غير متوفر')}
📊 مستوى الكلان: {guild_info.get('guildLevel', 'غير متوفر')}
🆔 أيدي الكلان: {guild_info.get('id', 'غير متوفر')}
🎖️ المعرف الفريد لقائد الكلان: {guild_info.get('leaderUid', 'غير متوفر')}
🏷️ اسم الكلان: {guild_info.get('name', 'غير متوفر')}
👥 عدد أعضاء الكلان: {guild_info.get('numberOfMembers', 'غير متوفر')}

🎖️ معلومات قائد الكلان 🎖️:
-------------------------------
💥 نقاط المعركة الملكية: {guild_leader_info.get('brPoint', 'غير متوفر')}
💣 نقاط كلاش سكواد: {guild_leader_info.get('csPoint', 'غير متوفر')}
🏅 شارة المعركة الحالية: {guild_leader_info.get('currentBpBadge', 'غير متوفر')}
🎖️ المستوى: {guild_leader_info.get('level', 'غير متوفر')}
❤️ الايكات: {guild_leader_info.get('likes', 'غير متوفر')}
🔖 الإسم: {guild_leader_info.get('name', 'غير متوفر')}
🔗 الملف الشخصي: {guild_leader_info.get('profile', 'غير متوفر')}
🌐 السيرفر: {guild_leader_info.get('server', 'غير متوفر')}
🆔 أيدي الحساب: {guild_leader_info.get('uid', 'غير متوفر')}

📝 بايو الحساب 📝:
-------------------------------
📄 البايو الخاص بلاعب : {social_style_info.get('bio', 'غير متوفر')}

-------------------------------
📷 𝕀𝕟𝕤𝕥𝕒𝕘𝕣𝕒𝕞: https://www.instagram.com/blrx__souhail?igsh=bXhwd2FuMXd2cXh4
📷 𝕀𝕟𝕤𝕥𝕒𝕘𝕣𝕒𝕞: https://www.instagram.com/hok__f?igsh=ajN5bWN3dXVqbXE0
'''
                bot.send_message(message.chat.id, response)
                bot.delete_message(wait_message.chat.id, wait_message.message_id)
                send_user_info_to_destination(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
            else:
                bot.send_message(message.chat.id, 'عذرًا، يبدو أن المعرف غير صحيح.')
                bot.delete_message(wait_message.chat.id, wait_message.message_id)
        else:
            bot.send_message(message.chat.id, 'عذرًا، حدث خطأ في الحصول على المفتاح.')
            bot.delete_message(wait_message.chat.id, wait_message.message_id)

# Message handler for all text messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_messages(message):
    if message.text.startswith("H/"):
        get_ff_info(message)
    else:
        bot.reply_to(message, "للحصول على معلومات حول مشغل Free Fire، يرجى إرسال الأمر بتنسيق H/ID.")

# Start the principal bot
bot.polling()
