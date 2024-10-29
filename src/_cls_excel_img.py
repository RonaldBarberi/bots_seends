# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:40:15 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

import os
import re
import time
import psutil
import shutil
import pyperclip
from PIL import ImageGrab
import win32com.client as win32
from unidecode import unidecode
from datetime import datetime, timedelta
from _cls_webscraping import WebScraping_Chrome as ws
from selenium.webdriver.common.keys import Keys

#%% Create Class

class Excel_Img:
    def __init__(self, excel_file_path, rangos, image_folder, whatsapp_group):
        self.excel_file_path = excel_file_path
        self.rangos = rangos
        self.image_folder = image_folder
        self.whatsapp_group = whatsapp_group
        self.xlSheetVisible = -1
        self.xlSheetHidden = 0
        self.xlSheetVeryHidden = 2
        self.xlBitmap = 2
    
    def kill_proccess(self):
        print("Se han cerrado todos los archivos Excel abiertos, continuando con el proceso.")
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'EXCEL.EXE':
                psutil.Process(proc.info['pid']).terminate()
    
    def ScreenshotExcel(self):
        print("Abriendo archivo: ", self.excel_file_path)
        excel_app = win32.DispatchEx("Excel.Application")
        excel_app.DisplayAlerts = False
        excel_app.Visible = False
        workbook = excel_app.workbooks.open(self.excel_file_path)
        print("Actualizando consultas")
        workbook.RefreshAll()
        excel_app.CalculateUntilAsyncQueriesDone()
        print("Actualizando tablas dinamicas")
        for sheet in workbook.Sheets:
            for pivot_table in sheet.PivotTables():
                pivot_table.RefreshTable()
                time.sleep(2)
                
        # Iterate through all sheets and capture images
        print("Capture images")
        for sheet in workbook.Sheets:
            if sheet.Visible == self.xlSheetVisible:
               sheet_name = sheet.Name
               if sheet_name in self.rangos:
                   try:
                       range_ = sheet.Range(self.rangos[sheet_name])
                       range_validacion = sheet.Range('A1:A1')
                       if range_validacion.Cells(1, 1).Value is not None and range_validacion.Cells(1, 1).Value > 0:
                          range_.CopyPicture(Format=self.xlBitmap)
                          time.sleep(2)
                          captura = ImageGrab.grabclipboard()
                          
                          # Save the image with a name based on the sheet name
                          pattern = r'[A-Za-z0-9]+'
                          sheet_name = sheet_name.replace('_','')
                          sheet_name = re.findall(pattern, sheet_name)[0]
                          sheet_name = unidecode(sheet_name)
                          print("Capture: ", sheet_name)
                          time.sleep(2)
                          if not os.path.exists(self.image_folder):
                              os.makedirs(self.image_folder)
                          image_path = os.path.join(self.image_folder, f"{self.whatsapp_group}_{sheet_name}.jpg" )
                          time.sleep(2)
                          captura.save(image_path)
                          pyperclip.copy('')
                          time.sleep(3)
                       else:
                          print(f"No data found in A1 of {sheet_name}. Image not captured.")
                   except Exception as n:
                      print(f"Error copy: {n}")
                      
        workbook.Save()
        workbook.Close(False)
        excel_app.Quit()
        print("Close workbook")
        del excel_app
    
    def get_image_paths(self):
        return self.image_paths
    
    def main(self):
        self.kill_proccess()
        self.ScreenshotExcel()


class SeendMsg_Wpp:
    def __init__(self, driver_path, profile_path, whatsapp_group, text_wpp, image_folder):
        self.driver_path = driver_path
        self.profile_path = profile_path
        self.whatsapp_group = whatsapp_group
        self.text_wpp = text_wpp
        self.image_folder = image_folder
    
    def Interval_Current(self):
        interval = datetime.now()
        interval -= timedelta(minutes=interval.minute % 30, seconds=interval.second)
        interval = interval.strftime('%d/%m/%Y - %H:00:00')
        return interval
    
    def Open_seend_img(self):
        interval = self.Interval_Current()
        print(f"Enviando PDC a {self.whatsapp_group}, a corte {interval}.")
        driver = ws.funWebDriver_ChrPP_DP(self.profile_path, self.driver_path)
        ws.funAccesLink(driver, 'https://web.whatsapp.com')
        ws.funWaitToElement_XPATH(driver, 300, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p")
        ws.funInsertKeys_XPATH(driver, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p", self.whatsapp_group)
        time.sleep(1)
        ws.funInsertKeys_XPATH(driver, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p", Keys.RETURN)
        time.sleep(3)
        for clave, valor in self.text_wpp:
            image_path = f"{self.image_folder}\\{self.whatsapp_group}_{clave}.jpg"
            attempt = 0
            max_attempts = 3
            if os.path.exists(image_path):
                while attempt < max_attempts:
                    try:
                        print(f"Intento {attempt+1}: Buscando archivo en la ruta: {image_path}")
                        ws.funClick_XPATH(driver, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div[2]/div/div') # Botón +
                        time.sleep(2)
                        ws.funInsertKeys_XPATH(driver, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]', image_path)
                        time.sleep(1)
                        try:
                            ws.funInsertKeys_XPATH(driver, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p', f"{valor} a corte {interval}")
                            time.sleep(0.5)
                            ws.funInsertKeys_XPATH(driver, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p', Keys.ENTER)
                        except:
                            ws.funInsertKeys_XPATH(driver, '//div[@aria-label="Añade un comentario"]', f"{valor} a corte {interval}")
                            time.sleep(0.5)
                            ws.funInsertKeys_XPATH(driver, '//div[@aria-label="Añade un comentario"]', Keys.ENTER)
                        print(f"Imagen {clave} enviada con éxito.")
                        break
                    except Exception as e:
                        print(f"Error al enviar {clave}, intento {attempt+1}: {e}")
                        attempt += 1
                        time.sleep(5)
            else:
                print(f"El archivo {clave} no se encuentra en la ruta especificada: {image_path}")
        time.sleep(30)
        shutil.rmtree(self.image_folder, ignore_errors=True)
        driver.quit()
        print("PDC enviado.")
    
    def main(self):
        self.Open_seend_img()
