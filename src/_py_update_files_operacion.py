# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:40:15 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

import time
from tqdm import tqdm
import win32com.client as win32

#%% Create class

class UpdateFilesOperacion:
    def __init__(self, lisExcelPaths):
        self.lisExcelPaths = lisExcelPaths

    def update_files(self):
        excel_app = win32.DispatchEx("Excel.Application")
        excel_app.DisplayAlerts = False
        excel_app.Visible = False
        
        for excel_path in tqdm(self.lisExcelPaths, desc='Updating Files'):
            workbook = excel_app.Workbooks.Open(excel_path)
            workbook.RefreshAll()
            excel_app.CalculateUntilAsyncQueriesDone()

            for sheet in workbook.Sheets:
                for pivot_table in sheet.PivotTables():
                    pivot_table.RefreshTable()
                    time.sleep(2)
            
            workbook.Save()
            workbook.Close(False)

        excel_app.Quit()
        del excel_app

    def main(self):
        self.update_files()

#%% Use class

if __name__ == "__main__":
    lisExcelPaths = [
        r'path/to/file.xlsx',
    ]

    script = UpdateFilesOperacion(lisExcelPaths)
    script.main()
