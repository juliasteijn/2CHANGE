# Required packages

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivyauth.google_auth import initialize_google, login_google, logout_google
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.uix.tab import MDTabsBase
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
import pandas as pd
import random
import math

# This fabricated data replaces real transaction data for demonstration purposes
# For access to real transaction data, a PSD2 AISP license is required
random.seed(42)
bank_data = [round(random.uniform(0, 200), 2) for _ in range(100)]
data = {'Transaction data': bank_data}
df = pd.DataFrame(data)

#initiate calculation of the total collected change
#wallet_sum is going to be the total collected change
#multiple represents the multiple to which the customer wants their transactions to be rounded
    #i.e. multiple = 1 means that transactions are rounded up to the nearest euro, multiple = 2 means that transactions are rounded up to the nearest multiple of 2
wallet_sum = 0
multiple = 2

for i in range(0,len(df)):
    rounded = (math.ceil(df.iloc[i][0]))
    total = multiple * math.ceil(rounded/multiple)
    wallet_sum = wallet_sum+round((total - df.iloc[i][0]),2)

# Assuming that the investment return is 5% of invested money, return_sum calculated the total return
return_sum = round(wallet_sum*0.05,2)

# total_sum represents the total money available (for potential payout)
total_sum = return_sum+wallet_sum

