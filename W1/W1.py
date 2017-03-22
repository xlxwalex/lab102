#七牛云上传文件到空间内.    By xlxw 2017
#请得到自己的secret和access key
#PS本来 AK 和SK 用了getpass库，但是因为终端不支持，所以暂时屏蔽了.

#import SDK
from qiniu import Auth,put_file,etag,BucketManager
import qiniu.config
from getpass import getpass
import requests

#上传
def upload(bucket,path,filename,key):
    token = key.upload_token(bucket, filename, 3600)
    print('正在上传..')
    reform,inform = put_file(token, filename, path)
    if reform != None:
        print('已经成功地将{}->>{}'.format(filename,bucket))
    else:
        print('这里出现了一个小错误.')

#下载        
def download(url,path):
    r = requests.get(url)
    contenter=r.content
    with open(path,'wb') as filer:
        filer.write(contenter)
        filer.close()
    print("已经保存文件到{}".format(path))
#删除
def delete(bucketer,filename,key):
    print('正在删除..')
    bucket = BucketManager(key)
    reform,fo = bucket.delete(bucketer, filename)
    if reform != None:
        print('已经成功地将{}->>X'.format(filename))
    else:
        print('这里出现了一个小错误.(可能是空间并没有这个文件)')

#主体        
def main():
    #填写你的 AK 和 SK
    accesskey = 'BoQckdkTak7R1n4nEW9Yv7G0jdNKs2SN61tVIA8T'
    secretkey = 'qgQZdDO4xXJenVJ5-WivF7I_Kt5_Slgu8onA9Djt'

    #鉴定身份
    keyq=Auth(accesskey,secretkey)

    #所要操作的空间
    bucketname =input("请输入要操作的空间(公开)名字:")

    #判定操作类型
    while 1:
        order=input('请输入你需要进行的操作：')
        mode=order.split(' ')[0]
        if mode == '上传':
            path=order.split(' ')[1]
            fname=path.split('/')[-1:][0]
            print('正在尝试生成Token.请稍后..')
            upload(bucketname,path,fname,keyq)
        elif mode == '下载':
            print('正在尝试生成Token.请稍后..')
            download(order.split(' ')[1],order.split(' ')[2])
        elif mode == '更换':
            if order.split(' ')[1] == '空间':
                bucketname =input("请输入您想要更改的空间(公开)名字:")
            elif order.split(' ')[1] == 'AK':
                #accesskey = getpass(prompt= '请输入新的AK:')
                accesskey = input( '请输入新的AK:')
            elif order.split(' ')[1] == 'SK':
                #secretkey = getpass('请输入新的SK:')
                secretkey = input('请输入新的SK:')
            else:
                print('您输入的命令有误')
        elif mode == '删除':
            print('正在尝试生成Token.请稍后..')
            delete(bucketname,order.split(' ')[1],keyq)
            
        elif mode =='退出':
            break
        else:
            print('输入的命令存在错误')

print('+---------------------------------------------------+')
print('|欢迎使用本Qiniu云的上传下载程序，以下为使用方法    |')
print('|---------------------------------------------------|')
print('|1.清先输入您的Accesskey和SecretKey进行鉴权         |')
print('|2.之后请输入您要进行操作的buket空间                |')
print('|3.上传操作的命令为: 上传 文件地址(带后缀)          |')
print('|4.下载操作的命令为: 下载 链接地址 本地路径带后缀)  |')
print('|5.删除操作的命令为: 删除 空间中的文件名称          |')
print('|6.更换bucket操作为: 更换 空间名                    |')
print('|7.更换AKSK的操作为: 更换 AK/SK                     |')
print('|8.退出程序的操作为: 退出                           |')
print('+---------------------------------------------------+')
main()
    
