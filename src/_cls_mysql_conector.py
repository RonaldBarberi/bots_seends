# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:24:30 2024

@author: Ronal.Barberi
"""

#%% Imported libraries

from urllib.parse import quote
from sqlalchemy import create_engine

#%% Create Class

class MySQLConnector:

    @staticmethod
    def funConectSql68(varSchema):
        varDbms = 'mysql+mysqldb'
        varUser = 'ronaldbarberi2999'
        varHost = "172.17.8.999"
        varPort = "3306"
        varPass = quote('passwordtoserver')
        cadena = f"{varDbms}://{varUser}:{varPass}@{varHost}:{varPort}/{varSchema}"
        engine = create_engine(cadena)
        return engine

    @staticmethod
    def funConectSql61(varSchema):
        varDbms = 'mysql+mysqldb'
        varUser = 'ronaldbarberi2999'
        varHost = '172.70.7.888'
        varPort = '3306'
        varPass = quote('passwordtoserver')
        cadena = f"{varDbms}://{varUser}:{varPass}@{varHost}:{varPort}/{varSchema}"
        engine = create_engine(cadena)
        return engine

    @staticmethod
    def funConectSql60(varSchema):
        varDbms = 'mysql+mysqldb'
        varUser = 'ronaldbarberi2999'
        varHost = '172.70.7.777'
        varPort = '3306'
        varPass = quote('passwordtoserver')
        cadena = f"{varDbms}://{varUser}:{varPass}@{varHost}:{varPort}/{varSchema}"
        engine = create_engine(cadena)
        return engine

    def close_engine(engine):
        engine.dispose()
