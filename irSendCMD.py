import machine
import utime
import micropython
micropython.alloc_emergency_exception_buf(100)

# how to use:
  # # logIrCMD(time list) -> auto save to /buttomCMD.txt:
      # from irGetCMD import *
      # a = irGetCMD(25) # 25 is GPIO PIN number

  # # get irRawCodeListObject
      # from irSelectCMD import *
      # irCMDList = irSelectCMD(0) 

  # # pwmObject
      # import machine
      # irLed = machine.Pin(16, machine.Pin.OUT) # 16 is GPIO PIN number
      # irLedPwmObject = machine.PWM(irLed, freq=38000, duty=0)

  # # ir send
      # irSendCMD(irLedPwmObject, irCMDList, duty=360)

def irSendCMD(pwmObject, ctrlList, duty=360):

    pwmObject.deinit()
    pwmObject.init()
    pwmObject.freq(38000)
    pwmObject.duty(0)
    utime.sleep_ms(100)

    ctrlListLen = len(ctrlList)

    for i in range(ctrlListLen):
        if i % 2 == 0:
            pwmObject.duty(duty)
        else:
            pwmObject.duty(0)
        utime.sleep_us(ctrlList[i])

    pwmObject.duty(0)

    utime.sleep_ms(100)


