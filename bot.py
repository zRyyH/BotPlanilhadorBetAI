from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
import logging

from computer_vision import ComputerVision
from api_sheets import SheetsAPI
from gpt_filter import GPTFilter
from authentication import Auth
from settings import Settings
from models import Models

from formatter import format_reply


AUTH = Auth()
AUTH.load_users()

SETTINGS = Settings()
SETTINGS.load_settings()
config = SETTINGS.get_config()

MODELS = Models()
MODELS.load_models()
models = MODELS.get_models()

SHEET_API = SheetsAPI(config=config)
GPT_FILTER = GPTFilter(config=config, models=models)
COMPUTER_VISION = ComputerVision(config=config)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not AUTH.auth_by_id(id=update.message.from_user.id):
        await update.message.reply_text(f"Digite a senha para liberar o bot.")
    else:
        await update.message.reply_text(f"Voce já está autenticado, voce já pode mandar seus prints para analise!")

        
async def handle_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.message.from_user.id
    name = update.message.from_user.first_name
    msg = update.message.text.strip()
    pw = SETTINGS.get_config()['password']
    isAuth = msg == pw
    
    if not AUTH.auth_by_id(id=id):
        if isAuth:
            AUTH.add_user(id=id, name=name)
            await update.message.reply_text(f"Usuário {name} autenticado com sucesso!")
        else:
            await update.message.reply_text(f"Digite a senha para liberar o bot.")
    else:
        if isAuth:
            await update.message.reply_text(f"Voce já está autenticado {name}!")
        else:
            await update.message.reply_text(f"Comando invalido!")
    
    
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.message.from_user.id
    msg_id = update.message.message_id
    
    if not AUTH.auth_by_id(id=id):
        await update.message.reply_text(f"Digite a senha para liberar o bot.")
        return
    
    file_id = update.message.photo[-1].file_id
    file = await context.bot.get_file(file_id)
    
    file_path = COMPUTER_VISION.get_file_path()
    await file.download_to_drive(file_path)
    
    dados = COMPUTER_VISION.extract_text(file_path)
    dados = GPT_FILTER.normalize(dados)
    values = SHEET_API.adicionar_aposta(dados)
    
    msg = format_reply(dados)
    
    if values:
        await update.message.reply_text(msg, reply_to_message_id=msg_id)
    else:
        await update.message.reply_text('⚠️ Ocorreu um erro.', reply_to_message_id=msg_id)
        
        
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(f'UPDATE "{update}" CAUSA DO ERRO: {context.error}')
    
    
def main():
    application = ApplicationBuilder().token(SETTINGS.get_config()['telegram_token']).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_password))
    application.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    application.add_error_handler(error)
    
    application.run_polling()

if __name__ == '__main__':
    logger.info('Bot Funcionando!')
    main()