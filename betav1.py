from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import cv2
import pytesseract
from selenium import webdriver
from tkinter import filedialog
import time
import os
import io
import re
import time
import sys
import speech_recognition as sr
import pyttsx3
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient, operations
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes,VisualFeatureTypes
import requests
from PIL import Image,ImageDraw,ImageFont
window = tk.Tk()
width= window.winfo_screenwidth()               
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.configure(bg = 'Cyan')
window.title("V1.0")
msg = tk.Label(text = "Smart Google Form Assistant",font = ("Algerian",30),bg = 'Cyan')
msg.place(x=430,y=10)
w = Canvas(window, width=1325, height=30,bg='Cyan',highlightthickness=0)
w.create_line(15, 25, 10000, 25,width=2)
w.place(x=0,y=50)
title = Label(window, text = "Enter your Details and select the Input Format",font =("Algerian", 15),bg='Cyan')
title.place(x= 400,y=80)
fname = Label(window, text = "Enter address of Gform",font =("Times New Roman", 13),bg='Cyan')
fname.place(x = 5, y= 115)
#lname = tk.Label(text = "Last Name",font = ("Times New Roman",13),bg = 'LightSkyBlue2')
#lname.place(x=550, y= 110)
photo = PhotoImage(file = r"icon.png")
photoimage = photo.subsample(3, 3)
Button(window,image = photoimage,
                    compound = LEFT).pack(side = RIGHT)
global fentry
fentry = tk.Entry()
fentry.place(x= 180, y=115)
def getname():
    name = fentry.get()
    return name
form_name = getname()
print(form_name)
#lentry.place(x= 650, y=115)
#level=ttk.Combobox(window, width = 20,font=("Times New Roman",15))
#level.insert(END,'Select level')
#level['values']=('Easy','Medium','Hard','Randomn')
#level.place(x=1000,y=110)
def Image2():
    global render
    loc = insertpic()
    load= Image.open(r"loc")
    rload=load.resize((300,250))
    render = ImageTk.PhotoImage(rload)
    img = Label(window, image = render)
    img.place(x=10, y=200)
def voice_recognizer():  
    # Initialize the recognizer 
    r = sr.Recognizer()
    flag = True
    # Loop infinitely for user to speak
    while(flag):    
        try:    
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                  
                # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.1)
                  
                #listens for the user's input 
                audio2 = r.listen(source2)
                  
                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Did you say "+MyText)
                MyText = MyText.split()
                auto(MyText)
                flag = False
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
              
        except sr.UnknownValueError:
            print("unknown error occured")
 #dependent on the system       
def ocr():
    msg1 = tk.Label(text = "Waiting for result",font = ("Times New Roman",12),bg = 'Cyan')
    msg1.place(x = 630,y=210)
    API_KEY="9a638f9172384a8aa7649063fede7484"
    ENDPOINT="https://ocrdh512.cognitiveservices.azure.com/"
    computervision_client=ComputerVisionClient(ENDPOINT,CognitiveServicesCredentials(API_KEY))
    images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
    read_image_path = os.path.join (images_folder, "img.jpeg")
    root = tk.Tk() 
    root.withdraw() 
    file_path = filedialog.askopenfilename()
    read_image = open(file_path, "rb")
    response = computervision_client.read_in_stream(read_image,raw=True)
    operationlocation=response.headers['Operation-Location']
    operation_id=operationlocation.split('/')[-1]
    result=computervision_client.get_read_result(operation_id)
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status.lower () not in ['notstarted', 'running']:
            break
        print ('Waiting for result...')
        msg1.after(1000, msg1.destroy())
        time.sleep(10)
    p = []    
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)
                p.append(line.text)
                
    
    auto(p)
    

def auto(text):
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless") Use this and the following option to run Headless
#option.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path=r"chromedriver.exe", options=option)

    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfe4EtquGpr_yKtBF9G5OhkH6wTkFhY15JtYGCDDXUadePOZA/viewform?vc=0&c=0&w=1&flr=0")


# Use the following snippets to get elements by their class names
    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    heading = browser.find_element_by_class_name("freebirdFormviewerComponentsQuestionBaseTitleDescContainer")

# Use the following snippets to get elements by their XPath
    otherboxes = browser.find_element_by_xpath("/html/body")
    #print(str(textboxes[0]))
    for x in range(0,3):
        k = "".join(text[x])
        textboxes[x].send_keys(k)
        time.sleep(2)
    time.sleep(10)
 

def headnames():
    option = webdriver.ChromeOptions()
    p = []
    #option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
    browser = webdriver.Chrome(executable_path=r"C:\Users\Hrudai Aditya\Desktop\chromedriver", options=option)
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfe4EtquGpr_yKtBF9G5OhkH6wTkFhY15JtYGCDDXUadePOZA/viewform?vc=0&c=0&w=1&flr=0")
    heading = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseHeader")
    l = []
    for ele in heading:
        s = ele.get_attribute("innerHTML")
        l.append(s)
    for i in range(0,len(l)):
        s = l[i]
        y = s.find(r'/')
        x1 = s.find(">")
        x2 = s.find(">",x1+1)
        p.append((s[x2+1:y-1]))
    
    s = '\n'.join(p)
    title = Label(window, text = str(s),font =("Algerian", 15),bg='Cyan')
    title.place(x= 500,y=240)
                                                
        
#b6 = tk.Button(window,text = "Show Image",command = insertpic,bg = "pink")
b3 = tk.Button(window,text  = "Show headings", command = headnames,bg = "yellow" )
b4 = tk.Button(window,text  = "Photo", command = ocr,bg = "red" )
b5 = tk.Button(window,text  = "Voice", command = voice_recognizer,bg = "green" )
b3.place(x = 500, y = 170)
b4.place(x = 630, y = 170)
b5.place(x = 760, y = 170)
#b6.place(x = 800,y=170)

window.mainloop()
