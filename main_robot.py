import pkgutil
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import config
from graia.saya import Saya

# bcc = create(Broadcast)
saya = create(Saya)
app = Ariadne(
    connection=config(
        114514,  # 你的机器人的 qq 号
        "1919810",  # 填入你的 mirai-api-http 配置中的 verifyKey
    ),
)

with saya.module_context():
    for module_info in pkgutil.iter_modules(["ReplyPack"]):
        if module_info.name.startswith("_"):  # 假设模组是以 `_` 开头的，就不去导入
            continue
        saya.require(f"ReplyPack.{module_info.name}")

# con = Console(broadcast=bcc, prompt="> ")
# # Windows控制台专属代码，不能作用于任何调试器
# saya.install_behaviours(ConsoleBehaviour(con))
app.launch_blocking()
