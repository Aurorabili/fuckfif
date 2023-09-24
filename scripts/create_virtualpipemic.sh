# Create virtual microphone
pactl load-module module-pipe-source source_name=VirtualPipeMic file=/tmp/VirtualPipeMic format=s16le rate=44100 channels=2
pacmd update-source-proplist VirtualPipeMic device.description=VirtualPipeMic
pacmd set-default-source VirtualPipeMic