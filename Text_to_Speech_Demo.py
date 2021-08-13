
import os
import gtts
""" 
Step1: Import Functionality (ex GTTS)
Step2:Call gTTS Constructor with Desired values
Step3: Save Data as Audio file 
Step4: Play Saved File   
"""
myText = "Hi Everyone, I hope you are learning some thing new in python. "
myData = gtts.gTTS(text=myText,lang='en',slow=False)
myData.save("MyData.mp3")
os.system("MyData.mp3")

