# micropython_espX_IR_Transceiver
micropython esp32  IR Transceiver


# how to use:
  # logIRCMD(time list) -> auto save to /buttomCMD.txt, i am use VS/HX1838B:
      from irGetCMD import *
      a = irGetCMD(25) # 25 is GPIO PIN number

  # get log code line -> json.loads -> get the listObject . 
      from irSelectCMD import *
      irCMDList = irSelectCMD(0) 

  # pwmObject
      import machine
      irLed = machine.Pin(16, machine.Pin.OUT) # 16 is GPIO PIN number
      irLedPwmObject = machine.PWM(irLed, freq=38000, duty=0)

  # ir send
      irSendCMD(irLedPwmObject, irCMDList, duty=360)
