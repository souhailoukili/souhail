from telegram import Bot
from telegram.ext import Updater, CommandHandler
import logging
import random

# Mettez votre token de bot Telegram ici
TOKEN = '7134890370:AAE9Aj3dIyskGvsSAkJeI_G-HWbcgYT7uV8'

# Liste de messages de maintenance
MAINTENANCE_MESSAGES = [
    'Nous sommes en cours de maintenance. Merci de votre compréhension.',
    'Le service est temporairement indisponible pour maintenance. Veuillez patienter.',
    'Nous effectuons des travaux de maintenance. Désolé pour le dérangement.'
]

# Mettez l'ID de votre groupe ici
GROUP_ID = '-1002136444842'

# Configurez le logger pour voir les erreurs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Définissez la fonction de la commande /maintenance
def maintenance(update, context):
    # Choisissez un message de maintenance au hasard
    maintenance_message = random.choice(MAINTENANCE_MESSAGES)
    
    # Envoie du message de maintenance au groupe spécifié
    context.bot.send_message(chat_id=GROUP_ID, text=maintenance_message)

# Démarrez le bot
def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Ajoutez un gestionnaire de commande pour la commande /maintenance
    dispatcher.add_handler(CommandHandler("maintenance", maintenance))

    # Démarrez le bot
    updater.start_polling()
    logger.info("Bot démarré")

    # Gardez le bot actif jusqu'à ce que vous appuyiez sur Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
