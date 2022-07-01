"""
@author:maohui
@time:2022/6/30 15:37
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
import os

import pytest
# """
# 运行所有：pytest.main()
# 指定模块：pytest.main(['-vs','login_test.py'])
# 指定目录: pytest.main(['-vs','/case'])
# 通过nodeid指定用例运行：nodeid由模块名，分隔符，类名，方法名，函数名组成
#     pytest.main(['-vs','./case/login_test.py::TestLogin::test_login'])
# 多线程： pytest.main(['-vs','/case'，'-n=2'])
# 失败用例再重跑2次： pytest.main(['-vs','/case'，'--reruns=2'])
#
#
# -s:输出调试信息，包括print打印的信息
# -v:显示更详细的信息
# -vs:这两个参数可以一起用
# -n :支持多线程或者分布式运行测试用例。
#     如：pytest -vs  ./login_test.py -n -2
# -x： 一个测试报错，那么测试停止
# --maxfail=2 出现两个用例失败就停止
# -k： 根据测试用例的部分字符串指定测试用例 -k “ao”
# -m： 指定执行的markers "smoke or usermanage"


#改变默认从上到下用例执行的顺序：
# @pytest.mark.run(order=1)


# pytest.ini这个文件它是pytest单元测试框架的核心配置文件
# 1.位置：一般放在项目的根目录
# 2.编码：必须是ANSI，可以使用notpad++修改编码格式
# 3.作用：改变pytest默认的行为
# 4.运行的规则：不管是主函数的模式运行，命令行模式运行，都会去读取这个配置文件


# [pytest]
# addopts= -vs            #命令行的参数，用空格分隔
# testpaths = ./case      #测试用例的路径
# python_files=test_*.py  #模块名规则
# python_classes=Test*    #类名规则
# python_functions=test   #方法名规则
# markers =
#     smoke：冒烟用例
#     usermanage：用户管理模块
#     productmanage：商品管理模块

# """


# 用例分组执行
# @pytest.mark.smoke
# 用例跳过
# @pytest.mark.skip(reason="")

if __name__ == '__main__':
    pytest.main(['-vs','login_test.py',"--alluredir","../report/tmp","--clean"])
    os.system("allure serve ../report/tmp")