# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 01:51:08 2019

@author: 90506
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:09:37 2019

@author: 90506
"""

import os 
import pandas as pd
import numpy as np
import xlrd
df2=pd.read_excel(r'D:\October\october17\HAZUSpy.xlsx',sheet_name="WaterLevelft2")
df2["frstRES4"]=1
df2["Finalwaterlevel"]=df2["WaterLevelft"]-df2["frstRES4"]
#StructureCOM2
def EconomicCOM2(df2):
    if (df2['Finalwaterlevel']<0):
        return 0
    else:
        lossCOM2=((-0.000004*(df2['Finalwaterlevel']**6))+(0.0003*(df2['Finalwaterlevel']**5)-(0.0111*(df2['Finalwaterlevel']**4))+(0.1657*(df2['Finalwaterlevel']**3))-(1.0811*(df2['Finalwaterlevel']**2))+(5.5689*(df2['Finalwaterlevel']))+0.2406))
    return lossCOM2
#StructureCOM3
def EconomicCOM3Structure(df2):
     if(df2['Finalwaterlevel']<1):
        return 0
     else:
        lossCOM3Structure=((0.000007*(df2['Finalwaterlevel']**5)+(-0.0003*(df2['Finalwaterlevel']**4))-(0.0014*(df2['Finalwaterlevel']**3))+(0.1627*(df2['Finalwaterlevel']**2))+(1.4816*(df2['Finalwaterlevel']))+7.6625))
     return lossCOM3Structure
#StructureCOM4
def EconomicCOM4Structure(df2):
     if(df2['Finalwaterlevel']<0):
        return 0
     else:
        lossCOM4Structure=((0.00002*(df2['Finalwaterlevel']**5)+(-0.0016*(df2['Finalwaterlevel']**4))+(0.0503*(df2['Finalwaterlevel']**3))-(0.7706*(df2['Finalwaterlevel']**2))+(9.0145*(df2['Finalwaterlevel']))+1.8601))
     return lossCOM4Structure     
#StructureCOM5
def EconomicCOM5Structure(df2):
     if(df2['Finalwaterlevel']<1):
        return 0
     else:
            lossCOM5Structure=((-0.0000005*(df2['Finalwaterlevel']**6))+(0.00002*(df2['Finalwaterlevel']**5)-(0.00007*(df2['Finalwaterlevel']**4))-(0.0151*(df2['Finalwaterlevel']**3))+(0.3924*(df2['Finalwaterlevel']**2))-(0.926*(df2['Finalwaterlevel']))+11.519))
     return lossCOM5Structure    
#StructureCOM6
def EconomicCOM6Structure(df2):
     if(df2['Finalwaterlevel']<2):
        return 0
     else:
        lossCOM6Structure=((-0.00003*(df2['Finalwaterlevel']**6))+(0.0022*(df2['Finalwaterlevel']**5)-(0.0709*(df2['Finalwaterlevel']**4))+(1.1579*(df2['Finalwaterlevel']**3))-(10.012*(df2['Finalwaterlevel']**2))+(47.311*(df2['Finalwaterlevel']))-61.313))
     return lossCOM6Structure     
#StructureCOM7
def EconomicCOM7Structure(df2):
     if(df2['Finalwaterlevel']<0):
        return 0
     else:
        lossCOM7Structure=((-0.000004*(df2['Finalwaterlevel']**6))+(0.0003*(df2['Finalwaterlevel']**5)-(0.013*(df2['Finalwaterlevel']**4))+(0.23*(df2['Finalwaterlevel']**3))-(1.8446*(df2['Finalwaterlevel']**2))+(7.444*(df2['Finalwaterlevel']))+3.0076))
     return lossCOM7Structure     
#StructureCOM8
def EconomicCOM8Structure(df2):
     if(df2['Finalwaterlevel']<0):
        return 0
     else:
        lossCOM8Structure=((-0.000007*(df2['Finalwaterlevel']**6))+(0.0006*(df2['Finalwaterlevel']**5)-(0.0188*(df2['Finalwaterlevel']**4))+(0.2936*(df2['Finalwaterlevel']**3))-(2.0628*(df2['Finalwaterlevel']**2))+(7.8332*(df2['Finalwaterlevel']))+1.5849))
     return lossCOM8Structure     
#StructureCOM9
def EconomicCOM9Structure(df2):
     if(df2['Finalwaterlevel']<0):
        return 0
     else:
        lossCOM9Structure=((0.000003*(df2['Finalwaterlevel']**6))-(0.0002*(df2['Finalwaterlevel']**5)+(0.0015*(df2['Finalwaterlevel']**4))+(0.0429*(df2['Finalwaterlevel']**3))-(0.5676*(df2['Finalwaterlevel']**2))+(2.8136*(df2['Finalwaterlevel']))-0.0181))
     return lossCOM9Structure    
#StructureCOM10
def EconomicCOM10Structure(df2):
     if(df2['Finalwaterlevel']<0):
        return 0
     else: 
         lossCOM10Structure=((-0.000003*(df2['Finalwaterlevel']**6))+(0.0003*(df2['Finalwaterlevel']**5)-(0.0097*(df2['Finalwaterlevel']**4))-(0.1596*(df2['Finalwaterlevel']**3))-(0.9819*(df2['Finalwaterlevel']**2))+(3.647*(df2['Finalwaterlevel']))+0.1506))
     return lossCOM10Structure     
#StructureIND1
def EconomicIND1Structure(df2):
    if(df2['Finalwaterlevel']<0):
        return 0
    else:
        lossIND1Structure=((-0.00001*(df2['Finalwaterlevel']**6))+(0.001*(df2['Finalwaterlevel']**5)-(0.0269*(df2['Finalwaterlevel']**4))+(0.334*(df2['Finalwaterlevel']**3))-(1.8763*(df2['Finalwaterlevel']**2))+(7.8969*(df2['Finalwaterlevel']))+1.8409))
    return lossIND1Structure     
#StructureIND2
def EconomicIND2Structure(df2):
    if(df2['Finalwaterlevel']<=0):
        return 0
    else:
        lossIND2Structure=((-0.000002*(df2['Finalwaterlevel']**6))+(0.0002*(df2['Finalwaterlevel']**5)-(0.006*(df2['Finalwaterlevel']**4))+(0.1008*(df2['Finalwaterlevel']**3))-(0.9503*(df2['Finalwaterlevel']**2))+(7.7555*(df2['Finalwaterlevel']))+1.3209))
    return lossIND2Structure    
#StructureIND3
def EconomicIND3Structure(df2):
    if(df2['Finalwaterlevel']<0):
        return 0
    else:
        lossIND3Structure=((-0.000009*(df2['Finalwaterlevel']**6))+(0.0008*(df2['Finalwaterlevel']**5)-(0.0331*(df2['Finalwaterlevel']**4))+(0.6502*(df2['Finalwaterlevel']**3))-(6.7584*(df2['Finalwaterlevel']**2))+(36.627*(df2['Finalwaterlevel']))+ 1.2069))
    return lossIND3Structure   
#StructureIND4
def EconomicIN4Structure(df2):
    if(df2['Finalwaterlevel']<=0):
        return 0
    else:
        lossIND4Structure=((0.000007*(df2['Finalwaterlevel']**6))-(0.0006*(df2['Finalwaterlevel']**5)+(0.0205*(df2['Finalwaterlevel']**4))-(0.3362*(df2['Finalwaterlevel']**3))+(2.4608*(df2['Finalwaterlevel']**2))-(2.6174*(df2['Finalwaterlevel']))+10.861))
    return lossIND4Structure    
#StuctureIND5
def EconomicIND5Structure(df2):
     if(df2['Finalwaterlevel']<=0):
        return 0
     else:
        lossIND5Structure=((-0.00000005*(df2['Finalwaterlevel']**6))+(0.000002*(df2['Finalwaterlevel']**5)+(0.0003*(df2['Finalwaterlevel']**4))-(0.0127*(df2['Finalwaterlevel']**3))+(0.0722*(df2['Finalwaterlevel']**2))+(3.0068*(df2['Finalwaterlevel']))+9.267))
     return lossIND5Structure
#StructureIND6
def EconomicIND6Structure(df2):
    if(df2['Finalwaterlevel']<=0):
        return 0
    else:
        lossIND6Structure=((-0.000004*(df2['Finalwaterlevel']**6))+(0.0003*(df2['Finalwaterlevel']**5)-(0.0095*(df2['Finalwaterlevel']**4))+(0.1498*(df2['Finalwaterlevel']**3))-(1.4996*(df2['Finalwaterlevel']**2))+(11.798*(df2['Finalwaterlevel']))+ 11.863))
    return lossIND6Structure     
#StructureRES4
def EconomicRES4Structure(df2):
    if(df2['Finalwaterlevel']<=0):
        return 0
    else:
        lossRES4Structure=((-0.000007*(df2['Finalwaterlevel']**6))+(0.0006*(df2['Finalwaterlevel']**5)-(0.0179*(df2['Finalwaterlevel']**4))+(0.2572*(df2['Finalwaterlevel']**3))-(1.5034*(df2['Finalwaterlevel']**2))+(4.9288*(df2['Finalwaterlevel']))-0.7128))
    return lossRES4Structure     
#StructureRES5
def EconomicRES5Structure(df2):
    if(df2['Finalwaterlevel']<=0):
        return 0
    else:
        lossRES5Structure=((-0.000006*(df2['Finalwaterlevel']**6))+(0.0005*(df2['Finalwaterlevel']**5)-(0.0177*(df2['Finalwaterlevel']**4))+(0.2972*(df2['Finalwaterlevel']**3))-(2.3194*(df2['Finalwaterlevel']**2))+(9.2402*(df2['Finalwaterlevel']))-0.4079))
    return lossRES5Structure     
#StructureRES6
def EconomicRES6Structure(df2):
    if(df2['WaterLevelft']<=0):
        return 0
    else:
        lossRES6Structure=((-0.000006*(df2['Finalwaterlevel']**6))+(0.0005*(df2['Finalwaterlevel']**5)-(0.0177*(df2['Finalwaterlevel']**4))+(0.2972*(df2['Finalwaterlevel']**3))-(2.3194*(df2['Finalwaterlevel']**2))+(9.2402*(df2['Finalwaterlevel']))-0.4079))
    return lossRES6Structure    
#StructureEDU1
def EconomicEDU1Structure(df2):
    if (df2['Finalwaterlevel']<0):
        return 0
    else:
        lossEDU1Structure=((0.000004*(df2['Finalwaterlevel']**6))-(0.0002*(df2['Finalwaterlevel']**5)+(0.0015*(df2['Finalwaterlevel']**4))+(0.0575*(df2['Finalwaterlevel']**3))-(0.8439*(df2['Finalwaterlevel']**2))+(4.7315*(df2['Finalwaterlevel']))+ 0.3962))
    return lossEDU1Structure     
#StructureEDU2
def EconomicEDU2Structure(df2):
    if (df2['Finalwaterlevel']<0):
        return 0
    else:
        lossEDU2Structure=((0.000004*(df2['Finalwaterlevel']**6))-(0.0002*(df2['Finalwaterlevel']**5)+(0.0015*(df2['Finalwaterlevel']**4))+(0.0575*(df2['Finalwaterlevel']**3))-(0.8439*(df2['Finalwaterlevel']**2))+(4.7315*(df2['Finalwaterlevel']))+ 0.3962))
    return lossEDU2Structure     
#StructureREL1
def EconomicREL1Structure(df2):
    if (df2['Finalwaterlevel']<0):
        return 0
    else:
        lossREL1Content=((-0.00002*(df2['Finalwaterlevel']**6))+(0.0019*(df2['Finalwaterlevel']**5)-(0.0638*(df2['Finalwaterlevel']**4))+(1.0851*(df2['Finalwaterlevel']**3))-(9.8797*(df2['Finalwaterlevel']**2))+(46.103*(df2['Finalwaterlevel']))+ 11.636))
    return lossREL1Content   
#StructureGOV1
def EconomicGOV1Structure(df2):
    if (df2['Finalwaterlevel']<0):
        return 0
    else:
        lossGOV1Structure=((-0.000002*(df2['Finalwaterlevel']**6))+(0.0003*(df2['Finalwaterlevel']**5)-(0.0169*(df2['Finalwaterlevel']**4))+(0.3583*(df2['Finalwaterlevel']**3))-(3.1465*(df2['Finalwaterlevel']**2))+(12.657*(df2['Finalwaterlevel']))- 5.627))
    return lossGOV1Structure   
#StructureGOV2
def EconomicGOV2Structure(df2):
    if (df2['Finalwaterlevel']<0):
        return 0
    else:
        lossGOV2Structure=((-0.000009*(df2['Finalwaterlevel']**6))+(0.0007*(df2['Finalwaterlevel']**5)-(0.0225*(df2['Finalwaterlevel']**4))+(0.3227*(df2['Finalwaterlevel']**3))-(2.0699*(df2['Finalwaterlevel']**2))+(7.5108*(df2['Finalwaterlevel']))+ 0.488))
    return lossGOV2Structure
df2['RES6StructureDamage']=df2.apply(EconomicRES6Structure,axis=1)/100
df2['RES5StructureDamage']=df2.apply(EconomicRES5Structure,axis=1)/100
df2['RES4StructureDamage']=df2.apply(EconomicRES4Structure,axis=1)/100
df2['IND1StructureDamage']=df2.apply(EconomicIND1Structure,axis=1)/100
df2['IND2StructureDamage']=df2.apply(EconomicIND2Structure,axis=1)/100
df2['IND3StructureDamage']=df2.apply(EconomicIND3Structure,axis=1)/100
df2['IND4StructureDamage']=df2.apply(EconomicIN4Structure,axis=1)/100
df2['IND5StructureDamage']=df2.apply(EconomicIND5Structure,axis=1)/100
df2['IND6StructureDamage']=df2.apply(EconomicIND6Structure,axis=1)/100
df2['COM2StructureDamage']=df2.apply(EconomicCOM2,axis=1)/100
df2['COM3structureDamage']=df2.apply(EconomicCOM3Structure,axis=1)/100
df2['COM4structureDamage']=df2.apply(EconomicCOM4Structure,axis=1)/100
df2['COM5structureDamage']=df2.apply(EconomicCOM5Structure,axis=1)/100
df2['COM6structureDamage']=df2.apply(EconomicCOM6Structure,axis=1)/100
df2['COM7structureDamage']=df2.apply(EconomicCOM7Structure,axis=1)/100
df2['COM8structureDamage']=df2.apply(EconomicCOM8Structure,axis=1)/100
df2['COM9structureDamage']=df2.apply(EconomicCOM9Structure,axis=1)/100
df2['COM10structureDamage']=df2.apply(EconomicCOM10Structure,axis=1)/100
df2['GOV1structureDamage']=df2.apply(EconomicGOV1Structure,axis=1)/100
df2['GOV2structureDamage']=df2.apply(EconomicGOV2Structure,axis=1)/100
df2['REL1structureDamage']=df2.apply(EconomicREL1Structure,axis=1)/100
###I
df3=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM2StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM2StructureWeigh')
df4=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM3structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM3StructureWeigh')
df5=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM4structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM4StructureWeigh')
df6=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM5structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM5StructureWeigh')
df7=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM6structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM6StructureWeigh')
df8=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM7structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM7StructureWeigh')
df9=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM8structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM8StructureWeigh')
df10=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM9structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM9StructureWeigh')
df11=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["COM10structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='COM10StructureWeigh')
df12=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["REL1structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='REL1StructureWeigh')
df13=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["GOV1structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='GOV1StructureWeigh')
df14=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["GOV2structureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='GOV2StructureWeigh')
df15=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["RES4StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES4StructureWeigh')
df16=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["RES5StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES5StructureWeigh')
df17=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["RES6StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='RES6StructureWeigh')
df18=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["IND1StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND1StructureWeigh')
df19=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["IND2StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND2StructureWeigh')
df20=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["IND3StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND3StructureWeigh')
df21=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["IND4StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND4StructureWeigh')
df22=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["IND5StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND5StructureWeigh')
df23=df2.groupby("CensusBloc").apply(lambda dfx: (dfx["IND6StructureDamage"]*dfx["km2"]).sum()/dfx["km2"].sum()).reset_index(name='IND6StructureWeigh')
df24=pd.read_excel(r'C:\Users\90506\Desktop\codes\thunder.xlsx',sheet_name="Sqt4")
df_area=pd.read_excel(r'D:\October\october17\AreaInundated.xlsx',sheet_name="meet")
df_comb=pd.merge(df24,df3,on='CensusBloc',how='left')
df_comb2=pd.merge(df_comb,df4,on='CensusBloc',how='left')
df_comb3=pd.merge(df_comb2,df5,on='CensusBloc',how='left')
df_comb4=pd.merge(df_comb3,df6,on='CensusBloc',how='left')
df_comb5=pd.merge(df_comb4,df7,on='CensusBloc',how='left')
df_comb6=pd.merge(df_comb5,df8,on='CensusBloc',how='left')
df_comb7=pd.merge(df_comb6,df9,on='CensusBloc',how='left')
df_comb8=pd.merge(df_comb7,df10,on='CensusBloc',how='left')
df_comb9=pd.merge(df_comb8,df11,on='CensusBloc',how='left')
df_comb10=pd.merge(df_comb9,df12,on='CensusBloc',how='left')
df_comb11=pd.merge(df_comb10,df13,on='CensusBloc',how='left')
df_comb12=pd.merge(df_comb11,df14,on='CensusBloc',how='left')
df_comb13=pd.merge(df_comb12,df15,on='CensusBloc',how='left')
df_comb14=pd.merge(df_comb13,df16,on='CensusBloc',how='left')
df_comb15=pd.merge(df_comb14,df17,on='CensusBloc',how='left')
df_comb16=pd.merge(df_comb15,df18,on='CensusBloc',how='left')
df_comb17=pd.merge(df_comb16,df19,on='CensusBloc',how='left')
df_comb18=pd.merge(df_comb17,df20,on='CensusBloc',how='left')
df_comb19=pd.merge(df_comb18,df21,on='CensusBloc',how='left')
df_comb20=pd.merge(df_comb19,df22,on='CensusBloc',how='left')
df_comb21=pd.merge(df_comb20,df23,on='CensusBloc',how='left')
df_comb22=pd.merge(df_comb21,df_area,on='CensusBloc',how='left')

##3
##REL1
def REL1Smake1(df_comb22):
    if (df_comb22['REL1StructureWeigh']>0.5):
        return 1
    elif (df_comb22['REL1StructureWeigh']<0):
        return 0
    else:
        return df_comb22['REL1StructureWeigh']
##GOV1
def GOV1Smake1(df_comb22):
    if (df_comb22['GOV1StructureWeigh']>0.5):
        return 1
    elif (df_comb22['GOV1StructureWeigh']<0):
        return 0
    else:
        return df_comb22['GOV1StructureWeigh']
#GOV2
def GOV2Smake1(df_comb22):
    if (df_comb22['GOV2StructureWeigh']>0.5):
        return 1
    elif (df_comb22['GOV2StructureWeigh']<0):
        return 0
    else:
        return df_comb22['GOV2StructureWeigh']
#COM10
def COM10Smake1(df_comb22):
    if (df_comb22['COM10StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM10StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM10StructureWeigh']
#COM9
def COM9Smake1(df_comb22):
    if (df_comb22['COM9StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM9StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM9StructureWeigh']
#COM8
def COM8Smake1(df_comb22):
    if (df_comb22['COM8StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM8StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM8StructureWeigh']
#COM7
def COM7Smake1(df_comb22):
    if (df_comb22['COM7StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM7StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM7StructureWeigh']
#COM6
def COM6Smake1(df_comb22):
    if (df_comb22['COM6StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM6StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM6StructureWeigh']
#COM5
def COM5Smake1(df_comb22):
    if (df_comb22['COM5StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM5StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM5StructureWeigh']
#COM4
def COM4Smake1(df_comb22):
    if (df_comb22['COM4StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM4StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM4StructureWeigh']
#COM3
def COM3Smake1(df_comb22):
    if (df_comb22['COM3StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM3StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM3StructureWeigh']
#COM2
def COM2Smake1(df_comb22):
    if (df_comb22['COM2StructureWeigh']>0.5):
        return 1
    elif (df_comb22['COM2StructureWeigh']<0):
        return 0
    else:
        return df_comb22['COM2StructureWeigh']
 #IND6
def IND6Smake1(df_comb22):
    if (df_comb22['IND6StructureWeigh']>0.5):
        return 1
    elif (df_comb22['IND6StructureWeigh']<0):
        return 0
    else:
        return df_comb22['IND6StructureWeigh']  
#IND5
def IND5Smake1(df_comb22):
    if (df_comb22['IND5StructureWeigh']>0.5):
        return 1
    elif (df_comb22['IND5StructureWeigh']<0):
        return 0
    else:
        return df_comb22['IND5StructureWeigh']
#IND4
def IND4Smake1(df_comb22):
    if (df_comb22['IND4StructureWeigh']>0.5):
        return 1
    elif (df_comb22['IND4StructureWeigh']<0):
        return 0
    else:
        return df_comb22['IND4StructureWeigh']
#IND3
def IND3Smake1(df_comb22):
    if (df_comb22['IND3StructureWeigh']>0.5):
        return 1
    elif (df_comb22['IND3StructureWeigh']<0):
        return 0
    else:
        return df_comb22['IND3StructureWeigh']
#IND2
def IND2Smake1(df_comb22):
    if (df_comb22['IND2StructureWeigh']>0.5):
        return 1
    elif (df_comb22['IND2StructureWeigh']<0):
        return 0
    else:
        return df_comb22['IND2StructureWeigh']
#IND1
def IND1Smake1(df_comb22):
    if (df_comb22['IND1StructureWeigh']>0.5):
        return 1
    elif (df_comb22['IND1StructureWeigh']<0):
        return 0
    else:
        return df_comb22['IND1StructureWeigh']
#RES6
def RES6Smake1(df_comb22):
    if (df_comb22['RES6StructureWeigh']>0.5):
        return 1
    elif (df_comb22['RES6StructureWeigh']<0):
        return 0
    else:
        return df_comb22['RES6StructureWeigh']
#RES5
def RES5Smake1(df_comb22):
    if (df_comb22['RES5StructureWeigh']>0.5):
        return 1
    elif (df_comb22['RES5StructureWeigh']<0):
        return 0
    else:
        return df_comb22['RES5StructureWeigh']
#RES4
def RES4Smake1(df_comb22):
    if (df_comb22['RES4StructureWeigh']>0.5):
        return 1
    elif (df_comb22['RES4StructureWeigh']<0):
        return 0
    else:
        return df_comb22['RES4StructureWeigh']
    
df_comb22['RES4StructureWeigh']=df_comb22.apply(RES4Smake1,axis=1)
df_comb22['RES5StructureWeigh']=df_comb22.apply(RES5Smake1,axis=1)    
df_comb22['RES6StructureWeigh']=df_comb22.apply(RES6Smake1,axis=1)
df_comb22['IND1StructureWeigh']=df_comb22.apply(IND1Smake1,axis=1)       
df_comb22['IND2StructureWeigh']=df_comb22.apply(IND2Smake1,axis=1)
df_comb22['IND3StructureWeigh']=df_comb22.apply(IND3Smake1,axis=1)
df_comb22['IND4StructureWeigh']=df_comb22.apply(IND4Smake1,axis=1)
df_comb22['IND5StructureWeigh']=df_comb22.apply(IND5Smake1,axis=1)     
df_comb22['IND6StructureWeigh']=df_comb22.apply(IND6Smake1,axis=1)    
df_comb22['COM2StructureWeigh']=df_comb22.apply(COM2Smake1,axis=1) 
df_comb22['COM3StructureWeigh']=df_comb22.apply(COM3Smake1,axis=1) 
df_comb22['COM4StructureWeigh']=df_comb22.apply(COM4Smake1,axis=1)  
df_comb22['COM5StructureWeigh']=df_comb22.apply(COM5Smake1,axis=1)   
df_comb22['COM6StructureWeigh']=df_comb22.apply(COM6Smake1,axis=1)
df_comb22['COM7StructureWeigh']=df_comb22.apply(COM7Smake1,axis=1) 
df_comb22['COM8StructureWeigh']=df_comb22.apply(COM8Smake1,axis=1)   
df_comb22['COM9StructureWeigh']=df_comb22.apply(COM9Smake1,axis=1) 
df_comb22['COM10StructureWeigh']=df_comb22.apply(COM10Smake1,axis=1)        
df_comb22['REL1StructureWeigh']=df_comb22.apply(REL1Smake1,axis=1)
df_comb22['GOV1StructureWeigh']=df_comb22.apply(GOV1Smake1,axis=1)
df_comb22['GOV2StructureWeigh']=df_comb22.apply(GOV2Smake1,axis=1)
df_comb22=df_comb22.fillna(0)
df_comb22['BuildinglossRES4Py']=df_comb22['RES4']*df_comb22['RES4StructureWeigh']*182.28*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossRES5Py']=df_comb22['RES5']*df_comb22['RES5StructureWeigh']*199.63*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossRES6Py']=df_comb22['RES6']*df_comb22['RES6StructureWeigh']*215.91*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM2Py']=df_comb22['COM2']*df_comb22['COM2StructureWeigh']*120*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM3Py']=df_comb22['COM3']*df_comb22['COM3StructureWeigh']*139.88*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM4Py']=df_comb22['COM4']*df_comb22['COM4StructureWeigh']*176.29*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM5Py']=df_comb22['COM5']*df_comb22['COM5StructureWeigh']*261.33*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM6Py']=df_comb22['COM6']*df_comb22['COM6StructureWeigh']*302.35*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM7Py']=df_comb22['COM7']*df_comb22['COM7StructureWeigh']*226.54*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM8Py']=df_comb22['COM8']*df_comb22['COM8StructureWeigh']*227.53*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM9Py']=df_comb22['COM9']*df_comb22['COM9StructureWeigh']*190.95*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossCOM10Py']=df_comb22['COM10']*df_comb22['COM10StructureWeigh']*80.59*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossIND1Py']=df_comb22['IND1']*df_comb22['IND1StructureWeigh']*133.03*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossIND2Py']=df_comb22['IND2']*df_comb22['IND2StructureWeigh']*120.00*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossIND3Py']=df_comb22['IND3']*df_comb22['IND3StructureWeigh']*180.47*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossIND4Py']=df_comb22['IND4']*df_comb22['IND4StructureWeigh']*180.47*df_comb22['PortionAreaInundated']
#df_comb21['BuildinglossIND5Py']=df_comb21['IND5']*df_comb21['IND5StructureWeigh']*180.47
df_comb22['BuildinglossIND6Py']=df_comb22['IND6']*df_comb22['IND6StructureWeigh']*120.00*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossREL1Py']=df_comb22['REL1']*df_comb22['REL1StructureWeigh']*190.53*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossGOV1Py']=df_comb22['GOV1']*df_comb22['GOV1StructureWeigh']*149.83*df_comb22['PortionAreaInundated']
df_comb22['BuildinglossGOV2Py']=df_comb22['GOV2']*df_comb22['GOV2StructureWeigh']*254.23*df_comb22['PortionAreaInundated']
dfa=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM2")
dfb=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM3")
dfc=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM4")
dfd=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM5")
dfe=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM6")
dff=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM7")
dfg=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM8")
dfh=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM9")
dfj=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="COM10")
dfk=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="IND1")
dfl=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="IND2")
dfz=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="IND3")
dfex=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="IND4")
dfc=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="IND5")
dfr=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="RES4")
dft=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="RES5")
dfy=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="RES6")
dfu=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="REL1")
dfo=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="GOV1")
dfot=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="GOV2")
dfof=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="EDU1")
dfots=pd.read_excel(r'D:\October\october17\HAZUSResults\HAZUSresult.xlsx',sheet_name="EDU2")
df_comb23=pd.merge(df_comb22,dfa,on='CensusBloc',how='left')
df_comb24=pd.merge(df_comb23,dfb,on='CensusBloc',how='left')
df_comb25=pd.merge(df_comb24,dfc,on='CensusBloc',how='left')
df_comb26=pd.merge(df_comb25,dfd,on='CensusBloc',how='left')
df_comb27=pd.merge(df_comb26,dfe,on='CensusBloc',how='left')
df_comb28=pd.merge(df_comb27,dff,on='CensusBloc',how='left')
df_comb29=pd.merge(df_comb28,dfg,on='CensusBloc',how='left')
df_comb30=pd.merge(df_comb29,dfh,on='CensusBloc',how='left')
df_comb31=pd.merge(df_comb30,dfj,on='CensusBloc',how='left')
df_comb32=pd.merge(df_comb31,dfk,on='CensusBloc',how='left')
df_comb33=pd.merge(df_comb32,dfl,on='CensusBloc',how='left')
df_comb34=pd.merge(df_comb33,dfz,on='CensusBloc',how='left')
df_comb35=pd.merge(df_comb34,dfex,on='CensusBloc',how='left')
df_comb36=pd.merge(df_comb35,dfc,on='CensusBloc',how='left')
df_comb37=pd.merge(df_comb36,dfr,on='CensusBloc',how='left')
df_comb38=pd.merge(df_comb37,dft,on='CensusBloc',how='left')
df_comb39=pd.merge(df_comb38,dfy,on='CensusBloc',how='left')
df_comb40=pd.merge(df_comb39,dfu,on='CensusBloc',how='left')
df_comb41=pd.merge(df_comb40,dfo,on='CensusBloc',how='left')
df_comb42=pd.merge(df_comb41,dfot,on='CensusBloc',how='left')
df_comb43=pd.merge(df_comb42,dfof,on='CensusBloc',how='left')
df_comb44=pd.merge(df_comb43,dfots,on='CensusBloc',how='left')
#NA'leri 0 yapmadan dene.
#ayrı bir yerde dene bu analizi problemli olanlar için. 

df_comb44=df_comb44.fillna(0)
df_comb44.to_excel(r'D:\October\october17\hmm2.xlsx',sheet_name="hazal")
print(df_comb44)

#ilki daha mantıklı

#df3=pd.read_excel(r'',sheet_name="")
#df=pd.read_excel(r'D:\October\october17\AreaInundated.xlsx',sheet_name="meet")