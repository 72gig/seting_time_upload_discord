# this program will copy screen and upload dc
# create  day 08/11/2024
# creator Lin Ming Xang

import time
import pyautogui
import os
import glob
import requests

FOLDER_PATH = r"C:\Users\User\Pictures\Screenshots"


def start():
    pass
    while True:
        # if (
        #    time.localtime(time.time()).tm_hour >= 9
        #    and time.localtime(time.time()).tm_hour < 14
        # ):
        if True:
            pass
            if time.localtime(time.time()).tm_min % 5 == 0:
                #  電腦要自動截圖
                print("we will run the upload")
                pyautogui.hotkey("printscreen")
                time.sleep(1)
                for i in range(3):
                    pyautogui.hotkey("tab")
                    time.sleep(0.1)
                pyautogui.hotkey("enter")
                time.sleep(0.1)
                for i in range(2):
                    pyautogui.hotkey("down")
                    time.sleep(0.1)
                pyautogui.hotkey("enter")
                time.sleep(1)
                upload_to_dc()
                pass
        elif time.localtime((time.time())).tm_hour >= 14:
            break
        print(
            "now time is "
            + str(time.localtime(time.time()).tm_hour)
            + ":"
            + str(time.localtime(time.time()).tm_min)
        )
        time.sleep(60)


def upload_to_dc():
    # 抓截圖的檔案到DC去

    focusPath = r"discordToken.txt"
    if not os.path.isfile(focusPath):
        open(focusPath, "w").close()  # 如果沒有則建立檔案
    focusToken = open(focusPath, "r").read()
    data = {
        "connent": "this stock image has upload complete",
        "username": "Python bot",
    }
    files = {}
    with open(str(get_image_path()), "rb") as imageFile:
        files = {"imageFile": ("image.png", imageFile)}
    response = requests.post(focusToken, data=data, files=files)  # 使用 POST 方法
    if response.status_code == 204:
        pass
    else:
        print("have something error in save image")
        print(response.text)
    pass


def get_image_path():
    pass
    files = glob.glob(os.path.join(FOLDER_PATH, "*"))
    if not files:
        return None
    latestFile = max(files, key=os.path.getctime)
    allPath = FOLDER_PATH + "\\" + latestFile
    return os.path.basename(allPath)


if __name__ == "__main__":
    start()
