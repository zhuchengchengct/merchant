from selenium import webdriver


page=webdriver.Ie()
page.get('https://webpos.boccfc.cn:8080/login-auth.jsp')
page.find_element_by_id('authUserInfoPo.userCode').send_keys('BMS_SH_XK005')
page.find_element_by_id('authUserInfoPo.userPwd').send_keys('')
page.find_element_by_name('image').click()

while 1:


print(page.page_source)
感谢您使用 中银消费金融公司联盟商户WEB-POS授权系统 V3.0【授权平台】
中银消费金融公司联盟商户WEB-POS授权系统 V3.0
# id:authUserInfoPo.userCode
# id:authUserInfoPo.userPwd
# name:image
# name:imageButton