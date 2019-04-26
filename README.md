# micropython_espX_IR_Transceiver
micropython esp32 esp8266  IR Transceiver


# how to use:
#   # logIrCMD(time list) -> auto save to /buttomCMD.txt:
#       from irGetCMD import *
#       a = irGetCMD(25) # 25 is GPIO PIN number
#
#   # get irRawCodeListObject
#       from irSelectCMD import *
#       irCMDList = irSelectCMD(0) 
#
#   # pwmObject
#       import machine
#       irLed = machine.Pin(16, machine.Pin.OUT) # 16 is GPIO PIN number
#       irLedPwmObject = machine.PWM(irLed, freq=38000, duty=0)
#
#   # ir send
#       irSendCMD(irLedPwmObject, irCMDList, duty=360)
