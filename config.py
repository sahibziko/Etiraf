#################################
# Etiraf Club Bot #
#################################
# Repo Sahibi - aykhan_s
# Telegram - t.me/aykhan_s
# Support - t.me/RoBotlarimTg
# GitHub - aykhan026
#################################
#################################
# Bu repo sıfırdan yığılıb
# Başka github hesabına yükləməy olmaz
# Reponu öz adına çıxaran peysərdi...!!!
#################################
#################################
#
import os
import heroku3
from telethon import TelegramClient, events
#
# Buranı qurdalama
# Yalnız deploy buttonuyla botunu yarat
# 
api_id = int(os.environ.get("2219492"))
api_hash = os.environ.get("e2714facad4b32d083303781af4d5029")
bot_token = os.environ.get("6114306244:AAFJSUOrxHruIVkU8FEPh6HfBMJw777lQ2U")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
admin_qrup = int(os.environ.get("-1001556282248"))
etiraf_qrup = int(os.environ.get("-1001556282248"))
kanal = os.environ.get("kmetiraf")
log_qrup = int(os.environ.get("-1001917971929"))
botad = os.environ.get("@Karabakhetirafbot")
etirafmsg = os.environ.get("**Etirafını necə paylaşım ?** 🤔")
startmesaj = os.environ.get("startmesaj")
etirafyaz = os.environ.get("Buyur bir etiraf yaz Daha sonra mən onun açıq və ya anonim olacağını soruşacam** 😍")
qrupstart = os.environ.get("✅ **Mən Aktivəm !** 💌 **Etiraf yazmaq üçün şəxsidən yazın")
gonderildi = os.environ.get("✅ **Etirafınız göndərildi Adminlər tərəfindən təsdiq olunduqdan sonra @Kmetiraf kanalında paylaşılacaq")
support = os.environ.get("kaarabachhbot")
sahib = os.environ.get("sjrvan")
#
# RoBotlarimTg
# RoBotlarimTg
# RoBotlarimTg

