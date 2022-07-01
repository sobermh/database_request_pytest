"""
@author:maohui
@time:2022/7/1 15:45
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

import pytest
import requests

from configs.config import TOKEN,HOST
from tools.httpclient import HttpClient

class TestCustomerMsg:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    # # 增加客户
    # def test_add_customer(self):
    #     pass
    #
    # # 按客户ID修改客户信息
    # def test_alter_customer_msg(self):
    #     pass
    #
    # # 按时间端查询客户信息
    # def test_acd_time_inquire_customer_msg(self):
    #     pass
    # 按客户ID查询客户信息
    def test_acd_id_inquire_customer_msg(self):
        # print(TOKEN)
        response=HttpClient().send_request(method='get',url=f'{HOST}/customer',param_type='application/json',data="1",headers={"Authorization":f'Bearer<{TOKEN}>'})

        # print(response.text)
        # print("-----------------------------11------------")
    # 按客户姓名和手机好查询客户
    # def test_acd_name_and_phonenum_inquire_customer_msg(self):
    #     pass

if __name__ == '__main__':

    pytest.main(['test_customer_msg.py','-sv'])