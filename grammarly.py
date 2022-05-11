from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from handlers import errors, error_fixes
import time
import json


class Grammarly:

    def __init__(self) -> None:

        self.errors = errors
        self.error_fixes = error_fixes

        options = Options()
        options = webdriver.ChromeOptions()

        #options.add_argument("--start-maximized")

        options.binary_location = "/chrome.exe"
        
        options.add_argument("user-data-dir=/home/user/chrome")
        
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # to prevent this error "Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)"
        
        try:
            self.driver = webdriver.Chrome(options=options)
        except InvalidArgumentException:
            print("A browser window is already open. Please close it and try again.")
            exit()

        self.actions = ActionChains(self.driver)


        f = open("credentials.json", "r")
        self.credentials = json.load(f)
        f.close()

        self.email = self.credentials["email"]
        self.password = self.credentials["password"]

        #self.text = "test text"


    def onboarding(self):
        pass


    def login(self):

        print("Logging in...")

        self.driver.get("https://www.grammarly.com/signin")

        self.driver.implicitly_wait(10)
        if self.driver.current_url == "https://app.grammarly.com/":
            print("Already Logged In!")
            time.sleep(10)
            return True

        else:
            email_input = self.driver.find_element(by=By.XPATH,value="//*[@id=\"email\"]")
            email_input.send_keys(self.email)

            self.driver.implicitly_wait(10)
            continue_button = self.driver.find_element(by=By.XPATH,value="//*[@id=\"page\"]/div/div/div[2]/div/form/button")
            continue_button.click()

            self.driver.implicitly_wait(10)
            password = self.driver.find_element(by=By.XPATH,value="//*[@id=\"password\"]")
            password.send_keys(self.password)

            signin_button = self.driver.find_element(by=By.XPATH,value="//*[@id=\"page\"]/div/div/div[2]/div/form/button")
            signin_button.click()

            self.driver.implicitly_wait(5)
            try:
                human_verification = self.driver.find_element(by=By.XPATH,value="//*[@id=\"page\"]/div/div/div[2]/div/div/div[1]").text
                if human_verification == "Verify that you’re human":
                    print("\nHUMAN VERIFICATION REQUIRED!!")
                    print("\nPlease complete the human verification process and then press enter.")

                    inp = input()

            except NoSuchElementException:
                pass

            time.sleep(10)

            if self.driver.current_url == "https://app.grammarly.com/":
                print("Login Succesfull!")

            else:
                print("Login Unsuccesfull! Please check your credentials.")

    
    
    def open_new_file(self):

        print("Opening New File...")

        possible_xpaths = ["//*[@id=\"page\"]/div/div/div[2]/div[4]/div/div[2]/div[2]/div/div[1]/div","//*[@id=\"page\"]/div/div/div[2]/div[4]/div/div[3]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div","//*[@id=\"page\"]/div/div/div[2]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div"]
        
        for xpath in possible_xpaths:
            try: 
                self.driver.implicitly_wait(5)
                new_file = self.driver.find_element(by=By.XPATH,value=xpath)
                new_file.click()
                time.sleep(1)
                print("New File Opened!")
                
                return self.driver.current_url

            except NoSuchElementException:
                if possible_xpaths[-1] == xpath:
                    print("Please clear all saved files first and then re-run the program!")
                    quit()
                

        k = 0
        while k==0:
            try:
                page_load = self.driver.find_element(by=By.XPATH,value="//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/div/main/div/div/div[10]/div[1]/p")
                if page_load:
                    k = 1
            except NoSuchElementException:
                pass
        if k==1:

            self.document_id = self.driver.current_url.split("/")[-1]
            return True
            
        else:
            return False
        


    def delete_new_file(self):

        """
        This function is not working as expected. "missing required headers" error is thrown.
        """

        self.driver.get("https://app.grammarly.com/")

        self.driver.get(f"https://dox.grammarly.com/documents/{self.document_id}")

        self.driver.refresh()

    

    def enter_text(self,text):

        self.text = text
        print("Entering Text...")
        while True:
            try:
                self.text_area = self.driver.find_element(by=By.XPATH,value="//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/div/main/div/div/div[10]/div[1]")
                self.text_area.send_keys(self.text)

                key = self.overall_score()

                if key:
                    print("Text Entered and Processing Complete!")

                    #time.sleep(1.5)
                    break
                
                else:
                    print("Processing incomplete")
                    break
            
            except NoSuchElementException:
                pass

    
    
    def overall_score(self):

        while True:
            for xpath in ["//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[2]/div/div[2]/div/nav/div/div[3]/div/div/header/div[2]/div/div/div[2]","//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[2]/div/div[2]/div/nav/div/div[3]/div/div/header/div[2]/div/div/div","//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/div/main/div/div/div[10]/div[1]/p"]:
                try:
                    processing_complete = (self.driver.find_element(by=By.XPATH,value=xpath)).text
                    if processing_complete == "Overall score" or processing_complete == "Great job!":
                        #time.sleep(0.5)
                        return True

                except NoSuchElementException:
                        pass


    
    def what_error(self):

        print("Identifying error...")
        
        for error in self.errors:
            try:

                e = self.driver.find_element(by=By.XPATH,value=error)
                if e:
                    self.err = (self.driver.find_element(by=By.XPATH,value=error)).text
                    print(self.err)

                    if self.err in self.error_fixes.keys():
                        break
                    '''
                    elif "Accept" in self.err or "suggestions" in self.err or "suggestion" in self.err:
                        self.err = "ACCEPT"
                        break
                    
                    else:
                        self.err = "DELETE"
                        break
                    '''
            except NoSuchElementException:
                continue
    

    def resolve_error(self):

        print("Resolving Error...")
        
        if self.err in self.error_fixes.keys():
            for e in self.error_fixes[self.err]:
                try:

                    if len(self.error_fixes[self.err]) == 1:
                        correction = self.driver.find_element(by=By.XPATH,value=self.error_fixes[self.err][0])
                    else:
                        correction = self.driver.find_element(by=By.XPATH,value=e)

                    if correction:
                        #time.sleep(0.3)
                        
                        correction.click()
                        #self.driver.execute_script("arguments[0].click()", correction)

                        try:
                            correction = self.driver.find_element(by=By.XPATH,value=e)
                            continue
                        except NoSuchElementException:
                            print("Error Resolved!")
                            #return 1

                except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException):
                    #self.actions.key_down(Keys.PAGE_UP).key_up(Keys.PAGE_UP).perform()
                    pass
        else:
            pass
        ''' 
        for e in self.error_fixes['DELETE']:
            try:
                delete = self.driver.find_element(by=By.XPATH,value=e)
                delete.click()
            except NoSuchElementException:
                pass
        '''
    
    
    def identify_and_resolve_error(self):
        
        try:
            time.sleep(0.5)
            self.driver.implicitly_wait(5)
            self.counter = int((self.driver.find_element(by=By.XPATH,value="//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[2]/div/div/div/div/div/div").text))
            print(self.counter)

        except NoSuchElementException:
            print("No Errors Found!")
            return self.text

        try:
            time.sleep(0.33)
            #self.driver.implicitly_wait(10)
            next_correction = self.driver.find_element(by=By.XPATH,value=f"//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div/div/div[2]/div")
            #time.sleep(0.5)
            next_correction.click()

        except (NoSuchElementException,StaleElementReferenceException):
            pass

        self.overall_score()

        while self.counter > 0:

            #self.overall_score()

            try:
                self.what_error()
                self.resolve_error()
                
                if self.if_completed() == True:

                    corrected_text = (self.text_area).text
                    print("No More ERRORS!")
                    print("Give yourself a pat on the back!")
                    return corrected_text

                else:
                    self.expand_error_wrapper()           
                
            except (NoSuchElementException,StaleElementReferenceException,ElementClickInterceptedException):
                if self.if_completed() == True:

                    corrected_text = (self.text_area).text
                    print("No More ERRORS!")
                    print("Give yourself a pat on the back!")
                    
                    return corrected_text

        print("Correction Complete!")

    
    
    def expand_error_wrapper(self):

        
        for k in range(1,6):
            try:
                time.sleep(0.33)
                #self.driver.implicitly_wait(10)
                next_correction = self.driver.find_element(by=By.XPATH,value=f"//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div[3]/div[2]/div/div[2]/div[{k}]/div/div/div/div/div/div[2]/div")
                time.sleep(0.12)

                #self.driver.execute_script("arguments[0].click()", next_correction)
                next_correction.click()

                
                break

            except (NoSuchElementException,StaleElementReferenceException):
                self.actions.key_down(Keys.PAGE_UP).key_up(Keys.PAGE_UP).perform()
                pass


    def if_completed(self):
            
        for xpath in ["//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[2]/div/div[2]/div/nav/div/div[3]/div/div/header/div[2]/div/div/div","//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[2]/div/div[2]/div/nav/div/div[3]/div/div/header/div[2]/div/div/div[2]","//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[2]/div/div[2]/div/nav/div/div[3]/div/div/header/div[2]/div/div/div","//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/div/main/div/div/div[10]/div[1]/p"]:
            try:
                processing_complete = (self.driver.find_element(by=By.XPATH,value=xpath)).text
                if processing_complete == "Great job!":
                    #time.sleep(0.5)
                    return True

            except NoSuchElementException:
                    pass

    def if_completed_two(self):
        for xpath in ["//*[@id=\"page\"]/div/div[2]/div[2]/div/div[4]/div[3]/aside/div/div/div/div/div[2]/div/div[2]/div/div[1]"]:
            try:
                success = (self.driver.find_element(by=By.XPATH,value=xpath)).text
                if success in ["To err is human; to edit, divine."]:
                    return True
            except NoSuchElementException:
                pass
    

    def clear_document(self):
        try:
            self.text_area.send_keys(Keys.CONTROL + "a")
            time.sleep(0.3)
            self.text_area.send_keys(Keys.DELETE)
            time.sleep(0.3)
        except NoSuchElementException:
            pass


    
    
    
    def run(self,text):
        
        self.text = text
        self.enter_text()
        
        correct_text = self.identify_and_resolve_error()
        return correct_text

        #self.driver.close()