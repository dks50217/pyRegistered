from model.param_email import Param_Email
from model.param_config import Param_Config
from control.ctr_email import Ctr_Email
from control.ctr_register import Ctr_Register
import os
import sys
import configparser

config_file_name = 'config.ini'

# get root 
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

# get setting
CONFIG_PATH = os.path.join(application_path, config_file_name)
config = configparser.ConfigParser()
config.read(CONFIG_PATH,encoding="utf-8")
objParamConfig = Param_Config(config)

# start register
ctr_register = Ctr_Register(objParamConfig)

if objParamConfig.version == '1':
    ctr_register.checkwebdriver()
    result = ctr_register.runWebDriver()
else :
    result = ctr_register.runPost()

# result process
if result == True:
    objParamEmail = Param_Email(
        "{0}_{1}門診掛號成功".format(objParamConfig.schdate,objParamConfig.drname),
        objParamConfig.mailfrom,
        objParamConfig.mailto,
        "這封信件是由系統自動寄出，附件為掛號結果",
        objParamConfig.schdate_picture,
        objParamConfig.mailkey
    )
else:
    objParamEmail = Param_Email(
        "{0}_{1}門診掛號失敗".format(objParamConfig.schdate,objParamConfig.drname),
        objParamConfig.mailfrom,
        objParamConfig.mailto,
        "這封信件是由系統自動寄出，附件為掛號結果",
        objParamConfig.schdate_picture,
        objParamConfig.mailkey
    )

# send mail
if objParamConfig.sendmail == '1':
    ctr_email = Ctr_Email(objParamEmail)
    ctr_email.sendMail()

#driver.close()
sys.exit()


