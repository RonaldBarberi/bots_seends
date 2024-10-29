# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:41:48 2024

@author: Ronal.Barberi
"""

#%% Import libraries

import os
import time
import pandas as pd
from _cls_nav_directorys import Nav_Directorys as nd
from _cls_webscraping import WebScraping_Chrome as ws
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#%% Create Class

class GTRealTime:
    def __init__(self, varProfilePath, varDriverPath, varWppGroup, varUser, varPassword, lisCampaing):
        self.varProfilePath = varProfilePath
        self.varDriverPath = varDriverPath
        self.varWppGroup = varWppGroup
        self.varUser = varUser
        self.varPassword = varPassword
        self.lisCampaing = lisCampaing

    def report_wpp(self):
        driver = ws.funWebDriver_ChrPP_DP(self.varProfilePath, self.varDriverPath)
        ws.funAccesLink(driver, 'https://web.whatsapp.com')
        ws.funWaitToElement_XPATH(driver, 300, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p")
        ws.funInsertKeys_XPATH(driver, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p", self.varWppGroup)
        time.sleep(1)
        ws.funInsertKeys_XPATH(driver, "//*[@id='side']/div[1]/div/div[2]/div[2]/div/div[1]/p", Keys.RETURN)
        driver.execute_script("window.open('');")
        while True:
            driver.switch_to.window(driver.window_handles[1])
            df_str = self.real_time_manage(driver)
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            ws.funInsertKeys_XPATH(driver, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p', df_str)
            time.sleep(0.5)
            ws.funInsertKeys_XPATH(driver, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p', Keys.ENTER)
            time.sleep(300)

    def real_time_manage(self, driver):
        ws.funAccesLink(driver, f'https://{self.varUser}:{self.varPassword}@soulphone-eigth.groupcos.com/vicidial/realtime_report.php')
        time.sleep(3)
        ws.funClick_XPATH(driver, '//*[@id="campaign_select_list_link"]/table/tbody/tr/td/a')
        time.sleep(1)
        ws.funClick_XPATH(driver, '//*[@id="groups[]"]/option[1]')
        for campaign in self.lisCampaing:
            ws.funSelectOption(driver, "groups[]", campaign)
            time.sleep(0.5)
        ws.funClick_XPATH(driver, '/html/body/table[2]/tbody/tr/td/form/font[1]/span[2]/table/tbody/tr[1]/td[2]/input[2]')
        time.sleep(2)
        tabla = driver.find_element(By.XPATH, '/html/body/table[2]')
        filas = tabla.find_elements(By.TAG_NAME, "tr")
        data = []
        for fila in filas:
            columnas = fila.find_elements(By.TAG_NAME, "td")
            fila_datos = [columna.text for columna in columnas]
            data.append(fila_datos)

        data_processed = []
        for item in data:
            for texto in item:
                lineas = texto.split("\n")
                data_processed.extend(lineas)
        df = pd.DataFrame(data_processed, columns=["Text"])
        df = self.read_data(df)
        df = self.filter_data_alerts(df)
        df_str = df.to_string()

        return df_str
        
    def read_data(self, df):
        print('process data')
        start_index = df[df.apply(lambda x: x.str.contains(r"^\s*\|?\s*ESTACIÓN", case=False, regex=True).any(), axis=1)].index[0]
        df = df.iloc[start_index+2:].reset_index(drop=True)

        fila_divisoria = "+----------------+------------------------+-----------+-----------------+---------+------------+-------+------+-------------------"
        indice_fila = df[df.apply(lambda fila: fila_divisoria in str(fila.values), axis=1)].index
        if len(indice_fila) > 0:
            df = df[:indice_fila[0]]

        df_texto = df.apply(lambda x: ' '.join(x.astype(str)), axis=1)
        df_dividido = df_texto.str.split('|', expand=True)
        df_dividido = df_dividido.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        columnas_estandar = ['DELETE', 'ESTACION', 'AGENTE', 'SESSION_ID', 'ESTADO_PAUSA', 'MM_SS', 'CAMPANA', 'LLAMADAS', 'MANT', 'GROUP']
        columnas_actuales = len(df_dividido.columns)
        
        if columnas_actuales < len(columnas_estandar):
            for i in range(len(columnas_estandar) - columnas_actuales):
                df_dividido[f'Columna_extra_{i+1}'] = None
        elif columnas_actuales > len(columnas_estandar):
            df_dividido = df_dividido.iloc[:, :len(columnas_estandar)]
        df_dividido.columns = columnas_estandar
        return df_dividido
        
    def filter_data_alerts(self, df):
        columns_need = ['AGENTE', 'ESTADO_PAUSA', 'MM_SS', 'CAMPANA']
        df = df[columns_need]

        df['MM_SS_segundos'] = df['MM_SS'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

        con_bano = (df['ESTADO_PAUSA'] == 'PAUSA    BANO') & (df['MM_SS_segundos'] >= 15 * 60)
        con_break = (df['ESTADO_PAUSA'] == 'PAUSA    BREAK') & (df['MM_SS_segundos'] >= 20 * 60)
        con_what = (df['ESTADO_PAUSA'] == 'PAUSA    WHAT') & (df['MM_SS_segundos'] >= 39 * 60)
        con_pausa = (df['ESTADO_PAUSA'] == 'PAUSA') & (df['MM_SS_segundos'] >= 1 * 60)
        con_dead = (df['ESTADO_PAUSA'] == 'DEAD  A') & (df['MM_SS_segundos'] >= 1 * 60)
        con_feed = (df['ESTADO_PAUSA'] == 'PAUSA    FEED') & (df['MM_SS_segundos'] >= 1 * 60)
        con_papro = (df['ESTADO_PAUSA'] == 'PAUSA    PAPRO') & (df['MM_SS_segundos'] >= 10 * 60)
        con_llms = (df['ESTADO_PAUSA'] == 'PAUSA    LLMS') & (df['MM_SS_segundos'] >= 1 * 60)

        condicion = con_bano | con_break | con_what | con_pausa | con_dead | con_feed | con_papro | con_llms
        df_filtrado = df[condicion]
        df = df_filtrado.drop(columns=['MM_SS_segundos'])
        print(df)
        return df

    def main(self):
        self.report_wpp()

#%% Use class

if __name__ == "__main__":
    varProfilePath = os.path.expanduser('~/Command_Center/Profile_claro_tmk_bog')
    varDriverPath = nd.funJoinTwoDic(nd.funDicOneBack(), 'config', 'chromedriver.exe')
    varWppGroup = 'Alertas OTR'
    varUser = 'username'
    varPassword = 'password_to_page'
    lisCampaing = [
        'HOGAR',
        'MIGRACION',
        'PORTABILIDAD',
    ]

    gtr_dts = GTRealTime(varProfilePath, varDriverPath, varWppGroup, varUser, varPassword, lisCampaing)
    gtr_dts.main()