kv = '''
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts
ScreenManager:
    id: screen_manager
    MDScreen:
        #this screen is the login screen, including a login button and the 2CHANGE logo
        name: "login"
        MDFloatLayout:
            md_bg_color: 253/255.,238/255.,199/255.,255/255.
            orientation: "vertical"
            Image:
                source: 'C:/Users/Julia/OneDrive/Documents/RSM BAM/Period 5/FinTech/Kivy_logo.jpg'
                size_hint: .5, .5
                pos_hint: {"center_x": 0.5,"center_y": 0.7}
            MDRaisedButton:
                text: "Login With Google"
                pos_hint: {"center_x": 0.5,"center_y": 0.3}
                on_release:app.login()
    MDScreen:
        #this is the main screen that is accessed after logging in, and shows the 3 main features: profile, education, and wallet
        name: "main"
        MDBoxLayout:
            orientation: "vertical"
            md_bg_color: 253/255.,238/255.,199/255.,255/255.
            MDTopAppBar:
                type: "top"
            MDBoxLayout:
                id: tabbox
                orientation: 'vertical'
                MDTabs:
                    id: tabs
                    on_tab_switch: app.on_tab_switch(*args)
                    Tab:
                        id: profile_tab
                        name: 'Profile'
                        title: "Profile"
                        text: "Profile"
                        MDFloatLayout:
                            BoxLayout:
                                Label:
                                    text: 'ESG responsible investing'
                                    color: 0, 0, 0, 1
                                    pos_hint: {"center_x": 0.3,"center_y": 0.7}
                                Switch:
                                    id: switch
                                    pos_hint: {"center_x": 0.75,"center_y": 0.7}
                                    active: True
                            MDLabel:
                                id: welcomelabel
                                text: ""
                                pos_hint: {"center_x": 0.3,"center_y": 0.9}
                                halign: "center"
                            MDRaisedButton:
                                text: "Logout"
                                pos_hint: {"center_x": 0.8,"center_y": 0.9}
                                on_release:app.logout()
                            BoxLayout:
                                Label:
                                    text: 'Risk profile'
                                    color: 0, 0, 0, 1
                                    pos_hint: {"center_x": 0.15,"center_y": 0.3}
                                CustomToggleButton:
                                    id: toggle_button_risk1
                                    text: "Low risk profile"
                                    group: 'risk'
                                    size_hint: 0.3, 0.1
                                    pos_hint: {"center_x": 0.65,"center_y": 0.3}
                                CustomToggleButton:
                                    id: toggle_button_risk2
                                    text: "Medium risk profile"
                                    group: 'risk'
                                    state: 'down'
                                    size_hint: 0.3, 0.1
                                    pos_hint: {"center_x": 0.75,"center_y": 0.3}
                                CustomToggleButton:
                                    id: toggle_button_risk3
                                    text: "High risk profile"
                                    group: 'risk'
                                    size_hint: 0.3, 0.1
                                    pos_hint: {"center_x": 0.85,"center_y": 0.3}
                    Tab:
                        id: education_tab
                        name: 'Education'
                        title: "Education"
                        text: "Education"
                        MDBoxLayout:
                            orientation: 'vertical'
                            MDTopAppBar:
                                type: "top"
                            MDBoxLayout:
                                id: tabeducation
                                orientation: 'vertical'
                                MDTabs:
                                    id: tabseducation
                                    on_tab_switch: app.on_tab_switch(*args)
                                    Tab:
                                        id: stocks
                                        name: 'stocks'
                                        title: "Stocks"
                                        MDFloatLayout:
                                            #cols: 1
                                            #size_hint_y: None
                                            #height: self.minimum_height
                                            orientation: "vertical"
                                            MDLabel:
                                                text: "Video resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.9}
                                            VideoPlayer:
                                                id: video
                                                source: "C:/Users/Julia/OneDrive/Documents/RSM BAM/Period 5/FinTech/FinTech_Pitch_497736JS_Steijn.mp4"
                                                state: "pause"
                                                allow_stretch: True
                                                size_hint: .5, .5
                                                pos_hint: {"center_x": 0.5,"center_y": 0.55}
                                            MDLabel:
                                                text: "Literature resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.2}
                                            MDRaisedButton:
                                                text:"Click here to open literature documentation"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.1}
                                                on_release:
                                                    import webbrowser
                                                    webbrowser.open('https://www.udemy.com/course/stock-market-trading/')
                                    Tab:
                                        id: bonds
                                        name: 'Bonds'
                                        title: "Bonds"
                                        MDFloatLayout:
                                            #cols: 1
                                            #size_hint_y: None
                                            #height: self.minimum_height
                                            orientation: "vertical"
                                            MDLabel:
                                                text: "Video resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.9}
                                            VideoPlayer:
                                                id: video
                                                source: "C:/Users/Julia/OneDrive/Documents/RSM BAM/Period 5/FinTech/FinTech_Pitch_497736JS_Steijn.mp4"
                                                state: "pause"
                                                allow_stretch: True
                                                size_hint: .5, .5
                                                pos_hint: {"center_x": 0.5,"center_y": 0.55}
                                            MDLabel:
                                                text: "Literature resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.2}
                                            MDRaisedButton:
                                                text:"Click here to open literature documentation"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.1}
                                                on_release:
                                                    import webbrowser
                                                    webbrowser.open('https://www.investor.gov/introduction-investing/investing-basics/investment-products/bonds-or-fixed-income-products/bonds')

                                    Tab:
                                        id: crypto
                                        name: 'Crypto'
                                        title: "Crypto"
                                        MDFloatLayout:
                                            #cols: 1
                                            #size_hint_y: None
                                            #height: self.minimum_height
                                            orientation: "vertical"
                                            MDLabel:
                                                text: "Video resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.9}
                                            VideoPlayer:
                                                id: video
                                                source: "C:/Users/Julia/OneDrive/Documents/RSM BAM/Period 5/FinTech/FinTech_Pitch_497736JS_Steijn.mp4"
                                                state: "pause"
                                                allow_stretch: True
                                                size_hint: .5, .5
                                                pos_hint: {"center_x": 0.5,"center_y": 0.55}
                                            MDLabel:
                                                text: "Literature resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.2}
                                            MDRaisedButton:
                                                text:"Click here to open literature documentation"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.1}
                                                on_release:
                                                    import webbrowser
                                                    webbrowser.open('https://www.udemy.com/course/cryptomeister-a-complete-cryptocurrency-investment-course/')
                                    Tab:
                                        id: nft
                                        name: 'NFTs'
                                        title: "NFTs"
                                        MDFloatLayout:
                                            #cols: 1
                                            #size_hint_y: None
                                            #height: self.minimum_height
                                            orientation: "vertical"
                                            MDLabel:
                                                text: "Video resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.9}
                                            VideoPlayer:
                                                id: video
                                                source: "C:/Users/Julia/OneDrive/Documents/RSM BAM/Period 5/FinTech/FinTech_Pitch_497736JS_Steijn.mp4"
                                                state: "pause"
                                                allow_stretch: True
                                                size_hint: .5, .5
                                                pos_hint: {"center_x": 0.5,"center_y": 0.55}
                                            MDLabel:
                                                text: "Literature resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.2}
                                            MDRaisedButton:
                                                text:"Click here to open literature documentation"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.1}
                                                on_release:
                                                    import webbrowser
                                                    webbrowser.open('https://www.udemy.com/course/nft-course-for-absolute-beginners/')
                                    Tab:
                                        id: realestate
                                        name: 'Real Estate'
                                        title: "Real Estate"
                                        MDFloatLayout:
                                            #cols: 1
                                            #size_hint_y: None
                                            #height: self.minimum_height
                                            orientation: "vertical"
                                            MDLabel:
                                                text: "Video resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.9}
                                            VideoPlayer:
                                                id: video
                                                source: "C:/Users/Julia/OneDrive/Documents/RSM BAM/Period 5/FinTech/FinTech_Pitch_497736JS_Steijn.mp4"
                                                state: "pause"
                                                allow_stretch: True
                                                size_hint: .5, .5
                                                pos_hint: {"center_x": 0.5,"center_y": 0.55}
                                            MDLabel:
                                                text: "Literature resource"
                                                halign: "center"
                                                font_size: "24sp"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.2}
                                            MDRaisedButton:
                                                text:"Click here to open literature documentation"
                                                pos_hint: {"center_x": 0.5,"center_y": 0.1}
                                                on_release:
                                                    import webbrowser
                                                    webbrowser.open('https://www.udemy.com/course/how-to-raise-capital-and-invest-in-crowd-fund-real-estate/')                    
                    Tab:
                        id: wallet_tab
                        name: 'Wallet'
                        title: "Wallet"
                        text: "Wallet"
                        MDFloatLayout:
                            MDLabel:
                                id: changelabel
                                text: ""
                                pos_hint: {"center_x": 0.5,"center_y": 0.9}
                                halign: "center"
                                font_size: "24sp"
                            MDLabel:
                                id: returnlabel
                                text: ""
                                pos_hint: {"center_x": 0.5,"center_y": 0.8}
                                halign: "center"
                                font_size: "24sp"
                            MDLabel:
                                id: walletlabel
                                text: ""
                                pos_hint: {"center_x": 0.5,"center_y": 0.7}
                                halign: "center"
                                font_size: "24sp"

'''

