<div align="center">
    <h1 align="center">Fuck FiF</h1>
    <p align="center">使用生成语音全自动完成FiF英语口语作业</p>
</div>

# 🎯 目标

任何人都有自己学习和练习英语口语的方式，特别是对于大学生来说，强制要求他们学习不感兴趣的语言和采用作业的形式评价他们的学习成果显然是十分糟糕的。大学生们通常有自己清晰的目标。时间应该被利用在更需要的地方。

本项目是针对于[FiF口语训练系统](https://www.fifedu.com/iplat/html/home/home.html)的自动完成脚本。旨在使用非侵入式的方法自动完成口语作业。
# 🌟 特性

- **YourTTS**模型只需要数秒即可模仿你的声音。

- 模拟点击而非网络包中间人攻击，FiF口语难以检测你的行为。

- 打开浏览器也是自动的。全程只需你一次点击。

- 使用虚拟麦克风输入，它将安静的在后台工作。

# 🍗 使用

**目前仅可在Linux中部署该项目。Windows部署将在计划内支持。**

## 驱动依赖
项目使用`pulseaudio`来创建虚拟麦克风，这是他只能在Linux平台部署的最大原因。
```
pulseaudio      # Linux声卡驱动
```
## 克隆项目到本地
```bash
git clone https://github.com/Aurorabili/fuckfif
cd fuckfif
```

## 使用pip安装项目依赖
```bash
pip install TTS playwright 
```

## 填写FiF口语用户名和密码
在项目根目录创建`user.json`:
```json
{
    "username": "你的FiF口语用户名",
    "password": "你的FiF口语密码"
}
```

## 录制样本声音
YourTTS需要一段10秒左右的录音来模仿你的音色以生成口语作业里的英语录音。你可以在安静的环境中使用手机录音机进行录音。然后重命名并放到这个路径`draft/target_voice.wav`。这个录音需要你朗读一段英文文本，大概在10秒钟左右，请在安静的地方进行以确保没有底噪。

这里提供一段英文文本：
```
The original vision of AI was re-articulated in two sousands via the term Artificial General Intelligence or AGI. This vision is to build Thinking Machines computer systems that can learn, reason, and solve problems similar to the way humans do.
```

## 启动项目
当一切准备就绪。使用python运行`src/main.py`。
```bash
python src/main.py
```
# 🗺️ 路线图
- [ ] 使用其他虚拟麦克风方案以支持在Windows平台部署。
- [ ] 一键部署脚本，方便任何人立刻开始他的FiF口语之旅。
- [ ] 添加Android版本FiF客户端连接器。
- [ ] 使用原音输出或在线TTS降低算力要求以支持边缘计算平台。
- [ ] 支持快速微调的模型以拟真声音。

# 😞 已知问题
- 当合成单个单词的录音时，YourTTS模型的效果不佳，这也许是和`speaker_wav`参数有关。
- 官方的网页端似乎未实现问答类型的题目，导致部分问答类型的题目无法完成。
- 在作业`四六级口语,六级口语模拟题 2,Part 2-1-1 个人发言`(levelid:e22e45aaeaf64e42ace1fa5ea038d2b0)中的第二题里FiF口语会在3秒后自动结束录音导致无法完成作业。

# 🪜 代码结构
```
src
├── main.py             # 主程序
├── connector           # FiF客户端连接器
├── speaker             # 语音合成器抽象
├── tts                 # TTS模型
└── vmic                # 虚拟麦克风
```

# 🎈 提交贡献
我一个人无法和日益更新的FiF口语系统抗衡。受限于我自己的口语作业，我也无法适配所有题目类型。

我们欢迎任何人提交贡献。如果你有任何想法、建议、新题型以及错误报告，欢迎提交issue，我们很期待与你讨论。如果你有任何代码上的改进，欢迎提交PR。

# 📝 说明
本项目仅供学习交流使用，不得用于商业用途。使用本项目造成的一切后果由使用者自行承担。

# 🔗 引用
- [microsoft/playwright](https://github.com/microsoft/playwright)
- [Edresson/YourTTS](https://github.com/Edresson/YourTTS)
- [coqui-ai/TTS](https://github.com/coqui-ai/TTS)

# 📜 许可证
本项目使用[MIT许可证](LICENSE)。