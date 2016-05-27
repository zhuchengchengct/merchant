# 商户申请填表
import time
from selenium import webdriver
from selenium.webdriver.support.ui  import Select

chrome=webdriver.Chrome()
chrome.get('http://merchant.boccfc.cn/loan')
chrome.find_element_by_id('username').send_keys('HZEF0040')
# chrome.find_element_by_id('password').send_keys('')
# chrome.find_element_by_id('checkCode').click()

while 1:
    time.sleep(0.2)
    try:
        if chrome.find_element_by_id('risk_yes_btn'):
            chrome.find_element_by_id('risk_yes_btn').click()
    except:
        pass
    try:
        if chrome.find_element_by_id('cbAgreement'):
            chrome.find_element_by_id('cbAgreement').click()
            chrome.find_element_by_id('cbAgreement_btn').click()
            break
    except:
        pass

chrome.find_element_by_id('coursePrice').send_keys('10000')
chrome.find_element_by_id('coursePeriod').send_keys('12')
chrome.find_element_by_id('loanAmount').send_keys('10000')
chrome.find_element_by_id('selfPayAmount').send_keys('1000')
Select(chrome.find_element_by_id('payType')).select_by_index(1)
Select(chrome.find_element_by_id('installPeriod')).select_by_index(1)
chrome.find_element_by_class_name('buttonNext').click()
chrome.find_element_by_id('customerName').send_keys('test')
chrome.find_element_by_id('idNo').send_keys('342402198801113816')
chrome.find_element_by_id('mobileNo').send_keys('13651807654')
chrome.find_element_by_id('email').send_keys('13651807654@qq.com')
Select(chrome.find_element_by_id('homeAddr1')).select_by_index(1)
Select(chrome.find_element_by_id('homeAddr2')).select_by_index(1)
Select(chrome.find_element_by_id('homeAddr3')).select_by_index(1)
chrome.find_element_by_id('homeAddr4').send_keys('test address')
chrome.find_element_by_id('homePostCd').send_keys('200000')
chrome.find_element_by_class_name('buttonNext').click()
chrome.find_element_by_id('jobUnit').send_keys('abc')
chrome.find_element_by_id('department').send_keys('test department')
Select(chrome.find_element_by_id('unitAddr1')).select_by_index(1)
Select(chrome.find_element_by_id('unitAddr2')).select_by_index(1)
Select(chrome.find_element_by_id('unitAddr3')).select_by_index(1)
chrome.find_element_by_id('unitAddr4').send_keys('test unitAddr')
chrome.find_element_by_id('unitPostCd').send_keys('200000')
chrome.find_element_by_id('startJobYear').send_keys('3')
chrome.find_element_by_id('startJobMonth').send_keys('2')
chrome.find_element_by_id('unitTelArea').send_keys('021')
chrome.find_element_by_id('unitTelNo').send_keys('63291111')
Select(chrome.find_element_by_id('vocaType')).select_by_index(3)
chrome.find_element_by_id('incomeCurMonth').send_keys('10000')
chrome.find_element_by_class_name('buttonNext').click()
chrome.find_element_by_id('linkmanName').send_keys('testlinknName')
chrome.find_element_by_id('linkmanMobile').send_keys('13111111111')
chrome.find_element_by_id('linkmanName2').send_keys('testlinknName2')
chrome.find_element_by_id('linkmanMobile2').send_keys('13122222222')
chrome.find_element_by_id('qqNumber').send_keys('326377945')
chrome.find_element_by_class_name('buttonFinish').click()







# # 课程价格
# coursePrice
# # 课程时长
# coursePeriod
# # 申请金额
# loanAmount
# # 首付
# selfPayAmount
# # 还款方式（select）
# payType
# # 分期期数（select）
# installPeriod
# # 下一步
# class='buttonNext'
# # 姓名
# customerName
# # 身份证号
# idNo
# # 手机
# mobileNo
# # email
# email
# # 住宅（select）
# homeAddr1 homeAddr2 homeAddr3
# # 详细地址
# homeAddr4
# # 邮编
# homePostCd
# # 下一步
# class='buttonNext'
# # 单位
# jobUnit
# # 部门
# department
# # 单位地址（select）
# unitAddr1 unitAddr2 unitAddr3
# # 单位地址详细
# unitAddr4
# # 单位邮编
# unitPostCd
# # 工作年限
# startJobYear startJobMonth
# # 单位电话（区号、号码、分机）
# unitTelArea unitTelNo unitTelExt
# # 行业性质（select）
# vocaType
# # 收入
# incomeCurMonth
# # 联系人
# linkmanName
# # 联系人手机
# linkmanMobile
# # 联系人2
# linkmanName2
# # 联系人2手机
# linkmanMobile2
# # 申请人QQ
# qqNumber
# # 提交
# class='buttonFinish'

print('all done!')
