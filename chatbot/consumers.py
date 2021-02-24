import json
from channels.generic.websocket import SyncConsumer
from main.models import Advert


class ChatBotConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        text_data_json = json.loads(event['text'])
        message = ''
        if '#' in text_data_json['message']:
            msg = text_data_json['message'].split('#')[1]
            if Advert.objects.filter(advert_title__icontains=msg):
                message = f'Обьявление {msg} ативно'
            else:
                message = 'Нету такого'
        else:
            message = 'формат запроса `# название объекта`'

        self.send({
            "type": "websocket.send",
            "text": json.dumps({'message': f'[bot]: {message}'}),
        })
