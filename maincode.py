from pygame import mixer
import time
mixer.init()
mixer.music.load("C:\\Users\\mudit\\Downloads\\water.mp3.mp3")   #you have to add the path for your music file which you want to play
print("Playing music")
mixer.music.play()
time.sleep(4)
print("Stopping music")
mixer.music.stop()
