from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

options = webdriver.ChromeOptions()
options.add_argument("--lang=en")
options.add_argument("--incognito")

sent = 1

def send_all(username,password,read1, read2 ,amount):
    browser = webdriver.Chrome()
    browser.close()
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    time.sleep(5)

    browser.find_element(By.NAME,'username').send_keys(username)
    browser.find_element(By.NAME,'password').send_keys(password)
    time.sleep(1)

    browser.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(7)

    browser.get(f"https://www.instagram.com/explore/tags/{read2}")
    time.sleep(5)

    try:
        browser.find_element(By.XPATH,"//*[@class='_aao7']/div/div/div/div/div/a").click()
        time.sleep(1)
    except:
        time.sleep(3)
        browser.find_element(By.XPATH,"//*[@class='_aao7']/div/div/div/div/div/a").click()
        time.sleep(1)

    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
    time.sleep(0.5)

    for i in range(int(amount)):
        try:
            #Comment on a post
            browser.find_element(By.XPATH,"//*[@class='_akhn']/textarea").click()
            browser.find_element(By.XPATH,"//*[@class='_akhn']/textarea").send_keys(read1)
            time.sleep(1)
            browser.find_element(By.XPATH,"//*[@class='_akhn']/div[2]/div").click()
            print("Comment ",i)
            time.sleep(3)
        except:
            browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
            time.sleep(1)

        #Move on to the next Post
        browser.find_element(By.XPATH,"//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']").click()
        # print("Next!")
        time.sleep(1)

    


for i in parser.sections():

    print(i)
    username = parser.get(i, 'username')
        #print(username)
    password = parser.get(i, 'password')
        #print(password)
    amount = 2
        #print(amount)

    file1=None
    read1=None
    file1=open('message.txt','r')
    read1 = file1.readlines()
    # message = parser.get(i, 'message')
        #print(message)
    
    file2=None
    read2=None
    file2=open('hashtag.txt','r')
    read2 =file2.readlines()
    
    # hashtag = parser.get(i,'hashtag')
    
    #for i in range(int(sent)):
    send_all(username,password,read1, read2,amount)
    time.sleep(5)

    #Quit the Program
    # browser.quit()

