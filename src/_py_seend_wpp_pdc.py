# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:40:15 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

import os
import json
from _cls_excel_img import Excel_Img, SeendMsg_Wpp
from _cls_nav_directorys import Nav_Directorys as nd

#%% create class

class Seend_PDC_TMK:
    def __init__(self, lisPathJson, lisExcelFilesPath, varImageFolder, varWppGroup, varDriverPath, varProfilePath):
        self.lisPathJson = lisPathJson
        self.lisExcelFilesPath = lisExcelFilesPath
        self.varImageFolder = varImageFolder
        self.varWppGroup = varWppGroup
        self.varDriverPath = varDriverPath
        self.varProfilePath = varProfilePath
    
    def read_json(self):
        self.rangos = {}
        self.text_wpp = []
        for json_path in self.lisPathJson:
            with open(json_path, 'r') as file:
                args = json.load(file)
            for key, value in args.items():
                self.rangos[key] = value[0]['range']
                self.text_wpp.append((key, value[0]['description']))
    
    def main(self):
        self.read_json()
        for excel_path in self.lisExcelFilesPath:
            excl_img = Excel_Img(excel_path, self.rangos, self.varImageFolder, self.varWppGroup)
            excl_img.main()
        message = SeendMsg_Wpp(self.varDriverPath, self.varProfilePath, self.varWppGroup, self.text_wpp, self.varImageFolder)
        message.main()

#%% Use class

varUserNow = os.getlogin()

if __name__ == "__main__":
    lisPathJson = [
        nd.funJoinThreeDic(nd.funDicOneBack(), 'data', 'json', 'wpp_pdc.json'),
        nd.funJoinThreeDic(nd.funDicOneBack(), 'data', 'json', 'productividad.json'),
    ]
    lisExcelFilesPath = [
        r'first\path\to\file.xlsx',
        r'second\path\to\file.xlsx',
    ]
    varImageFolder = nd.funJoinTwoDic(nd.funDicOneBack(), 'data', 'img_pdc')
    varWppGroup = 'Calculo de Varias en Variables'
    varDriverPath = nd.funJoinTwoDic(nd.funDicOneBack(), 'config', 'chromedriver.exe')
    varProfilePath = os.path.expanduser('~/Command_Center/Profile_save')

    pdc = Seend_PDC_TMK(lisPathJson, lisExcelFilesPath, varImageFolder, varWppGroup, varDriverPath, varProfilePath)
    pdc.main()
