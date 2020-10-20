import pytest, allure


@allure.feature('搜索模块')
class TestSearch():

    def test_case1(self):
        print('case1')

    def test_case2(self):
        print('case2')


@allure.feature("登录模块")
class TestLogin():

    @allure.title('登录')
    @allure.story("登录成功")
    def test_login_succeess(self):
        with allure.step('步骤一：打开应用'):
            print('打开应用')
        with allure.step('步骤二：进入登录页面'):
            print('进入登录页面')
        with allure.step('步骤三：输入user/password'):
            print('输入用户名和密码')
        print('登录成功')
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        print('登录失败')
        pass

    @allure.story("用户名缺失")
    def test_login_noUser(self):
        print("用户名缺失")
        pass

    @allure.story('密码缺失')
    def test_login_noPwd(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print('输入密码')
        print('点击登录')
        with allure.step("点击登录之后失败"):
            assert '1' == 1
            print('登录失败')
        pass
