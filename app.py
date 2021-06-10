from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('3olV0BESY/L3z5LX6EdWbem8l25TMwq/xPM1ngzVizdUzbLi55v/9NwPMkhQ+jyPBgSgFAgCjIB6U22hMyUoq2pBbjeSiKGclsTZSaP0gPFIoTxFpK4G7mr5+BpVtjMi6zYMKbrXuAXmfKG+VttLrgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2053e006837f6d880d1271d753978294')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    
    if '今日紫外線預警' in msg:
        message = TextSendMessage(
            '''請輸入想查詢紫外線預警的地區：
【北部：桃園市、基隆市、台北和新北、陽明山、新竹縣市】
【中部：彰化縣、南投縣、台中市】
【南部：嘉義市、屏東縣、台南市、玉山、高雄市】
【東部：宜蘭縣、台東縣、花蓮縣、三仙台】
【外島：澎湖縣、金門縣、蘭嶼、連江縣】
            '''
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif '桃園市' in msg:
        message = TextSendMessage(text=uv_alert('桃園'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '基隆市' in msg:
        message = TextSendMessage(text=uv_alert('基隆'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台北和新北' in msg:
        message = TextSendMessage(text=uv_alert('台北'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '陽明山' in msg:
        message = TextSendMessage(text=uv_alert('陽明山'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '新竹縣市' in msg:
        message = TextSendMessage(text=uv_alert('新竹'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '彰化線' in msg:
        message = TextSendMessage(text=uv_alert('彰化'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '南投縣' in msg:
        message = TextSendMessage(text=uv_alert('南投'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '嘉義市' in msg:
        message = TextSendMessage(text=uv_alert('嘉義'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台中市' in msg:
        message = TextSendMessage(text=uv_alert('台中'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '屏東縣' in msg:
        message = TextSendMessage(text=uv_alert('屏東'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台南市' in msg:
        message = TextSendMessage(text=uv_alert('台南'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '玉山' in msg:
        message = TextSendMessage(text=uv_alert('玉山'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '高雄市' in msg:
        message = TextSendMessage(text=uv_alert('高雄'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '宜蘭縣' in msg:
        message = TextSendMessage(text=uv_alert('宜蘭'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台東縣' in msg:
        message = TextSendMessage(text=uv_alert('台東'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '花蓮縣' in msg:
        message = TextSendMessage(text=uv_alert('花蓮'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '三仙台' in msg:
        message = TextSendMessage(text=uv_alert('三仙台'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '澎湖縣' in msg:
        message = TextSendMessage(text=uv_alert('澎湖'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '金門縣' in msg:
        message = TextSendMessage(text=uv_alert('金門'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '蘭嶼' in msg:
        message = TextSendMessage(text=uv_alert('蘭嶼'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '連江縣' in msg:
        message = TextSendMessage(text=uv_alert('馬祖'))
        line_bot_api.reply_message(event.reply_token, message)

    elif '今日浪況提醒' in msg:
        message = TextSendMessage(
            '''請輸入想要查詢今日浪況的地區：
    北海岸：龍洞、富貴角
    中部：新竹、台中
    南部：彌陀、七股、鵝鸞鼻
    東部：蘇澳、花蓮、台東
    離島：小琉球、金門、馬祖、澎湖、蘭嶼、龜山島、彭佳嶼
            '''
        )
        line_bot_api.reply_message(event.reply_token, message)
    #北海岸
    elif '龍洞' in msg:
        message = TextSendMessage(text=wave_alert('龍洞'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '富貴角' in msg:
        message = TextSendMessage(text=wave_alert('富貴角'))
        line_bot_api.reply_message(event.reply_token, message)
    #中部
    elif '新竹' in msg:
        message = TextSendMessage(text=wave_alert('新竹'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台中' in msg:
        message = TextSendMessage(text=wave_alert('台中'))
        line_bot_api.reply_message(event.reply_token, message)
    #南部
    elif '彌陀' in msg:
        message = TextSendMessage(text=wave_alert('彌陀'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '七股' in msg:
        message = TextSendMessage(text=wave_alert('七股'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '鵝鑾鼻' in msg:
        message = TextSendMessage(text=wave_alert('鵝鑾鼻'))
        line_bot_api.reply_message(event.reply_token, message)
    #東部
    elif '蘇澳' in msg:
        message = TextSendMessage(text=wave_alert('蘇澳'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台東' in msg:
        message = TextSendMessage(text=wave_alert('台東'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '花蓮' in msg:
        message = TextSendMessage(text=wave_alert('花蓮'))
        line_bot_api.reply_message(event.reply_token, message)
    #離島
    elif '小琉球' in msg:
        message = TextSendMessage(text=wave_alert('小琉球'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '金門' in msg:
        message = TextSendMessage(text=wave_alert('金門'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '馬祖' in msg:
        message = TextSendMessage(text=wave_alert('馬祖'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '澎湖' in msg:
        message = TextSendMessage(text=wave_alert('澎湖'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '蘭嶼' in msg:
        message = TextSendMessage(text=wave_alert('蘭嶼'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '龜山島' in msg:
        message = TextSendMessage(text=wave_alert('龜山島'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '彭佳嶼' in msg:
        message = TextSendMessage(text=wave_alert('彭佳嶼'))
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='你說的是不是 ' + msg)
        line_bot_api.reply_message(event.reply_token, message)
    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
