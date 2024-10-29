# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:35:32 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

import time
import pandas as pd
from tqdm import tqdm
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.mysql import insert

#%% Create class

class SqlAchemy:
    
    def funExecuteQuery(objConection, varSp):
        if isinstance(varSp, str):
            varSp = [varSp]
        print('Executing')
        with objConection.connect() as connection:
            for query in varSp:
                transaction = connection.begin()
                try:
                    start_time = time.time()
                    query_execute = text(query)
                    connection.execute(query_execute)
                    transaction.commit()
                    end_time = time.time()
                    duration = end_time - start_time
                    duration_round = round(duration, 2)
                    print(f'Action: {query} || Message: correct || Duration: {duration_round}')
                    time.sleep(1)
                except SQLAlchemyError as e:
                    transaction.rollback()
                    print(f'Error: {query}, ', e)
                except Exception as e:
                    print(f'Error inesperado: {query}, ', e)
        

    def funExportDF_csv(objConection, varQueryDF, varPathExport, varNameFile):
        df = pd.read_sql_query(varQueryDF, objConection)
        full_path = varPathExport + f'/{varNameFile}.csv'
        df.to_excel(full_path, index=False)


    def funExportDF_csv_InChunksize(objConection, varQueryDF, varPathExport, varNameFile, varChunk):
        file_count = 1
        for df_chunk in tqdm(pd.read_sql_query(varQueryDF, objConection, chunksize=varChunk), desc='Exporting data'):
            filename = f'{varPathExport}/{varNameFile}_{file_count}.csv'
            df_chunk.to_csv(filename, mode='w', sep=',', index=False, float_format='%.2f')
            file_count += 1
            time.sleep(1)


    def funExportDF_xlsx(objConection, varQueryDF, varPathExport, varNameFile):
        df = pd.read_sql_query(varQueryDF, objConection)
        full_path = varPathExport + f'/{varNameFile}.xlsx'
        df.to_excel(full_path, index=False)


    def funExportDF_xlsx_InChunksize(objConection, varQueryDF, varPathExport, varNameFile, varChunk):
        file_count = 1
        for df_chunk in tqdm(pd.read_sql_query(varQueryDF, objConection, chunksize=varChunk), desc='Exporting data'):
            filename = f'{varPathExport}/{varNameFile}_{file_count}.xlsx'
            df_chunk.to_excel(filename, index=False, float_format='%.2f', engine='openpyxl')
            file_count += 1
            time.sleep(1)


    def funInsertDFNotTruncate(objConection, varDfUpdate, varSchema, varTable): 
        
        def funInsertOnDuplicate(table, conn, key, data_iter):
            insert_stmt = insert(table.table).values(list(data_iter)) 
            on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(insert_stmt.inserted)
            conn.execute(on_duplicate_key_stmt) 

        varDfUpdate.to_sql(name=varTable, con=objConection, schema=varSchema, if_exists='append', index=False,  method=funInsertOnDuplicate, chunksize=10000)
        print(f'Insert/Update {varDfUpdate.shape[0]}')


    def funInsertDFYesTruncate(objConection, varDfUpdate, varSchema, varTable): 
        tc_query = f'TRUNCATE TABLE `{varSchema}`.`{varTable}`;'
        truncate_query = text(tc_query)
        connection = objConection.connect()
        connection.execute(truncate_query)
        print(f'Truncate {varTable}')
        
        def funInsertOnDuplicate(table, conn, key, data_iter):
            insert_stmt = insert(table.table).values(list(data_iter)) 
            on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(insert_stmt.inserted)
            conn.execute(on_duplicate_key_stmt) 
            
        varDfUpdate.to_sql(name=varTable, con=objConection, schema=varSchema, if_exists='append', index=False,  method=funInsertOnDuplicate, chunksize=10000)
        print(f'Insert/Update {varDfUpdate.shape[0]}')

    def funDropTable(objConection, varSchema, varTable):
        query = f"DROP TABLE `{varSchema}`.`{varTable}`;"
        with objConection.connect() as connection:
            transaction = connection.begin()
            try:
                start_time = time.time()
                query_execute = text(query)
                connection.execute(query_execute)
                transaction.commit()
                end_time = time.time()
                duration = end_time - start_time
                duration_round = round(duration, 2)
                print(f'Action: {query} || Message: correct || Duration: {duration_round}')
            except SQLAlchemyError as e:
                transaction.rollback()
                print(f'Error: {query}, ', e)
            except Exception as e:
                print(f'Error inesperado: {query}, ', e)
                