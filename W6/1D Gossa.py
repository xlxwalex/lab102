#一维高斯模糊 -xlxw
from PIL import Image as p
import numpy as np
from time import clock
import math

#define
sizepic = [0,0]
timer = [0,0,0,0]
PI = math.pi

def getrgb(path,r):#得到图像中各个点像素的RGB三通道值
    timer[0] = clock()
    pd = p.open(path)
    sizepic[0],sizepic[1] = pd.size[0],pd.size[1]
    nr = np.zeros((sizepic[0],sizepic[1]))
    ng = np.zeros((sizepic[0],sizepic[1]))
    nb = np.zeros((sizepic[0],sizepic[1]))
    for i in range(0,sizepic[0]):
        for j in range(0,sizepic[1]):
            nr[i][j] = pd.getpixel((i,j))[0]
            ng[i][j] = pd.getpixel((i,j))[1]
            nb[i][j] = pd.getpixel((i,j))[2]
    #镜像扩充
    for i in range(1,r+1):#顶部
        nxr = nr[i*2-1]
        nxg = ng[i*2-1]
        nxb = nb[i*2-1]
        nr = np.insert(nr,0,values = nxr ,axis = 0)
        ng = np.insert(ng,0,values = nxg ,axis = 0)
        nb = np.insert(nb,0,values = nxb ,axis = 0)
    for i in range(sizepic[0]+r-1,sizepic[0]-1,-1):#底部
        nxr = nr[i]
        nxg = ng[i]
        nxb = nb[i]
        nr = np.insert(nr,(sizepic[0]+r-1)*2-i,values = nxr ,axis = 0)
        ng = np.insert(ng,(sizepic[0]+r-1)*2-i,values = nxg ,axis = 0)
        nb = np.insert(nb,(sizepic[0]+r-1)*2-i,values = nxb ,axis = 0)
    for i in range(1,r+1):#左侧
        nxr = nr[:,i*2-1]
        nxg = ng[:,i*2-1]
        nxb = nb[:,i*2-1]
        nr = np.insert(nr,0,values = nxr ,axis = 1)
        ng = np.insert(ng,0,values = nxg ,axis = 1)
        nb = np.insert(nb,0,values = nxb ,axis = 1)
    for i in range(sizepic[1]+r-1,sizepic[1]-1,-1):#右侧
        nxr = nr[:,i]
        nxg = ng[:,i]
        nxb = nb[:,i]
        nr = np.insert(nr,(sizepic[1]+r-1)*2-i,values = nxr ,axis = 1)
        ng = np.insert(ng,(sizepic[1]+r-1)*2-i,values = nxg ,axis = 1)
        nb = np.insert(nb,(sizepic[1]+r-1)*2-i,values = nxb ,axis = 1)
    print("已经得到所有像素的R,G,B的值，所花时间为{:.3f}s".format(clock()-timer[0]))
    timer[0] = clock()-timer[0]
    return nr,ng,nb

def matcombine(r,g,b,rd):
    #模糊矩阵
    summat = 0
    timer[1] = clock()
    ma = np.zeros(2*rd+1)
    for i in range(0,2*rd+1):
        ma[i] = (1/(((2*PI)**0.5)*rd))*math.e**(-((i-rd)**2)/(2*(rd**2)))
        summat += ma[i]
    ma[0::1] /= summat
    print("已经计算出高斯函数矩阵，所花时间为{:.3f}s".format(clock()-timer[1]))
    timer[1] = clock()-timer[1]
    #blur
    ner,neg,neb = np.zeros_like(r),np.zeros_like(g),np.zeros_like(b)
    u,p,q = 0,0,0
    #y向模糊
    timer[2] = clock()

    for i in range(rd+1,sizepic[0]+rd-1):
        for j in range(rd+1,sizepic[1]+rd-1):
            u += r[j-rd:j+rd+1:1,i]*ma[0::1]
            p += g[j-rd:j+rd+1:1,i]*ma[0::1]
            q += b[j-rd:j+rd+1:1,i]*ma[0::1]
            ner[j][i],neg[j][i],neb[j][i] = u.sum(0),p.sum(0),q.sum(0)
            u,p,q = 0,0,0
    #x向模糊
    for i in range(rd+1,sizepic[0]+rd-1):
        for j in range(rd+1,sizepic[1]+rd-1):
            u += ner[i,j-rd:j+rd+1:1]*ma[0::1]
            p += neg[i,j-rd:j+rd+1:1]*ma[0::1]
            q += neb[i,j-rd:j+rd+1:1]*ma[0::1]
            ner[i][j] = u.sum(0)
            neg[i][j] = p.sum(0)
            neb[i][j] = q.sum(0)
            u,p,q = 0,0,0
    print("已经完成模糊，所花时间为{:.3f}s".format(clock()-timer[2]))
    timer[2] = clock()-timer[2]
    return ner,neg,neb
    
def cpic(r,g,b,path,rd):#图片输出
    timer[3] = clock()
    pd = p.new("RGB",(sizepic[0]-rd-1,sizepic[1]-rd-1))
    for i in range(rd+1,sizepic[0]):
        for j in range(rd+1,sizepic[1]):
            pd.putpixel((i-rd-1,j-rd-1),(int(r[i][j]),int(g[i][j]),int(b[i][j])))
    print("已经完成生成，所花时间为{:.3f}s".format(clock() - timer[3]))
    timer[3] = clock()-timer[3]
    print("正在导出图片..")
    pd.save("blurred.jpg")

def main():
    rd = eval(input("请输入模糊的半径："))
    path = input("请输入图片的地址(包括后缀)：")
    nr,ng,nb = getrgb(path,rd)
    nr,ng,nb = matcombine(nr,ng,nb,rd)
    cpic(nr,ng,nb,path,rd)
    print("{} - >> {}".format(path.split('/')[-1],"blurred.jpg"))
    print("总计耗时:{:.3f}s,感谢您的使用.".format(timer[0]+timer[1]+timer[2]+timer[3]))
main()

