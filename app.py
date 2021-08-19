from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models.messages import StickerMessage

app = Flask(__name__)

line_bot_api = LineBotApi(
    'R5xWYeC0pvKPbizw+L4Ij8qgTwm583uCrdWVPnAucDpVd4wK47D2eV5KHvIKVafue5wQZ14CU27bhJoLq7pZ0S3GRZN0jbYgjTDwk4sWHL4avWOS7KP7VxqL79JiyOyPSj+1i8Sc68R8K04pT3gagAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('64a2f536f82c74d58b59120a151100f7')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    rmsg = '哈囉，聽不懂你在說甚麼~'

    # if "圖" or "貼圖" in msg:
    #     sticker_msg = StickerMessage(
    #         package_id="2",
    #         sticker_id="23",
    #     )
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         sticker_msg)
    #     return

    if msg in ["hi", "Hi", "hello", "Hello"]:
        rmsg = "嗨，我是賈斯伯!"
    elif msg in ["ㄟ", "欸", "hey"]:
        rmsg = "幹嘛"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=rmsg))


if __name__ == "__main__":
    app.run()
