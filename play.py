import os,time
from playsound import playsound


os.system("clear")

print("Scanning and adding frames to buffer...")
filenames = sorted(os.listdir("./txt_files"))

frames = []

for name in filenames:
    with open("./txt_files/"+name, "r", encoding="utf8") as f:
        frames.append(f.read())

#not really recommended because it depends on how fast your computer is.
#playsound('./audio.m4a', block=False)

for frame in frames:
    print(str(frame))
    time.sleep(0.029)
    os.system('clear')