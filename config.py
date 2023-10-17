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
API_ID = int(os.environ.get("2219492"))
API_HASH = os.environ.get("e2714facad4b32d083303781af4d5029")
BOT_TOKEN = os.environ.get("TOKEN")
# Telethon 
client = TelegramClient('client', API_ID, API_HASH).start(BOT_TOKEN=BOT_TOKEN)
#
ADMIN_QRUP_qrup = int(os.environ.get("ADMIN_QRUP"))
ETIRAF_QRUP = int(os.environ.get("ETIRAF_QRUP"))
KANAL = os.environ.get("kanal")
LOG_QRUP = int(os.environ.get("LOG_QRUP"))
BOTAD = os.environ.get("BOT_AD")
ETİRAFMSG = os.environ.get("etirafmsg")
STARTMESAJ = os.environ.get("startmesaj")
ETİRAFYAZ = os.environ.get("etirafyaz")
QRUPSTART = os.environ.get("qrupstart")
GONDERİLDİ = os.environ.get("gonderildi")
SUPPORT = os.environ.get("support")
SAHİB = os.environ.get("sahib")
#
# RoBotlarimTg
# RoBotlarimTg
# RoBotlarimTg
