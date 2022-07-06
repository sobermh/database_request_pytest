"""
@author:maohui
@time:2022/7/5 13:10
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

from configs.config import TOKEN, HOST
from tools.httpclient import HttpClient
from tools.yamlControl import get_yaml_data1


class TestSampleMsg():

    @classmethod
    def setup_class(cls):
        cls.file_id=""

    @classmethod
    def teardown_class(cls):
        pass

    #3.1增加样本
    @pytest.mark.skip(reason="自增字段，不能随意增加样本")
    def test_add_sample(self):
        """增加样本，暂时不测试,跳过"""
        pass
    #3.2按样本id修改样本信息
    def test_acd_sampleId_alter_sampleMsg(self):
        """3.2按样本id修改样本信息"""
        request_data = {
            # "sys_id": 1,
            # "type": 1,
            # "cid": 1,
            # "collect_time": "2020-12-16",
            # "channel": "",
            # "risk": 2,
            # "result": "好",
            "guidance": f"继续作{datetime.datetime.today()}"
        }
        response = HttpClient().send_request(method='put', url=f'{HOST}/sample/1330', param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == True
        print(response.json())
    #3.3按样本id插入文件信息
    @pytest.mark.parametrize('data',get_yaml_data1('../data/Acd_sampleid_insert_file_msg.yaml'))
    def test_acd_sampleId_insert_filemsg(self,data):
        """3.3按样本id插入文件信息"""
        request_data = {
                "sys_id":1,
                "sid":1330,
                "files":[{"group":1,"type":1,"oss_id":1,"path":"1516-2ba8-4ba6-bdc9-7af7852b02ae.html"}]
                }
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}',
                                             param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        global file_id
        file_id=response.json()["fid_map"][0]["id"]
        print(response.json())
    #3.4按文件id删除文件
    @pytest.mark.parametrize('data', get_yaml_data1('../data/Acd_fileid_delete_file.yaml'))
    def test_acd_fileId_delete_file(self,data):
        """3.4按文件id删除文件"""
        request_data = ""
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}/{file_id}',
                                             param_type='application/json',
                                             data=None, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())
    #3.5按文件id插入（修改）项目代号
    @pytest.mark.parametrize('data', get_yaml_data1('../data/Acd_fileid_change_project.yaml'))
    def test_acd_fileId_change_project(self,data):
        """3.5按文件id插入（修改）项目代号"""
        request_data = data["request"]
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}',
                                             param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())
    #3.6按时间段查询样本
    @pytest.mark.parametrize('data', get_yaml_data1('../data/Acd_time_inquire_sample.yaml'))
    def test_acd_time_inquire_sample(self,data):
        """3.6按时间段查询样本"""
        # request_data = {"begin_date":data["request"]['begin_date'],
        #                 "end_date":data["request"]['end_date']}
        request_data =data["request"]
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}',
                                             param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())
    #3.7按样本id查询样本
    @pytest.mark.parametrize('data', get_yaml_data1('../data/Acd_sampleid_inquire_sample.yaml'))
    def test_acd_sampleId_inquire_sample(self,data):
        """3.7按样本id查询样本"""
        request_data = ""
        response = HttpClient().send_request(method=data['method'], url=f'{HOST}/{data["url"]}',
                                             param_type='application/json',
                                             data=request_data, headers={"Authorization": f'Bearer<{TOKEN}>'})
        assert response.json()['success'] == data["success"]
        print(response.json())

if __name__ == '__main__':
    pytest.main(['test_sample_msg.py','-sv'])