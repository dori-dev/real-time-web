from channels.generic.websocket import AsyncWebsocketConsumer


class PriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("prices", self.channel_name)

    async def update(self, data):
        await self.send(text_data=data['text'])
