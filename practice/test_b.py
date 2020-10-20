import pytest, allure

TEST_CASE_LINK = 'http://172.17.33.152:88'


@allure.title('测试link功能')
@allure.testcase(TEST_CASE_LINK, 'link测试')
def test_with_testcase_link():
    pass
