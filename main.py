'''Main class for creating the game'''
#Main imports
import sys
import time
import threading
import multiprocessing
import numpy as np
import warnings
#importing my custom scripts
import hardware
#from ai import Dqn
import basic_brain
import s_and_c

try:
    lvl_arg = sys.argv[1]
except:
    warnings.warn('couldnt find a level argument---> starting lvl0')
    lvl_arg = 'lvl0'


class MainGame:
    def __init__(self,level='lvl0'):
        self.bot = hardware.main_bot(level) #creating the robot object
        self.is_playing = False #help control if the game is currently running
        self.on_start() #calling on start function

    def on_start(self): #function thats called on initalization
        print('calling all functions before the game starts')
        self.bot.start() #calling the start function of the hardware
        self.is_playing = True #updating that we are playing now

    def on_end(self):
        self.is_playing = False
        print('/// ENDING THE GAME ///')
    def update(self):
        print('###UPDATE###')
        #take in the observation
        info = self.bot.get_sensor_info()

        #use a policy based of the action to make a decision
        direction = basic_brain.simple_policy(info)

        #chack if the user has quit otherwise do the specified action
        if info[2] == True:
            self.on_end()
        else:
            self.bot.action(direction)
            if direction == -1:
                self.on_end()


    def get_sleep_time(self):
        sleep_length = .1  # constant for how long the function should sleep
        next_call = time.time() # saving the current time
        self._last_sleep_time = next_call # creating debug var
        print('current time:',self._last_sleep_time)
        next_call += sleep_length #updating the next call based on how long you want it to sleep
        return next_call # add this to the update sleep
        #time.sleep(next_call - time.time())  # add this to main func to sleep until called

if __name__ == "__main__":
    game = MainGame(level = lvl_arg)

    while True:
        # wait for the game to start with a button press
        print('waiting to start the game')
        if game.is_playing == False: #waiting for game to start
            print('is_playing is false')
            time.sleep(5)
            print('###STARTING GAME####')
            game.on_start()
        else:
            print('STARTING GAME')
            while game.is_playing: #if game is started keep running this
                sleep_time = game.get_sleep_time()#getting the next sleep time for the function
                info = game.bot.get_sensor_info()
                print('info:\t',info) #prints the info
                game.update()
                time.sleep(sleep_time-time.time())
