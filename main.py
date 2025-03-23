from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.core.message.components import At, Image


@register("random_img", "昼阳Helios", "一个随机图片插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("img")
    async def helloworld(self, event: AstrMessageEvent):
        '''获取随机图片''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        chain = [
            At(qq=event.get_sender_id()),  # At 消息发送者
            Image.fromURL("https://pic.static.cv/api/random")  # 从本地文件目录发送图片
        ]
        yield event.chain_result(chain)