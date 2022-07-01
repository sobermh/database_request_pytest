"""
@author:maohui
@time:2022/6/30 13:28
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
from tools.yamlControl import get_yaml_data
from libs.login import Login

# # 执行用例
# # 1.获取用例
# res = get_yaml_data('../data/loginCase.yaml')[1]
# print(res)
# # 2.调用接口方法
# respData = Login().login(res['data'], False)
# print(respData)
#
# # 3.断言
# if respData['success'] == bool(res['resp']['message']):
#     print("----------------1")

#使用pytest 执行测试需要遵循的规则
# 1. py测试文件必须以test开头（或者以_test结尾）
# 2. 测试类必须以Test开头，并且不能有init方法
# 3. 测试方法必须以test_开头
# 4. 断言必须使用assert

import pytest
import allure,os

"""

"""
#登录接口-测试类封装
class TestLogin:

    @classmethod
    def setup_class(cls):
        pass
    @classmethod
    def teardown_class(cls):
        pass
    #测试方法
    @pytest.mark.parametrize('inBody,expData',get_yaml_data('../data/loginCase.yaml'))
    def test_login(self,inBody,expData):
        #调用业务代码
        res = Login().login(inBody, False)
        print(res)
        #断言
        assert res['success']==expData['message']


if __name__ == '__main__':
    pytest.main(["login_test.py",'-s',"--alluredir","../report/tmp" "--clean"]) #-s打印 输出
    #使用 allure 产生报告
    os.system("allure serve ../report/tmp")
    """
     1- 生成报告所需的文件
     2- 使用一些工具打开可视化报告
    """