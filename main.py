import time
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display

sid = r"AC4b2f208b53b72484bfa6715199fee9ad"
token = r"9142b2e5bb0b3464c208aa39a3fa7dad"

client = Client(sid,token)
display = Display(visible=False,size=(1024,768))
display.start()

class SMCrawl():
    login_url = r"https://www.swmaestro.org/sw/member/user/forLogin.do?menuNo=200025"
    mentor_url = r"https://www.swmaestro.org/sw/mypage/mentoLec/list.do?menuNo=200046"

    def __init__(self,id,pw):
        self.broswer = webdriver.Chrome()
        self.id = id
        self.pw = pw
        self.mList = []


    def login(self):

        self.broswer.get(SMCrawl.login_url)

        self.broswer.find_element(By.ID,'username').send_keys(self.id)
        self.broswer.find_element(By.ID,'password').send_keys(self.pw)

        self.broswer.find_element(By.CLASS_NAME,'btn5').click()

    def get_list(self,send_message=False):
        self.broswer.get(SMCrawl.mentor_url)
        raw = self.broswer.find_elements(By.CLASS_NAME,"rel")
        for content in raw:
            real_content = content.find_element(By.TAG_NAME, 'a').text
            if real_content not in self.mList:
                self.mList.append(real_content)
                if len(self.mList) > 10 :
                    self.mList.pop(0)

                print(real_content)
                if send_message:
                    print("Here")
                    # message = client.messages.create(
                    #     to="+8201082733891",
                    #     from_="+15855952968",
                    #     body="Hey"
                    # )

    def run(self,timer=2):
        while True:
            self.login()
            self.get_list(send_message=True)
            time.sleep(timer*60)






if __name__ == "__main__":
    id = r"well87865@gmail.com"
    pw = r"amortrai98!"
    crawler = SMCrawl(id,pw)
    crawler.login()
    crawler.get_list()
    crawler.run()