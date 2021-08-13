"""
Step1 : Import package
Step2: use Function
Step3: Output
"""
import  gtts
from gtts import gTTS
import os

#googlr text to speech Converter

MyMessage1 = "Thank you Himanshi for attending this session of  Python, I appreciate your efforts. All the best for future  "

My_Value = gtts.gTTS(text= MyMessage1,slow=False,lang ='en')


My_Value.save("message2.Mp3")
os.system("message2.mp3")