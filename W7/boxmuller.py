#import 
import numpy as np  

def boxmuller():
    sigma = 1
    size = 1
    u = np.random.uniform(size=size)  
    v = np.random.uniform(size=size)  
    z = np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * v)  
    return z * sigma  
  
print(boxmuller()[0])
