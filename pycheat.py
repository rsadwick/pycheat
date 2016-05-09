import pyscreenshot as ImageGrab
import os
import time
import win32api, win32con
from PIL import ImageChops

x_pad = 144
y_pad = 136


class Cords:

    top_left_cord = (65, 66)
    top_left_pixel = (63, 71, 70)
    top_right_cord = (213, 65)
    top_right_pixel = (67, 73, 73)
    b_50_cord = (138, 63)
    b_50_pixel = (164, 174, 172)
    b_40_cord = (143, 79)
    b_40_pixel = (169, 180, 183)
    b_30_cord = (136, 117)
    b_30_pixel = (1, 5, 2)
    b_20_cord = (136, 144)
    b_20_pixel = (0, 0, 0)
    b_10_cord = (136, 189)
    b_10_pixel = (0, 0, 0)


def detect_free_turn():
    image = screenGrab()

    if image.getpixel(Cords.top_left_cord) != Cords.top_left_pixel:
        btl()
    elif image.getpixel(Cords.top_right_cord) != Cords.top_right_pixel:
        btr()
    elif image.getpixel(Cords.b_50_cord) != Cords.b_50_pixel:
        b50()
    elif image.getpixel(Cords.b_40_cord) != Cords.b_40_pixel:
        b40()
    elif image.getpixel(Cords.b_30_cord) != Cords.b_30_pixel:
        b30()
    elif image.getpixel(Cords.b_20_cord) != Cords.b_20_pixel:
        b20()
    elif image.getpixel(Cords.b_10_cord) != Cords.b_10_pixel:
        b10()
    else:
        btl()

    time.sleep(3.9)
    detect_free_turn()


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print "click"


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print 'left Down'


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print 'left release'


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x, y


def screenGrab():
    box = (x_pad + 200, y_pad + 90, x_pad + 480, y_pad + 300)
    im = ImageGrab.grab(box)
    #im.show()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def get_diff(img1):
    box = (x_pad + 200, y_pad + 90, x_pad + 480, y_pad + 300)
    im2 = ImageGrab.grab(box)
    diff = ImageChops.difference(img1, im2)
    return diff


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def btr():
    mousePos((406, 36))
    time.sleep(1)
    leftDown()
    time.sleep(.1)
    mousePos((406, 190))
    leftUp()
    #time.sleep(4)
    #bowl()


def btl():
    mousePos((265, 36))
    time.sleep(1)
    leftDown()
    time.sleep(.2)
    mousePos((265, 220))
    leftUp()
    #time.sleep(4)
    #bowl()


def b40():
    mousePos((334, 36))
    time.sleep(1)
    leftDown()
    time.sleep(1)
    mousePos((334, 130))
    leftUp()


def b50():
    mousePos((332, 293))
    time.sleep(1)
    leftDown()
    time.sleep(.7)
    mousePos((332, 460))
    leftUp()


def b30():
    mousePos((336, 36))
    time.sleep(1)
    leftDown()
    time.sleep(1)
    mousePos((335, 105))
    leftUp()


def b20():
    mousePos((338, 219))
    time.sleep(1)
    leftDown()
    time.sleep(1)
    mousePos((335, 100))
    leftUp()


def b10():
    mousePos((333, 309))
    time.sleep(1)
    leftDown()
    time.sleep(.3)
    mousePos((335, 350))
    leftUp()


def startGame():
    #first menu
    mousePos((278, 335))
    leftClick()
    time.sleep(.1)

    #second menu
    mousePos((275, 513))
    leftClick()
    time.sleep(.1)

    #third
    mousePos((557, 581))
    leftClick()
    time.sleep(.1)

    mousePos((283, 504))
    leftClick()
    time.sleep(.1)





def main():
    pass


if __name__ == '__main__':
    main()