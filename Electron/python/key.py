import keyboard
from time import sleep


def bind(action):
    if(action == 'play' or action == 'pause'):
        keyboard.press('space')
    elif(action == 'increase'):
        keyboard.press('up')
    elif(action == 'present'):
        keyboard.press('F5')
    elif(action == 'next'):
        keyboard.press('right')
    elif(action == 'previous'):
        keyboard.press('left')
    elif(action == 'escape'):
        keyboard.press('esc')
    elif(action == 'windows'):
        keyboard.press_and_release('windows')
    elif(action == 'ok'):
        keyboard.press('enter')
    elif(action == 'down'):
        keyboard.press_and_release('tab')
    elif(action == 'close'):
        keyboard.press_and_release('alt + F4')
    elif(len(action != 0)):
        # keyboard.press('p')
        # keyboard.press('o')
        # keyboard.press('w')
        # keyboard.press('e')
        # keyboard.press('r')
        # keyboard.press('p')
        # keyboard.press('o')
        # keyboard.press('i')
        # keyboard.press('n')
        # keyboard.press('t')
        # for i in action:
        #     keyboard.press_and_release(i)
        arr = list(action)
        print(arr)
        for i in arr:
            keyboard.press_and_release(i)