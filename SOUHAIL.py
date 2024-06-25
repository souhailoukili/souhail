import requests
import telebot
from telebot import types
from datetime import datetime
import  urllib.parse

# استبدل بالتوكن الفعلي الخاص بك
TOKEN = "7263112829:AAEEmqWJTFAuLhRsinRXtXoTbnktTG8CM-U"
bot = telebot.TeleBot(TOKEN)

# قائمة معرفات المجموعات
GROUP_CHAT_IDS = [-1002136444842]  # أضف معرفات المجموعات الأخرى هنا
password = '0529aizen003fshy'

def get_player_info(uid):
    server = 'sg'
    url = f"https://ff.samsedrain.com.np/playerinfo?uid={uid}&password={password}&server={server}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'message' in data and isinstance(data['message'], dict) and data['message']:
            return data['message']
        else:
            return None
    except requests.RequestException as e:
        print(f"Failed to fetch data: {e}")
        return None

def get_map_info(map_code, password, server):
    url = f"https://ff.samsedrain.com.np/mapinfo?password={password}&server={server}&map={map_code}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def profile_url(avatar, banner, uid, name, level):
    return f"https://ff.samsedrain.com.np/profile?avatar={avatar}&banner={banner}&uid={uid}&name={name}&level={level}&password={password}"
def outfits_url(outfits):
    string_to_encode = outfits
    encoded_string = urllib.parse.quote(string_to_encode)


    return f"https://ff.samsedrain.com.np/outfits?outfits={encoded_string}&password={password}&ok=3"

