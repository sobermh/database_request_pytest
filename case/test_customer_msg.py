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
import datetime

import pytest
import requests

from configs.config import TOKEN, HOST
from tools.httpclient import HttpClient


class TestCustomerMsg:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    # 增加客户
    def test_add_customer(self):
        """增加客户"""
        request_data = {
            "sys_id": 1,
            "name": f"毛{datetime.datetime.now()}",
            "gender": 0,  # 0男 1女
            "born": "1998-11-04",
            "idcard": "",
            "cellphone": "19357665827"
        }
        response = HttpClient().send_request(method='post', url=f'{HOST}/customer', param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == True
        print(response.json())

    # 按客户ID修改客户信息
    def test_alter_customer_msg(self):
        """按客户ID修改客户信息"""
        request_data = {
            # "sys_id": 1,
            "name": f"毛{datetime.datetime.now()}",
            # "gender": 1,
            # "born": "1964-12-31",
            # "idcard": "",
            # "cellphone": f"13967145255"
        }
        response = HttpClient().send_request(method='put', url=f'{HOST}/customer/1052', param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == True
        print(response.json())

    # # 按时间端查询客户信息
    def test_acd_time_inquire_customer_msg(self):
        """按时间端查询客户信息"""
        response = HttpClient().send_request(method='get',
                                             url=f'{HOST}/customer?begin_date=2021-12-24&end_date=2021-12-28',
                                             param_type='application/json',
                                             data="", headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == True
        print(response.json())

    # 按客户ID查询客户信息
    # @pytest.mark.parametrize('url,assert_data','../data/Acd_id_inquire_cutomer_msg.yaml')
    def test_acd_id_inquire_customer_msg(self):
        """按客户ID查询客户信息"""
        response = HttpClient().send_request(method='get', url=f'{HOST}/customer/1052', param_type='application/json',
                                             data="", headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['customer']["id"] == 1052
        print(response.json())

    # 按客户姓名和手机号查询客户
    def test_acd_name_and_phonenum_inquire_customer_msg(self):
        """按客户姓名和手机号查询客户"""
        request_data={
            "name": "毛辉",
            "cellphone": "19357665827"
        }
        response = HttpClient().send_request(method='post', url=f'{HOST}/customer/info', param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == True
        print(response.json())

# if __name__ == '__main__':
#     pytest.main(['test_customer_msg.py', '-sv'])
