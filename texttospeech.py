from gtts import gTTS 
import os, sys
from time import sleep  
# The text that you want to convert to audio 
os.system('mode con: cols=55 lines=20')
line_1 = '----------------------------------------------------'
line_2 = '----------Welcome to Text to Audio creator----------'
line_3 = '--Make sure you have an active internet connection--'
line_4 = '--Made with ♥ by Krishnendu - krishn3ndu@gmail.com--'

for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)
print('\n')
for x in line_2:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)
print('\n')
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)
print('\n')
for x in line_4:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)
print('\n')
print('\n')


f= open("input.txt","r")
text = f.read()
print('Your Input : ')

for x in text:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.01)
print('\n')

line_4 = "Please wait while I'm converting....."
for x in line_4:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)
  
# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=text, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
print('\n')
myobj.save("output.mp3") 
print("Converted Successfully....")
  
# Playing the converted file 
os.system("output.mp3")
print('If you have liked my work do give me a feedback at \nkrishn3ndu@gmail.com... ☺☻♥')
print('Exiting in 10 Seconds...')
sleep(10)