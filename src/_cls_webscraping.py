# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:28:59 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#%% Create Class

class WebScraping_Chrome:
    
    def funWebDriver_ChrDP(varDriverPath):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        service = Service(executable_path=varDriverPath)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver

    def funWebDriver_ChrDP_DP(varDriverPath, varDownloadPath):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        prefs = {"download.default_directory": varDownloadPath}
        options.add_experimental_option("prefs", prefs)
        service = Service(executable_path=varDriverPath)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver

    def funWebDriver_ChrPP_DP(varProfilePath, varDriverPath):
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-data-dir={varProfilePath}')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        service = Service(executable_path=varDriverPath)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver
    
    def funWebDriver_DP_notGUI(varDriverPath):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--headless") # don't interfaz grafic
        options.add_argument("--disable-gpu") # don't interfaz grafic
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("window-size=1920x1080")
        service = Service(executable_path=varDriverPath)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver

    def funWebDriver_ChrDP_DP_notGUI(varDriverPath, varDownloadPath):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--headless") # don't interfaz grafic
        options.add_argument("--disable-gpu") # don't interfaz grafic
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("window-size=1920x1080")
        prefs = {"download.default_directory": varDownloadPath}
        options.add_experimental_option("prefs", prefs)
        service = Service(executable_path=varDriverPath)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver

    def funWebDriver_ChrPP_DP_notGUI(varProfilePath, varDriverPath):
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-data-dir={varProfilePath}')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--headless") # don't interfaz grafic
        options.add_argument("--disable-gpu") # don't interfaz grafic
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("window-size=1920x1080")
        service = Service(executable_path=varDriverPath)
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver

    def funAccesLink(driver, link):
        driver.get(link)
    
    def funInsertKeys_XPATH(driver, xpath_, s_keys):
        keys = driver.find_element(By.XPATH, xpath_)
        keys.send_keys(s_keys)
    
    def funInsertKeys_CSS(driver, xpath_, s_keys):
        keys = driver.find_element(By.CSS_SELECTOR, xpath_)
        keys.send_keys(s_keys)
    
    def funClick_XPATH(driver, xpath_):
        button = driver.find_element(By.XPATH, xpath_)
        button.click()
    
    def funClick_CSS(driver, xpath_):
        button = driver.find_element(By.CSS_SELECTOR, xpath_)
        button.click()
    
    def funWaitToElement_XPATH(driver, wait, xpath_):
        wait_xpath = xpath_
        WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.XPATH, wait_xpath)))
    
    def funWaitToElement_CSS(driver, wait, css_):
        wait_xpath = css_
        WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, wait_xpath)))

    def funWaitToClick_XPATH(driver, wait, xpath_):
        wait_xpath = xpath_
        element = WebDriverWait(driver, wait).until(
                EC.element_to_be_clickable((By.XPATH, wait_xpath))
            )
        element.click()
    
    def funWaitToClick_CSS(driver, wait, css_path):
        wait_xpath = css_path
        element = WebDriverWait(driver, wait).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, wait_xpath))
            )
        element.click()

    def funSelectOption(driver, name_id, text):
        source = driver.find_element(By.NAME , name_id)
        source_select = Select(source)
        source_select.select_by_visible_text(f'{text}')

    def funClearCamp_XPATH(driver, xpath_):
        input_element = driver.find_element(By.XPATH, xpath_)
        input_element.clear()