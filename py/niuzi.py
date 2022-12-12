import requests
import random


from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.message.parser.base import DetectPrefix
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain, Plain
from graia.ariadne.model import Group, Member
from graia.ariadne.message.element import At
from graia.saya import Saya

channel = Channel.current()
saya = create(Saya)


@channel.use(ListenerSchema(listening_events=[GroupMessage], decorators=[DetectPrefix('/nz')]))
async def shutdown(app: Ariadne, group: Group, member: Member, message: MessageChain):
    command = message.display.split()
    respa = 0
    respb = 0
    if len(command) == 2:
        qq1 = str(member.id)
        qq2 = str(command[1])[1:]
        respa = requests.get('http://your_web/niuzichaxunban.php?qq=' + qq1).text
        respb = requests.get('http://your_web/niuzichaxunban.php?qq=' + qq2).text
    else:
        qq1 = str(member.id)
        respa = requests.get('http://your_web/niuzichaxunban.php?qq=' + qq1).text
    respa = str(respa)
    respb = str(respb)
    if respa == "0" and respb == "0":
        
        if message.display == '/nzget':
            qq=str(member.id)
            resp = requests.get('http://your_web/woyaoniuzi.php?qq=' + qq + "&name=" + member.name).text
            
            await app.send_message(
                group,
                MessageChain(At(member.id), resp),
            )
        if message.display == '/nzdj':
            qq=str(member.id)
            resp1 = requests.get('http://your_web/niuzichaxuntextjoy.php?qq=' + qq).text
            resp2 = requests.get('http://your_web/niuzichaxuntext.php?qq=' + qq).text
            if resp2 == "不存在的牛子":
                await app.send_message(
                        group,
                        MessageChain(At(member.id), "不存在的牛子，请输入/nzget以获取"),
                )
                
            else:
                if float(resp2)>float(resp1)*0.0062*5+5:
                    dj = random.uniform(3.5, 5)
                    dj = float(dj)+(float(dj)*float(resp1)*0.0062)
                    joy1 = 8+float(resp1)
                    joy2 = 8
                    cd = float(resp2)-float(dj)
                    resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq +'&cd=' + str(cd)).text
                    resp = requests.get('http://your_web/niuzixiugaijoy.php?qq=' + qq +'&joy=' + str(joy1)).text
                    await app.send_message(
                        group,
                        MessageChain(At(member.id), "打∠完成，消耗了" + str(dj) + "cm，愉悦值+" + str(joy2) + "！"),
                    )
                else:
                    await app.send_message(
                        group,
                        MessageChain(At(member.id), "你尝试打∠，但是由于牛子疲软失败了"),
                    )
        if message.display == '/nzqd':
            qq=str(member.id)
            name=str(member.name)
            resp = requests.get('http://your_web/niuziqiandao.php?qq=' + qq + "&name=" + name).text
            resp=str.lstrip(resp)
            await app.send_message(
                group,
                MessageChain(At(member.id), resp),
            )
        if message.display == '/nzzg':
            qq=str(member.id)
            name=str(member.name)
            resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq + "&cd=" + "0").text
            resp=str.lstrip(resp)
            await app.send_message(
                group,
                MessageChain(At(member.id), resp),
            )
        if message.display == '/nzzt':
            qq=str(member.id)
            resp = requests.get('http://your_web/niuzilengqueonlyget.php?qq=' + qq).text
            resp=str.lstrip(resp)
            await app.send_message(
                group,
                MessageChain(At(member.id), resp),
            )
        if message.display == '/nzph':
            a = "0"
            if a == "1":
                qq=str(member.id)
                resp = requests.get('http://your_web/niuzipaihang2.php').text
                await app.send_message(
                    group,
                    MessageChain(At(member.id), "\n" + resp),
                )
            else:
                await app.send_message(
                    group,
                    MessageChain(At(member.id), "\n由于消息转发还在研究，为防止刷屏，该功能已禁用"),
                )
        if message.display == '/myname':  
            await app.send_message(
                group,
                MessageChain(At(member.id), "你叫" + str(member.name)),
            )
        if message.display == '/myname':  
            await app.send_message(
                group,
                MessageChain(At(member.id), "你叫" + str(member.name)),
            )


        if message.display.startswith('/nzpk'):
            command = message.display.split()
            if len(command) == 2:
                qq1 = str(member.id)
                qq2 = str(command[1])[1:]
                resp = requests.get('http://your_web/haveniuzi.php?qq=' + qq1).text
                if resp == "这个人有牛子":
                    resp = requests.get('http://your_web/niuzilengque.php?qq=' + qq1).text
                    resp=str.lstrip(resp)
                    if resp == "你的牛子很健康":
                        resp = requests.get('http://your_web/haveniuzi.php?qq=' + qq2).text
                        if resp == "这个人有牛子":
                            resp = requests.get('http://your_web/niuzilengque.php?qq=' + qq2).text
                            resp=str.lstrip(resp)
                            if resp == "你的牛子很健康":
                                win = random.randint(1,99)
                                pknum = random.uniform(0.2, 1.2)
                                yyzjs = random.randint(0, 1)
                                pknum = float(pknum)
                                print(win)
                                
                                if win <= 50:
                                    resp = requests.get('http://your_web/niuzichaxuntext.php?qq=' + qq1).text
                                    resp = float(resp)
                                    cd = resp + float(pknum)
                                    cd = str(cd)
                                    resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq1 +'&cd=' + cd).text

                                    resp1 = requests.get('http://your_web/niuzichaxuntext.php?qq=' + qq2).text
                                    resp2 = requests.get('http://your_web/niuzigetjoy.php?qq=' + qq2).text
                                    resp3 = requests.get('http://your_web/niuzichaxuntextjoy.php?qq=' + qq2).text
                                    zsj = float(resp2)*0.0035*float(pknum)
                                    cd = float(resp1)-float(pknum)+float(zsj)
                                    ccd = float(pknum)-float(zsj)
                                    joy = float(resp3)-yyzjs
                                    resp = requests.get('http://your_web/niuzixiugai.php?qq=' + str(qq2) +'&cd=' + str(cd)).text
                                    resp = requests.get('http://your_web/niuzixiugaijoy.php?qq=' + str(qq2) +'&joy=' + str(joy)).text
                                    await app.send_message(group, MessageChain(At(member.id),"你赢了" + str(pknum) + "cm，对方长度-" + str(ccd) + "cm且愉悦值-" + str(yyzjs)),)
                                else:
                                    resp = requests.get('http://your_web/niuzichaxuntext.php?qq=' + qq2).text
                                    resp = float(resp)
                                    cd = resp + float(pknum)
                                    cd = str(cd)
                                    resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq2 +'&cd=' + cd).text

                                    resp1 = requests.get('http://your_web/niuzichaxuntext.php?qq=' + qq1).text
                                    resp2 = requests.get('http://your_web/niuzigetjoy.php?qq=' + qq1).text
                                    resp3 = requests.get('http://your_web/niuzichaxuntextjoy.php?qq=' + qq1).text
                                    joy = float(resp3)-yyzjs
                                    zsj = float(resp2)*0.0035*float(pknum)
                                    cd = float(resp1)-float(pknum)+float(zsj)
                                    ccd = float(pknum)-float(zsj)
                                    resp = requests.get('http://your_web/niuzixiugai.php?qq=' + str(qq1) +'&cd=' + str(cd)).text
                                    resp = requests.get('http://your_web/niuzixiugaijoy.php?qq=' + str(qq1) +'&joy=' + str(joy)).text
                                    await app.send_message(group, MessageChain(At(member.id),"你输了" + str(ccd) + "cm且愉悦值-" + str(yyzjs) + "，对方长度+" + str(pknum) + "cm！"),)
                            else:
                                await app.send_message(group, "受约者的牛子很累了！你不能与这个人pk！")
                        else:
                            await app.send_message(group, "受约者还没有牛子！你不能与这个人pk！")
                    else:
                        await app.send_message(group, "你的牛子很累了！你不能与这个人pk！")
                else:
                    await app.send_message(group, "你还没有牛子！你不能与这个人pk！") 
            else:
                await app.send_message(group, "参数错误")
        if message.display.startswith('/nztt'):
            command = message.display.split()
            if len(command) == 2:
                
                qq1 = str(member.id)
                qq2 = str(command[1])[1:]
                resp = requests.get('http://your_web/haveniuzi.php?qq=' + qq1).text
                resp = str.lstrip(resp)
                
                if resp == "这个人有牛子":
                    resp = requests.get('http://your_web/haveniuzi.php?qq=' + qq2).text
                    resp=str.lstrip(resp)
                    
     
                    if resp == "这个人有牛子":
                        resp1 = requests.get('http://your_web/niuzitietie.php?qq=' + qq1).text
                        resp1 = str.lstrip(resp1)
                        
                        if resp1 == "贴贴成功":
                            resp2 = requests.get('http://your_web/niuzitietie.php?qq=' + qq2).text
                            resp2 = str.lstrip(resp2)
                            
                            if resp2 == "贴贴成功":
                                
                                pknum = random.uniform(0.2, 0.5)
                                pknum = float(pknum)
                                
                                resp1 = requests.get('http://your_web/niuzichaxuntext.php?qq=' + qq1).text
                                
                                resp2 = requests.get('http://your_web/niuzigetjoy.php?qq=' + qq1).text
                                zj1 = 0.0048*float(pknum)*float(resp2)+float(pknum)
                                cd = float(resp1)+float(zj1)
                                cd1 = str(cd)
                                resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq1 +'&cd=' + str(cd1)).text
                                
                                resp1 = requests.get('http://your_web/niuzichaxuntext.php?qq=' + qq2).text
                                
                                resp2 = requests.get('http://your_web/niuzigetjoy.php?qq=' + qq2).text
                                zj2 = 0.0048*float(pknum)*float(resp2)+float(pknum)
                                cd = float(resp1)+float(zj2)
                                cd2 = str(cd)
                                resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq2 +'&cd=' + str(cd2)).text
                                await app.send_message(group, MessageChain(At(member.id),"贴贴成功惹，你的牛子增加了" + str(zj1) + "cm,对方增加了" + str(zj2) + "cm！"))
            
                            else:
                                await app.send_message(group, "贴贴失败！因为受约者筋疲力尽...没力气贴贴了..." )
                        else:
                            await app.send_message(group, "贴贴失败！因为你筋疲力尽...没力气贴贴了..." )
                    else:
                        await app.send_message(group, "贴贴失败！因为受约者没有获取牛子，输入/nzget以获取")
                else:
                    await app.send_message(group, "贴贴失败！因为没有获取牛子，输入/nzget以获取")
            else:
                await app.send_message(group, "参数错误")
    else:
        if respa == "2" or respb == "2":
            if message.display == '/nzjh':
                baoliu = "0"
                
            else:
                await app.send_message(group, MessageChain(At(member.id), "你或者受约者设置了不允许交互！"),)
                
        else:
            baoliu="2333"
            if respa == "1" or respb == "1":
                if respa == "1":
                    if message.display == '/nzjh':
                        baoliu = "6666"
                    else:
                        await app.send_message(group, MessageChain(At(member.id), "你的牛子长度小于0了，已被封禁，请期待后续版本更新，感谢支持！"),)
                else:
                    if message.display == '/nzjh':
                        baoliu = "6666"
                    else:
                        await app.send_message(group, MessageChain(At(member.id), "受约者的牛子长度小于0了，已被封禁，请期待后续版本更新，感谢支持！"),)
                
    if message.display.startswith('/nzxg'):
            if member.id in [2874660056]:
                command = message.display.split()
                if len(command) == 3:
                    qq = str(command[1])[1:]
                    cd = str(command[2])
                    resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq +'&cd=' + cd).text
                    await app.send_message(group, str(resp))
                else:
                    await app.send_message(group, "参数错误")
            else:
                await app.send_message(group, MessageChain(At(member.id), "我不想听你的话..."),)

    if message.display.startswith('/nzxj'):
        if member.id in [2874660056]:
            command = message.display.split()
            if len(command) == 3:
                qq = str(command[1])[1:]
                joy = str(command[2])
                print(joy)
                resp = requests.get('http://your_web/niuzixiugaijoy.php?qq=' + qq +'&joy=' + str(joy)).text
                await app.send_message(group, str(resp))
            else:
                await app.send_message(group, "参数错误")
        else:
            await app.send_message(group, MessageChain(At(member.id), "我不想听你的话..."),)
    if message.display == '/nzjh':  
            qq=str(member.id)
            resp = requests.get('http://your_web/niuziwantban.php?qq=' + qq).text
            resp=str.lstrip(resp)
           
            await app.send_message(
                group,
                MessageChain(At(member.id), resp),
            )


