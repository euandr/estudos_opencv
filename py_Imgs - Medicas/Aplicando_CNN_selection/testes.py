# import cv2
# import glob


# base_path = r'C:\Users\andre\Downloads\archive\OvarianCancer\duas\\'

# rotulos=["Non_Cancerous","Endometri"]

# for rotulo in rotulos:
#     path = base_path+rotulo
#     images_list = glob.glob(path + '/*.jpg')

#     for item in images_list:
#         img = cv2.imread(item)





#                       passar slide
# import keyboard
# import pyautogui
# from time import sleep
# sleep(3)
# x, y = pyautogui.position()
# print(x,y)

# while True:

#     pyautogui.moveTo(997,1051)
#     pyautogui.click()
#     sleep(2)
#     if keyboard.is_pressed('f'):
#         break