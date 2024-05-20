import keyboard
import uuid
import time
from PIL import Image
from mss import mss

# "https://www.trex-game.skipser.com/"

mon = {"top": 505, "left": 655, "width": 300, "height": 130}  #önündeki katüsün dinazordan uzaklığınınn kordinatları
sct = mss() #reo yu kesip frame dönüşütrecek olan kütüüphane

i = 0

def record_screen(record_id, key):
    global i

    i+=1
    print("{}: {}:".format(key,i)) #key basma tuşu, i kaç kere bastığımız
    img = sct.grab(mon)
    im = Image.frombytes("RGB", img.size, img.rgb)
    im.save("trex/img/{}_{}_{}.png".format(key,record_id,i))


is_exit = False

def exit():
    global is_exit
    is_exit = True

keyboard.add_hotkey("esc", exit)
record_id = uuid.uuid4()

while True:
    if is_exit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            record_screen(record_id, "up")
            time.sleep(0.1)

        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            record_screen(record_id, "down")
            time.sleep(0.1)

        elif keyboard.is_pressed("right"):
            record_screen(record_id, "right")
            time.sleep(0.1)

    except RuntimeError: continue
