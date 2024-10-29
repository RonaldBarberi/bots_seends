# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:07:57 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

import os
import json
import zipfile
from datetime import datetime
import win32com.client as win32
from _cls_excel_img import Excel_Img
from _cls_nav_directorys import Nav_Directorys as nd

#%% Create Class

class UpdateSeendMail:
    def __init__(self, varMathJson, varExcelsPath, varPathZip, varImgFolder, varWppGroup, dicArgs):
            self.varMathJson = varMathJson
            self.varExcelsPath = varExcelsPath
            self.varPathZip = varPathZip
            self.varImgFolder = varImgFolder
            self.varWppGroup = varWppGroup
            self.dicArgs = dicArgs

    def read_json(self):
        self.varRangos = {}
        self.varTxtWpp = []
        for json_path in self.varMathJson:
            with open(json_path, 'r') as file:
                args = json.load(file)
            for key, value in args.items():
                self.varRangos[key] = value[0]['range']
                self.varTxtWpp.append((key, value[0]['description']))
    
    def update_workbooks(self):
        self.read_json()
        for excel in self.varExcelsPath:
            excl_img = Excel_Img(excel, self.varRangos, self.varImgFolder, self.varWppGroup)
            excl_img.main()

    def compress_data(self):
        with zipfile.ZipFile(self.varPathZip, 'w') as zipf:
            for path in varExcelsPath:
                name_file = os.path.basename(path)
                zipf.write(path, arcname=name_file)

    def seend_mail(self):
        outlook_app = win32.Dispatch('Outlook.Application')
        outlook_app.GetNamespace('MAPI')
        message = outlook_app.CreateItem(0)
        message.To = self.dicArgs['Destinatario']
        message.CC = self.dicArgs['Copia']
        message.BCC = self.dicArgs['CopiaOculta']
        message.Subject = self.dicArgs['Asunto']
        os.path.basename(self.dicArgs['Imagen'])
        attachment = message.Attachments.Add(self.dicArgs['Imagen'])
        attachment.PropertyAccessor.SetProperty('http://schemas.microsoft.com/mapi/proptag/0x3712001F', 'image_cid')
        message.HTMLBody = f"""
        <html>
            <body>
                <p>Buen día,</p>
                <p>{self.dicArgs['Mensaje']}</p>
                <img src="cid:image_cid">
                <p>Greetings!,</p>
                <p>Ronald Barberi,</p>
                <p>Datamining</p>
            </body>
        </html>
        """
        attachment_path = os.path.abspath(self.varPathZip)
        message.Attachments.Add(attachment_path)
        try:
            message.Send()
            print('Mensaje enviado exitosamente.')
        except Exception as e:
            print('Error al enviar el correo, por favor validar:', e)

    def main(self):
        self.read_json()
        self.update_workbooks()
        self.compress_data()
        self.seend_mail()

#%% Use class

curdate = datetime.today()
curdate = curdate.strftime('%d/%m/%Y')

if __name__ == "__main__":
    varMathJson = [
        nd.funJoinThreeDic(nd.funDicOneBack(), 'data', 'json', 'mail_head_count.json'),
        nd.funJoinThreeDic(nd.funDicOneBack(), 'data', 'json', 'mail_ausentismo.json'),
        nd.funJoinThreeDic(nd.funDicOneBack(), 'data', 'json', 'mail_conection_auxiliares.json'),
    ]
    varExcelsPath = [
        r'first\path\to\file.xlsx',
        r'second\path\to\file.xlsx',
    ]
    varPathZip = nd.funJoinTwoDic(nd.funDicOneBack(), 'data', 'informes_clarotmk_bog.zip')
    varImgFolder = nd.funJoinOneDic(nd.funDicOneBack(), 'data')
    varWppGroup = 'ClaroTMK Bogota - DTS'
    dicArgs = {
        'Destinatario': 'remitente_1@outlook.com; remitente_2@outlook.com; remitente_3@outlook.com;',
        'Copia': 'copia_1@outlook.com; copia_2@outlook.com; copia_3@outlook.com;',
        'CopiaOculta': '',
        'Asunto': 'Presentación Repo GitHub' + curdate,
        'Mensaje': f"""
            • Look my perfil to Linkedin!. <br> <br>
            • Look my perfil to Instagram. <br> <br>
            """,
        'Imagen': nd.funJoinTwoDic(nd.funDicOneBack(), 'data', 'img_to_seend.jpg'),
    }

    script = UpdateSeendMail(varMathJson, varExcelsPath, varPathZip, varImgFolder, varWppGroup, dicArgs)
    script.main()
