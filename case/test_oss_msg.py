"""
@author:maohui
@time:2022/7/5 17:45
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

import pytest

from configs.config import TOKEN, HOST
from tools.httpclient import HttpClient
from tools.yamlControl import get_yaml_data1

class TestOssMsg:
    #按oss的id查询oss信息
    @pytest.mark.parametrize('data',get_yaml_data1('../data/Ossid_inquire_oss_msg.yaml'))
    def test_ossId_inquire_oss_msg(self,data):
        """按oss的id查询oss信息"""
        request_data={"pwd":{data["pwd"]}}
        response = HttpClient().send_request(method='get', url=f'{HOST}/{data["url"]}', param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())


if __name__ == '__main__':
    pytest.main(['test_oss_msg.py','-sv'])