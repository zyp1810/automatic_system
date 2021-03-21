# 目标：抽取公共方法，优化API调用
from selenium.webdriver.common.by import By
import yaml
# coding=gbk

# 使用继承的方式进行封装
class BasePage():
    # 保存页面操作中需要的公共方法
    def __init__(self, driver):
        self.driver=driver
        eles = yaml.load(open("banniu.yml").read(), Loader=yaml.FullLoader)[self.__class__.__name__]
        for ele in eles:
            self.__setattr__(ele, eles[ele])


    def click(self,*locator):
        self.driver.find_element(*locator).click()

    # 输入文本
    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    # 获取目标元素文本
    def get_text(self,*locator):
        return self.driver.find_element(*locator).text


class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self,driver)
        self.driver.get("https://work.banniu.im/account.html#/login")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    # 进入登录页
    def to_login(self,username,password):
        # 输入账号、密码登录
        # 参数1：元素的定位方式，参数2：对应定位方式的表达式
        self.input_text(username,*self.username_input)
        self.input_text(password,*self.password_input)
        self.click(*self.login_btn)
        res = self.get_text(*self.check_point)
        assert "赤兔" in res

        # 返回登录页对象
        return Qunzu(self.driver)

# 班牛群组
class Qunzu(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

# 班牛知识库
class ZhiShiKu(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

# 班牛小程序
class XiaoChengXu(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def to_xiaochengxu(self):
        # 点击"小程序"
        self.click(*self.xiaochengxu_btn0)

        # 点击小程序名称“批量转款应用【正式环境】”
        self.click(*self.xiaochengxu_btn)

        # 点击工作表名称“花样年华”
        self.click(*self.gongzuobiao_btn)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    a = LoginPage(driver)
    a.to_login("18939461688","wjb12345")
    b = XiaoChengXu(driver)
    b.to_xiaochengxu()

    # import yaml
    # res = yaml.load(open("banniu.yml").read(),Loader=yaml.FullLoader)
    # print(res)
    # print(res["LoginPage"]["username_input"])
修改
