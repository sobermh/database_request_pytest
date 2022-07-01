"""
@author:maohui
@time:2022/6/30 13:22
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

#需要按照第三方库 终端 pip install pyYaml
import yaml

def get_yaml_data(fileDir):

    resList=[] #存放结果[(请求1，期望响应1)，(请求2，期望响应2)]

    #1- 读取文件操作-----从磁盘读取到内存里
    file = open(fileDir,'r',encoding="utf-8")
    #2- 使用yaml方法获取数据
    res=yaml.load(file,Loader=yaml.FullLoader)
    file.close()
    #具体返回什么类型，根据需求

    info=res[0] #自己封装基类可以使用
    del res[0]
    for one in res:
        resList.append((one['data'],one['resp']))
    return resList #存放结果[(请求1，期望响应1)，(请求2，期望响应2)]

if __name__ == '__main__':
    res=get_yaml_data('../data/loginCase.yaml')
    for one in res:
        print(one)
