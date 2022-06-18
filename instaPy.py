
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import random
import datetime


class InstaPy():
    
    def __init__(self):
        #Write a path to your geckodriver or chromedriver
        s=Service('C:\Program Files\gecko\geckodriver.exe')
        self.browser = webdriver.Firefox(service=s)  
        
    ### logIN
    def login(self):
        self.login = "YOUR_IG_LOGIN" ### login
        self.password = "yOUR_ig_pASSWORD" ### hasło
        self.browser.get('https://www.instagram.com/')
        print(self.browser.title)
        time.sleep(5)
    ## cookies  
        self.acceptbutton = self.browser.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[1]/button[1]')
        time.sleep(2)
        self.acceptbutton.click()
        self.acceptbutton.click()
        time.sleep(2)
    ## end  of cookies  
        self.emailForm = self.browser.find_element(By.NAME, 'username')
        self.emailForm.click()
        self.emailForm.send_keys(self.login)
        time.sleep(2)
        self.passwordForm = self.browser.find_element(By.NAME, 'password')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)
        time.sleep(1)
        self.loginButton = self.browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        time.sleep(1)
        self.loginButton.click()
        time.sleep(4)


    ### input your own hashtags
    def add_hashtags_and_search(self):   
        
        self.hashtags = ['hashtag', 'hashtag', 'hashtag']
        self.liczba = len(self.hashtags)
        self.hashtags_rand = random.randint(0, self.liczba -1)
        time.sleep(4)
        self.browser.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/' )
        time.sleep(3)
        self.rand = random.randint(1000,3000)
        self.rand = str(self.rand)
        self.browser.refresh()
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(10," + self.rand + ")")
        print('hashtag #', self.hashtags[self.hashtags_rand], "\n")
        time.sleep(3)
    
    ### opening random picture
    def open_photo(self): 
        
        self.left = random.randint(1,3)
        self.left = str(self.left)
        self.downIndex = random.randint(1,3)
        self.downIndex = str(self.downIndex)
        self.photo = self.browser.find_element(By.XPATH, '//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+ self.left + ']/div['+ self.downIndex +']/a/div')
        self.photo.click()
        time.sleep(2)
        
        
    ### negt picture without liking
    def skip_photo(self):
        time.sleep(2)
        self.skip_photo_button = self.browser.find_element(By.CSS_SELECTOR, 'body')
        self.logic_skip_photo = random.randint(4,9) #number of photos (from, to)
        self.i = 0
        while self.i < self.logic_skip_photo:
            time.sleep(1.5)
            self.skip_photo_button = self.browser.find_element(By.CSS_SELECTOR, 'body')
            time.sleep(1)
            self.skip_photo_button.send_keys(Keys.RIGHT)
            self.i = self.i + 1
            print('skip {} photo, {}'.format(self.logic_skip_photo, self.i), "\n")    
            
     
    ### like + printing username + date and time
    def like_photo_or_get_info(self):
        
        now = datetime.datetime.now()
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp.replace(" ","_")
        file_name = date_stamp + ".png"
        time.sleep(0.5)
        print(self.browser.title)
        self.like_button = self.browser.find_element(By.CLASS_NAME, 'fr66n')
        time.sleep(0.5)
        self.get_name = self.browser.find_element(By.CLASS_NAME, 'e1e1d')
        time.sleep(0.5)
        self.get_name.text
        print('liked photo: {}'.format(self.get_name.text))
        self.browser.get_screenshot_as_file(file_name)
        print(now, "\n")
        self.like_button.click()
        
        
    ### just next picture click
    def next_photo(self):
        time.sleep(2)
        self.next_photo_button = self.browser.find_element(By.CSS_SELECTOR, 'body')
        time.sleep(2)
        self.next_photo_button.send_keys(Keys.RIGHT)
        # /html[1]/body[1]/div[6]/div[1]/div[1]/div[1]/div[2]/button[1] - prawo
        # /html[1]/body[1]/div[6]/div[1]/div[1]/div[1]/div[1]/button[1] - lewo
        
    ### pause
    def relax(self):
        
        self.relax_time = random.randint(12,29) # how many seconds of pause (from, to)
        print('Waiting', self.relax_time, ' seconds')
        time.sleep(self.relax_time)
        
    ### just changing hashtags
    def change_hash(self):
        
        self.hashtags_rand = random.randint(0, self.liczba -1)
        time.sleep(2)
        self.browser.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/' )
        print('New hashtag' + self.hashtags[self.hashtags_rand], "#", "\n")
        time.sleep(5)
    
    def random_like(self):
        
        self.amount = random.randint(1000,2000) # how many likes for hashtag (from, to)
        print('Liked - ', self.amount, "\n")
        
        
    ### auto like
    def auto_like(self):
        
        self.random_like()
        p_liked = 0
        while True:
            
          if p_liked == self.amount:
              self.change_hash() 
              p_liked = 0
              self.relax()
              self.browser.refresh()
              time.sleep(7)
              try:
                  self.open_photo()
              except Exception:     
                  self.open_photo()
              time.sleep(4)
              self.skip_photo()
          else:
            time.sleep(5)
            try:
                self.like_photo_or_get_info()
            except Exception:     
                self.next_photo()       
            self.relax_after_like = random.randint(2,14)
            time.sleep(self.relax_after_like)
            self.next_photo()
            p_liked = p_liked + 1

bot = InstaPy()
bot.login()
bot.add_hashtags_and_search()     
bot.open_photo()   
bot.skip_photo()
bot.auto_like()