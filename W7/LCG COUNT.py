#Random - LCG Ver by xlxw
#import
from time import time,clock
import sys
sys.setrecursionlimit(100000000)

#define
m = 2**32
a = 1103515245
c = 12345
rdls = []

def LCG(seed,mi,ma,n):
    if n == 1:
        return 0
    else:
        seed = (a * seed + c) % m
        rdls.append(int((ma-mi)*seed/float(m-1)) + mi)
        n = n-1
        LCG(seed,mi,ma,n)

def POSCheck():
    counts = {}
    for i in rdls:
        if i in counts:
            counts[i] = counts.get(i,0) + 1
        else:
            counts[i] = 1
    print(counts)
    
def main():
    br = input("请输入随机数产生的范围(用,隔开):")
    co = eval(input("请输入需要产生的随机数的个数:"))
    mi = eval(br.split(',')[0])
    ma = eval(br.split(',')[1])
    seed = time()
    LCG(seed,mi,ma,co)
    POSCheck()
    #print("随机生成的数字",rdls)
    
main()
