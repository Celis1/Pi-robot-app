'''Initializing the gpio pins for the pi
started: 7/22/2020
 '''
#gpiozero imports
from gpiozero import Robot,RGBLED,MCP3008
from gpiozero import DistanceSensor,RGBLED,TonalBuzzer
#importing the Tones
from gpiozero.tones import Tone
#importing my own file
import s_and_c #probably not needed in this script

#in case need to cancel the signal
from signal import pause
from time import sleep

#other imports
import warnings

#setting constants of gpio pins hardware is connected to
MOTOR_L = (5,6)
MOTOR_R = (16,26)
SONIC_TRIG = 23
SONIC_ECHO = 25
IR_L = 0
IR_R = 1
BTN = 3
BZ = 24
R,G,B = 22,27,17

class main_bot:
    def __init__(self,level='lvl0'):
        #instantiating all the motors and sensors on the bot
        self.robot = Robot(left = MOTOR_L,right = MOTOR_R)
        self.sonic = DistanceSensor(echo = SONIC_ECHO, trigger = SONIC_TRIG)
        self.ir_l = MCP3008(IR_L)
        self.ir_r = MCP3008(IR_R)
        self.button = MCP3008(BTN)
        self.bz = TonalBuzzer(BZ)
        self.led = RGBLED(R,G,B)
        #creating custom variables
        self.speed = self.get_speed(level)
        
    def get_sensor_info(self):
        #getting the the sonic info
        self.sonic_info = self.sonic.distance*100
        #getting both ir values and putting it into a tuple
        self.ir_info = (0 if self.ir_l.value == 1 else 1,
        0 if self.ir_r.value == 1 else 1)
        #getting the button value and storing it
        self.button_info = 1 if self.button.value == 1 else 0
        #returning a tuple of the info
        return (self.sonic_info,self.ir_info,self.button_info)

    def get_speed(self,level):
        default_speed = .4
        lvl_dict = { #creating the levels and corrispondoing speeds
        '0': default_speed,
        '1':.5,
        '2':.6,
        '3':.7,
        '4':.8,
        '5':1
        }

        if len(level) == 4: #checking to see if level is written as lvl<int>
            lvl = level[-1] #gets the last str
            try: #tries to return a value within the dict
                return lvl_dict[lvl] #returns the value associated with the key lvl
            except: #if the value selected wasnt in the dictionary
                warnings.warn('the selected lvl doesnt exists, defaulting to lvl0')
                return default_speed
        else:
            #creates a warning of missmatching vals and returns default speed
            warnings.warn('len(level)!=4, resulting to DEFAULT SPEED')
            return default_speed

    def start(self): #starts the robot motors with selected speed
        print('##### starting the motors #####')
        sleep(3)
        self.robot.forward(self.speed)


    def action(self,value): #function that controls the turn
        #checking the value of action and either turning, go forward or stopping
        if value == 0:
            self.robot.forward(self.speed)
        elif value == 1:
            self.robot.left(self.speed)
        elif value == 2:
            self.robot.right(self.speed)
        elif value == -1:
            self.robot.stop()
        else:
            raise ValueError('The Hardware.action value was not 0, 1 or 2 or -1')


    def _test_sensors(self): #testing all the sensors
        #initalizing all the gpio pins
        for _ in range(120):
            #printing all the values of the sensors
            print('SONIC: {}\t IR_LEFT: {}\t IR_RIGHT: {}\t \
             BUTTON: {}'.format(self.sonic.distance*100,
             self.ir_l.value,self.ir_r.value,self.button.value))
            sleep(.5)

    def _test_motors(self): #testing motors
        print('testing motors')
        self.robot.left(self.speed)
        sleep(1)
        self.robot.right(self.speed)
        sleep(1)

    def _test_audio(self): #testing audio
        print('testing audio')
        self.bz.play('A4')
        sleep(.2)
        self.bz.stop()

    def _test_audio_import(self):
        print('testing audio import')
        s_and_c.game_start_audio(self.bz)

    def _test_led_import(self):
        print('testing led')
        s_and_c.game_start_led(self.led)

if __name__ == "__main__": #only used for debugging purposes
    print('this script was run \n ######## STARTING INITIALIZATION...')
    sleep(.3)

    bot = main_bot()
    #bot.test_motors()
    #print('ENDING MOTOR TEST')
    #bot.stop()
    #print('###TESTING SENSOR###')
    #bot._test_sensors()
    for _ in range(150):
        info = bot.get_sensor_info()
        print(info)
        sleep(.3)
    print('testing audio import')
    bot._test_audio_import()
    print('ending audio')

    print('testing led')
    bot._test_led_import()
    print('ending led test')
