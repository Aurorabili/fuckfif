import os


class VirtualMic:
    def __init__(self, device_name, format, rate, channels):
        self.device_name = device_name
        self.format = format
        self.rate = rate
        self.channels = channels

        retry = 0
        while not os.path.exists("/tmp/" + self.device_name):
            retry = retry + 1
            if retry > 5:
                raise Exception("[VirtualMic] 虚拟声卡初始化失败。")
            print("[VirtualMic] 开始初始化虚拟声卡。")
            os.system(
                "pactl load-module module-pipe-source source_name={} file=/tmp/{} format={} rate={} channels={}".format(
                    self.device_name,
                    self.device_name,
                    self.format,
                    self.rate,
                    self.channels,
                )
            )
            os.system(
                "pacmd update-source-proplist {} device.description={}".format(
                    self.device_name, self.device_name
                )
            )
            os.system("pacmd set-default-source {}".format(self.device_name))
        print("[VirtualMic] 虚拟声卡初始化完成。")

    def play(self, file_path):
        print("[VirtualMic] 音频流开始从{}读到虚拟声卡中。".format(file_path))
        os.system(
            "ffmpeg -re -i {} -f {} -ar {} -ac {} -async 1 -filter:a volume=0.8 - > /tmp/{}".format(
                file_path, self.format, self.rate, self.channels, self.device_name
            )
        )

        # process = subprocess.Popen(
        #     [
        #         "ffmpeg",
        #         "-re",
        #         "-i",
        #         file_path,
        #         "-f",
        #         self.format,
        #         "-ar",
        #         self.rate,
        #         "-ac",
        #         self.channels,
        #         "-async",
        #         "1",
        #         "-filter:a",
        #         "volume=0.1",
        #         "-",
        #         ">",
        #         self.device_name,
        #     ],
        # )
        # exit_code = process.wait()
        # if exit_code != 0:
        #     raise Exception("ffmpeg failed")
        print("[VirtualMic] 音频流结束。".format(file_path))
        return
