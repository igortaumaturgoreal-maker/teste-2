import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def notificar_telegram(anuncio):
    msg = f"🚘 Oportunidade detectada! {anuncio['modelo']}/{anuncio['ano']} - R$ {anuncio['preco']} | FIPE: R$ {anuncio['fipe']} | Margem: R$ {anuncio['diferenca']} | {anuncio['link']}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg})
