# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:49:42 2023

@author: mahta
"""
import os
import pandas as pd
import numpy as np
#%%Read the CSV file deox_period of each model each senarios 

#gfdl

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his')
input_file_path = 'deox_period_surf_gfdl_his.csv'  # Replace with your actual input file path
df_deox_period_surf_gfdl_his = pd.read_csv(input_file_path)

#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26')
input_file_path = 'deox_period_surf_gfdl_rcp26.csv'  # Replace with your actual input file path
df_deox_period_surf_gfdl_rcp26 = pd.read_csv(input_file_path)

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60')
input_file_path = 'deox_period_surf_gfdl_rcp60.csv'  # Replace with your actual input file path
df_deox_period_surf_gfdl_rcp60 = pd.read_csv(input_file_path)

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85')
input_file_path = 'deox_period_surf_gfdl_rcp85.csv'  # Replace with your actual input file path
df_deox_period_surf_gfdl_rcp85 = pd.read_csv(input_file_path)


#hadgem

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his')
input_file_path = 'deox_period_surf_hadgem_his.csv'  # Replace with your actual input file path
df_deox_period_surf_hadgem_his = pd.read_csv(input_file_path)

#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26')
input_file_path = 'deox_period_surf_hadgem_rcp26.csv'  # Replace with your actual input file path
df_deox_period_surf_hadgem_rcp26 = pd.read_csv(input_file_path)

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60')
input_file_path = 'deox_period_surf_hadgem_rcp60.csv'  # Replace with your actual input file path
df_deox_period_surf_hadgem_rcp60 = pd.read_csv(input_file_path)

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85')
input_file_path = 'deox_period_surf_hadgem_rcp85.csv'  # Replace with your actual input file path
df_deox_period_surf_hadgem_rcp85 = pd.read_csv(input_file_path)

#ipsl

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his')
input_file_path = 'deox_period_surf_ipsl_his.csv'  # Replace with your actual input file path
df_deox_period_surf_ipsl_his = pd.read_csv(input_file_path)

#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26')
input_file_path = 'deox_period_surf_ipsl_rcp26.csv'  # Replace with your actual input file path
df_deox_period_surf_ipsl_rcp26 = pd.read_csv(input_file_path)

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60')
input_file_path = 'deox_period_surf_ipsl_rcp60.csv'  # Replace with your actual input file path
df_deox_period_surf_ipsl_rcp60 = pd.read_csv(input_file_path)

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85')
input_file_path = 'deox_period_surf_ipsl_rcp85.csv'  # Replace with your actual input file path
df_deox_period_surf_ipsl_rcp85 = pd.read_csv(input_file_path)

#miroc 

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his')
input_file_path = 'deox_period_surf_miroc_his.csv'  # Replace with your actual input file path
df_deox_period_surf_miroc_his = pd.read_csv(input_file_path)

#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26')
input_file_path = 'deox_period_surf_miroc_rcp26.csv'  # Replace with your actual input file path
df_deox_period_surf_miroc_rcp26 = pd.read_csv(input_file_path)

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60')
input_file_path = 'deox_period_surf_miroc_rcp60.csv'  # Replace with your actual input file path
df_deox_period_surf_miroc_rcp60 = pd.read_csv(input_file_path)

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85')
input_file_path = 'deox_period_surf_miroc_rcp85.csv'  # Replace with your actual input file path
df_deox_period_surf_miroc_rcp85 = pd.read_csv(input_file_path)

#%%his 

df_deox_period_surf_gfdl_his
df_deox_period_surf_hadgem_his
df_deox_period_surf_ipsl_his
df_deox_period_surf_miroc_his

#%%rcp26 

df_deox_period_surf_gfdl_rcp26
df_deox_period_surf_hadgem_rcp26
df_deox_period_surf_ipsl_rcp26
df_deox_period_surf_miroc_rcp26

#%%rcp60 

df_deox_period_surf_gfdl_rcp60
df_deox_period_surf_hadgem_rcp60
df_deox_period_surf_ipsl_rcp60
df_deox_period_surf_miroc_rcp60


#%%rcp85 

df_deox_period_surf_gfdl_rcp85
df_deox_period_surf_hadgem_rcp85
df_deox_period_surf_ipsl_rcp85
df_deox_period_surf_miroc_rcp85


#%%annual_deox_duarion

def annual_deox_duarion (df_deox):
    deox_duarion=df_deox.groupby(df_deox['year'])['deox_duration'].sum()
    return (deox_duarion)

#%% his 

deox_dur_gfdl_his=annual_deox_duarion(df_deox_period_surf_gfdl_his)
deox_dur_hadgem_his=annual_deox_duarion(df_deox_period_surf_hadgem_his)
deox_dur_ipsl_his=annual_deox_duarion(df_deox_period_surf_ipsl_his)
deox_dur_miroc_his=annual_deox_duarion(df_deox_period_surf_miroc_his) 

# geting average of 4 GCMs simply 
deox_dur_mean4models_his= np.round((deox_dur_gfdl_his +deox_dur_hadgem_his +deox_dur_ipsl_his+ deox_dur_miroc_his)/4 , 0)
    



#Glue of duration of deoxygenation period for different GCMs model without ranking them 

all_deox_dur_his = pd.concat([deox_dur_gfdl_his, deox_dur_hadgem_his, deox_dur_ipsl_his, deox_dur_miroc_his], axis=1)




quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_deox_dur_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_deox_dur_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_deox_dur_his= glue_df_deox_dur_his.set_index(all_deox_dur_his.index)



#%% saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_deox_dur_his.csv'

glue_df_deox_dur_his.to_csv(file_path )

#%% rcp26 

deox_dur_gfdl_rcp26=annual_deox_duarion(df_deox_period_surf_gfdl_rcp26)
deox_dur_hadgem_rcp26=annual_deox_duarion(df_deox_period_surf_hadgem_rcp26)
deox_dur_ipsl_rcp26=annual_deox_duarion(df_deox_period_surf_ipsl_rcp26)
deox_dur_miroc_rcp26=annual_deox_duarion(df_deox_period_surf_miroc_rcp26) 
# geting average of 4 GCMs simply 
deox_dur_mean4models_rcp26= np.round((deox_dur_gfdl_rcp26 +deox_dur_hadgem_rcp26 +deox_dur_ipsl_rcp26+ deox_dur_miroc_rcp26)/4 , 0)
   

#Glue of duration of deoxygenation period for different GCMs model without ranking them 

all_deox_dur_rcp26 = pd.concat([deox_dur_gfdl_rcp26, deox_dur_hadgem_rcp26, deox_dur_ipsl_rcp26, deox_dur_miroc_rcp26], axis=1)




quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_deox_dur_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_deox_dur_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_deox_dur_rcp26= glue_df_deox_dur_rcp26.set_index(all_deox_dur_rcp26.index)



#%% saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_deox_dur_rcp26.csv'

glue_df_deox_dur_rcp26.to_csv(file_path )


#%% rcp60 

deox_dur_gfdl_rcp60=annual_deox_duarion(df_deox_period_surf_gfdl_rcp60)
deox_dur_hadgem_rcp60=annual_deox_duarion(df_deox_period_surf_hadgem_rcp60)
deox_dur_ipsl_rcp60=annual_deox_duarion(df_deox_period_surf_ipsl_rcp60)
deox_dur_miroc_rcp60=annual_deox_duarion(df_deox_period_surf_miroc_rcp60) 


# geting average of 4 GCMs simply 
deox_dur_mean4models_rcp60= np.round((deox_dur_gfdl_rcp60 +deox_dur_hadgem_rcp60 +deox_dur_ipsl_rcp60+ deox_dur_miroc_rcp60)/4 , 0)
   
#Glue of duration of deoxygenation period for different GCMs model without ranking them 

all_deox_dur_rcp60 = pd.concat([deox_dur_gfdl_rcp60, deox_dur_hadgem_rcp60, deox_dur_ipsl_rcp60, deox_dur_miroc_rcp60], axis=1)




quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_deox_dur_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_deox_dur_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_deox_dur_rcp60= glue_df_deox_dur_rcp60.set_index(all_deox_dur_rcp60.index)



#%% saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_deox_dur_rcp60.csv'

glue_df_deox_dur_rcp60.to_csv(file_path )

#%% rcp85 

deox_dur_gfdl_rcp85=annual_deox_duarion(df_deox_period_surf_gfdl_rcp85)
deox_dur_hadgem_rcp85=annual_deox_duarion(df_deox_period_surf_hadgem_rcp85)
deox_dur_ipsl_rcp85=annual_deox_duarion(df_deox_period_surf_ipsl_rcp85)
deox_dur_miroc_rcp85=annual_deox_duarion(df_deox_period_surf_miroc_rcp85) 

# geting average of 4 GCMs simply 
deox_dur_mean4models_rcp85= np.round((deox_dur_gfdl_rcp85 +deox_dur_hadgem_rcp85 +deox_dur_ipsl_rcp85+ deox_dur_miroc_rcp85)/4 , 0)
   
#Glue of duration of deoxygenation period for different GCMs model without ranking them 

all_deox_dur_rcp85 = pd.concat([deox_dur_gfdl_rcp85, deox_dur_hadgem_rcp85, deox_dur_ipsl_rcp85, deox_dur_miroc_rcp85], axis=1)




quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_deox_dur_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_deox_dur_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_deox_dur_rcp85= glue_df_deox_dur_rcp85.set_index(all_deox_dur_rcp85.index)



#%% saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_deox_dur_rcp85.csv'

glue_df_deox_dur_rcp85.to_csv(file_path )

#%%80 years for GCMs 
###########################################rcp26
#gfdl
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp26[all_deox_dur_rcp26.index>2019].iloc[:, 0])
"""
(0.026317653106537837,
 'positively autocorrelated',
 'no trend',
 0.38542344694889863,
 0,
 0)
"""

#hadgem
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp26[all_deox_dur_rcp26.index>2019].iloc[:, 1])
"""
(0.018441487199747603,
 'positively autocorrelated',
 'no trend',
 0.12899178758994245,
 0,
 0)
"""

#ipsl
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp26[all_deox_dur_rcp26.index>2019].iloc[:, 2])
"""
(0.03214136761745879,
 'positively autocorrelated',
 'no trend',
 0.0563883360384414,
 0,
 0)
"""

#miroc
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp26[all_deox_dur_rcp26.index>2019].iloc[:, 3])
"""
(0.021191580949209147,
 'positively autocorrelated',
 'no trend',
 0.3764767231764572,
 0,
 0)
"""


###########################################rcp60
#gfdl
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp60[all_deox_dur_rcp60.index>2019].iloc[:, 0])
"""
(0.03232571436843172,
 'positively autocorrelated',
 'increasing',
 0.04053488109575132,
 0.1348752598752599,
 110.67242723492723)
"""

#hadgem
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp60[all_deox_dur_rcp60.index>2019].iloc[:, 1])
"""
(0.01722125301452101,
 'positively autocorrelated',
 'increasing',
 3.174769269254085e-06,
 0.3333333333333333,
 127.83333333333333)
"""

#ipsl
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp60[all_deox_dur_rcp60.index>2019].iloc[:, 2])
"""
(0.02218004052566235,
 'positively autocorrelated',
 'increasing',
 2.273490546800261e-05,
 0.3,
 119.15)
"""

#miroc
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp60[all_deox_dur_rcp60.index>2019].iloc[:, 3])
"""
(0.022304096317965618,
 'positively autocorrelated',
 'increasing',
 1.0291064638900949e-05,
 0.2857142857142857,
 118.71428571428572)
"""



###########################################rcp85
#gfdl
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp85[all_deox_dur_rcp85.index>2019].iloc[:, 0])
"""
(0.035545573508802865,
 'positively autocorrelated',
 'increasing',
 7.022391557143237e-10,
 0.43243243243243246,
 85.41891891891892)
"""

#hadgem
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp85[all_deox_dur_rcp85.index>2019].iloc[:, 1])
"""
(0.012217257950440414,
 'positively autocorrelated',
 'increasing',
 2.793321129956894e-13,
 0.5161290322580645,
 124.61290322580645)
"""

#ipsl
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp85[all_deox_dur_rcp85.index>2019].iloc[:, 2])
"""
(0.015904305107997185,
 'positively autocorrelated',
 'increasing',
 5.227486692183092e-06,
 0.375,
 123.1875)
"""

#miroc
autocorr_MK_org_modif_sens_slope_test(all_deox_dur_rcp85[all_deox_dur_rcp85.index>2019].iloc[:, 3])
"""
(0.010288546403299148,
 'positively autocorrelated',
 'increasing',
 1.3883338922937583e-11,
 0.47058823529411764,
 119.91176470588235)
"""







#%% trendline (80 years) 2019-2099


glue_df_deox_dur_80years_rcp26=glue_df_deox_dur_rcp26[glue_df_deox_dur_rcp26.index>2019] 

glue_df_deox_dur_80years_rcp60=glue_df_deox_dur_rcp60[glue_df_deox_dur_rcp60.index>2019] 


glue_df_deox_dur_80years_rcp85=glue_df_deox_dur_rcp85[glue_df_deox_dur_rcp85.index>2019] 

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp26['50%'])
(0.007640291012656352,
 'positively autocorrelated',
 'increasing',
 0.03183393401249135,
 0.06445868945868946,
 124.20388176638177)

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp60['50%'])
(0.004156959430447248,
 'positively autocorrelated',
 'increasing',
 4.39914771277472e-12,
 0.2903225806451613,
 118.78225806451613)

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp85['50%'])
(0.006703860839201443,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.46551268498942916,
 117.36224894291755)



#%% 80 years plotiing for different senarios and their results of sens's slope and intercept 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for80years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_deox_dur_80years_rcp26.index, glue_df_deox_dur_80years_rcp26['5%'], glue_df_deox_dur_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_deox_dur_80years_rcp26.index, glue_df_deox_dur_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp26['50%'])
ax=plt.plot(glue_df_deox_dur_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--')

ax= plt.text(2060, 65, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )


ax=plt.fill_between(glue_df_deox_dur_80years_rcp60.index, glue_df_deox_dur_80years_rcp60['5%'], glue_df_deox_dur_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_deox_dur_80years_rcp60.index, glue_df_deox_dur_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp60['50%'])
ax=plt.plot(glue_df_deox_dur_80years_rcp60.index,trendline_rcp60[-2]*(np.arange(1,81))+trendline_rcp60[-1] ,color='yellow',  linestyle='--')

ax=plt.text(2060, 60, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.0001', color='gold', fontsize= 20 )




ax=plt.fill_between(glue_df_deox_dur_80years_rcp85.index, glue_df_deox_dur_80years_rcp85['5%'], glue_df_deox_dur_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_deox_dur_80years_rcp85.index, glue_df_deox_dur_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp85['50%'])
ax=plt.plot(glue_df_deox_dur_80years_rcp85.index,trendline_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--')

ax = plt.text(2060, 55, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize=20)


ax=plt.ylabel('Deoxygenation duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(50, 180, 30) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22, ncol= 3) 

fig.savefig("GLUE_Timeseries_deox_dur_80years.png", dpi=300, bbox_inches='tight')





#%% considering one century trendline (200 years) 2000-2099
glue_df_deox_dur_his_1900=glue_df_deox_dur_his[glue_df_deox_dur_his.index>1900]

glue_df_deox_dur_200years_rcp26=pd.concat([glue_df_deox_dur_his[glue_df_deox_dur_his.index>1900] , glue_df_deox_dur_rcp26])

glue_df_deox_dur_200years_rcp60=pd.concat([glue_df_deox_dur_his[glue_df_deox_dur_his.index>1900] , glue_df_deox_dur_rcp60])

glue_df_deox_dur_200years_rcp85=pd.concat([glue_df_deox_dur_his[glue_df_deox_dur_his.index>1900] , glue_df_deox_dur_rcp85])



#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_200years_rcp26['50%'])
"""
(0.00971202023175622,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.15,
 102.65)
"""
#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_200years_rcp60['50%'])
"""
(0.00840115250738639,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.1891891891891892,
 98.27027027027027)
"""
#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_200years_rcp85['50%'])
"""
(0.009317265067533713,
 'positively autocorrelated',
 'increasing',
 2.0096013140236124e-06,
 0.24766355140186916,
 92.98130841121495)
"""

#%% 200 years plotiing for different senarios and their results of sens's slope and intercept 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for100years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_df_deox_dur_his_1900.index, glue_df_deox_dur_his_1900['5%'], glue_df_deox_dur_his_1900['95%'], color='grey', alpha=0.4,  label= 'His 90% CI')
ax=plt.plot(glue_df_deox_dur_his_1900.index, glue_df_deox_dur_his_1900['50%'], 'k', label='His median', alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_deox_dur_rcp26.index, glue_df_deox_dur_rcp26['5%'], glue_df_deox_dur_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_deox_dur_rcp26.index, glue_df_deox_dur_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_200years_rcp26['50%'])
ax= plt.text(2000, 65, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )


ax=plt.fill_between(glue_df_deox_dur_rcp60.index, glue_df_deox_dur_rcp60['5%'], glue_df_deox_dur_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_deox_dur_rcp60.index, glue_df_deox_dur_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_200years_rcp60['50%'])
ax=plt.text(2000, 60, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value = {trendline_rcp60[-3]:.3f}', color='orange', fontsize= 20 )




ax=plt.fill_between(glue_df_deox_dur_rcp85.index, glue_df_deox_dur_rcp85['5%'], glue_df_deox_dur_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_deox_dur_rcp85.index, glue_df_deox_dur_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_200years_rcp85['50%'])
ax = plt.text(2000, 55, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value = {trendline_rcp85[-3]:.3f}', color='r', fontsize=20)


ax=plt.ylabel('Deoxygenation duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(50, 180, 30) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22) 

fig.savefig("GLUE_Timeseries_deox_dur_200years.png", dpi=300, bbox_inches='tight')


#%% considering one century trendline (100 years) 2000-2099


glue_df_deox_dur_100years_rcp26=pd.concat([glue_df_deox_dur_his[glue_df_deox_dur_his.index>1999] , glue_df_deox_dur_rcp26])

glue_df_deox_dur_100years_rcp60=pd.concat([glue_df_deox_dur_his[glue_df_deox_dur_his.index>1999] , glue_df_deox_dur_rcp60])

glue_df_deox_dur_100years_rcp85=pd.concat([glue_df_deox_dur_his[glue_df_deox_dur_his.index>1999] , glue_df_deox_dur_rcp85])



#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_100years_rcp26['50%'])
"""
(0.006850862205803608,
 'positively autocorrelated',
 'increasing',
 0.0016245521272495456,# p_value
 0.056394820536119945,# slope
 123.20845638346206)# intercept
"""
#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_100years_rcp60['50%'])
"""
(0.004717653031533401,
 'positively autocorrelated',
 'increasing',
 3.609914589475238e-10,
 0.23179568752209262,
 116.02611346765642)
"""
#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_100years_rcp85['50%'])
"""
(0.006513313632517885,
 'positively autocorrelated',
 'increasing',
 8.881784197001252e-16,
 0.40384615384615385,
 111.25961538461539)
"""


#%% graph liner showing all model and scanrios

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(deox_dur_mean4models_his)    
plt.plot(deox_dur_mean4models_rcp26)    
plt.plot(deox_dur_mean4models_rcp60)
plt.plot(deox_dur_mean4models_rcp85)
"""



# Plot mean data

plt.figure(figsize=(15, 10))  


plt.plot(deox_dur_mean4models_his[deox_dur_mean4models_his.index>1975], label='His', color='grey')#marker='o',
plt.plot(deox_dur_mean4models_rcp26, label='RCP2.6',  color='g')#marker='o',
plt.plot(deox_dur_mean4models_rcp60, label='RCP6.0',  color='yellow', alpha=0.9)#marker='o',
plt.plot(deox_dur_mean4models_rcp85, label='RCP8.5',  color='r', alpha=0.8)#marker='o',


# Calculate trendlines
trendline_his = np.polyfit(deox_dur_mean4models_his[deox_dur_mean4models_his.index>1975].index, deox_dur_mean4models_his[deox_dur_mean4models_his.index>1975], 1)
trendline_values_his = np.polyval(trendline_his, deox_dur_mean4models_his[deox_dur_mean4models_his.index>1975].index)
plt.plot(deox_dur_mean4models_his[deox_dur_mean4models_his.index>1975].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 95, f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='grey')
trendline_his[0]
#0.060750275547158006


trendline_rcp26 = np.polyfit(deox_dur_mean4models_rcp26.index, deox_dur_mean4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, deox_dur_mean4models_rcp26.index)
plt.plot(deox_dur_mean4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='g')
plt.text(2000, 90, f'y = {trendline_rcp26[0]:.2f}x + {trendline_rcp26[1]:.2f}', color='g')
trendline_rcp26[0]#slop of trendline
#0.08425387421883374


trendline_rcp60 = np.polyfit(deox_dur_mean4models_rcp60.index, deox_dur_mean4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, deox_dur_mean4models_rcp60.index)
plt.plot(deox_dur_mean4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 85, f'y = {trendline_rcp60[0]:.2f}x + {trendline_rcp60[1]:.2f}, p< 0.05', color='yellow')
trendline_rcp60[0]#slop of trendline
#0.24936603691796252


trendline_rcp85 = np.polyfit(deox_dur_mean4models_rcp85.index, deox_dur_mean4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, deox_dur_mean4models_rcp85.index)
plt.plot(deox_dur_mean4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 80, f'y = {trendline_rcp85[0]:.2f}x + {trendline_rcp85[1]:.2f}', color='r')
trendline_rcp85[0]
#0.41460824332622637



# Set the y-axis limits with an interval of 25
y_ticks = np.arange(50, 180, 30)
plt.yticks(y_ticks)

