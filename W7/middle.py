#平方取中 -xlxw
from time import time

def rander(seed,n):
    if n ==1:
        return 0
    seed = int(seed)
    length = len(str(seed))
    seed = int(seed**2/pow(10,(length/2))) % int(pow(10.0,length))
    print(str(seed) +" " ,end='')
    rander(seed,n-1)
def main():
    seed = time()
    rander(seed,100)

main()
