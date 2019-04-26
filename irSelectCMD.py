import ujson
# how to use:
#   from irSelectCMD import *
#   irCMDList = irSelectCMD(0)

def irSelectCMD(ctrlNum, txtAddr="/buttomCMD.txt"):
    with open(txtAddr, "r", encoding="utf-8") as txt:
        n = 0
        for line in txt:
            if ctrlNum == n:
                lineDict = ujson.loads(line)
                return lineDict[str(n)]
            n += 1                
                
                