def format_player_info(player_info, lang='ar'):
    basic_info = player_info.get('basicInfo', {})
    profile_info = player_info.get('profileInfo', {})
    captain_info = player_info.get('captainBasicInfo', {})
    clan_info = player_info.get('clanBasicInfo', {})
    social_info = player_info.get('socialInfo', {})

    last_login = datetime.fromtimestamp(int(basic_info.get('lastLoginAt', 0))).strftime('%Y-%m-%d %H:%M:%S')
    created_at = datetime.fromtimestamp(int(basic_info.get('createAt', 0))).strftime('%Y-%m-%d %H:%M:%S')

    if lang == 'ar':
        formatted_info = (
            f"📋 تـاريخ الحـساب [×]\n"
            f"├─آخر تسجيل دخول   : {last_login}\n"
            f"└─تم الإنشاء في   : {created_at}\n\n"
            f"👤 مـعـلومات الـحسـاب\n"
            f"├─ معرف الحساب : {basic_info.get('accountId')}\n"
            f"├─ اللقب : {basic_info.get('nickname')}\n"
            f"├─ المستوى : {basic_info.get('level')}\n"
            f"├─ الإعجابات : {basic_info.get('liked')}\n"
            f"├─ الخبرة : {basic_info.get('exp')}\n"
            f"├─ الصورة الرمزية: {basic_info.get('headPic')}\n"
            f"├─ البانر : {basic_info.get('bannerId')}\n"
            f"├─ الرتبة : {basic_info.get('rank')}\n"
            f"├─ نقاط الترتيب : {basic_info.get('rankingPoints')}\n"
            f"├─ عدد الشارات: {basic_info.get('badgeCnt')}\n"
            f"├─ بطاقة Booyah: {basic_info.get('booyahPass')}\n"
            f"├─ رتبة CS: {basic_info.get('csRank')}\n"
            f"├─ نقاط تصنيف CS: {basic_info.get('csRankingPoints')}\n"
            f"└─ السيرة الذاتية : {social_info.get('signature')}\n\n"
            f"🛡 مـعـلومات الـرابـطه\n"
            f"├─ معرف العشيرة : {clan_info.get('clanId')}\n"
            f"├─ اللقب : {clan_info.get('clanName')}\n"
            f"├─ المستوى ➩ {clan_info.get('clanLevel')}\n"
            f"├─ السعة: {clan_info.get('capacity')}\n"
            f"├─ رقم العضو : {clan_info.get('memberNum')}\n"
            f"├─ معرف الكابتن: {clan_info.get('captainId')}\n"
            f"└─ اسم الكابتن : {captain_info.get('nickname')}\n\n"
            f"♻️ مـعـلومات قائـد الرابــطـه\n"
            f"├─ اللقب : {captain_info.get('nickname')}\n"
            f"├─ المستوى : {captain_info.get('level')}\n"
            f"├─ الخبرة : {captain_info.get('exp')}\n"
            f"├─ المرتبة : {captain_info.get('rank')}\n"
            f"├─ نقاط الترتيب : {captain_info.get('rankingPoints')}\n"
            f"├─ عدد الشارات: {captain_info.get('badgeCnt')}\n"
            f"├─ إعجاب : {captain_info.get('liked')}\n"
            f"├─ رتبة CS: {captain_info.get('csRank')}\n"
            f"├─ نقاط تصنيف CS: {captain_info.get('csRankingPoints')}\n"
            f"├─ آخر تسجيل دخول كان على: {last_login}\n"
            f"└─ تم الإنشاء في : {created_at}\n\n"
            
        )
    else:
        formatted_info = (
            f"📋 Account history [×]\n"
            f"├─ Last Login   : {last_login}\n"
            f"└─ Created At   : {created_at}\n\n"
            f"👤 Account information\n"
            f"├─ Account ID : {basic_info.get('accountId')}\n"
            f"├─ Nickname : {basic_info.get('nickname')}\n"
            f"├─ Level : {basic_info.get('level')}\n"
            f"├─ Likes : {basic_info.get('liked')}\n"
            f"├─ Experience : {basic_info.get('exp')}\n"
            f"├─ Avatar : {basic_info.get('headPic')}\n"
            f"├─ Banner : {basic_info.get('bannerId')}\n"
            f"├─ Rank : {basic_info.get('rank')}\n"
            f"├─ Ranking Points : {basic_info.get('rankingPoints')}\n"
            f"├─ Badge Count: {basic_info.get('badgeCnt')}\n"
            f"├─ Booyah Pass: {basic_info.get('booyahPass')}\n"
            f"├─ CS Rank : {basic_info.get('csRank')}\n"
            f"├─ CS Ranking Points : {basic_info.get('csRankingPoints')}\n"
            f"└─ Bio : {social_info.get('signature')}\n\n"
            f"🛡 Guild information\n"
            f"├─ Clan ID : {clan_info.get('clanId')}\n"
            f"├─ Clan Name : {clan_info.get('clanName')}\n"
            f"├─ Clan Level : {clan_info.get('clanLevel')}\n"
            f"├─ Capacity : {clan_info.get('capacity')}\n"
            f"├─ Member Number : {clan_info.get('memberNum')}\n"
            f"├─ Captain ID : {clan_info.get('captainId')}\n"
            f"└─ Captain Name : {captain_info.get('nickname')}\n\n"
            f"♻️ Guild leader information\n"
            f"├─ Nickname : {captain_info.get('nickname')}\n"
            f"├─ Level : {captain_info.get('level')}\n"
            f"├─ Experience : {captain_info.get('exp')}\n"
            f"├─ Rank : {captain_info.get('rank')}\n"
            f"├─ Ranking Points : {captain_info.get('rankingPoints')}\n"
            f"├─ Badge Count : {captain_info.get('badgeCnt')}\n"
            f"├─ Liked : {captain_info.get('liked')}\n"
            f"├─ CS Rank : {captain_info.get('csRank')}\n"
            f"├─ CS Ranking Points : {captain_info.get('csRankingPoints')}\n"
            f"├─ Last Login : {last_login}\n"
            f"└─ Created At : {created_at}\n\n"
            
        )

    profile = profile_url(basic_info.get('headPic',900000013),basic_info.get('bannerId',900000014),basic_info.get('accountId'),basic_info.get('nickname'),basic_info.get('level'))

    outfits = outfits_url(profile_info.get('equipedSkills'))

    return [formatted_info, profile,outfits]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.chat.id in GROUP_CHAT_IDS:
        bot.reply_to(message, "أرسل /Get <UID> لجلب معلومات الحساب.\n"
                              "أرسل /BH <رقم الحساب> للتحقق من حالة البند.\n"
                              "أرسل /stats لعرض إحصائيات استخدام البوت.\n"
                              "أرسل /BW <رقم الحساب> لجلب قائمة الأمنيات.\n"
                              "أرسل /i <رقم العنصر> لإضافة عنصر إلى قائمة الأمنيات.")
    else:
        bot.reply_to(message, "مرحبًا! أرسل لي رسالة تحتوي على '#' للحصول على معلومات الخريطة.")
