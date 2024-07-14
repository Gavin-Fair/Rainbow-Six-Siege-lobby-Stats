import pyscreenshot as ImageGrab
from pytesseract import pytesseract
from PIL import Image
import webbrowser
import keyboard
import os


def onPress():
    PLAYERS = []  # all the players in the lobby username's

    # starting bbox values to capture the first player on the second team
    X_ONE = 860
    X_TWO = 1325
    y1 = 335
    y2 = 400

    # capturing all the players usernames on the first team
    for i in range(1, 6):
        im = ImageGrab.grab(bbox=(X_ONE, y1, X_TWO, y2))  # X1,Y1,X2,Y2
        im.save(f'Player{i}.png')
        y1 += 72
        y2 += 72

    # setting the bbox's y1 and y2 values to capture first player on the second team
    y1 = 863
    y2 = 928

    # screenshotting all the players usernames on the second team
    for i in range(6, 11):
        im = ImageGrab.grab(bbox=(X_ONE, y1, X_TWO, y2))  # X1,Y1,X2,Y2
        im.save(f'Player{i}.png')
        y1 += 72
        y2 += 72

    # initializing the tesseract path
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tesseract

    # reading the user names from all the players and adding them to @PLAYERS
    for i in range(1, 11):
        image = Image.open(f'Player{i}.png')
        userName = pytesseract.image_to_string(image)
        if ' ' in userName:
            i = userName.index(' ')
            userName = userName[i + 1:]
        PLAYERS.append(userName.strip())  # use .strip() to strip '\n' from all usernames

    # opening chrome tab with each players stats using r6Tracker
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    i = 1
    for player in PLAYERS:
        webbrowser.get(chrome_path).open(f'https://r6.tracker.network/r6siege/profile/ubi/{player}/overview')
        os.remove(f'Player{i}.png')
        i += 1


# adding keyboard hotkey
keyboard.add_hotkey('tab+F1', onPress, suppress=True, trigger_on_release=True)
keyboard.wait()
