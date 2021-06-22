from kivy.app import App
from kivy.uix.label import Label
import operator
import speech_recognition as s_r
from gtts import gTTS 
import os

class Program(App):
    def build(self):
        r = s_r.Recognizer()
        my_mic_device = s_r.Microphone(device_index=1)
        with my_mic_device as source:  
            yazi = Label(text="işlemizzin Sonucu : ")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            my_string=r.recognize_google(audio, language="tr-tr") 

            

            
            
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            my_string=r.recognize_google(audio, language="tr-tr")
            def get_operator_fn(op):
                return {
                    'art' : operator.add,
                    'eksi' : operator.sub, 
                    'kere' : operator.mul,
                    'bölüm' : operator.truediv,
                    'Mod' : operator.mod,
                    '^' : operator.xor, 
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            yazi = Label(text="işlemizzin Sonucu : " + str(eval_binary_expr(*(my_string.split()))))
        
        

        
        tts = gTTS(text=str(eval_binary_expr(*(my_string.split()))), lang='tr')
        tts.save("merhaba.mp3")
        os.system("merhaba.mp3") 

        return yazi


Program().run()