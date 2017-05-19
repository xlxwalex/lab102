#梅森旋转算法   -xlxw
#参考:mersenne twister from wikipedia

#import
from time import time
import numpy as np

#var
index = 624
MT = [0]*index
# MT[0] ->seed

def inter(t):
    return(0xFFFFFFFF & t) #取最后32位->t

def twister():
    global index
    for i in range(624):
        y = inter((MT[i] & 0x80000000) +(MT[(i + 1) % 624] & 0x7fffffff))
        MT[i] = MT[(i + 397) % 624] ^ y >> 1
        if y % 2 != 0:
            MT[i] = MT[i] ^ 0x9908b0df
    index = 0

def exnum():
    global index
    if index >= 624:
        twister()
    y = MT[index]
    y = y ^ y >> 11
    y = y ^ y << 7 & 2636928640
    y = y ^ y << 15 & 4022730752
    y = y ^ y >> 18
    index = index + 1
    return inter(y)

def mainset(seed):
    MT[0] = seed    #seed
    for i in range(1,624):
        MT[i] = inter(1812433253 * (MT[i - 1] ^ MT[i - 1] >> 30) + i)
    return exnum()

def main():
    br = input("请输入随机数产生的范围(用,隔开):")
    mi = eval(br.split(',')[0])
    ma = eval(br.split(',')[1])    
    so = mainset(int(time())) / (2**32-1)
    rd = mi + int((ma-mi)*so)
    print("产生的随机整数为：",rd)
main()
