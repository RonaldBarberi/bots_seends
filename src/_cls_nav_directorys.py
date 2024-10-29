    # -*- coding: utf-8 -*-
"""
Created on Tue Juns 14 09:05:20 2024

@author: Ronal.Barberi
"""

#%% Import libraries

import os

#%% Create class

class Nav_Directorys:
    
    def funDicCurrent():
        varCurrentFolder = os.path.dirname(os.path.abspath(__file__))
        return varCurrentFolder
    
    def funDicOneBack():
        varCurrentFolder = Nav_Directorys.funDicCurrent()
        varBackOneFolder = os.path.dirname(varCurrentFolder)
        return varBackOneFolder
    
    def funDicTwoBack():
        varBackOneFolder = Nav_Directorys.funDicOneBack()
        varBackTwoFolder = os.path.dirname(varBackOneFolder)
        return varBackTwoFolder
    
    def funDicThreeBack():
        varBackTwoFolder = Nav_Directorys.funDicTwoBack()
        varBackThreeFolder = os.path.dirname(varBackTwoFolder)
        return varBackThreeFolder
    
    def funJoinOneDic(varDicCurrent, varOneJoin):
        return os.path.join(varDicCurrent, varOneJoin)
    
    def funJoinTwoDic(varDicCurrent, varOneJoin, varTwoJoin):
        return os.path.join(varDicCurrent, varOneJoin, varTwoJoin)
    
    def funJoinThreeDic(varDicCurrent, varOneJoin, varTwoJoin, varThreeJoin):
        return os.path.join(varDicCurrent, varOneJoin, varTwoJoin, varThreeJoin)
