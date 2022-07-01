"""
@author:maohui
@time:2022/6/30 11:46
  　　　　　　　 ┏┓    ┏┓+ +
  　　　　　　　┏┛┻━━━━┛┻┓ + +
  　　　　　　　┃        ┃ 　 
  　　　　　　　┃     ━  ┃ ++ + + +
  　　　　　 　████━████ ┃+
  　　　　　　　┃        ┃ +
  　　　　　　　┃   ┻    ┃
  　　　　　　　┃        ┃ + +
  　　　　　　　┗━┓   ┏━━┛
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃ + + + +
  　　　　　　　  ┃   ┃　　　Code is far away from bug with the animal protecting
  　　　　　　　  ┃   ┃+ 　　　　神兽保佑,代码无bug
  　　　　　　　  ┃   ┃
  　　　　　　　  ┃   ┃　　+
  　　　　　　　  ┃   ┗━━━━━━━┓ + +     
  　　　　　　　  ┃           ┣┓
  　　　　　　　  ┃           ┏┛
  　　　　　　　  ┗┓┓┏━━━━━┳┓┏┛ + + + +
  　　　　　　　   ┃┫┫     ┃┫┫
  　　　　　　　   ┗┻┛     ┗┻┛+ + + +
"""
import hashlib
import requests

from configs.config import HOST

#封装一个md5加密
def get_md5(psw):
    """
    :param psw:
    :return:md5加密结果
    """
    #实例化一个md5对象
    md5=hashlib.md5()
    #调用加密方法直接加密
    md5.update(psw.encode("utf-8"))
    return md5.hexdigest()

#封装一个登录的类
class Login():

    token=None
    def login(self,InData,mode=True):
        url=f"{HOST}/login"
        #参数
        payload=InData
        #请求
        resp=requests.post(url,json=payload)
        #查看响应
        # return resp.text  # json字符串
        if mode: # 获取token
            token=resp.json()["token"]
            return resp.json()["token"]
        else: # 获取相应数据
            return resp.json()# 返回字典类型
    ##单引号是 “字典”
    ##双引号是 “json”


# if __name__ == '__main__': #ctrl+j
#     res=Login().login({"appname":"LungScr","password":"LungScr"})
#     print(res)
#     print(get_md5("12"))