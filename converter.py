from asciier import main

# main('./aaaa.png','one.txt')
# main('./test.jpg','two.txt')

import os

files = os.listdir("./imgs")

for file in files:
    main("imgs/"+file,file[0:len(file)-4]+".txt")
    