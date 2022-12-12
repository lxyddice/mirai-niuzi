from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.message.parser.base import DetectPrefix
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group, Member
from graia.ariadne.message.element import At
from graia.saya import Saya

channel = Channel.current()
saya = create(Saya)


@channel.use(ListenerSchema(listening_events=[GroupMessage], decorators=[DetectPrefix('/')]))
async def helpmessage(app: Ariadne, group: Group, member: Member, message: MessageChain):

    if message.display == '/nzhelp':
        help_information = "\n/nz我的牛子\n/nzget获取牛子\n/nzqd牛子签到\n/nzdj打∠\n/nzph牛子排行\n/nzzt牛子状态\n/nzpk <@user>与某人比划比划\n/nztt <@user>与某人贴贴\n/nzjh启用或禁止与他人交互\n/nzkf牛子开发信息" \
                           ""
        await app.send_message(
            group,
            MessageChain(At(member.id), help_information),
        )
    if message.display == '/nzkf':
        help_information = "\n本项目是因为看到有个有趣的小游戏以开发的，为了练习编程，我们使用了python与php进行构建模仿，已获得不错的进展。" \
                           "\n警告：牛子长度小于0时将被封禁，直到新功能开发完毕，敬请期待，感谢支持！\n项目地址：https://github.com/lxyddice/mirai-niuzi"
        await app.send_message(
            group,
            MessageChain(At(member.id), help_information),
        )
