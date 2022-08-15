from pyPS4Controller.controller import Controller
import pyautogui

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       pyautogui.press("x", interval=0.3)

    def on_triangle_press(self):
        pyautogui.press("w", interval=0.3)

    def on_square_press(self):
        pyautogui.press("c", interval=0.3)

    def on_circle_press(self):
        pyautogui.press("e", interval=0.3)

    def on_up_arrow_press(self):
        pyautogui.press("i", interval=0.3)

    def on_down_arrow_press(self):
        pyautogui.press(",", interval=0.3)

    def on_up_down_arrow_release(self):
        pyautogui.press("k", interval=0.3)

    def on_right_arrow_press(self):
        pyautogui.press("l", interval=0.3)

    def on_left_arrow_press(self):
        pyautogui.press("j", interval=0.3)

    def on_left_right_arrow_release(self):
        pyautogui.press("k", interval=0.3)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()