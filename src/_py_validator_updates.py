# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 09:41:48 2024

@author: Ronal.Barberi
"""

#%% Import libraries

from tqdm import tqdm
import requests
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from _cls_mysql_conector import MySQLConnector as ms
from _cls_nav_directorys import Nav_Directorys as nd

#%% Create class

class ValidatorUpdateTables:
    def __init__(self, varSchema, listPathQuery, varPathSaveImg, varToken, varChatId):
        self.varSchema = varSchema
        self.engine = ms.funConectSql60(varSchema)
        self.listPathQuery = listPathQuery
        self.varPathSaveImg = varPathSaveImg
        self.varToken = varToken
        self.varChatId = varChatId

    def excute_query(self, query):
        with open(query, "r") as sql_file:
            exec_query = sql_file.read()
            df = pd.read_sql_query(exec_query, self.engine)
            self.df = df

    def dataframe_to_image(self):
        padding = 8
        font_size = 11
        font = ImageFont.truetype("consola.ttf", font_size)

        max_col_width = [max(self.df[col].astype(str).map(len).max(), len(col)) * font_size for col in self.df.columns]
        img_width = sum(max_col_width) + padding * (len(self.df.columns) + 1)
        img_height = (len(self.df) + 1) * (font_size + padding)
        img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        y_start = padding
        y_end = img_height - padding
        x_start = padding
        x_end = img_width - padding
        y_offset = padding
        for i in range(len(self.df) + 1):
            draw.line([(x_start, y_offset), (x_end, y_offset)], fill='black', width=1)
            y_offset += font_size + padding
        x_offset = padding
        for width in max_col_width:
            draw.line([(x_offset, y_start), (x_offset, y_end)], fill='black', width=1)
            x_offset += width + padding
        draw.line([(x_offset, y_start), (x_offset, y_end)], fill='black', width=1)

        x_offset = padding
        for i, col in enumerate(self.df.columns):
            draw.text((x_offset, padding), col, font=font, fill=(0, 0, 0))
            x_offset += max_col_width[i] + padding

        y_offset = font_size + 2 * padding
        for index, row in self.df.iterrows():
            x_offset = padding
            for i, value in enumerate(row):
                draw.text((x_offset, y_offset), str(value), font=font, fill=(0, 0, 0))
                x_offset += max_col_width[i] + padding
            y_offset += font_size + padding
        img.save(self.varPathSaveImg)

    def enviar_imagen_por_telegram(self):
        url_telegram = f"https://api.telegram.org/bot{self.varToken}/sendPhoto"
        with open(self.varPathSaveImg, 'rb') as imagen:
            parametros = {
                'chat_id': self.varChatId
            }
            archivos = {
                'photo': imagen
            }
            response = requests.post(url_telegram, data=parametros, files=archivos)
            return response.json()

    def main(self):
        for query in tqdm(self.listPathQuery, desc='Seend Resports'):
            self.excute_query(query)
            self.dataframe_to_image()
            self.enviar_imagen_por_telegram()

#%% Use class

if __name__ == "__main__":
    varSchema = 'bbdd_cs_bog_tmk'
    listPathQuery = [
        nd.funJoinTwoDic(nd.funDicOneBack(), 'sql', 'sql_validator_update_all_tables.sql'),
        nd.funJoinTwoDic(nd.funDicOneBack(), 'sql', 'sql_validator_update_bdds.sql')
    ]
    varPathSaveImg = nd.funJoinTwoDic(nd.funDicOneBack(), 'data', 'img_update.png')
    varToken = 'tokentobotinTelegram'
    varChatId = 'idchattobotinTelegram'

    update_process = ValidatorUpdateTables(varSchema, listPathQuery, varPathSaveImg, varToken, varChatId)
    update_process.main()
