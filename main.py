from datetime import datetime  
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
import configparser

config_file_name = 'config.ini'

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

CONFIG_PATH = os.path.join(application_path, config_file_name)
config = configparser.ConfigParser()
config.read(CONFIG_PATH,encoding="utf-8")


config_auto_click = config['system']['autoclick']
config_screenshot = config['system']['screenshot']
config_driver = config['path']['driver']
config_URL = config['url']['router']
config_dept =  config['url']['dept']
config_dr =  config['url']['dr']
config_drname =  config['url']['drname']
config_schap =  config['url']['schap']
config_chgdr =  config['url']['chgdr']
config_Lang =  config['url']['Lang']
config_idno =  config['url']['idno']
config_birth =  config['url']['birth']
registerDate = datetime.now() + timedelta(days=14) 
schdate = registerDate.strftime("%Y/%m/%d")


registerURL = "{URL}?dept={dept}&dr={dr}&drname={drname}&schdate={schdate}&schap={schap}&chgdr={chgdr}&Lang={Lang}&idno={idno}&birth={birth}".format(
    URL = config_URL,
    dept = config_dept,
    dr = config_dr,
    drname = config_drname,
    schdate = schdate,
    schap = config_schap,
    chgdr = config_chgdr,
    Lang = config_Lang,
    idno = config_idno,
    birth = config_birth
)

options = Options()
driver = webdriver.Chrome(config_driver, chrome_options=options)
driver.set_window_size(1024, 960)
driver.get(registerURL)

if config_auto_click == '1':
    driver.find_element_by_xpath('//*[@id="btnInput"]').click()

if config_screenshot == '1':
    driver.save_screenshot('{0}_registered.png'.format(schdate))
