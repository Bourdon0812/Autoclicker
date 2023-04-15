from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
from time import sleep

click = Controller()
click.position = (300, 400)

active = Key.f2
running = False


def on_press(key):
    '''
    :param key:
    :return: void
    '''
    global active, running
    if key == active:
        if not running:
            running = True
            start()
        else:
            running = False


def start():
    '''

    :return: void
    '''
    global running, click
    while running:
        click.press(Button.left)
        click.release(Button.left)
        sleep(0.2)


def main():
    '''

    :return: void
    '''
    event = Listener(on_press=on_press)
    event.start()


while 0 < 1:
    sleep(1)
    main()
