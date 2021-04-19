''' this is the basic brain. that returns the direction the robot should be taking
No ai in this script
'''
import random

def get_action(sensor_data):
    ''' takes in the sensor data and returns an action to take '''
    pass

def simple_policy(sensor_data):
    #constants for taking in sensor sensor data
    history = 5 # some value for how far back in the srray we wanna look back
    sonic = sensor_data[0]
    ir_l =sensor_data[1][0]
    ir_r = sensor_data[1][1]
    btn = sensor_data[2]

    sonic_range = 16
    direction = 1

    #creating a scenario for if the sonic sees something first
    if sonic <= sonic_range:
        if ir_l == 0 and ir_r == 0: #nothing on either side of it
            return random.randint(1,2)
        elif ir_l == 1 and ir_r ==0: #something on its left side
            return 2
        elif ir_l == 0 and ir_r ==1: #something on its right side
            return 1

    #creating a scenario for if the ir_l sees something first
    if ir_l == 1:
        if sonic < sonic_range and ir_r == 1: #nothing in front of it
            return random.randint(1,2)
        elif ir_r == 0: #nothing on its right
            return 2
        elif sonic > sonic_range: #nothing in fr
            return 0



    #creating a scenario for if the ir_r sees something first
    if ir_r == 1:
        if sonic < sonic_range and ir_left == 1: #if something is infront of it
            return random.randint(1,2)
        elif ir_l == 0: #nothing in its left
            return 1
        elif sonic > sonic_range: #nothing infront of it
            return 0


    if btn == 1: #if the button to end was called
        return -1

    return 0
