from datetime import datetime
from datetime import timedelta

class Param_Config():
    def __init__(self,config):
        self.sendmail = config['system']['sendmail']
        self.auto_click = config['system']['autoclick']
        self.screenshot = config['system']['screenshot']
        self.checkdriver = config['system']['checkdriver']
        self.driver = config['path']['driver']
        self.URL2 = config['url']['router2']
        self.URL = config['url']['router']
        self.dept =  config['url']['dept']
        self.dr =  config['url']['dr']
        self.drname =  config['url']['drname']
        self.schap =  config['url']['schap']
        self.chgdr =  config['url']['chgdr']
        self.Lang =  config['url']['Lang']
        self.idno =  config['url']['idno']
        self.birth =  config['url']['birth']
        self.day = int(config['url']['day'])
        self.version = config['url']['version']
        self.workflag = config['url']['workflag']
        self.mailfrom = config['email']['from']
        self.mailto = config['email']['to']
        self.mailkey = config['email']['key']

        registerDate = datetime.now() + timedelta(days=int(self.day))
        self.schdate = registerDate.strftime("%Y/%m/%d")
        self.schdate_picture = "{0}_registered.png".format(registerDate.strftime("%Y%m%d"))