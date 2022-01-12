from abc import abstractmethod
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import sys

def element_exists_q(checker):
     try:
        driver.find_element(By.LINK_TEXT,checker)
     except NoSuchElementException:
        return False
     return True

def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def site_login():
     driver.get("https://vsn.ac.in/student.vsn.ac.in/")  #Connect to School Website
     driver.find_element(By.ID,"txtStudentID").send_keys("H1079") #Enter School ID
     driver.find_element(By.ID,"txtPass").send_keys("31122003") #Enter Password
     driver.find_element(By.ID,"btnSubmit").click() #Click On Submit
     #driver.find_element_by_link_text("Live Class").click()
     element=WebDriverWait(driver,50).until(
           lambda driver: driver.find_elements(By.LINK_TEXT,"Attendance Time UP") or driver.find_elements(By.LINK_TEXT,"Attendance") or driver.find_elements(By.LINK_TEXT,"Attendance Done") or driver.find_elements(By.LINK_TEXT,"Holiday")
         )
     print(element)
     
     if(element_exists_q("Attendance Time UP")): #is it timeout??
            print("Sorry, Time is UP")
           
     if(element_exists_q("Holiday")): #is it a Holiday??
            print("Its a Holiday")
       
     
     if(element_exists_q("Attendance Done")): #Is attendance already given??
            print("You have Already Given Attendance")
            
     
     if(element_exists_q("Attendance")): #if not then do it
            element=driver.find_element(By.LINK_TEXT,"Attendance")
            element.click()
            if(element_exists_q("Attendance Done")):  #Was it successful
                print("Attendance Successful")
            else :
                if(element_exists_q("Attendance")): #An unknown error has occured.
                    print("Attendance Failed")
                else:
                    print("Unknown Error Occured! Pls give Attendance Manually") #Attendance must be given Manually.
     driver.close()
         
ser = Service(resource_path(".\\driver\\chromedriver.exe")) 
op=webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser,options=op)
site_login()

