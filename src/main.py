import io
import json

print("[main] 正在检测环境并加载神经网络。")

from connector.FiFWebClient import FiFWebClient
from speaker.Speaker import Speaker

print("[main] FiF口语,启动!")

fif = FiFWebClient()  # 初始化FiF口语网页客户端
speaker = Speaker(  # 初始化语音合成器
    "tts_models/multilingual/multi-dataset/your_tts",  # 语音合成器模型
    "cuda",  # cuda|cpu 是否启用GPU加速
    "VirtualPipeMic",  # 虚拟麦克风名称 最后会将音频流输出到/tmp/{此选项的名称}
    "draft/target_boy_voice.wav",  # 10秒左右的你的录音，用于生成目标音色
)

with io.open("user.json") as f:
    user_json = json.load(f)
    username = user_json["username"]
    password = user_json["password"]

user_info = fif.login(username, password)

print(
    "[main] {}登录成功。用户ID为{}。".format(
        user_info["data"]["realName"], user_info["data"]["userId"]
    )
)

for i, task in enumerate(fif.get_task_list(fif.get_page())["data"]["ttiList"]):
    ttd_list = fif.get_ttd_list(fif.get_page(), task["id"])
    print(
        "[main] 正在开始第{}个任务。任务代码为{}。任务名为{}。".format(i + 1, task["id"], task["taskName"])
    )
    for j, ttd in enumerate(ttd_list["data"]["ttdList"]):
        print(
            "[main] 正在开始第{}个单元。单元代码为{}。单元名为{}。".format(
                j + 1, ttd["id"], ttd["unitName"]
            )
        )
        unit_info = fif.get_unit_info(fif.get_page(), ttd["unitid"], task["taskId"])[
            "data"
        ]
        print("[main] 正在开始第{}个单元。单元代码为{}。".format(j + 1, unit_info["id"]))
        for k, level in enumerate(unit_info["levelList"]):
            if level["levelScore"] >= 80:
                print("[main] 等级{}超过目标分数。已跳过。".format(level["levelName"]))
                continue
            print(
                "[main] 正在开始第{}个等级。等级代码为{}。等级名为{}。".format(
                    k + 1, level["levelId"], level["levelName"]
                )
            )

            # ? FiF口语网页端似乎没有实现问答类型题目，它无法录音。故跳过。
            if "问答" in level["levelName"] and not "简短问答" in level["levelName"]:
                print("[main] 第{}个等级为问答题。已跳过。".format(k + 1))
                continue

            fif.start_level_test(
                fif.get_page(),
                speaker,
                unit_id=unit_info["id"],
                task_id=task["id"],
                level_id=level["levelId"],
            ),

            print("[main] 第{}个等级完成。".format(k + 1))
