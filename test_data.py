import pytest
import yaml


# class TestData:
#
#     @pytest.mark.parametrize(['a','b'],yaml.safe_load(open('./data.yaml')))
#     def test_data1(self,a,b):
#
#         print(a + b)

class TestDemo:
    @pytest.mark.parametrize("data", yaml.safe_load(open('./data.yaml')))
    def test_demo(self, data):
        if 'te' in data:
            print('测试环境')
            print(data)
        elif 'pro' in data:
            print('生产环境')

    def test_yaml(self):
        print(yaml.safe_load(open('./data.yaml')))