@channel.use(ListenerSchema(listening_events=[GroupMessage], decorators=[DetectPrefix('/mynz')]))
async def shutdown(app: Ariadne, group: Group, member: Member, message: MessageChain):
    if message.display == '/mynz':
            qq=str(member.id)
            respa = requests.get('http://your_web/niuzichaxun.php?qq=' + qq).text
            respb = requests.get('http://your_web/niuzichaxunjoy.php?qq=' + qq).text
            resp = str(respa) + str(respb)
            await app.send_message(
                group,
                MessageChain(At(member.id), resp),
            )



@channel.use(ListenerSchema(listening_events=[GroupMessage], decorators=[DetectPrefix('/opnz')]))
async def shutdown(app: Ariadne, group: Group, member: Member, message: MessageChain):
    if message.display.startswith('/opnzxg'):
            if member.id in [2874660056]:
                command = message.display.split()
                if len(command) == 3:
                    qq = str(command[1])[1:]
                    cd = str(command[2])
                    resp = requests.get('http://your_web/niuzixiugai.php?qq=' + qq +'&cd=' + cd).text
                    await app.send_message(group, str(resp))
                else:
                    await app.send_message(group, "参数错误")
            else:
                await app.send_message(group, MessageChain(At(member.id), "我不想听你的话..."),)

    if message.display.startswith('/opnzxj'):
        if member.id in [2874660056]:
            command = message.display.split()
            if len(command) == 3:
                qq = str(command[1])[1:]
                joy = str(command[2])
                print(joy)
                resp = requests.get('http://your_web/niuzixiugaijoy.php?qq=' + qq +'&joy=' + str(joy)).text
                await app.send_message(group, str(resp))
            else:
                await app.send_message(group, "参数错误")
        else:
            await app.send_message(group, MessageChain(At(member.id), "我不想听你的话..."),)
