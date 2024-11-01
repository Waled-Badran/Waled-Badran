from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager



Window.size=(400,500)
Window.clearcolor =(0,0,.5,0)

Builder.load_string('''
<MainScreen>:
    RelativeLayout:
        orientation: 'vertical'
        Button:
            text: 'Vodafone' 
            size_hint:0.3,0.1
            pos:(120,400)
            color:(1,0,0)                        
            on_press: root.manager.current = 'interNumber'                 
        Button:
            text: 'Orange'
            size_hint:0.3,0.1
            pos:(120,300)
            color:(1, 0.647, 0)        
        Button:
            text:" close"
            size_hint:0.3,0.1
            pos:(120,100)
            on_press:  command=close_program 
<InterNumber>:                   
    RelativeLayout: 
        orientation: 'vertical'          
        TextInput:  
            id: phone_input  
            hint_text: 'input your number'  
            size_hint: 0.6, 0.1  
            pos: (120, 300)  
        Button:  
            text: ' save number'  
            size_hint: 0.3, 0.1  
            pos: (120, 200)  
            on_press: app.store_phone_number(phone_input.text)  
        Button:  
            text: 'Go'  
            size_hint: 0.3, 0.1  
            pos: (120, 100)  
            on_press: root.manager.current = 'vodafonelist'                    
<VodafoneListScreem>:
    RelativeLayout:
        orientation: 'vertical'                                 
        Button:
            text:'cach' 
            size_hint:0.3,0.1
            pos:(120,400)             
        Button:
            text: 'renewal'
            size_hint:0.3,0.1
            pos:(120,250)        
            on_press: root.manager.current = 'charg'          
        Button:
            text: 'back'
            size_hint:0.3,0.1
            pos:(120,100)
            on_press: root.manager.current = 'main'        
<ChargList>:
    RelativeLayout:
        orientation: 'vertical'
        Button:
            text:'flex'
            size_hint:0.3,0.1
            pos:(120,400)
            on_press: root.manager.current = 'FlexList'                 
        Button:
            text: 'Second'
            size_hint:0.3,0.1
            pos:(120,250)          
        Button:
            text: 'back'
            size_hint:0.3,0.1
            pos:(120,100)          
            on_press: root.manager.current = 'vodafonelist'                                                                                                    
        Button:
            text: 'back to main'
            size_hint:0.3,0.1
            pos:(120,20)          
            on_press: root.manager.current = 'main'          
<FlexList>:
    RelativeLayout:
        orientation: 'vertical'                                 
        Button:
            text:'Flex30' 
            size_hint:0.3,0.1
            pos:(120,410)
            on_press: app.open_call_app('*30#')                                 
        Button:
            text:'Flex45' 
            size_hint:0.3,0.1
            pos:(120,310) 
        Button:
            text:'Flex70' 
            size_hint:0.3,0.1
            pos:(120,210) 
        Button:
            text:'Flex100' 
            size_hint:0.3,0.1
            pos:(120,110) 
        Button:
            text:'flex200' 
            size_hint:0.3,0.1
            pos:(120,20) 

''')
class MainScreen(Screen):
    pass
class VodafoneListScreem(Screen):
    pass
class ChargList(Screen):
    pass
class FlexList(Screen):
    pass
class InterNumber(Screen):
    pass
class phonApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(VodafoneListScreem(name='vodafonelist'))
        sm.add_widget(ChargList(name='charg'))
        sm.add_widget(FlexList(name='FlexList'))
        sm.add_widget(InterNumber(name='interNumber'))
        return sm
    
    def store_phone_number(self, phone_number):  
        self.user_phone = phone_number  # تخزين الرقم المدخل  
        print(f"تم تخزين الرقم: {self.user_phone}")  # يمكنك إظهار رسالة للمستخدم هنا  

   



if __name__ == '__main__':
    phonApp().run()
