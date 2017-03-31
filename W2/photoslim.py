#七牛云"图片瘦身"功能的python实现方法：
#请得到自己的secret和access key用于上传图片到空间中进行处理
#图片瘦身是七牛云的一项收费项目，价格为 ￥0.1/1000次 测试时请先存1元进入

#import SDK
from qiniu import Auth,put_file,etag
import qiniu.config
import requests

#指定图片处理后缀的格式
picu=['jpg','jpeg','png','PNG','JPEG','JPG']

#上传
def upload(bucket,path,filename,key,url):
    token = key.upload_token(bucket, filename, 3600)
    print('正在上传..')
    reform,inform = put_file(token, filename, path)
    if reform != None:
        print('已经成功地将{}->>{}'.format(filename,bucket))
        print("正在处理您的图片...")
        url=url + '/' + filename
        path=path.split('/')[-1]
        download(url,path)
    else:
        print('这里出现了一个小错误.无法上传..')
        
        
#下载
def download(url,path):

    if url.split('.')[-1] in picu:
        r = requests.get(url,params='imageslim')
        r.raise_for_status()
        contenter=r.content
        with open(path,'wb') as filer:
            filer.write(contenter)
            filer.close()
        print("已经将转换后的文件{}保存到了本地".format(path))
    else:
        print('抱歉，您的图片的格式不支持瘦身操作.')

    
#主体
def main():
    #填写你的 AK 和 SK
    accesskey = input('请输入您在七牛云的AccessKey：')
    secretkey = input('请输入您在七牛云的SecretKey：')

    #鉴定身份
    keyq=Auth(accesskey,secretkey)
    
    #所要操作的空间
    bucketname =input("请输入要操作的空间(公开)名字：")

    #所要操作空间的外链地址
    urlbucket = input("请输入空间所绑定的域名或者默认外链地址：")

    #判定操作类型
    while 1:
        order=input('请输入你需要进行的操作：')
        mode=order.split(' ')[0]
        if mode == '转换':
            path=order.split(' ')[1]
            fname=path.split('/')[-1:][0]
            print('正在尝试生成Token.请稍后..')
            upload(bucketname,path,fname,keyq,urlbucket)
        if mode == '退出':
            print("欢迎您的使用..")
            break

print("+----------------------------------------+")
print("|        欢迎使用七牛的图片瘦身功能      |")
print("+----------------------------------------+")
print("|本程序须知：                            |")
print("|1.七牛只能对jpg和png格式的图片进行瘦身  |")
print("|2.您需要提供服务的Accesskey，Secretkey  |")
print("|3.您需要提供 bucket名字和bucket外链地址 |")
print("+----------------------------------------+")
print("|使用方法:                               |")
print("|1.瘦身输入格式： 转换 图片位置(包括后缀)|")
print("|2.退出输入格式： 退出                   |")
print("+----------------------------------------+")
main()
