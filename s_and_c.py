''' SOUND AND COLORS
This File controls all the colors and sounds of the game
'''
from gpiozero.tones import Tone
import threading
from time import sleep


def game_start_audio(bz): # audio played on startup
    delays = [.4,.2,.2,.4,.2,.4]
    notes = ['A3','A4','A3','B4','B3','C5']
    for i in range(len(delays)):
        note = notes[i]
        delay = delays[i]
        bz.play(Tone(note))
        sleep(delay)
    bz.stop()

def game_end_audio(bz):
    delays = [.4,.3,.2,.1,.3,.6]
    notes = ['A4','B4','D4']
    for i in range(len(delays)):
        note = notes[i]
        delay = delays[i]
        bz.play(Tone(note))
        sleep(delay)


def game_start_led(led):
    led.color = (1,0,0)
    sleep(1)
    led.color = (0,0,1)
    sleep(1)
    led.color = (0,1,0)
    sleep(1)


def game_pending_led(led):
    led.color = (1,1,1)
    led.blink()
    sleep(5)
    led.off()
