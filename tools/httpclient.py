"""
@author:maohui
@time:2022/7/1 15:27
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
import requests


class HttpClient:
    """请求工具类"""
    # 只要用到这个类 就会进入到init 这个函数里面去
    def __init__(self):
        self.session = requests.Session()

    # 封装请求 post delete get put..
    # 接口地址 不同的接口
    # 接口参数 不同的参数
    # 参数类型 表单 json
    # 请求头   数据类型设置 **kwargs 接收不确定的几个参数

    def send_request(self, method, url, param_type, data=None, **kwargs):
        # 请求方式转成大写
        method = method.upper()
        # 参数类型转成大写
        param_type = param_type.upper()
        # 判断 post get
        if 'GET' == method:
            response = self.session.request(method=method, url=url, params=data, **kwargs)
        elif 'POST' == method:
            if 'FROM' == param_type:
            # 参数json提交 data提交 判断传的类型
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif 'DELETE' == method:
            if 'FROM' == param_type:
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        elif 'PUT' == method:
            if 'FROM' == param_type:
                response = self.session.request(method=method, url=url, data=data, **kwargs)
            else:
                response = self.session.request(method=method, url=url, json=data, **kwargs)
        else:
            raise  ValueError

        return response

    def close_session(self):
        self.session.close()