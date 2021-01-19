from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Bot:
        def __init__(self):
            self.messages = ["Jao, vamos contar carneirinhos?"]
            self.chats = ['Ana']
            options = webdriver.ChromeOptions()
            options.add_argument('lang=pt-br')
            self.driver = webdriver.Chrome(
                executable_path=r'./chromedriver', chrome_options=options)

        def SendMessages(self):
            self.driver.get('https://web.whatsapp.com')
            time.sleep(20)
            for chat in self.chats:
                chat_field = self.driver.find_element_by_xpath("//span[@title='Ana']")
                time.sleep(3)
                chat_field.click()
                for message in self.messages:
                    chat_box = self.driver.find_element_by_class_name('DuUXI')
                    time.sleep(3)
                    chat_box.click()
                    chat_box.send_keys(message)
                    send_button = self.driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                    time.sleep(3)
                    send_button.click()
                time.sleep(5)


bot = Bot()
bot.SendMessages()
