from pynput import keyboard

def on_press(key):
    try:
        print(key.char, end='')
        #print('alphanumeric key {0} pressed'.format(
        #    key.char))
    except AttributeError:
        if key == keyboard.Key.enter:
            print()
            
        #print()
        #print('special key {0} pressed'.format(
        #    key))

def on_release(key):
    #print('{0} released'.format(
    #    key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()