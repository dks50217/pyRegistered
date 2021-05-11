from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import util.chrome_helper
import requests

class Ctr_Register():
    def __init__(self, objParamConfig):
        self.param_config = objParamConfig
        self.registerURL = objParamConfig.URL if objParamConfig.version == '1' else objParamConfig.URL2
    def runWebDriver(self):
        success_msg = '預約掛號成功'

        full_registerURL = "{URL}?dept={dept}&dr={dr}&drname={drname}&schdate={schdate}&schap={schap}&chgdr={chgdr}&Lang={Lang}&idno={idno}&birth={birth}".format(
            URL = self.registerURL,
            dept = self.param_config.dept,
            dr = self.param_config.dr,
            drname = self.param_config.drname,
            schdate = self.param_config.schdate,
            schap = self.param_config.schap,
            chgdr = self.param_config.chgdr,
            Lang = self.param_config.Lang,
            idno = self.param_config.idno,
            birth = self.param_config.birth
        )

        driver_path = self.param_config.driver
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        chr_driver = webdriver.Chrome(driver_path, options=chr_options)
        chr_driver.get(full_registerURL)

        if self.param_config.auto_click == '1':
           chr_driver.find_element_by_xpath('//*[@id="btnInput"]').click()
        if self.param_config.screenshot == '1':
           chr_driver.save_screenshot(self.param_config.schdate_picture)
        
        return success_msg in chr_driver.page_source

    def runPost(self):
        params = {
            'workflag':self.param_config.workflag,
            'strSchdate':self.param_config.schdate,
            'strSchap':self.param_config.schap,
            'strDept':self.param_config.dept,
            'strDr':self.param_config.dr,
            'txtID':self.param_config.idno,
            'txtBirth':self.param_config.birth
        }

        result = requests.post(self.registerURL, data=params)

        return result.status_code == 200

    def checkwebdriver(self):
        util.chrome_helper.check_browser_driver_available()