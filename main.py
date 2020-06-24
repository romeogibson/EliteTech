from kivy.app import App
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.image import Image

from kivy.lang.builder import Builder
from kivy.uix. label import Label
import os
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, Animation, AnimationTransition
from kivy.core.window import Window



Window.clearcolor = (1,1,1,1)



class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass
class identifyWindow(Screen):
    pass

class wifi(Screen):
    pass

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class transfer(Screen):
    pass

class PCTs(Screen):
    pass

class pcRestart(Screen):
    pass

class winRestart(Screen):
    pass

class macRestart(Screen):
    pass

class modPlug(Screen):
    pass

class bypassRout(Screen):
    pass

class noResolve(Screen):
    pass

class bypassRout(Screen):
    pass

class checkAdapt1(Screen):
    pass

class ispRef(Screen):
    pass

class afterBoot(Screen):
    pass

class pcManu(Screen):
    pass

class macAdapt(Screen):
    pass


class MacBoy(ButtonBehavior, Image):
    pass

class BackButton(ButtonBehavior, Image):
    pass

class WindowsButton(ButtonBehavior, Image):
    pass

class MacButton(ButtonBehavior, Image):
    pass



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("elite.kv")

class elite(App):
    title= "Elite-Tech® Troubleshooter"
    def build(self):
        return kv




elite().run()