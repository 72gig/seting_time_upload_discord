# this program will copy screen and upload dc
# upload to github in 2025
# create  day 08/11/2024
# creator Lin Ming Xang

import time
import pyautogui
import os
import glob
import requests
import argparse

FOLDER_PATH = r"screenData"
SCREEN_TIMES = 1
TIME_SETTING = 5


def start():
    pass
    while True:
        if (
            time.localtime(time.time()).tm_hour >= 8
            and time.localtime(time.time()).tm_hour <= 13
        ):
            # if True:
            if (
                time.localtime(time.time()).tm_hour == 13
                and time.localtime(time.time()).tm_min >= 31
            ):
                break
            # pass
            if (
                time.localtime(time.time()).tm_min % TIME_SETTING == 0
                and time.localtime(time.time()).tm_sec == 0
            ):
                #  電腦要自動截圖
                print("we will run the upload")

                # 一次截全部太大會有解析度問題
                # 應情況分開截
                for i in range(SCREEN_TIMES):
                    os.makedirs("screenData", exist_ok=True)
                    screenshot = pyautogui.screenshot()
                    screenName = (
                        r"screenData\\"
                        + str(time.localtime(time.time()).tm_year)
                        + "_"
                        + str(time.localtime(time.time()).tm_mon)
                        + "_"
                        + str(time.localtime(time.time()).tm_mday)
                        + "_"
                        + str(time.localtime(time.time()).tm_hour)
                        + "_"
                        + str(time.localtime(time.time()).tm_min)
                        + str(time.localtime(time.time()).tm_sec)
                        + r"_screen.png"
                    )
                    screenshot.save(screenName)
                    upload_to_dc()
                    pass
                    if SCREEN_TIMES != i + 1:
                        # 換到下一個畫面
                        switch_desktop("right")
                        time.sleep(1)

                # 畫面截完要換回來
                if SCREEN_TIMES != 1:
                    for i in range(SCREEN_TIMES):
                        switch_desktop("left")
                        time.sleep(1)
        elif time.localtime((time.time())).tm_hour >= 14:
            break
        print(
            "now time is "
            + str(time.localtime(time.time()).tm_hour)
            + ":"
            + str(time.localtime(time.time()).tm_min)
            + ":"
            + str(time.localtime(time.time()).tm_sec)
            + " sleep until next "
            + str(TIME_SETTING)
            + " min"
        )
        time.sleep(0.9)


def upload_to_dc():
    # 抓截圖的檔案到DC去
    # DC 需要聊天室的 TOKEN 才能夠傳上去
    focusPath = r"discordToken.txt"
    if not os.path.isfile(focusPath):
        open(focusPath, "w").close()  # 如果沒有則建立檔案
    focusToken = open(focusPath, "r").read()
    data = {
        "connent": "this stock image has upload complete",
        "username": "Python bot",
    }
    with open(str(get_image_path()), "rb") as imageFile:
        files = {"imageFile": ("image.png", imageFile)}
        response = requests.post(focusToken, data=data, files=files)  # 使用 POST 方法
        if response.status_code == 204 or response.status_code == 200:
            pass
        else:
            print("have something error in save image")
            print(response.status_code)
    pass


def get_image_path():
    pass
    files = glob.glob(os.path.join(FOLDER_PATH, "*"))
    if not files:
        return None
    latestFile = max(files, key=os.path.getctime)

    return latestFile


def shot_time_check():
    global SCREEN_TIMES
    global TIME_SETTING
    parser = argparse.ArgumentParser(description="setting times that I need screenshot")
    parser.add_argument("-S", type=int, help="set int type for screenshot times")
    parser.add_argument("-T", type=int, help="set int type for screenshot delay min")

    args = parser.parse_args()

    if args.S is not None:
        SCREEN_TIMES = args.S
    if args.T is not None:
        TIME_SETTING = args.T
    pass


def switch_desktop(var):
    pyautogui.keyDown("win")
    pyautogui.keyDown("ctrl")

    pyautogui.press(var)

    pyautogui.keyUp("win")
    pyautogui.keyUp("ctrl")


if __name__ == "__main__":
    shot_time_check()
    start()
