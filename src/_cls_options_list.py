# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 15:41:48 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

import tkinter as tk
from tkinter import messagebox

#%% Create Class

class SelectOption:
    def __init__(self, args):
        self.args = args
        self.selection = None
    
    def select(self):
        self.root = tk.Tk()
        self.root.title('DataScience')
        self.listbox = tk.Listbox(self.root)
        for key in self.args:
            self.listbox.insert(tk.END, key)
        self.listbox.pack(padx=60, pady=0)
        select_button = tk.Button(self.root, text='Seleccionar', command=self.get_selection)
        select_button.pack(padx=20, pady=5)
        self.root.mainloop()
    
    def get_selection(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_key = self.listbox.get(selected_index)
            self.selection = {selected_key: self.args[selected_key]}
            self.root.destroy()
        else:
            messagebox.showerror('Error', 'Por favor, selecciona una opción.')
    
    def main(self):
        self.select()
        return self.selection

#%% Use class

"""
if __name__ == "__main__":
	year_month = '202408'
	day = '20'
	dicArgs = {
		'CLARVEN3': ('CLARVEN3 - 0020205 CLAR MOVIL CS', f'Z:/WORKFORCE/02. Workforce/WFM_CAMPANAS/claro_ventas_bogota_tmk/BASES_DTS/PREDICTIVO/{year_month}/{day}/MIGRACION'),
		'CLAROV4': ('CLAROV4 - 0020205 MOVIL MIGRA CS', f'Z:/WORKFORCE/02. Workforce/WFM_CAMPANAS/claro_ventas_bogota_tmk/BASES_DTS/PREDICTIVO/{year_month}/{day}/PORTABILIDAD'),
	}
	etl = SelectOption(dicArgs)
	selection = etl.main()
	print(selection)

	print(dicArgs)
	print(list(dicArgs.keys())[0])
	print(dicArgs['CLARVEN3'][0])
	print(dicArgs['CLARVEN3'][1])
"""