@bot.message_handler(commands=['Get'])
def handle_info(message):
    if message.chat.id in GROUP_CHAT_IDS:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "يرجى إدخال UID صحيح.")
        else:
            uid = parts[1].strip()
            if not uid.isdigit():
                bot.reply_to(message, "هذا الايدي غير صالح.")
            else:
                markup = types.InlineKeyboardMarkup()
                arabic_button = types.InlineKeyboardButton("🇸🇦 اللغة العربية", callback_data=f'info_ar_{uid}')
                english_button = types.InlineKeyboardButton("🇬🇧 English", callback_data=f'info_en_{uid}')
                markup.add(arabic_button, english_button)
                bot.reply_to(message, "اختر اللغة:", reply_markup=markup)

@bot.message_handler(func=lambda message: "#" in message.text.strip())
def map_info(message):
    map_code = message.text.strip().split("#", 1)[-1]
    password = "0529aizen003fshy"
    server = "sg"
    map_info_data = get_map_info(map_code, password, server)
    if map_info_data:
        if "message" in map_info_data and "mapInfo" in map_info_data["message"]:
            map_info = map_info_data["message"]["mapInfo"]
            map_name = map_info.get("name", "")
            owner_name = map_info.get("ownerName", "")
            owner_uid = map_info.get("ownerUid", "")
            likes = map_info.get("likes", "")
            dislikes = map_info.get("dislikes", "")
            subs = map_info.get("subs", "")
            desc = map_info.get("desc", "")
            response_message = f"اسم الخريطة: {map_name}\nالمالك: {owner_name}\nمعرف المالك: {owner_uid}\nالإعجابات: {likes}\nالتعديلات: {dislikes}\nالمشتركون: {subs}\nالوصف: {desc}"
            bot.reply_to(message, response_message)
        else:
            bot.reply_to(message, "لم يتم العثور على معلومات الخريطة. لن يتم إيقاف البرنامج.")
    else:
        bot.reply_to(message, "حدث خطأ أثناء جلب معلومات الخريطة. لن يتم إيقاف البرنامج.")

@bot.callback_query_handler(func=lambda call: call.data.startswith('info'))
def callback_info(call):
    try:
        _, lang, uid = call.data.split('_')
        player_info = get_player_info(uid)
        if player_info:
            formatted_info, profile, outfits = format_player_info(player_info, lang)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=formatted_info)
            bot.send_sticker(chat_id=call.message.chat.id, sticker=profile,reply_to_message_id=call.message.message_id)
            bot.send_sticker(chat_id=call.message.chat.id, sticker=outfits,reply_to_message_id=call.message.message_id)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="هذا الايدي غير صالح أو لا يحتوي على بيانات.")
    except Exception as e:
        print(str(e))
def check_status(message, player_id):
    url = f"https://ff.garena.com/api/antihack/check_banned?lang=en&uid={player_id}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/plain, */*",
        'authority': "ff.garena.com",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'referer': "https://ff.garena.com/en/support/",
        'sec-ch-ua': "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'x-requested-with': "B6FksShzIgjfrYImLpTsadjS86sddhFH",
        'Cookie': "_ga_8RFDT0P8N9=GS1.1.1706295767.2.0.1706295767.0.0.0; apple_state_key=8236785ac31b11ee960a621594e13693; datadome=bbC6XTzUAS0pXgvEs7uZOGJRMPj4wRJzOh2zJmrQaYViaPVLZOIi__jw~cnNaIU1FzrByJ_qVJa7MwmpH3Z2jjRxtDkzsy2hiDTQ4cPY_n0mAwB3seemjGYszNpsfteh; token_session=f40bfc2e69a573f3bdb597e03c81c41f9ecf255f69d086aac38061fc350315ba5d64968819fe750f19910a1313b8c19b; _ga_Y1QNJ6ZLV6=GS1.1.1707023329.1.1.1707023568.0.0.0; _ga_KE3SY7MRSD=GS1.1.1707023591.1.1.1707023591.0.0.0; _gid=GA1.2.1798904638.1707023592; _gat_gtag_UA_207309476_25=1; _ga_RF9R6YT614=GS1.1.1707023592.1.0.1707023592.0.0.0; _ga=GA1.1.925801730.1706287088"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        result = response.json()
        is_banned = result.get('data', {}).get('is_banned', 0)
        period = result.get('data', {}).get('period', 0)
        region = result.get('data', {}).get('region', 'N/A')  # Default to 'N/A' if region not available
        developer_info = "\nمطور البوت\n."  # Developer information
        if is_banned == 1:
            message_text = f"ايدي الاعب 😀: {player_id}\nحالة الحساب 👍: مبند\nوقت البند 🕒: {period} ايام 🚫"
        else:
            message_text = f"ايدي الاعب 😀: {player_id}\nحالة الحساب 👍: هذا الاعب غير مبند"
        bot.reply_to(message, message_text)
    except requests.RequestException as e:
        bot.reply_to(message, f"Failed to fetch data from the API: {e}")

