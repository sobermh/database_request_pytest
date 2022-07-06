"""
@author:maohui
@time:2022/7/5 17:38
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

from configs.config import TOKEN, HOST
from tools.httpclient import HttpClient
from tools.yamlControl import get_yaml_data1

class TestProjectMsg:
    @classmethod
    def setup_class(cls):
        pass
    @classmethod
    def teardown_class(cls):
        pass
    #4.1按文件id查询项目代号
    @pytest.mark.parametrize('data', get_yaml_data1('../data/Acd_fileid_inquire_project.yaml'))
    def test_acd_fileId_inquire_project(self,data):
        """4.1按文件id查询项目代号"""
        request_data=""
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}', param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())
    #4.2按项目代号查询样本信息
    @pytest.mark.parametrize('data', get_yaml_data1('../data/Acd_projectID_inquire_sample_msg.yaml'))
    def test_acd_projectID_inquire_sample_msg(self,data):
        """4.2按项目代号查询样本信息"""
        request_data = ""
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}',
                                             param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())
    #4.3查询项目列表
    @pytest.mark.parametrize('data', get_yaml_data1('../data/project_list.yaml'))
    def test_project_list(self,data):
        """4.3查询项目列表"""
        request_data = ""
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}',
                                             param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())


if __name__ == '__main__':
    pytest.main(['test_project_msg.py','-sv'])