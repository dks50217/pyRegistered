
class Ctr_Version():
    def __init__(self,driver):
        self.driver = driver
    def checkWebDriver(self):
        browserVersion = self.driver.capabilities['browserVersion']
        chromedriverVersion = self.driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        if browserVersion[0:2] != chromedriverVersion[0:2]: 
            return 0
        else:
            return 1

        
    
