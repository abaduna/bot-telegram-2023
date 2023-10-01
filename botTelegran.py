
from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
TOKEN: Final = "6658013709:AAHyiACRg3neY6AMy0oIu67flb-963Mouo4"
BOT_USERNAME:Final="@abaduna_bot"


#comandos
async def strat_command(updata:Update, contex:ContextTypes.DEFAULT_TYPE):
    
    await updata.message.reply_text("hola soy un bot de artu")

async def help_command(updata:Update, contex:ContextTypes.DEFAULT_TYPE):
    await updata.message.reply_text("Puede hablar conmigo")
async def custom_command(updata:Update, contex:ContextTypes.DEFAULT_TYPE):
    await updata.message.reply_text("Probando x2 xd")


#respondes

def handle_response(text:str) -> str:
    processed: str = text.lower()

    if "hola" in processed:
        return "Hola soy un boy contruido por Artu"
    if "como estas" in processed:
        return "bien y vs"
    if "amo python" in processed:
        return "si yo tambien lo amo sabias que se puede construir satalites"
    if "que te gusta" in processed:
        return "me gusta las ia y todo lo que tiene que ver con py" 
    return "no entiendo lo que dices"

async def handle_message(updata:Update,contex:ContextTypes.DEFAULT_TYPE):
    message_type:str = updata.message.chat.type
    text:str = updata.message.text
    print(f'Usuario ({updata.message.chat.id}) in {message_type}:"{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,"").strip()
            response:str =handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)
    print("bot", response)
    await updata.message.reply_text(response)



async  def error(updata:Update,contex:ContextTypes.DEFAULT_TYPE):
    print(f'Update {updata} causa error {contex.error}')

if __name__ == "__main__":
    print("funcionaaa")
    app = Application.builder().token(TOKEN).build()
    #comandos
    app.add_handler((CommandHandler('start',strat_command)))
    app.add_handler((CommandHandler('help',help_command)))
    app.add_handler((CommandHandler('custom',custom_command)))

    #mensajes 

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #erores

    app.add_error_handler(error)
    print("corriendo")
    app.run_polling(poll_interval=5)