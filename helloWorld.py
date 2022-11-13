import pyautogui as gui
import pydirectinput
import json
from time import sleep


cards = []


# x 896, y 386
# x 1383, y 386

# x 896, y 589
# x 1383, y 589
# region=(left,top,width,height)
# x effect: (958,543,70,50)
# support : (1233,386,100,80)
# print(gui.position())

# click epsxe window
gui.click(611, 315)
i = 0
while (True):
    card = {
    "number": "",
    "x_speed": "0",
    "support_speed": "0",
    }
    pydirectinput.press('space')
    sleep(1)
    card['number'] = i

    # locate x effect
    for j in range(3):
        number = str(j + 1)
        image = "images/effect" + number + ".png"
        x_effect_location = gui.locateOnScreen(image, region=(958,543,70,50), confidence=0.5)
        if (x_effect_location is not None):
            # 0:none, 1:slow, 2:normal:, 3:fast
            card['x_speed'] = number
            break
    # locate support effect
    for j in range(3):
        number = str(j + 1)
        image = "images/effect" + number + ".png"
        support_location = gui.locateOnScreen(image, region=(1233,386,100,80), confidence=0.5)
        if (support_location is not None):
            card['support_speed'] = number
            break

    
    pydirectinput.press('backspace')
    pydirectinput.press('down')
    i += 1
    
    cards.append(card)
    result = {"cards": cards}

    # write effect cards Python list dict to JSON file
    with open("result.json", "w") as f:
        json.dump(result, f, indent=2)