#!/usr/bin/python

import smbus
import math
import time

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def is_carrying(x,y,z,counter):
    if counter == 0:
        return 0
    else:
        average_x = sum(x) /10
        average_y = sum(y) /10
        average_z = sum(z) /10
        
        x_determine = average_x - x[9]
        y_determine = average_y - y[9]
        z_determine = average_z - z[9]
        
        factor=40
        
        if x_determine > factor or y_determine > factor or z_determine > factor:
            return 1
        else:
            return 0

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

if __name__=="__main__":

    bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
    address = 0x68       # This is the address value read via the i2cdetect command
    x_outs=[0 for i in range(11)]
    y_outs=[0 for i in range(11)]
    z_outs=[0 for i in range(11)]
# Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(address, power_mgmt_1, 0)
    
    clock=0
    counter=0
    
    while 1:
        if clock ==10:
            counter=1
        clock=clock%10
        clock+=1
        
        time.sleep(0.1)

        gyro_xout = read_word_2c(0x43)
        gyro_yout = read_word_2c(0x45)
        gyro_zout = read_word_2c(0x47)
        
        #x_outs[clock]=gyro_xout
        #y_outs[clock]=gyro_yout
        #z_outs[clock]=gyro_zout
        
        x_outs=x_outs[1:10]
        x_outs.append(gyro_xout)
        
        y_outs=y_outs[1:10]
        y_outs.append(gyro_yout)

        z_outs=x_outs[1:10]
        z_outs.append(gyro_zout)

        
        print("carrying:")
        print(is_carrying(x_outs,y_outs,z_outs,counter))