# Fonction pour lire le nombre d'utilisations du bot
def read_usage_count(user_id):
    try:
        with open('usage_stats.txt', 'r') as file:
            for line in file:
                line_parts = line.strip().split(',')
                if int(line_parts[0]) == user_id:
                    return int(line_parts[1])
    except FileNotFoundError:
        return 0
    except IndexError:
        return 0
    return 0

# Fonction pour mettre à jour le nombre d'utilisations du bot
def update_usage_count(user_id):
    try:
        with open('usage_stats.txt', 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            found = False
            for line in lines:
                line_parts = line.strip().split(',')
                if int(line_parts[0]) == user_id:
                    line_parts[1] = str(int(line_parts[1]) + 1)
                    found = True
                file.write(','.join(line_parts) + '\n')
            if not found:
                file.write(f"{user_id},1\n")
            file.truncate()
    except FileNotFoundError:
        with open('usage_stats.txt', 'w') as file:
            file.write(f"{user_id},1\n")

# Commande /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐅𝐫𝐞𝐞 𝐅𝐢𝐫𝐞 𝐁𝐚𝐧 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐁𝐨𝐭! 𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚 𝐩𝐥𝐚𝐲𝐞𝐫'𝐬 𝐈𝐃 𝐮𝐬𝐢𝐧𝐠 /BH 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞𝐢𝐫 𝐛𝐚𝐧 𝐬𝐭𝐚𝐭𝐮𝐬. 𝐄𝐱𝐚𝐦𝐩𝐥𝐞: /BH 𝐎𝐃𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖 🕵️‍♂️.")

# Commande /check
@bot.message_handler(commands=['BH'])
def check_command(message):

    player_id = message.text.split()[1]
    update_usage_count(message.from_user.id)
    check_status(message, player_id)

# Commande /stats
@bot.message_handler(commands=['stats'])
def show_stats(message):
    try:
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name

        usage_count = read_usage_count(user_id)
        stats_message = f"ℹ️ Statistiques d'utilisation pour @{username} ({user_id}):\n\nNombre d'utilisations du bot: {usage_count}\nPrénom: {first_name}\nNom de famille: {last_name}"
        bot.reply_to(message, stats_message)
    except FileNotFoundError:
        bot.reply_to(message, "Aucune statistique d'utilisation disponible pour le moment.")

def get_wishlist(uid, password, server):
    url = f"https://ff.samsedrain.com.np/wishlist?uid={uid}&password={password}&server={server}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبا بك! يمكنك استخدام الأمر /BW تتبعه رقم الحساب لجلب قائمة الأمنيات الخاصة بك.")

@bot.message_handler(commands=['BW'])
def get_wishlist_command(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "الرجاء تقديم رقم الحساب بعد الأمر /BW.")
        return
    uid = message.text.split()[1]
    password = "0529aizen003fshy"  # يمكنك إدراج طريقة للحصول على كلمة المرور هنا
    server = "sg"

    wishlist_data = get_wishlist(uid, password, server)
    if wishlist_data:
        items_info = "Item ID\t\tAdded Time\n"
        items = wishlist_data.get("message", {}).get("items", [])
        if not items:
            bot.reply_to(message, f"الايدي {uid} لا يحتوي على قائمة أمنيات.")
            return
        for item in items:
            added_at_timestamp = int(item.get("addedAt", 0))
            added_at_date = datetime.fromtimestamp(added_at_timestamp).strftime('%d/%m/%y, %I:%M:%S %p')
            item_id = item.get("itemId", "")
            items_info += f"{item_id}\t\t{added_at_date}\n"
        bot.reply_to(message, items_info)
    else:
        bot.reply_to(message, "حدث خطأ أثناء جلب قائمة الأمنيات.")

@bot.message_handler(commands=['i'])
def add_to_wishlist(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "الرجاء تقديم رقم العنصر بعد الأمر /i.")
        return
    item_id = message.text.split()[1]
    # الآن يمكنك إضافة كود لإضافة العنصر إلى قائمة الأمنيات

bot.polling()
