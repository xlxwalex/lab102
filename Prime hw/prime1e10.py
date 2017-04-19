#求解2-1e10以内的素数
from time import clock
import numpy as np

def prime(N):
    n = int(N)
    half = int(n/2)
    s = int(n ** 0.5)+1
    sls = np.ones(n,dtype=np.bool)
    b=0
    sls[3::3]=False
    sls[5::5]=False
    tim=clock()
    for i in range(3,s,2):
        if sls[i]:
            sls[i**2::i]=False
    print('共计花费时间：{:.5f}s   '.format(clock()-tim),end='')

    for i in range(3,n,2):
        if sls[i]:
            b+=1
            #print('{:5}'.format(i),end='')        
    print('共计在2-{}间有{}个素数'.format(n,b+3))

prime(1e10)
