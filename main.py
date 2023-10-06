from logging import root
import kivymd
from kivymd import *
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import MDList
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemableBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView, MapSource
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior, RectangularElevationBehavior, RectangularRippleBehavior 
from kivymd.uix.card import MDCard
from os.path import join, dirname
class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    '''Implements a material design v3 card.'''

    text = StringProperty()
class ContentScreen(Screen):
    pass
class InicioScreen(Screen):
    pass
class ConfiguracionScreen(Screen):
    pass
class ContactoScreen(Screen):
    pass
class AcercaDeScreen(Screen):
    pass
class AppScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class InformacionScreen(Screen):
    pass
class Dis_AuditivaScreen(Screen):
    pass
class Dis_ComunicativaScreen(Screen):
    pass
class Dis_FisicaScreen(Screen):
    pass
class Dis_VisualScreen(Screen):
    pass
class AyudaScreen(Screen):
    pass
class Pais_CostaRicaScreen(Screen):
    pass
class Pais_GuatemalaScreen(Screen):
    pass
class Pais_PanamaScreen(Screen):
    pass
class Pais_RepublicaDominicanaScreen(Screen):
    pass
class ComunidadScreen(Screen):
    pass
class LugaresScreen(Screen):
    pass
class Pais_Lugares_CostaRicaScreen(Screen):
    pass
class Pais_Lugares_GuatemalaScreen(Screen):
    pass
class Pais_Lugares_PanamaScreen(Screen):
    pass
class Pais_Lugares_RepublicaDominicanaScreen(Screen):
    pass
class ForoScreen(Screen):
    pass
class ItemDrawer(OneLineIconListItem): 
    icon = StringProperty()
class ContentNavigationDrawer(BoxLayout):
    pass
class MyCard(RectangularElevationBehavior, RectangularRippleBehavior, FloatLayout):
    ripple_scale = 1.4
    text = StringProperty()
    text_label = StringProperty()
class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
class generisapp(MDApp):
    title = "Generis"
    estado_asistente = 1
#Esta funcion solicita un nombre de archivo y nos retornara una ruta completa para acceder al archivo, dependiendo de la plataforma en la que se este ejecutando la app nos retornara la ruta para el archivo adecuado
    def on_start(self):
        icons_item = {
            "home": "Inicio",
            "phone-message": "Contacto",
            "cog": "Configuración",
            "information-variant": "Acerca de",
            "power": "Salir",
        }
        for icon_name in icons_item.keys():
            self.root.ids.appscreen.ids.md_list.add_widget(ItemDrawer(icon=icon_name, text=icons_item[icon_name]))
    def showtext(self, txtfile):
        with open(self.ruta(txtfile),"r") as f:
            filetext = f.read()
        return filetext
    def back_to_appscreen(self):
        self.root.current = "AppScreen"
        self.root.ids.appscreen.ids.nav_drawer.set_state("toggle")
    def call_drawerlist_menuderecho(self, button):   
        if button.icon == "book-information-variant":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_informacion.current = "InformacionScreen"
        elif button.icon == "phone-message":
            self.root.current = "ContactoScreen"
        elif button.icon == "cog":
            self.root.current = "ConfiguracionScreen"
        elif button.icon == "information-variant":
            self.root.current = "AcercaDeScreen"
        elif button.icon == "power":
            self.stop()
    def call_btnspeeddial_informacion(self, button):
        if button.icon == "book-information-variant":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_informacion.current = "InformacionScreen"
        elif button.icon == "ear-hearing":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_informacion.current = "Dis_AuditivaScreen"
        elif button.icon == "account-question":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_informacion.current = "Dis_ComunicativaScreen"
        elif button.icon == "wheelchair-accessibility":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_informacion.current = "Dis_FisicaScreen"
        elif button.icon == "eye":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_informacion.current = "Dis_VisualScreen"
    def call_btnspeeddial_ayuda(self, button):
        if button.icon == "account-question":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_ayuda.current = "AyudaScreen"
        elif button.icon == str(self.ruta("images/CR.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_ayuda.current = "Pais_CostaRicaScreen"
        elif button.icon == str(self.ruta("images/GT.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_ayuda.current = "Pais_GuatemalaScreen"
        elif button.icon == str(self.ruta("images/PA.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_ayuda.current = "Pais_PanamaScreen"
        elif button.icon == str(self.ruta("images/DO.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_ayuda.current = "Pais_RepublicaDominicanaScreen"
    def call_btnspeeddial_lugares(self, button):
        if button.icon == "map-marker-radius":
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_lugares.current = "LugaresScreen"
        elif button.icon == str(self.ruta("images/CR.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_lugares.current = "Pais_Lugares_CostaRicaScreen"
        elif button.icon == str(self.ruta("images/GT.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_lugares.current = "Pais_Lugares_GuatemalaScreen"
        elif button.icon == str(self.ruta("images/PA.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_lugares.current = "Pais_Lugares_PanamaScreen"
        elif button.icon == str(self.ruta("images/DO.png")):
            self.root.ids.appscreen.ids.inicio_screen.ids.screen_manager_lugares.current = "Pais_Lugares_RepublicaDominicanaScreen"
    def ruta(self, nombre_archivo):
            curdir = dirname(__file__)
            ruta_completa = join(curdir, 'resources/', nombre_archivo)
            return ruta_completa

    ############################################
#Esta funcion permite mantener la app abierta aunque salgamos de ella, en android
    def on_pause(self):
        return True  
#Ejecuta la app
if __name__ == '__main__':
    generisapp().run() 