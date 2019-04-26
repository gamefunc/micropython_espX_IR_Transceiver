import machine
import utime
import micropython
import ujson
micropython.alloc_emergency_exception_buf(100)

# how to use:
#   from irGetCMD import *
#   a = irGetCMD(25) # 25 is GPIO PIN number


class irGetCMD(object):
    def __init__(self, gpioNum):
        self.irRecv = machine.Pin(gpioNum, machine.Pin.IN, machine.Pin.PULL_UP)

        self.irRecv.irq(
            trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING,
            handler=self.__logHandler)
        print("preir", self.irRecv.value())

        self.logList = [0 for x in range(1000)]
        self.index = 0
        self.start = 0

        self.dictKeyNum = 0
        self.irDict = {}

        self.__loop()

    def __logHandler(self, source):
        thisComeInTime = utime.ticks_us()
        if self.start == 0:
            self.start = thisComeInTime
            self.index = 0
            return

        self.logList[self.index] = utime.ticks_diff(thisComeInTime, self.start)
        self.start = thisComeInTime
        self.index += 1

    def __loop(self):
        while True:
            utime.sleep_ms(200)
            
            if utime.ticks_diff(
                    utime.ticks_us(),
                    self.start) > 800000 and self.index > 0:
                    
                thisIRcodeList = []

                n = 0
                for i in self.logList:
                    if (self.logList[n] == 0) and (self.logList[n +
                        1] == 0) and (self.logList[n +
                        2] == 0) and (self.logList[n +
                        3] == 0) and (self.logList[n +
                        4] == 0) and (self.logList[n +
                        5] == 0):
                        break
                    else:
                        thisIRcodeList.append(i)
                        n += 1
                print(thisIRcodeList, "\n")

                # append to buttomCMD.txt
                tmpDict = {}
                tmpDict[str(self.dictKeyNum)] = thisIRcodeList
                jsDump = ujson.dumps(tmpDict)
                with open("/buttomCMD.txt", "a", encoding="utf-8") as out:
                    out.write(jsDump + "\n")
                print("log ok %s; \n" % str(self.dictKeyNum))

                self.dictKeyNum += 1
                
                # reset 
                print("endir", self.irRecv.value())
                self.logList = [0 for x in range(1000)]
                self.index = 0
                self.start = 0