plt.ylabel('Deoxygenation duration [d]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_mean_deoxygenation_periods_trendline_last30years.png", dpi=300)






#%%Read the CSV file kz in deox of each model each senarios 

#%%######gfdl 

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his')
input_file_path = 'kz_prof_gfdl_his.csv'  # Replace with your actual input file path
kz_prof_gfdl_his = pd.read_csv(input_file_path)
kz_prof_2D_gfdl_his=kz_prof_gfdl_his.iloc[:, 1:].values
time_series_gfdl_his = pd.to_datetime(kz_prof_gfdl_his['Datetime'] )
kz_prof_gfdl_his=kz_prof_gfdl_his.set_index(time_series_gfdl_his)

kz_prof_gfdl_his= kz_prof_gfdl_his.drop('Datetime', axis=1)


# analyse of surf hypo kz gfdl his
kz_mean_surf_gfdl_his=kz_prof_gfdl_his.groupby(kz_prof_gfdl_his.index.year)['-14.25m'].mean()
kz_max_surf_gfdl_his=kz_prof_gfdl_his.groupby(kz_prof_gfdl_his.index.year)['-14.25m'].max()
kz_q1_surf_gfdl_his=kz_prof_gfdl_his.groupby(kz_prof_gfdl_his.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_gfdl_his=kz_prof_gfdl_his.groupby(kz_prof_gfdl_his.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz gfdl his
hypo_kz_daily_gfdl_his=hypolimnetic_ave(kz_prof_2D_gfdl_his, hypo_morpho_vriables_gotm_grid[0] , time_series_gfdl_his)

mean_annual_hypo_kz_daily_gfdl_his=hypo_kz_daily_gfdl_his.groupby(hypo_kz_daily_gfdl_his.index.year).mean()
max_annual_hypo_kz_daily_gfdl_his=hypo_kz_daily_gfdl_his.groupby(hypo_kz_daily_gfdl_his.index.year).max()
q1_annual_hypo_kz_daily_gfdl_his=hypo_kz_daily_gfdl_his.groupby(hypo_kz_daily_gfdl_his.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_gfdl_his=hypo_kz_daily_gfdl_his.groupby(hypo_kz_daily_gfdl_his.index.year).quantile(0.75)



#profile kz in deox gfdl his

#q1_annual_prof_kz_daily_gfdl_his= kz_prof_gfdl_his.groupby(kz_prof_gfdl_his.index.year).quantile(0.25)

#q3_annual_prof_kz_daily_gfdl_his= kz_prof_gfdl_his.groupby(kz_prof_gfdl_his.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_gfdl_his_no_nan = kz_prof_gfdl_his.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_gfdl_his = kz_prof_gfdl_his_no_nan.groupby(kz_prof_gfdl_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_gfdl_his = kz_prof_gfdl_his_no_nan.groupby(kz_prof_gfdl_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)






#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26')
input_file_path = 'kz_prof_gfdl_rcp26.csv'  # Replace with your actual input file path
kz_prof_gfdl_rcp26 = pd.read_csv(input_file_path)
kz_prof_2D_gfdl_rcp26=kz_prof_gfdl_rcp26.iloc[:, 1:].values
time_series_gfdl_rcp26 = pd.to_datetime(kz_prof_gfdl_rcp26['Datetime'] )
kz_prof_gfdl_rcp26=kz_prof_gfdl_rcp26.set_index(time_series_gfdl_rcp26)

kz_prof_gfdl_rcp26= kz_prof_gfdl_rcp26.drop('Datetime', axis=1)


# analyse of surf kz gfdl rcp26
kz_mean_surf_gfdl_rcp26=kz_prof_gfdl_rcp26.groupby(kz_prof_gfdl_rcp26.index.year)['-14.25m'].mean()
kz_max_surf_gfdl_rcp26=kz_prof_gfdl_rcp26.groupby(kz_prof_gfdl_rcp26.index.year)['-14.25m'].max()
kz_q1_surf_gfdl_rcp26=kz_prof_gfdl_rcp26.groupby(kz_prof_gfdl_rcp26.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_gfdl_rcp26=kz_prof_gfdl_rcp26.groupby(kz_prof_gfdl_rcp26.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz gfdl rcp26
hypo_kz_daily_gfdl_rcp26=hypolimnetic_ave(kz_prof_2D_gfdl_rcp26, hypo_morpho_vriables_gotm_grid[0] , time_series_gfdl_rcp26)

mean_annual_hypo_kz_daily_gfdl_rcp26=hypo_kz_daily_gfdl_rcp26.groupby(hypo_kz_daily_gfdl_rcp26.index.year).mean()
max_annual_hypo_kz_daily_gfdl_rcp26=hypo_kz_daily_gfdl_rcp26.groupby(hypo_kz_daily_gfdl_rcp26.index.year).max()
q1_annual_hypo_kz_daily_gfdl_rcp26=hypo_kz_daily_gfdl_rcp26.groupby(hypo_kz_daily_gfdl_rcp26.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_gfdl_rcp26=hypo_kz_daily_gfdl_rcp26.groupby(hypo_kz_daily_gfdl_rcp26.index.year).quantile(0.75)



#profile kz in deox gfdl rcp26

#q1_annual_prof_kz_daily_gfdl_rcp26= kz_prof_gfdl_rcp26.groupby(kz_prof_gfdl_rcp26.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_gfdl_rcp26= kz_prof_gfdl_rcp26.groupby(kz_prof_gfdl_rcp26.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_gfdl_rcp26_no_nan = kz_prof_gfdl_rcp26.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_gfdl_rcp26 = kz_prof_gfdl_rcp26_no_nan.groupby(kz_prof_gfdl_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_gfdl_rcp26 = kz_prof_gfdl_rcp26_no_nan.groupby(kz_prof_gfdl_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)



#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60')
input_file_path = 'kz_prof_gfdl_rcp60.csv'  # Replace with your actual input file path
kz_prof_gfdl_rcp60 = pd.read_csv(input_file_path)
kz_prof_2D_gfdl_rcp60=kz_prof_gfdl_rcp60.iloc[:, 1:].values
time_series_gfdl_rcp60 = pd.to_datetime(kz_prof_gfdl_rcp60['Datetime'] )
kz_prof_gfdl_rcp60=kz_prof_gfdl_rcp60.set_index(time_series_gfdl_rcp60)

kz_prof_gfdl_rcp60= kz_prof_gfdl_rcp60.drop('Datetime', axis=1)


# analyse of surf kz gfdl rcp60
kz_mean_surf_gfdl_rcp60=kz_prof_gfdl_rcp60.groupby(kz_prof_gfdl_rcp60.index.year)['-14.25m'].mean()
kz_max_surf_gfdl_rcp60=kz_prof_gfdl_rcp60.groupby(kz_prof_gfdl_rcp60.index.year)['-14.25m'].max()
kz_q1_surf_gfdl_rcp60=kz_prof_gfdl_rcp60.groupby(kz_prof_gfdl_rcp60.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_gfdl_rcp60=kz_prof_gfdl_rcp60.groupby(kz_prof_gfdl_rcp60.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz gfdl rcp60
hypo_kz_daily_gfdl_rcp60=hypolimnetic_ave(kz_prof_2D_gfdl_rcp60, hypo_morpho_vriables_gotm_grid[0] , time_series_gfdl_rcp60)

mean_annual_hypo_kz_daily_gfdl_rcp60=hypo_kz_daily_gfdl_rcp60.groupby(hypo_kz_daily_gfdl_rcp60.index.year).mean()
max_annual_hypo_kz_daily_gfdl_rcp60=hypo_kz_daily_gfdl_rcp60.groupby(hypo_kz_daily_gfdl_rcp60.index.year).max()
q1_annual_hypo_kz_daily_gfdl_rcp60=hypo_kz_daily_gfdl_rcp60.groupby(hypo_kz_daily_gfdl_rcp60.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_gfdl_rcp60=hypo_kz_daily_gfdl_rcp60.groupby(hypo_kz_daily_gfdl_rcp60.index.year).quantile(0.75)



#profile kz in deox gfdl rcp60

#q1_annual_prof_kz_daily_gfdl_rcp60= kz_prof_gfdl_rcp60.groupby(kz_prof_gfdl_rcp60.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_gfdl_rcp60= kz_prof_gfdl_rcp60.groupby(kz_prof_gfdl_rcp60.index.year).quantile(0.75)


# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_gfdl_rcp60_no_nan = kz_prof_gfdl_rcp60.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_gfdl_rcp60 = kz_prof_gfdl_rcp60_no_nan.groupby(kz_prof_gfdl_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_gfdl_rcp60 = kz_prof_gfdl_rcp60_no_nan.groupby(kz_prof_gfdl_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)




#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85')
input_file_path = 'kz_prof_gfdl_rcp85.csv'  # Replace with your actual input file path
kz_prof_gfdl_rcp85 = pd.read_csv(input_file_path )
kz_prof_2D_gfdl_rcp85=kz_prof_gfdl_rcp85.iloc[:, 1:].values
time_series_gfdl_rcp85 = pd.to_datetime(kz_prof_gfdl_rcp85['Datetime'] )
kz_prof_gfdl_rcp85=kz_prof_gfdl_rcp85.set_index(time_series_gfdl_rcp85)

kz_prof_gfdl_rcp85= kz_prof_gfdl_rcp85.drop('Datetime', axis=1)


# analyse of surf kz gfdl rcp85
kz_mean_surf_gfdl_rcp85=kz_prof_gfdl_rcp85.groupby(kz_prof_gfdl_rcp85.index.year)['-14.25m'].mean()
kz_max_surf_gfdl_rcp85=kz_prof_gfdl_rcp85.groupby(kz_prof_gfdl_rcp85.index.year)['-14.25m'].max()
kz_q1_surf_gfdl_rcp85=kz_prof_gfdl_rcp85.groupby(kz_prof_gfdl_rcp85.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_gfdl_rcp85=kz_prof_gfdl_rcp85.groupby(kz_prof_gfdl_rcp85.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz gfdl rcp85
hypo_kz_daily_gfdl_rcp85=hypolimnetic_ave(kz_prof_2D_gfdl_rcp85, hypo_morpho_vriables_gotm_grid[0] , time_series_gfdl_rcp85)

mean_annual_hypo_kz_daily_gfdl_rcp85=hypo_kz_daily_gfdl_rcp85.groupby(hypo_kz_daily_gfdl_rcp85.index.year).mean()
max_annual_hypo_kz_daily_gfdl_rcp85=hypo_kz_daily_gfdl_rcp85.groupby(hypo_kz_daily_gfdl_rcp85.index.year).max()
q1_annual_hypo_kz_daily_gfdl_rcp85=hypo_kz_daily_gfdl_rcp85.groupby(hypo_kz_daily_gfdl_rcp85.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_gfdl_rcp85=hypo_kz_daily_gfdl_rcp85.groupby(hypo_kz_daily_gfdl_rcp85.index.year).quantile(0.75)



#profile kz in deox gfdl rcp85

#q1_annual_prof_kz_daily_gfdl_rcp85= kz_prof_gfdl_rcp85.groupby(kz_prof_gfdl_rcp85.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_gfdl_rcp85= kz_prof_gfdl_rcp85.groupby(kz_prof_gfdl_rcp85.index.year).quantile(0.75)




# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_gfdl_rcp85_no_nan = kz_prof_gfdl_rcp85.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_gfdl_rcp85 = kz_prof_gfdl_rcp85_no_nan.groupby(kz_prof_gfdl_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_gfdl_rcp85 = kz_prof_gfdl_rcp85_no_nan.groupby(kz_prof_gfdl_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)




#%%######hadgem 

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his')
input_file_path = 'kz_prof_hadgem_his.csv'  # Replace with your actual input file path
kz_prof_hadgem_his = pd.read_csv(input_file_path)
kz_prof_2D_hadgem_his=kz_prof_hadgem_his.iloc[:, 1:].values
time_series_hadgem_his = pd.to_datetime(kz_prof_hadgem_his['Datetime'] )
kz_prof_hadgem_his=kz_prof_hadgem_his.set_index(time_series_hadgem_his)

kz_prof_hadgem_his= kz_prof_hadgem_his.drop('Datetime', axis=1)


# analyse of surf kz hadgem his
kz_mean_surf_hadgem_his=kz_prof_hadgem_his.groupby(kz_prof_hadgem_his.index.year)['-14.25m'].mean()
kz_max_surf_hadgem_his=kz_prof_hadgem_his.groupby(kz_prof_hadgem_his.index.year)['-14.25m'].max()
kz_q1_surf_hadgem_his=kz_prof_hadgem_his.groupby(kz_prof_hadgem_his.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_hadgem_his=kz_prof_hadgem_his.groupby(kz_prof_hadgem_his.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz hadgem his
hypo_kz_daily_hadgem_his=hypolimnetic_ave(kz_prof_2D_hadgem_his, hypo_morpho_vriables_gotm_grid[0] , time_series_hadgem_his)

mean_annual_hypo_kz_daily_hadgem_his=hypo_kz_daily_hadgem_his.groupby(hypo_kz_daily_hadgem_his.index.year).mean()
max_annual_hypo_kz_daily_hadgem_his=hypo_kz_daily_hadgem_his.groupby(hypo_kz_daily_hadgem_his.index.year).max()
q1_annual_hypo_kz_daily_hadgem_his=hypo_kz_daily_hadgem_his.groupby(hypo_kz_daily_hadgem_his.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_hadgem_his=hypo_kz_daily_hadgem_his.groupby(hypo_kz_daily_hadgem_his.index.year).quantile(0.75)



#profile kz in deox hadgem his

#q1_annual_prof_kz_daily_hadgem_his= kz_prof_hadgem_his.groupby(kz_prof_hadgem_his.index.year).quantile(0.25)

#q3_annual_prof_kz_daily_hadgem_his= kz_prof_hadgem_his.groupby(kz_prof_hadgem_his.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_hadgem_his_no_nan = kz_prof_hadgem_his.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_hadgem_his = kz_prof_hadgem_his_no_nan.groupby(kz_prof_hadgem_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_hadgem_his = kz_prof_hadgem_his_no_nan.groupby(kz_prof_hadgem_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)






#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26')
input_file_path = 'kz_prof_hadgem_rcp26.csv'  # Replace with your actual input file path
kz_prof_hadgem_rcp26 = pd.read_csv(input_file_path)
kz_prof_2D_hadgem_rcp26=kz_prof_hadgem_rcp26.iloc[:, 1:].values
time_series_hadgem_rcp26 = pd.to_datetime(kz_prof_hadgem_rcp26['Datetime'] )
kz_prof_hadgem_rcp26=kz_prof_hadgem_rcp26.set_index(time_series_hadgem_rcp26)

kz_prof_hadgem_rcp26= kz_prof_hadgem_rcp26.drop('Datetime', axis=1)


# analyse of surf kz hadgem rcp26
kz_mean_surf_hadgem_rcp26=kz_prof_hadgem_rcp26.groupby(kz_prof_hadgem_rcp26.index.year)['-14.25m'].mean()
kz_max_surf_hadgem_rcp26=kz_prof_hadgem_rcp26.groupby(kz_prof_hadgem_rcp26.index.year)['-14.25m'].max()
kz_q1_surf_hadgem_rcp26=kz_prof_hadgem_rcp26.groupby(kz_prof_hadgem_rcp26.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_hadgem_rcp26=kz_prof_hadgem_rcp26.groupby(kz_prof_hadgem_rcp26.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz hadgem rcp26
hypo_kz_daily_hadgem_rcp26=hypolimnetic_ave(kz_prof_2D_hadgem_rcp26, hypo_morpho_vriables_gotm_grid[0] , time_series_hadgem_rcp26)

mean_annual_hypo_kz_daily_hadgem_rcp26=hypo_kz_daily_hadgem_rcp26.groupby(hypo_kz_daily_hadgem_rcp26.index.year).mean()
max_annual_hypo_kz_daily_hadgem_rcp26=hypo_kz_daily_hadgem_rcp26.groupby(hypo_kz_daily_hadgem_rcp26.index.year).max()
q1_annual_hypo_kz_daily_hadgem_rcp26=hypo_kz_daily_hadgem_rcp26.groupby(hypo_kz_daily_hadgem_rcp26.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_hadgem_rcp26=hypo_kz_daily_hadgem_rcp26.groupby(hypo_kz_daily_hadgem_rcp26.index.year).quantile(0.75)



#profile kz in deox hadgem rcp26

#q1_annual_prof_kz_daily_hadgem_rcp26= kz_prof_hadgem_rcp26.groupby(kz_prof_hadgem_rcp26.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_hadgem_rcp26= kz_prof_hadgem_rcp26.groupby(kz_prof_hadgem_rcp26.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_hadgem_rcp26_no_nan = kz_prof_hadgem_rcp26.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_hadgem_rcp26 = kz_prof_hadgem_rcp26_no_nan.groupby(kz_prof_hadgem_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_hadgem_rcp26 = kz_prof_hadgem_rcp26_no_nan.groupby(kz_prof_hadgem_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)



#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60')
input_file_path = 'kz_prof_hadgem_rcp60.csv'  # Replace with your actual input file path
kz_prof_hadgem_rcp60 = pd.read_csv(input_file_path)
kz_prof_2D_hadgem_rcp60=kz_prof_hadgem_rcp60.iloc[:, 1:].values
time_series_hadgem_rcp60 = pd.to_datetime(kz_prof_hadgem_rcp60['Datetime'] )
kz_prof_hadgem_rcp60=kz_prof_hadgem_rcp60.set_index(time_series_hadgem_rcp60)

kz_prof_hadgem_rcp60= kz_prof_hadgem_rcp60.drop('Datetime', axis=1)


# analyse of surf kz hadgem rcp60
kz_mean_surf_hadgem_rcp60=kz_prof_hadgem_rcp60.groupby(kz_prof_hadgem_rcp60.index.year)['-14.25m'].mean()
kz_max_surf_hadgem_rcp60=kz_prof_hadgem_rcp60.groupby(kz_prof_hadgem_rcp60.index.year)['-14.25m'].max()
kz_q1_surf_hadgem_rcp60=kz_prof_hadgem_rcp60.groupby(kz_prof_hadgem_rcp60.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_hadgem_rcp60=kz_prof_hadgem_rcp60.groupby(kz_prof_hadgem_rcp60.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz hadgem rcp60
hypo_kz_daily_hadgem_rcp60=hypolimnetic_ave(kz_prof_2D_hadgem_rcp60, hypo_morpho_vriables_gotm_grid[0] , time_series_hadgem_rcp60)

mean_annual_hypo_kz_daily_hadgem_rcp60=hypo_kz_daily_hadgem_rcp60.groupby(hypo_kz_daily_hadgem_rcp60.index.year).mean()
max_annual_hypo_kz_daily_hadgem_rcp60=hypo_kz_daily_hadgem_rcp60.groupby(hypo_kz_daily_hadgem_rcp60.index.year).max()
q1_annual_hypo_kz_daily_hadgem_rcp60=hypo_kz_daily_hadgem_rcp60.groupby(hypo_kz_daily_hadgem_rcp60.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_hadgem_rcp60=hypo_kz_daily_hadgem_rcp60.groupby(hypo_kz_daily_hadgem_rcp60.index.year).quantile(0.75)



#profile kz in deox hadgem rcp60

#q1_annual_prof_kz_daily_hadgem_rcp60= kz_prof_hadgem_rcp60.groupby(kz_prof_hadgem_rcp60.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_hadgem_rcp60= kz_prof_hadgem_rcp60.groupby(kz_prof_hadgem_rcp60.index.year).quantile(0.75)


# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_hadgem_rcp60_no_nan = kz_prof_hadgem_rcp60.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_hadgem_rcp60 = kz_prof_hadgem_rcp60_no_nan.groupby(kz_prof_hadgem_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_hadgem_rcp60 = kz_prof_hadgem_rcp60_no_nan.groupby(kz_prof_hadgem_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)




#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85')
input_file_path = 'kz_prof_hadgem_rcp85.csv'  # Replace with your actual input file path
kz_prof_hadgem_rcp85 = pd.read_csv(input_file_path )
kz_prof_2D_hadgem_rcp85=kz_prof_hadgem_rcp85.iloc[:, 1:].values
time_series_hadgem_rcp85 = pd.to_datetime(kz_prof_hadgem_rcp85['Datetime'] )
kz_prof_hadgem_rcp85=kz_prof_hadgem_rcp85.set_index(time_series_hadgem_rcp85)

kz_prof_hadgem_rcp85= kz_prof_hadgem_rcp85.drop('Datetime', axis=1)


# analyse of surf kz hadgem rcp85
kz_mean_surf_hadgem_rcp85=kz_prof_hadgem_rcp85.groupby(kz_prof_hadgem_rcp85.index.year)['-14.25m'].mean()
kz_max_surf_hadgem_rcp85=kz_prof_hadgem_rcp85.groupby(kz_prof_hadgem_rcp85.index.year)['-14.25m'].max()
kz_q1_surf_hadgem_rcp85=kz_prof_hadgem_rcp85.groupby(kz_prof_hadgem_rcp85.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_hadgem_rcp85=kz_prof_hadgem_rcp85.groupby(kz_prof_hadgem_rcp85.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz hadgem rcp85
hypo_kz_daily_hadgem_rcp85=hypolimnetic_ave(kz_prof_2D_hadgem_rcp85, hypo_morpho_vriables_gotm_grid[0] , time_series_hadgem_rcp85)

mean_annual_hypo_kz_daily_hadgem_rcp85=hypo_kz_daily_hadgem_rcp85.groupby(hypo_kz_daily_hadgem_rcp85.index.year).mean()
max_annual_hypo_kz_daily_hadgem_rcp85=hypo_kz_daily_hadgem_rcp85.groupby(hypo_kz_daily_hadgem_rcp85.index.year).max()
q1_annual_hypo_kz_daily_hadgem_rcp85=hypo_kz_daily_hadgem_rcp85.groupby(hypo_kz_daily_hadgem_rcp85.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_hadgem_rcp85=hypo_kz_daily_hadgem_rcp85.groupby(hypo_kz_daily_hadgem_rcp85.index.year).quantile(0.75)



#profile kz in deox hadgem rcp85

#q1_annual_prof_kz_daily_hadgem_rcp85= kz_prof_hadgem_rcp85.groupby(kz_prof_hadgem_rcp85.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_hadgem_rcp85= kz_prof_hadgem_rcp85.groupby(kz_prof_hadgem_rcp85.index.year).quantile(0.75)




# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_hadgem_rcp85_no_nan = kz_prof_hadgem_rcp85.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_hadgem_rcp85 = kz_prof_hadgem_rcp85_no_nan.groupby(kz_prof_hadgem_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_hadgem_rcp85 = kz_prof_hadgem_rcp85_no_nan.groupby(kz_prof_hadgem_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)



#%%#######ipsl 

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his')
input_file_path = 'kz_prof_ipsl_his.csv'  # Replace with your actual input file path
kz_prof_ipsl_his = pd.read_csv(input_file_path)
kz_prof_2D_ipsl_his=kz_prof_ipsl_his.iloc[:, 1:].values
time_series_ipsl_his = pd.to_datetime(kz_prof_ipsl_his['Datetime'] )
kz_prof_ipsl_his=kz_prof_ipsl_his.set_index(time_series_ipsl_his)

kz_prof_ipsl_his= kz_prof_ipsl_his.drop('Datetime', axis=1)


# analyse of surf kz ipsl his
kz_mean_surf_ipsl_his=kz_prof_ipsl_his.groupby(kz_prof_ipsl_his.index.year)['-14.25m'].mean()
kz_max_surf_ipsl_his=kz_prof_ipsl_his.groupby(kz_prof_ipsl_his.index.year)['-14.25m'].max()
kz_q1_surf_ipsl_his=kz_prof_ipsl_his.groupby(kz_prof_ipsl_his.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_ipsl_his=kz_prof_ipsl_his.groupby(kz_prof_ipsl_his.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz ipsl his
hypo_kz_daily_ipsl_his=hypolimnetic_ave(kz_prof_2D_ipsl_his, hypo_morpho_vriables_gotm_grid[0] , time_series_ipsl_his)

mean_annual_hypo_kz_daily_ipsl_his=hypo_kz_daily_ipsl_his.groupby(hypo_kz_daily_ipsl_his.index.year).mean()
max_annual_hypo_kz_daily_ipsl_his=hypo_kz_daily_ipsl_his.groupby(hypo_kz_daily_ipsl_his.index.year).max()
q1_annual_hypo_kz_daily_ipsl_his=hypo_kz_daily_ipsl_his.groupby(hypo_kz_daily_ipsl_his.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_ipsl_his=hypo_kz_daily_ipsl_his.groupby(hypo_kz_daily_ipsl_his.index.year).quantile(0.75)



#profile kz in deox ipsl his

#q1_annual_prof_kz_daily_ipsl_his= kz_prof_ipsl_his.groupby(kz_prof_ipsl_his.index.year).quantile(0.25)

#q3_annual_prof_kz_daily_ipsl_his= kz_prof_ipsl_his.groupby(kz_prof_ipsl_his.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_ipsl_his_no_nan = kz_prof_ipsl_his.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_ipsl_his = kz_prof_ipsl_his_no_nan.groupby(kz_prof_ipsl_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_ipsl_his = kz_prof_ipsl_his_no_nan.groupby(kz_prof_ipsl_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)






#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26')
input_file_path = 'kz_prof_ipsl_rcp26.csv'  # Replace with your actual input file path
kz_prof_ipsl_rcp26 = pd.read_csv(input_file_path)
kz_prof_2D_ipsl_rcp26=kz_prof_ipsl_rcp26.iloc[:, 1:].values
time_series_ipsl_rcp26 = pd.to_datetime(kz_prof_ipsl_rcp26['Datetime'] )
kz_prof_ipsl_rcp26=kz_prof_ipsl_rcp26.set_index(time_series_ipsl_rcp26)

kz_prof_ipsl_rcp26= kz_prof_ipsl_rcp26.drop('Datetime', axis=1)


# analyse of surf kz ipsl rcp26
kz_mean_surf_ipsl_rcp26=kz_prof_ipsl_rcp26.groupby(kz_prof_ipsl_rcp26.index.year)['-14.25m'].mean()
kz_max_surf_ipsl_rcp26=kz_prof_ipsl_rcp26.groupby(kz_prof_ipsl_rcp26.index.year)['-14.25m'].max()
kz_q1_surf_ipsl_rcp26=kz_prof_ipsl_rcp26.groupby(kz_prof_ipsl_rcp26.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_ipsl_rcp26=kz_prof_ipsl_rcp26.groupby(kz_prof_ipsl_rcp26.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz ipsl rcp26
hypo_kz_daily_ipsl_rcp26=hypolimnetic_ave(kz_prof_2D_ipsl_rcp26, hypo_morpho_vriables_gotm_grid[0] , time_series_ipsl_rcp26)

mean_annual_hypo_kz_daily_ipsl_rcp26=hypo_kz_daily_ipsl_rcp26.groupby(hypo_kz_daily_ipsl_rcp26.index.year).mean()
max_annual_hypo_kz_daily_ipsl_rcp26=hypo_kz_daily_ipsl_rcp26.groupby(hypo_kz_daily_ipsl_rcp26.index.year).max()
q1_annual_hypo_kz_daily_ipsl_rcp26=hypo_kz_daily_ipsl_rcp26.groupby(hypo_kz_daily_ipsl_rcp26.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_ipsl_rcp26=hypo_kz_daily_ipsl_rcp26.groupby(hypo_kz_daily_ipsl_rcp26.index.year).quantile(0.75)



#profile kz in deox ipsl rcp26

#q1_annual_prof_kz_daily_ipsl_rcp26= kz_prof_ipsl_rcp26.groupby(kz_prof_ipsl_rcp26.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_ipsl_rcp26= kz_prof_ipsl_rcp26.groupby(kz_prof_ipsl_rcp26.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_ipsl_rcp26_no_nan = kz_prof_ipsl_rcp26.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_ipsl_rcp26 = kz_prof_ipsl_rcp26_no_nan.groupby(kz_prof_ipsl_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_ipsl_rcp26 = kz_prof_ipsl_rcp26_no_nan.groupby(kz_prof_ipsl_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)



#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60')
input_file_path = 'kz_prof_ipsl_rcp60.csv'  # Replace with your actual input file path
kz_prof_ipsl_rcp60 = pd.read_csv(input_file_path)
kz_prof_2D_ipsl_rcp60=kz_prof_ipsl_rcp60.iloc[:, 1:].values
time_series_ipsl_rcp60 = pd.to_datetime(kz_prof_ipsl_rcp60['Datetime'] )
kz_prof_ipsl_rcp60=kz_prof_ipsl_rcp60.set_index(time_series_ipsl_rcp60)

kz_prof_ipsl_rcp60= kz_prof_ipsl_rcp60.drop('Datetime', axis=1)


# analyse of surf kz ipsl rcp60
kz_mean_surf_ipsl_rcp60=kz_prof_ipsl_rcp60.groupby(kz_prof_ipsl_rcp60.index.year)['-14.25m'].mean()
kz_max_surf_ipsl_rcp60=kz_prof_ipsl_rcp60.groupby(kz_prof_ipsl_rcp60.index.year)['-14.25m'].max()
kz_q1_surf_ipsl_rcp60=kz_prof_ipsl_rcp60.groupby(kz_prof_ipsl_rcp60.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_ipsl_rcp60=kz_prof_ipsl_rcp60.groupby(kz_prof_ipsl_rcp60.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz ipsl rcp60
hypo_kz_daily_ipsl_rcp60=hypolimnetic_ave(kz_prof_2D_ipsl_rcp60, hypo_morpho_vriables_gotm_grid[0] , time_series_ipsl_rcp60)

mean_annual_hypo_kz_daily_ipsl_rcp60=hypo_kz_daily_ipsl_rcp60.groupby(hypo_kz_daily_ipsl_rcp60.index.year).mean()
max_annual_hypo_kz_daily_ipsl_rcp60=hypo_kz_daily_ipsl_rcp60.groupby(hypo_kz_daily_ipsl_rcp60.index.year).max()
q1_annual_hypo_kz_daily_ipsl_rcp60=hypo_kz_daily_ipsl_rcp60.groupby(hypo_kz_daily_ipsl_rcp60.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_ipsl_rcp60=hypo_kz_daily_ipsl_rcp60.groupby(hypo_kz_daily_ipsl_rcp60.index.year).quantile(0.75)



#profile kz in deox ipsl rcp60

#q1_annual_prof_kz_daily_ipsl_rcp60= kz_prof_ipsl_rcp60.groupby(kz_prof_ipsl_rcp60.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_ipsl_rcp60= kz_prof_ipsl_rcp60.groupby(kz_prof_ipsl_rcp60.index.year).quantile(0.75)


# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_ipsl_rcp60_no_nan = kz_prof_ipsl_rcp60.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_ipsl_rcp60 = kz_prof_ipsl_rcp60_no_nan.groupby(kz_prof_ipsl_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_ipsl_rcp60 = kz_prof_ipsl_rcp60_no_nan.groupby(kz_prof_ipsl_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)




#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85')
input_file_path = 'kz_prof_ipsl_rcp85.csv'  # Replace with your actual input file path
kz_prof_ipsl_rcp85 = pd.read_csv(input_file_path )
kz_prof_2D_ipsl_rcp85=kz_prof_ipsl_rcp85.iloc[:, 1:].values
time_series_ipsl_rcp85 = pd.to_datetime(kz_prof_ipsl_rcp85['Datetime'] )
kz_prof_ipsl_rcp85=kz_prof_ipsl_rcp85.set_index(time_series_ipsl_rcp85)

kz_prof_ipsl_rcp85= kz_prof_ipsl_rcp85.drop('Datetime', axis=1)


# analyse of surf kz ipsl rcp85
kz_mean_surf_ipsl_rcp85=kz_prof_ipsl_rcp85.groupby(kz_prof_ipsl_rcp85.index.year)['-14.25m'].mean()
kz_max_surf_ipsl_rcp85=kz_prof_ipsl_rcp85.groupby(kz_prof_ipsl_rcp85.index.year)['-14.25m'].max()
kz_q1_surf_ipsl_rcp85=kz_prof_ipsl_rcp85.groupby(kz_prof_ipsl_rcp85.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_ipsl_rcp85=kz_prof_ipsl_rcp85.groupby(kz_prof_ipsl_rcp85.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz ipsl rcp85
hypo_kz_daily_ipsl_rcp85=hypolimnetic_ave(kz_prof_2D_ipsl_rcp85, hypo_morpho_vriables_gotm_grid[0] , time_series_ipsl_rcp85)

mean_annual_hypo_kz_daily_ipsl_rcp85=hypo_kz_daily_ipsl_rcp85.groupby(hypo_kz_daily_ipsl_rcp85.index.year).mean()
max_annual_hypo_kz_daily_ipsl_rcp85=hypo_kz_daily_ipsl_rcp85.groupby(hypo_kz_daily_ipsl_rcp85.index.year).max()
q1_annual_hypo_kz_daily_ipsl_rcp85=hypo_kz_daily_ipsl_rcp85.groupby(hypo_kz_daily_ipsl_rcp85.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_ipsl_rcp85=hypo_kz_daily_ipsl_rcp85.groupby(hypo_kz_daily_ipsl_rcp85.index.year).quantile(0.75)



#profile kz in deox ipsl rcp85

#q1_annual_prof_kz_daily_ipsl_rcp85= kz_prof_ipsl_rcp85.groupby(kz_prof_ipsl_rcp85.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_ipsl_rcp85= kz_prof_ipsl_rcp85.groupby(kz_prof_ipsl_rcp85.index.year).quantile(0.75)




# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_ipsl_rcp85_no_nan = kz_prof_ipsl_rcp85.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_ipsl_rcp85 = kz_prof_ipsl_rcp85_no_nan.groupby(kz_prof_ipsl_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_ipsl_rcp85 = kz_prof_ipsl_rcp85_no_nan.groupby(kz_prof_ipsl_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)



#%%#######miroc 

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his')
input_file_path = 'kz_prof_miroc_his.csv'  # Replace with your actual input file path
kz_prof_miroc_his = pd.read_csv(input_file_path)
kz_prof_2D_miroc_his=kz_prof_miroc_his.iloc[:, 1:].values
time_series_miroc_his = pd.to_datetime(kz_prof_miroc_his['Datetime'] )
kz_prof_miroc_his=kz_prof_miroc_his.set_index(time_series_miroc_his)

kz_prof_miroc_his= kz_prof_miroc_his.drop('Datetime', axis=1)


# analyse of surf kz miroc his
kz_mean_surf_miroc_his=kz_prof_miroc_his.groupby(kz_prof_miroc_his.index.year)['-14.25m'].mean()
kz_max_surf_miroc_his=kz_prof_miroc_his.groupby(kz_prof_miroc_his.index.year)['-14.25m'].max()
kz_q1_surf_miroc_his=kz_prof_miroc_his.groupby(kz_prof_miroc_his.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_miroc_his=kz_prof_miroc_his.groupby(kz_prof_miroc_his.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz miroc his
hypo_kz_daily_miroc_his=hypolimnetic_ave(kz_prof_2D_miroc_his, hypo_morpho_vriables_gotm_grid[0] , time_series_miroc_his)

mean_annual_hypo_kz_daily_miroc_his=hypo_kz_daily_miroc_his.groupby(hypo_kz_daily_miroc_his.index.year).mean()
max_annual_hypo_kz_daily_miroc_his=hypo_kz_daily_miroc_his.groupby(hypo_kz_daily_miroc_his.index.year).max()
q1_annual_hypo_kz_daily_miroc_his=hypo_kz_daily_miroc_his.groupby(hypo_kz_daily_miroc_his.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_miroc_his=hypo_kz_daily_miroc_his.groupby(hypo_kz_daily_miroc_his.index.year).quantile(0.75)



#profile kz in deox miroc his

#q1_annual_prof_kz_daily_miroc_his= kz_prof_miroc_his.groupby(kz_prof_miroc_his.index.year).quantile(0.25)

#q3_annual_prof_kz_daily_miroc_his= kz_prof_miroc_his.groupby(kz_prof_miroc_his.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_miroc_his_no_nan = kz_prof_miroc_his.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_miroc_his = kz_prof_miroc_his_no_nan.groupby(kz_prof_miroc_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_miroc_his = kz_prof_miroc_his_no_nan.groupby(kz_prof_miroc_his_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)






#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26')
input_file_path = 'kz_prof_miroc_rcp26.csv'  # Replace with your actual input file path
kz_prof_miroc_rcp26 = pd.read_csv(input_file_path)
kz_prof_2D_miroc_rcp26=kz_prof_miroc_rcp26.iloc[:, 1:].values
time_series_miroc_rcp26 = pd.to_datetime(kz_prof_miroc_rcp26['Datetime'] )
kz_prof_miroc_rcp26=kz_prof_miroc_rcp26.set_index(time_series_miroc_rcp26)

kz_prof_miroc_rcp26= kz_prof_miroc_rcp26.drop('Datetime', axis=1)


# analyse of surf kz miroc rcp26
kz_mean_surf_miroc_rcp26=kz_prof_miroc_rcp26.groupby(kz_prof_miroc_rcp26.index.year)['-14.25m'].mean()
kz_max_surf_miroc_rcp26=kz_prof_miroc_rcp26.groupby(kz_prof_miroc_rcp26.index.year)['-14.25m'].max()
kz_q1_surf_miroc_rcp26=kz_prof_miroc_rcp26.groupby(kz_prof_miroc_rcp26.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_miroc_rcp26=kz_prof_miroc_rcp26.groupby(kz_prof_miroc_rcp26.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz miroc rcp26
hypo_kz_daily_miroc_rcp26=hypolimnetic_ave(kz_prof_2D_miroc_rcp26, hypo_morpho_vriables_gotm_grid[0] , time_series_miroc_rcp26)

mean_annual_hypo_kz_daily_miroc_rcp26=hypo_kz_daily_miroc_rcp26.groupby(hypo_kz_daily_miroc_rcp26.index.year).mean()
max_annual_hypo_kz_daily_miroc_rcp26=hypo_kz_daily_miroc_rcp26.groupby(hypo_kz_daily_miroc_rcp26.index.year).max()
q1_annual_hypo_kz_daily_miroc_rcp26=hypo_kz_daily_miroc_rcp26.groupby(hypo_kz_daily_miroc_rcp26.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_miroc_rcp26=hypo_kz_daily_miroc_rcp26.groupby(hypo_kz_daily_miroc_rcp26.index.year).quantile(0.75)



#profile kz in deox miroc rcp26

#q1_annual_prof_kz_daily_miroc_rcp26= kz_prof_miroc_rcp26.groupby(kz_prof_miroc_rcp26.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_miroc_rcp26= kz_prof_miroc_rcp26.groupby(kz_prof_miroc_rcp26.index.year).quantile(0.75)

# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_miroc_rcp26_no_nan = kz_prof_miroc_rcp26.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_miroc_rcp26 = kz_prof_miroc_rcp26_no_nan.groupby(kz_prof_miroc_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_miroc_rcp26 = kz_prof_miroc_rcp26_no_nan.groupby(kz_prof_miroc_rcp26_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)



#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60')
input_file_path = 'kz_prof_miroc_rcp60.csv'  # Replace with your actual input file path
kz_prof_miroc_rcp60 = pd.read_csv(input_file_path)
kz_prof_2D_miroc_rcp60=kz_prof_miroc_rcp60.iloc[:, 1:].values
time_series_miroc_rcp60 = pd.to_datetime(kz_prof_miroc_rcp60['Datetime'] )
kz_prof_miroc_rcp60=kz_prof_miroc_rcp60.set_index(time_series_miroc_rcp60)

kz_prof_miroc_rcp60= kz_prof_miroc_rcp60.drop('Datetime', axis=1)


# analyse of surf kz miroc rcp60
kz_mean_surf_miroc_rcp60=kz_prof_miroc_rcp60.groupby(kz_prof_miroc_rcp60.index.year)['-14.25m'].mean()
kz_max_surf_miroc_rcp60=kz_prof_miroc_rcp60.groupby(kz_prof_miroc_rcp60.index.year)['-14.25m'].max()
kz_q1_surf_miroc_rcp60=kz_prof_miroc_rcp60.groupby(kz_prof_miroc_rcp60.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_miroc_rcp60=kz_prof_miroc_rcp60.groupby(kz_prof_miroc_rcp60.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz miroc rcp60
hypo_kz_daily_miroc_rcp60=hypolimnetic_ave(kz_prof_2D_miroc_rcp60, hypo_morpho_vriables_gotm_grid[0] , time_series_miroc_rcp60)

mean_annual_hypo_kz_daily_miroc_rcp60=hypo_kz_daily_miroc_rcp60.groupby(hypo_kz_daily_miroc_rcp60.index.year).mean()
max_annual_hypo_kz_daily_miroc_rcp60=hypo_kz_daily_miroc_rcp60.groupby(hypo_kz_daily_miroc_rcp60.index.year).max()
q1_annual_hypo_kz_daily_miroc_rcp60=hypo_kz_daily_miroc_rcp60.groupby(hypo_kz_daily_miroc_rcp60.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_miroc_rcp60=hypo_kz_daily_miroc_rcp60.groupby(hypo_kz_daily_miroc_rcp60.index.year).quantile(0.75)



#profile kz in deox miroc rcp60

#q1_annual_prof_kz_daily_miroc_rcp60= kz_prof_miroc_rcp60.groupby(kz_prof_miroc_rcp60.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_miroc_rcp60= kz_prof_miroc_rcp60.groupby(kz_prof_miroc_rcp60.index.year).quantile(0.75)


# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_miroc_rcp60_no_nan = kz_prof_miroc_rcp60.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_miroc_rcp60 = kz_prof_miroc_rcp60_no_nan.groupby(kz_prof_miroc_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_miroc_rcp60 = kz_prof_miroc_rcp60_no_nan.groupby(kz_prof_miroc_rcp60_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)




#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85')
input_file_path = 'kz_prof_miroc_rcp85.csv'  # Replace with your actual input file path
kz_prof_miroc_rcp85 = pd.read_csv(input_file_path )
kz_prof_2D_miroc_rcp85=kz_prof_miroc_rcp85.iloc[:, 1:].values
time_series_miroc_rcp85 = pd.to_datetime(kz_prof_miroc_rcp85['Datetime'] )
kz_prof_miroc_rcp85=kz_prof_miroc_rcp85.set_index(time_series_miroc_rcp85)

kz_prof_miroc_rcp85= kz_prof_miroc_rcp85.drop('Datetime', axis=1)


# analyse of surf kz miroc rcp85
kz_mean_surf_miroc_rcp85=kz_prof_miroc_rcp85.groupby(kz_prof_miroc_rcp85.index.year)['-14.25m'].mean()
kz_max_surf_miroc_rcp85=kz_prof_miroc_rcp85.groupby(kz_prof_miroc_rcp85.index.year)['-14.25m'].max()
kz_q1_surf_miroc_rcp85=kz_prof_miroc_rcp85.groupby(kz_prof_miroc_rcp85.index.year)['-14.25m'].quantile(0.25)
kz_q3_surf_miroc_rcp85=kz_prof_miroc_rcp85.groupby(kz_prof_miroc_rcp85.index.year)['-14.25m'].quantile(0.75)


#analyse of ave hypolimnetic kz miroc rcp85
hypo_kz_daily_miroc_rcp85=hypolimnetic_ave(kz_prof_2D_miroc_rcp85, hypo_morpho_vriables_gotm_grid[0] , time_series_miroc_rcp85)

mean_annual_hypo_kz_daily_miroc_rcp85=hypo_kz_daily_miroc_rcp85.groupby(hypo_kz_daily_miroc_rcp85.index.year).mean()
max_annual_hypo_kz_daily_miroc_rcp85=hypo_kz_daily_miroc_rcp85.groupby(hypo_kz_daily_miroc_rcp85.index.year).max()
q1_annual_hypo_kz_daily_miroc_rcp85=hypo_kz_daily_miroc_rcp85.groupby(hypo_kz_daily_miroc_rcp85.index.year).quantile(0.25)
q3_annual_hypo_kz_daily_miroc_rcp85=hypo_kz_daily_miroc_rcp85.groupby(hypo_kz_daily_miroc_rcp85.index.year).quantile(0.75)



#profile kz in deox miroc rcp85

#q1_annual_prof_kz_daily_miroc_rcp85= kz_prof_miroc_rcp85.groupby(kz_prof_miroc_rcp85.index.year).quantile(0.25)
#q3_annual_prof_kz_daily_miroc_rcp85= kz_prof_miroc_rcp85.groupby(kz_prof_miroc_rcp85.index.year).quantile(0.75)




# Define a custom function to calculate quantiles along columns
def calculate_group_quantile(group, quantile_value):
    return np.quantile(group, quantile_value)

kz_prof_miroc_rcp85_no_nan = kz_prof_miroc_rcp85.dropna()

# Group by the year and apply the custom function to calculate quantiles for each group
q1_annual_prof_kz_daily_miroc_rcp85 = kz_prof_miroc_rcp85_no_nan.groupby(kz_prof_miroc_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.25)


q3_annual_prof_kz_daily_miroc_rcp85 = kz_prof_miroc_rcp85_no_nan.groupby(kz_prof_miroc_rcp85_no_nan.index.year).apply(
    calculate_group_quantile, quantile_value=0.75)


#%% Averaging the GCMs 



######his
# surf kz for boundry condition 

kz_mean_surf_4models_his=(kz_mean_surf_gfdl_his+kz_mean_surf_hadgem_his+kz_mean_surf_ipsl_his+kz_mean_surf_miroc_his)/4
kz_max_surf_4models_his=(kz_max_surf_gfdl_his+kz_max_surf_hadgem_his+kz_max_surf_ipsl_his+kz_max_surf_miroc_his)/4
kz_q1_surf_4models_his=(kz_q1_surf_gfdl_his+kz_q1_surf_hadgem_his+kz_q1_surf_ipsl_his+kz_q1_surf_miroc_his)/4
kz_q3_surf_4models_his=(kz_q3_surf_gfdl_his+kz_q3_surf_hadgem_his+kz_q3_surf_ipsl_his+kz_q3_surf_miroc_his)/4

# ave hypolimnetic kz

mean_annual_hypo_kz_daily_4models_his=(mean_annual_hypo_kz_daily_gfdl_his+mean_annual_hypo_kz_daily_hadgem_his+mean_annual_hypo_kz_daily_ipsl_his+mean_annual_hypo_kz_daily_miroc_his)/4
max_annual_hypo_kz_daily_4models_his=(max_annual_hypo_kz_daily_gfdl_his+max_annual_hypo_kz_daily_hadgem_his+max_annual_hypo_kz_daily_ipsl_his+max_annual_hypo_kz_daily_miroc_his)/4
q1_annual_hypo_kz_daily_4models_his=(q1_annual_hypo_kz_daily_gfdl_his+q1_annual_hypo_kz_daily_hadgem_his+q1_annual_hypo_kz_daily_ipsl_his+q1_annual_hypo_kz_daily_miroc_his)/4
q3_annual_hypo_kz_daily_4models_his=(q3_annual_hypo_kz_daily_gfdl_his+q3_annual_hypo_kz_daily_hadgem_his+q3_annual_hypo_kz_daily_ipsl_his+q3_annual_hypo_kz_daily_miroc_his)/4


# profile kz 

q1_annual_prof_kz_daily_4models_his=(q1_annual_prof_kz_daily_gfdl_his+ q1_annual_prof_kz_daily_hadgem_his+ q1_annual_prof_kz_daily_ipsl_his+ q1_annual_prof_kz_daily_miroc_his)/4
q3_annual_prof_kz_daily_4models_his=(q3_annual_prof_kz_daily_gfdl_his+ q3_annual_prof_kz_daily_hadgem_his+ q3_annual_prof_kz_daily_ipsl_his+ q3_annual_prof_kz_daily_miroc_his)/4




######rcp26
# surf kz

kz_mean_surf_4models_rcp26=(kz_mean_surf_gfdl_rcp26+kz_mean_surf_hadgem_rcp26+kz_mean_surf_ipsl_rcp26+kz_mean_surf_miroc_rcp26)/4
kz_max_surf_4models_rcp26=(kz_max_surf_gfdl_rcp26+kz_max_surf_hadgem_rcp26+kz_max_surf_ipsl_rcp26+kz_max_surf_miroc_rcp26)/4
kz_q1_surf_4models_rcp26=(kz_q1_surf_gfdl_rcp26+kz_q1_surf_hadgem_rcp26+kz_q1_surf_ipsl_rcp26+kz_q1_surf_miroc_rcp26)/4
kz_q3_surf_4models_rcp26=(kz_q3_surf_gfdl_rcp26+kz_q3_surf_hadgem_rcp26+kz_q3_surf_ipsl_rcp26+kz_q3_surf_miroc_rcp26)/4

# ave hypolimnetic kz

mean_annual_hypo_kz_daily_4models_rcp26=(mean_annual_hypo_kz_daily_gfdl_rcp26+mean_annual_hypo_kz_daily_hadgem_rcp26+mean_annual_hypo_kz_daily_ipsl_rcp26+mean_annual_hypo_kz_daily_miroc_rcp26)/4
max_annual_hypo_kz_daily_4models_rcp26=(max_annual_hypo_kz_daily_gfdl_rcp26+max_annual_hypo_kz_daily_hadgem_rcp26+max_annual_hypo_kz_daily_ipsl_rcp26+max_annual_hypo_kz_daily_miroc_rcp26)/4
q1_annual_hypo_kz_daily_4models_rcp26=(q1_annual_hypo_kz_daily_gfdl_rcp26+q1_annual_hypo_kz_daily_hadgem_rcp26+q1_annual_hypo_kz_daily_ipsl_rcp26+q1_annual_hypo_kz_daily_miroc_rcp26)/4
q3_annual_hypo_kz_daily_4models_rcp26=(q3_annual_hypo_kz_daily_gfdl_rcp26+q3_annual_hypo_kz_daily_hadgem_rcp26+q3_annual_hypo_kz_daily_ipsl_rcp26+q3_annual_hypo_kz_daily_miroc_rcp26)/4


# profile kz 

q1_annual_prof_kz_daily_4models_rcp26=(q1_annual_prof_kz_daily_gfdl_rcp26+ q1_annual_prof_kz_daily_hadgem_rcp26+ q1_annual_prof_kz_daily_ipsl_rcp26+ q1_annual_prof_kz_daily_miroc_rcp26)/4
q3_annual_prof_kz_daily_4models_rcp26=(q3_annual_prof_kz_daily_gfdl_rcp26+ q3_annual_prof_kz_daily_hadgem_rcp26+ q3_annual_prof_kz_daily_ipsl_rcp26+ q3_annual_prof_kz_daily_miroc_rcp26)/4





######rcp60
# surf kz

kz_mean_surf_4models_rcp60=(kz_mean_surf_gfdl_rcp60+kz_mean_surf_hadgem_rcp60+kz_mean_surf_ipsl_rcp60+kz_mean_surf_miroc_rcp60)/4
kz_max_surf_4models_rcp60=(kz_max_surf_gfdl_rcp60+kz_max_surf_hadgem_rcp60+kz_max_surf_ipsl_rcp60+kz_max_surf_miroc_rcp60)/4
kz_q1_surf_4models_rcp60=(kz_q1_surf_gfdl_rcp60+kz_q1_surf_hadgem_rcp60+kz_q1_surf_ipsl_rcp60+kz_q1_surf_miroc_rcp60)/4
kz_q3_surf_4models_rcp60=(kz_q3_surf_gfdl_rcp60+kz_q3_surf_hadgem_rcp60+kz_q3_surf_ipsl_rcp60+kz_q3_surf_miroc_rcp60)/4

# ave hypolimnetic kz

mean_annual_hypo_kz_daily_4models_rcp60=(mean_annual_hypo_kz_daily_gfdl_rcp60+mean_annual_hypo_kz_daily_hadgem_rcp60+mean_annual_hypo_kz_daily_ipsl_rcp60+mean_annual_hypo_kz_daily_miroc_rcp60)/4
max_annual_hypo_kz_daily_4models_rcp60=(max_annual_hypo_kz_daily_gfdl_rcp60+max_annual_hypo_kz_daily_hadgem_rcp60+max_annual_hypo_kz_daily_ipsl_rcp60+max_annual_hypo_kz_daily_miroc_rcp60)/4
q1_annual_hypo_kz_daily_4models_rcp60=(q1_annual_hypo_kz_daily_gfdl_rcp60+q1_annual_hypo_kz_daily_hadgem_rcp60+q1_annual_hypo_kz_daily_ipsl_rcp60+q1_annual_hypo_kz_daily_miroc_rcp60)/4
q3_annual_hypo_kz_daily_4models_rcp60=(q3_annual_hypo_kz_daily_gfdl_rcp60+q3_annual_hypo_kz_daily_hadgem_rcp60+q3_annual_hypo_kz_daily_ipsl_rcp60+q3_annual_hypo_kz_daily_miroc_rcp60)/4


# profile kz 

q1_annual_prof_kz_daily_4models_rcp60=(q1_annual_prof_kz_daily_gfdl_rcp60+ q1_annual_prof_kz_daily_hadgem_rcp60+ q1_annual_prof_kz_daily_ipsl_rcp60+ q1_annual_prof_kz_daily_miroc_rcp60)/4
q3_annual_prof_kz_daily_4models_rcp60=(q3_annual_prof_kz_daily_gfdl_rcp60+ q3_annual_prof_kz_daily_hadgem_rcp60+ q3_annual_prof_kz_daily_ipsl_rcp60+ q3_annual_prof_kz_daily_miroc_rcp60)/4




######rcp85
# surf kz

kz_mean_surf_4models_rcp85=(kz_mean_surf_gfdl_rcp85+kz_mean_surf_hadgem_rcp85+kz_mean_surf_ipsl_rcp85+kz_mean_surf_miroc_rcp85)/4
kz_max_surf_4models_rcp85=(kz_max_surf_gfdl_rcp85+kz_max_surf_hadgem_rcp85+kz_max_surf_ipsl_rcp85+kz_max_surf_miroc_rcp85)/4
kz_q1_surf_4models_rcp85=(kz_q1_surf_gfdl_rcp85+kz_q1_surf_hadgem_rcp85+kz_q1_surf_ipsl_rcp85+kz_q1_surf_miroc_rcp85)/4
kz_q3_surf_4models_rcp85=(kz_q3_surf_gfdl_rcp85+kz_q3_surf_hadgem_rcp85+kz_q3_surf_ipsl_rcp85+kz_q3_surf_miroc_rcp85)/4

# ave hypolimnetic kz

mean_annual_hypo_kz_daily_4models_rcp85=(mean_annual_hypo_kz_daily_gfdl_rcp85+mean_annual_hypo_kz_daily_hadgem_rcp85+mean_annual_hypo_kz_daily_ipsl_rcp85+mean_annual_hypo_kz_daily_miroc_rcp85)/4
max_annual_hypo_kz_daily_4models_rcp85=(max_annual_hypo_kz_daily_gfdl_rcp85+max_annual_hypo_kz_daily_hadgem_rcp85+max_annual_hypo_kz_daily_ipsl_rcp85+max_annual_hypo_kz_daily_miroc_rcp85)/4
q1_annual_hypo_kz_daily_4models_rcp85=(q1_annual_hypo_kz_daily_gfdl_rcp85+q1_annual_hypo_kz_daily_hadgem_rcp85+q1_annual_hypo_kz_daily_ipsl_rcp85+q1_annual_hypo_kz_daily_miroc_rcp85)/4
q3_annual_hypo_kz_daily_4models_rcp85=(q3_annual_hypo_kz_daily_gfdl_rcp85+q3_annual_hypo_kz_daily_hadgem_rcp85+q3_annual_hypo_kz_daily_ipsl_rcp85+q3_annual_hypo_kz_daily_miroc_rcp85)/4


# profile kz 

q1_annual_prof_kz_daily_4models_rcp85=(q1_annual_prof_kz_daily_gfdl_rcp85+ q1_annual_prof_kz_daily_hadgem_rcp85+ q1_annual_prof_kz_daily_ipsl_rcp85+ q1_annual_prof_kz_daily_miroc_rcp85)/4
q3_annual_prof_kz_daily_4models_rcp85=(q3_annual_prof_kz_daily_gfdl_rcp85+ q3_annual_prof_kz_daily_hadgem_rcp85+ q3_annual_prof_kz_daily_ipsl_rcp85+ q3_annual_prof_kz_daily_miroc_rcp85)/4


#%%GLUE method apply for different GCMs:
    
#%%###################His
#%%his
# surf kz

all_kz_mean_surf_his = pd.concat([kz_mean_surf_gfdl_his, kz_mean_surf_hadgem_his, kz_mean_surf_ipsl_his, kz_mean_surf_miroc_his], axis=1)
all_kz_max_surf_his = pd.concat([kz_max_surf_gfdl_his, kz_max_surf_hadgem_his, kz_max_surf_ipsl_his, kz_max_surf_miroc_his], axis=1)
all_kz_q1_surf_his = pd.concat([kz_q1_surf_gfdl_his, kz_q1_surf_hadgem_his, kz_q1_surf_ipsl_his, kz_q1_surf_miroc_his], axis=1)
all_kz_q3_surf_his = pd.concat([kz_q3_surf_gfdl_his, kz_q3_surf_hadgem_his, kz_q3_surf_ipsl_his, kz_q3_surf_miroc_his], axis=1)


#kz_mean_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_mean_surf_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_mean_surf_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_mean_surf_his= glue_df_kz_mean_surf_his.set_index(all_kz_mean_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_his.csv'

glue_df_kz_mean_surf_his.to_csv(file_path )


#kz_max_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_max_surf_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_max_surf_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_max_surf_his= glue_df_kz_max_surf_his.set_index(all_kz_max_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_max_surf_his.csv'

glue_df_kz_max_surf_his.to_csv(file_path )



#kz_q1_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q1_surf_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q1_surf_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q1_surf_his= glue_df_kz_q1_surf_his.set_index(all_kz_q1_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q1_surf_his.csv'

glue_df_kz_q1_surf_his.to_csv(file_path )




#kz_q3_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q3_surf_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q3_surf_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q3_surf_his= glue_df_kz_q3_surf_his.set_index(all_kz_q3_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q3_surf_his.csv'

glue_df_kz_q3_surf_his.to_csv(file_path )


#%%his
# ave hypolimnetic kz


all_mean_annual_hypo_kz_his = pd.concat([mean_annual_hypo_kz_daily_gfdl_his, mean_annual_hypo_kz_daily_hadgem_his, mean_annual_hypo_kz_daily_ipsl_his, mean_annual_hypo_kz_daily_miroc_his], axis=1)
all_max_annual_hypo_kz_his = pd.concat([max_annual_hypo_kz_daily_gfdl_his, max_annual_hypo_kz_daily_hadgem_his, max_annual_hypo_kz_daily_ipsl_his, max_annual_hypo_kz_daily_miroc_his], axis=1)
all_q1_annual_hypo_kz_his = pd.concat([q1_annual_hypo_kz_daily_gfdl_his, q1_annual_hypo_kz_daily_hadgem_his, q1_annual_hypo_kz_daily_ipsl_his, q1_annual_hypo_kz_daily_miroc_his], axis=1)
all_q3_annual_hypo_kz_his = pd.concat([q3_annual_hypo_kz_daily_gfdl_his, q3_annual_hypo_kz_daily_hadgem_his, q3_annual_hypo_kz_daily_ipsl_his, q3_annual_hypo_kz_daily_miroc_his], axis=1)



#all_mean_annual_hypo_kz_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_mean_annual_hypo_kz_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_mean_annual_hypo_kz_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_mean_annual_hypo_kz_his= glue_df_mean_annual_hypo_kz_his.set_index(all_kz_mean_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_his.csv'

glue_df_mean_annual_hypo_kz_his.to_csv(file_path )



#all_max_annual_hypo_kz_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_max_annual_hypo_kz_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_max_annual_hypo_kz_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_max_annual_hypo_kz_his= glue_df_max_annual_hypo_kz_his.set_index(all_kz_max_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_max_annual_hypo_kz_his.csv'

glue_df_max_annual_hypo_kz_his.to_csv(file_path )



#all_q1_annual_hypo_kz_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_hypo_kz_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_hypo_kz_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_hypo_kz_his= glue_df_q1_annual_hypo_kz_his.set_index(all_kz_q1_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_hypo_kz_his.csv'

glue_df_q1_annual_hypo_kz_his.to_csv(file_path )



#all_q3_annual_hypo_kz_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_hypo_kz_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_hypo_kz_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_hypo_kz_his= glue_df_q3_annual_hypo_kz_his.set_index(all_kz_q3_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_hypo_kz_his.csv'

glue_df_q3_annual_hypo_kz_his.to_csv(file_path )


#%%his
# profile kz 


all_q1_annual_prof_kz_his = pd.concat([q1_annual_prof_kz_daily_gfdl_his, q1_annual_prof_kz_daily_hadgem_his, q1_annual_prof_kz_daily_ipsl_his, q1_annual_prof_kz_daily_miroc_his], axis=1)
all_q3_annual_prof_kz_his = pd.concat([q3_annual_prof_kz_daily_gfdl_his, q3_annual_prof_kz_daily_hadgem_his, q3_annual_prof_kz_daily_ipsl_his, q3_annual_prof_kz_daily_miroc_his], axis=1)




#all_q1_annual_prof_kz_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_prof_kz_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_prof_kz_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_prof_kz_his= glue_df_q1_annual_prof_kz_his.set_index(all_kz_q1_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_prof_kz_his.csv'

glue_df_q1_annual_prof_kz_his.to_csv(file_path )





#all_q3_annual_prof_kz_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_prof_kz_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_prof_kz_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_prof_kz_his= glue_df_q3_annual_prof_kz_his.set_index(all_kz_q3_surf_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_prof_kz_his.csv'

glue_df_q3_annual_prof_kz_his.to_csv(file_path )




#%%=====================rcp26
#%%rcp26
# surf kz

all_kz_mean_surf_rcp26 = pd.concat([kz_mean_surf_gfdl_rcp26, kz_mean_surf_hadgem_rcp26, kz_mean_surf_ipsl_rcp26, kz_mean_surf_miroc_rcp26], axis=1)
all_kz_max_surf_rcp26 = pd.concat([kz_max_surf_gfdl_rcp26, kz_max_surf_hadgem_rcp26, kz_max_surf_ipsl_rcp26, kz_max_surf_miroc_rcp26], axis=1)
all_kz_q1_surf_rcp26 = pd.concat([kz_q1_surf_gfdl_rcp26, kz_q1_surf_hadgem_rcp26, kz_q1_surf_ipsl_rcp26, kz_q1_surf_miroc_rcp26], axis=1)
all_kz_q3_surf_rcp26 = pd.concat([kz_q3_surf_gfdl_rcp26, kz_q3_surf_hadgem_rcp26, kz_q3_surf_ipsl_rcp26, kz_q3_surf_miroc_rcp26], axis=1)


#kz_mean_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_mean_surf_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_mean_surf_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_mean_surf_rcp26= glue_df_kz_mean_surf_rcp26.set_index(all_kz_mean_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_rcp26.csv'

glue_df_kz_mean_surf_rcp26.to_csv(file_path )


#kz_max_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_max_surf_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_max_surf_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_max_surf_rcp26= glue_df_kz_max_surf_rcp26.set_index(all_kz_max_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_max_surf_rcp26.csv'

glue_df_kz_max_surf_rcp26.to_csv(file_path )



#kz_q1_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q1_surf_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q1_surf_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q1_surf_rcp26= glue_df_kz_q1_surf_rcp26.set_index(all_kz_q1_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q1_surf_rcp26.csv'

glue_df_kz_q1_surf_rcp26.to_csv(file_path )




#kz_q3_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q3_surf_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q3_surf_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q3_surf_rcp26= glue_df_kz_q3_surf_rcp26.set_index(all_kz_q3_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q3_surf_rcp26.csv'

glue_df_kz_q3_surf_rcp26.to_csv(file_path )


#%%rcp26
# ave hypolimnetic kz


all_mean_annual_hypo_kz_rcp26 = pd.concat([mean_annual_hypo_kz_daily_gfdl_rcp26, mean_annual_hypo_kz_daily_hadgem_rcp26, mean_annual_hypo_kz_daily_ipsl_rcp26, mean_annual_hypo_kz_daily_miroc_rcp26], axis=1)
all_max_annual_hypo_kz_rcp26 = pd.concat([max_annual_hypo_kz_daily_gfdl_rcp26, max_annual_hypo_kz_daily_hadgem_rcp26, max_annual_hypo_kz_daily_ipsl_rcp26, max_annual_hypo_kz_daily_miroc_rcp26], axis=1)
all_q1_annual_hypo_kz_rcp26 = pd.concat([q1_annual_hypo_kz_daily_gfdl_rcp26, q1_annual_hypo_kz_daily_hadgem_rcp26, q1_annual_hypo_kz_daily_ipsl_rcp26, q1_annual_hypo_kz_daily_miroc_rcp26], axis=1)
all_q3_annual_hypo_kz_rcp26 = pd.concat([q3_annual_hypo_kz_daily_gfdl_rcp26, q3_annual_hypo_kz_daily_hadgem_rcp26, q3_annual_hypo_kz_daily_ipsl_rcp26, q3_annual_hypo_kz_daily_miroc_rcp26], axis=1)



#all_mean_annual_hypo_kz_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_mean_annual_hypo_kz_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_mean_annual_hypo_kz_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_mean_annual_hypo_kz_rcp26= glue_df_mean_annual_hypo_kz_rcp26.set_index(all_kz_mean_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_rcp26.csv'

glue_df_mean_annual_hypo_kz_rcp26.to_csv(file_path )



#all_max_annual_hypo_kz_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_max_annual_hypo_kz_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_max_annual_hypo_kz_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_max_annual_hypo_kz_rcp26= glue_df_max_annual_hypo_kz_rcp26.set_index(all_kz_max_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_max_annual_hypo_kz_rcp26.csv'

glue_df_max_annual_hypo_kz_rcp26.to_csv(file_path )



#all_q1_annual_hypo_kz_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_hypo_kz_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_hypo_kz_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_hypo_kz_rcp26= glue_df_q1_annual_hypo_kz_rcp26.set_index(all_kz_q1_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_hypo_kz_rcp26.csv'

glue_df_q1_annual_hypo_kz_rcp26.to_csv(file_path )



#all_q3_annual_hypo_kz_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_hypo_kz_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_hypo_kz_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_hypo_kz_rcp26= glue_df_q3_annual_hypo_kz_rcp26.set_index(all_kz_q3_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_hypo_kz_rcp26.csv'

glue_df_q3_annual_hypo_kz_rcp26.to_csv(file_path )


#%%rcp26
# profile kz 


all_q1_annual_prof_kz_rcp26 = pd.concat([q1_annual_prof_kz_daily_gfdl_rcp26, q1_annual_prof_kz_daily_hadgem_rcp26, q1_annual_prof_kz_daily_ipsl_rcp26, q1_annual_prof_kz_daily_miroc_rcp26], axis=1)
all_q3_annual_prof_kz_rcp26 = pd.concat([q3_annual_prof_kz_daily_gfdl_rcp26, q3_annual_prof_kz_daily_hadgem_rcp26, q3_annual_prof_kz_daily_ipsl_rcp26, q3_annual_prof_kz_daily_miroc_rcp26], axis=1)




#all_q1_annual_prof_kz_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_prof_kz_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_prof_kz_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_prof_kz_rcp26= glue_df_q1_annual_prof_kz_rcp26.set_index(all_kz_q1_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_prof_kz_rcp26.csv'

glue_df_q1_annual_prof_kz_rcp26.to_csv(file_path )





#all_q3_annual_prof_kz_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_prof_kz_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_prof_kz_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_prof_kz_rcp26= glue_df_q3_annual_prof_kz_rcp26.set_index(all_kz_q3_surf_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_prof_kz_rcp26.csv'

glue_df_q3_annual_prof_kz_rcp26.to_csv(file_path )


#%%=============rcp60
#%%rcp60
# surf kz

all_kz_mean_surf_rcp60 = pd.concat([kz_mean_surf_gfdl_rcp60, kz_mean_surf_hadgem_rcp60, kz_mean_surf_ipsl_rcp60, kz_mean_surf_miroc_rcp60], axis=1)
all_kz_max_surf_rcp60 = pd.concat([kz_max_surf_gfdl_rcp60, kz_max_surf_hadgem_rcp60, kz_max_surf_ipsl_rcp60, kz_max_surf_miroc_rcp60], axis=1)
all_kz_q1_surf_rcp60 = pd.concat([kz_q1_surf_gfdl_rcp60, kz_q1_surf_hadgem_rcp60, kz_q1_surf_ipsl_rcp60, kz_q1_surf_miroc_rcp60], axis=1)
all_kz_q3_surf_rcp60 = pd.concat([kz_q3_surf_gfdl_rcp60, kz_q3_surf_hadgem_rcp60, kz_q3_surf_ipsl_rcp60, kz_q3_surf_miroc_rcp60], axis=1)


#kz_mean_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_mean_surf_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_mean_surf_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_mean_surf_rcp60= glue_df_kz_mean_surf_rcp60.set_index(all_kz_mean_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_rcp60.csv'

glue_df_kz_mean_surf_rcp60.to_csv(file_path )


#kz_max_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_max_surf_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_max_surf_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_max_surf_rcp60= glue_df_kz_max_surf_rcp60.set_index(all_kz_max_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_max_surf_rcp60.csv'

glue_df_kz_max_surf_rcp60.to_csv(file_path )



#kz_q1_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q1_surf_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q1_surf_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q1_surf_rcp60= glue_df_kz_q1_surf_rcp60.set_index(all_kz_q1_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q1_surf_rcp60.csv'

glue_df_kz_q1_surf_rcp60.to_csv(file_path )




#kz_q3_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q3_surf_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q3_surf_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q3_surf_rcp60= glue_df_kz_q3_surf_rcp60.set_index(all_kz_q3_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q3_surf_rcp60.csv'

glue_df_kz_q3_surf_rcp60.to_csv(file_path )


#%%rcp60
# ave hypolimnetic kz


all_mean_annual_hypo_kz_rcp60 = pd.concat([mean_annual_hypo_kz_daily_gfdl_rcp60, mean_annual_hypo_kz_daily_hadgem_rcp60, mean_annual_hypo_kz_daily_ipsl_rcp60, mean_annual_hypo_kz_daily_miroc_rcp60], axis=1)
all_max_annual_hypo_kz_rcp60 = pd.concat([max_annual_hypo_kz_daily_gfdl_rcp60, max_annual_hypo_kz_daily_hadgem_rcp60, max_annual_hypo_kz_daily_ipsl_rcp60, max_annual_hypo_kz_daily_miroc_rcp60], axis=1)
all_q1_annual_hypo_kz_rcp60 = pd.concat([q1_annual_hypo_kz_daily_gfdl_rcp60, q1_annual_hypo_kz_daily_hadgem_rcp60, q1_annual_hypo_kz_daily_ipsl_rcp60, q1_annual_hypo_kz_daily_miroc_rcp60], axis=1)
all_q3_annual_hypo_kz_rcp60 = pd.concat([q3_annual_hypo_kz_daily_gfdl_rcp60, q3_annual_hypo_kz_daily_hadgem_rcp60, q3_annual_hypo_kz_daily_ipsl_rcp60, q3_annual_hypo_kz_daily_miroc_rcp60], axis=1)



#all_mean_annual_hypo_kz_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_mean_annual_hypo_kz_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_mean_annual_hypo_kz_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_mean_annual_hypo_kz_rcp60= glue_df_mean_annual_hypo_kz_rcp60.set_index(all_kz_mean_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_rcp60.csv'

glue_df_mean_annual_hypo_kz_rcp60.to_csv(file_path )



#all_max_annual_hypo_kz_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_max_annual_hypo_kz_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_max_annual_hypo_kz_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_max_annual_hypo_kz_rcp60= glue_df_max_annual_hypo_kz_rcp60.set_index(all_kz_max_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_max_annual_hypo_kz_rcp60.csv'

glue_df_max_annual_hypo_kz_rcp60.to_csv(file_path )



#all_q1_annual_hypo_kz_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_hypo_kz_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_hypo_kz_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_hypo_kz_rcp60= glue_df_q1_annual_hypo_kz_rcp60.set_index(all_kz_q1_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_hypo_kz_rcp60.csv'

glue_df_q1_annual_hypo_kz_rcp60.to_csv(file_path )



#all_q3_annual_hypo_kz_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_hypo_kz_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_hypo_kz_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_hypo_kz_rcp60= glue_df_q3_annual_hypo_kz_rcp60.set_index(all_kz_q3_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_hypo_kz_rcp60.csv'

glue_df_q3_annual_hypo_kz_rcp60.to_csv(file_path )


#%%rcp60
# profile kz 


all_q1_annual_prof_kz_rcp60 = pd.concat([q1_annual_prof_kz_daily_gfdl_rcp60, q1_annual_prof_kz_daily_hadgem_rcp60, q1_annual_prof_kz_daily_ipsl_rcp60, q1_annual_prof_kz_daily_miroc_rcp60], axis=1)
all_q3_annual_prof_kz_rcp60 = pd.concat([q3_annual_prof_kz_daily_gfdl_rcp60, q3_annual_prof_kz_daily_hadgem_rcp60, q3_annual_prof_kz_daily_ipsl_rcp60, q3_annual_prof_kz_daily_miroc_rcp60], axis=1)




#all_q1_annual_prof_kz_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_prof_kz_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_prof_kz_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_prof_kz_rcp60= glue_df_q1_annual_prof_kz_rcp60.set_index(all_kz_q1_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_prof_kz_rcp60.csv'

glue_df_q1_annual_prof_kz_rcp60.to_csv(file_path )





#all_q3_annual_prof_kz_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_prof_kz_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_prof_kz_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_prof_kz_rcp60= glue_df_q3_annual_prof_kz_rcp60.set_index(all_kz_q3_surf_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_prof_kz_rcp60.csv'

glue_df_q3_annual_prof_kz_rcp60.to_csv(file_path )

#%%============rcp85
#%%rcp85
# surf kz

all_kz_mean_surf_rcp85 = pd.concat([kz_mean_surf_gfdl_rcp85, kz_mean_surf_hadgem_rcp85, kz_mean_surf_ipsl_rcp85, kz_mean_surf_miroc_rcp85], axis=1)
all_kz_max_surf_rcp85 = pd.concat([kz_max_surf_gfdl_rcp85, kz_max_surf_hadgem_rcp85, kz_max_surf_ipsl_rcp85, kz_max_surf_miroc_rcp85], axis=1)
all_kz_q1_surf_rcp85 = pd.concat([kz_q1_surf_gfdl_rcp85, kz_q1_surf_hadgem_rcp85, kz_q1_surf_ipsl_rcp85, kz_q1_surf_miroc_rcp85], axis=1)
all_kz_q3_surf_rcp85 = pd.concat([kz_q3_surf_gfdl_rcp85, kz_q3_surf_hadgem_rcp85, kz_q3_surf_ipsl_rcp85, kz_q3_surf_miroc_rcp85], axis=1)


#kz_mean_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_mean_surf_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_mean_surf_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_mean_surf_rcp85= glue_df_kz_mean_surf_rcp85.set_index(all_kz_mean_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_rcp85.csv'

glue_df_kz_mean_surf_rcp85.to_csv(file_path )


#kz_max_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_max_surf_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_max_surf_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_max_surf_rcp85= glue_df_kz_max_surf_rcp85.set_index(all_kz_max_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_max_surf_rcp85.csv'

glue_df_kz_max_surf_rcp85.to_csv(file_path )



#kz_q1_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q1_surf_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q1_surf_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q1_surf_rcp85= glue_df_kz_q1_surf_rcp85.set_index(all_kz_q1_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q1_surf_rcp85.csv'

glue_df_kz_q1_surf_rcp85.to_csv(file_path )




#kz_q3_surf
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_kz_q3_surf_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_kz_q3_surf_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_kz_q3_surf_rcp85= glue_df_kz_q3_surf_rcp85.set_index(all_kz_q3_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_q3_surf_rcp85.csv'

glue_df_kz_q3_surf_rcp85.to_csv(file_path )


#%%rcp85
# ave hypolimnetic kz


all_mean_annual_hypo_kz_rcp85 = pd.concat([mean_annual_hypo_kz_daily_gfdl_rcp85, mean_annual_hypo_kz_daily_hadgem_rcp85, mean_annual_hypo_kz_daily_ipsl_rcp85, mean_annual_hypo_kz_daily_miroc_rcp85], axis=1)
all_max_annual_hypo_kz_rcp85 = pd.concat([max_annual_hypo_kz_daily_gfdl_rcp85, max_annual_hypo_kz_daily_hadgem_rcp85, max_annual_hypo_kz_daily_ipsl_rcp85, max_annual_hypo_kz_daily_miroc_rcp85], axis=1)
all_q1_annual_hypo_kz_rcp85 = pd.concat([q1_annual_hypo_kz_daily_gfdl_rcp85, q1_annual_hypo_kz_daily_hadgem_rcp85, q1_annual_hypo_kz_daily_ipsl_rcp85, q1_annual_hypo_kz_daily_miroc_rcp85], axis=1)
all_q3_annual_hypo_kz_rcp85 = pd.concat([q3_annual_hypo_kz_daily_gfdl_rcp85, q3_annual_hypo_kz_daily_hadgem_rcp85, q3_annual_hypo_kz_daily_ipsl_rcp85, q3_annual_hypo_kz_daily_miroc_rcp85], axis=1)



#all_mean_annual_hypo_kz_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_mean_annual_hypo_kz_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_mean_annual_hypo_kz_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_mean_annual_hypo_kz_rcp85= glue_df_mean_annual_hypo_kz_rcp85.set_index(all_kz_mean_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_kz_mean_surf_rcp85.csv'

glue_df_mean_annual_hypo_kz_rcp85.to_csv(file_path )



#all_max_annual_hypo_kz_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_max_annual_hypo_kz_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_max_annual_hypo_kz_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_max_annual_hypo_kz_rcp85= glue_df_max_annual_hypo_kz_rcp85.set_index(all_kz_max_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_max_annual_hypo_kz_rcp85.csv'

glue_df_max_annual_hypo_kz_rcp85.to_csv(file_path )



#all_q1_annual_hypo_kz_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_hypo_kz_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_hypo_kz_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_hypo_kz_rcp85= glue_df_q1_annual_hypo_kz_rcp85.set_index(all_kz_q1_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_hypo_kz_rcp85.csv'

glue_df_q1_annual_hypo_kz_rcp85.to_csv(file_path )



#all_q3_annual_hypo_kz_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_hypo_kz_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_hypo_kz_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_hypo_kz_rcp85= glue_df_q3_annual_hypo_kz_rcp85.set_index(all_kz_q3_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_hypo_kz_rcp85.csv'

glue_df_q3_annual_hypo_kz_rcp85.to_csv(file_path )


#%%rcp85
# profile kz 


all_q1_annual_prof_kz_rcp85 = pd.concat([q1_annual_prof_kz_daily_gfdl_rcp85, q1_annual_prof_kz_daily_hadgem_rcp85, q1_annual_prof_kz_daily_ipsl_rcp85, q1_annual_prof_kz_daily_miroc_rcp85], axis=1)
all_q3_annual_prof_kz_rcp85 = pd.concat([q3_annual_prof_kz_daily_gfdl_rcp85, q3_annual_prof_kz_daily_hadgem_rcp85, q3_annual_prof_kz_daily_ipsl_rcp85, q3_annual_prof_kz_daily_miroc_rcp85], axis=1)




#all_q1_annual_prof_kz_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q1_annual_prof_kz_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q1_annual_prof_kz_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q1_annual_prof_kz_rcp85= glue_df_q1_annual_prof_kz_rcp85.set_index(all_kz_q1_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q1_annual_prof_kz_rcp85.csv'

glue_df_q1_annual_prof_kz_rcp85.to_csv(file_path )





#all_q3_annual_prof_kz_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_q3_annual_prof_kz_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_q3_annual_prof_kz_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_q3_annual_prof_kz_rcp85= glue_df_q3_annual_prof_kz_rcp85.set_index(all_kz_q3_surf_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_q3_annual_prof_kz_rcp85.csv'

glue_df_q3_annual_prof_kz_rcp85.to_csv(file_path )

#%%80yeras for mena surface of hypolimnion kz 


glue_df_kz_mean_surf_80years_rcp26=glue_df_kz_mean_surf_rcp26[glue_df_kz_mean_surf_rcp26.index>2019]
glue_df_kz_mean_surf_80years_rcp60=glue_df_kz_mean_surf_rcp60[glue_df_kz_mean_surf_rcp60.index>2019]
glue_df_kz_mean_surf_80years_rcp85=glue_df_kz_mean_surf_rcp85[glue_df_kz_mean_surf_rcp85.index>2019]


#trends on median glue method aftersubstracting 



autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_80years_rcp26['50%'])
"""
(0.05417432217392027,
 'positively autocorrelated',
 'no trend',
 0.13582402545394978,
 1.0746178293689123e-08,
 8.55776274548289e-06)
"""
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_80years_rcp60['50%'])
"""
(0.04798423901787456,
 'positively autocorrelated',
 'no trend',
 0.9195845047358031,
 4.969795106792337e-10,
 8.735593945838803e-06)
"""
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_80years_rcp85['50%'])
"""
(0.045482080388108095,
 'positively autocorrelated',
 'no trend',
 0.3347506318028546,
 4.4423686483659546e-09,
 8.45554592927376e-06)
"""

#%%100years_rcp26

# kz_surf

glue_df_kz_mean_surf_100years_rcp26=pd.concat([glue_df_kz_mean_surf_his[glue_df_kz_mean_surf_his.index>1999] , glue_df_kz_mean_surf_rcp26])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_100years_rcp26['50%'])
(0.046884035188155974,
 'positively autocorrelated',
 'no trend',
 0.5417633890092233,
 -3.5361739827413693e-09,
 9.363124706356363e-06)



glue_df_kz_max_surf_100years_rcp26=pd.concat([glue_df_kz_max_surf_his[glue_df_kz_max_surf_his.index>1999] , glue_df_kz_max_surf_rcp26])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_max_surf_100years_rcp26['50%'])
(0.3688036887514171,
 'positively autocorrelated',
 'no trend',
 0.7364733460404922,
 -1.9027320461204654e-08,
 3.529931257124143e-05)




#************
glue_df_kz_q1_surf_100years_rcp26=pd.concat([glue_df_kz_q1_surf_his[glue_df_kz_q1_surf_his.index>1999] , glue_df_kz_q1_surf_rcp26])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q1_surf_100years_rcp26['50%'])
(0.009896329003630666,
 'positively autocorrelated',
 'decreasing',
 0.007008152030631765,
 -3.1893761943860208e-09,
 5.258969447321242e-06)

glue_df_kz_q3_surf_100years_rcp26=pd.concat([glue_df_kz_q3_surf_his[glue_df_kz_q3_surf_his.index>1999] , glue_df_kz_q3_surf_rcp26])
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q3_surf_100years_rcp26['50%'])
(0.05163903570818445,
 'positively autocorrelated',
 'no trend',
 0.7502915246932909,
 -1.5911755498632947e-09,
 9.804571430264263e-06)


glue_df_mean_annual_hypo_kz_100years_rcp26=pd.concat([glue_df_mean_annual_hypo_kz_his[glue_df_mean_annual_hypo_kz_his.index>1999] , glue_df_mean_annual_hypo_kz_rcp26])
autocorr_MK_org_modif_sens_slope_test(glue_df_mean_annual_hypo_kz_100years_rcp26['50%'])
(0.05943017728705878,
 'positively autocorrelated',
 'no trend',
 0.429994567578992,
 -5.988155385092922e-09,
 1.4372642164614984e-05)


glue_df_max_annual_hypo_kz_100years_rcp26=pd.concat([glue_df_max_annual_hypo_kz_his[glue_df_max_annual_hypo_kz_his.index>1999] , glue_df_max_annual_hypo_kz_rcp26])

autocorr_MK_org_modif_sens_slope_test(glue_df_max_annual_hypo_kz_100years_rcp26['50%'])
(0.5434295868438984,
 'positively autocorrelated',
 'no trend',
 0.7545068763348606,
 -2.6997034140222474e-08,
 5.306572970570196e-05)



#*********
glue_df_q1_annual_hypo_kz_100years_rcp26=pd.concat([glue_df_q1_annual_hypo_kz_his[glue_df_q1_annual_hypo_kz_his.index>1999] , glue_df_q1_annual_hypo_kz_rcp26])

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_hypo_kz_100years_rcp26['50%'])

(0.010480834286798907,
 'positively autocorrelated',
 'decreasing',
 0.0047187022744212825,
 -5.058803487126356e-09,
 8.023699792637555e-06)


glue_df_q3_annual_hypo_kz_100years_rcp26=pd.concat([glue_df_q3_annual_hypo_kz_his[glue_df_q3_annual_hypo_kz_his.index>1999] , glue_df_q3_annual_hypo_kz_rcp26])
autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_hypo_kz_100years_rcp26['50%'])
(0.05382367396974506,
 'positively autocorrelated',
 'no trend',
 0.414137300389986,
 -7.345646365444172e-09,
 1.5306433669211783e-05)

#**********
glue_df_q1_annual_prof_kz_100years_rcp26=pd.concat([glue_df_q1_annual_prof_kz_his[glue_df_q1_annual_prof_kz_his.index>1999] , glue_df_q1_annual_prof_kz_rcp26])

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_prof_kz_100years_rcp26['50%'])
(0.0131873002199893,
 'positively autocorrelated',
 'decreasing',
 0.036294192036571804,
 -6.79870903278849e-09,
 1.0325015843548612e-05)


glue_df_q3_annual_prof_kz_100years_rcp26=pd.concat([glue_df_q3_annual_prof_kz_his[glue_df_q3_annual_prof_kz_his.index>1999] , glue_df_q3_annual_prof_kz_rcp26])

autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_prof_kz_100years_rcp26['50%'])
(0.04470986544111163,
 'positively autocorrelated',
 'no trend',
 0.20321765272968184,
 -2.257300302233034e-08,
 3.205282810103682e-05)


########100years_rcp60

# kz_surf

glue_df_kz_mean_surf_100years_rcp60=pd.concat([glue_df_kz_mean_surf_his[glue_df_kz_mean_surf_his.index>1999] , glue_df_kz_mean_surf_rcp60])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_100years_rcp60['50%'])
(0.051103716140044046,
 'positively autocorrelated',
 'no trend',
 0.518706156904464,
 -2.7267217999686867e-09,
 9.047168696874266e-06)


glue_df_kz_max_surf_100years_rcp60=pd.concat([glue_df_kz_max_surf_his[glue_df_kz_max_surf_his.index>1999] , glue_df_kz_max_surf_rcp60])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_max_surf_100years_rcp60['50%'])
(0.2755338610764595,
 'positively autocorrelated',
 'no trend',
 0.1831172231921261,
 5.495175871500888e-08,
 3.263293653175631e-05)


#********
glue_df_kz_q1_surf_100years_rcp60=pd.concat([glue_df_kz_q1_surf_his[glue_df_kz_q1_surf_his.index>1999] , glue_df_kz_q1_surf_rcp60])


autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q1_surf_100years_rcp60['50%'])
(0.01500255255500623,
 'positively autocorrelated',
 'decreasing',
 0.04869994685257306,
 -3.201315855811984e-09,
 5.003350090308798e-06)



#********
glue_df_kz_q3_surf_100years_rcp60=pd.concat([glue_df_kz_q3_surf_his[glue_df_kz_q3_surf_his.index>1999] , glue_df_kz_q3_surf_rcp60])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q3_surf_100years_rcp60['50%'])
(0.060112128101325234,
 'positively autocorrelated',
 'decreasing',
 0.0009101998201297423,
 -9.361894190872063e-09,
 9.935631261699369e-06)

#hypolimnetic average kz 

glue_df_mean_annual_hypo_kz_100years_rcp60=pd.concat([glue_df_mean_annual_hypo_kz_his[glue_df_mean_annual_hypo_kz_his.index>1999] , glue_df_mean_annual_hypo_kz_rcp60])

autocorr_MK_org_modif_sens_slope_test(glue_df_mean_annual_hypo_kz_100years_rcp60['50%'])
(0.05775567457682771,
 'positively autocorrelated',
 'no trend',
 0.47951254715795044,
 -4.099411775210935e-09,
 1.377147368191975e-05)




glue_df_max_annual_hypo_kz_100years_rcp60=pd.concat([glue_df_max_annual_hypo_kz_his[glue_df_max_annual_hypo_kz_his.index>1999] , glue_df_max_annual_hypo_kz_rcp60])

autocorr_MK_org_modif_sens_slope_test(glue_df_max_annual_hypo_kz_100years_rcp60['50%'])
(0.3101986437245928,
 'positively autocorrelated',
 'no trend',
 0.25194801456513805,
 1.0328241448477959e-07,
 5.065689644317174e-05)

#*************
glue_df_q1_annual_hypo_kz_100years_rcp60=pd.concat([glue_df_q1_annual_hypo_kz_his[glue_df_q1_annual_hypo_kz_his.index>1999] , glue_df_q1_annual_hypo_kz_rcp60])

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_hypo_kz_100years_rcp60['50%'])
(0.014740766664791412,
 'positively autocorrelated',
 'decreasing',
 0.016587065252473998,
 -5.122552673569674e-09,
 7.633994082116036e-06)




glue_df_q3_annual_hypo_kz_100years_rcp60=pd.concat([glue_df_q3_annual_hypo_kz_his[glue_df_q3_annual_hypo_kz_his.index>1999] , glue_df_q3_annual_hypo_kz_rcp60])

#*************
autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_hypo_kz_100years_rcp60['50%'])
(0.05978024407405554,
 'positively autocorrelated',
 'decreasing',
 0.01420324944550222,
 -1.7214066869694555e-08,
 1.5399047794253387e-05)


# q1 and q3 of the kz profile in each year 

glue_df_q1_annual_prof_kz_100years_rcp60=pd.concat([glue_df_q1_annual_prof_kz_his[glue_df_q1_annual_prof_kz_his.index>1999] , glue_df_q1_annual_prof_kz_rcp60])

#************
autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_prof_kz_100years_rcp60['50%'])
(0.014399744110414309,
 'positively autocorrelated',
 'decreasing',
 0.013109846222880028,
 -8.216742181892706e-09,
 1.0020593073737213e-05)



glue_df_q3_annual_prof_kz_100years_rcp60=pd.concat([glue_df_q3_annual_prof_kz_his[glue_df_q3_annual_prof_kz_his.index>1999] , glue_df_q3_annual_prof_kz_rcp60])

autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_prof_kz_100years_rcp60['50%'])
(0.043710042575329275,
 'positively autocorrelated',
 'no trend',
 0.0636517179624001,
 0,
 0)


#########100years_rcp85

# kz_surf

glue_df_kz_mean_surf_100years_rcp85=pd.concat([glue_df_kz_mean_surf_his[glue_df_kz_mean_surf_his.index>1999] , glue_df_kz_mean_surf_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_100years_rcp85['50%'])
(0.047420472236848005,
 'positively autocorrelated',
 'no trend',
 0.7818070877001895,
 -1.3764035597563987e-09,
 8.748336607674429e-06)



glue_df_kz_max_surf_100years_rcp85=pd.concat([glue_df_kz_max_surf_his[glue_df_kz_max_surf_his.index>1999] , glue_df_kz_max_surf_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_max_surf_100years_rcp85['50%'])
(0.382264945529652,
 'positively autocorrelated',
 'no trend',
 0.0971733455988324,
 7.7152924585255e-08,
 3.1086828024789224e-05)




glue_df_kz_q1_surf_100years_rcp85=pd.concat([glue_df_kz_q1_surf_his[glue_df_kz_q1_surf_his.index>1999] , glue_df_kz_q1_surf_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q1_surf_100years_rcp85['50%'])
(0.015320149847864997,
 'positively autocorrelated',
 'no trend',
 0.13191473135599852,
 -2.2676014156523197e-09,
 4.929254076043177e-06)


glue_df_kz_q3_surf_100years_rcp85=pd.concat([glue_df_kz_q3_surf_his[glue_df_kz_q3_surf_his.index>1999] , glue_df_kz_q3_surf_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q3_surf_100years_rcp85['50%'])
(0.052359728128059536,
 'positively autocorrelated',
 'no trend',
 0.447601484321563,
 -4.178000515368833e-09,
 9.690471588147698e-06)



#hypolimnetic average kz 

glue_df_mean_annual_hypo_kz_100years_rcp85=pd.concat([glue_df_mean_annual_hypo_kz_his[glue_df_mean_annual_hypo_kz_his.index>1999] , glue_df_mean_annual_hypo_kz_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_mean_annual_hypo_kz_100years_rcp85['50%'])
(0.05881963174839293,
 'positively autocorrelated',
 'no trend',
 0.9453902579786444,
 -4.970634941612069e-10,
 1.3367804065831055e-05)


#************
glue_df_max_annual_hypo_kz_100years_rcp85=pd.concat([glue_df_max_annual_hypo_kz_his[glue_df_max_annual_hypo_kz_his.index>1999] , glue_df_max_annual_hypo_kz_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_max_annual_hypo_kz_100years_rcp85['50%'])
(0.5400988937200495,
 'positively autocorrelated',
 'increasing',
 0.02406035964682207,
 1.4629325937566286e-07,
 4.6348875633331066e-05)


#***********
glue_df_q1_annual_hypo_kz_100years_rcp85=pd.concat([glue_df_q1_annual_hypo_kz_his[glue_df_q1_annual_hypo_kz_his.index>1999] , glue_df_q1_annual_hypo_kz_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_hypo_kz_100years_rcp85['50%'])
(0.014855020687852206,
 'positively autocorrelated',
 'decreasing',
 0.017215442850234686,
 -3.612440296524522e-09,
 7.4755752758871605e-06)

glue_df_q3_annual_hypo_kz_100years_rcp85=pd.concat([glue_df_q3_annual_hypo_kz_his[glue_df_q3_annual_hypo_kz_his.index>1999] , glue_df_q3_annual_hypo_kz_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_hypo_kz_100years_rcp85['50%'])
(0.057634344553260254,
 'positively autocorrelated',
 'no trend',
 0.3360839024166671,
 -9.434941712172255e-09,
 1.5003463236504557e-05)

# q1 and q3 of the kz profile in each year 

glue_df_q1_annual_prof_kz_100years_rcp85=pd.concat([glue_df_q1_annual_prof_kz_his[glue_df_q1_annual_prof_kz_his.index>1999] , glue_df_q1_annual_prof_kz_rcp85])

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_prof_kz_100years_rcp85['50%'])
(0.014560238516021663,
 'positively autocorrelated',
 'no trend',
 0.208148239730217,
 -3.941368049709126e-09,
 9.84522224371176e-06)



glue_df_q3_annual_prof_kz_100years_rcp85=pd.concat([glue_df_q3_annual_prof_kz_his[glue_df_q3_annual_prof_kz_his.index>1999] , glue_df_q3_annual_prof_kz_rcp85])


autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_prof_kz_100years_rcp85['50%'])
(0.040986174982611395,
 'positively autocorrelated',
 'no trend',
 0.777237323618158,
 -5.104325264701902e-09,
 2.979967006607174e-05)



#%% 80 years for RCPs












#In tow cases 
#glue_df_kz_max_surf_80years_rcp60 (incresaing) and 
#glue_df_q1_annual_hypo_kz_80years_rcp85 (increasing )

# But they are no chjanges in ave or q1, q3 of  profile 

glue_df_kz_mean_surf_80years_rcp26=glue_df_kz_mean_surf_rcp26[glue_df_kz_mean_surf_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_80years_rcp26['50%'])
(0.05417432217392027,
 'positively autocorrelated',
 'no trend',
 0.13582402545394978,
 0,
 0)



glue_df_kz_max_surf_80years_rcp26=glue_df_kz_max_surf_rcp26[glue_df_kz_max_surf_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_max_surf_80years_rcp26['50%'])
(0.4271494021835759,
 'positively autocorrelated',
 'no trend',
 0.26730299952847436,
 0,
 0)



glue_df_kz_q1_surf_80years_rcp26=glue_df_kz_q1_surf_rcp26[glue_df_kz_q1_surf_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q1_surf_80years_rcp26['50%'])
(0.010434659253858102,
 'positively autocorrelated',
 'no trend',
 0.43276811912715285,
 0,
 0)



glue_df_kz_q3_surf_80years_rcp26=glue_df_kz_q1_surf_rcp26[glue_df_kz_q3_surf_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q3_surf_80years_rcp26['50%'])
(0.010434659253858102,
 'positively autocorrelated',
 'no trend',
 0.43276811912715285,
 0,
 0)
#hypolimnetic average kz 

glue_df_mean_annual_hypo_kz_80years_rcp26=glue_df_mean_annual_hypo_kz_rcp26[glue_df_mean_annual_hypo_kz_rcp26.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_mean_annual_hypo_kz_80years_rcp26['50%'])

(0.06909550775243613,
 'positively autocorrelated',
 'no trend',
 0.16651081537512114,
 0,
 0)



glue_df_max_annual_hypo_kz_80years_rcp26=glue_df_max_annual_hypo_kz_rcp26[glue_df_max_annual_hypo_kz_rcp26.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_max_annual_hypo_kz_80years_rcp26['50%'])
(0.6258114310450531,
 'positively autocorrelated',
 'no trend',
 0.3047965594350388,
 0,
 0)



glue_df_q1_annual_hypo_kz_80years_rcp26=glue_df_q1_annual_hypo_kz_rcp26[glue_df_q1_annual_hypo_kz_rcp26.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_hypo_kz_80years_rcp26['50%'])
(0.011021821257463517,
 'positively autocorrelated',
 'no trend',
 0.4221340615856821,
 0,
 0)

glue_df_q3_annual_hypo_kz_80years_rcp26=glue_df_q3_annual_hypo_kz_rcp26[glue_df_q3_annual_hypo_kz_rcp26.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_hypo_kz_80years_rcp26['50%'])
(0.05658991227752683,
 'positively autocorrelated',
 'no trend',
 0.638728826191882,
 0,
 0)

# q1 and q3 of the kz profile in each year 

glue_df_q1_annual_prof_kz_80years_rcp26=glue_df_q1_annual_prof_kz_rcp26[glue_df_q1_annual_prof_kz_rcp26.index>2019] 

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_prof_kz_80years_rcp26['50%'])

(0.014467447120444985,
 'positively autocorrelated',
 'no trend',
 0.674762414945552,
 0,
 0)



glue_df_q3_annual_prof_kz_80years_rcp26=glue_df_q3_annual_prof_kz_rcp26[glue_df_q3_annual_prof_kz_rcp26.index>2019] 

autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_prof_kz_80years_rcp26['50%'])

(0.050860255675347944,
 'positively autocorrelated',
 'no trend',
 0.4274629703032451,
 0,
 0)


#############80 years _rcp60


glue_df_kz_mean_surf_80years_rcp60=glue_df_kz_mean_surf_rcp60[glue_df_kz_mean_surf_rcp60.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_80years_rcp60['50%'])
(0.04798423901787456,
 'positively autocorrelated',
 'no trend',
 0.9195845047358031,
 0,
 0)



#*********
glue_df_kz_max_surf_80years_rcp60=glue_df_kz_max_surf_rcp60[glue_df_kz_max_surf_rcp60.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_max_surf_80years_rcp60['50%'])
(0.2622936110272661,
 'positively autocorrelated',
 'increasing',
 0.045405532148872885,
 1.0001330980123706e-07,
 3.100446521437013e-05)


glue_df_kz_max_surf_80years_rcp60['50%'].min()
#1.3912438589613886e-05
glue_df_kz_max_surf_80years_rcp60['50%'].mean()
#3.827962044624639e-05




glue_df_kz_q1_surf_80years_rcp60=glue_df_kz_q1_surf_rcp60[glue_df_kz_q1_surf_rcp60.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q1_surf_80years_rcp60['50%'])
(0.01440987718313781,
 'positively autocorrelated',
 'no trend',
 0.5833425147709617,
 0,
 0)




glue_df_kz_q3_surf_80years_rcp60=glue_df_kz_q1_surf_rcp60[glue_df_kz_q3_surf_rcp60.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q3_surf_80years_rcp60['50%'])
(0.01440987718313781,
 'positively autocorrelated',
 'no trend',
 0.5833425147709617,
 0,
 0)



glue_df_mean_annual_hypo_kz_80years_rcp60=glue_df_mean_annual_hypo_kz_rcp60[glue_df_mean_annual_hypo_kz_rcp60.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_mean_annual_hypo_kz_80years_rcp60['50%'])
(0.05352944109919666,
 'positively autocorrelated',
 'no trend',
 0.9610612651640871,
 0,
 0)




glue_df_max_annual_hypo_kz_80years_rcp60=glue_df_max_annual_hypo_kz_rcp60[glue_df_max_annual_hypo_kz_rcp60.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_max_annual_hypo_kz_80years_rcp60['50%'])
(0.2862374598717925,
 'positively autocorrelated',
 'no trend',
 0.1252585021417334,
 0,
 0)





glue_df_q1_annual_hypo_kz_80years_rcp60=glue_df_q1_annual_hypo_kz_rcp60[glue_df_q1_annual_hypo_kz_rcp60.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_hypo_kz_80years_rcp60['50%'])
(0.013864718278684582,
 'positively autocorrelated',
 'no trend',
 0.40921450763249334,
 0,
 0)




glue_df_q3_annual_hypo_kz_80years_rcp60=glue_df_q3_annual_hypo_kz_rcp60[glue_df_q3_annual_hypo_kz_rcp60.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_hypo_kz_80years_rcp60['50%'])
(0.058773269486418006,
 'positively autocorrelated',
 'no trend',
 0.10414311548706134,
 0,
 0)





glue_df_q1_annual_prof_kz_80years_rcp60=glue_df_q1_annual_prof_kz_rcp60[glue_df_q1_annual_prof_kz_rcp60.index>2019] 

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_prof_kz_80years_rcp60['50%'])
(0.014187225441608546,
 'positively autocorrelated',
 'no trend',
 0.14912264429616284,
 0,
 0)





glue_df_q3_annual_prof_kz_80years_rcp60=glue_df_q3_annual_prof_kz_rcp60[glue_df_q3_annual_prof_kz_rcp60.index>2019] 

autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_prof_kz_80years_rcp60['50%'])
(0.043573841487048404,
 'positively autocorrelated',
 'no trend',
 0.3456254757274817,
 0,
 0)



######80 years-RCP85

glue_df_kz_mean_surf_80years_rcp85=glue_df_kz_mean_surf_rcp85[glue_df_kz_mean_surf_rcp85.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_mean_surf_80years_rcp85['50%'])
(0.045482080388108095,
 'positively autocorrelated',
 'no trend',
 0.3347506318028546,
 0,
 0)




glue_df_kz_max_surf_80years_rcp85=glue_df_kz_max_surf_rcp85[glue_df_kz_max_surf_rcp85.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_max_surf_80years_rcp85['50%'])
(0.3758280269466802,
 'positively autocorrelated',
 'no trend',
 0.07216870671884457,
 0,
 0)



glue_df_kz_q1_surf_80years_rcp85=glue_df_kz_q1_surf_rcp85[glue_df_kz_q1_surf_rcp85.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q1_surf_80years_rcp85['50%'])
(0.013596377741936675,
 'positively autocorrelated',
 'no trend',
 0.10641222407128836,
 0,
 0)




glue_df_kz_q3_surf_80years_rcp85=glue_df_kz_q1_surf_rcp85[glue_df_kz_q3_surf_rcp85.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_df_kz_q3_surf_80years_rcp85['50%'])
(0.013596377741936675,
 'positively autocorrelated',
 'no trend',
 0.10641222407128836,
 0,
 0)



glue_df_mean_annual_hypo_kz_80years_rcp85=glue_df_mean_annual_hypo_kz_rcp85[glue_df_mean_annual_hypo_kz_rcp85.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_mean_annual_hypo_kz_80years_rcp85['50%'])

(0.05550847936372615,
 'positively autocorrelated',
 'no trend',
 0.5195931535545983,
 0,
 0)



glue_df_max_annual_hypo_kz_80years_rcp85=glue_df_max_annual_hypo_kz_rcp85[glue_df_max_annual_hypo_kz_rcp85.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_max_annual_hypo_kz_80years_rcp85['50%'])
(0.5495305256273352,
 'positively autocorrelated',
 'no trend',
 0.056354342864081364,
 0,
 0)




#***************
glue_df_q1_annual_hypo_kz_80years_rcp85=glue_df_q1_annual_hypo_kz_rcp85[glue_df_q1_annual_hypo_kz_rcp85.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_hypo_kz_80years_rcp85['50%'])
(0.014032793561696764,
 'positively autocorrelated',
 'increasing',
 0.011253012472052903,
 3.3559938334056238e-09,
 7.1348006270213415e-06)
glue_df_q1_annual_hypo_kz_80years_rcp85['50%'].min()
#6.071884229123979e-06
glue_df_q1_annual_hypo_kz_80years_rcp85['50%'].mean()
#7.204498539129504e-06


glue_df_q3_annual_hypo_kz_80years_rcp85=glue_df_q3_annual_hypo_kz_rcp85[glue_df_q3_annual_hypo_kz_rcp85.index>2019] 
autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_hypo_kz_80years_rcp85['50%'])
(0.05736808977340656,
 'positively autocorrelated',
 'no trend',
 0.6626629329022817,
 0,
 0)





glue_df_q1_annual_prof_kz_80years_rcp85=glue_df_q1_annual_prof_kz_rcp85[glue_df_q1_annual_prof_kz_rcp85.index>2019] 

autocorr_MK_org_modif_sens_slope_test(glue_df_q1_annual_prof_kz_80years_rcp85['50%'])
(0.015080320314727683,
 'positively autocorrelated',
 'no trend',
 0.27453598621584985,
 0,
 0)





glue_df_q3_annual_prof_kz_80years_rcp85=glue_df_q3_annual_prof_kz_rcp85[glue_df_q3_annual_prof_kz_rcp85.index>2019] 

autocorr_MK_org_modif_sens_slope_test(glue_df_q3_annual_prof_kz_80years_rcp85['50%'])
(0.036655815608387626,
 'positively autocorrelated',
 'no trend',
 0.28162090787268923,
 0,
 0)




#%%###################Ploting the Kz values 

#KZ GLUE plotting:


import matplotlib.pyplot as plt


fig = plt.figure(figsize=(15,  10))
ax = plt.subplot(111)

# Set y-axis to log scale
ax.set_yscale('log')
# Set the y-axis range

# Specify the y-axis tick values
#y_ticks = [0.5*10**-5, 10**-5, 2*10**-5, 3*10**-5, 4*10**-5 , 5*10**-5, 6*10**-5]  # Replace with your actual values

# Set the y-axis ticks
#ax.set_yticks(y_ticks)

# Set the y-axis range (replace with your desired values)
#ax.set_ylim([0.5*10**-5, 5*10**-5])

ax.set_ylim([0.5*10**-5, 10**-4])

# Your existing plotting code remains unchanged
ax = plt.fill_between(glue_df_mean_annual_hypo_kz_80years_rcp26.index, glue_df_mean_annual_hypo_kz_80years_rcp26['5%'], glue_df_mean_annual_hypo_kz_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6  90% CI')
ax = plt.plot(glue_df_mean_annual_hypo_kz_80years_rcp26.index, glue_df_mean_annual_hypo_kz_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
ax=plt.fill_between(glue_df_mean_annual_hypo_kz_80years_rcp60.index, glue_df_mean_annual_hypo_kz_80years_rcp60['5%'], glue_df_mean_annual_hypo_kz_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_mean_annual_hypo_kz_80years_rcp60.index, glue_df_mean_annual_hypo_kz_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )

ax=plt.fill_between(glue_df_mean_annual_hypo_kz_80years_rcp85.index, glue_df_mean_annual_hypo_kz_80years_rcp85['5%'], glue_df_mean_annual_hypo_kz_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_mean_annual_hypo_kz_80years_rcp85.index, glue_df_mean_annual_hypo_kz_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )



ax = plt.ylabel('Hypolimnetic K$_z$ [m$^{2}$ s$^{-1}$]' , fontsize=26)
ax = plt.xlabel('Year' , fontsize=26)
ax = plt.yticks(fontsize=22)
ax = plt.xticks(rotation=45 , fontsize=22)
ax = plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22, ncol=3)  

fig.savefig("GLUE_Timeseries_kz_ave_hypo_annual _80years.png", dpi=300, bbox_inches='tight')





#%%#1.kz_mean_surf_4models:

    
#kz_mean_surf_4models_his, kz_mean_surf_4models_rcp26, kz_mean_surf_4models_rcp60 , kz_mean_surf_4models_rcp85




os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(kz_mean_surf_4models_his)    
plt.plot(kz_mean_surf_4models_rcp26)    
plt.plot(kz_mean_surf_4models_rcp60)
plt.plot(kz_mean_surf_4models_rcp85)
"""

# Plot mean data

plt.figure(figsize=(15, 12))  


plt.plot(kz_mean_surf_4models_his[1975 <kz_mean_surf_4models_his.index], label='His', color='grey')
plt.plot(kz_mean_surf_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(kz_mean_surf_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(kz_mean_surf_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(kz_mean_surf_4models_his.index, kz_mean_surf_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, kz_mean_surf_4models_his.index)
plt.plot(kz_mean_surf_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(kz_mean_surf_4models_his[1975 <kz_mean_surf_4models_his.index].index, kz_mean_surf_4models_his[1975 <kz_mean_surf_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, kz_mean_surf_4models_his[1975 <kz_mean_surf_4models_his.index].index)
plt.plot(kz_mean_surf_4models_his[1975 <kz_mean_surf_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2042, 0.65*10**-5, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(kz_mean_surf_4models_rcp26.index, kz_mean_surf_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, kz_mean_surf_4models_rcp26.index)
plt.plot(kz_mean_surf_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2042, 0.625*10**-5, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(kz_mean_surf_4models_rcp60.index, kz_mean_surf_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, kz_mean_surf_4models_rcp60.index)
plt.plot(kz_mean_surf_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2042, 0.6*10**-5, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(kz_mean_surf_4models_rcp85.index, kz_mean_surf_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, kz_mean_surf_4models_rcp85.index)
plt.plot(kz_mean_surf_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2042, 0.575*10**-5, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937


# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(5*10**-6), np.log10(1.5*10**-5))#, num=2)
#np.arange(10**-6, 2*10**-5 , 2*10**-6)
plt.yticks(y_ticks  )
plt.yscale('log')
plt.ylabel('Mean Kz in first hypolimnion during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_mean_deoxygenation_Kz_surfhypo_trendline_last30hist.png", dpi=300)



#%%#2.kz_max_surf_4models:

    
#kz_max_surf_4models_his, kz_max_surf_4models_rcp26, kz_max_surf_4models_rcp60 , kz_max_surf_4models_rcp85




os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(kz_max_surf_4models_his)    
plt.plot(kz_max_surf_4models_rcp26)    
plt.plot(kz_max_surf_4models_rcp60)
plt.plot(kz_max_surf_4models_rcp85)
"""

# Plot max data

plt.figure(figsize=(15, 12))  


plt.plot(kz_max_surf_4models_his[1975 <kz_max_surf_4models_his.index], label='His', color='grey')
plt.plot(kz_max_surf_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(kz_max_surf_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(kz_max_surf_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(kz_max_surf_4models_his.index, kz_max_surf_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, kz_max_surf_4models_his.index)
plt.plot(kz_max_surf_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(kz_max_surf_4models_his[1975 <kz_max_surf_4models_his.index].index, kz_max_surf_4models_his[1975 <kz_max_surf_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, kz_max_surf_4models_his[1975 <kz_max_surf_4models_his.index].index)
plt.plot(kz_max_surf_4models_his[1975 <kz_max_surf_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 0.6*10**-3, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(kz_max_surf_4models_rcp26.index, kz_max_surf_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, kz_max_surf_4models_rcp26.index)
plt.plot(kz_max_surf_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 0.5*10**-3, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(kz_max_surf_4models_rcp60.index, kz_max_surf_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, kz_max_surf_4models_rcp60.index)
plt.plot(kz_max_surf_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 0.4*10**-3, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(kz_max_surf_4models_rcp85.index, kz_max_surf_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, kz_max_surf_4models_rcp85.index)
plt.plot(kz_max_surf_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 0.3*10**-3, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937

plt.yscale('log')
# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(-5, -3, num=9)
plt.yticks(y_ticks  )

plt.ylabel('Maximum Kz in first hypolimnion during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='upper right')

plt.savefig("allsenarios_max_deoxygenation_Kz_surfhypo_trendline_last30hist.png", dpi=300)



#%%#3.kz_q1_surf_4models:

    
#kz_q1_surf_4models_his, kz_q1_surf_4models_rcp26, kz_q1_surf_4models_rcp60 , kz_q1_surf_4models_rcp85




os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(kz_q1_surf_4models_his)    
plt.plot(kz_q1_surf_4models_rcp26)    
plt.plot(kz_q1_surf_4models_rcp60)
plt.plot(kz_q1_surf_4models_rcp85)
"""

# Plot q1 data

plt.figure(figsize=(15, 12))  


plt.plot(kz_q1_surf_4models_his[1975 <kz_q1_surf_4models_his.index], label='His', color='grey')
plt.plot(kz_q1_surf_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(kz_q1_surf_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(kz_q1_surf_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(kz_q1_surf_4models_his.index, kz_q1_surf_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, kz_q1_surf_4models_his.index)
plt.plot(kz_q1_surf_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(kz_q1_surf_4models_his[1975 <kz_q1_surf_4models_his.index].index, kz_q1_surf_4models_his[1975 <kz_q1_surf_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, kz_q1_surf_4models_his[1975 <kz_q1_surf_4models_his.index].index)
plt.plot(kz_q1_surf_4models_his[1975 <kz_q1_surf_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 0.8*10**-5, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(kz_q1_surf_4models_rcp26.index, kz_q1_surf_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, kz_q1_surf_4models_rcp26.index)
plt.plot(kz_q1_surf_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 0.775*10**-5, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(kz_q1_surf_4models_rcp60.index, kz_q1_surf_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, kz_q1_surf_4models_rcp60.index)
plt.plot(kz_q1_surf_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 0.750*10**-5, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(kz_q1_surf_4models_rcp85.index, kz_q1_surf_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, kz_q1_surf_4models_rcp85.index)
plt.plot(kz_q1_surf_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 0.725*10**-5, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937
plt.yscale('log')
# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(3*10**-6) , np.log10(10**-5), num=3)
plt.yticks(y_ticks  )




plt.ylabel('1st quartile Kz in first hypolimnion during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='upper right')

plt.savefig("allsenarios_q1_deoxygenation_Kz_surfhypo_trendline_last30hist.png", dpi=300)


#%%#4.kz_q3_surf_4models:

    
#kz_q3_surf_4models_his, kz_q3_surf_4models_rcp26, kz_q3_surf_4models_rcp60 , kz_q3_surf_4models_rcp85




os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(kz_q3_surf_4models_his)    
plt.plot(kz_q3_surf_4models_rcp26)    
plt.plot(kz_q3_surf_4models_rcp60)
plt.plot(kz_q3_surf_4models_rcp85)
"""

# Plot q3 data

plt.figure(figsize=(15, 12))  


plt.plot(kz_q3_surf_4models_his[1975 <kz_q3_surf_4models_his.index], label='His', color='grey')
plt.plot(kz_q3_surf_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(kz_q3_surf_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(kz_q3_surf_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(kz_q3_surf_4models_his.index, kz_q3_surf_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, kz_q3_surf_4models_his.index)
plt.plot(kz_q3_surf_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(kz_q3_surf_4models_his[1975 <kz_q3_surf_4models_his.index].index, kz_q3_surf_4models_his[1975 <kz_q3_surf_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, kz_q3_surf_4models_his[1975 <kz_q3_surf_4models_his.index].index)
plt.plot(kz_q3_surf_4models_his[1975 <kz_q3_surf_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 0.6*10**-5, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(kz_q3_surf_4models_rcp26.index, kz_q3_surf_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, kz_q3_surf_4models_rcp26.index)
plt.plot(kz_q3_surf_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 0.575*10**-5, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(kz_q3_surf_4models_rcp60.index, kz_q3_surf_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, kz_q3_surf_4models_rcp60.index)
plt.plot(kz_q3_surf_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 0.550*10**-5, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(kz_q3_surf_4models_rcp85.index, kz_q3_surf_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, kz_q3_surf_4models_rcp85.index)
plt.plot(kz_q3_surf_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 0.525*10**-5, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937

plt.yscale('log')
# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(0.5*10**-5) , np.log10(2*10**-5), num=3)
plt.yticks(y_ticks  )



plt.ylabel('3rd quartile Kz in first hypolimnion during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='upper right')

plt.savefig("allsenarios_q3_deoxygenation_Kz_surfhypo_trendline_last30hist.png", dpi=300)



#%%#5.kz_mean_hypo_ave_prof_4models:

    
#mean_annual_hypo_kz_daily_4models_his, mean_annual_hypo_kz_daily_4models_rcp26, mean_annual_hypo_kz_daily_4models_rcp60 , mean_annual_hypo_kz_daily_4models_rcp85


os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(mean_annual_hypo_kz_daily_4models_his)    
plt.plot(mean_annual_hypo_kz_daily_4models_rcp26)    
plt.plot(mean_annual_hypo_kz_daily_4models_rcp60)
plt.plot(mean_annual_hypo_kz_daily_4models_rcp85)
"""

# Plot mean data

plt.figure(figsize=(15, 12))  


plt.plot(mean_annual_hypo_kz_daily_4models_his[1975 <mean_annual_hypo_kz_daily_4models_his.index], label='His', color='grey')
plt.plot(mean_annual_hypo_kz_daily_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(mean_annual_hypo_kz_daily_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(mean_annual_hypo_kz_daily_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(mean_annual_hypo_kz_daily_4models_his.index, mean_annual_hypo_kz_daily_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, mean_annual_hypo_kz_daily_4models_his.index)
plt.plot(mean_annual_hypo_kz_daily_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(mean_annual_hypo_kz_daily_4models_his[1975 <mean_annual_hypo_kz_daily_4models_his.index].index, mean_annual_hypo_kz_daily_4models_his[1975 <mean_annual_hypo_kz_daily_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, mean_annual_hypo_kz_daily_4models_his[1975 <mean_annual_hypo_kz_daily_4models_his.index].index)
plt.plot(mean_annual_hypo_kz_daily_4models_his[1975 <mean_annual_hypo_kz_daily_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2042, 1*10**-5, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(mean_annual_hypo_kz_daily_4models_rcp26.index, mean_annual_hypo_kz_daily_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, mean_annual_hypo_kz_daily_4models_rcp26.index)
plt.plot(mean_annual_hypo_kz_daily_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2042, 0.97*10**-5, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(mean_annual_hypo_kz_daily_4models_rcp60.index, mean_annual_hypo_kz_daily_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, mean_annual_hypo_kz_daily_4models_rcp60.index)
plt.plot(mean_annual_hypo_kz_daily_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2042, 0.94*10**-5, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(mean_annual_hypo_kz_daily_4models_rcp85.index, mean_annual_hypo_kz_daily_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, mean_annual_hypo_kz_daily_4models_rcp85.index)
plt.plot(mean_annual_hypo_kz_daily_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2042, 0.91*10**-5, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937


# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(5*10**-6), np.log10(1.5*10**-5))#, num=2)
#np.arange(10**-6, 2*10**-5 , 2*10**-6)
plt.yticks(y_ticks  )
plt.yscale('log')
plt.ylabel('Mean hypolimnetic average Kz during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_mean_hypolimnetic_Kz_prof_trendline_last30hist.png", dpi=300)


#%%#6.kz_max_hypo_ave_prof_4models:

    
#max_annual_hypo_kz_daily_4models_his, max_annual_hypo_kz_daily_4models_rcp26, max_annual_hypo_kz_daily_4models_rcp60 , max_annual_hypo_kz_daily_4models_rcp85


os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(max_annual_hypo_kz_daily_4models_his)    
plt.plot(max_annual_hypo_kz_daily_4models_rcp26)    
plt.plot(max_annual_hypo_kz_daily_4models_rcp60)
plt.plot(max_annual_hypo_kz_daily_4models_rcp85)
"""

# Plot max data

plt.figure(figsize=(15, 12))  


plt.plot(max_annual_hypo_kz_daily_4models_his[1975 <max_annual_hypo_kz_daily_4models_his.index], label='His', color='grey')
plt.plot(max_annual_hypo_kz_daily_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(max_annual_hypo_kz_daily_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(max_annual_hypo_kz_daily_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(max_annual_hypo_kz_daily_4models_his.index, max_annual_hypo_kz_daily_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, max_annual_hypo_kz_daily_4models_his.index)
plt.plot(max_annual_hypo_kz_daily_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(max_annual_hypo_kz_daily_4models_his[1975 <max_annual_hypo_kz_daily_4models_his.index].index, max_annual_hypo_kz_daily_4models_his[1975 <max_annual_hypo_kz_daily_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, max_annual_hypo_kz_daily_4models_his[1975 <max_annual_hypo_kz_daily_4models_his.index].index)
plt.plot(max_annual_hypo_kz_daily_4models_his[1975 <max_annual_hypo_kz_daily_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2042, 5*10**-4, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(max_annual_hypo_kz_daily_4models_rcp26.index, max_annual_hypo_kz_daily_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, max_annual_hypo_kz_daily_4models_rcp26.index)
plt.plot(max_annual_hypo_kz_daily_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2042, 6*10**-4, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(max_annual_hypo_kz_daily_4models_rcp60.index, max_annual_hypo_kz_daily_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, max_annual_hypo_kz_daily_4models_rcp60.index)
plt.plot(max_annual_hypo_kz_daily_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2042, 7*10**-4, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(max_annual_hypo_kz_daily_4models_rcp85.index, max_annual_hypo_kz_daily_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, max_annual_hypo_kz_daily_4models_rcp85.index)
plt.plot(max_annual_hypo_kz_daily_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2042, 8*10**-4, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937

plt.yscale('log')
# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(10**-5), np.log10(10**-3), num=5)#)
#np.arange(10**-6, 2*10**-5 , 2*10**-6)
plt.yticks(y_ticks  )

plt.ylabel('Maximum hypolimnetic average Kz during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='upper left')

plt.savefig("allsenarios_max_hypolimnetic_Kz_prof_trendline_last30hist.png", dpi=300)


#%%#7.kz_q1_hypo_ave_prof_4models:

    
#q1_annual_hypo_kz_daily_4models_his, q1_annual_hypo_kz_daily_4models_rcp26, q1_annual_hypo_kz_daily_4models_rcp60 , q1_annual_hypo_kz_daily_4models_rcp85


os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(q1_annual_hypo_kz_daily_4models_his)    
plt.plot(q1_annual_hypo_kz_daily_4models_rcp26)    
plt.plot(q1_annual_hypo_kz_daily_4models_rcp60)
plt.plot(q1_annual_hypo_kz_daily_4models_rcp85)
"""

# Plot q1 data

plt.figure(figsize=(15, 12))  


plt.plot(q1_annual_hypo_kz_daily_4models_his[1975 <q1_annual_hypo_kz_daily_4models_his.index], label='His', color='grey')
plt.plot(q1_annual_hypo_kz_daily_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(q1_annual_hypo_kz_daily_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(q1_annual_hypo_kz_daily_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(q1_annual_hypo_kz_daily_4models_his.index, q1_annual_hypo_kz_daily_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, q1_annual_hypo_kz_daily_4models_his.index)
plt.plot(q1_annual_hypo_kz_daily_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(q1_annual_hypo_kz_daily_4models_his[1975 <q1_annual_hypo_kz_daily_4models_his.index].index, q1_annual_hypo_kz_daily_4models_his[1975 <q1_annual_hypo_kz_daily_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, q1_annual_hypo_kz_daily_4models_his[1975 <q1_annual_hypo_kz_daily_4models_his.index].index)
plt.plot(q1_annual_hypo_kz_daily_4models_his[1975 <q1_annual_hypo_kz_daily_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2042, 9.25*10**-6, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(q1_annual_hypo_kz_daily_4models_rcp26.index, q1_annual_hypo_kz_daily_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, q1_annual_hypo_kz_daily_4models_rcp26.index)
plt.plot(q1_annual_hypo_kz_daily_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2042, 9*10**-6, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(q1_annual_hypo_kz_daily_4models_rcp60.index, q1_annual_hypo_kz_daily_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, q1_annual_hypo_kz_daily_4models_rcp60.index)
plt.plot(q1_annual_hypo_kz_daily_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2042, 8.75*10**-6, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(q1_annual_hypo_kz_daily_4models_rcp85.index, q1_annual_hypo_kz_daily_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, q1_annual_hypo_kz_daily_4models_rcp85.index)
plt.plot(q1_annual_hypo_kz_daily_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2042, 8.5*10**-6, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937

# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(5*10**-6), np.log10(10**-5), num=5)#)
#np.arange(10**-6, 2*10**-5 , 2*10**-6)
plt.yticks(y_ticks  )

plt.yscale('log')
plt.ylabel('1st quartile hypolimnetic average Kz during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_q1_hypolimnetic_Kz_prof_trendline_last30hist.png", dpi=300)



#%%#8.kz_q3_hypo_ave_prof_4models:

    
#q3_annual_hypo_kz_daily_4models_his, q3_annual_hypo_kz_daily_4models_rcp26, q3_annual_hypo_kz_daily_4models_rcp60 , q3_annual_hypo_kz_daily_4models_rcp85


os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(q3_annual_hypo_kz_daily_4models_his)    
plt.plot(q3_annual_hypo_kz_daily_4models_rcp26)    
plt.plot(q3_annual_hypo_kz_daily_4models_rcp60)
plt.plot(q3_annual_hypo_kz_daily_4models_rcp85)
"""

# Plot q3 data

plt.figure(figsize=(15, 12))  


plt.plot(q3_annual_hypo_kz_daily_4models_his[1975 <q3_annual_hypo_kz_daily_4models_his.index], label='His', color='grey')
plt.plot(q3_annual_hypo_kz_daily_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(q3_annual_hypo_kz_daily_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(q3_annual_hypo_kz_daily_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(q3_annual_hypo_kz_daily_4models_his.index, q3_annual_hypo_kz_daily_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, q3_annual_hypo_kz_daily_4models_his.index)
plt.plot(q3_annual_hypo_kz_daily_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(q3_annual_hypo_kz_daily_4models_his[1975 <q3_annual_hypo_kz_daily_4models_his.index].index, q3_annual_hypo_kz_daily_4models_his[1975 <q3_annual_hypo_kz_daily_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, q3_annual_hypo_kz_daily_4models_his[1975 <q3_annual_hypo_kz_daily_4models_his.index].index)
plt.plot(q3_annual_hypo_kz_daily_4models_his[1975 <q3_annual_hypo_kz_daily_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2042, 2.55*10**-5, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(q3_annual_hypo_kz_daily_4models_rcp26.index, q3_annual_hypo_kz_daily_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, q3_annual_hypo_kz_daily_4models_rcp26.index)
plt.plot(q3_annual_hypo_kz_daily_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2042, 2.45*10**-5, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(q3_annual_hypo_kz_daily_4models_rcp60.index, q3_annual_hypo_kz_daily_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, q3_annual_hypo_kz_daily_4models_rcp60.index)
plt.plot(q3_annual_hypo_kz_daily_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2042, 2.35*10**-5, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(q3_annual_hypo_kz_daily_4models_rcp85.index, q3_annual_hypo_kz_daily_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, q3_annual_hypo_kz_daily_4models_rcp85.index)
plt.plot(q3_annual_hypo_kz_daily_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2042, 2.25*10**-5, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937

plt.yscale('log')
# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(10**-5), np.log10(3*10**-5), num=2)#)
#np.arange(10**-6, 2*10**-5 , 2*10**-6)
plt.yticks(y_ticks  )

plt.ylabel('3rd quartile hypolimnetic average Kz during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='upper left')

plt.savefig("allsenarios_q3_hypolimnetic_Kz_prof_trendline_last30hist.png", dpi=300)

#%%.kz_q1_hypo_prof_4models:


#q1_annual_prof_kz_daily_4models_his, q1_annual_prof_kz_daily_4models_rcp26, q1_annual_prof_kz_daily_4models_rcp60 , q1_annual_prof_kz_daily_4models_rcp85


os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(q1_annual_prof_kz_daily_4models_his)    
plt.plot(q1_annual_prof_kz_daily_4models_rcp26)    
plt.plot(q1_annual_prof_kz_daily_4models_rcp60)
plt.plot(q1_annual_prof_kz_daily_4models_rcp85)
"""

# Plot q1 data

plt.figure(figsize=(17, 12))  


plt.plot(q1_annual_prof_kz_daily_4models_his[1975 <q1_annual_prof_kz_daily_4models_his.index], label='His', color='grey')
plt.plot(q1_annual_prof_kz_daily_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(q1_annual_prof_kz_daily_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(q1_annual_prof_kz_daily_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(q1_annual_prof_kz_daily_4models_his.index, q1_annual_prof_kz_daily_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, q1_annual_prof_kz_daily_4models_his.index)
plt.plot(q1_annual_prof_kz_daily_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(q1_annual_prof_kz_daily_4models_his[1975 <q1_annual_prof_kz_daily_4models_his.index].index, q1_annual_prof_kz_daily_4models_his[1975 <q1_annual_prof_kz_daily_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, q1_annual_prof_kz_daily_4models_his[1975 <q1_annual_prof_kz_daily_4models_his.index].index)
plt.plot(q1_annual_prof_kz_daily_4models_his[1975 <q1_annual_prof_kz_daily_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2042, 7.25*10**-6, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(q1_annual_prof_kz_daily_4models_rcp26.index, q1_annual_prof_kz_daily_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, q1_annual_prof_kz_daily_4models_rcp26.index)
plt.plot(q1_annual_prof_kz_daily_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2042, 7*10**-6, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(q1_annual_prof_kz_daily_4models_rcp60.index, q1_annual_prof_kz_daily_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, q1_annual_prof_kz_daily_4models_rcp60.index)
plt.plot(q1_annual_prof_kz_daily_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2042, 6.75*10**-6, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(q1_annual_prof_kz_daily_4models_rcp85.index, q1_annual_prof_kz_daily_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, q1_annual_prof_kz_daily_4models_rcp85.index)
plt.plot(q1_annual_prof_kz_daily_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2042,6.5*10**-6, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937

plt.yscale('log')
# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(0.6*10**-5), np.log10(1.2*10**-5), num=2)#)
#np.arange(10**-6, 2*10**-5 , 2*10**-6)
plt.yticks(y_ticks  )

plt.ylabel('1st quartile hypolimnetic Kz profile during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_q1_Kz_prof_trendline_last30hist.png", dpi=300)




#%%#10.kz_q3_hypo_prof_4models:

    
#q3_annual_prof_kz_daily_4models_his, q3_annual_prof_kz_daily_4models_rcp26, q3_annual_prof_kz_daily_4models_rcp60 , q3_annual_prof_kz_daily_4models_rcp85


os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
plt.plot(q3_annual_prof_kz_daily_4models_his)    
plt.plot(q3_annual_prof_kz_daily_4models_rcp26)    
plt.plot(q3_annual_prof_kz_daily_4models_rcp60)
plt.plot(q3_annual_prof_kz_daily_4models_rcp85)
"""

# Plot q3 data

plt.figure(figsize=(17, 12))  


plt.plot(q3_annual_prof_kz_daily_4models_his[1975 <q3_annual_prof_kz_daily_4models_his.index], label='His', color='grey')
plt.plot(q3_annual_prof_kz_daily_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(q3_annual_prof_kz_daily_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(q3_annual_prof_kz_daily_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(q3_annual_prof_kz_daily_4models_his.index, q3_annual_prof_kz_daily_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, q3_annual_prof_kz_daily_4models_his.index)
plt.plot(q3_annual_prof_kz_daily_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(q3_annual_prof_kz_daily_4models_his[1975 <q3_annual_prof_kz_daily_4models_his.index].index, q3_annual_prof_kz_daily_4models_his[1975 <q3_annual_prof_kz_daily_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, q3_annual_prof_kz_daily_4models_his[1975 <q3_annual_prof_kz_daily_4models_his.index].index)
plt.plot(q3_annual_prof_kz_daily_4models_his[1975 <q3_annual_prof_kz_daily_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2042, 1.75*10**-5, f'y = {trendline_his[0]}x ', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(q3_annual_prof_kz_daily_4models_rcp26.index, q3_annual_prof_kz_daily_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, q3_annual_prof_kz_daily_4models_rcp26.index)
plt.plot(q3_annual_prof_kz_daily_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2042, 1.85*10**-5, f'y = {trendline_rcp26[0]}x ', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(q3_annual_prof_kz_daily_4models_rcp60.index, q3_annual_prof_kz_daily_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, q3_annual_prof_kz_daily_4models_rcp60.index)
plt.plot(q3_annual_prof_kz_daily_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2042, 1.95*10**-5, f'y = {trendline_rcp60[0]}x ', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(q3_annual_prof_kz_daily_4models_rcp85.index, q3_annual_prof_kz_daily_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, q3_annual_prof_kz_daily_4models_rcp85.index)
plt.plot(q3_annual_prof_kz_daily_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2042, 2.05*10**-5, f'y = {trendline_rcp85[0]}x ', color='r')
trendline_rcp85[0]
#-0.22818336162987937

plt.yscale('log')
# Set the y-axis limits with an interval of 25
y_ticks = np.logspace(np.log10(1.5*10**-5), np.log10(3*10**-5), num=2)#)
#np.arange(10**-6, 2*10**-5 , 2*10**-6)
plt.yticks(y_ticks  )

plt.ylabel('3rd quartile hypolimnetic Kz profile during deoxygenation [m$^{2}$ s$^{-1}$]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_q3_Kz_prof_trendline_last30hist.png", dpi=300)






#%%
"""
['start_dates_Jday']
"""
def start_dates_Jday (df_deox):
    start_jday=df_deox.groupby('year').min()['start_dates_Jday']
    return (start_jday)


#%%his 

onset_jday_gfdl_his=start_dates_Jday(df_deox_period_surf_gfdl_his)
onset_jday_hadgem_his=start_dates_Jday(df_deox_period_surf_hadgem_his)
onset_jday_ipsl_his=start_dates_Jday(df_deox_period_surf_ipsl_his)
onset_jday_miroc_his=start_dates_Jday(df_deox_period_surf_miroc_his)


onset_jday_allgcms_his=pd.concat([onset_jday_gfdl_his, onset_jday_hadgem_his, onset_jday_ipsl_his , onset_jday_miroc_his], axis=0)


onset_jday_4models_his=(onset_jday_gfdl_his+ onset_jday_hadgem_his+ onset_jday_ipsl_his+ onset_jday_miroc_his)/4

all_onset_jday_4models_his=pd.concat([onset_jday_gfdl_his, onset_jday_hadgem_his, onset_jday_ipsl_his, onset_jday_miroc_his], axis=1)

#glue_df_onset_jday_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_onset_jday_4models_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_onset_jday_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_onset_jday_his= glue_df_onset_jday_his.set_index(all_onset_jday_4models_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_onset_jday_his.csv'

glue_df_onset_jday_his.to_csv(file_path )
#%%rcp26 

onset_jday_gfdl_rcp26=start_dates_Jday(df_deox_period_surf_gfdl_rcp26)
onset_jday_hadgem_rcp26=start_dates_Jday(df_deox_period_surf_hadgem_rcp26)
onset_jday_ipsl_rcp26=start_dates_Jday(df_deox_period_surf_ipsl_rcp26)
onset_jday_miroc_rcp26=start_dates_Jday(df_deox_period_surf_miroc_rcp26)


onset_jday_allgcms_rcp26=pd.concat([onset_jday_gfdl_rcp26, onset_jday_hadgem_rcp26, onset_jday_ipsl_rcp26 , onset_jday_miroc_rcp26], axis=0)

onset_jday_4models_rcp26=(onset_jday_gfdl_rcp26+ onset_jday_hadgem_rcp26+ onset_jday_ipsl_rcp26+ onset_jday_miroc_rcp26)/4

all_onset_jday_4models_rcp26=pd.concat([onset_jday_gfdl_rcp26, onset_jday_hadgem_rcp26, onset_jday_ipsl_rcp26, onset_jday_miroc_rcp26], axis=1)

#glue_df_onset_jday_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_onset_jday_4models_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_onset_jday_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_onset_jday_rcp26= glue_df_onset_jday_rcp26.set_index(all_onset_jday_4models_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_onset_jday_rcp26.csv'

glue_df_onset_jday_rcp26.to_csv(file_path )
#%%rcp60 

onset_jday_gfdl_rcp60=start_dates_Jday(df_deox_period_surf_gfdl_rcp60)
onset_jday_hadgem_rcp60=start_dates_Jday(df_deox_period_surf_hadgem_rcp60)
onset_jday_ipsl_rcp60=start_dates_Jday(df_deox_period_surf_ipsl_rcp60)
onset_jday_miroc_rcp60=start_dates_Jday(df_deox_period_surf_miroc_rcp60)


onset_jday_allgcms_rcp60=pd.concat([onset_jday_gfdl_rcp60, onset_jday_hadgem_rcp60, onset_jday_ipsl_rcp60 , onset_jday_miroc_rcp60], axis=0)


onset_jday_4models_rcp60=(onset_jday_gfdl_rcp60+ onset_jday_hadgem_rcp60+ onset_jday_ipsl_rcp60+ onset_jday_miroc_rcp60)/4

all_onset_jday_4models_rcp60=pd.concat([onset_jday_gfdl_rcp60, onset_jday_hadgem_rcp60, onset_jday_ipsl_rcp60, onset_jday_miroc_rcp60], axis=1)

#glue_df_onset_jday_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_onset_jday_4models_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_onset_jday_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_onset_jday_rcp60= glue_df_onset_jday_rcp60.set_index(all_onset_jday_4models_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_onset_jday_rcp60.csv'

glue_df_onset_jday_rcp60.to_csv(file_path )


#%%rcp85 

onset_jday_gfdl_rcp85=start_dates_Jday(df_deox_period_surf_gfdl_rcp85)
onset_jday_hadgem_rcp85=start_dates_Jday(df_deox_period_surf_hadgem_rcp85)
onset_jday_ipsl_rcp85=start_dates_Jday(df_deox_period_surf_ipsl_rcp85)
onset_jday_miroc_rcp85=start_dates_Jday(df_deox_period_surf_miroc_rcp85)

onset_jday_allgcms_rcp85=pd.concat([onset_jday_gfdl_rcp85, onset_jday_hadgem_rcp85, onset_jday_ipsl_rcp85 , onset_jday_miroc_rcp85], axis=0)

onset_jday_4models_rcp85=(onset_jday_gfdl_rcp85+ onset_jday_hadgem_rcp85+ onset_jday_ipsl_rcp85+ onset_jday_miroc_rcp85)/4

all_onset_jday_4models_rcp85=pd.concat([onset_jday_gfdl_rcp85, onset_jday_hadgem_rcp85, onset_jday_ipsl_rcp85, onset_jday_miroc_rcp85], axis=1)

#glue_df_onset_jday_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_onset_jday_4models_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_onset_jday_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_onset_jday_rcp85= glue_df_onset_jday_rcp85.set_index(all_onset_jday_4models_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_onset_jday_rcp85.csv'

glue_df_onset_jday_rcp85.to_csv(file_path )


#%%onset minimum of all models 

onset_jday_gfdl_his.min()#112
onset_jday_hadgem_his.min()#106
onset_jday_ipsl_his.min()#107
onset_jday_miroc_his.min()#112



onset_jday_gfdl_rcp26.min()#107
onset_jday_hadgem_rcp26.min()#101
onset_jday_ipsl_rcp26.min()#100
onset_jday_miroc_rcp26.min()#102


onset_jday_gfdl_rcp60.min()#93
onset_jday_hadgem_rcp60.min()#93
onset_jday_ipsl_rcp60.min()#90
onset_jday_miroc_rcp60.min()#100


onset_jday_gfdl_rcp85.min()#104
onset_jday_hadgem_rcp85.min()#88
onset_jday_ipsl_rcp85.min()#86
onset_jday_miroc_rcp85.min()#86

#We assume Minum April 90 (although the minimum is 86 )

onset_jday_gfdl_his.max()#159
onset_jday_hadgem_his.max()#179
onset_jday_ipsl_his.max()#178
onset_jday_miroc_his.max()#162



onset_jday_gfdl_rcp26.max()#153
onset_jday_hadgem_rcp26.max()#143
onset_jday_ipsl_rcp26.max()#151
onset_jday_miroc_rcp26.max()#143


onset_jday_gfdl_rcp60.max()#176
onset_jday_hadgem_rcp60.max()#148
onset_jday_ipsl_rcp60.max()#173
onset_jday_miroc_rcp60.max()#158


onset_jday_gfdl_rcp85.max()#181
onset_jday_hadgem_rcp85.max()#144
onset_jday_ipsl_rcp85.max()#152
onset_jday_miroc_rcp85.max()#170


#%% MK test on onset Jday 100 years 

glue_df_onset_jday_100years_rcp26=pd.concat([glue_df_onset_jday_his[glue_df_onset_jday_his.index>1999] , glue_df_onset_jday_rcp26])

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp26['50%'])
(0.00464906927142881,
 'positively autocorrelated',
 'decreasing',
 0.0012085965626316142,
 -0.06060606060606061,
 126.0)



glue_df_onset_jday_100years_rcp60=pd.concat([glue_df_onset_jday_his[glue_df_onset_jday_his.index>1999] , glue_df_onset_jday_rcp60])

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp60['50%'])
(0.002970558864774804,
 'positively autocorrelated',
 'decreasing',
 1.1159563428897457e-07,
 -0.13006849315068492,
 127.9383904109589)


glue_df_onset_jday_100years_rcp85=pd.concat([glue_df_onset_jday_his[glue_df_onset_jday_his.index>1999] , glue_df_onset_jday_rcp85])

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp85['50%'])
(0.0052083754406322775,
 'positively autocorrelated',
 'decreasing',
 8.881784197001252e-16,
 -0.239356884057971,
 132.34816576086956)


#%% 100 years plotiing for different senarios and their results of sens's slope and intercept 


os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for100years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_onset_jday_100years_rcp26.index, glue_df_onset_jday_100years_rcp26['5%'], glue_df_onset_jday_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_onset_jday_100years_rcp26.index, glue_df_onset_jday_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp26['50%'])
ax= plt.text(2000, 100, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f},  p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )

x_values = np.arange(len(glue_df_onset_jday_100years_rcp26.index))
y_values = trendline_rcp26[-2] * x_values + trendline_rcp26[-1]

ax = plt.plot(glue_df_onset_jday_100years_rcp26.index, y_values, label='RCP2.6 trendline', linewidth=2, linestyle='--', color='green')




ax=plt.fill_between(glue_df_onset_jday_100years_rcp60.index, glue_df_onset_jday_100years_rcp60['5%'], glue_df_onset_jday_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_onset_jday_100years_rcp60.index, glue_df_onset_jday_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp60['50%'])
ax=plt.text(2000, 96, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.0001', color='gold', fontsize= 20 )

x_values = np.arange(len(glue_df_onset_jday_100years_rcp60.index))
y_values = trendline_rcp60[-2] * x_values + trendline_rcp60[-1]

ax = plt.plot(glue_df_onset_jday_100years_rcp60.index, y_values, label='RCP6.0 trendline', linewidth=2, linestyle='--', color='gold')



ax=plt.fill_between(glue_df_onset_jday_100years_rcp85.index, glue_df_onset_jday_100years_rcp85['5%'], glue_df_onset_jday_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_onset_jday_100years_rcp85.index, glue_df_onset_jday_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp85['50%'])
ax = plt.text(2000, 92, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize=20)
x_values = np.arange(len(glue_df_onset_jday_100years_rcp85.index))
y_values = trendline_rcp85[-2] * x_values + trendline_rcp85[-1]

ax = plt.plot(glue_df_onset_jday_100years_rcp85.index, y_values, label='RCP8.5 trendline', linewidth=2, linestyle='--', color='red')


ax=plt.ylabel('Deoxygenation onset date [Jd]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(90, 180, 15) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22 , ncol=3) 


fig.savefig("GLUE_deox_onset_date_100years.png", dpi=300, bbox_inches='tight')






#%%each GCMs different rcps
################################################rcp2.6
autocorr_MK_org_modif_sens_slope_test(onset_jday_gfdl_rcp26[onset_jday_gfdl_rcp26.index>2019])
"""
(0.015038185659819086,
 'positively autocorrelated',
 'no trend',
 0.15487768295064197,
 0,
 0)
"""

autocorr_MK_org_modif_sens_slope_test(onset_jday_hadgem_rcp26[onset_jday_hadgem_rcp26.index>2019])
"""
(0.01033331105631747,
 'positively autocorrelated',
 'no trend',
 0.13118489831651825,
 0,
 0)
"""





autocorr_MK_org_modif_sens_slope_test(onset_jday_ipsl_rcp26[onset_jday_ipsl_rcp26.index>2019])

"""
(0.017462804762335624,
 'positively autocorrelated',
 'no trend',
 0.4222311822958571,
 0,
 0)
"""


autocorr_MK_org_modif_sens_slope_test(onset_jday_miroc_rcp26[onset_jday_miroc_rcp26.index>2019])
"""
(0.009616956649833397,
 'positively autocorrelated',
 'no trend',
 0.2164193099609295,
 0,
 0)
"""

#################################################rcp6.0
autocorr_MK_org_modif_sens_slope_test(onset_jday_gfdl_rcp60[onset_jday_gfdl_rcp60.index>2019])
"""
(0.014892579872274339,
 'positively autocorrelated',
 'no trend',
 0.5164255725940006,
 0,
 0)
"""




autocorr_MK_org_modif_sens_slope_test(onset_jday_hadgem_rcp60[onset_jday_hadgem_rcp60.index>2019])
"""
(0.011158186898022204,
 'positively autocorrelated',
 'decreasing',
 0.00046812680835128795,
 -0.1457513768686074,
 119.75717938630999)
"""



autocorr_MK_org_modif_sens_slope_test(onset_jday_ipsl_rcp60[onset_jday_ipsl_rcp60.index>2019])
"""
(0.01763062352144165,
 'positively autocorrelated',
 'decreasing',
 0.0010888876842876094,
 -0.15184453227931488,
 126.49785902503294)
"""



autocorr_MK_org_modif_sens_slope_test(onset_jday_miroc_rcp60[onset_jday_miroc_rcp60.index>2019])
"""
(0.013510580296942217,
 'positively autocorrelated',
 'decreasing',
 3.5792451058558328e-06,
 -0.16,
 126.32)
"""


###################################################rcp8.5
autocorr_MK_org_modif_sens_slope_test(onset_jday_gfdl_rcp85[onset_jday_gfdl_rcp85.index>2019])

"""
(0.017435165104834217,
 'positively autocorrelated',
 'decreasing',
 0.0002214682640040433,
 -0.2037357315807679,
 136.54756139744035)
"""

autocorr_MK_org_modif_sens_slope_test(onset_jday_hadgem_rcp85[onset_jday_hadgem_rcp85.index>2019])

"""
(0.013267773753931192,
 'positively autocorrelated',
 'decreasing',
 3.1165194145366115e-06,
 -0.22418519646664636,
 119.35531526043253)
"""

autocorr_MK_org_modif_sens_slope_test(onset_jday_ipsl_rcp85[onset_jday_ipsl_rcp85.index>2019])

"""
(0.024840948210122667,
 'positively autocorrelated',
 'decreasing',
 7.21921536839254e-05,
 -0.24459272894615738,
 126.66141279337322)
"""

autocorr_MK_org_modif_sens_slope_test(onset_jday_miroc_rcp85[onset_jday_miroc_rcp85.index>2019])
"""
(0.008530483192835382,
 'positively autocorrelated',
 'decreasing',
 2.597383863545133e-09,
 -0.25,
 126.875)
"""




#%% MK test on onset Jday 80 years 

glue_df_onset_jday_80years_rcp26=glue_df_onset_jday_rcp26[glue_df_onset_jday_rcp26.index>2019] 

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_80years_rcp26['50%'])
(0.00504611883085769,
 'positively autocorrelated',
 'decreasing',
 0.0016535033726348125,
 -0.05517503805175038,
 124.67941400304414)



glue_df_onset_jday_80years_rcp60=glue_df_onset_jday_rcp60[glue_df_onset_jday_rcp60.index>2019] 

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_80years_rcp60['50%'])
(0.0031168100369260714,
 'positively autocorrelated',
 'decreasing',
 5.135500913411306e-09,
 -0.14285714285714285,
 125.39285714285714)


glue_df_onset_jday_80years_rcp85=glue_df_onset_jday_rcp85[glue_df_onset_jday_rcp85.index>2019] 

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_80years_rcp85['50%'])
(0.005559937014175383,
 'positively autocorrelated',
 'decreasing',
 7.106426558323164e-11,
 -0.2613871635610766,
 128.82479296066253)


#%% 80 years plotiing for different senarios and their results of sens's slope and intercept 


os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for80years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_onset_jday_80years_rcp26.index, glue_df_onset_jday_80years_rcp26['5%'], glue_df_onset_jday_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_onset_jday_80years_rcp26.index, glue_df_onset_jday_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_80years_rcp26['50%'])
ax=plt.plot(glue_df_onset_jday_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--')
ax= plt.text(2060, 160, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )


ax=plt.fill_between(glue_df_onset_jday_80years_rcp60.index, glue_df_onset_jday_80years_rcp60['5%'], glue_df_onset_jday_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_onset_jday_80years_rcp60.index, glue_df_onset_jday_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_80years_rcp60['50%'])
ax=plt.plot(glue_df_onset_jday_80years_rcp60.index,trendline_rcp60[-2]*(np.arange(1,81))+trendline_rcp60[-1] ,color='gold',  linestyle='--')
ax=plt.text(2060, 155, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_onset_jday_80years_rcp85.index, glue_df_onset_jday_80years_rcp85['5%'], glue_df_onset_jday_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_onset_jday_80years_rcp85.index, glue_df_onset_jday_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_80years_rcp85['50%'])
ax=plt.plot(glue_df_onset_jday_80years_rcp85.index,trendline_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--')

ax = plt.text(2060, 150, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value = {trendline_rcp85[-3]:.3f}', color='r', fontsize=20)


ax=plt.ylabel('Deoxygenation onset date [Jd]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(90, 180, 15) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22) 



fig.savefig("GLUE_deox_onset_date_80years.png", dpi=300, bbox_inches='tight')




#%% graph liner showing all model and scanrios

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# only averages:
    
    
"""  
np.mean(onset_jday_4models_his[1975 <onset_jday_4models_his.index])   # 132.05# [1975 <onset_jday_4models_his.index]
np.mean(onset_jday_4models_rcp26)    #123.25
np.mean(onset_jday_4models_rcp60)#121.69
np.mean(onset_jday_4models_rcp85)#120




np.mean(offset_jday_4models_his[1975 <offset_jday_4models_his.index])   # 244.45# [1975 <offset_jday_4models_his.index]
np.mean(offset_jday_4models_rcp26)    #248.4095744680851
np.mean(offset_jday_4models_rcp60)#248.58244680851064
np.mean(offset_jday_4models_rcp85)#249.56914893617022










"""

# Plot mean data

plt.figure(figsize=(15, 10))  


#plt.plot(onset_jday_4models_his, label='His', color='grey')#marker='o',

plt.plot(onset_jday_4models_his[1975 <onset_jday_4models_his.index], label='His', color='grey')
plt.plot(onset_jday_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(onset_jday_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(onset_jday_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(onset_jday_4models_his.index, onset_jday_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, onset_jday_4models_his.index)
plt.plot(onset_jday_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(2000, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(onset_jday_4models_his[1975 <onset_jday_4models_his.index].index, onset_jday_4models_his[1975 <onset_jday_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, onset_jday_4models_his[1975 <onset_jday_4models_his.index].index)
plt.plot(onset_jday_4models_his[1975 <onset_jday_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 146, f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(onset_jday_4models_rcp26.index, onset_jday_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, onset_jday_4models_rcp26.index)
plt.plot(onset_jday_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 143, f'y = {trendline_rcp26[0]:.2f}x + {trendline_rcp26[1]:.2f}', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(onset_jday_4models_rcp60.index, onset_jday_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, onset_jday_4models_rcp60.index)
plt.plot(onset_jday_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 140, f'y = {trendline_rcp60[0]:.2f}x + {trendline_rcp60[1]:.2f}', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(onset_jday_4models_rcp85.index, onset_jday_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, onset_jday_4models_rcp85.index)
plt.plot(onset_jday_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 137, f'y = {trendline_rcp85[0]:.2f}x + {trendline_rcp85[1]:.2f}', color='r')
trendline_rcp85[0]
#-0.22818336162987937



# Set the y-axis limits with an interval of 25
y_ticks = np.arange(90, 180, 15)
plt.yticks(y_ticks)

plt.ylabel('Deoxygenation onset date [Jd]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_mean_deoxygenation_start_date_periods_trendline_last30hist.png", dpi=300)








#%%initial_cond_ave_deep-water_temp

def initial_cond_ave_temp (df_deox , temp_2D_hypo ,Vr= hypo_morpho_vriables_gotm_grid[0] ):
    initial_indices=df_deox.groupby('year').min()['initial_cond_indices']
    temp_hypo_inital_cond=temp_2D_hypo[np.array(initial_indices).astype(int) , :]
    temp_ave_inital_cond= np.dot (temp_hypo_inital_cond , Vr) / sum (Vr)        
    temp_ave_inital_cond_indexed=pd.Series(temp_ave_inital_cond, index=initial_indices.index)
    return (temp_ave_inital_cond_indexed)




#%%


# gfdl
temp_ave_inital_cond_gfdl_his=initial_cond_ave_temp (df_deox_period_surf_gfdl_his, temp_gfdl_his_hypo_TB)
temp_ave_inital_cond_gfdl_rcp26=initial_cond_ave_temp (df_deox_period_surf_gfdl_rcp26, temp_gfdl_rcp26_hypo_TB)
temp_ave_inital_cond_gfdl_rcp60=initial_cond_ave_temp (df_deox_period_surf_gfdl_rcp60, temp_gfdl_rcp60_hypo_TB)
temp_ave_inital_cond_gfdl_rcp85=initial_cond_ave_temp (df_deox_period_surf_gfdl_rcp85, temp_gfdl_rcp85_hypo_TB)

# hadgem
temp_ave_inital_cond_hadgem_his=initial_cond_ave_temp (df_deox_period_surf_hadgem_his, temp_hadgem_his_hypo_TB)
temp_ave_inital_cond_hadgem_rcp26=initial_cond_ave_temp (df_deox_period_surf_hadgem_rcp26, temp_hadgem_rcp26_hypo_TB)
temp_ave_inital_cond_hadgem_rcp60=initial_cond_ave_temp (df_deox_period_surf_hadgem_rcp60, temp_hadgem_rcp60_hypo_TB)
temp_ave_inital_cond_hadgem_rcp85=initial_cond_ave_temp (df_deox_period_surf_hadgem_rcp85, temp_hadgem_rcp85_hypo_TB)

# ipsl
temp_ave_inital_cond_ipsl_his=initial_cond_ave_temp (df_deox_period_surf_ipsl_his, temp_ipsl_his_hypo_TB)
temp_ave_inital_cond_ipsl_rcp26=initial_cond_ave_temp (df_deox_period_surf_ipsl_rcp26, temp_ipsl_rcp26_hypo_TB)
temp_ave_inital_cond_ipsl_rcp60=initial_cond_ave_temp (df_deox_period_surf_ipsl_rcp60, temp_ipsl_rcp60_hypo_TB)
temp_ave_inital_cond_ipsl_rcp85=initial_cond_ave_temp (df_deox_period_surf_ipsl_rcp85, temp_ipsl_rcp85_hypo_TB)

# miroc
temp_ave_inital_cond_miroc_his=initial_cond_ave_temp (df_deox_period_surf_miroc_his, temp_miroc_his_hypo_TB)
temp_ave_inital_cond_miroc_rcp26=initial_cond_ave_temp (df_deox_period_surf_miroc_rcp26, temp_miroc_rcp26_hypo_TB)
temp_ave_inital_cond_miroc_rcp60=initial_cond_ave_temp (df_deox_period_surf_miroc_rcp60, temp_miroc_rcp60_hypo_TB)
temp_ave_inital_cond_miroc_rcp85=initial_cond_ave_temp (df_deox_period_surf_miroc_rcp85, temp_miroc_rcp85_hypo_TB)


#%%four models togther 

#%%simply average 
temp_ave_inital_cond_4models_his=(temp_ave_inital_cond_gfdl_his+temp_ave_inital_cond_hadgem_his+temp_ave_inital_cond_ipsl_his+temp_ave_inital_cond_miroc_his)/4
temp_ave_inital_cond_4models_rcp26=(temp_ave_inital_cond_gfdl_rcp26+temp_ave_inital_cond_hadgem_rcp26+temp_ave_inital_cond_ipsl_rcp26+temp_ave_inital_cond_miroc_rcp26)/4
temp_ave_inital_cond_4models_rcp60=(temp_ave_inital_cond_gfdl_rcp60+temp_ave_inital_cond_hadgem_rcp60+temp_ave_inital_cond_ipsl_rcp60+temp_ave_inital_cond_miroc_rcp60)/4
temp_ave_inital_cond_4models_rcp85=(temp_ave_inital_cond_gfdl_rcp85+temp_ave_inital_cond_hadgem_rcp85+temp_ave_inital_cond_ipsl_rcp85+temp_ave_inital_cond_miroc_rcp85)/4

#%% Plot mean data

plt.figure(figsize=(15, 10))  


plt.plot(temp_ave_inital_cond_4models_his[1975 <temp_ave_inital_cond_4models_his.index], label='His', color='grey')#marker='o',
plt.plot(temp_ave_inital_cond_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(temp_ave_inital_cond_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(temp_ave_inital_cond_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines
trendline_his = np.polyfit(temp_ave_inital_cond_4models_his[1975 <temp_ave_inital_cond_4models_his.index].index, temp_ave_inital_cond_4models_his[1975 <temp_ave_inital_cond_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, temp_ave_inital_cond_4models_his[1975 <temp_ave_inital_cond_4models_his.index].index)
plt.plot(temp_ave_inital_cond_4models_his[1975 <temp_ave_inital_cond_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 8.75, f'y = {trendline_his[0]:.3f}x + {trendline_his[1]:.2f}', color='grey')
trendline_his[0]
#-0.014019445756573861#whole historical period 
#-0.03297386981203487


trendline_rcp26 = np.polyfit(temp_ave_inital_cond_4models_rcp26.index, temp_ave_inital_cond_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, temp_ave_inital_cond_4models_rcp26.index)
plt.plot(temp_ave_inital_cond_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 8.5, f'y = {trendline_rcp26[0]:.3f}x + {trendline_rcp26[1]:.2f}', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(temp_ave_inital_cond_4models_rcp60.index, temp_ave_inital_cond_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, temp_ave_inital_cond_4models_rcp60.index)
plt.plot(temp_ave_inital_cond_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 8.25, f'y = {trendline_rcp60[0]:.3f}x + {trendline_rcp60[1]:.2f}', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(temp_ave_inital_cond_4models_rcp85.index, temp_ave_inital_cond_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, temp_ave_inital_cond_4models_rcp85.index)
plt.plot(temp_ave_inital_cond_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 8, f'y = {trendline_rcp85[0]:.3f}x + {trendline_rcp85[1]:.2f}', color='r')
trendline_rcp85[0]
#-0.22818336162987937



# Set the y-axis limits with an interval of 25
y_ticks = np.arange(3, 10, 1)
plt.yticks(y_ticks)

plt.ylabel('Hypolimnetic average temperature on initial condition day [°C]')
#plt.xlabel('Year')
plt.legend(loc='lower center')

plt.savefig("allsenarios_mean_hypolimnetic_ave_initial_cond_temp_trendline_30yearshisto.png", dpi=300)



#%% weighting in the same value 

###########his
all_temp_ave_inital_cond_4models_his=pd.concat([temp_ave_inital_cond_gfdl_his, temp_ave_inital_cond_hadgem_his, temp_ave_inital_cond_ipsl_his, temp_ave_inital_cond_miroc_his], axis=1)



#glue_df_temp_ave_inital_cond_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_ave_inital_cond_4models_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_ave_inital_cond_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_ave_inital_cond_his= glue_df_temp_ave_inital_cond_his.set_index(all_temp_ave_inital_cond_4models_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_ave_inital_cond_his.csv'

glue_df_temp_ave_inital_cond_his.to_csv(file_path )


#########rcp26
all_temp_ave_inital_cond_4models_rcp26=pd.concat([temp_ave_inital_cond_gfdl_rcp26, temp_ave_inital_cond_hadgem_rcp26, temp_ave_inital_cond_ipsl_rcp26, temp_ave_inital_cond_miroc_rcp26], axis=1)



#glue_df_temp_ave_inital_cond_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_ave_inital_cond_4models_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_ave_inital_cond_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_ave_inital_cond_rcp26= glue_df_temp_ave_inital_cond_rcp26.set_index(all_temp_ave_inital_cond_4models_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_ave_inital_cond_rcp26.csv'

glue_df_temp_ave_inital_cond_rcp26.to_csv(file_path )


#########rcp60
all_temp_ave_inital_cond_4models_rcp60=pd.concat([temp_ave_inital_cond_gfdl_rcp60, temp_ave_inital_cond_hadgem_rcp60, temp_ave_inital_cond_ipsl_rcp60, temp_ave_inital_cond_miroc_rcp60], axis=1)



#glue_df_temp_ave_inital_cond_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_ave_inital_cond_4models_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_ave_inital_cond_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_ave_inital_cond_rcp60= glue_df_temp_ave_inital_cond_rcp60.set_index(all_temp_ave_inital_cond_4models_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_ave_inital_cond_rcp60.csv'

glue_df_temp_ave_inital_cond_rcp60.to_csv(file_path )


######rcp85
all_temp_ave_inital_cond_4models_rcp85=pd.concat([temp_ave_inital_cond_gfdl_rcp85, temp_ave_inital_cond_hadgem_rcp85, temp_ave_inital_cond_ipsl_rcp85, temp_ave_inital_cond_miroc_rcp85], axis=1)



#glue_df_temp_ave_inital_cond_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_ave_inital_cond_4models_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_ave_inital_cond_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_ave_inital_cond_rcp85= glue_df_temp_ave_inital_cond_rcp85.set_index(all_temp_ave_inital_cond_4models_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_ave_inital_cond_rcp85.csv'

glue_df_temp_ave_inital_cond_rcp85.to_csv(file_path )


#%% MK test on onset Jday 100 years 

glue_df_temp_ave_inital_cond_100years_rcp26=pd.concat([glue_df_temp_ave_inital_cond_his[glue_df_temp_ave_inital_cond_his.index>1999] , glue_df_temp_ave_inital_cond_rcp26])

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_ave_inital_cond_100years_rcp26['50%'])

(0.042909585188926215,
 'positively autocorrelated',
 'no trend',
 0.39537976650245854,
 -0.0030987870366662286,
 6.203108804534785)


glue_df_temp_ave_inital_cond_100years_rcp60=pd.concat([glue_df_temp_ave_inital_cond_his[glue_df_temp_ave_inital_cond_his.index>1999] , glue_df_temp_ave_inital_cond_rcp60])

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_ave_inital_cond_100years_rcp60['50%'])
(0.031133374418379583,
 'positively autocorrelated',
 'no trend',
 0.3894166517890816,
 0.0023226978998165853,
 6.168823304990549)




glue_df_temp_ave_inital_cond_100years_rcp85=pd.concat([glue_df_temp_ave_inital_cond_his[glue_df_temp_ave_inital_cond_his.index>1999] , glue_df_temp_ave_inital_cond_rcp85])

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_ave_inital_cond_100years_rcp85['50%'])
(0.04161580149173012,
 'positively autocorrelated',
 'no trend',
 0.2168281017103313,
 0.00323671379653651,
 6.37754845493745)


#%% plotting the temp on inital condition day 100years

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_temp_ave_inital_cond_100years_rcp26.index, glue_df_temp_ave_inital_cond_100years_rcp26['5%'], glue_df_temp_ave_inital_cond_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_temp_ave_inital_cond_100years_rcp26.index, glue_df_temp_ave_inital_cond_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )


ax=plt.fill_between(glue_df_temp_ave_inital_cond_100years_rcp60.index, glue_df_temp_ave_inital_cond_100years_rcp60['5%'], glue_df_temp_ave_inital_cond_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_temp_ave_inital_cond_100years_rcp60.index, glue_df_temp_ave_inital_cond_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_temp_ave_inital_cond_100years_rcp85.index, glue_df_temp_ave_inital_cond_100years_rcp85['5%'], glue_df_temp_ave_inital_cond_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_temp_ave_inital_cond_100years_rcp85.index, glue_df_temp_ave_inital_cond_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


ax=plt.ylabel('Hypolimnetic average temperature\n on initial condition day [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(3, 16, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.9, -0.15), fontsize=22,ncol= 3) 

fig.savefig("GLUE_Timeseries_deox_temp_hypo_initalcond_day_100years.png", dpi=300, bbox_inches='tight')


#%% seperate GCMs trends over 80 years 

############################################rcp2.6


autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_gfdl_rcp26[temp_ave_inital_cond_gfdl_rcp26.index>2019])
"""
(0.15938365918083347,
 'positively autocorrelated',
 'decreasing',
 0.012117526300158277,
 -0.011769883690332758,
 6.543024949499741)
"""




autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_hadgem_rcp26[temp_ave_inital_cond_hadgem_rcp26.index>2019])
"""
(0.10395940660991956,
 'positively autocorrelated',
 'no trend',
 0.5324880133973859,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_ipsl_rcp26[temp_ave_inital_cond_ipsl_rcp26.index>2019])
"""
(0.11678737935710992,
 'positively autocorrelated',
 'no trend',
 0.055454335409584,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_miroc_rcp26[temp_ave_inital_cond_miroc_rcp26.index>2019])
"""
(0.10599677170762745,
 'positively autocorrelated',
 'no trend',
 0.18231969145577365,
 0,
 0)
"""





#############################################rcp6.0

autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_gfdl_rcp60[temp_ave_inital_cond_gfdl_rcp60.index>2019])
"""
(0.10305488167871998,
 'positively autocorrelated',
 'no trend',
 0.23128905261097055,
 0,
 0)
"""




autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_hadgem_rcp60[temp_ave_inital_cond_hadgem_rcp60.index>2019])
"""
(0.10088666101296807,
 'positively autocorrelated',
 'no trend',
 0.8650599648948218,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_ipsl_rcp60[temp_ave_inital_cond_ipsl_rcp60.index>2019])
"""
(0.1405672538032982,
 'positively autocorrelated',
 'no trend',
 0.5805578199014052,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_miroc_rcp60[temp_ave_inital_cond_miroc_rcp60.index>2019])
"""
(0.15416455629352468,
 'positively autocorrelated',
 'no trend', 
 nan, 
 0, 
 0)
"""









#############################################rcp8.5


autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_gfdl_rcp85[temp_ave_inital_cond_gfdl_rcp85.index>2019])
"""
(0.11930497881189889,
 'positively autocorrelated',
 'no trend',
 0.9801077788323262,
 0,
 0)
"""




autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_hadgem_rcp85[temp_ave_inital_cond_hadgem_rcp85.index>2019])
"""
(0.09264119728763183,
 'positively autocorrelated',
 'no trend',
 0.8180770985228265,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_ipsl_rcp85[temp_ave_inital_cond_ipsl_rcp85.index>2019])
"""
(0.11475547118764928,
 'positively autocorrelated',
 'increasing',
 0.004093415905650266,
 0.0253864717979907,
 5.660363041796757)
"""



autocorr_MK_org_modif_sens_slope_test(temp_ave_inital_cond_miroc_rcp85[temp_ave_inital_cond_miroc_rcp85.index>2019])
"""
(0.09123911798264389,
 'positively autocorrelated',
 'decreasing',
 0.04105612349516985,
 -0.011971851115066549,
 6.381835170157583)
"""





#%% MK test on onset Jday 80 years 

glue_df_temp_ave_inital_cond_80years_rcp26=glue_df_temp_ave_inital_cond_rcp26[glue_df_temp_ave_inital_cond_rcp26.index>2019]

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_ave_inital_cond_80years_rcp26['50%'])

(0.04521290083216052,
 'positively autocorrelated',
 'decreasing',
 4.237578663612851e-05,
 -0.01068088701748445,
 6.475502956998175)

glue_df_temp_ave_inital_cond_80years_rcp60=glue_df_temp_ave_inital_cond_rcp60[glue_df_temp_ave_inital_cond_rcp60.index>2019]

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_ave_inital_cond_80years_rcp60['50%'])
(0.029062473937444776,
 'positively autocorrelated',
 'no trend',
 0.5862620341690845,
 0,
 0)



glue_df_temp_ave_inital_cond_80years_rcp85=glue_df_temp_ave_inital_cond_rcp85[glue_df_temp_ave_inital_cond_rcp85.index>2019]

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_ave_inital_cond_80years_rcp85['50%'])
(0.03749711801320919,
 'positively autocorrelated',
 'no trend',
 0.8540873177929522,
 0,
 0)



#%% plotting the temp on inital condition day 80years

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_temp_ave_inital_cond_80years_rcp26.index, glue_df_temp_ave_inital_cond_80years_rcp26['5%'], glue_df_temp_ave_inital_cond_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_temp_ave_inital_cond_80years_rcp26.index, glue_df_temp_ave_inital_cond_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_temp_ave_inital_cond_80years_rcp26['50%'])
ax=plt.plot(glue_df_temp_ave_inital_cond_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--')

ax= plt.text(2065, 13, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value < 0.0001', color='g' , fontsize= 20 )



ax=plt.fill_between(glue_df_temp_ave_inital_cond_80years_rcp60.index, glue_df_temp_ave_inital_cond_80years_rcp60['5%'], glue_df_temp_ave_inital_cond_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_temp_ave_inital_cond_80years_rcp60.index, glue_df_temp_ave_inital_cond_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_temp_ave_inital_cond_80years_rcp85.index, glue_df_temp_ave_inital_cond_80years_rcp85['5%'], glue_df_temp_ave_inital_cond_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_temp_ave_inital_cond_80years_rcp85.index, glue_df_temp_ave_inital_cond_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


ax=plt.ylabel('Hypolimnetic average temperature\n on initial condition day [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(3, 14, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22, ncol=3) 

fig.savefig("GLUE_Timeseries_deox_temp_hypo_initalcond_day_80years.png", dpi=300, bbox_inches='tight')



#%%initial_cond_ave_surface_water_temp

def initial_cond_surf_temp (df_deox , temp_surf ):
    initial_indices=df_deox.groupby('year').min()['initial_cond_indices']
    temp_T_inital_cond=temp_surf[np.array(initial_indices).astype(int) ]      
    temp_T_inital_cond_indexed=pd.Series(temp_T_inital_cond, index=initial_indices.index)
    return (temp_T_inital_cond_indexed)

#%%

#gfdl
temp_initial_cond_surf_gfdl_his=initial_cond_surf_temp(df_deox_period_surf_gfdl_his,  tem_gfdl_his_surf)
temp_initial_cond_surf_gfdl_rcp26=initial_cond_surf_temp(df_deox_period_surf_gfdl_rcp26,  tem_gfdl_rcp26_surf)
temp_initial_cond_surf_gfdl_rcp60=initial_cond_surf_temp(df_deox_period_surf_gfdl_rcp60,  tem_gfdl_rcp60_surf)
temp_initial_cond_surf_gfdl_rcp85=initial_cond_surf_temp(df_deox_period_surf_gfdl_rcp85,  tem_gfdl_rcp85_surf)

#hadgem
temp_initial_cond_surf_hadgem_his=initial_cond_surf_temp(df_deox_period_surf_hadgem_his,  tem_hadgem_his_surf)
temp_initial_cond_surf_hadgem_rcp26=initial_cond_surf_temp(df_deox_period_surf_hadgem_rcp26,  tem_hadgem_rcp26_surf)
temp_initial_cond_surf_hadgem_rcp60=initial_cond_surf_temp(df_deox_period_surf_hadgem_rcp60,  tem_hadgem_rcp60_surf)
temp_initial_cond_surf_hadgem_rcp85=initial_cond_surf_temp(df_deox_period_surf_hadgem_rcp85,  tem_hadgem_rcp85_surf)


#ipsl
temp_initial_cond_surf_ipsl_his=initial_cond_surf_temp(df_deox_period_surf_ipsl_his,  tem_ipsl_his_surf)
temp_initial_cond_surf_ipsl_rcp26=initial_cond_surf_temp(df_deox_period_surf_ipsl_rcp26,  tem_ipsl_rcp26_surf)
temp_initial_cond_surf_ipsl_rcp60=initial_cond_surf_temp(df_deox_period_surf_ipsl_rcp60,  tem_ipsl_rcp60_surf)
temp_initial_cond_surf_ipsl_rcp85=initial_cond_surf_temp(df_deox_period_surf_ipsl_rcp85,  tem_ipsl_rcp85_surf)

#miroc
temp_initial_cond_surf_miroc_his=initial_cond_surf_temp(df_deox_period_surf_miroc_his,  tem_miroc_his_surf)
temp_initial_cond_surf_miroc_rcp26=initial_cond_surf_temp(df_deox_period_surf_miroc_rcp26,  tem_miroc_rcp26_surf)
temp_initial_cond_surf_miroc_rcp60=initial_cond_surf_temp(df_deox_period_surf_miroc_rcp60,  tem_miroc_rcp60_surf)
temp_initial_cond_surf_miroc_rcp85=initial_cond_surf_temp(df_deox_period_surf_miroc_rcp85,  tem_miroc_rcp85_surf)


#%%four models togther 

#%%simply average 
temp_initial_cond_surf_4models_his=(temp_initial_cond_surf_gfdl_his+temp_initial_cond_surf_hadgem_his+temp_initial_cond_surf_ipsl_his+temp_initial_cond_surf_miroc_his)/4
temp_initial_cond_surf_4models_rcp26=(temp_initial_cond_surf_gfdl_rcp26+temp_initial_cond_surf_hadgem_rcp26+temp_initial_cond_surf_ipsl_rcp26+temp_initial_cond_surf_miroc_rcp26)/4
temp_initial_cond_surf_4models_rcp60=(temp_initial_cond_surf_gfdl_rcp60+temp_initial_cond_surf_hadgem_rcp60+temp_initial_cond_surf_ipsl_rcp60+temp_initial_cond_surf_miroc_rcp60)/4
temp_initial_cond_surf_4models_rcp85=(temp_initial_cond_surf_gfdl_rcp85+temp_initial_cond_surf_hadgem_rcp85+temp_initial_cond_surf_ipsl_rcp85+temp_initial_cond_surf_miroc_rcp85)/4

#%% Plot mean data

plt.figure(figsize=(15, 10))  


plt.plot(temp_initial_cond_surf_4models_his[1975 <temp_initial_cond_surf_4models_his.index], label='His', color='grey')#marker='o',
plt.plot(temp_initial_cond_surf_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(temp_initial_cond_surf_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(temp_initial_cond_surf_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines
trendline_his = np.polyfit(temp_initial_cond_surf_4models_his[1975 <temp_initial_cond_surf_4models_his.index].index, temp_initial_cond_surf_4models_his[1975 <temp_initial_cond_surf_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, temp_initial_cond_surf_4models_his[1975 <temp_initial_cond_surf_4models_his.index].index)
plt.plot(temp_initial_cond_surf_4models_his[1975 <temp_initial_cond_surf_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 8.75, f'y = {trendline_his[0]:.3f}x + {trendline_his[1]:.2f}', color='grey')
trendline_his[0]
#-0.02666296709631443#whole historical period 



trendline_rcp26 = np.polyfit(temp_initial_cond_surf_4models_rcp26.index, temp_initial_cond_surf_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, temp_initial_cond_surf_4models_rcp26.index)
plt.plot(temp_initial_cond_surf_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 8.5, f'y = {trendline_rcp26[0]:.3f}x + {trendline_rcp26[1]:.2f}', color='green')
trendline_rcp26[0]#slop of trendline
#-0.003223956172548877


trendline_rcp60 = np.polyfit(temp_initial_cond_surf_4models_rcp60.index, temp_initial_cond_surf_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, temp_initial_cond_surf_4models_rcp60.index)
plt.plot(temp_initial_cond_surf_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 8.25, f'y = {trendline_rcp60[0]:.3f}x + {trendline_rcp60[1]:.2f}', color='yellow')
trendline_rcp60[0]#slop of trendline
#0.0015787463309951642


trendline_rcp85 = np.polyfit(temp_initial_cond_surf_4models_rcp85.index, temp_initial_cond_surf_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, temp_initial_cond_surf_4models_rcp85.index)
plt.plot(temp_initial_cond_surf_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 8, f'y = {trendline_rcp85[0]:.3f}x + {trendline_rcp85[1]:.2f}', color='r')
trendline_rcp85[0]
# 0.0002418619762269367



# Set the y-axis limits with an interval of 25
y_ticks = np.arange(3, 10, 1)
plt.yticks(y_ticks)

plt.ylabel('Surface temperature on initial condition day [°C]')
#plt.xlabel('Year')
plt.legend(loc='lower center')

plt.savefig("allsenarios_mean_hypolimnetic_ave_initial_cond_temp_trendline_30yearshisto.png", dpi=300)



#%% weighting in the same value 

###########his
all_temp_initial_cond_surf_4models_his=pd.concat([temp_initial_cond_surf_gfdl_his, temp_initial_cond_surf_hadgem_his, temp_initial_cond_surf_ipsl_his, temp_initial_cond_surf_miroc_his], axis=1)



#glue_df_temp_initial_cond_surf_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_initial_cond_surf_4models_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_initial_cond_surf_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_initial_cond_surf_his= glue_df_temp_initial_cond_surf_his.set_index(all_temp_initial_cond_surf_4models_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_initial_cond_surf_his.csv'

glue_df_temp_initial_cond_surf_his.to_csv(file_path )


#########rcp26
all_temp_initial_cond_surf_4models_rcp26=pd.concat([temp_initial_cond_surf_gfdl_rcp26, temp_initial_cond_surf_hadgem_rcp26, temp_initial_cond_surf_ipsl_rcp26, temp_initial_cond_surf_miroc_rcp26], axis=1)



#glue_df_temp_initial_cond_surf_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_initial_cond_surf_4models_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_initial_cond_surf_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_initial_cond_surf_rcp26= glue_df_temp_initial_cond_surf_rcp26.set_index(all_temp_initial_cond_surf_4models_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_initial_cond_surf_rcp26.csv'

glue_df_temp_initial_cond_surf_rcp26.to_csv(file_path )


#########rcp60
all_temp_initial_cond_surf_4models_rcp60=pd.concat([temp_initial_cond_surf_gfdl_rcp60, temp_initial_cond_surf_hadgem_rcp60, temp_initial_cond_surf_ipsl_rcp60, temp_initial_cond_surf_miroc_rcp60], axis=1)



#glue_df_temp_initial_cond_surf_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_initial_cond_surf_4models_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_initial_cond_surf_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_initial_cond_surf_rcp60= glue_df_temp_initial_cond_surf_rcp60.set_index(all_temp_initial_cond_surf_4models_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_initial_cond_surf_rcp60.csv'

glue_df_temp_initial_cond_surf_rcp60.to_csv(file_path )


######rcp85
all_temp_initial_cond_surf_4models_rcp85=pd.concat([temp_initial_cond_surf_gfdl_rcp85, temp_initial_cond_surf_hadgem_rcp85, temp_initial_cond_surf_ipsl_rcp85, temp_initial_cond_surf_miroc_rcp85], axis=1)



#glue_df_temp_initial_cond_surf_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_initial_cond_surf_4models_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_initial_cond_surf_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_initial_cond_surf_rcp85= glue_df_temp_initial_cond_surf_rcp85.set_index(all_temp_initial_cond_surf_4models_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_initial_cond_surf_rcp85.csv'

glue_df_temp_initial_cond_surf_rcp85.to_csv(file_path )


#%% MK test on onset Jday 100 years 

glue_df_temp_initial_cond_surf_100years_rcp26=pd.concat([glue_df_temp_initial_cond_surf_his[glue_df_temp_initial_cond_surf_his.index>1999] , glue_df_temp_initial_cond_surf_rcp26])

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_initial_cond_surf_100years_rcp26['50%'])
(0.017167772480710698,
 'positively autocorrelated',
 'no trend',
 0.5714602923224503,
 0,
 0)


glue_df_temp_initial_cond_surf_100years_rcp60=pd.concat([glue_df_temp_initial_cond_surf_his[glue_df_temp_initial_cond_surf_his.index>1999] , glue_df_temp_initial_cond_surf_rcp60])

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_initial_cond_surf_100years_rcp60['50%'])
(0.013905968238924763,
 'positively autocorrelated',
 'no trend',
 0.3732205908375017,
 0,
 0)



glue_df_temp_initial_cond_surf_100years_rcp85=pd.concat([glue_df_temp_initial_cond_surf_his[glue_df_temp_initial_cond_surf_his.index>1999] , glue_df_temp_initial_cond_surf_rcp85])

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_initial_cond_surf_100years_rcp85['50%'])
(0.01696609249290171,
 'positively autocorrelated',
 'no trend',
 0.2322785302590349,
 0,
 0)


#%% plotting the temp on inital condition day 100years

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_temp_initial_cond_surf_100years_rcp26.index, glue_df_temp_initial_cond_surf_100years_rcp26['5%'], glue_df_temp_initial_cond_surf_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_temp_initial_cond_surf_100years_rcp26.index, glue_df_temp_initial_cond_surf_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )


ax=plt.fill_between(glue_df_temp_initial_cond_surf_100years_rcp60.index, glue_df_temp_initial_cond_surf_100years_rcp60['5%'], glue_df_temp_initial_cond_surf_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_temp_initial_cond_surf_100years_rcp60.index, glue_df_temp_initial_cond_surf_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_temp_initial_cond_surf_100years_rcp85.index, glue_df_temp_initial_cond_surf_100years_rcp85['5%'], glue_df_temp_initial_cond_surf_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_temp_initial_cond_surf_100years_rcp85.index, glue_df_temp_initial_cond_surf_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


ax=plt.ylabel('Surface temperature on \nstratification onset [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(5, 16, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.9, -0.15), fontsize=22,ncol= 3) 

fig.savefig("GLUE_Timeseries_deox_temp_hypo_initalcond_day_100years.png", dpi=300, bbox_inches='tight')


#%% seperate GCMs trends over 80 years 

############################################rcp2.6


autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_gfdl_rcp26[temp_initial_cond_surf_gfdl_rcp26.index>2019])
"""
(0.07464242, 
 'positively autocorrelated',
 'no trend',
 0.079004399377683,
 0,
 0)
"""




autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_hadgem_rcp26[temp_initial_cond_surf_hadgem_rcp26.index>2019])
"""
(0.040026065, 
 'positively autocorrelated',
 'no trend', 
 0.293199074995266,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_ipsl_rcp26[temp_initial_cond_surf_ipsl_rcp26.index>2019])
"""
(0.06304009,
 'positively autocorrelated',
 'no trend',
 0.06692071659850218,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_miroc_rcp26[temp_initial_cond_surf_miroc_rcp26.index>2019])
"""
(0.04871719,
 'positively autocorrelated',
 'no trend',
 0.36253683132376047,
 0,
 0)
"""





#############################################rcp6.0

autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_gfdl_rcp60[temp_initial_cond_surf_gfdl_rcp60.index>2019])
"""
(0.06353531,
 'positively autocorrelated',
 'no trend',
 0.26020212827084466,
 0,
 0)
"""




autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_hadgem_rcp60[temp_initial_cond_surf_hadgem_rcp60.index>2019])
"""
(0.044764392,
 'positively autocorrelated',
 'no trend',
 0.9684674544736636,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_ipsl_rcp60[temp_initial_cond_surf_ipsl_rcp60.index>2019])
"""
(0.075958684,
 'positively autocorrelated',
 'no trend',
 0.4877896897967642,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_miroc_rcp60[temp_initial_cond_surf_miroc_rcp60.index>2019])
"""
(0.07577876, 
 'positively autocorrelated',
 'no trend', 
 0.8077974225398818,
 0,
 0)
"""









#############################################rcp8.5


autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_gfdl_rcp85[temp_initial_cond_surf_gfdl_rcp85.index>2019])
"""
(0.06563772, 
 'positively autocorrelated',
 'no trend',
 0.6457860526096959, 
 0,
 0)
"""




autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_hadgem_rcp85[temp_initial_cond_surf_hadgem_rcp85.index>2019])
"""
(0.032154866,
 'positively autocorrelated',
 'no trend',
 0.9222349062072386,
 0,
 0)
"""



autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_ipsl_rcp85[temp_initial_cond_surf_ipsl_rcp85.index>2019])
"""
(0.060745303,
 'positively autocorrelated',
 'increasing',
 0.003614053767594827,
 0.01632559514260507,
 6.928876374755894)
"""



autocorr_MK_org_modif_sens_slope_test(temp_initial_cond_surf_miroc_rcp85[temp_initial_cond_surf_miroc_rcp85.index>2019])
"""
(0.03633252,
 'positively autocorrelated',
 'decreasing',
 0.02020837936615205,
 -0.012577518418028549,
 7.382974496967083)
"""





#%% MK test on onset Jday 80 years 

glue_df_temp_initial_cond_surf_80years_rcp26=glue_df_temp_initial_cond_surf_rcp26[glue_df_temp_initial_cond_surf_rcp26.index>2019]

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_initial_cond_surf_80years_rcp26['50%'])

(0.019133369670584762,
 'positively autocorrelated',
 'no trend',
 0.06789845332333866,
 0,
 0)
glue_df_temp_initial_cond_surf_80years_rcp60=glue_df_temp_initial_cond_surf_rcp60[glue_df_temp_initial_cond_surf_rcp60.index>2019]

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_initial_cond_surf_80years_rcp60['50%'])
(0.014477258620502973,
 'positively autocorrelated',
 'no trend',
 0.7680083699552058,
 0,
 0)



glue_df_temp_initial_cond_surf_80years_rcp85=glue_df_temp_initial_cond_surf_rcp85[glue_df_temp_initial_cond_surf_rcp85.index>2019]

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_initial_cond_surf_80years_rcp85['50%'])
(0.016021912915072715,
 'positively autocorrelated',
 'no trend',
 0.7643549891311205,
 0,
 0)



#%% plotting the temp on inital condition day 80years

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_temp_initial_cond_surf_80years_rcp26.index, glue_df_temp_initial_cond_surf_80years_rcp26['5%'], glue_df_temp_initial_cond_surf_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_temp_initial_cond_surf_80years_rcp26.index, glue_df_temp_initial_cond_surf_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )


ax=plt.fill_between(glue_df_temp_initial_cond_surf_80years_rcp60.index, glue_df_temp_initial_cond_surf_80years_rcp60['5%'], glue_df_temp_initial_cond_surf_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_temp_initial_cond_surf_80years_rcp60.index, glue_df_temp_initial_cond_surf_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_temp_initial_cond_surf_80years_rcp85.index, glue_df_temp_initial_cond_surf_80years_rcp85['5%'], glue_df_temp_initial_cond_surf_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_temp_initial_cond_surf_80years_rcp85.index, glue_df_temp_initial_cond_surf_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


ax=plt.ylabel('Surface temperature\n on initial condition day [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(5, 16, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22, ncol=3) 

fig.savefig("GLUE_Timeseries_deox_temp_surface_initalcond_day_80years.png", dpi=300, bbox_inches='tight')


#%%initial_cond_ave_DO


def initial_cond_ave_DO (df_deox , temp_2D_hypo ,Vr= hypo_morpho_vriables_gotm_grid[0] ):
    initial_indices=df_deox.groupby('year').min()['initial_cond_indices']
    temp_hypo_inital_cond=temp_2D_hypo[np.array(initial_indices).astype(int) , :]
    C_sat_inital=C_satur(temp_hypo_inital_cond, percent=1)
    C_ave_inital_cond= np.dot (C_sat_inital , Vr) / sum (Vr)        
    C_ave_inital_cond_indexed=pd.Series(C_ave_inital_cond, index=initial_indices.index)
    return (C_ave_inital_cond_indexed)


#%%in each GCM model

# gfdl
C_ave_inital_cond_gfdl_his=initial_cond_ave_DO (df_deox_period_surf_gfdl_his, temp_gfdl_his_hypo_TB)
C_ave_inital_cond_gfdl_rcp26=initial_cond_ave_DO (df_deox_period_surf_gfdl_rcp26, temp_gfdl_rcp26_hypo_TB)
C_ave_inital_cond_gfdl_rcp60=initial_cond_ave_DO (df_deox_period_surf_gfdl_rcp60, temp_gfdl_rcp60_hypo_TB)
C_ave_inital_cond_gfdl_rcp85=initial_cond_ave_DO (df_deox_period_surf_gfdl_rcp85, temp_gfdl_rcp85_hypo_TB)

# hadgem
C_ave_inital_cond_hadgem_his=initial_cond_ave_DO (df_deox_period_surf_hadgem_his, temp_hadgem_his_hypo_TB)
C_ave_inital_cond_hadgem_rcp26=initial_cond_ave_DO (df_deox_period_surf_hadgem_rcp26, temp_hadgem_rcp26_hypo_TB)
C_ave_inital_cond_hadgem_rcp60=initial_cond_ave_DO (df_deox_period_surf_hadgem_rcp60, temp_hadgem_rcp60_hypo_TB)
C_ave_inital_cond_hadgem_rcp85=initial_cond_ave_DO (df_deox_period_surf_hadgem_rcp85, temp_hadgem_rcp85_hypo_TB)

# ipsl
C_ave_inital_cond_ipsl_his=initial_cond_ave_DO (df_deox_period_surf_ipsl_his, temp_ipsl_his_hypo_TB)
C_ave_inital_cond_ipsl_rcp26=initial_cond_ave_DO (df_deox_period_surf_ipsl_rcp26, temp_ipsl_rcp26_hypo_TB)
C_ave_inital_cond_ipsl_rcp60=initial_cond_ave_DO (df_deox_period_surf_ipsl_rcp60, temp_ipsl_rcp60_hypo_TB)
C_ave_inital_cond_ipsl_rcp85=initial_cond_ave_DO (df_deox_period_surf_ipsl_rcp85, temp_ipsl_rcp85_hypo_TB)

# miroc
C_ave_inital_cond_miroc_his=initial_cond_ave_DO (df_deox_period_surf_miroc_his, temp_miroc_his_hypo_TB)
C_ave_inital_cond_miroc_rcp26=initial_cond_ave_DO (df_deox_period_surf_miroc_rcp26, temp_miroc_rcp26_hypo_TB)
C_ave_inital_cond_miroc_rcp60=initial_cond_ave_DO (df_deox_period_surf_miroc_rcp60, temp_miroc_rcp60_hypo_TB)
C_ave_inital_cond_miroc_rcp85=initial_cond_ave_DO (df_deox_period_surf_miroc_rcp85, temp_miroc_rcp85_hypo_TB)


#%%four models togther 

#%%simply mean 
C_ave_inital_cond_4models_his=(C_ave_inital_cond_gfdl_his+C_ave_inital_cond_hadgem_his+C_ave_inital_cond_ipsl_his+C_ave_inital_cond_miroc_his)/4
C_ave_inital_cond_4models_rcp26=(C_ave_inital_cond_gfdl_rcp26+C_ave_inital_cond_hadgem_rcp26+C_ave_inital_cond_ipsl_rcp26+C_ave_inital_cond_miroc_rcp26)/4
C_ave_inital_cond_4models_rcp60=(C_ave_inital_cond_gfdl_rcp60+C_ave_inital_cond_hadgem_rcp60+C_ave_inital_cond_ipsl_rcp60+C_ave_inital_cond_miroc_rcp60)/4
C_ave_inital_cond_4models_rcp85=(C_ave_inital_cond_gfdl_rcp85+C_ave_inital_cond_hadgem_rcp85+C_ave_inital_cond_ipsl_rcp85+C_ave_inital_cond_miroc_rcp85)/4


# Plot mean data

plt.figure(figsize=(15, 10))  


plt.plot(C_ave_inital_cond_4models_his[1975 <C_ave_inital_cond_4models_his.index], label='His', color='grey')#marker='o',
plt.plot(C_ave_inital_cond_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(C_ave_inital_cond_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(C_ave_inital_cond_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines
trendline_his = np.polyfit(C_ave_inital_cond_4models_his[1975 <C_ave_inital_cond_4models_his.index].index, C_ave_inital_cond_4models_his[1975 <C_ave_inital_cond_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, C_ave_inital_cond_4models_his[1975 <C_ave_inital_cond_4models_his.index].index)
plt.plot(C_ave_inital_cond_4models_his[1975 <C_ave_inital_cond_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 11.75, f'y = {trendline_his[0]:.3f}x + {trendline_his[1]:.2f}', color='grey')
trendline_his[0]
#-0.014019445756573861


trendline_rcp26 = np.polyfit(C_ave_inital_cond_4models_rcp26.index, C_ave_inital_cond_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, C_ave_inital_cond_4models_rcp26.index)
plt.plot(C_ave_inital_cond_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 11.65, f'y = {trendline_rcp26[0]:.3f}x + {trendline_rcp26[1]:.2f}', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(C_ave_inital_cond_4models_rcp60.index, C_ave_inital_cond_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, C_ave_inital_cond_4models_rcp60.index)
plt.plot(C_ave_inital_cond_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 11.55, f'y = {trendline_rcp60[0]:.3f}x + {trendline_rcp60[1]:.2f}', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(C_ave_inital_cond_4models_rcp85.index, C_ave_inital_cond_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, C_ave_inital_cond_4models_rcp85.index)
plt.plot(C_ave_inital_cond_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 11.45, f'y = {trendline_rcp85[0]:.4f}x + {trendline_rcp85[1]:.2f}', color='r')
trendline_rcp85[0]
#-0.22818336162987937



# Set the y-axis limits with an interval of 25
y_ticks = np.arange(11, 13.5, 0.5)
plt.yticks(y_ticks)

plt.ylabel('Hypolimnetic average DO on initial condition day [g m$^{-3}$]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_mean_hypolimnetic_ave_initial_cond_DO_trendline_last30his.png", dpi=300)


#%%GLUE method all models togther 


#his
all_C_ave_inital_cond_4models_his=pd.concat([C_ave_inital_cond_gfdl_his, C_ave_inital_cond_hadgem_his, C_ave_inital_cond_ipsl_his, C_ave_inital_cond_miroc_his], axis=1)



#glue_df_C_ave_inital_cond_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_ave_inital_cond_4models_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_C_ave_inital_cond_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_C_ave_inital_cond_his= glue_df_C_ave_inital_cond_his.set_index(all_C_ave_inital_cond_4models_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_C_ave_inital_cond_his.csv'

glue_df_C_ave_inital_cond_his.to_csv(file_path )





#rcp26
all_C_ave_inital_cond_4models_rcp26=pd.concat([C_ave_inital_cond_gfdl_rcp26, C_ave_inital_cond_hadgem_rcp26, C_ave_inital_cond_ipsl_rcp26, C_ave_inital_cond_miroc_rcp26], axis=1)



#glue_df_C_ave_inital_cond_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_ave_inital_cond_4models_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_C_ave_inital_cond_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_C_ave_inital_cond_rcp26= glue_df_C_ave_inital_cond_rcp26.set_index(all_C_ave_inital_cond_4models_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_C_ave_inital_cond_rcp26.csv'

glue_df_C_ave_inital_cond_rcp26.to_csv(file_path )





#rcp60
all_C_ave_inital_cond_4models_rcp60=pd.concat([C_ave_inital_cond_gfdl_rcp60, C_ave_inital_cond_hadgem_rcp60, C_ave_inital_cond_ipsl_rcp60, C_ave_inital_cond_miroc_rcp60], axis=1)



#glue_df_C_ave_inital_cond_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_ave_inital_cond_4models_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_C_ave_inital_cond_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_C_ave_inital_cond_rcp60= glue_df_C_ave_inital_cond_rcp60.set_index(all_C_ave_inital_cond_4models_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_C_ave_inital_cond_rcp60.csv'

glue_df_C_ave_inital_cond_rcp60.to_csv(file_path )







#rcp85
all_C_ave_inital_cond_4models_rcp85=pd.concat([C_ave_inital_cond_gfdl_rcp85, C_ave_inital_cond_hadgem_rcp85, C_ave_inital_cond_ipsl_rcp85, C_ave_inital_cond_miroc_rcp85], axis=1)



#glue_df_C_ave_inital_cond_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_ave_inital_cond_4models_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_C_ave_inital_cond_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_C_ave_inital_cond_rcp85= glue_df_C_ave_inital_cond_rcp85.set_index(all_C_ave_inital_cond_4models_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_C_ave_inital_cond_rcp85.csv'

glue_df_C_ave_inital_cond_rcp85.to_csv(file_path )

#%% MK test on onset Jday 100 years 

glue_df_C_ave_inital_cond_100years_rcp26=pd.concat([glue_df_C_ave_inital_cond_his[glue_df_C_ave_inital_cond_his.index>1999] , glue_df_C_ave_inital_cond_rcp26])

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_100years_rcp26['50%'])
(0.001020861247627576,
 'positively autocorrelated',
 'no trend',
 0.38719034045273015,
 0.0009616792964703065,
 12.385009474651524)

glue_df_C_ave_inital_cond_100years_rcp60=pd.concat([glue_df_C_ave_inital_cond_his[glue_df_C_ave_inital_cond_his.index>1999] , glue_df_C_ave_inital_cond_rcp60])

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_100years_rcp60['50%'])
(0.0007853250092493819,
 'positively autocorrelated',
 'no trend',
 0.4060331836696607,
 -0.000738024003508433,
 12.394341428123429)




glue_df_C_ave_inital_cond_100years_rcp85=pd.concat([glue_df_C_ave_inital_cond_his[glue_df_C_ave_inital_cond_his.index>1999] , glue_df_C_ave_inital_cond_rcp85])

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_100years_rcp85['50%'])
(0.0011066323236927046,
 'positively autocorrelated',
 'no trend',
 0.20104794141334037,
 -0.0009542402425554665,
 12.325149894450892)



#%%Trendline of onset for all years in his and rcps


autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_his['50%'])
(0.0012171621494560978,
 'positively autocorrelated',
 'no trend',
 0.23414817277433886,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_rcp26['50%'])
(0.0010165772289419306,
 'positively autocorrelated',
 'no trend',
 0.07954884460682665,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_rcp60['50%'])
(0.0007418377238313894,
 'positively autocorrelated',
 'no trend',
 0.9895758681841262,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_rcp85['50%'])

(0.0011007243879855087,
 'positively autocorrelated',
 'no trend',
 0.951281927570192,
 0,
 0)


#%%1980-2019

glue_df_C_ave_inital_cond_40years_rcp26=pd.concat([glue_df_C_ave_inital_cond_his[glue_df_C_ave_inital_cond_his.index>1979] , glue_df_C_ave_inital_cond_rcp26[glue_df_C_ave_inital_cond_rcp26.index<2020]])
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_40years_rcp26['50%'])

(0.0012034342620742115,
 'positively autocorrelated',
 'no trend',
 0.2125219354050587,
 0,
 0)







glue_df_C_ave_inital_cond_40years_rcp60=pd.concat([glue_df_C_ave_inital_cond_his[glue_df_C_ave_inital_cond_his.index>1979] , glue_df_C_ave_inital_cond_rcp60[glue_df_C_ave_inital_cond_rcp60.index<2020]])
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_40years_rcp60['50%'])
(0.001207210803950601,
 'positively autocorrelated',
 'no trend',
 0.9535453737590693,
 0,
 0)


glue_df_C_ave_inital_cond_40years_rcp85=pd.concat([glue_df_C_ave_inital_cond_his[glue_df_C_ave_inital_cond_his.index>1979] , glue_df_C_ave_inital_cond_rcp85[glue_df_C_ave_inital_cond_rcp85.index<2020]])
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_40years_rcp85['50%'])
(0.0015123568768715388,
 'positively autocorrelated',
 'no trend',
 0.8067106222830902,
 0,
 0)




#%% plotting the C on inital condition day 100years

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_C_ave_inital_cond_100years_rcp26.index, glue_df_C_ave_inital_cond_100years_rcp26['5%'], glue_df_C_ave_inital_cond_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_100years_rcp26.index, glue_df_C_ave_inital_cond_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )


ax=plt.fill_between(glue_df_C_ave_inital_cond_100years_rcp60.index, glue_df_C_ave_inital_cond_100years_rcp60['5%'], glue_df_C_ave_inital_cond_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_100years_rcp60.index, glue_df_C_ave_inital_cond_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_C_ave_inital_cond_100years_rcp85.index, glue_df_C_ave_inital_cond_100years_rcp85['5%'], glue_df_C_ave_inital_cond_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_100years_rcp85.index, glue_df_C_ave_inital_cond_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


ax=plt.ylabel('Hypolimnetic average DO \non initial condition day [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(10, 14, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22 , ncol=3) 

fig.savefig("GLUE_Timeseries_deox_C_hypo_initalcond_day_100years.png", dpi=300, bbox_inches='tight')

#%% plotting the C on inital condition day 100years

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_C_ave_inital_cond_100years_rcp26.index, glue_df_C_ave_inital_cond_100years_rcp26['5%'], glue_df_C_ave_inital_cond_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_100years_rcp26.index, glue_df_C_ave_inital_cond_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )


ax=plt.fill_between(glue_df_C_ave_inital_cond_100years_rcp60.index, glue_df_C_ave_inital_cond_100years_rcp60['5%'], glue_df_C_ave_inital_cond_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_100years_rcp60.index, glue_df_C_ave_inital_cond_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_C_ave_inital_cond_100years_rcp85.index, glue_df_C_ave_inital_cond_100years_rcp85['5%'], glue_df_C_ave_inital_cond_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_100years_rcp85.index, glue_df_C_ave_inital_cond_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


ax=plt.ylabel('Hypolimnetic average DO \non initial condition day [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(10, 14, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.9, -0.15), fontsize=22, ncol=3) 

fig.savefig("GLUE_Timeseries_deox_C_hypo_initalcond_day_100years.png", dpi=300, bbox_inches='tight')






#%% MK test on onset C 80 years 

glue_df_C_ave_inital_cond_80years_rcp26=glue_df_C_ave_inital_cond_rcp26[glue_df_C_ave_inital_cond_rcp26.index>2019] 

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_80years_rcp26['50%'])
(0.0010930901912147009,
 'positively autocorrelated',
 'increasing',
 0.002048824548563699,
 0.0032757754218705713,
 12.297800028993818)

glue_df_C_ave_inital_cond_80years_rcp60=glue_df_C_ave_inital_cond_rcp60[glue_df_C_ave_inital_cond_rcp60.index>2019] 

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_80years_rcp60['50%'])
(0.0007313024618795072,
 'positively autocorrelated',
 'no trend',
 0.6093346175234022,
 0,
 0)



glue_df_C_ave_inital_cond_80years_rcp85=glue_df_C_ave_inital_cond_rcp85[glue_df_C_ave_inital_cond_rcp85.index>2019] 

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_80years_rcp85['50%'])
(0.0010080453761555249,
 'positively autocorrelated',
 'no trend',
 0.8436794050858154,
 0,
 0)

#%% plotting the C on inital condition day 80years

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_C_ave_inital_cond_80years_rcp26.index, glue_df_C_ave_inital_cond_80years_rcp26['5%'], glue_df_C_ave_inital_cond_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_80years_rcp26.index, glue_df_C_ave_inital_cond_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_80years_rcp26['50%'])
ax=plt.plot(glue_df_C_ave_inital_cond_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--')

ax= plt.text(2065, 10.5, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f},  p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )


ax=plt.fill_between(glue_df_C_ave_inital_cond_80years_rcp60.index, glue_df_C_ave_inital_cond_80years_rcp60['5%'], glue_df_C_ave_inital_cond_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_80years_rcp60.index, glue_df_C_ave_inital_cond_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )



ax=plt.fill_between(glue_df_C_ave_inital_cond_80years_rcp85.index, glue_df_C_ave_inital_cond_80years_rcp85['5%'], glue_df_C_ave_inital_cond_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_C_ave_inital_cond_80years_rcp85.index, glue_df_C_ave_inital_cond_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


ax=plt.ylabel('Hypolimnetic average DO on\n initial condition day [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(10, 14, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22, ncol=3) 

fig.savefig("GLUE_Timeseries_deox_C_hypo_initalcond_day_80years.png", dpi=300, bbox_inches='tight')












#%%Read the CSV file

#gfdl

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/his')
input_file_path = 'temp_prof_gfdl_his.csv'  # Replace with your actual input file path
temp_deox_gfdl_his = pd.read_csv(input_file_path)
temp_deox_2D_gfdl_his=temp_deox_gfdl_his.iloc[:, 1:].values
time_series_gfdl_his = pd.to_datetime(temp_deox_gfdl_his['Datetime'])
temp_hypo_deox_ave_gfdl_his=hypolimnetic_ave(temp_deox_2D_gfdl_his, hypo_morpho_vriables_gotm_grid[0], time_series_gfdl_his)
temp_hypo_deox_ave_annual_gfdl_his=temp_hypo_deox_ave_gfdl_his.groupby(temp_hypo_deox_ave_gfdl_his.index.year).mean()


#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp26')
input_file_path = 'temp_prof_gfdl_rcp26.csv'  # Replace with your actual input file path
temp_deox_gfdl_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_gfdl_rcp26=temp_deox_gfdl_rcp26.iloc[:, 1:].values
time_series_gfdl_rcp26 = pd.to_datetime(temp_deox_gfdl_rcp26['Datetime'])
temp_hypo_deox_ave_gfdl_rcp26=hypolimnetic_ave(temp_deox_2D_gfdl_rcp26, hypo_morpho_vriables_gotm_grid[0], time_series_gfdl_rcp26)
temp_hypo_deox_ave_annual_gfdl_rcp26=temp_hypo_deox_ave_gfdl_rcp26.groupby(temp_hypo_deox_ave_gfdl_rcp26.index.year).mean()

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp60')
input_file_path = 'temp_prof_gfdl_rcp60.csv'  # Replace with your actual input file path
temp_deox_gfdl_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_gfdl_rcp60=temp_deox_gfdl_rcp60.iloc[:, 1:].values
time_series_gfdl_rcp60 = pd.to_datetime(temp_deox_gfdl_rcp60['Datetime'])
temp_hypo_deox_ave_gfdl_rcp60=hypolimnetic_ave(temp_deox_2D_gfdl_rcp60, hypo_morpho_vriables_gotm_grid[0], time_series_gfdl_rcp60)
temp_hypo_deox_ave_annual_gfdl_rcp60=temp_hypo_deox_ave_gfdl_rcp60.groupby(temp_hypo_deox_ave_gfdl_rcp60.index.year).mean()

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/gfdl_senarios/rcp85')
input_file_path = 'temp_prof_gfdl_rcp85.csv'  # Replace with your actual input file path
temp_deox_gfdl_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_gfdl_rcp85=temp_deox_gfdl_rcp85.iloc[:, 1:].values
time_series_gfdl_rcp85 = pd.to_datetime(temp_deox_gfdl_rcp85['Datetime'])
temp_hypo_deox_ave_gfdl_rcp85=hypolimnetic_ave(temp_deox_2D_gfdl_rcp85, hypo_morpho_vriables_gotm_grid[0], time_series_gfdl_rcp85)
temp_hypo_deox_ave_annual_gfdl_rcp85=temp_hypo_deox_ave_gfdl_rcp85.groupby(temp_hypo_deox_ave_gfdl_rcp85.index.year).mean()



#hadgem

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/his')
input_file_path = 'temp_prof_hadgem_his.csv'  # Replace with your actual input file path
temp_deox_hadgem_his = pd.read_csv(input_file_path)
temp_deox_2D_hadgem_his=temp_deox_hadgem_his.iloc[:, 1:].values
time_series_hadgem_his = pd.to_datetime(temp_deox_hadgem_his['Datetime'])
temp_hypo_deox_ave_hadgem_his=hypolimnetic_ave(temp_deox_2D_hadgem_his, hypo_morpho_vriables_gotm_grid[0], time_series_hadgem_his)
temp_hypo_deox_ave_annual_hadgem_his=temp_hypo_deox_ave_hadgem_his.groupby(temp_hypo_deox_ave_hadgem_his.index.year).mean()


#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp26')
input_file_path = 'temp_prof_hadgem_rcp26.csv'  # Replace with your actual input file path
temp_deox_hadgem_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_hadgem_rcp26=temp_deox_hadgem_rcp26.iloc[:, 1:].values
time_series_hadgem_rcp26 = pd.to_datetime(temp_deox_hadgem_rcp26['Datetime'])
temp_hypo_deox_ave_hadgem_rcp26=hypolimnetic_ave(temp_deox_2D_hadgem_rcp26, hypo_morpho_vriables_gotm_grid[0], time_series_hadgem_rcp26)
temp_hypo_deox_ave_annual_hadgem_rcp26=temp_hypo_deox_ave_hadgem_rcp26.groupby(temp_hypo_deox_ave_hadgem_rcp26.index.year).mean()

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp60')
input_file_path = 'temp_prof_hadgem_rcp60.csv'  # Replace with your actual input file path
temp_deox_hadgem_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_hadgem_rcp60=temp_deox_hadgem_rcp60.iloc[:, 1:].values
time_series_hadgem_rcp60 = pd.to_datetime(temp_deox_hadgem_rcp60['Datetime'])
temp_hypo_deox_ave_hadgem_rcp60=hypolimnetic_ave(temp_deox_2D_hadgem_rcp60, hypo_morpho_vriables_gotm_grid[0], time_series_hadgem_rcp60)
temp_hypo_deox_ave_annual_hadgem_rcp60=temp_hypo_deox_ave_hadgem_rcp60.groupby(temp_hypo_deox_ave_hadgem_rcp60.index.year).mean()

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/hadgem_senarios/rcp85')
input_file_path = 'temp_prof_hadgem_rcp85.csv'  # Replace with your actual input file path
temp_deox_hadgem_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_hadgem_rcp85=temp_deox_hadgem_rcp85.iloc[:, 1:].values
time_series_hadgem_rcp85 = pd.to_datetime(temp_deox_hadgem_rcp85['Datetime'])
temp_hypo_deox_ave_hadgem_rcp85=hypolimnetic_ave(temp_deox_2D_hadgem_rcp85, hypo_morpho_vriables_gotm_grid[0], time_series_hadgem_rcp85)
temp_hypo_deox_ave_annual_hadgem_rcp85=temp_hypo_deox_ave_hadgem_rcp85.groupby(temp_hypo_deox_ave_hadgem_rcp85.index.year).mean()




#ipsl

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/his')
input_file_path = 'temp_prof_ipsl_his.csv'  # Replace with your actual input file path
temp_deox_ipsl_his = pd.read_csv(input_file_path)
temp_deox_2D_ipsl_his=temp_deox_ipsl_his.iloc[:, 1:].values
time_series_ipsl_his = pd.to_datetime(temp_deox_ipsl_his['Datetime'])
temp_hypo_deox_ave_ipsl_his=hypolimnetic_ave(temp_deox_2D_ipsl_his, hypo_morpho_vriables_gotm_grid[0], time_series_ipsl_his)
temp_hypo_deox_ave_annual_ipsl_his=temp_hypo_deox_ave_ipsl_his.groupby(temp_hypo_deox_ave_ipsl_his.index.year).mean()


#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp26')
input_file_path = 'temp_prof_ipsl_rcp26.csv'  # Replace with your actual input file path
temp_deox_ipsl_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_ipsl_rcp26=temp_deox_ipsl_rcp26.iloc[:, 1:].values
time_series_ipsl_rcp26 = pd.to_datetime(temp_deox_ipsl_rcp26['Datetime'])
temp_hypo_deox_ave_ipsl_rcp26=hypolimnetic_ave(temp_deox_2D_ipsl_rcp26, hypo_morpho_vriables_gotm_grid[0], time_series_ipsl_rcp26)
temp_hypo_deox_ave_annual_ipsl_rcp26=temp_hypo_deox_ave_ipsl_rcp26.groupby(temp_hypo_deox_ave_ipsl_rcp26.index.year).mean()

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp60')
input_file_path = 'temp_prof_ipsl_rcp60.csv'  # Replace with your actual input file path
temp_deox_ipsl_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_ipsl_rcp60=temp_deox_ipsl_rcp60.iloc[:, 1:].values
time_series_ipsl_rcp60 = pd.to_datetime(temp_deox_ipsl_rcp60['Datetime'])
temp_hypo_deox_ave_ipsl_rcp60=hypolimnetic_ave(temp_deox_2D_ipsl_rcp60, hypo_morpho_vriables_gotm_grid[0], time_series_ipsl_rcp60)
temp_hypo_deox_ave_annual_ipsl_rcp60=temp_hypo_deox_ave_ipsl_rcp60.groupby(temp_hypo_deox_ave_ipsl_rcp60.index.year).mean()

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/ipsl_senarios/rcp85')
input_file_path = 'temp_prof_ipsl_rcp85.csv'  # Replace with your actual input file path
temp_deox_ipsl_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_ipsl_rcp85=temp_deox_ipsl_rcp85.iloc[:, 1:].values
time_series_ipsl_rcp85 = pd.to_datetime(temp_deox_ipsl_rcp85['Datetime'])
temp_hypo_deox_ave_ipsl_rcp85=hypolimnetic_ave(temp_deox_2D_ipsl_rcp85, hypo_morpho_vriables_gotm_grid[0], time_series_ipsl_rcp85)
temp_hypo_deox_ave_annual_ipsl_rcp85=temp_hypo_deox_ave_ipsl_rcp85.groupby(temp_hypo_deox_ave_ipsl_rcp85.index.year).mean()



#miroc

#his:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/his')
input_file_path = 'temp_prof_miroc_his.csv'  # Replace with your actual input file path
temp_deox_miroc_his = pd.read_csv(input_file_path)
temp_deox_2D_miroc_his=temp_deox_miroc_his.iloc[:, 1:].values
time_series_miroc_his = pd.to_datetime(temp_deox_miroc_his['Datetime'])
temp_hypo_deox_ave_miroc_his=hypolimnetic_ave(temp_deox_2D_miroc_his, hypo_morpho_vriables_gotm_grid[0], time_series_miroc_his)
temp_hypo_deox_ave_annual_miroc_his=temp_hypo_deox_ave_miroc_his.groupby(temp_hypo_deox_ave_miroc_his.index.year).mean()


#rcp26
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp26')
input_file_path = 'temp_prof_miroc_rcp26.csv'  # Replace with your actual input file path
temp_deox_miroc_rcp26 = pd.read_csv(input_file_path)
temp_deox_2D_miroc_rcp26=temp_deox_miroc_rcp26.iloc[:, 1:].values
time_series_miroc_rcp26 = pd.to_datetime(temp_deox_miroc_rcp26['Datetime'])
temp_hypo_deox_ave_miroc_rcp26=hypolimnetic_ave(temp_deox_2D_miroc_rcp26, hypo_morpho_vriables_gotm_grid[0], time_series_miroc_rcp26)
temp_hypo_deox_ave_annual_miroc_rcp26=temp_hypo_deox_ave_miroc_rcp26.groupby(temp_hypo_deox_ave_miroc_rcp26.index.year).mean()

#rcp60
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp60')
input_file_path = 'temp_prof_miroc_rcp60.csv'  # Replace with your actual input file path
temp_deox_miroc_rcp60 = pd.read_csv(input_file_path)
temp_deox_2D_miroc_rcp60=temp_deox_miroc_rcp60.iloc[:, 1:].values
time_series_miroc_rcp60 = pd.to_datetime(temp_deox_miroc_rcp60['Datetime'])
temp_hypo_deox_ave_miroc_rcp60=hypolimnetic_ave(temp_deox_2D_miroc_rcp60, hypo_morpho_vriables_gotm_grid[0], time_series_miroc_rcp60)
temp_hypo_deox_ave_annual_miroc_rcp60=temp_hypo_deox_ave_miroc_rcp60.groupby(temp_hypo_deox_ave_miroc_rcp60.index.year).mean()

#rcp85
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/miroc_senarios/rcp85')
input_file_path = 'temp_prof_miroc_rcp85.csv'  # Replace with your actual input file path
temp_deox_miroc_rcp85 = pd.read_csv(input_file_path)
temp_deox_2D_miroc_rcp85=temp_deox_miroc_rcp85.iloc[:, 1:].values
time_series_miroc_rcp85 = pd.to_datetime(temp_deox_miroc_rcp85['Datetime'])
temp_hypo_deox_ave_miroc_rcp85=hypolimnetic_ave(temp_deox_2D_miroc_rcp85, hypo_morpho_vriables_gotm_grid[0], time_series_miroc_rcp85)
temp_hypo_deox_ave_annual_miroc_rcp85=temp_hypo_deox_ave_miroc_rcp85.groupby(temp_hypo_deox_ave_miroc_rcp85.index.year).mean()



#%%



temp_hypo_ave_TB_gfdl_rcp85=hypolimnetic_ave(temp_gfdl_rcp85_hypo_TB, hypo_morpho_vriables_gotm_grid[0], formatted_time_series_gfdl_rcp85)

temp_hypo_ave_TB_hadgem_rcp85=hypolimnetic_ave(temp_hadgem_rcp85_hypo_TB, hypo_morpho_vriables_gotm_grid[0], formatted_time_series_hadgem_rcp85)

temp_hypo_ave_TB_ipsl_rcp85=hypolimnetic_ave(temp_ipsl_rcp85_hypo_TB, hypo_morpho_vriables_gotm_grid[0], formatted_time_series_ipsl_rcp85)

temp_hypo_ave_TB_miroc_rcp85=hypolimnetic_ave(temp_miroc_rcp85_hypo_TB, hypo_morpho_vriables_gotm_grid[0], formatted_time_series_miroc_rcp85)





temp_hypo_ave_TB_gfdl_rcp85.loc['2020-05-22':'2020-07-02'].mean()#9.257142397947236
temp_hypo_ave_TB_gfdl_rcp85.loc['2021-05-13':'2021-07-15'].mean()#9.255425504161593
(9.257142397947236+9.255425504161593)/2 # 9.256283951054414


temp_hypo_ave_TB_hadgem_rcp85.loc['2020-05-22':'2020-07-02'].mean()#9.58953054638234
temp_hypo_ave_TB_hadgem_rcp85.loc['2021-05-13':'2021-07-15'].mean()#8.721022126772358
(9.58953054638234+8.721022126772358)/2 #9.155276336577348


temp_hypo_ave_TB_ipsl_rcp85.loc['2020-05-22':'2020-07-02'].mean()#9.574653159442057
temp_hypo_ave_TB_ipsl_rcp85.loc['2021-05-13':'2021-07-15'].mean()#9.720405884408894
(9.574653159442057+9.720405884408894)/2 #9.647529521925476


temp_hypo_ave_TB_miroc_rcp85.loc['2020-05-22':'2020-07-02'].mean()#8.962389347442032
temp_hypo_ave_TB_miroc_rcp85.loc['2021-05-13':'2021-07-15'].mean()#9.31535563682219
(8.962389347442032+9.31535563682219)/2 # 9.138872492132112


0.25*(9.256283951054414+9.155276336577348+9.647529521925476+9.138872492132112)#9.299490575422336




#%%4 models average 

#%%daily average 


temp_hypo_deox_ave_4models_his=0.25* (temp_hypo_deox_ave_gfdl_his+temp_hypo_deox_ave_hadgem_his+temp_hypo_deox_ave_ipsl_his +temp_hypo_deox_ave_miroc_his)

temp_hypo_deox_ave_4models_rcp26=0.25* (temp_hypo_deox_ave_gfdl_rcp26+temp_hypo_deox_ave_hadgem_rcp26+temp_hypo_deox_ave_ipsl_rcp26 +temp_hypo_deox_ave_miroc_rcp26)

temp_hypo_deox_ave_4models_rcp60=0.25* (temp_hypo_deox_ave_gfdl_rcp60+temp_hypo_deox_ave_hadgem_rcp60+temp_hypo_deox_ave_ipsl_rcp60 +temp_hypo_deox_ave_miroc_rcp60)

temp_hypo_deox_ave_4models_rcp85=0.25* (temp_hypo_deox_ave_gfdl_rcp85+temp_hypo_deox_ave_hadgem_rcp85+temp_hypo_deox_ave_ipsl_rcp85 +temp_hypo_deox_ave_miroc_rcp85)





#temp average in 2020 and 2021

temp_ave_hypo_2020_2021_rcp26=temp_hypo_deox_ave_4models_rcp26[(temp_hypo_deox_ave_4models_rcp26.index.year == 2020) | (temp_hypo_deox_ave_4models_rcp26.index.year == 2021)].mean()
# 11.143963749870672
temp_ave_hypo_2020_2021_rcp60=temp_hypo_deox_ave_4models_rcp60[(temp_hypo_deox_ave_4models_rcp60.index.year == 2020) | (temp_hypo_deox_ave_4models_rcp60.index.year == 2021)].mean()
# 10.002890681537313
temp_ave_hypo_2020_2021_rcp85= temp_hypo_deox_ave_4models_rcp85[(temp_hypo_deox_ave_4models_rcp85.index.year == 2020) | (temp_hypo_deox_ave_4models_rcp85.index.year == 2021)].mean()
# 10.217768779996623


#find the same time ave before first deep hypoxia

temp_hypo_deox_ave_4models_rcp26.loc['2020-05-22': '2020-07-02'].mean()#9.278189878600244

temp_hypo_deox_ave_4models_rcp60.loc['2020-05-22': '2020-07-02'].mean()#7.567294531409121

temp_hypo_deox_ave_4models_rcp85.loc['2020-05-22': '2020-07-02'].mean()#9.75305038882451


temp_hypo_deox_ave_4models_rcp26.loc['2021-05-13': '2021-07-15'].mean()#10.965559566411308

temp_hypo_deox_ave_4models_rcp60.loc['2021-05-13': '2021-07-15'].mean()#11.177947592921456

temp_hypo_deox_ave_4models_rcp85.loc['2021-05-13': '2021-07-15'].mean()#9.25305228804126





(temp_hypo_deox_ave_4models_rcp26.loc['2020-05-22': '2020-07-02'].mean()+temp_hypo_deox_ave_4models_rcp26.loc['2021-05-13': '2021-07-15'].mean())/2
#10.121874722505776


(temp_hypo_deox_ave_4models_rcp60.loc['2020-05-22': '2020-07-02'].mean()+temp_hypo_deox_ave_4models_rcp60.loc['2021-05-13': '2021-07-15'].mean())/2
#9.372621062165289

(temp_hypo_deox_ave_4models_rcp85.loc['2020-05-22': '2020-07-02'].mean()+temp_hypo_deox_ave_4models_rcp85.loc['2021-05-13': '2021-07-15'].mean())/2
#9.503051338432886


(temp_hypo_deox_ave_4models_rcp85.loc['2020-05-31': '2020-07-11'].mean()+temp_hypo_deox_ave_4models_rcp85.loc['2021-05-07':'2021-07-09'].mean())/2#.loc['2021-04-24': '2021-06-26'].mean())/2
# 9.254149206998132
#9.462567094680415










# First Jday with higher ave temp than ave of 2020 and 2021
firstdate_higher_ave_temp_4models_his=temp_hypo_deox_ave_4models_his[temp_hypo_deox_ave_4models_his > 10.52547].groupby(temp_hypo_deox_ave_4models_his[temp_hypo_deox_ave_4models_his > 10.52547].index.year).idxmin().dt.dayofyear

firstdate_higher_ave_temp_4models_rcp26=temp_hypo_deox_ave_4models_rcp26[temp_hypo_deox_ave_4models_rcp26 > 10.52547].groupby(temp_hypo_deox_ave_4models_rcp26[temp_hypo_deox_ave_4models_rcp26 > 10.52547].index.year).idxmin().dt.dayofyear

firstdate_higher_ave_temp_4models_rcp60=temp_hypo_deox_ave_4models_rcp60[temp_hypo_deox_ave_4models_rcp60 > 10.52547].groupby(temp_hypo_deox_ave_4models_rcp60[temp_hypo_deox_ave_4models_rcp60 > 10.52547].index.year).idxmin().dt.dayofyear

firstdate_higher_ave_temp_4models_rcp85=temp_hypo_deox_ave_4models_rcp85[temp_hypo_deox_ave_4models_rcp85 > 10.52547].groupby(temp_hypo_deox_ave_4models_rcp85[temp_hypo_deox_ave_4models_rcp85 > 10.52547].index.year).idxmin().dt.dayofyear


#Calculate the ave temp hypo in 2020 and 2021 from rcps senarios:
 
temp_2years_4models_his=temp_hypo_deox_ave_4models_his[(temp_hypo_deox_ave_4models_his.index == 2020) | (temp_hypo_deox_ave_4models_his.index == 2021)]
temp_2years_4models_rcp26=temp_hypo_deox_ave_4models_rcp26[(temp_hypo_deox_ave_4models_rcp26.index == 2020) | (temp_hypo_deox_ave_4models_rcp26.index == 2021)]
temp_2years_4models_rcp60=temp_hypo_deox_ave_4models_rcp60[(temp_hypo_deox_ave_4models_rcp60.index == 2020) | (temp_hypo_deox_ave_4models_rcp60.index == 2021)]
temp_2years_4models_rcp85=temp_hypo_deox_ave_4models_rcp85[(temp_hypo_deox_ave_4models_rcp85.index == 2020) | (temp_hypo_deox_ave_4models_rcp85.index == 2021)]







"""
np.mean(firstdate_higher_ave_temp_4models_his[firstdate_higher_ave_temp_4models_his.index>1975])# 196.2
np.mean(firstdate_higher_ave_temp_4models_rcp26)#189.46
np.mean(firstdate_higher_ave_temp_4models_rcp60)#185.52
np.mean(firstdate_higher_ave_temp_4models_rcp85)#181.223

"""

#annual average 

temp_hypo_deox_ave_annual_4models_his=(temp_hypo_deox_ave_annual_gfdl_his+temp_hypo_deox_ave_annual_hadgem_his+temp_hypo_deox_ave_annual_ipsl_his+temp_hypo_deox_ave_annual_miroc_his)/4
temp_hypo_deox_ave_annual_4models_rcp26=(temp_hypo_deox_ave_annual_gfdl_rcp26+temp_hypo_deox_ave_annual_hadgem_rcp26+temp_hypo_deox_ave_annual_ipsl_rcp26+temp_hypo_deox_ave_annual_miroc_rcp26)/4
temp_hypo_deox_ave_annual_4models_rcp60=(temp_hypo_deox_ave_annual_gfdl_rcp60+temp_hypo_deox_ave_annual_hadgem_rcp60+temp_hypo_deox_ave_annual_ipsl_rcp60+temp_hypo_deox_ave_annual_miroc_rcp60)/4
temp_hypo_deox_ave_annual_4models_rcp85=(temp_hypo_deox_ave_annual_gfdl_rcp85+temp_hypo_deox_ave_annual_hadgem_rcp85+temp_hypo_deox_ave_annual_ipsl_rcp85+temp_hypo_deox_ave_annual_miroc_rcp85)/4


# Plot mean data

plt.figure(figsize=(15, 10))  


plt.plot(temp_hypo_deox_ave_annual_4models_his[temp_hypo_deox_ave_annual_4models_his.index>1975], label='His', color='grey')#marker='o',
plt.plot(temp_hypo_deox_ave_annual_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(temp_hypo_deox_ave_annual_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(temp_hypo_deox_ave_annual_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines
trendline_his = np.polyfit(temp_hypo_deox_ave_annual_4models_his[temp_hypo_deox_ave_annual_4models_his.index>1975].index, temp_hypo_deox_ave_annual_4models_his[temp_hypo_deox_ave_annual_4models_his.index>1975], 1)
trendline_values_his = np.polyval(trendline_his, temp_hypo_deox_ave_annual_4models_his[temp_hypo_deox_ave_annual_4models_his.index>1975].index)
plt.plot(temp_hypo_deox_ave_annual_4models_his[temp_hypo_deox_ave_annual_4models_his.index>1975].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 9, f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='grey')
trendline_his[0]
#-0.014019445756573861


trendline_rcp26 = np.polyfit(temp_hypo_deox_ave_annual_4models_rcp26.index, temp_hypo_deox_ave_annual_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, temp_hypo_deox_ave_annual_4models_rcp26.index)
plt.plot(temp_hypo_deox_ave_annual_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 8.75, f'y = {trendline_rcp26[0]:.3f}x + {trendline_rcp26[1]:.2f}', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(temp_hypo_deox_ave_annual_4models_rcp60.index, temp_hypo_deox_ave_annual_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, temp_hypo_deox_ave_annual_4models_rcp60.index)
plt.plot(temp_hypo_deox_ave_annual_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 8.5, f'y = {trendline_rcp60[0]:.3f}x + {trendline_rcp60[1]:.2f}', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(temp_hypo_deox_ave_annual_4models_rcp85.index, temp_hypo_deox_ave_annual_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, temp_hypo_deox_ave_annual_4models_rcp85.index)
plt.plot(temp_hypo_deox_ave_annual_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 8.25, f'y = {trendline_rcp85[0]:.3f}x + {trendline_rcp85[1]:.2f}', color='r')
trendline_rcp85[0]
#-0.22818336162987937



# Set the y-axis limits with an interval of 25
y_ticks = np.arange(7, 13, 0.5)
plt.yticks(y_ticks)

plt.ylabel('Hypolimnetic average temperature in deox period [°C]')
#plt.xlabel('Year')
plt.legend(loc='lower left')

plt.savefig("allsenarios_mean_hypolimnetic_ave_annual_temp_trendline_30lastyears.png", dpi=300)


#%%glue 4 models:
    
  
 
#his
all_temp_hypo_deox_ave_annual_4models_his=pd.concat([temp_hypo_deox_ave_annual_gfdl_his, temp_hypo_deox_ave_annual_hadgem_his, temp_hypo_deox_ave_annual_ipsl_his, temp_hypo_deox_ave_annual_miroc_his], axis=1)



#glue_df_temp_hypo_deox_ave_annual_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_hypo_deox_ave_annual_4models_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_hypo_deox_ave_annual_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_hypo_deox_ave_annual_his= glue_df_temp_hypo_deox_ave_annual_his.set_index(all_temp_hypo_deox_ave_annual_4models_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_hypo_deox_ave_annual_his.csv'

glue_df_temp_hypo_deox_ave_annual_his.to_csv(file_path )  









   
#rcp26
all_temp_hypo_deox_ave_annual_4models_rcp26=pd.concat([temp_hypo_deox_ave_annual_gfdl_rcp26, temp_hypo_deox_ave_annual_hadgem_rcp26, temp_hypo_deox_ave_annual_ipsl_rcp26, temp_hypo_deox_ave_annual_miroc_rcp26], axis=1)



all_temp_hypo_deox_ave_annual_4models_rcp26_80years= all_temp_hypo_deox_ave_annual_4models_rcp26[all_temp_hypo_deox_ave_annual_4models_rcp26.index>2019]


#gfdl
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp26_80years[0])
(0.02922272262043528,
 'positively autocorrelated',
 'no trend',
 0.15017031507230683,
 0,
 0)
#hadgem
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp26_80years[1])
(0.020343525059440287,
 'positively autocorrelated',
 'no trend',
 0.574734149515209,
 0,
 0)
#ipsl
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp26_80years[2])
(0.021384299460391974,
 'positively autocorrelated',
 'no trend',
 0.3126951334776096,
 0,
 0)
#miroc
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp26_80years[3])
(0.01862430774312095,
 'positively autocorrelated',
 'no trend',
 0.8127997263431497,
 0,
 0)


#glue_df_temp_hypo_deox_ave_annual_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_hypo_deox_ave_annual_4models_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_hypo_deox_ave_annual_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_hypo_deox_ave_annual_rcp26= glue_df_temp_hypo_deox_ave_annual_rcp26.set_index(all_temp_hypo_deox_ave_annual_4models_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_hypo_deox_ave_annual_rcp26.csv'

glue_df_temp_hypo_deox_ave_annual_rcp26.to_csv(file_path )    
    
  
    
    
#rcp60
all_temp_hypo_deox_ave_annual_4models_rcp60=pd.concat([temp_hypo_deox_ave_annual_gfdl_rcp60, temp_hypo_deox_ave_annual_hadgem_rcp60, temp_hypo_deox_ave_annual_ipsl_rcp60, temp_hypo_deox_ave_annual_miroc_rcp60], axis=1)


all_temp_hypo_deox_ave_annual_4models_rcp60_80years= all_temp_hypo_deox_ave_annual_4models_rcp60[all_temp_hypo_deox_ave_annual_4models_rcp60.index>2019]


#gfdl
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp60_80years[0])
(0.022247177256186274,
 'positively autocorrelated',
 'no trend',
 0.2924761478136211,
 0,
 0)
#hadgem
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp60_80years[1])
(0.018066519078417182,
 'positively autocorrelated',
 'no trend',
 0.19220916108196096,
 0,
 0)
#ipsl
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp60_80years[2])
(0.02830889792258025,
 'positively autocorrelated',
 'no trend',
 0.7490373105270323,
 0,
 0)
#miroc
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp60_80years[3])
(0.02542418840771152,
 'positively autocorrelated',
 'no trend',
 0.12246792821023589,
 0,
 0)








#glue_df_temp_hypo_deox_ave_annual_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_hypo_deox_ave_annual_4models_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_hypo_deox_ave_annual_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_hypo_deox_ave_annual_rcp60= glue_df_temp_hypo_deox_ave_annual_rcp60.set_index(all_temp_hypo_deox_ave_annual_4models_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_hypo_deox_ave_annual_rcp60.csv'

glue_df_temp_hypo_deox_ave_annual_rcp60.to_csv(file_path )   
    
    
    
    
    
    
    
    
    
#rcp85
all_temp_hypo_deox_ave_annual_4models_rcp85=pd.concat([temp_hypo_deox_ave_annual_gfdl_rcp85, temp_hypo_deox_ave_annual_hadgem_rcp85, temp_hypo_deox_ave_annual_ipsl_rcp85, temp_hypo_deox_ave_annual_miroc_rcp85], axis=1)

all_temp_hypo_deox_ave_annual_4models_rcp85_80years= all_temp_hypo_deox_ave_annual_4models_rcp85[all_temp_hypo_deox_ave_annual_4models_rcp85.index>2019]


#gfdl
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp85_80years[0])
(0.02488163791204312,
 'positively autocorrelated',
 'no trend',
 0.2924125948449072,
 0,
 0)
#hadgem
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp85_80years[1])

(0.012975989654225266,
 'positively autocorrelated',
 'no trend',
 0.06497629443849484,
 0,
 0)
#ipsl
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp85_80years[2])
(0.0252454557421748,
 'positively autocorrelated',
 'increasing',
 0.003492149272987355,
 0.019631832363420573,
 10.224365197293318)
#miroc
autocorr_MK_org_modif_sens_slope_test(all_temp_hypo_deox_ave_annual_4models_rcp85_80years[3])
(0.010960483771142676,
 'positively autocorrelated',
 'no trend',
 0.3806855907019999,
 0,
 0)


#glue_df_temp_hypo_deox_ave_annual_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_temp_hypo_deox_ave_annual_4models_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_temp_hypo_deox_ave_annual_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_temp_hypo_deox_ave_annual_rcp85= glue_df_temp_hypo_deox_ave_annual_rcp85.set_index(all_temp_hypo_deox_ave_annual_4models_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_temp_hypo_deox_ave_annual_rcp85.csv'

glue_df_temp_hypo_deox_ave_annual_rcp85.to_csv(file_path ) 



#%%


# 2020, 2021


temp_median_ave_2020_2021_rcp26= (np.array(glue_df_temp_hypo_deox_ave_annual_rcp26[glue_df_temp_hypo_deox_ave_annual_rcp26.index== 2020]['50%']) + np.array(glue_df_temp_hypo_deox_ave_annual_rcp26[glue_df_temp_hypo_deox_ave_annual_rcp26.index== 2021]['50%']))/2
#array([10.8753296])

temp_median_ave_2020_2021_rcp60= (np.array(glue_df_temp_hypo_deox_ave_annual_rcp60[glue_df_temp_hypo_deox_ave_annual_rcp60.index== 2020]['50%']) + np.array(glue_df_temp_hypo_deox_ave_annual_rcp60[glue_df_temp_hypo_deox_ave_annual_rcp60.index== 2021]['50%']))/2
#array([9.60141506])

temp_median_ave_2020_2021_rcp85= (np.array(glue_df_temp_hypo_deox_ave_annual_rcp85[glue_df_temp_hypo_deox_ave_annual_rcp85.index== 2020]['50%']) + np.array(glue_df_temp_hypo_deox_ave_annual_rcp85[glue_df_temp_hypo_deox_ave_annual_rcp85.index== 2021]['50%']))/2
#array([10.40467467])


#First 10 years from 2020 [2020-2030]

np.mean(glue_df_temp_hypo_deox_ave_annual_rcp26[(glue_df_temp_hypo_deox_ave_annual_rcp26.index >2019) & (glue_df_temp_hypo_deox_ave_annual_rcp26.index<2030)]['50%'])
#10.447882416112016

np.mean(glue_df_temp_hypo_deox_ave_annual_rcp60[(glue_df_temp_hypo_deox_ave_annual_rcp60.index >2019) & (glue_df_temp_hypo_deox_ave_annual_rcp60.index<2030)]['50%'])
#10.042853480093452

np.mean(glue_df_temp_hypo_deox_ave_annual_rcp85[(glue_df_temp_hypo_deox_ave_annual_rcp85.index >2019) & (glue_df_temp_hypo_deox_ave_annual_rcp85.index<2030)]['50%'])
#10.554501751187365

#Last 10 years of each rcps [2090-2099]


np.mean(glue_df_temp_hypo_deox_ave_annual_rcp26[glue_df_temp_hypo_deox_ave_annual_rcp26.index>2089]['50%'])
#10.255518954463678

np.mean(glue_df_temp_hypo_deox_ave_annual_rcp60[glue_df_temp_hypo_deox_ave_annual_rcp60.index>2089]['50%'])
#10.444091404723286

np.mean(glue_df_temp_hypo_deox_ave_annual_rcp85[glue_df_temp_hypo_deox_ave_annual_rcp85.index>2089]['50%'])
# 11.10752051110289



#%%80 years glue method cut from 2020

glue_df_temp_hypo_deox_ave_annual_80years_rcp26= glue_df_temp_hypo_deox_ave_annual_rcp26[glue_df_temp_hypo_deox_ave_annual_rcp26.index>2019]
#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_80years_rcp26['50%'])
(0.006976032159904319,
 'positively autocorrelated',
 'no trend',
 0.5088744343515299,
 0,
 0)

glue_df_temp_hypo_deox_ave_annual_80years_rcp60= glue_df_temp_hypo_deox_ave_annual_rcp60[glue_df_temp_hypo_deox_ave_annual_rcp60.index>2019]
#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_80years_rcp60['50%'])
(0.004609894081441866,
 'positively autocorrelated',
 'no trend',
 0.08698224793375631,
 0,
 0)

glue_df_temp_hypo_deox_ave_annual_80years_rcp85= glue_df_temp_hypo_deox_ave_annual_rcp85[glue_df_temp_hypo_deox_ave_annual_rcp85.index>2019]
#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_80years_rcp85['50%'])
(0.006549647882369905,
 'positively autocorrelated',
 'increasing',
 0.029788714455492027,
 0.00745940389570332,
 10.356474294251887)


#%%plotting the glue 80 years of ave temp hypo

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for80years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_temp_hypo_deox_ave_annual_80years_rcp26.index, glue_df_temp_hypo_deox_ave_annual_80years_rcp26['5%'], glue_df_temp_hypo_deox_ave_annual_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_temp_hypo_deox_ave_annual_80years_rcp26.index, glue_df_temp_hypo_deox_ave_annual_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_80years_rcp26['50%'])


ax=plt.fill_between(glue_df_temp_hypo_deox_ave_annual_80years_rcp60.index, glue_df_temp_hypo_deox_ave_annual_80years_rcp60['5%'], glue_df_temp_hypo_deox_ave_annual_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_temp_hypo_deox_ave_annual_80years_rcp60.index, glue_df_temp_hypo_deox_ave_annual_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_80years_rcp60['50%'])
#ax=plt.text(2060, 15, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.05', color='gold', fontsize= 20 )




ax=plt.fill_between(glue_df_temp_hypo_deox_ave_annual_80years_rcp85.index, glue_df_temp_hypo_deox_ave_annual_80years_rcp85['5%'], glue_df_temp_hypo_deox_ave_annual_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_temp_hypo_deox_ave_annual_80years_rcp85.index, glue_df_temp_hypo_deox_ave_annual_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_80years_rcp85['50%'])
ax=plt.plot(glue_df_temp_hypo_deox_ave_annual_80years_rcp85.index,trendline_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--')
ax = plt.text(2060, 14.7, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.05', color='r', fontsize=20)


ax=plt.ylabel('Hypolimnetic average temperature in deoxygenation period [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(8, 16, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22) 

fig.savefig("GLUE_Ttemp_hypo_deox_ave_annual_80years.png", dpi=300, bbox_inches='tight')



#%%
#estimation of trendline for hypo_temp_deoxygenation:
    
2020: 10.356    
2021: 10.356+0.007=10.363

2020, 2021:0.5*(10.356+10.363)=10.3595


   
    
#%%100years glue method RCPs 



glue_df_temp_hypo_deox_ave_annual_100years_rcp26=pd.concat([glue_df_temp_hypo_deox_ave_annual_his[glue_df_temp_hypo_deox_ave_annual_his.index>1999] , glue_df_temp_hypo_deox_ave_annual_rcp26])

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_100years_rcp26['50%'])
(0.00658670287560712,
 'positively autocorrelated',
 'no trend',
 0.06103587777059016,
 0.004066354365771813,
 9.954196401132233)

"""
glue_df_temp_hypo_deox_ave_annual_whole_rcp26=pd.concat([glue_df_temp_hypo_deox_ave_annual_his , glue_df_temp_hypo_deox_ave_annual_rcp26])
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_whole_rcp26['50%'])
(0.006592462032638861,
 'positively autocorrelated',
 'no trend',
 0.46066702911117163,
 -0.00044922908380796886,
 10.233627430284397)


autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_rcp26['50%'])
(0.006463213058262786,
 'positively autocorrelated',
 'no trend',
 0.43693905240401065,
 0.0017506407924237845,
 10.096504538151954)

"""



glue_df_temp_hypo_deox_ave_annual_100years_rcp60=pd.concat([glue_df_temp_hypo_deox_ave_annual_his[glue_df_temp_hypo_deox_ave_annual_his.index>1999] , glue_df_temp_hypo_deox_ave_annual_rcp60])

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_100years_rcp60['50%'])

(0.004947316776583001,
 'positively autocorrelated',
 'increasing',
 0.00916460011882747,
 0.006019773217516849,
 10.068015910706942)




glue_df_temp_hypo_deox_ave_annual_100years_rcp85=pd.concat([glue_df_temp_hypo_deox_ave_annual_his[glue_df_temp_hypo_deox_ave_annual_his.index>1999] , glue_df_temp_hypo_deox_ave_annual_rcp85])

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_100years_rcp85['50%'])

(0.006653446110794187,
 'positively autocorrelated',
 'increasing',
 1.0408652912907712e-06,
 0.009602610790596678,
 10.048547781686166)

#%%plotting the glue 100 years of ave temp hypo


os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for100years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_temp_hypo_deox_ave_annual_100years_rcp26.index, glue_df_temp_hypo_deox_ave_annual_100years_rcp26['5%'], glue_df_temp_hypo_deox_ave_annual_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_temp_hypo_deox_ave_annual_100years_rcp26.index, glue_df_temp_hypo_deox_ave_annual_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_100years_rcp26['50%'])


ax=plt.fill_between(glue_df_temp_hypo_deox_ave_annual_100years_rcp60.index, glue_df_temp_hypo_deox_ave_annual_100years_rcp60['5%'], glue_df_temp_hypo_deox_ave_annual_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_temp_hypo_deox_ave_annual_100years_rcp60.index, glue_df_temp_hypo_deox_ave_annual_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_100years_rcp60['50%'])
ax=plt.text(2000, 15, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.05', color='gold', fontsize= 20 )




ax=plt.fill_between(glue_df_temp_hypo_deox_ave_annual_100years_rcp85.index, glue_df_temp_hypo_deox_ave_annual_100years_rcp85['5%'], glue_df_temp_hypo_deox_ave_annual_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_temp_hypo_deox_ave_annual_100years_rcp85.index, glue_df_temp_hypo_deox_ave_annual_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_temp_hypo_deox_ave_annual_100years_rcp85['50%'])
ax = plt.text(2000, 14.7, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.05', color='r', fontsize=20)


ax=plt.ylabel('Hypolimnetic average temperature in deoxygenation period [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(8, 16, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22) 

fig.savefig("GLUE_Ttemp_hypo_deox_ave_annual_100years.png", dpi=300, bbox_inches='tight')




#%%

def k_temp(temp , jz=0.49):
    
    return(1.087**(temp-20))


glue_df_Jz_ave_annual_100years_rcp26=glue_df_temp_hypo_deox_ave_annual_100years_rcp26.apply(k_temp)

glue_df_Jz_ave_annual_100years_rcp60=glue_df_temp_hypo_deox_ave_annual_100years_rcp60.apply(k_temp)

glue_df_Jz_ave_annual_100years_rcp85=glue_df_temp_hypo_deox_ave_annual_100years_rcp85.apply(k_temp)


os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for100years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_Jz_ave_annual_100years_rcp26.index, glue_df_Jz_ave_annual_100years_rcp26['5%'], glue_df_Jz_ave_annual_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_Jz_ave_annual_100years_rcp26.index, glue_df_Jz_ave_annual_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_Jz_ave_annual_100years_rcp26['50%'])


ax=plt.fill_between(glue_df_Jz_ave_annual_100years_rcp60.index, glue_df_Jz_ave_annual_100years_rcp60['5%'], glue_df_Jz_ave_annual_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_Jz_ave_annual_100years_rcp60.index, glue_df_Jz_ave_annual_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_Jz_ave_annual_100years_rcp60['50%'])
ax=plt.text(2000, 0.68, f'y = {trendline_rcp60[-2]:.5f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.05', color='gold', fontsize= 20 )




ax=plt.fill_between(glue_df_Jz_ave_annual_100years_rcp85.index, glue_df_Jz_ave_annual_100years_rcp85['5%'], glue_df_Jz_ave_annual_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_Jz_ave_annual_100years_rcp85.index, glue_df_Jz_ave_annual_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_Jz_ave_annual_100years_rcp85['50%'])
ax = plt.text(2000, 0.65, f'y = {trendline_rcp85[-2]:.5f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.05', color='r', fontsize=20)


ax=plt.ylabel('Modified average Jz [g m$^{-3}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(0.3, 0.7, 0.1) , fontsize= 22)
ax=plt.xticks( fontsize=22)#rotation=45 ,
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22) 

fig.savefig("GLUE_modified_jz_ave_annual_100years.png", dpi=300, bbox_inches='tight')









#%%

"""
['end_dates_Jday']
"""
def end_dates_Jday (df_deox):
    start_jday=start_dates_Jday (df_deox)
    deox_dur=annual_deox_duarion (df_deox)
    end_jday=start_jday+ deox_dur
    return (end_jday)


#%%his 

offset_jday_gfdl_his=end_dates_Jday(df_deox_period_surf_gfdl_his)
offset_jday_hadgem_his=end_dates_Jday(df_deox_period_surf_hadgem_his)
offset_jday_ipsl_his=end_dates_Jday(df_deox_period_surf_ipsl_his)
offset_jday_miroc_his=end_dates_Jday(df_deox_period_surf_miroc_his)


offset_jday_allgcms_his=pd.concat([offset_jday_gfdl_his, offset_jday_hadgem_his, offset_jday_ipsl_his , offset_jday_miroc_his], axis=0)

offset_jday_4models_his=(offset_jday_gfdl_his+ offset_jday_hadgem_his+ offset_jday_ipsl_his+ offset_jday_miroc_his)/4

all_offset_jday_4models_his=pd.concat([offset_jday_gfdl_his, offset_jday_hadgem_his, offset_jday_ipsl_his, offset_jday_miroc_his], axis=1)


#glue_df_offset_jday_4models_his
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_offset_jday_4models_his.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_offset_jday_4models_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_offset_jday_4models_his= glue_df_offset_jday_4models_his.set_index(all_offset_jday_4models_his.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_offset_jday_4models_his.csv'

glue_df_offset_jday_4models_his.to_csv(file_path ) 
#%%rcp26 

offset_jday_gfdl_rcp26=end_dates_Jday(df_deox_period_surf_gfdl_rcp26)
offset_jday_hadgem_rcp26=end_dates_Jday(df_deox_period_surf_hadgem_rcp26)
offset_jday_ipsl_rcp26=end_dates_Jday(df_deox_period_surf_ipsl_rcp26)
offset_jday_miroc_rcp26=end_dates_Jday(df_deox_period_surf_miroc_rcp26)

offset_jday_allgcms_rcp26=pd.concat([offset_jday_gfdl_rcp26, offset_jday_hadgem_rcp26, offset_jday_ipsl_rcp26 , offset_jday_miroc_rcp26], axis=0)

offset_jday_4models_rcp26=(offset_jday_gfdl_rcp26+ offset_jday_hadgem_rcp26+ offset_jday_ipsl_rcp26+ offset_jday_miroc_rcp26)/4

all_offset_jday_4models_rcp26=pd.concat([offset_jday_gfdl_rcp26, offset_jday_hadgem_rcp26, offset_jday_ipsl_rcp26, offset_jday_miroc_rcp26], axis=1)


#glue_df_offset_jday_4models_rcp26
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_offset_jday_4models_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_offset_jday_4models_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_offset_jday_4models_rcp26= glue_df_offset_jday_4models_rcp26.set_index(all_offset_jday_4models_rcp26.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_offset_jday_4models_rcp26.csv'

glue_df_offset_jday_4models_rcp26.to_csv(file_path ) 

#%%rcp60 

offset_jday_gfdl_rcp60=end_dates_Jday(df_deox_period_surf_gfdl_rcp60)
offset_jday_hadgem_rcp60=end_dates_Jday(df_deox_period_surf_hadgem_rcp60)
offset_jday_ipsl_rcp60=end_dates_Jday(df_deox_period_surf_ipsl_rcp60)
offset_jday_miroc_rcp60=end_dates_Jday(df_deox_period_surf_miroc_rcp60)

offset_jday_allgcms_rcp60=pd.concat([offset_jday_gfdl_rcp60, offset_jday_hadgem_rcp60, offset_jday_ipsl_rcp60 , offset_jday_miroc_rcp60], axis=0)


offset_jday_4models_rcp60=(offset_jday_gfdl_rcp60+ offset_jday_hadgem_rcp60+ offset_jday_ipsl_rcp60+ offset_jday_miroc_rcp60)/4

all_offset_jday_4models_rcp60=pd.concat([offset_jday_gfdl_rcp60, offset_jday_hadgem_rcp60, offset_jday_ipsl_rcp60, offset_jday_miroc_rcp60], axis=1)


#glue_df_offset_jday_4models_rcp60
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_offset_jday_4models_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_offset_jday_4models_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_offset_jday_4models_rcp60= glue_df_offset_jday_4models_rcp60.set_index(all_offset_jday_4models_rcp60.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_offset_jday_4models_rcp60.csv'

glue_df_offset_jday_4models_rcp60.to_csv(file_path ) 


#%%rcp85 

offset_jday_gfdl_rcp85=end_dates_Jday(df_deox_period_surf_gfdl_rcp85)
offset_jday_hadgem_rcp85=end_dates_Jday(df_deox_period_surf_hadgem_rcp85)
offset_jday_ipsl_rcp85=end_dates_Jday(df_deox_period_surf_ipsl_rcp85)
offset_jday_miroc_rcp85=end_dates_Jday(df_deox_period_surf_miroc_rcp85)

offset_jday_allgcms_rcp85=pd.concat([offset_jday_gfdl_rcp85, offset_jday_hadgem_rcp85, offset_jday_ipsl_rcp85 , offset_jday_miroc_rcp85], axis=0)

offset_jday_4models_rcp85=(offset_jday_gfdl_rcp85+ offset_jday_hadgem_rcp85+ offset_jday_ipsl_rcp85+ offset_jday_miroc_rcp85)/4
all_offset_jday_4models_rcp85=pd.concat([offset_jday_gfdl_rcp85, offset_jday_hadgem_rcp85, offset_jday_ipsl_rcp85, offset_jday_miroc_rcp85], axis=1)


#glue_df_offset_jday_4models_rcp85
# weighted_quantilesdataframe
quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_offset_jday_4models_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=None))

    # Build df
    glue_df_offset_jday_4models_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_offset_jday_4models_rcp85= glue_df_offset_jday_4models_rcp85.set_index(all_offset_jday_4models_rcp85.index)


# saving the results of glue method using the same weighting in GCMs 

file_path = 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther/glue_df_offset_jday_4models_rcp85.csv'

glue_df_offset_jday_4models_rcp85.to_csv(file_path )   


#%%



offset_jday_gfdl_his.max()#261
offset_jday_hadgem_his.max()#257
offset_jday_ipsl_his.max()#265
offset_jday_miroc_his.max()#259


offset_jday_gfdl_rcp26.max()#261
offset_jday_hadgem_rcp26.max()#271
offset_jday_ipsl_rcp26.max()#267
offset_jday_miroc_rcp26.max()#270


offset_jday_gfdl_rcp60.max()#260
offset_jday_hadgem_rcp60.max()#277+
offset_jday_ipsl_rcp60.max()#268
offset_jday_miroc_rcp60.max()#266



offset_jday_gfdl_rcp85.max()#257
offset_jday_hadgem_rcp85.max()#281+
offset_jday_ipsl_rcp85.max()#281+
offset_jday_miroc_rcp85.max()#272

#min

offset_jday_gfdl_his.min()#230
offset_jday_hadgem_his.min()#223
offset_jday_ipsl_his.min()#210
offset_jday_miroc_his.min()#210


offset_jday_gfdl_rcp26.min()#229
offset_jday_hadgem_rcp26.min()#229
offset_jday_ipsl_rcp26.min()#228
offset_jday_miroc_rcp26.min()#227


offset_jday_gfdl_rcp60.min()#220
offset_jday_hadgem_rcp60.min()#230
offset_jday_ipsl_rcp60.min()#232
offset_jday_miroc_rcp60.min()#233



offset_jday_gfdl_rcp85.min()#209
offset_jday_hadgem_rcp85.min()#237
offset_jday_ipsl_rcp85.min()#228
offset_jday_miroc_rcp85.min()#222








#%%100 years RCPs 


glue_df_offset_jday_4models_100years_rcp26=pd.concat([glue_df_offset_jday_4models_his[glue_df_offset_jday_4models_his.index>1999] , glue_df_offset_jday_4models_rcp26])

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp26['50%'])

(0.0005459550833601071,
 'positively autocorrelated',
 'no trend',
 0.42604124294008416,
 0.013888888888888888,
 247.3125)




glue_df_offset_jday_4models_100years_rcp60=pd.concat([glue_df_offset_jday_4models_his[glue_df_offset_jday_4models_his.index>1999] , glue_df_offset_jday_4models_rcp60])

#RCP60
autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp60['50%'])
(0.0004873267207665509,
 'positively autocorrelated',
 'increasing',
 0.0010374255448084568,
 0.07775414240931483,
 244.6511699507389)




glue_df_offset_jday_4models_100years_rcp85=pd.concat([glue_df_offset_jday_4models_his[glue_df_offset_jday_4models_his.index>1999] , glue_df_offset_jday_4models_rcp85])

#RCP85
autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp85['50%'])

(0.0006914874244109819,
 'positively autocorrelated',
 'increasing',
 4.440892098500626e-16,
 0.171875,
 242.4921875)


#%% plotiing the glue of 100 years of offsets 
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for100years/')



fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_offset_jday_4models_100years_rcp26.index, glue_df_offset_jday_4models_100years_rcp26['5%'], glue_df_offset_jday_4models_100years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_offset_jday_4models_100years_rcp26.index, glue_df_offset_jday_4models_100years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp26['50%'])


ax=plt.fill_between(glue_df_offset_jday_4models_100years_rcp60.index, glue_df_offset_jday_4models_100years_rcp60['5%'], glue_df_offset_jday_4models_100years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_offset_jday_4models_100years_rcp60.index, glue_df_offset_jday_4models_100years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp60['50%'])
ax=plt.text(2000, 210, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value = {trendline_rcp60[-3]:.3f}', color='orange', fontsize= 20 )
x_values = np.arange(len(glue_df_offset_jday_4models_100years_rcp60.index))
y_values = trendline_rcp60[-2] * x_values + trendline_rcp60[-1]

ax = plt.plot(glue_df_offset_jday_4models_100years_rcp60.index, y_values, label='RCP6.0 trendline', linewidth=2, linestyle='--', color='orange')


ax=plt.fill_between(glue_df_offset_jday_4models_100years_rcp85.index, glue_df_offset_jday_4models_100years_rcp85['5%'], glue_df_offset_jday_4models_100years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_offset_jday_4models_100years_rcp85.index, glue_df_offset_jday_4models_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp85['50%'])
ax = plt.text(2000, 215, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize=20)
x_values = np.arange(len(glue_df_offset_jday_4models_100years_rcp85.index))
y_values = trendline_rcp85[-2] * x_values + trendline_rcp85[-1]

ax = plt.plot(glue_df_offset_jday_4models_100years_rcp85.index, y_values, label='RCP8.5 trendline', linewidth=2, linestyle='--', color='red')


# Create custom legend handles
handles_rcp26 = [
    Line2D([0], [0], color='green', linewidth=3, linestyle='-', label='RCP2.6 median'),
    Patch(facecolor='green', alpha=0.4, edgecolor='green', label='RCP2.6  90% CI'),
    Line2D([0], [0], color='white', linewidth=2, linestyle='--', label='')]

handles_rcp60 = [
    Line2D([0], [0], color='yellow', linewidth=3, linestyle='-', label='RCP6.0 median'),
    Patch(facecolor='yellow', alpha=0.4, edgecolor='yellow', label='RCP6.0  90% CI'),
    Line2D([0], [0], color='orange', linewidth=2, linestyle='--', label='RCP6.0 trendline')
]

handles_rcp85 = [
    Line2D([0], [0], color='r', linewidth=3, linestyle='-', label='RCP8.5 median'),
    Patch(facecolor='r', alpha=0.3, edgecolor='r', label='RCP8.5  90% CI'),
    Line2D([0], [0], color='red', linewidth=2, linestyle='--', label='RCP8.5 trendline')
]

# Combine all handles into a single list
all_handles = handles_rcp26 + handles_rcp60 + handles_rcp85

# Create a legend with  3 columns and the first column having  2 rows, and the second and third columns having  3 rows
plt.legend(handles=all_handles, ncol=3, bbox_to_anchor=(1, -0.15), fontsize=22)



ax=plt.ylabel('Deoxygenation period turnover date [Jd]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(210, 300, 10) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
 

fig.savefig("GLUE_offset_jday_annual_100years.png", dpi=300, bbox_inches='tight')


#%%80 yaers offset rcps slopes 

################################################rcp2.6
autocorr_MK_org_modif_sens_slope_test(offset_jday_gfdl_rcp26[offset_jday_gfdl_rcp26.index>2019])
"""
(0.0022505283600845376,
 'positively autocorrelated',
 'no trend',
 0.8809269374341957,
 0,
 0)
"""

autocorr_MK_org_modif_sens_slope_test(offset_jday_hadgem_rcp26[offset_jday_hadgem_rcp26.index>2019])
"""
(0.002314933202342765,
 'positively autocorrelated',
 'no trend',
 0.5741076022915221,
 0,
 0)

"""





autocorr_MK_org_modif_sens_slope_test(offset_jday_ipsl_rcp26[offset_jday_ipsl_rcp26.index>2019])

"""
(0.0036029237613539773,
 'positively autocorrelated',
 'no trend',
 0.05958767112647134,
 0,
 0)

"""


autocorr_MK_org_modif_sens_slope_test(offset_jday_miroc_rcp26[offset_jday_miroc_rcp26.index>2019])
"""
(0.002939072477575823,
 'positively autocorrelated',
 'no trend',
 0.9395803818551156,
 0,
 0)

"""

#################################################rcp6.0
autocorr_MK_org_modif_sens_slope_test(offset_jday_gfdl_rcp60[offset_jday_gfdl_rcp60.index>2019])
"""
(0.003138865131772607,
 'positively autocorrelated',
 'increasing',
 0.02631974800677961,
 0.09090909090909091,
 239.9090909090909)
"""




autocorr_MK_org_modif_sens_slope_test(offset_jday_hadgem_rcp60[offset_jday_hadgem_rcp60.index>2019])
"""
(0.0027370062753216753,
 'positively autocorrelated',
 'increasing',
 7.993605777301127e-15,
 0.1791044776119403,
 248.42537313432837)
"""



autocorr_MK_org_modif_sens_slope_test(offset_jday_ipsl_rcp60[offset_jday_ipsl_rcp60.index>2019])
"""
(0.0020091363120954427,
 'positively autocorrelated',
 'increasing',
 0.00014992476489350537,
 0.1297335203366059,
 246.37552594670407)
"""



autocorr_MK_org_modif_sens_slope_test(offset_jday_miroc_rcp60[offset_jday_miroc_rcp60.index>2019])
"""
(0.0016505344210009172,
 'positively autocorrelated',
 'increasing',
 0.00015424862014734586,
 0.11189358372456965,
 244.5802034428795)
"""


###################################################rcp8.5
autocorr_MK_org_modif_sens_slope_test(offset_jday_gfdl_rcp85[offset_jday_gfdl_rcp85.index>2019])

"""
(0.0031799230104325093,
 'positively autocorrelated',
 'increasing',
 1.6775876887642482e-07,
 0.22857142857142856,
 223.97142857142856)
"""

autocorr_MK_org_modif_sens_slope_test(offset_jday_hadgem_rcp85[offset_jday_hadgem_rcp85.index>2019])

"""
(0.0016909166900371361,
 'positively autocorrelated',
 'increasing',
 1.0949019468853294e-12,
 0.29912280701754385,
 244.68464912280703)
"""

autocorr_MK_org_modif_sens_slope_test(offset_jday_ipsl_rcp85[offset_jday_ipsl_rcp85.index>2019])

"""
(0.0027811853174075692,
 'positively autocorrelated',
 'increasing',
 0.00044841311231169634,
 0.17073170731707318,
 249.2560975609756)
"""

autocorr_MK_org_modif_sens_slope_test(offset_jday_miroc_rcp85[offset_jday_miroc_rcp85.index>2019])
"""
(0.0011865851283509447,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.20689655172413793,
 245.82758620689654)
"""




#%%80years RCPs 



glue_df_offset_jday_4models_80years_rcp26=glue_df_offset_jday_4models_rcp26[glue_df_offset_jday_4models_rcp26.index>2019]

#RCP26
autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_80years_rcp26['50%'])

Out[2837]: 
(0.0007799293472206301,
 'positively autocorrelated',
 'no trend',
 0.22234227064782752,
 0,
 0)


glue_df_offset_jday_4models_80years_rcp60=glue_df_offset_jday_4models_rcp60[glue_df_offset_jday_4models_rcp60.index>2019]

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_80years_rcp60['50%'])
(0.0004929985850105528,
 'positively autocorrelated',
 'increasing',
 1.1008462363903959e-08,
 0.14035087719298245,
 243.9561403508772)


glue_df_offset_jday_4models_80years_rcp85=glue_df_offset_jday_4models_rcp85[glue_df_offset_jday_4models_rcp85.index>2019]

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_80years_rcp85['50%'])
(0.0007586430808897881,
 'positively autocorrelated',
 'increasing',
 7.083000852503574e-12,
 0.21153846153846154,
 243.89423076923077)




#%% plotiing the glue of 80 years of offsets 




os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for80years/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_offset_jday_4models_80years_rcp26.index, glue_df_offset_jday_4models_80years_rcp26['5%'], glue_df_offset_jday_4models_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_offset_jday_4models_80years_rcp26.index, glue_df_offset_jday_4models_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_80years_rcp26['50%'])


ax=plt.fill_between(glue_df_offset_jday_4models_80years_rcp60.index, glue_df_offset_jday_4models_80years_rcp60['5%'], glue_df_offset_jday_4models_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_offset_jday_4models_80years_rcp60.index, glue_df_offset_jday_4models_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_80years_rcp60['50%'])
ax=plt.plot(glue_df_offset_jday_4models_80years_rcp60.index,trendline_rcp60[-2]*(np.arange(1,81))+trendline_rcp60[-1] ,color='gold',  linestyle='--')
ax=plt.text(2060, 210, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.0001', color='gold', fontsize= 20 )




ax=plt.fill_between(glue_df_offset_jday_4models_80years_rcp85.index, glue_df_offset_jday_4models_80years_rcp85['5%'], glue_df_offset_jday_4models_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_offset_jday_4models_80years_rcp85.index, glue_df_offset_jday_4models_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_80years_rcp85['50%'])
ax=plt.plot(glue_df_offset_jday_4models_80years_rcp85.index,trendline_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--')
ax = plt.text(2060, 215, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize=20)


ax=plt.ylabel('Deoxygenation period turnover date [Jd]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(210, 300, 10) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.15), fontsize=22, ncol=3) 

fig.savefig("GLUE_offset_jday_annual_80years.png", dpi=300, bbox_inches='tight')












#%% Visulazation onset andf offset Jday:
    
onset_jday_4models_his
onset_jday_4models_rcp26
onset_jday_4models_rcp60
onset_jday_4models_rcp85    
    
# Create a DataFrame with NaN values
df_onset_jday_4models =pd.concat([
    pd.Series(onset_jday_4models_his, name='His' ),
    pd.Series(onset_jday_4models_rcp26, name='RCP2.6'),
    pd.Series(onset_jday_4models_rcp60, name='RCP6.0' ),
    pd.Series(onset_jday_4models_rcp85, name='RCP8.5' )], axis=1)    
    

# Reset indexes of the Series
onset_jday_allgcms_his.reset_index(drop=True, inplace=True)
onset_jday_allgcms_rcp26.reset_index(drop=True, inplace=True)
onset_jday_allgcms_rcp60.reset_index(drop=True, inplace=True)
onset_jday_allgcms_rcp85.reset_index(drop=True, inplace=True)
    
df_onset_jday_allgcms =pd.concat([
    pd.Series(onset_jday_allgcms_his, name='His' ),
    pd.Series(onset_jday_allgcms_rcp26, name='RCP2.6'),
    pd.Series(onset_jday_allgcms_rcp60, name='RCP6.0' ),
    pd.Series(onset_jday_allgcms_rcp85, name='RCP8.5' )], axis=1)    
    

offset_jday_4models_his
offset_jday_4models_rcp26
offset_jday_4models_rcp60
offset_jday_4models_rcp85


# Create a DataFrame with NaN values
df_offset_jday_4models =pd.concat([
    pd.Series(offset_jday_4models_his, name='His' ),
    pd.Series(offset_jday_4models_rcp26, name='RCP2.6'),
    pd.Series(offset_jday_4models_rcp60, name='RCP6.0' ),
    pd.Series(offset_jday_4models_rcp85, name='RCP8.5' )], axis=1)



# Reset indexes of the Series
offset_jday_allgcms_his.reset_index(drop=True, inplace=True)
offset_jday_allgcms_rcp26.reset_index(drop=True, inplace=True)
offset_jday_allgcms_rcp60.reset_index(drop=True, inplace=True)
offset_jday_allgcms_rcp85.reset_index(drop=True, inplace=True)
      


df_offset_jday_allgcms =pd.concat([
    pd.Series(offset_jday_allgcms_his, name='His' ),
    pd.Series(offset_jday_allgcms_rcp26, name='RCP2.6'),
    pd.Series(offset_jday_allgcms_rcp60, name='RCP6.0' ),
    pd.Series(offset_jday_allgcms_rcp85, name='RCP8.5' )], axis=1)    





#%%Average of onset and offset dates 
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')



# Set up the color palette
custom_palette = ['grey', 'green', 'yellow', 'red']

# Create subplots with space between them
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Adjust the width space between subplots
plt.subplots_adjust(wspace=0.3)
# Use axes[0] instead of ax[0]
sns.violinplot(ax=axes[0], data=df_onset_jday_4models, palette=custom_palette)
axes[0].set_ylabel('Deoxygenation onset date [Jday]')

axes[0].set_ylim(60, 210)  # Set the y-axis limits
axes[0].set_yticks(range(60, 211, 30))  # Set the y-axis ticks at intervals of 20



# Use axes[1] instead of ax[1]
sns.violinplot(ax=axes[1], data=df_offset_jday_4models, palette=custom_palette)
axes[1].set_ylabel('Deoxygenation turnover date [Jday]')

axes[1].set_ylim(180, 300)  # Set the y-axis limits
axes[1].set_yticks(range(180, 330, 30))  # Set the y-axis ticks at intervals of 20


plt.savefig("allsenarios_4models_onset_offset_Jday.png", dpi=300)
"""




#%%all GCMs of onset and offset dates 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results')


# Set up the color palette
custom_palette = ['grey', 'green', 'gold', 'red']

# Create subplots with space between them
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Adjust the width space between subplots
plt.subplots_adjust(wspace=0.3)

# Use axes[0] instead of ax[0]
sns.violinplot(ax=axes[0], data=df_onset_jday_allgcms, palette=custom_palette)
axes[0].set_ylabel('Deoxygenation onset date [Jday]', fontsize=20)  # Increase font size
axes[0].set_ylim(60, 210)  # Set the y-axis limits
axes[0].set_yticks(range(60, 211, 30))  # Set the y-axis ticks at intervals of 20
axes[0].tick_params(axis='both', which='major', labelsize=19)  # Increase tick label size

axes[0].text(0.95, 0.95, '(a)', transform=axes[0].transAxes, fontsize=18, va='top', ha='right')


# Use axes[1] instead of ax[1]
sns.violinplot(ax=axes[1], data=df_offset_jday_allgcms, palette=custom_palette)
axes[1].set_ylabel('Deoxygenation turnover date [Jday]', fontsize=20)  # Increase font size
axes[1].set_ylim(180, 300)  # Set the y-axis limits
axes[1].set_yticks(range(180, 330, 30))  # Set the y-axis ticks at intervals of 20
axes[1].tick_params(axis='both', which='major', labelsize=19)  # Increase tick label size
axes[1].text(0.95, 0.95, '(b)', transform=axes[1].transAxes, fontsize=18, va='top', ha='right')


plt.savefig("allsenarios_allgcms_onset_offset_Jday.png", dpi=300)

#%%Trndlines of onset and offsets over 100 years # for paper ######
#onset_offset


glue_df_onset_jday_his_1999=glue_df_onset_jday_his[glue_df_onset_jday_his.index>1999]
glue_df_offset_jday_4models_his_1999=glue_df_offset_jday_4models_his[glue_df_offset_jday_4models_his.index>1999] 


os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Future_simulation_results/all_4_models/alltogther_for100years/')


import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(30, 10))


axs[0].fill_between(glue_df_onset_jday_his_1999.index, glue_df_onset_jday_his_1999['5%'], glue_df_onset_jday_his_1999['95%'], color='grey', alpha=0.4,  label= 'His 90% CI')
axs[0].plot(glue_df_onset_jday_his_1999.index, glue_df_onset_jday_his_1999['50%'], 'k', label='His median', alpha=1, linewidth=3 )


axs[0].fill_between(glue_df_onset_jday_rcp26.index, glue_df_onset_jday_rcp26['5%'], glue_df_onset_jday_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
axs[0].plot(glue_df_onset_jday_rcp26.index, glue_df_onset_jday_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp26['50%'])
axs[0].text(2000, 100, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f},  p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )

x_values = np.arange(len(glue_df_onset_jday_100years_rcp26.index))
y_values = trendline_rcp26[-2] * x_values + trendline_rcp26[-1]

axs[0].plot(glue_df_onset_jday_100years_rcp26.index, y_values, label='RCP2.6 trendline', linewidth=2, linestyle='--', color='green')




axs[0].fill_between(glue_df_onset_jday_rcp60.index, glue_df_onset_jday_rcp60['5%'], glue_df_onset_jday_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
axs[0].plot(glue_df_onset_jday_rcp60.index, glue_df_onset_jday_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp60['50%'])
axs[0].text(2000, 96, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.0001', color='orange', fontsize= 20 )

x_values = np.arange(len(glue_df_onset_jday_100years_rcp60.index))
y_values = trendline_rcp60[-2] * x_values + trendline_rcp60[-1]

axs[0].plot(glue_df_onset_jday_100years_rcp60.index, y_values, label='RCP6.0 trendline', linewidth=2, linestyle='--', color='yellow')



axs[0].fill_between(glue_df_onset_jday_rcp85.index, glue_df_onset_jday_rcp85['5%'], glue_df_onset_jday_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
axs[0].plot(glue_df_onset_jday_rcp85.index, glue_df_onset_jday_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_onset_jday_100years_rcp85['50%'])
axs[0].text(2000, 92, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize=20)
x_values = np.arange(len(glue_df_onset_jday_100years_rcp85.index))
y_values = trendline_rcp85[-2] * x_values + trendline_rcp85[-1]

axs[0].plot(glue_df_onset_jday_100years_rcp85.index, y_values, label='RCP8.5 trendline', linewidth=2, linestyle='--', color='red')


axs[0].set_ylabel('Deoxygenation onset date [Jd]' , fontsize=26)
axs[0].set_xlabel('Year' , fontsize=26)
axs[0].set_yticks(np.arange(90, 185, 15) , fontsize= 22)

# Now you can set the rotation and fontsize for the labels
#axs[0].set_xticklabels(glue_df_onset_jday_100years_rcp85.index, rotation=45, fontsize=22)
axs[0].text(2098, 180, '(a)', fontsize= 20 )



axs[1].fill_between(glue_df_offset_jday_4models_his_1999.index, glue_df_offset_jday_4models_his_1999['5%'], glue_df_offset_jday_4models_his_1999['95%'], color='grey', alpha=0.4,  label= 'His 90% CI')
axs[1].plot(glue_df_offset_jday_4models_his_1999.index, glue_df_offset_jday_4models_his_1999['50%'], 'k', label='His median', alpha=1, linewidth=3 )

#glue_df_offset_jday_4models_his

axs[1].fill_between(glue_df_offset_jday_4models_rcp26.index, glue_df_offset_jday_4models_rcp26['5%'], glue_df_offset_jday_4models_rcp26['95%'], color='green', alpha=0.4)#,  label= 'RCP2.6 90% CI')
axs[1].plot(glue_df_offset_jday_4models_rcp26.index, glue_df_offset_jday_4models_rcp26['50%'], 'green',  alpha=1, linewidth=3 )#label='RCP2.6 median',
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp26['50%'])


axs[1].fill_between(glue_df_offset_jday_4models_rcp60.index, glue_df_offset_jday_4models_rcp60['5%'], glue_df_offset_jday_4models_rcp60['95%'], color='yellow', alpha=0.4 )#,  label= 'RCP6.0 90% CI')
axs[1].plot(glue_df_offset_jday_4models_rcp60.index, glue_df_offset_jday_4models_rcp60['50%'], 'yellow',alpha=1, linewidth=3 )#, label='RCP6.0 median'
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp60['50%'])
axs[1].text(2000, 212, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value = {trendline_rcp60[-3]:.3f}', color='orange', fontsize= 20 )
x_values = np.arange(len(glue_df_offset_jday_4models_100years_rcp60.index))
y_values = trendline_rcp60[-2] * x_values + trendline_rcp60[-1]

axs[1].plot(glue_df_offset_jday_4models_100years_rcp60.index, y_values, linewidth=2, linestyle='--', color='orange')#, label='RCP6.0 trendline'


axs[1].fill_between(glue_df_offset_jday_4models_rcp85.index, glue_df_offset_jday_4models_rcp85['5%'], glue_df_offset_jday_4models_rcp85['95%'], color='r', alpha=0.3)#,  label= 'RCP8.5 90% CI'
axs[1].plot(glue_df_offset_jday_4models_rcp85.index, glue_df_offset_jday_4models_rcp85['50%'], 'r', alpha=0.9, linewidth=3 )#, label='RCP8.5 median'
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_offset_jday_4models_100years_rcp85['50%'])
axs[1].text(2000, 208, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize=20)
x_values = np.arange(len(glue_df_offset_jday_4models_100years_rcp85.index))
y_values = trendline_rcp85[-2] * x_values + trendline_rcp85[-1]

axs[1].plot(glue_df_offset_jday_4models_100years_rcp85.index, y_values,  linewidth=2, linestyle='--', color='red')#label='RCP8.5 trendline',
axs[1].text(2098, 280, '(b)', fontsize= 20 )


axs[1].set_ylabel('Deoxygenation period turnover date [Jd]' , fontsize=26)
axs[1].set_xlabel('Year' , fontsize=26)
#axs[1].set_yticks(np.arange(210, 300, 10) , fontsize= 22)
# Now you can set the rotation and fontsize for the labels
#axs[1].set_xticklabels(glue_df_offset_jday_4models_100years_rcp85.index, rotation=45, fontsize=22)

# Create custom legend handles
handles_his = [
    Line2D([0], [0], color='k', linewidth=3, linestyle='-', label='His median'),
    Patch(facecolor='grey', alpha=0.4, edgecolor='green', label='His  90% CI'),
    Line2D([0], [0], color='white', linewidth=2, linestyle='--', label='')]


handles_rcp26 = [
    Line2D([0], [0], color='green', linewidth=3, linestyle='-', label='RCP2.6 median'),
    Patch(facecolor='green', alpha=0.4, edgecolor='green', label='RCP2.6  90% CI'),
    Line2D([0], [0], color='green', linewidth=2, linestyle='--', label='RCP2.6 trendline')]

handles_rcp60 = [
    Line2D([0], [0], color='yellow', linewidth=3, linestyle='-', label='RCP6.0 median'),
    Patch(facecolor='yellow', alpha=0.4, edgecolor='yellow', label='RCP6.0  90% CI'),
    Line2D([0], [0], color='orange', linewidth=2, linestyle='--', label='RCP6.0 trendline')
]

handles_rcp85 = [
    Line2D([0], [0], color='r', linewidth=3, linestyle='-', label='RCP8.5 median'),
    Patch(facecolor='r', alpha=0.3, edgecolor='r', label='RCP8.5  90% CI'),
    Line2D([0], [0], color='red', linewidth=2, linestyle='--', label='RCP8.5 trendline')
]

# Combine all handles into a single list
all_handles = handles_his+handles_rcp26 + handles_rcp60 + handles_rcp85

# Create a legend with  3 columns and the first column having  2 rows, and the second and third columns having  3 rows
plt.legend(handles=all_handles, ncol=4, bbox_to_anchor=(0.6, -0.15), fontsize=22)

fig.savefig("GLUE_deox_onset_offset_date_100years.png", dpi=300, bbox_inches='tight')






#%%Timeseries of offset 

np.array(offset_jday_4models_his).mean()
Out[1711]: 241.6206896551724
np.array(offset_jday_4models_rcp26).mean()
Out[1710]: 248.4095744680851
np.array(offset_jday_4models_rcp60).mean()
Out[1709]: 248.58244680851064
np.array(offset_jday_4models_rcp85).mean()
Out[1708]: 249.56914893617022



import matplotlib.pyplot as plt

# Assuming offset_jday_4models_his, offset_jday_4models_rcp26, offset_jday_4models_rcp60, 
# and offset_jday_4models_rcp85 are lists or arrays containing your data.

plt.figure(figsize=(15, 10))  

plt.plot(offset_jday_4models_his, 'grey', label='Historical')
plt.plot(offset_jday_4models_rcp26, 'green', label='RCP 2.6')
plt.plot(offset_jday_4models_rcp60, 'yellow', label='RCP 6.0')
plt.plot(offset_jday_4models_rcp85, 'r', label='RCP 8.5')

#plt.ylim(0, 1)  # Set the y-axis range from 0 to 1

plt.legend()  # Show legend
plt.ylabel('Deoxygenation turnover date [Jday]')

plt.savefig('offset_Jday_ave_4models.png' ,dpi=300)  # Save the plot
 # Show the plot


#%%trendline of offset
plt.figure(figsize=(15, 10))  


#plt.plot(offset_jday_4models_his, label='His', color='grey')#marker='o',

plt.plot(offset_jday_4models_his[1975 <offset_jday_4models_his.index], label='His', color='grey')
plt.plot(offset_jday_4models_rcp26, label='RCP2.6',  color='green')#, alpha= 1)#marker='o',
plt.plot(offset_jday_4models_rcp60, label='RCP6.0',  color='yellow', alpha= 0.9)#marker='o',
plt.plot(offset_jday_4models_rcp85, label='RCP8.5',  color='r' , alpha=0.8 )#marker='o',


# Calculate trendlines

"""
# His slope feom 1850
trendline_his = np.polyfit(offset_jday_4models_his.index, offset_jday_4models_his, 1)
trendline_values_his = np.polyval(trendline_his, offset_jday_4models_his.index)
plt.plot(offset_jday_4models_his.index, trendline_values_his, linestyle='--', color='grey')
#plt.text(1950, trendline_values_his[0], f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='k')
trendline_his[0]
#-0.014019445756573861# # His slope feom 1850

"""

trendline_his = np.polyfit(offset_jday_4models_his[1975 <offset_jday_4models_his.index].index, offset_jday_4models_his[1975 <offset_jday_4models_his.index], 1)
trendline_values_his = np.polyval(trendline_his, offset_jday_4models_his[1975 <offset_jday_4models_his.index].index)
plt.plot(offset_jday_4models_his[1975 <offset_jday_4models_his.index].index, trendline_values_his, linestyle='--', color='grey')
plt.text(2000, 260, f'y = {trendline_his[0]:.2f}x + {trendline_his[1]:.2f}', color='grey')
trendline_his[0]
#-0.30211345939934053  # last 30yaers of his




trendline_rcp26 = np.polyfit(offset_jday_4models_rcp26.index, offset_jday_4models_rcp26, 1)
trendline_values_rcp26 = np.polyval(trendline_rcp26, offset_jday_4models_rcp26.index)
plt.plot(offset_jday_4models_rcp26.index, trendline_values_rcp26, linestyle='--', color='green')
plt.text(2000, 258, f'y = {trendline_rcp26[0]:.2f}x + {trendline_rcp26[1]:.2f}', color='green')
trendline_rcp26[0]#slop of trendline
#-0.05372972582451179


trendline_rcp60 = np.polyfit(offset_jday_4models_rcp60.index, offset_jday_4models_rcp60, 1)
trendline_values_rcp60 = np.polyval(trendline_rcp60, offset_jday_4models_rcp60.index)
plt.plot(offset_jday_4models_rcp60.index, trendline_values_rcp60, linestyle='--', color='yellow')
plt.text(2000, 256, f'y = {trendline_rcp60[0]:.2f}x + {trendline_rcp60[1]:.2f}', color='yellow')
trendline_rcp60[0]#slop of trendline
#-0.12820864790665643


trendline_rcp85 = np.polyfit(offset_jday_4models_rcp85.index, offset_jday_4models_rcp85, 1)
trendline_values_rcp85 = np.polyval(trendline_rcp85, offset_jday_4models_rcp85.index)
plt.plot(offset_jday_4models_rcp85.index, trendline_values_rcp85, linestyle='--', color='r')
plt.text(2000, 254, f'y = {trendline_rcp85[0]:.2f}x + {trendline_rcp85[1]:.2f}', color='r')
trendline_rcp85[0]
#-0.22818336162987937



# Set the y-axis limits with an interval of 25
y_ticks = np.arange(230, 270, 5)
plt.yticks(y_ticks)

plt.ylabel('Deoxygenation turnover date [Jd]')
#plt.xlabel('Year')
plt.legend(loc='upper left')

plt.savefig("allsenarios_mean_deoxygenation_turnover_date_periods_trendline_last30hist.png", dpi=300)














#%%prportion of date with hypolimnetic ave higher than 10.52

prop_higher_ave_temp_4models_his=(offset_jday_4models_his-firstdate_higher_ave_temp_4models_his)/(offset_jday_4models_his -onset_jday_4models_his)
prop_higher_ave_temp_4models_rcp26=(offset_jday_4models_rcp26-firstdate_higher_ave_temp_4models_rcp26)/(offset_jday_4models_rcp26 -onset_jday_4models_rcp26)
prop_higher_ave_temp_4models_rcp60=(offset_jday_4models_rcp60-firstdate_higher_ave_temp_4models_rcp60)/(offset_jday_4models_rcp60 -onset_jday_4models_rcp60)
prop_higher_ave_temp_4models_rcp85=(offset_jday_4models_rcp85-firstdate_higher_ave_temp_4models_rcp85)/(offset_jday_4models_rcp60 -onset_jday_4models_rcp85)


######
np.array(prop_higher_ave_temp_4models_his).mean()
Out[1711]: 0.4623791013743072

prop_higher_ave_temp_4models_his[1975 <prop_higher_ave_temp_4models_his.index].mean()
0.4313701993877796

np.array(prop_higher_ave_temp_4models_rcp26).mean()
Out[1710]: 0.4728081563280892
np.array(prop_higher_ave_temp_4models_rcp60).mean()
Out[1709]: 0.4983328674953909
np.array(prop_higher_ave_temp_4models_rcp85).mean()
Out[1708]: 0.532783505136511





import matplotlib.pyplot as plt

# Assuming prop_higher_ave_temp_4models_his, prop_higher_ave_temp_4models_rcp26, prop_higher_ave_temp_4models_rcp60, 
# and prop_higher_ave_temp_4models_rcp85 are lists or arrays containing your data.

plt.figure(figsize=(15, 10))  

plt.plot(prop_higher_ave_temp_4models_his[1975 <prop_higher_ave_temp_4models_his.index], 'grey', label='Historical')
plt.plot(prop_higher_ave_temp_4models_rcp26, 'green', label='RCP 2.6')
plt.plot(prop_higher_ave_temp_4models_rcp60, 'yellow', label='RCP 6.0')
plt.plot(prop_higher_ave_temp_4models_rcp85, 'r', label='RCP 8.5')

plt.ylim(0, 1)  # Set the y-axis range from 0 to 1

plt.legend()  # Show legend
plt.ylabel('Proportion of date with higher temp than 10.52°C in deox')

plt.savefig('prop_higher_ave_temp_4models.png' ,dpi=300)  # Save the plot
# Show the plot



#%%J day of higher temp than 10.52



plt.figure(figsize=(15, 10))  

plt.plot(firstdate_higher_ave_temp_4models_his[1975 <firstdate_higher_ave_temp_4models_his.index], 'grey', label='Historical')
plt.plot(firstdate_higher_ave_temp_4models_rcp26, 'green', label='RCP 2.6')
plt.plot(firstdate_higher_ave_temp_4models_rcp60, 'yellow', label='RCP 6.0')
plt.plot(firstdate_higher_ave_temp_4models_rcp85, 'r', label='RCP 8.5')

plt.ylim(145, 220)  # Set the y-axis range from 0 to 1

plt.legend()  # Show legend
plt.ylabel('The first date with higher hypolimnetic temp than 10.52°C [Jday]')

plt.savefig('date_of_higher_ave_temp_4models.png' ,dpi=300)  # Save the plot
# Show the plot