class MainScreen(Screen):
    pass

class CustomToggleButton(ToggleButton):
    pass

class Tab(BoxLayout, MDTabsBase):
    pass

class ScrollableLabel(ScrollView):
    pass

# Creating the main application by building the kv string
# Theme colors of the app are defined based on the company logo's colors
class TWOCHANGE(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.accent_hue = "700"
        client_id = open('client_id.txt')
        client_secret = open('client_secret.txt')
        initialize_google(self.after_login, self.error_listener, client_id.read(), client_secret.read())
        return Builder.load_string(kv)

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.
        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        self.root.ids.changelabel.text = f"Total change invested €{wallet_sum}"
        self.root.ids.returnlabel.text = f"Total return generated €{return_sum}"
        self.root.ids.walletlabel.text = f"Total money in wallet €{total_sum}"

    def after_login(self, name, email, photo_uri):
        self.root.ids.welcomelabel.text = f"Welcome to your 2CHANGE profile, {name}"
        self.root.transition.direction = "left"

        self.root.current = "main"

    def error_listener(self):
        print("Login Failed!")

    def login(self):
        login_google()

    def logout(self):
        logout_google(self.after_logout)

    def after_logout(self):
        self.root.ids.welcomelabel.text = ""
        self.root.transition.direction = "right"
        self.root.current = "login"

if __name__ == '__main__':
    TWOCHANGE().run()