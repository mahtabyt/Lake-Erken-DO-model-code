# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 17:27:31 2023

@author: mahta
"""

#%% Reading the bathymetry data:

#import    
import pandas as pd
import os    
# specify the current working directory
os.chdir(r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\inputs')

# reading CSV files:

# 1. bath file
bath = pd.read_csv('bath_Erken.csv')
Z_b = bath['Z(m)']


A_bath = bath['A(m2)']
V_bath = bath['V(m3)']

A_bath_cum = bath['A_cum']
V_bath_cum = bath['V_cum']    


# %% A and V calculation for YSI prof= A_r(sediment are or latteral area) , V_r(Volume for each layer), A_cum(surface area for each layer top)
#bathymetric data are within inerval of 2m should interpolated to 0.5m 
# defining V cum and A cum from interpolation:

#import     
import scipy.interpolate
import numpy as np

As_interp = scipy.interpolate.interp1d(bath['Z(m)'], bath['A_cum'])
Vcum_interp = scipy.interpolate.interp1d(bath['Z(m)'], bath['V_cum'])

# boundry A_s and V_cum in the upper boundry of each Z_m    
Z_up_bndr_m= np.append(0  , np.arange(-1.25,-17.25 , -0.5))

As_up_bndr_m= np.array([])
Vcum_up_bndr= np.array([])

for i in Z_up_bndr_m:
    A=As_interp(i)
    As_up_bndr_m= np.append (As_up_bndr_m , A )
    
    V=Vcum_interp(i)
    Vcum_up_bndr= np.append (Vcum_up_bndr , V )
# boundry A_s and V_cum in the lower boundry of each Z_m    
Z_lo_bndr_m= np.append(np.arange(-1.25,-17.25 , -0.5) , -21)
    
As_lo_bndr_m= np.array([])
Vcum_lo_bndr= np.array([])

for i in Z_lo_bndr_m:
    A=As_interp(i)
    As_lo_bndr_m= np.append (As_lo_bndr_m , A )
    
    V=Vcum_interp(i)
    Vcum_lo_bndr= np.append (Vcum_lo_bndr , V )    
    
# calculating V_r (for each layer) and A_l (latteral or sediment )  
V_r_m=Vcum_up_bndr - Vcum_lo_bndr 
A_l_m=As_up_bndr_m- As_lo_bndr_m
As_up_bndr_m
As_lo_bndr_m    
Z_m= np.arange(-1, -17.5, -0.5 )
thickness_up_lo_of_m= np.append( -1*np.diff(Z_m) , 21-16.75)
thickness_up_lo_of_m[0]= 1.25
dZ_up_bndr_down=thickness_up_lo_of_m



df_morphro = pd.DataFrame({'Z_m': Z_m,
    'thikness': thickness_up_lo_of_m,# first 1.25m , last 4.25m
    'dZ_up_bndr_down': dZ_up_bndr_down,
    'V_r_m': V_r_m,
    'A_l_m': A_l_m,
    'As_up_bndr_m': As_up_bndr_m,
    'As_lo_bndr_m': As_lo_bndr_m})#,
    #"As_m": As_m,
    #"Vcum_m": Vcum_m})
#%%df_geometry_full_prof_obsgrid


df_geometry_full_prof_obsgrid=df_morphro.copy()


#%% subseting the geometry datframe for hypolimnion calculation 

#V_r
V_r_full_prof= np.array(df_geometry_full_prof_obsgrid['V_r_m'])

V_r_epi= np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] > -14 , 'V_r_m'])

V_r_hypo=np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] < -13.5 , 'V_r_m'])



#A_s
A_s_full_prof= np.array(df_geometry_full_prof_obsgrid['As_up_bndr_m'])

A_s_epi= np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] > -14 , 'As_up_bndr_m'])

A_s_hypo=np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] < -13.5 , 'As_up_bndr_m'])


#A_l
A_l_full_prof= np.array(df_geometry_full_prof_obsgrid['A_l_m'])

A_l_epi= np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] > -14 , 'A_l_m'])

A_l_hypo=np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] < -13.5 , 'A_l_m'])




#Z_m


Z_m_full_prof= np.array(df_geometry_full_prof_obsgrid['Z_m'])

Z_m_epi= np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] > -14 , 'Z_m'])

Z_m_hypo=np.array(df_geometry_full_prof_obsgrid.loc[df_geometry_full_prof_obsgrid['Z_m'] < -13.5 , 'Z_m'])


#%%Reading the each years YSI profilers:

from sklearn.linear_model import LinearRegression

# Change the current working directory
os.chdir(r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\raw_data_SITE_2018_2022')

def mydateparser(x):
    return pd.to_datetime(x, format="%d/%m/%Y %H:%M")


# rounding to 0.5 interval

def custom_round(value):
    rounded_value = np.clip(value, 1, 17)  # Clip the value within the range (1, 17)
    return np.round(rounded_value * 2) / 2


# Standard Method (1992) & Gill (1982)  
# other references:
# https://doi.org/10.1016/0198-0149(81)90122-9 UNESCO 1981-> 1 atm pressure 
# (BIGG, 1967, British Journal of Applied Physics, 8, 521-537
# APHA (American Public Health Association), AWWA (American Water Works Association), WEF (Water Environment Federation). (2017). Standard Methods for the Examination of Water and Wastewater. APHA.-> link: https://beta-static.fishersci.com/content/dam/fishersci/en_US/documents/programs/scientific/technical-documents/white-papers/apha-water-testing-standard-methods-introduction-white-paper.pdf
#  physical limnionlogy imberger https://sci-hub.se/10.1016/S0065-2156(08)70199-6
  
def Lab_Density(Temp):
    return (999.842594+6.793952*10**-2*Temp-9.095290*10**-3*Temp**2 + 1.001685*10**-4*Temp**3-1.120083*10**-6 * Temp**4+6.536332 * 10**-9*Temp**5)
       

def process_excel_file(file_name):
    # Read the Excel file and parse the dates column
    df = pd.read_csv(file_name, delimiter=',', skiprows=36, parse_dates=['TIMESTAMP'], date_parser=mydateparser)
    df=df.set_index('TIMESTAMP')
    # Apply custom rounding to 'D_Water' column
    df['Z_m+'] = df['D_WATER'].apply(custom_round)

    # Resample 'TW' column by day for each depth and calculate the mean
    df_tem_resampled = df.groupby('Z_m+')['TW'].resample('D').mean().reset_index()
   
    # Resample 'O2' column by day for each depth and calculate the mean
    df_O2_resampled = df.groupby('Z_m+')['O2'].resample('D').mean().reset_index()
         
    # Resample 'O2SAT' column by day for each depth and calculate the mean
    df_O2SAT_resampled = df.groupby('Z_m+')['O2SAT'].resample('D').mean().reset_index()
    
    
    #using pivot for having unique dates in index and depth in each column
    reshaped_df_TW = df_tem_resampled.pivot(index='TIMESTAMP', columns='Z_m+', values='TW')
    
    reshaped_df_O2 = df_O2_resampled.pivot(index='TIMESTAMP', columns='Z_m+', values='O2')
    
    reshaped_df_O2SAT = df_O2SAT_resampled.pivot(index='TIMESTAMP', columns='Z_m+',values='O2SAT')
    
    
    # Reindex the DataFrame to include all dates
    date_range = pd.date_range(start=reshaped_df_TW.index.min(), end=reshaped_df_TW.index.max(), freq='D')
    reshaped_df_TW = reshaped_df_TW.reindex(date_range)
    
    # Fill missing rows with NaN values
    reshaped_df_TW = reshaped_df_TW.sort_index()  # Sort the DataFrame by index
    
    
    # Reindex the DataFrame to include all dates
    date_range = pd.date_range(start=reshaped_df_O2.index.min(), end=reshaped_df_O2.index.max(), freq='D')
    reshaped_df_O2 = reshaped_df_O2.reindex(date_range)
    
    # Fill missing rows with NaN values
    reshaped_df_O2 = reshaped_df_O2.sort_index()  #  Sort the DataFrame by index
    
    
    # Reindex the DataFrame to include all dates
    date_range = pd.date_range(start=reshaped_df_O2SAT.index.min(), end=reshaped_df_O2SAT.index.max(), freq='D')
    reshaped_df_O2SAT = reshaped_df_O2SAT.reindex(date_range)
    
    # Fill missing rows with NaN values
    reshaped_df_O2SAT = reshaped_df_O2SAT.sort_index()  #  Sort the DataFrame by index
    

    
    #count number of nan values:
        
    num_dates_with_nan = reshaped_df_TW.isnull().any(axis=1).sum()
    print("Number of dates with NaN values in DO profile:", num_dates_with_nan)    
    
    
    num_dates_with_nan = reshaped_df_O2.isnull().any(axis=1).sum()
    print("Number of dates with NaN values in DO profile:", num_dates_with_nan)
    
    
    num_dates_with_nan = reshaped_df_O2SAT.isnull().any(axis=1).sum()
    print("Number of dates with NaN values in DO saturation percentage profile:", num_dates_with_nan)
    
    #fill the nan values according interpolation method  
    reshaped_df_O2=reshaped_df_O2.interpolate()
    reshaped_df_TW= reshaped_df_TW.interpolate()
    reshaped_df_O2SAT= reshaped_df_O2SAT.interpolate()
    
    
    #Reshape the dataframe to the repeating Datetime and Z_m+:
    df_TW = reshaped_df_TW.stack().reset_index()
    df_TW.columns = ['Datetime', 'Z_m+', 'Temp']

    
    df_O2 = reshaped_df_O2.stack().reset_index()
    df_O2.columns = ['Datetime', 'Z_m+', 'DO']
    
    
    df_O2sat= reshaped_df_O2SAT.stack().reset_index()
    df_O2sat.columns= ['Datetime' , 'Z_m+' , 'DO_sat']
    
    #mergeing the temp and DO , DOsat 
    daily_prof_Temp_DO = df_TW.merge(df_O2, on=['Datetime', 'Z_m+']).merge(df_O2sat, on=['Datetime', 'Z_m+'])

    # Add density column
    daily_prof_Temp_DO['density2'] = Lab_Density(daily_prof_Temp_DO['Temp'])

    # Add Z_m column
    daily_prof_Temp_DO['Z_m'] = -1 * daily_prof_Temp_DO['Z_m+']


    # Merge with morphology characteristics dataframe
    daily_prof_Temp_DO_morpho = pd.merge(daily_prof_Temp_DO, df_morphro, on="Z_m", how="outer")
    daily_prof_Temp_DO_morpho = daily_prof_Temp_DO_morpho.sort_values(['Datetime', 'Z_m+'])


    # Save dataframes to CSV files with unique names
    output_folder = "each year daily profiles preprocessors"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    
    output_file_temp_do = os.path.join(output_folder, f"daily_prof_{file_name}_Temp_DO.csv")
    daily_prof_Temp_DO.to_csv(output_file_temp_do, index=False)
    
    output_file_temp_do_morpho = os.path.join(output_folder, f"daily_prof_{file_name}_Temp_DO_morpho.csv")
    daily_prof_Temp_DO_morpho.to_csv(output_file_temp_do_morpho, index=False)

    return daily_prof_Temp_DO, daily_prof_Temp_DO_morpho , num_dates_with_nan  



#using for each year separately:
    
daily_prof_Temp_DO_2018 , daily_prof_Temp_DO_morpho_2018 , counts_of_missing_day_2018 =process_excel_file('SITES_SONDE-PROF_ERK_YSI-present_20180508-20181114_L2_60min.csv')    
#20 number of missing dates 
daily_prof_Temp_DO_2019 , daily_prof_Temp_DO_morpho_2019 , counts_of_missing_day_2019 =process_excel_file('SITES_SONDE-PROF_ERK_YSI-present_20190417-20190926_L2_60min.csv')
#13 number of missing dates 
daily_prof_Temp_DO_2020 , daily_prof_Temp_DO_morpho_2020 , counts_of_missing_day_2020 =process_excel_file('SITES_SONDE-PROF_ERK_YSI-present_20200306-20201112_L2_60min.csv')
#14 number of missing dates 
daily_prof_Temp_DO_2021 , daily_prof_Temp_DO_morpho_2021 , counts_of_missing_day_2021 =process_excel_file('SITES_SONDE-PROF_ERK_YSI-present_20210401-20211115_L2_60min.csv')
#1 number of missing dates 
daily_prof_Temp_DO_2022 , daily_prof_Temp_DO_morpho_2022 , counts_of_missing_day_2022 =process_excel_file('SITES_SONDE-PROF_ERK_YSI-present_20220428-20221107_L2_60min.csv')
#2 number of missing dates 


#%% function of DO satuareted:
    
def C_satur(temp, percent, altitude_m=10 ): # altitude in km for lake erken was 10/1000
    altitude_km = altitude_m/1000 
    P = np.exp(5.25 * np.log(1 - altitude_km/44.3))
    t = temp
    T = 273.15 + t
    teta = 0.000975 - (t*1.426*10**-5) + ((t**2)*6.436*10**-8)
    Pwv = 11.8571 - (3840.70/T)-(216961/T**2)
    C_star =np.exp(7.7117 - 1.31403 * np.log(t+45.93))
    return percent*(C_star * P*(((1-(Pwv/P))*(1-teta*P))/((1-Pwv)*(1-teta))))  
    

def estimate_satur_percentage ( C , temp , altitude_m=10 ):
        est_satur=(C/C_satur (temp , 1))*100
        return (est_satur)





#%% finding recalibartion correlation for DO:     
#%% 1. using the 4 fixed sensors in 1m, 2m, 3m, 17m:
#======= No need to run the results put in the below section    
"""    
2018_YSI_Aux_Daily.xlsx
2019_YSI_Aux_Daily.xlsx
2020_YSI_Aux_Daily.xlsx
2021_YSI_Aux_Daily.xlsx
2022_YSI_Aux_Daily.xlsx
"""
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
# Import the required function from the scipy.stats module# for 'linregress'
from scipy.stats import linregress

# Change the current working directory
os.chdir(r'C:\Users\mahta\OneDrive\Documents\Chapter_1_PhD_py_codes_results\recalibration of YSI profilers according to daily fixed_sensors_1_2_3_17m\Four_fixed_depth_sensors_measurement_2018_2022')
 
"""
# List of columns to read
columns_to_read = ['TMSTAMP' , 'O2_conc1_Avg', 'O2_conc2_Avg', 'O2_conc3_Avg', 'O2_conc4_Avg',
                   'WTemp_C1_Avg', 'WTemp_C2_Avg', 'WTemp_C3_Avg', 'WTemp_C4_Avg']

def mydateparser(x):
    return pd.to_datetime(x, format="%d/%m/%Y")

# Specify the file paths for the five years
file_paths = ['2018_YSI_Aux_Daily.xlsx', '2019_YSI_Aux_Daily.xlsx', '2020_YSI_Aux_Daily.xlsx', '2021_YSI_Aux_Daily.xlsx', '2022_YSI_Aux_Daily.xlsx']

# List to store the individual DataFrames
dfs = []

# Loop through the file paths
for file_path in file_paths:
    # Read the Excel file, parsing the second column as a date-time object
    df = pd.read_excel(file_path, skiprows=1, parse_dates=['TMSTAMP'], date_parser=mydateparser, usecols=columns_to_read)
    # Append the DataFrame to the list
    dfs.append(df)


# Concatenate the individual DataFrames into a single DataFrame
fixed_sensors_5years = pd.concat(dfs)

# renaming 'WTemp_C4_Avg' , 'O2_conc4_Avg' to 'WTemp_C17_Avg', 'O2_conc17_Avg'

fixed_sensors_5years=fixed_sensors_5years.rename(columns={'WTemp_C4_Avg': 'WTemp_C17_Avg', 'O2_conc4_Avg': 'O2_conc17_Avg'})


# concating all years profile YSI
daily_prof_Temp_DO_5years= pd.concat ([daily_prof_Temp_DO_2018 , daily_prof_Temp_DO_2019
                                       , daily_prof_Temp_DO_2020 , daily_prof_Temp_DO_2021
                                       , daily_prof_Temp_DO_2022])

#%%
# Assuming you have the 'fixed_sensors_5years' DataFrame and 'daily_prof_Temp_DO_5years' DataFrame available

# Available depths in fixed_sensors_5years DataFrame
avail_depths = ['1', '2', '3', '17']

# Initialize an empty DataFrame to store the relationship results
depth_relationships_DO = pd.DataFrame(columns=['Depth', 'DO', 'R2_score', 'Slope', 'Intercept'])
# Filter the daily_prof_Temp_DO_5years DataFrame for the depths of interest
filtered_daily_prof = daily_prof_Temp_DO_5years[daily_prof_Temp_DO_5years['Z_m+'].isin([1, 2 , 3, 17])]
y_DO_total= np.array([])
X_DO_total=np.array([])
year_list_total= np.array([])
# Iterate over each depth
for depth in avail_depths:
    # Get the corresponding temperature and DO column names in fixed_sensors_5years DataFrame

    do_column = f'O2_conc{depth}_Avg'
    
    # Filter the daily_prof_Temp_DO_5years DataFrame for the current depth
    depth_df = daily_prof_Temp_DO_5years[daily_prof_Temp_DO_5years['Z_m+'] == float(depth)]
    
    # Merge the DO values with the fixed_sensors_5years DataFrame based on the common date column
    merged_df = pd.merge(fixed_sensors_5years[['TMSTAMP', do_column]], depth_df[['Datetime', 'DO']], left_on='TMSTAMP', right_on='Datetime')
    # Calculate the correlation between DO values in fixed_sensors_5years and daily_prof_Temp_DO_5years for the current depth
    R2 = r2_score (merged_df[do_column] , merged_df['DO'])
    
    # Perform linear regression to calculate the slope and intercept
    y = merged_df[do_column].values.reshape(-1, 1).flatten()
    X = merged_df['DO'].values
    year= merged_df['TMSTAMP'].dt.year
    
    slope, intercept , r_value , p_value= linregress(X , y)[:4] 
    n_samples=len(X)
    
    
    
    X_DO_total= np.append (X_DO_total , X)
    y_DO_total= np.append (y_DO_total , y)
    year_list_total= np.append (year_list_total , year)
    
    
    
    
#===============================#all depth and years  availble togther :     
slope_DO_total, intercept_DO_total ,r_value_DO_total, p_value_DO_total= linregress(X_DO_total , y_DO_total)[:4] 

n_samples_DO_total=len(X_DO_total)
R2_DO_total=r2_score(X_DO_total , y_DO_total)



slope_DO_total
Out[78]: 1.07024483204196

intercept_DO_total
Out[79]: -0.8784611114425989

R2_DO_total
Out[70]: 0.9555841899340843

n_samples_DO_total
Out[71]: 4056


#%%

depth_relationships_DO = depth_relationships_DO.append({'Depth': "1/2/3/17m" , 'DO': do_column, 'R2_score': R2_DO_total, 'Slope': slope_DO_total, 'Intercept': intercept_DO_total , 'R_value' : r_value_DO_total , 'P_value' : p_value_DO_total ,  'n_samples':n_samples_DO_total }, ignore_index=True)
"""
#the number of day for estimating the realtion ship:1013
	Depth	DO	R2_score	Slope	Intercept	P_value	R_value	n_samples
0	1	O2_conc1_Avg	0.911412438432981	1.062023130046011	-0.7708421811159969	0.0	0.9586660520583459	1014.0
1	2	O2_conc2_Avg	0.9031951510740799	1.0595539850238918	-0.7931122405544091	0.0	0.9564833865921534	1014.0
2	3	O2_conc3_Avg	0.9104140186158061	1.080198220300418	-0.8642688185632394	0.0	0.9569153979951569	1014.0
3	17	O2_conc17_Avg	0.9667377329394673	1.053108106595173	-0.8732205451437283	0.0	0.9897420940197431	1014.0
4	1/2/3/17m	O2_conc17_Avg	0.9555841899340843	1.07024483204196	-0.8784611114425989	0.0	0.9850029157057675	4056.0

"""
#profiler correction 
def DO_profiler_correction (x):
    y= 1.070245*x -0.878461
    if y<0:
        y=0
    return (y)


#%% seperately for each year 

import pandas as pd
import numpy as np
from scipy.stats import linregress
from sklearn.metrics import r2_score

# Initialize an empty list to collect data frames
relationships_DO_annual_frames = []

# Assuming X_DO_total, y_DO_total, and year_list_total are already defined
data = {'X_DO_total': X_DO_total, 'y_DO_total': y_DO_total, 'year': year_list_total}

# Create a DataFrame from the dictionary
DO_total_dated = pd.DataFrame(data)

# Iterate over each year
for i in range(int(min(year_list_total)), int(max(year_list_total)) + 1):
    # Filter data for the current year
    year_data = DO_total_dated[DO_total_dated['year'] == i]
    X_total_annual = year_data['X_DO_total']
    y_total_annual = year_data['y_DO_total']
    
    # Perform linear regression
    slope_total_annual, intercept_total_annual, r_value_total_annual, p_value_total_annual, _ = linregress(X_total_annual, y_total_annual)
    n_samples_total_annual = len(X_total_annual)
    R2_total_annual = r2_score(X_total_annual, y_total_annual)
    
    # Create a DataFrame for current year's data
    annual_data = pd.DataFrame({
        'year': [i],
        'R2_score': [R2_total_annual],
        'Slope': [slope_total_annual],
        'Intercept': [intercept_total_annual],
        'R_value': [r_value_total_annual],
        'P_value': [p_value_total_annual],
        'n_samples': [n_samples_total_annual]
    })
    
    # Append DataFrame to the list
    relationships_DO_annual_frames.append(annual_data)

# Concatenate all DataFrames in the list into one DataFrame
relationships_DO_annual = pd.concat(relationships_DO_annual_frames, ignore_index=True)


#all depth togther sepearely foer each year temp:
#relationships_temp_annual    
slope_temp_total, intercept_temp_total,r_value_temp_total, p_value_temp_total =linregress(X_temp_total , y_temp_total)[:4] 
n_samples_temp_total=len(X_temp_total)
R2_temp_total=r2_score(X_temp_total , y_temp_total)
"""
     year  R2_score     Slope  Intercept   R_value  P_value  n_samples
0  2018.0  0.943679  0.997536  -0.537432  0.989570      0.0      764.0
1  2019.0  0.964787  1.064893  -0.486206  0.987167      0.0      652.0
2  2020.0  0.978145  1.087411  -0.750853  0.994619      0.0     1004.0
3  2021.0  0.967767  1.105551  -1.106157  0.991702      0.0      916.0
4  2022.0  0.903117  1.040044  -1.124539  0.984674      0.0      720.0
"""

#profiler correction 

Slope_annual_fixed_sensor= np.array([0.997536 ,1.064893 , 1.087411, 1.105551, 1.040044])
Intercept_annual_fixed_sensor= np.array([ -0.537432, -0.486206 ,-0.750853,  -1.106157 , -1.124539 ])


#relationships_DO_annual['n_samples'].sum()
#Out[71]: 4056.0


#%%plotting 
import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Assuming X_DO_total, y_DO_total, and year_list_total are already defined

# Create a DataFrame from the dictionary
data = {'X_DO_total': X_DO_total, 'y_DO_total': y_DO_total, 'year': year_list_total}
DO_total_dated = pd.DataFrame(data)

# Filter data for the years 2019 to 2022
years_of_interest = [2019, 2020, 2021, 2022]
filtered_data = DO_total_dated[DO_total_dated['year'].isin(years_of_interest)]

# Initialize lists to store results
slope_annual = []
intercept_annual = []
r_squared_annual = []

# Set up figure and axes for plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Iterate over each year
for year in years_of_interest:
    # Filter data for the current year
    year_data = filtered_data[filtered_data['year'] == year]
    X_total_annual = year_data['X_DO_total']
    y_total_annual = year_data['y_DO_total']
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(X_total_annual, y_total_annual)
    r_squared = r_value ** 2
    
    # Store results for annotation later
    slope_annual.append(slope)
    intercept_annual.append(intercept)
    r_squared_annual.append(r_squared)
    
    # Plot scatter plot
    ax.scatter(X_total_annual, y_total_annual, label=f'Year {year}')
    
    # Plot regression line
    ax.plot(X_total_annual, intercept + slope * X_total_annual, '-', label=f'Year {year} Regression')
    
    # Annotate the plot with the equation of the regression line
    ax.annotate(f'y = {slope:.2f} * x + {intercept:.2f}\n$R^2$ = {r_squared:.2f}',
                xy=(0.05, 0.85 - years_of_interest.index(year) * 0.1),
                xycoords='axes fraction', fontsize=12)
    
# Set labels and title
ax.set_xlabel('X_DO_total (mg L$^{-1}$)')
ax.set_ylabel('y_DO_total (mg L$^{-1}$)')
#ax.set_title('Relationship between X_DO_total and y_DO_total (2019-2022)')

# Add legend
ax.legend('lowerright')

# Show plot
plt.tight_layout()
plt.show()
#%%
import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Assuming X_DO_total, y_DO_total, and year_list_total are already defined

# Create a DataFrame from the dictionary
data = {'X_DO_total': X_DO_total, 'y_DO_total': y_DO_total, 'year': year_list_total}
DO_total_dated = pd.DataFrame(data)

# Filter data for the years 2019 to 2022
years_of_interest = [2019, 2020, 2021, 2022]
filtered_data = DO_total_dated[DO_total_dated['year'].isin(years_of_interest)]

# Initialize lists to store results
slope_annual = []
intercept_annual = []
r_squared_annual = []

# Set up figure and axes for plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Iterate over each year
for year in years_of_interest:
    # Filter data for the current year
    year_data = filtered_data[filtered_data['year'] == year]
    X_total_annual = year_data['X_DO_total']
    y_total_annual = year_data['y_DO_total']
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(X_total_annual, y_total_annual)
    r_squared = r_value ** 2
    
    # Store results for annotation later
    slope_annual.append(slope)
    intercept_annual.append(intercept)
    r_squared_annual.append(r_squared)
    
    # Plot scatter plot
    ax.scatter(X_total_annual, y_total_annual, label=f'Year {year} observations')
    
    # Plot regression line
    ax.plot(X_total_annual, intercept + slope * X_total_annual, '-', label=f'Year {year} regression')
    
    # Annotate the plot with the equation of the regression line and R-squared value
    ax.annotate(f'y = {slope:.2f}x - {intercept:.2f} , $R^2$ = {r_squared:.2f}',
                xy=(0.01, 0.6 + years_of_interest.index(year) * 0.1),
                xycoords='axes fraction', fontsize=12, color=f'C{years_of_interest.index(year)}')
    
# Set labels and title
ax.set_xlabel('YSI measures [mg L$^{-1}$]', fontsize=12)
ax.set_ylabel('Fixed sensors measures[mg L$^{-1}$]' , fontsize=12)

# Set legend position and labels
ax.legend(loc='lower right')

# Save the figure with its title
plt.savefig('DO_total_relationship.png', bbox_inches='tight')

# Show plot
plt.show()





#%%Temp recalibration relationship over differet depths 


import pandas as pd
import numpy as np
from scipy.stats import linregress
from sklearn.metrics import r2_score

# Initialize depth_relationships_temp DataFrame
depth_relationships_temp = pd.DataFrame(columns=['Depth', 'Temp', 'R2_score', 'Slope', 'Intercept', 'R_value', 'P_value', 'n_samples'])

# Initialize lists to store aggregated data
depth_data = []
X_temp_total = np.array([])
y_temp_total = np.array([])

# Filter the daily_prof_Temp_DO_5years DataFrame for the depths of interest
filtered_daily_prof = daily_prof_Temp_DO_5years[daily_prof_Temp_DO_5years['Z_m+'].isin([1, 2, 3, 17])]

# Iterate over each depth
for depth in avail_depths:
    # Get the corresponding temperature column name in fixed_sensors_5years DataFrame
    temp_column = f'WTemp_C{depth}_Avg'

    # Filter the daily_prof_Temp_DO_5years DataFrame for the current depth
    depth_df = daily_prof_Temp_DO_5years[daily_prof_Temp_DO_5years['Z_m+'] == float(depth)]

    # Merge the Temp values with the fixed_sensors_5years DataFrame based on the common date column
    merged_df = pd.merge(fixed_sensors_5years[['TMSTAMP', temp_column]], depth_df[['Datetime', 'Temp']], left_on='TMSTAMP', right_on='Datetime')

    # Calculate the correlation between temp values in fixed_sensors_5years and daily_prof_Temp_DO_5years for the current depth
    R2 = r2_score(merged_df[temp_column], merged_df['Temp'])

    # Perform linear regression to calculate the slope and intercept
    y = merged_df[temp_column].values.reshape(-1, 1).flatten()
    X = merged_df['Temp'].values
    slope, intercept, r_value, p_value = linregress(X, y)[:4]
    n_samples = len(X)

    # Append current depth's data to depth_data list
    depth_data.append({
        'Depth': depth,
        'Temp': temp_column,
        'R2_score': R2,
        'Slope': slope,
        'Intercept': intercept,
        'R_value': r_value,
        'P_value': p_value,
        'n_samples': n_samples
    })

    # Aggregate X and y values
    X_temp_total = np.append(X_temp_total, X)
    y_temp_total = np.append(y_temp_total, y)

# Convert depth_data list to DataFrame
depth_relationships_temp = pd.DataFrame(depth_data)

# Calculate total values for all depths
R2_temp_total = r2_score(y_temp_total, X_temp_total)
slope_temp_total, intercept_temp_total, r_value_temp_total, p_value_temp_total, n_samples_temp_total = linregress(X_temp_total, y_temp_total)

# Append summary row for total values to depth_relationships_temp
depth_relationships_temp = pd.concat([depth_relationships_temp, pd.DataFrame([{
    'Depth': "1/2/3/17m",
    'Temp': "Total",
    'R2_score': R2_temp_total,
    'Slope': slope_temp_total,
    'Intercept': intercept_temp_total,
    'R_value': r_value_temp_total,
    'P_value': p_value_temp_total,
    'n_samples': n_samples_temp_total
}])], ignore_index=True)

"""
depth_relationships_temp
Out[47]: 
       Depth           Temp  R2_score  ...   R_value  P_value    n_samples
0          1   WTemp_C1_Avg  0.994282  ...  0.997201      0.0  1014.000000
1          2   WTemp_C2_Avg  0.994481  ...  0.997273      0.0  1014.000000
2          3   WTemp_C3_Avg  0.994290  ...  0.997165      0.0  1014.000000
3         17  WTemp_C17_Avg  0.993611  ...  0.996813      0.0  1014.000000
4  1/2/3/17m          Total  0.994818  ...  0.997433      0.0     0.001133

"""
#temp profiler correction previously 
def temp_profiler_correction (x):
    y= 1.005306*x -0.044020
    return (y)
"""

#%%annual correction according to annual fixed depth sensor  :



#The above section was commented but the
#results of correlation were pased to use here 


    
Slope_annual_fixed_sensor= np.array([0.997536 ,1.064893 , 1.087411, 1.105551, 1.040044])
Intercept_annual_fixed_sensor= np.array([ -0.537432, -0.486206 ,-0.750853,  -1.106157 , -1.124539 ])


daily_prof_Temp_DO_2018['DO'] , daily_prof_Temp_DO_morpho_2018['DO']= Slope_annual_fixed_sensor[0]* daily_prof_Temp_DO_2018['DO']+ Intercept_annual_fixed_sensor[0],  Slope_annual_fixed_sensor[0]*daily_prof_Temp_DO_morpho_2018['DO']+ Intercept_annual_fixed_sensor[0]
    
daily_prof_Temp_DO_2019['DO'] , daily_prof_Temp_DO_morpho_2019['DO']=  Slope_annual_fixed_sensor[1]*daily_prof_Temp_DO_2019['DO']+ Intercept_annual_fixed_sensor[1] , Slope_annual_fixed_sensor[1]*daily_prof_Temp_DO_morpho_2019['DO']+ Intercept_annual_fixed_sensor[1] 
   
daily_prof_Temp_DO_2020['DO'] , daily_prof_Temp_DO_morpho_2020['DO']= Slope_annual_fixed_sensor[2]*daily_prof_Temp_DO_2020['DO']+ Intercept_annual_fixed_sensor[2] ,Slope_annual_fixed_sensor[2]*daily_prof_Temp_DO_morpho_2020['DO']+ Intercept_annual_fixed_sensor[2]
   
daily_prof_Temp_DO_2021['DO'] , daily_prof_Temp_DO_morpho_2021['DO']= Slope_annual_fixed_sensor[3]*daily_prof_Temp_DO_2021['DO']+ Intercept_annual_fixed_sensor[3] , Slope_annual_fixed_sensor[3]*daily_prof_Temp_DO_morpho_2021['DO']+ Intercept_annual_fixed_sensor[3]
  
daily_prof_Temp_DO_2022['DO'] , daily_prof_Temp_DO_morpho_2022['DO']= Slope_annual_fixed_sensor[4]*daily_prof_Temp_DO_2022['DO']+ Intercept_annual_fixed_sensor[4],  Slope_annual_fixed_sensor[4]*daily_prof_Temp_DO_morpho_2022['DO']+ Intercept_annual_fixed_sensor[4]
  

# checked there is no data below 0 

(daily_prof_Temp_DO_morpho_2018['DO']<0).sum()#81
(daily_prof_Temp_DO_morpho_2019['DO']<0).sum()#0
(daily_prof_Temp_DO_morpho_2020['DO']<0).sum()#0
(daily_prof_Temp_DO_morpho_2021['DO']<0).sum()#24
(daily_prof_Temp_DO_morpho_2022['DO']<0).sum()#71


# replace the estimated DO below 0 equals to 0:
    
daily_prof_Temp_DO_morpho_2018['DO']=np.where((daily_prof_Temp_DO_morpho_2018['DO']<0), 0, daily_prof_Temp_DO_morpho_2018['DO'])
daily_prof_Temp_DO_morpho_2019['DO']=np.where((daily_prof_Temp_DO_morpho_2019['DO']<0), 0, daily_prof_Temp_DO_morpho_2019['DO'])
daily_prof_Temp_DO_morpho_2020['DO']=np.where((daily_prof_Temp_DO_morpho_2020['DO']<0), 0, daily_prof_Temp_DO_morpho_2020['DO'])
daily_prof_Temp_DO_morpho_2021['DO']=np.where((daily_prof_Temp_DO_morpho_2021['DO']<0), 0, daily_prof_Temp_DO_morpho_2021['DO'])
daily_prof_Temp_DO_morpho_2022['DO']=np.where((daily_prof_Temp_DO_morpho_2022['DO']<0), 0, daily_prof_Temp_DO_morpho_2022['DO'])




#%% 2. usinghon_coding/recalibration of YSI profilers according to weekly sampling(monitoring)')
#not usable in this stage 

"""
# Change the current working directory
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/recalibration of YSI profilers according to weekly sampling(monitoring)')


def mydateparser(x):
    return pd.to_datetime(x, format="%d/%m/%Y")

# reading xlsx files:

forthnightly_sampling = pd.read_excel('only_weekly_sampling_2018_2022.xlsx' ,  parse_dates=['Datetime'], date_parser=mydateparser)
# cause only need the days with whole profile in station called 'Bojen'
forthnightly_sampling = forthnightly_sampling.groupby(forthnightly_sampling['Datetime'].dt.date).filter(lambda x: x['Depth'].min() <= -15)



# Extract date portion from Datetime columns
forthnightly_sampling['Date'] = forthnightly_sampling['Datetime'].dt.date


daily_prof_Temp_DO_5years= pd.concat ([daily_prof_Temp_DO_2018 , daily_prof_Temp_DO_2019
                                       , daily_prof_Temp_DO_2020 , daily_prof_Temp_DO_2021
                                       , daily_prof_Temp_DO_2022])
daily_prof_Temp_DO_5years['Date'] = daily_prof_Temp_DO_5years['Datetime'].dt.date


forthnightly_sampling = forthnightly_sampling.merge(daily_prof_Temp_DO_5years[['Date', 'Z_m', 'DO']], left_on=['Date', 'Depth'], right_on=['Date', 'Z_m'], how='left')
forthnightly_sampling['DO_YSI_profilers'] = forthnightly_sampling['DO']

forthnightly_sampling.drop(['Z_m', 'DO'], axis=1, inplace=True)


forthnightly_sampling.dropna(inplace=True)


#Discoveing the correlation equation:

import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt


years = forthnightly_sampling.Datetime.dt.year.unique()
slopes= np.array([])
intercepts= np.array ([])
for year in years:
    do_ysi_profilers = forthnightly_sampling[forthnightly_sampling.Datetime.dt.year == year]['DO_YSI_profilers']
    do_sampling = forthnightly_sampling[forthnightly_sampling.Datetime.dt.year == year]['DO_sampling']
    
    # Calculate the linear regression
    slope, intercept, r_value, p_value, std_err = linregress(do_ysi_profilers, do_sampling)
    r_squared = r_value ** 2
    
    #saving the slopes and intercepts in one array for all avialble depth:
    slopes= np.append (slopes , slope)    
    intercepts= np.append (intercepts , intercept )
    
    
    
    
    
    print(f"years: {year}")
    print(f"Correlation Equation: y = {slope}x + {intercept}")
    print(f"R-squared: {r_squared}")
    print()



 # Plotting the data points
    plt.scatter(do_ysi_profilers, do_sampling, label=f'Year {year}')
    
    # Plot the regression line
    plt.plot(do_ysi_profilers, slope * do_ysi_profilers + intercept, color='red', label='Linear Fit')
    plt.text(0.4, 0.8, f'y = {slope:.2f}x + {intercept:.2f}', transform=plt.gca().transAxes, fontsize=12)#, color='blue')
   
    plt.text(0.4, 0.7, f'R² = {r_squared:.2f}', transform=plt.gca().transAxes, fontsize=12)#, color='green')
  
   
    plt.xlabel('DO_YSI_profilers')
    plt.ylabel('DO_sampling')
    plt.title(f'Year: {year}')
    plt.savefig(f'correlation_of_weekly_sampling_and_YSI_profiler_{year}.png', dpi= 300)
    #plt.legend()
    plt.show()


"""

slopes
#array([1.04075741, 1.00359295, 1.01358038, 1.0128015 , 0.96500006])
intercepts
#array([-0.5136458 , -0.37050375, -0.41377025, -0.54471354, -0.72666828])





"""
years: 2018
Correlation Equation: y = 1.0407574075422033x + -0.5136457961378813
R-squared: 0.9882770301929101

years: 2019
Correlation Equation: y = 1.0035929486654045x + -0.3705037477736557
R-squared: 0.9634423176341773

years: 2020
Correlation Equation: y = 1.0135803810299615x + -0.4137702548463853
R-squared: 0.9775498615342224

years: 2021
Correlation Equation: y = 1.0128015041595273x + -0.5447135364788167
R-squared: 0.9852875062102411

years: 2022
Correlation Equation: y = 0.9650000584267837x + -0.7266682844372712
R-squared: 0.9795581877468907
"""











#for each depth which didn't use: 
"""
depths = forthnightly_sampling['Depth'].unique()
slopes= np.array([])
intercepts= np.array ([])
for depth in depths:
    do_ysi_profilers = forthnightly_sampling[forthnightly_sampling['Depth'] == depth]['DO_YSI_profilers']
    do_sampling = forthnightly_sampling[forthnightly_sampling['Depth'] == depth]['DO_sampling']
    
    # Calculate the linear regression
    slope, intercept, r_value, p_value, std_err = linregress(do_ysi_profilers, do_sampling)
    r_squared = r_value ** 2
    
    #saving the slopes and intercepts in one array for all avialble depth:
    slopes= np.append (slopes , slope)    
    intercepts= np.append (intercepts , intercept )
    
    
    print(f"Depth: {depth}")
    print(f"Correlation Equation: y = {slope}x + {intercept}")
    print(f"R-squared: {r_squared}")
    print()


depths_full_m  = daily_prof_Temp_DO_5years['Z_m'].unique()

# Interpolate the slopes and intercepts for the depths_full_m array
slopes_full = np.interp(depths_full_m, depths, slopes)
intercepts_full = np.interp(depths_full_m, depths, intercepts)

"""
"""

# the relation is estimate based on only 132 day (2-week interval)
Depth: -1.0
Correlation Equation: y = 0.9174048992272277x + 0.591052420358567
R-squared: 0.9546803334264332

Depth: -2.0
Correlation Equation: y = 0.9278648652962581x + 0.4712028408228104
R-squared: 0.9563560770112388

Depth: -3.0
Correlation Equation: y = 0.927409374415657x + 0.46999902184388276
R-squared: 0.9550277327281139

Depth: -4.0
Correlation Equation: y = 0.9274827128364107x + 0.45732338042644116
R-squared: 0.9534454346294156

Depth: -5.0
Correlation Equation: y = 0.9369021284183128x + 0.3088062392407789
R-squared: 0.9033713310227894

Depth: -6.0
Correlation Equation: y = 0.940184441807599x + 0.2962370101516498
R-squared: 0.9535500809070702

Depth: -7.0
Correlation Equation: y = 0.9233453161525046x + 0.4855725777637723
R-squared: 0.9442304202418637

Depth: -8.0
Correlation Equation: y = 0.9294584878612816x + 0.40759516173681476
R-squared: 0.9320241949370405

Depth: -9.0
Correlation Equation: y = 0.9520764652884174x + 0.08972552473346163
R-squared: 0.9209636587222761

Depth: -10.0
Correlation Equation: y = 1.0203215635617024x + -0.719140778574932
R-squared: 0.952972066836732

Depth: -11.0
Correlation Equation: y = 1.0130597036434412x + -0.6005969824072359
R-squared: 0.959247140715333

Depth: -12.0
Correlation Equation: y = 1.0065709920875903x + -0.6015829141225586
R-squared: 0.9532360585644489

Depth: -13.0
Correlation Equation: y = 1.0176688587853429x + -0.7484240896756518
R-squared: 0.9910427595916682

Depth: -14.0
Correlation Equation: y = 1.0171315378514356x + -0.7695269251378472
R-squared: 0.9880965786343049

Depth: -15.0
Correlation Equation: y = 0.9980127973365064x + -0.5916470089839105
R-squared: 0.9767008741462223

Depth: -16.0
Correlation Equation: y = 1.0060692023910769x + -0.6635537855401887
R-squared: 0.9901171996513891


Depth: -17.0
Correlation Equation: y = 1.0055700077455456x + -0.640091487347771
R-squared: 0.992927713262559

"""





"""

# Extract the required columns
#do_ysi_profilers = forthnightly_sampling['DO_YSI_profilers']   
do_ysi_profilers_1 =forthnightly_sampling[forthnightly_sampling['Depth']== -1]['DO_YSI_profilers']
                                     
#do_sampling = forthnightly_sampling['DO_sampling']  
do_sampling_1 = forthnightly_sampling[forthnightly_sampling['Depth']==-1]['DO_sampling']

#the numbers of days ready for buliding up the correlation (132,) only fo rthr hypolimnion 
#forthnightly_sampling['Date'].unique().shape


# Calculate the linear regression



slope, intercept, r_value, p_value, std_err = linregress(do_ysi_profilers,do_sampling )
r_squared = r_value**2


slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = linregress(do_ysi_profilers_1,do_sampling_1 )
r_squared_1 = r_value_1**2


def recalibration_correlation(do):
    y=slope*do +  intercept
    if y<0: 
        y=0
    return ( y )# 1.01- 0.66X
"""

"""
# Create a string for the linear regression equation
equation = f'Y = {slope:.2f}X {intercept:.2f}'

# Plot the relationship
plt.figure( figsize= (6, 7), dpi=200)
plt.scatter(do_ysi_profilers,do_sampling , s=10)
plt.plot(do_ysi_profilers, intercept+ slope * do_ysi_profilers, 'r', label='Linear Regression')
plt.xlabel('DO_sampling')
plt.ylabel('DO_YSI_profilers')
plt.title('Linear Relationship: DO_YSI_profilers vs. DO_sampling')
plt.legend()


# Calculate the coordinates for the text
text_x = np.max(do_ysi_profilers)
text_y = np.mean(do_sampling)
r2_x = np.max(do_ysi_profilers)
r2_y = np.mean(do_sampling)

# Display the linear regression equation and R2 value on the plot
plt.text(text_x, text_y, equation, fontsize=12, ha='right', va='top')
plt.text(r2_x, r2_y, f'R2 = {r_squared:.2f}', fontsize=12, ha='right', va='bottom')

plt.savefig('correlation_equation_between_weekly_sampling_YSI.png', dpi=200)
plt.show()


# intercept for even depth of lower than 10m is -0.66 
# but intercept for whole profile is -0.53 
# the slop is all same for each depth selection 1.01
"""


#%%function for correction each depth diferently- based on 2-weekly correlation:
#Not Appliable NA    
"""    
import numpy as np

def correct_dissolved_oxygen(dataframe, slopes=slopes_full, intercepts= intercepts_full, depths= depths_full_m):
    # Copy the original DataFrame to avoid modifying the input data
    corrected_df = dataframe.copy()

    # Interpolate the slopes and intercepts for the depths in the DataFrame
    interpolated_slopes = np.interp(dataframe['Z_m'], depths, slopes)
    interpolated_intercepts = np.interp(dataframe['Z_m'], depths, intercepts)

    # Correct the dissolved oxygen values using the interpolated slopes and intercepts
    corrected_df['DO'] = dataframe['DO'] * interpolated_slopes + interpolated_intercepts

    return corrected_df
"""



#%% functiom of recalibration based on the fixed sensores estimations(all years and depth togther) 
"""
def temp_DO_prof_recalibration(dataframe):
    # Copy the original DataFrame to avoid modifying the input data
    corrected_df = dataframe.copy()


    # Correct the temp values 
    #corrected_df['Temp'] = dataframe['Temp'].apply(temp_profiler_correction)

    # Correct the dissolved oxygen values 
    corrected_df['DO'] = dataframe['DO'].apply(DO_profiler_correction)

    return corrected_df
"""
#%%apply the selected function for DO YSI profile data :
    
""" 
daily_prof_Temp_DO_2018 , daily_prof_Temp_DO_morpho_2018 = temp_DO_prof_recalibration(daily_prof_Temp_DO_2018) , temp_DO_prof_recalibration(daily_prof_Temp_DO_morpho_2018)

daily_prof_Temp_DO_2019 , daily_prof_Temp_DO_morpho_2019 = temp_DO_prof_recalibration(daily_prof_Temp_DO_2019) , temp_DO_prof_recalibration(daily_prof_Temp_DO_morpho_2019)

daily_prof_Temp_DO_2020 , daily_prof_Temp_DO_morpho_2020 = temp_DO_prof_recalibration(daily_prof_Temp_DO_2020) , temp_DO_prof_recalibration(daily_prof_Temp_DO_morpho_2020)

daily_prof_Temp_DO_2021 , daily_prof_Temp_DO_morpho_2021 = temp_DO_prof_recalibration(daily_prof_Temp_DO_2021) , temp_DO_prof_recalibration(daily_prof_Temp_DO_morpho_2021)

daily_prof_Temp_DO_2022 , daily_prof_Temp_DO_morpho_2022 = temp_DO_prof_recalibration(daily_prof_Temp_DO_2022) , temp_DO_prof_recalibration(daily_prof_Temp_DO_morpho_2022)
"""

#seperate years based on two_weekly sampling values 
"""
slopes
Out[35]: array([1.04075741, 1.00359295, 1.01358038, 1.0128015 , 0.96500006])

intercepts
Out[36]: array([-0.5136458 , -0.37050375, -0.41377025, -0.54471354, -0.72666828])

    
daily_prof_Temp_DO_2018['DO'] , daily_prof_Temp_DO_morpho_2018['DO']= slopes[0]* daily_prof_Temp_DO_2018['DO']+ intercepts[0],  slopes[0]*daily_prof_Temp_DO_morpho_2018['DO']+ intercepts[0]
    
daily_prof_Temp_DO_2019['DO'] , daily_prof_Temp_DO_morpho_2019['DO']=  slopes[1]*daily_prof_Temp_DO_2019['DO']+ intercepts[1] , slopes[1]*daily_prof_Temp_DO_morpho_2019['DO']+ intercepts[1] 
   
daily_prof_Temp_DO_2020['DO'] , daily_prof_Temp_DO_morpho_2020['DO']= slopes[2]*daily_prof_Temp_DO_2020['DO']+ intercepts[2] ,slopes[2]*daily_prof_Temp_DO_morpho_2020['DO']+ intercepts[2]
   
daily_prof_Temp_DO_2021['DO'] , daily_prof_Temp_DO_morpho_2021['DO']= slopes[3]*daily_prof_Temp_DO_2021['DO']+ intercepts[3] , slopes[3]*daily_prof_Temp_DO_morpho_2021['DO']+ intercepts[3]
  
daily_prof_Temp_DO_2022['DO'] , daily_prof_Temp_DO_morpho_2022['DO']= slopes[4]*daily_prof_Temp_DO_2022['DO']+ intercepts[4],  slopes[4]*daily_prof_Temp_DO_morpho_2022['DO']+ intercepts[4]
  

# checked there is no data below 0 

(daily_prof_Temp_DO_morpho_2018['DO']<0).sum()#0
(daily_prof_Temp_DO_morpho_2019['DO']<0).sum()#0
(daily_prof_Temp_DO_morpho_2020['DO']<0).sum()#0
(daily_prof_Temp_DO_morpho_2021['DO']<0).sum()#0
(daily_prof_Temp_DO_morpho_2022['DO']<0).sum()#0
"""





"""    
#just in case 
#daily_prof_Temp_DO_5years['DO'] = daily_prof_Temp_DO_5years['DO'].apply (recalibration_correlation) 
"""

"""profiler_correction
daily_prof_Temp_DO_2018['DO'] , daily_prof_Temp_DO_morpho_2018['DO']= daily_prof_Temp_DO_2018['DO'].apply (profiler_correction) , daily_prof_Temp_DO_morpho_2018['DO'].apply (profiler_correction)
    
daily_prof_Temp_DO_2019['DO'] , daily_prof_Temp_DO_morpho_2019['DO']= daily_prof_Temp_DO_2019['DO'].apply (profiler_correction) , daily_prof_Temp_DO_morpho_2019['DO'].apply (profiler_correction)
   
daily_prof_Temp_DO_2020['DO'] , daily_prof_Temp_DO_morpho_2020['DO']= daily_prof_Temp_DO_2020['DO'].apply (profiler_correction) , daily_prof_Temp_DO_morpho_2020['DO'].apply (profiler_correction)
   
daily_prof_Temp_DO_2021['DO'] , daily_prof_Temp_DO_morpho_2021['DO']= daily_prof_Temp_DO_2021['DO'].apply (profiler_correction) , daily_prof_Temp_DO_morpho_2021['DO'].apply (profiler_correction)
  
daily_prof_Temp_DO_2022['DO'] , daily_prof_Temp_DO_morpho_2022['DO']= daily_prof_Temp_DO_2022['DO'].apply (profiler_correction) , daily_prof_Temp_DO_morpho_2022['DO'].apply (profiler_correction)
  
#just in case 
#daily_prof_Temp_DO_5years['DO'] = daily_prof_Temp_DO_5years['DO'].apply (profiler_correction) 
"""

#%% The saturation percentage shoud be corrected according the new recalibated DO values and the tempaerture

from sklearn.metrics import r2_score
from scipy.stats import linregress



#originaly got it from 
#https://www.waterontheweb.org/under/waterquality/oxygen.html

#1956 Mortimer, C.H.
#Mortimer, C.H. 1956. The oxygen content of air-saturated fresh waters, and aids in calculating percentage saturation. Intern. Assoc. Theoret. Appl. Commun. No 6.

def C_satur(temp, percent=1):
    altitude = 10/1000  # altitude in km from sea level for lake erken was 10/1000
    P = np.exp(5.25 * np.log(1 - altitude/44.3))
    t = temp
    T = 273.15 + t
    teta = 0.000975 - (t*1.426*10**-5) + ((t**2)*6.436*10**-8)
    Pwv = 11.8571 - (3840.70/T)-(216961/T**2)
    C_star =np.exp(7.7117 - 1.31403 * np.log(t+45.93))
    return percent*(C_star * P*(((1-(Pwv/P))*(1-teta*P))/((1-Pwv)*(1-teta))))    


def estimate_satuartion_percentage (df):
    est_saturation_percenatge=(df['DO']/C_satur(df ['Temp'] , 1))* 100
    df['est_DO_sat']=est_saturation_percenatge
    return (df)



daily_prof_Temp_DO_morpho_2018= estimate_satuartion_percentage(daily_prof_Temp_DO_morpho_2018)
daily_prof_Temp_DO_morpho_2019= estimate_satuartion_percentage(daily_prof_Temp_DO_morpho_2019)
daily_prof_Temp_DO_morpho_2020= estimate_satuartion_percentage(daily_prof_Temp_DO_morpho_2020)
daily_prof_Temp_DO_morpho_2021= estimate_satuartion_percentage(daily_prof_Temp_DO_morpho_2021)
daily_prof_Temp_DO_morpho_2022= estimate_satuartion_percentage(daily_prof_Temp_DO_morpho_2022)


daily_prof_Temp_DO_2018= estimate_satuartion_percentage(daily_prof_Temp_DO_2018)
daily_prof_Temp_DO_2019= estimate_satuartion_percentage(daily_prof_Temp_DO_2019)
daily_prof_Temp_DO_2020= estimate_satuartion_percentage(daily_prof_Temp_DO_2020)
daily_prof_Temp_DO_2021= estimate_satuartion_percentage(daily_prof_Temp_DO_2021)
daily_prof_Temp_DO_2022= estimate_satuartion_percentage(daily_prof_Temp_DO_2022)


daily_prof_Temp_DO_morpho_5years= pd.concat ([ daily_prof_Temp_DO_morpho_2018  ,  daily_prof_Temp_DO_morpho_2019,
            daily_prof_Temp_DO_morpho_2020 , daily_prof_Temp_DO_morpho_2021, 
            daily_prof_Temp_DO_morpho_2022])


daily_prof_Temp_DO_5years= pd.concat ([daily_prof_Temp_DO_2018 , daily_prof_Temp_DO_2019
                                       , daily_prof_Temp_DO_2020 , daily_prof_Temp_DO_2021
                                       , daily_prof_Temp_DO_2022])



import matplotlib.pyplot as plt 
#plt.plot( daily_prof_Temp_DO_morpho_5years['DO_sat'] , daily_prof_Temp_DO_morpho_5years['est_DO_sat'])


slope_sat_total, intercept_sat_total,r_value_sat_total, p_value_sat_total =linregress(daily_prof_Temp_DO_morpho_5years['DO_sat'] , daily_prof_Temp_DO_morpho_5years['est_DO_sat'])[:4] 
n_samples_sat_total=len(daily_prof_Temp_DO_morpho_5years['DO_sat'])
R2_sat_total=r2_score(daily_prof_Temp_DO_morpho_5years['DO_sat'] , daily_prof_Temp_DO_morpho_5years['est_DO_sat'])


"""The corelation results of ['DO_sat'] and ['DO_sat_est'] (came from the recalibrated DO and the observed tempaerature)

print ( slope_sat_total , intercept_sat_total , r_value_sat_total, p_value_sat_total ,
       n_samples_sat_total , R2_sat_total) 


1.0599230490941283 -7.62693687256521 
0.9930954016367688 0.0 
33957 0.9728666688861795

"""



#%%two_D_array_from_df function definition 

def two_D_array_from_df(df, values_name, index_name='Datetime', column_name='Z_m'):

    piv = df.pivot_table(
        index=index_name, columns=column_name, values=values_name)

    if df[column_name].min() < 0:
        piv = piv.sort_index(
            axis='columns', level=column_name, ascending=False)

    return (np.array(piv))



#%%SSI_daily_full_prof and SSI_daily_epi functions
"""
#1.
def SSI_daily_full_prof(density_gotm_full_prof_obsgrid , V_r_full_prof , Z_m_full_prof ,A0 = 23.67* 10**6 ):
    
    g = 9.81838509231682  # m/s2 or N/kg
    
    
    prof_mass_full_prof=density_gotm_full_prof_obsgrid * V_r_full_prof 
    daily_mass_full_prof = np.dot(density_gotm_full_prof_obsgrid , V_r_full_prof)
    
    prof_momentum_full_prof= density_gotm_full_prof_obsgrid*(-1* Z_m_full_prof* V_r_full_prof )
    daily_momentum_full_prof = np.dot( density_gotm_full_prof_obsgrid , (-1*Z_m_full_prof*V_r_full_prof))
    
    
    Z_centeroid_daily_full_prof = daily_momentum_full_prof / daily_mass_full_prof
    density_centeroid_daily_full_prof = daily_mass_full_prof /( V_r_full_prof.sum())
    
    
    diff_density_full_prof_from_cernteroid = density_gotm_full_prof_obsgrid - density_centeroid_daily_full_prof[:, np.newaxis]
    diff_Z_full_prof_from_cernteroid=(-1* Z_m_full_prof)- (Z_centeroid_daily_full_prof[:, np.newaxis]) 
    
    densitydiff_dot_zdiff_daily_profile=np.dot( (diff_density_full_prof_from_cernteroid *diff_Z_full_prof_from_cernteroid)   , V_r_full_prof)
    
    SSI_full_prof =  (1 / A0) * g * densitydiff_dot_zdiff_daily_profile 
    
    return SSI_full_prof





#2.
def SSI_daily_epi(density_gotm_epi_obsgrid , V_r_epi , Z_m_epi ,A0 = 23.67* 10**6 ):
    
    g = 9.81838509231682  # m/s2 or N/kg
    
    
    prof_mass_epi=density_gotm_epi_obsgrid * V_r_epi 
    daily_mass_epi = np.dot(density_gotm_epi_obsgrid , V_r_epi)
    
    prof_momentum_epi= density_gotm_epi_obsgrid*(-1* Z_m_epi *V_r_epi)
    daily_momentum_epi = np.dot( density_gotm_epi_obsgrid ,(-1* Z_m_epi *V_r_epi))
    
    
    Z_centeroid_daily_epi = daily_momentum_epi / daily_mass_epi
    density_centeroid_daily_epi = daily_mass_epi /( V_r_epi.sum())
    
    diff_density_epi_from_cernteroid = density_gotm_epi_obsgrid + -density_centeroid_daily_epi[:, np.newaxis]
    diff_Z_epi_from_cernteroid=  (-1*Z_m_epi) - (Z_centeroid_daily_epi[:, np.newaxis]) 
    
    densitydiff_dot_zdiff_daily_profile=np.dot( (diff_density_epi_from_cernteroid *diff_Z_epi_from_cernteroid)   , V_r_epi)
    
    
    SSI_epi =  (1 / A0) * g * densitydiff_dot_zdiff_daily_profile 
    
    return SSI_epi



#3.Stability index (adrien et al., 2009 in paper of Sahoo 2016)

def SI_daily_epi(density_gotm_epi_obsgrid , V_r_epi , Z_m_epi  ):
    
    
    prof_mass_epi=density_gotm_epi_obsgrid * V_r_epi 
    daily_mass_epi = np.dot(density_gotm_epi_obsgrid , V_r_epi)
    
    prof_momentum_epi= density_gotm_epi_obsgrid*(-1* Z_m_epi *V_r_epi)
    daily_momentum_epi = np.dot( density_gotm_epi_obsgrid ,(-1* Z_m_epi *V_r_epi))
    
    
    Z_centeroid_daily_epi = daily_momentum_epi / daily_mass_epi
    
    
    diff_Z_epi_from_cernteroid=  (-1*Z_m_epi) - (Z_centeroid_daily_epi[:, np.newaxis]) 
    
    
    product_array =diff_Z_epi_from_cernteroid *density_gotm_epi_obsgrid
    
    SI_epi = np.sum(product_array, axis=1)
    
    return SI_epi
"""



#%%testing the function biulted in future scenarios simulation.py file 

density_2D_epi_2018_2022=two_D_array_from_df(daily_prof_Temp_DO_5years[daily_prof_Temp_DO_5years['Z_m'] >-14] , 'density2' ,  index_name='Datetime', column_name='Z_m' ) 

density_2D_full_2018_2022= two_D_array_from_df(daily_prof_Temp_DO_5years , 'density2' )

temp_2D_full_2018_2022= two_D_array_from_df(daily_prof_Temp_DO_5years , 'Temp' )



#SSI_daily_epi_2018_2022=SSI_daily_epi(density_2D_epi_2018_2022 , V_r_epi , Z_m_epi ,A0 = 23.67* 10**6 )
    
#SSI_daily_full_2018_2022= SSI_daily_full_prof(density_2D_full_2018_2022 , V_r_full_prof , Z_m_full_prof  ,A0 = 23.67* 10**6 )


datetime_unique_2018_2022=daily_prof_Temp_DO_5years['Datetime'].unique()


#SSI_daily_epi_2018_2022_indexed = pd.DataFrame({'SSI': SSI_daily_epi_2018_2022}, index=datetime_unique_2018_2022)
#SSI_daily_full_2018_2022_indexed = pd.DataFrame({'SSI':SSI_daily_full_2018_2022} , index=datetime_unique_2018_2022)


#SI_epi_2018_2022=SI_daily_epi(density_2D_epi_2018_2022 , V_r_epi , Z_m_epi)
#SI_daily_epi_2018_2022_indexed = pd.DataFrame({'SI_epi': SI_epi_2018_2022}, index=datetime_unique_2018_2022)


#SI_full_2018_2022=SI_daily_epi(density_2D_full_2018_2022, V_r_full_prof , Z_m_full_prof)
#SI_daily_full_2018_2022_indexed = pd.DataFrame({'SI_full': SI_full_2018_2022}, index=datetime_unique_2018_2022)

#%%2D array of density difference of top and 13.5m 

density_2D_2022_obs= two_D_array_from_df(daily_prof_Temp_DO_morpho_2022 ,'density2' )



#%%Water_Profile_Density_Year separetly for each year timeseries

import matplotlib.pyplot as plt
import numpy as np

# Assuming density_2D_full_2018_2022 is the density data
# You may need to adjust this depending on how your data is structured
density_data = density_2D_full_2018_2022.T  # Transpose the data if needed

# Create a grid of dates and depths
dates = datetime_unique_2018_2022
depths = daily_prof_Temp_DO_5years['Z_m'].unique()       
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Get years from the dates
years = np.unique(np.array([np.datetime_as_string(date, unit='Y') for date in dates]))

# Plot each year separately
for year in years:
    year_dates = dates[np.datetime_as_string(dates, unit='Y') == year]
    year_density_data = density_data[:, np.isin(dates, year_dates)]
    
    
    dates_mesh,depths_mesh= np.meshgrid(year_dates, depths)
    
    
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(dates_mesh, depths_mesh, year_density_data, cmap='viridis')  # Change the cmap as needed
    plt.colorbar(label='Density (kg m$^{-3}$)')
    plt.xlabel('Dates')
    plt.ylabel('Depth (m)')
    plt.title(f'Water Profile Density - Year {year}')
    plt.xticks(rotation=45)
    
    
    # Save the figure
    plt.savefig(f'Water_Profile_Density_Year_{year}.png', dpi=300)
    plt.show()

#%%Water_Profile_temperature_Year timeseries separetly for eacfh year

import matplotlib.pyplot as plt
import numpy as np

# Assuming density_2D_full_2018_2022 is the density data
# You may need to adjust this depending on how your data is structured
temp_data = temp_2D_full_2018_2022.T  # Transpose the data if needed

# Create a grid of dates and depths
dates = datetime_unique_2018_2022
depths = daily_prof_Temp_DO_5years['Z_m'].unique()       
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Get years from the dates
years = np.unique(np.array([np.datetime_as_string(date, unit='Y') for date in dates]))

# Plot each year separately
for year in years:
    year_dates = dates[np.datetime_as_string(dates, unit='Y') == year]
    year_density_data = temp_data[:, np.isin(dates, year_dates)]
    
    
    dates_mesh,depths_mesh= np.meshgrid(year_dates, depths)
    
    
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(dates_mesh, depths_mesh, year_density_data, cmap='coolwarm')  # Change the cmap as needed
    plt.colorbar(label='Temperature (°C) ')
    plt.xlabel('Dates')
    plt.ylabel('Depth (m)')
    plt.title(f'Water Profile Temperature - Year {year}')
    plt.xticks(rotation=45)
    
    
    # Save the figure
    plt.savefig(f'Water_Profile_Temperature_Year_{year}.png', dpi=300)
    plt.show()

#%%filtering the datafram for years 2019-2022


#2018_2022:
density_2D_epi_2018_2022=two_D_array_from_df(daily_prof_Temp_DO_5years[daily_prof_Temp_DO_5years['Z_m'] >-14] , 'density2' ,  index_name='Datetime', column_name='Z_m' ) 

density_2D_full_2018_2022= two_D_array_from_df(daily_prof_Temp_DO_5years , 'density2' )

temp_2D_full_2018_2022= two_D_array_from_df(daily_prof_Temp_DO_5years , 'Temp' )

datetime_unique_2018_2022=daily_prof_Temp_DO_5years['Datetime'].unique()


#2019_2022:
    
   
daily_prof_Temp_DO_4years=daily_prof_Temp_DO_5years[daily_prof_Temp_DO_5years['Datetime'].dt.year!= 2018]    
   
density_2D_epi_2019_2022=two_D_array_from_df(daily_prof_Temp_DO_4years[daily_prof_Temp_DO_4years['Z_m'] >-14] , 'density2' ,  index_name='Datetime', column_name='Z_m' ) 

density_2D_full_2019_2022= two_D_array_from_df(daily_prof_Temp_DO_4years , 'density2' )

temp_2D_full_2019_2022= two_D_array_from_df(daily_prof_Temp_DO_4years , 'Temp' )

datetime_unique_2019_2022=daily_prof_Temp_DO_4years['Datetime'].unique()

    

#%%Water_Profile_density_all_Years timeseries subplots


import matplotlib.pyplot as plt
import numpy as np

# Assuming density_2D_full_2019_2022 is the density data
# You may need to adjust this depending on how your data is structured
density_data = density_2D_full_2019_2022.T  # Transpose the data if needed
min_density=density_data.min()
max_density= density_data.max()
# Create a grid of dates and depths
dates = datetime_unique_2019_2022
depths = daily_prof_Temp_DO_4years['Z_m'].unique()       
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Get years from the dates
years = np.unique(np.array([np.datetime_as_string(date, unit='Y') for date in dates]))

# Calculate the number of rows and columns needed for the grid
num_rows = 2#int(np.ceil(len(years) / 2))
num_cols = 2

# Create a grid of subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10) )#
# wspace=0.4, hspace=0.4)

# Adjust the spacing between the subplots
plt.subplots_adjust(wspace=0.3, hspace=0.3)
# Flatten the axes array to simplify indexing
axes = axes.flatten()

plt.rcParams.update({'font.size': 12})
for i, year in enumerate(years):
    year_dates = dates[np.datetime_as_string(dates, unit='Y') == year]
    year_density_data = density_data[:, np.isin(dates, year_dates)]
    
    dates_mesh, depths_mesh = np.meshgrid(year_dates, depths)
    
    # Plot in the corresponding subplot
    ax = axes[i]
    im = ax.pcolormesh(dates_mesh, depths_mesh, year_density_data, cmap='viridis')  # Change the cmap as needed
    #cb = fig.colorbar(im, ax=ax, label='Density [kg m$^{-3}$]')
    #cb.ax.yaxis.label.set_fontsize(12)  # Set font size for colorbar label
    
    ax.set_ylabel('Depth (m)', fontsize=12)
    ax.tick_params(axis='x', rotation=45)

# Create a colorbar using the maximum density value for all years
norm = matplotlib.colors.Normalize(vmin=min_density, vmax=max_density)
ticks = np.arange(997, 1000, 0.25)
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])  # An empty array is needed for the ScalarMappable

# Add the colorbar
cb = plt.colorbar(sm, ax=axes, ticks=ticks, label='Density [kg m$^{-3}$]')
cb.ax.yaxis.label.set_fontsize(12)

# Adjust layout

# Save the figure
fig.savefig('water_profile_density_4_years.png', dpi=300)


#%%Water_Profile_Temperature_All_Years_timeseries_subplot 

import matplotlib.pyplot as plt
import numpy as np

# Assuming density_2D_full_2019_2022 is the density data
# You may need to adjust this depending on how your data is structured
temp_data = temp_2D_full_2019_2022.T  # Transpose the data if needed
min_temp= temp_data.min()
max_temp= temp_data.max()
# Create a grid of dates and depths
dates = datetime_unique_2019_2022
depths = daily_prof_Temp_DO_4years['Z_m'].unique()       
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Get years from the dates
years = np.unique(np.array([np.datetime_as_string(date, unit='Y') for date in dates]))

# Calculate the number of rows and columns needed for the grid
num_rows = 2#int(np.ceil(len(years) / 2))
num_cols = 2

# Create a grid of subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10) )#
# wspace=0.4, hspace=0.4)

# Adjust the spacing between the subplots
plt.subplots_adjust(wspace=0.3, hspace=0.3)
# Flatten the axes array to simplify indexing
axes = axes.flatten()

plt.rcParams.update({'font.size': 12})
for i, year in enumerate(years):
    year_dates = dates[np.datetime_as_string(dates, unit='Y') == year]
    year_temp_data = temp_data[:, np.isin(dates, year_dates)]
    
    dates_mesh, depths_mesh = np.meshgrid(year_dates, depths)
    
    # Plot in the corresponding subplot
    ax = axes[i]
    im = ax.pcolormesh(dates_mesh, depths_mesh, year_temp_data, cmap='coolwarm')  # Change the cmap as needed
    #cb = fig.colorbar(im, ax=ax, label='Density [kg m$^{-3}$]')
    #cb.ax.yaxis.label.set_fontsize(12)  # Set font size for colorbar label
    
    ax.set_ylabel('Depth (m)', fontsize=12)
    ax.tick_params(axis='x', rotation=45)

# Create a colorbar using the maximum density value for all years
norm = matplotlib.colors.Normalize(vmin=min_temp, vmax=max_temp)
ticks = np.arange(0, 26, 2)
sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
sm.set_array([])  # An empty array is needed for the ScalarMappable

# Add the colorbar
cb = plt.colorbar(sm, ax=axes, ticks=ticks, label='Temperature [°C]')
cb.ax.yaxis.label.set_fontsize(12)

# Adjust layout

# Save the figure
fig.savefig('water_profile_temperature_4_years.png', dpi=300)


#%%Density all years subplot but the interval of depth .5 m (suitable for my analyse )
"""
import matplotlib.pyplot as plt
import numpy as np

# Assuming density_2D_full_2018_2022 is the density data
# You may need to adjust this depending on how your data is structured
density_data = density_2D_full_2018_2022.T  # Transpose the data if needed

# Create a grid of dates and depths
dates = datetime_unique_2018_2022
depths = daily_prof_Temp_DO_5years['Z_m'].unique()       
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Get years from the dates
years = np.unique(np.array([np.datetime_as_string(date, unit='Y') for date in dates]))

# Calculate the number of rows and columns needed for the grid
num_rows = int(np.ceil(len(years) / 2))
num_cols = 2

# Create a grid of subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 10))

# Flatten the axes array to simplify indexing
axes = axes.flatten()

# Plot each year separately
for i, year in enumerate(years):
    year_dates = dates[np.datetime_as_string(dates, unit='Y') == year]
    year_density_data = density_data[:, np.isin(dates, year_dates)]
    
    dates_mesh, depths_mesh = np.meshgrid(year_dates, depths)
    
    # Plot in the corresponding subplot
    ax = axes[i]
    im = ax.pcolormesh(dates_mesh, depths_mesh, year_density_data, cmap='viridis')  # Change the cmap as needed
    fig.colorbar(im, ax=ax, label='Density (kg m$^{-3}$)')
    ax.set_xlabel('Dates')
    ax.set_ylabel('Depth (m)')
    ax.set_title(f'Water Profile Density - Year {year}')
    ax.tick_params(axis='x', rotation=45)
    
    # Set y-axis ticks with one meter interval
    ax.set_yticks(np.arange(depths.min(), depths.max()+1, 1))

# Remove any empty subplots
for i in range(len(years), num_rows*num_cols):
    fig.delaxes(axes[i])

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('Water_Profile_Density_All_Years.png', dpi=300)

# Show the plot
plt.show()
"""

#%%Density profile all years timeseries in one plot 

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Assuming density_2D_full_2018_2022 is a 2D array with shape (1029, 33)
# and dates and depths are defined as you mentioned

# Create a meshgrid for dates and depths
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Assuming density_2D_full_2018_2022 is the density data
# You may need to adjust this depending on how your data is structured
density_data = density_2D_full_2018_2022.T  # Transpose the data if needed

# Create the plot
plt.figure(figsize=(10, 6))
plt.pcolormesh(dates_mesh, depths_mesh, density_data, cmap='viridis')  # Change the cmap as needed
plt.colorbar(label='Density (kg m$^{-3}$)')
plt.xlabel('Dates')
plt.ylabel('Depth (m)')
plt.title('Water Profile Density')
plt.xticks(rotation=45)

# Customize date formatting
date_format = mdates.DateFormatter('%Y-%m-%d')  # Adjust the format as needed
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()

# Save the figure with higher quality
#plt.savefig('water_profile_density_2018_2022.png', dpi=300)  # Adjust the file name and dpi as needed


#%%Temperature profile tiemseries in one plot 

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Assuming density_2D_full_2018_2022 is a 2D array with shape (1029, 33)
# and dates and depths are defined as you mentioned

# Create a meshgrid for dates and depths
dates_mesh, depths_mesh = np.meshgrid(dates, depths)

# Assuming density_2D_full_2018_2022 is the density data
# You may need to adjust this depending on how your data is structured
temp_data = temp_2D_full_2018_2022.T  # Transpose the data if needed

# Create the plot
plt.figure(figsize=(10, 6))
plt.pcolormesh(dates_mesh, depths_mesh, temp_data, cmap='coolwarm')  # Change the cmap as needed
plt.colorbar(label='Temperature (°C)')
plt.xlabel('Dates')
plt.ylabel('Depth (m)')
plt.title('Water Profile Temperature ')
plt.xticks(rotation=45)

# Customize date formatting
date_format = mdates.DateFormatter('%Y-%m-%d')  # Adjust the format as needed
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()

# Save the figure with higher quality
#plt.savefig('water_profile_temperature_2018_2022.png', dpi=300)  # Adjust the file name and dpi as needed


#%%

depth_full_obs=daily_prof_Temp_DO_5years['Z_m'].unique()  

np.where(depth_full_obs==-14)# 26


temp_hypo_obs_2018_2022=temp_2D_full_2018_2022[:, 26:]
density_hypo_obs_2018_2022=density_2D_full_2018_2022[:, 26:]



#%%thermocline_depth with 0.01 

density_difference_surf= density_2D_full_2018_2022.T.copy()


density_difference_surf[1:, :] -= density_difference_surf[0, :]


# Replace values greater than 0.01 with 0 in density_data[1:, :]
density_difference_surf[1:, :] = np.where(density_difference_surf[1:, :] >= 0.1,1, np.nan)

density_difference_surf_ex=density_difference_surf[1:, :].copy()

depths= daily_prof_Temp_DO_5years['Z_m'].unique()

depth_ex_surf=depths[1:].copy()

result = density_difference_surf_ex * depth_ex_surf[:, np.newaxis]

thermocline_depth = np.nanmax(result, axis=0)

dates = datetime_unique_2018_2022




nan_mask = np.isnan(thermocline_depth)

# Use the mask to remove the NaN values
cleaned_thermocline_depth = thermocline_depth[~nan_mask]


thermocline_depth_17 = np.nan_to_num(thermocline_depth, nan=-17)


#plt.plot(dates , thermocline_depth_17)# simple plot
plt.hist(thermocline_depth, bins=12, edgecolor='k')
plt.xlabel('Thermocline Layer Depth')
plt.ylabel('Frequency')
plt.title('Distribution of Thermocline Depth')

# Show the plot
plt.show()

#%% histograph of frequency percentage of thermocline layer depth: 


import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.pyplot as plt

# Assuming `cleaned_thermocline_depth` is your modified array

# Calculate the histogram
counts, bins, _ = plt.hist(cleaned_thermocline_depth*-1, bins=31, density=True, edgecolor='k')

# Calculate the bin width
bin_width = bins[1] - bins[0]

# Calculate the percentages
percentage = counts * bin_width * 100

# Plotting the distribution with percentages on the y-axis
plt.bar(bins[:-1], percentage, width=bin_width, edgecolor='k' , color='grey' )

plt.xlabel('Upper mixing layer depth (m)')
plt.ylabel('Frequency percentage (%)')
#plt.title('Distribution of upper mixing layer')

# Save the plot with dpi=300
plt.savefig('thermocline_depth_distribution_frequency_percentage.png', dpi=300)

# Show the plot (optional)
plt.show()




#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Assuming `thermocline_depth` is your array and `dates` is your list of dates
fig, ax = plt.subplots(1,1, figsize=(8, 6))

# Plotting the distribution
sns.histplot(np.array(thermocline_depth*-1), bins=31,  color='grey', edgecolor='black')

# Change the y-axis to percentage
total_obs = len(thermocline_depth)
ticks_loc = ax.get_yticks().tolist()
ax.set_yticklabels([f'{tick/total_obs*100:.0f}%' for tick in ticks_loc])

#ax.get_lines()[0].set_color('red')
ax.set_xlabel('Upper mixing layer depth [m]')
ax.set_ylabel('Frequency percentage')
# Save the figure with 300 dpi
plt.savefig('histogram_Upper_mixing_layer_depth_for_paper.png', dpi=300)



#%% Analyse of thermocline depth 

#0.1 Kg/m3
percentage
array([0.49833887, 1.1627907 , 0.66445183, 0.83056478, 1.49501661,
       1.32890365, 1.82724252, 1.66112957, 1.1627907 , 1.49501661,
       2.3255814 , 3.15614618, 2.3255814 , 3.82059801, 2.49169435,
       3.48837209, 3.15614618, 4.81727575, 5.48172757, 5.14950166,
       6.47840532, 3.98671096, 3.65448505, 3.98671096, 3.98671096,
       5.81395349, 4.31893688, 5.98006645, 4.65116279, 6.31229236,
       2.49169435])

bins
array([-17. , -16.5, -16. , -15.5, -15. , -14.5, -14. , -13.5, -13. ,
       -12.5, -12. , -11.5, -11. , -10.5, -10. ,  -9.5,  -9. ,  -8.5,
        -8. ,  -7.5,  -7. ,  -6.5,  -6. ,  -5.5,  -5. ,  -4.5,  -4. ,
        -3.5,  -3. ,  -2.5,  -2. ,  -1.5])

sum(percentage)
Out[312]: 100.00000000000004

bins[0:7]
Out[168]: array([-17. , -16.5, -16. , -15.5, -15. , -14.5, -14. ])

100-sum(percentage[0:7])#92.19269102990033# chance of having thermocline or lower mixing depth
# with density differenec of 0.1 Kg/m3 form surface is located in range of layer 14m and below is only #sum(percentage[0:7]) # 7.81%
# then we select our hypolimnion may located below the mixing depth with possibility of 92.19%

# for my self :
# with the same threshold and analyses there is 85.55% that hypolimnion locates below 12m 
# can be usde for more investigation for future 

#%%est satuartion percentage on each day:
    
daily_prof_Temp_DO_morpho_5years=daily_prof_Temp_DO_morpho_5years.set_index('Datetime') 
    
DO_sat_est_2D_prof_hypo_2018_2022= two_D_array_from_df(daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m'] <-13.5], 'est_DO_sat' )

DO_sat_est_ave_hypo_daily_2018_2022= (np.dot (DO_sat_est_2D_prof_hypo_2018_2022 , V_r_hypo))/ sum(V_r_hypo)


  
DO_2D_prof_hypo_2018_2022= two_D_array_from_df(daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m'] <-13.5], 'DO' )

DO_ave_hypo_daily_2018_2022= (np.dot (DO_2D_prof_hypo_2018_2022 , V_r_hypo))/ sum(V_r_hypo)


 
Temp_2D_prof_hypo_2018_2022= two_D_array_from_df(daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m'] <-13.5], 'Temp' )

Temp_ave_hypo_daily_2018_2022= (np.dot (Temp_2D_prof_hypo_2018_2022 , V_r_hypo))/ sum(V_r_hypo)






#date_unique_5yaers=daily_prof_Temp_DO_morpho_5years['Datetime'].unique()
#daily_prof_Temp_DO_morpho_5years=daily_prof_Temp_DO_morpho_5years.set_index('Datetime') 

density_top=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-1]['density2']
density_bot=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-17]['density2']
density_14m=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-14]['density2']
density_135m=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-13.5]['density2']

Temp_top=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-1]['Temp']
Temp_bot=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-17]['Temp']
Temp_14m=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-14]['Temp']
Temp_135m=daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']==-13.5]['Temp']


temp_diff_top_bot= Temp_top-Temp_bot
temp_diff_top_135m=Temp_top- Temp_135m
temp_diff_hypo= Temp_14m-Temp_bot


dens_diff_top_bot= density_top-density_bot
dens_diff_top_135m=density_top- density_135m
dens_diff_hypo= density_14m-density_bot


# creat a dataframe with all the temp and density and est_sat_ percentage 

data = {
    "est_DO_sat": DO_sat_est_ave_hypo_daily_2018_2022,
    "DO_hypo_ave":DO_ave_hypo_daily_2018_2022,
    'Temp_hypo_ave': Temp_ave_hypo_daily_2018_2022,
    "temp_surf": Temp_top,
    "temp_diff_top_bot": temp_diff_top_bot,
    "temp_diff_top_135m": temp_diff_top_135m,
    "temp_diff_hypo": temp_diff_hypo,
    "dens_diff_top_bot": dens_diff_top_bot,
    "dens_diff_top_135m": dens_diff_top_135m,
    "dens_diff_hypo": dens_diff_hypo}


df_analyse_est_sat_temp_dens_diff = pd.DataFrame(data)

# Calculate the difference between one day and the next for each year
result =np.array([])

for year, group in df_analyse_est_sat_temp_dens_diff.groupby(df_analyse_est_sat_temp_dens_diff.index.year):
    diffs = group['est_DO_sat'].diff().tolist()
    result= np.append (result , diffs)
    

df_analyse_est_sat_temp_dens_diff['diff_est_sat']=result

satuartion_percentage_2018_2022=df_analyse_est_sat_temp_dens_diff["est_DO_sat"]


df_analyse_est_sat_temp_dens_diff['temp_diff_top_135m']

df_analyse_est_sat_temp_dens_diff['temp_surf']
#%%diff density of 13.5m and topmost layer >=1

dens_diff_top_135=df_analyse_est_sat_temp_dens_diff['dens_diff_top_135m']

temp_surf_1m=df_analyse_est_sat_temp_dens_diff['temp_surf']

#%% find_dod_periods_densdiff_old version
 """   
def find_dod_periods_densdiff(dens_diff_top_135, threshold=-0.05, concequetive_day=7):
    
    
    subset_indices = {}
    for year in range(dens_diff_top_135.index.year.min(), dens_diff_top_135.index.year.max()+1):
        year_data = dens_diff_top_135.loc[dens_diff_top_135.index.year == year]#.values
        consecutive_true = (year_data < threshold).rolling(window=concequetive_day, min_periods=concequetive_day, center=False).sum() == concequetive_day
        consecutive_true=consecutive_true.shift(-concequetive_day)# the last 5 values in the new series will be NaN
        
        diffs = consecutive_true.diff()
        
        starts = diffs.where((diffs == 1))# actually including the turnover date
        starts = starts.dropna()
        
        ends = diffs.where((diffs == -1))#.shift(concequetive_day-1)# only the onset should have the 5 days in row limitation but not the offset 
        ends = ends.dropna()
        
        if len(starts)==0:
            starts= diffs[diffs.index== diffs.index.min() ]
        
        if len(ends)==0:
            ends= diffs[diffs.index== diffs.index.max() ]
        
        length= (ends.index- (starts.index + pd.Timedelta(days=1))).days

        starts= starts[length> concequetive_day] 
        ends= ends[length> concequetive_day]
        
        for i, (start_index, end_index) in enumerate(zip(starts.index, ends.index)):
               
              
               
               year_subset= daily_prof_Temp_DO_morpho_5years.loc[ start_index: end_index]#end_index- pd.Timedelta(days=1) ####including a day before startification 
               #year_subset=year_subset.reset_index(drop=True)
               SSI_top_to_bottom_str= SSI_daily_full_2018_2022_indexed[ start_index + pd.Timedelta(days=1):end_index]#end_index- pd.Timedelta(days=1)# excluding turnover 
               SSI_top_to_135_str=SSI_daily_epi_2018_2022_indexed[ start_index+ pd.Timedelta(days=1) :end_index]# - pd.Timedelta(days=1)
                
               SI_full_str=SI_daily_full_2018_2022_indexed [ start_index+ pd.Timedelta(days=1) :end_index]#- pd.Timedelta(days=1)
               SI_epi_str=SI_daily_epi_2018_2022_indexed[ start_index+ pd.Timedelta(days=1) :end_index]#- pd.Timedelta(days=1)
                
               temp_hypo_ave_on_day_before_onset=df_analyse_est_sat_temp_dens_diff.loc[start_index].Temp_hypo_ave
               DO_sat_day_before_onset= C_satur( np.array (temp_hypo_ave_on_day_before_onset) , 1)
               # Calculate mean
               mean_SSI_full_str = np.mean(SSI_top_to_bottom_str)
               mean_SSI_epi_str = np.mean(SSI_top_to_135_str)
               mean_SI_full_str = np.mean(SI_full_str)
               mean_SI_epi_str  = np.mean(SI_epi_str)
               # Calculate variance
               variance_SSI_full_str = np.var(SSI_top_to_bottom_str)
               variance_SSI_epi_str = np.var(SSI_top_to_135_str)
               variance_SI_full_str = np.var(SI_full_str)
               variance_SI_epi_str  = np.var(SI_epi_str)
                
               # Calculate standard deviation
               std_SSI_full_str = np.std(SSI_top_to_bottom_str)
               std_SSI_epi_str = np.std(SSI_top_to_135_str)
               std_SI_full_str = np.std(SI_full_str)
               std_SI_epi_str  = np.std(SI_epi_str)


               
                
               var_name = f'df_str_{year}_{i+1}_14'# next time make str to deoxy
               globals()[var_name] = year_subset
               subset_name = f"{year}_{i+1}"# 
               subset_indices[subset_name] = {'A_day_before_strart_index': start_index,
                                              'end_index': end_index  , 
                                              'duration of stratification period' : end_index-start_index,
                                              'temp_hypo_ave_on_day_before_onset':temp_hypo_ave_on_day_before_onset,
                                              'DO_full_sat_day_before_onset': DO_sat_day_before_onset,   
                                              'DO_sat_on_day_before_onset': satuartion_percentage_2018_2022.loc[start_index],
                                              'DO_sat_on_day_end': satuartion_percentage_2018_2022.loc[end_index]}
                                              
                                             # 'mean_SSI_full_str': mean_SSI_full_str,
                                             # 'variance_SSI_full_str':variance_SSI_full_str,
                                             # 'std_SSI_full_str': std_SSI_full_str,
                                              
                                             # 'mean_SSI_epi_str': mean_SSI_epi_str,
                                             # 'variance_SSI_epi_str': variance_SSI_epi_str,
                                             # 'std_SSI_epi_str':std_SSI_epi_str,
                                              
                                             # 'mean_SI_full_str':mean_SI_full_str,
                                             # 'variance_SI_full_str':variance_SI_full_str,
                                             # 'std_SI_full_str':std_SI_full_str,
                                              
                                             # 'mean_SI_epi_str':mean_SI_epi_str,
                                             # 'variance_SI_epi_str':variance_SI_epi_str,
                                             # 'std_SI_epi_str':std_SI_epi_str}
               
               
 
               
    return subset_indices, var_name  
"""




#%%Ideal deoxygenation period definition#basic#!?? # should be corrected for other lake- it is not working correctly******:/
# I just copied the reults of data expolration in file excel:
# 
    
import pandas as pd

for year in range(satuartion_percentage_2018_2022.index.year.min(), satuartion_percentage_2018_2022.index.year.max()+1):
    
    data = satuartion_percentage_2018_2022.loc[satuartion_percentage_2018_2022.index.year == year]
         
    # Assuming data is your DataFrame
    data.index = pd.to_datetime(data.index)
    
    # Criteria 1
    criteria_1 = data < 100# lowe than 100% 
    
    # Criteria 2 # lower than first day of onset at least for 7 days 
    criteria_2 = (data.shift(-1)-data <=0) & \
                 (data.shift(-2)-data <=0) & \
                 (data.shift(-3)-data <=0) & \
                 (data.shift(-4)-data <=0) & \
                 (data.shift(-5)-data <=0) & \
                 (data.shift(-6)-data <=0)
                 
                 
    combine_criteria_start = criteria_1 & criteria_2
    potetial_start_dates = data[combine_criteria_start].index
    
    #potetial_start_dates[np.append(True, np.diff(potetial_start_dates).astype('timedelta64[D]').astype(int)<7)]
    final_start_dates= potetial_start_dates[np.append(True, np.diff(potetial_start_dates).astype('timedelta64[D]').astype(int)>7)]
    
    
    
    
    # Criteria 3#10% increase over 7 days 
    criteria_3 = data.shift(-7) - data>= 10
    
    potetial_end_dates=data[criteria_3].index
    
    final_end_dates=potetial_end_dates[np.append(True, np.diff(potetial_end_dates).astype('timedelta64[D]').astype(int)>7)]
    
    
    # Print out the start and end dates of each group
    for start_date,end_date  in zip( final_start_dates, final_end_dates):
        if (end_date-start_date).days>=10: # duration of deoxygenation should be at least 2 weeks otherwise it will capture the several days in Oct-Nov
            print(f'Start Date: {start_date}, End Date: {end_date}')
            print( satuartion_percentage_2018_2022 [start_date])
            print (f'Duration: {end_date-start_date}')
            print( satuartion_percentage_2018_2022 [end_date])


"""
Revised ideal onset and offsets:						
Onsets: DO_sat[day=0]<100 , DO_sat[day=0]< DO_sat[day=1- 6] & DO_sat [day before day=0 or onset]> DO[day=0]						
Offset: (DO_sat[day= end+7]- DO_sat[day= end] )>10%		

day before onset/ sat_day before start/ day of satrt/ sat on day of start/ day of turnover/ sat on day of turnover/ duartion of deoxygenation period 			
10/05/2019	101.309503	11/05/2019	99.85098218	29/06/2019	32.49057332	49
10/07/2019	78.43521841	11/07/2019	82.2406882	24/08/2019	3.595519599	44
12/05/2020	100.9890351	13/05/2020	99.92430365	04/09/2020	1.400437567	114
10/05/2021	100.1303355	11/05/2021	99.06027748	29/08/2021	0.344226608	110
19/05/2022	102.1043698	20/05/2022	99.05097333	01/09/2022	0.76	104
"""



#%%finding density difference based deoxygenation period_basic
"""
for year in range(dens_diff_top_135.index.year.min(), dens_diff_top_135.index.year.max()+1):
    data = dens_diff_top_135.loc[dens_diff_top_135.index.year ==2021]

    # Assuming data is your DataFrame
    data.index = pd.to_datetime(data.index)
    
    # Criteria 1
    criteria_1 = (data <= -0.01) & \
             (data.shift(-1) <= -0.01) & \
             (data.shift(-2) <= -0.01) & \
             (data.shift(-3) <= -0.01) & \
             (data.shift(-4) <= -0.01) & \
             (data.shift(-5) <= -0.01) & \
             (data.shift(-6) <= -0.01) 

                 
    criteria_2= (data >-0.1) & \
                  (data.shift(-1)>-0.1) & \
                  (data.shift(-2)>-0.1) & \
                  (data.shift(-3)>-0.1) & \
                  (data.shift(-4)>-0.1) & \
                  (data.shift(-5)>-0.1) & \
                  (data.shift(-6)>-0.1)               
                 
                 
   
   
    potetial_start_dates= data[criteria_1].index# & criteria_1
    final_start_dates= potetial_start_dates[np.append(True, np.diff(potetial_start_dates).astype('timedelta64[D]').astype(int)>7)]
    

    # Criteria 2
    criteria_3= (data <-0.1) & \
                 (data.shift(-1)<-0.1) & \
                 (data.shift(-2)<-0.1) & \
                 (data.shift(-3)<-0.1) & \
                 (data.shift(-4)<-0.1) & \
                 (data.shift(-5)<-0.1) & \
                 (data.shift(-6)<-0.1)   

    potetial_end_dates=data[criteria_3].index
    
    if (np.diff(potetial_end_dates).astype('timedelta64[D]').astype(int)>7).sum()==0:
        final_end_dates=[potetial_end_dates.min() , potetial_end_dates.max()]
    else:
        final_end_dates=potetial_end_dates[np.append(True, np.diff(potetial_end_dates).astype('timedelta64[D]').astype(int)>7)]
    
     # Print out the start and end dates of each group
    for start_date,end_date  in zip( final_start_dates, final_end_dates):
         if (end_date-start_date).days>=7: 

                 print(f'Start Date: {start_date}, End Date: {end_date}')
                 print( data [start_date: end_date])
                 print (f'Duration: {end_date-start_date}')
"""
#%%finding density difference deoxygenation period_advance:
# subseting each year to     df_str_nomixing_{year} and df_str_{year}_{i+1}_14
from datetime import timedelta
    
for year in range(dens_diff_top_135.index.year.min(), dens_diff_top_135.index.year.max()+1):
   
    data = dens_diff_top_135.loc[dens_diff_top_135.index.year ==year]
    data_non_date_index=dens_diff_top_135.reset_index()
    
    criteria = (data <= -0.05) & \
              (data.shift(-1) <= -0.05) & \
              (data.shift(-2) <= -0.05) & \
              (data.shift(-3) <= -0.05) & \
              (data.shift(-4) <= -0.05) & \
              (data.shift(-5) <= -0.05) & \
              (data.shift(-6) <= -0.05) 
    
    true_criteria_dates= data[criteria].index
    
    # Initialize a list to hold the time series subsets and their initial indices
    time_series_subsets = []

    current_subset = [true_criteria_dates[0]]
    current_date = true_criteria_dates[0]
    current_index = 0
    
    for date in true_criteria_dates[1:]:
        if (date - current_date).days == 1:
            current_subset.append(date)
            current_date = date
        else:
            if len(current_subset) >= 7:
                time_series_subsets.append((current_subset[0], current_subset[-1]))

            current_subset = [date]
            current_date = date
            current_index += 1
    
    if len(current_subset) >= 7:
        time_series_subsets.append((current_subset[0], current_subset[-1]))

    for i, subset in enumerate(time_series_subsets):
        start_index = np.where(data_non_date_index['Datetime'] == subset[0])[0][0]
        end_index = np.where(data_non_date_index['Datetime'] == subset[1])[0][0]
        print(f"Subset {year}_{i+1}: Start: {subset[0]}, End: {subset[1]}, Indices: {start_index} - {end_index}")
        year_subset= daily_prof_Temp_DO_morpho_5years[subset[0]-timedelta(days=1): subset[1]]
        year_subset_2= daily_prof_Temp_DO_morpho_5years[subset[0]: subset[1]]
        var_name = f'df_str_{year}_{i+1}_14'# next time make str to deoxy
        var_name_2 = f'df_str_nomixing_{year}_{i+1}_14'
        globals()[var_name] = year_subset
        globals()[var_name_2] = year_subset_2




"""
Subset 2018_1: Start: 2018-05-08 00:00:00, End: 2018-09-05 00:00:00, Indices: 0 - 120
Subset 2019_1: Start: 2019-05-15 00:00:00, End: 2019-06-30 00:00:00, Indices: 219 - 265
Subset 2019_2: Start: 2019-07-12 00:00:00, End: 2019-08-30 00:00:00, Indices: 277 - 326
Subset 2020_1: Start: 2020-05-22 00:00:00, End: 2020-09-03 00:00:00, Indices: 431 - 535
Subset 2021_1: Start: 2021-05-13 00:00:00, End: 2021-08-27 00:00:00, Indices: 648 - 754
Subset 2022_1: Start: 2022-05-23 00:00:00, End: 2022-08-31 00:00:00, Indices: 860 - 960
"""        

    





#%%Testing the NOT++ codes for generic way of defining deoxygenation period


# From this function we create a boolen type array that checkes the meeting of a threshold for several consecutive days 
def consecutive_criteria(density_difference_top_meta, threshold , consecutive_days):
    criteria = None
    for i in range(consecutive_days):
        shift_data = density_difference_top_meta.shift(-i)
        condition = shift_data <= threshold
        if criteria is None:
            criteria = condition
        else:
            criteria = criteria & condition
    return criteria
	

# Function for findig subsets of days when they meet the condition 
def find_consecutive_ranges(dates , min_duration):
    onset_dates=[]
    offset_dates = []
    start_date = None
    end_date = None

    for date in dates:
        if end_date is None or (date - end_date).days == 1:
            end_date = date
            if start_date is None:
                start_date = date
        else:
            if start_date is not None and end_date is not None and (end_date - start_date).days >=min_duration:
                onset_dates.append(start_date)
                offset_dates.append(end_date)
                
            start_date = date
            end_date = date
    
    if start_date is not None and end_date is not None and (end_date - start_date).days >= min_duration:
        onset_dates.append(start_date)
        offset_dates.append(end_date)
    return onset_dates, offset_dates


# The inputs of finding deox period function are:
	
#1. dens_diff_top_meta= A dataframe hold the daily density difference from top most layer and above the hypolimnion with index of date time 
#2. dens_diff_threshold=threshold for density differences between top most layer and layer above the hypolimnion called metalimnion  
#3. consecutive_days_num= The number of consecutive days for meeting the critera for sake of presistancy  
#4. temp_surf 
#dens_diff_top_meta=density_diff_gotm_indexed.copy()


#dens_diff_top_meta= dens_diff_top_135
#temp_surf=temp_surf_1m
#%%new 
import pandas as pd
import numpy as np

def find_deox_period(dens_diff_top_meta, temp_surf, temp_lower_threshold=4, dens_diff_threshold=-0.05, consecutive_days_num=7):
    # Removing those days with surface temp of less than 4°C:
    df_surf_temp = pd.DataFrame({'temp_surf': temp_surf})
    df_surf_temp = df_surf_temp.set_index(dens_diff_top_meta.index)

    dens_diff_allyears_non_index = dens_diff_top_meta.reset_index()

    start_dates = []
    end_dates = []

    start_indices = []
    end_indices = []

    deox_duration = []
    replanishment_duration = []

    for year in range(dens_diff_top_meta.index.year.min(), dens_diff_top_meta.index.year.max() + 1):
        dens_diff_oneyear = dens_diff_top_meta.loc[dens_diff_top_meta.index.year == year]
        df_surf_temp_oneyear = df_surf_temp.loc[df_surf_temp.index.year == year]

        criteria = consecutive_criteria(dens_diff_oneyear, dens_diff_threshold, consecutive_days_num)
        true_criteria_dates_density = dens_diff_oneyear[criteria].index

        true_criteria_dates_temp = df_surf_temp_oneyear[df_surf_temp_oneyear['temp_surf'] > temp_lower_threshold].index

        # combination of temp threshold for surface, and density diff for consecutive days
        true_criteria_dates = true_criteria_dates_temp.intersection(true_criteria_dates_density)

        deox_start, deox_end = find_consecutive_ranges(true_criteria_dates, consecutive_days_num)

        start_dates.extend(deox_start)
        end_dates.extend(deox_end)

    for s, e in zip(start_dates, end_dates):
        start_index = np.where(dens_diff_allyears_non_index['Datetime'] == s)[0][0]
        end_index = np.where(dens_diff_allyears_non_index['Datetime'] == e)[0][0]

        start_indices.append(start_index)
        end_indices.append(end_index)

    deox_duration_deltas = np.array(end_dates) - np.array(start_dates)
    deox_duration = [delta.days + 1 for delta in deox_duration_deltas]

    replan_duration_deltas = np.array(start_dates[1:]) - np.roll(np.array(end_dates), 1)[1:]
    replanishment_duration = [np.nan] + [delta.days - 1 for delta in replan_duration_deltas]

    initial_cond_indices = np.array(start_indices) - 1

    # Extract the year from each date and count occurrences
    years = [date.year for date in start_dates]

    # Create a dictionary to store counts
    year_counts = {}

    # Create an array with the count of each year
    index_deox_period_in_year = []

    for year in years:
        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1
        index_deox_period_in_year.append(year_counts[year] - 1)

    # Create a dictionary with the collected data
    data = {
        'index_deox_period_in_year': index_deox_period_in_year,
        'start_dates': start_dates,
        'start_indices': start_indices,
        'initial_cond_indices': initial_cond_indices,
        'end_dates': end_dates,
        'end_indices': end_indices,
        'deox_duration': deox_duration,
        'replanishment_duration': replanishment_duration
    }

    # Create a DataFrame
    df = pd.DataFrame(data)
    df['start_dates'] = pd.to_datetime(df['start_dates'])
    df['end_dates'] = pd.to_datetime(df['end_dates'])

    df['end_dates_Jday'] = df['end_dates'].dt.dayofyear
    df['start_dates_Jday'] = df['start_dates'].dt.dayofyear
    df['year'] = df['start_dates'].dt.year

    return df



#%% Important rule for using up this function is that it is a data series 
# and no name for values but 6the oindex name should be 'Datetime'
"""
dens_diff_top_135
Out[360]: 
Datetime
2018-05-08   -0.119435
2018-05-09   -0.115375
2018-05-10   -0.106321
2018-05-11   -0.111240
2018-05-12   -0.182287
  
2022-11-03   -0.000597
2022-11-04    0.000276
2022-11-05   -0.000102
2022-11-06   -0.000100
2022-11-07    0.000387
Name: dens_diff_top_135m, Length: 1029, dtype: float64
"""
#%%testing using

    
df_deox_period_2018_2022=find_deox_period ( dens_diff_top_135 , temp_surf_1m)    
"""
	index_deox_period_in_year	start_dates	start_indices	initial_cond_indices	end_dates	end_indices	deox_duration	replanishment_duration
0	0	2018-05-08	0.0	-1.0	2018-09-05	120.0	121	
1	0	2019-05-15	219.0	218.0	2019-06-30	265.0	47	251.0
2	1	2019-07-12	277.0	276.0	2019-08-30	326.0	50	11.0
3	0	2020-05-22	431.0	430.0	2020-09-03	535.0	105	265.0
4	0	2021-05-13	648.0	647.0	2021-08-27	754.0	107	251.0
5	0	2022-05-23	860.0	859.0	2022-08-31	960.0	101	268.0

"""


for index, row in df_deox_period_2018_2022.iterrows():
    #print(f'Row {index}, Column index_deox_period_in_year:')
    
    print(row['index_deox_period_in_year'])
    print(row['start_indices'] , row['end_indices'])
    print(row['initial_cond_indices'])
    print(row['replanishment_duration'])
    
    
#%%dataframe 2019_2022 should be work on and needed to be filtterd:


dens_diff_top_135_2019_2022 = dens_diff_top_135[dens_diff_top_135.index.year > 2018]   

temp_surf_1m_2019_2022 = temp_surf_1m[temp_surf_1m.index.year > 2018]   

###############################################################
# temperature 2_D array filtering and having it for these years:

def two_D_array_from_df(df, values_name, index_name='Datetime', column_name='Z_m'):

    piv = df.pivot_table(
        index=index_name, columns=column_name, values=values_name)

    if df[column_name].min() < 0:
        piv = piv.sort_index(
            axis='columns', level=column_name, ascending=False)

    return (np.array(piv))


    
temp_2D_2019_2022_fullprof=two_D_array_from_df(daily_prof_Temp_DO_morpho_5years, 'Temp')
    
temp_2D_2019_2022_hypoprof=two_D_array_from_df(daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years['Z_m']<-13.5] , 'Temp')

DO_2D_2019_2022_hypoprof = np.full(temp_2D_2019_2022_hypoprof.shape, np.nan)


##########
df_deox_period_2019_2022=find_deox_period ( dens_diff_top_135_2019_2022 , temp_surf_1m_2019_2022)    

df_deox_period_2019_2022['num_day_of_year_start']=df_deox_period_2019_2022['start_dates'].dt.dayofyear

df_deox_period_2019_2022['num_day_of_year_end']=df_deox_period_2019_2022['end_dates'].dt.dayofyear

"""
	index_deox_period_in_year	start_dates	start_indices	initial_cond_indices	end_dates	end_indices	deox_duration	replanishment_duration	num_day_of_year_start	num_day_of_year_end
0	0	2019-05-15	28.0	27.0	2019-06-30	74.0	47		135	181
1	1	2019-07-12	86.0	85.0	2019-08-30	135.0	50	11.0	193	242
2	0	2020-05-22	240.0	239.0	2020-09-03	344.0	105	265.0	143	247
3	0	2021-05-13	457.0	456.0	2021-08-27	563.0	107	251.0	133	239
4	0	2022-05-23	669.0	668.0	2022-08-31	769.0	101	268.0	143	243

"""



for index, row in df_deox_period_2019_2022.iterrows():
    #print(f'Row {index}, Column index_deox_period_in_year:')
    print(row['index_deox_period_in_year'])
    print(row['start_indices'] , row['end_indices'])
    print(row['initial_cond_indices'])
    print(row['replanishment_duration'])
    
 
#%%dataframes with no mixing days 


#df_str_nomixing_2018_1_14= daily_prof_Temp_DO_morpho_5years['2018/05/08': '2018/09/05']
df_str_nomixing_2019_1_14=daily_prof_Temp_DO_morpho_5years['2019/05/15': '2019/06/30']
df_str_nomixing_2019_2_14=daily_prof_Temp_DO_morpho_5years['2019/07/12': '2019/08/30']
df_str_nomixing_2020_1_14=daily_prof_Temp_DO_morpho_5years['2020/05/22': '2020/09/03']
df_str_nomixing_2021_1_14=daily_prof_Temp_DO_morpho_5years['2021/05/13': '2021/08/27']
df_str_nomixing_2022_1_14=daily_prof_Temp_DO_morpho_5years['2022/05/23': '2022/08/31']





# including a day before onset values 
#df_str_nomixing_2018_1_14_below14= df_str_nomixing_2018_1_14[df_str_nomixing_2018_1_14['Z_m']<-13.5]
df_str_nomixing_2019_1_14_below14= df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m']<-13.5]
df_str_nomixing_2019_2_14_below14= df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m']<-13.5]
df_str_nomixing_2020_1_14_below14= df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m']<-13.5]
df_str_nomixing_2021_1_14_below14= df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m']<-13.5]
df_str_nomixing_2022_1_14_below14= df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m']<-13.5]

    

df_str_nomixing_2019_2022=pd.concat([df_str_nomixing_2019_1_14 , df_str_nomixing_2019_2_14 , df_str_nomixing_2020_1_14 , df_str_nomixing_2021_1_14 , df_str_nomixing_2022_1_14 ])
    




#%% Create subplots of each year to analyse DO differences of 13.5m and 14m   during deoxygenation period 


boundry_condition_2019_1=  df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m']==-13.5]['DO'] - df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m']==-14]['DO']

boundry_condition_2019_2=  df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m']==-13.5]['DO'] - df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m']==-14]['DO']

boundry_condition_2020_1=  df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m']==-13.5]['DO'] - df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m']==-14]['DO']

boundry_condition_2021_1=  df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m']==-13.5]['DO'] - df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m']==-14]['DO']

boundry_condition_2022_1=  df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m']==-13.5]['DO'] - df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m']==-14]['DO']




fig, axes = plt.subplots(3, 2, figsize=(20, 22))
# Plot for 2020_2021 calibration period

#axes[0, 0].plot(boundry_condition_2019_1.index, boundry_condition_2019_1)#, 'k--', label='Median model', alpha=0.9 )

axes[0, 0].scatter(boundry_condition_2019_1.index, boundry_condition_2019_1)#, 'k--', label='Median model', alpha=0.9 )
axes[0, 0].set_yscale('log')  # Set log scale for the y-axis
axes[0, 0].tick_params(axis='both', which='major', labelsize=15)  # Increase tick label font size



#axes[0, 1].plot(boundry_condition_2019_2.index, boundry_condition_2019_2)#, 'k--', label='Median model', alpha=0.9 )

axes[0, 1].scatter(boundry_condition_2019_2.index, boundry_condition_2019_2)#, 'k--', label='Median model', alpha=0.9 )
axes[0, 1].set_yscale('log')
axes[0, 1].tick_params(axis='both', which='major', labelsize=15)

#axes[1, 0].plot(boundry_condition_2020_1.index, boundry_condition_2020_1)#, 'k--', label='Median model', alpha=0.9 )

axes[1, 0].scatter(boundry_condition_2020_1.index, boundry_condition_2020_1)#, 'k--', label='Median model', alpha=0.9 )
axes[1, 0].set_yscale('log')
axes[1, 0].tick_params(axis='both', which='major', labelsize=15)

#axes[1, 1].plot(boundry_condition_2021_1.index, boundry_condition_2021_1)#, 'k--', label='Median model', alpha=0.9 )

axes[1, 1].scatter(boundry_condition_2021_1.index, boundry_condition_2021_1)#, 'k--', label='Median model', alpha=0.9 )
axes[1, 1].set_yscale('log')
axes[1, 1].tick_params(axis='both', which='major', labelsize=15)

#axes[2, 0].plot(boundry_condition_2022_1.index, boundry_condition_2022_1)#, 'k--', label='Median model', alpha=0.9 )

axes[2, 0].scatter(boundry_condition_2022_1.index, boundry_condition_2022_1)#, 'k--', label='Median model', alpha=0.9 )
axes[2, 0].set_yscale('log')
axes[2, 0].tick_params(axis='both', which='major', labelsize=15 , ratio= 45)




#%%

import matplotlib.pyplot as plt

# Assuming you have already defined boundry_condition_2019_1, boundry_condition_2019_2, etc.

fig, axes = plt.subplots(3, 2, figsize=(20, 22), constrained_layout=True, sharey=True)

# Plot for 2020_2021 calibration period

for ax, data in zip(axes.flatten(), [boundry_condition_2019_1, boundry_condition_2019_2,
                                     boundry_condition_2020_1, boundry_condition_2021_1,
                                     boundry_condition_2022_1]):
    ax.scatter(data.index, data)
    #ax.plot(data.index, data)
    ax.set_yscale('log')  # Set log scale for the y-axis
    ax.tick_params(axis='both', which='major', labelsize=24)  # Increase tick label font size

    # Rotate x-axis labels to 45 degrees
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)

# Set the same y-axis range for all subplots

for ax in axes.flatten():
    ax.set_ylim(10**-3, 1.5)

# Adjust layout to prevent clipping of tick-labels
plt.tight_layout()

plt.savefig("boundry_condition_each_year_separatly_scatter.png", dpi=300)









#%%testing the normality of boundry condition (all 4 years) for DO differences of 13.5m and 14m   during deoxygenation period 


boundry_condition= df_str_nomixing_2019_2022[df_str_nomixing_2019_2022['Z_m']==-13.5]['DO'] - df_str_nomixing_2019_2022[df_str_nomixing_2019_2022['Z_m']==-14]['DO']

      
#plotting the histogram 
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))

# Plot the distribution histogram
sns.histplot(np.array(boundry_condition), kde=True, color='grey', edgecolor='black', ax=ax1)#color='blue'
ax1.get_lines()[0].set_color('red') 
ax1.set_xlabel('Concentration difference [mg L$^{-1}$]')
ax1.set_ylabel('Frequency')
#ax1.set_title('Distribution Plot')

# Plot the Q-Q plot
stats.probplot(np.array(boundry_condition), dist="norm", plot=ax2)
ax2.set_title("")

# Modify the color of points in the Q-Q plot
ax2.get_lines()[0].set_markerfacecolor('grey')  # Set marker face color
ax2.get_lines()[0].set_markeredgecolor('grey')  # Set marker edge color
ax2.set_ylabel('Sample quantiles')
ax2.set_xlabel('Normal theorical quantiles')
# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('normality_test_boundry_condition.png', dpi= 300)



#%%the right-skewed or positive skewed distribution plot 

#===========the Shapiro–Wilk test is used for testing normality.
from scipy.stats import shapiro

# Perform the Shapiro-Wilk test
stat, p_value = shapiro(np.array(boundry_condition))

# Print the results
print(f"Shapiro-Wilk Test Statistic: {stat}, p-value: {p_value}")
if p_value > 0.05:
    print("The data appears to be normally distributed.")
else:
    print("The data does not appear to be normally distributed.")

#Shapiro-Wilk Test Statistic: 0.6680734157562256, p-value: 1.5730816674270114e-27
#The data does not appear to be normally distributed.
# if the Shapiro_wilk statictic was 1-> normal distributed 
#=========
from scipy.stats import anderson

# Perform the Anderson-Darling test
result = anderson(boundry_condition)

# Print the results
print(f"Anderson-Darling Test Statistic: {result.statistic}")
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < cv:
        print(f"At {sl * 100}% significance level, data appears to be normally distributed.")
    else:
        print(f"At {sl * 100}% significance level, data does not appear to be normally distributed.")

"""
Anderson-Darling Test Statistic: 18.00369069050913
At 1500.0% significance level, data does not appear to be normally distributed.
At 1000.0% significance level, data does not appear to be normally distributed.
At 500.0% significance level, data does not appear to be normally distributed.
At 250.0% significance level, data does not appear to be normally distributed.
At 100.0% significance level, data does not appear to be normally distributed.
"""
#==========
import statistics

median_value = statistics.median(np.array(boundry_condition))

print("The median is:", median_value)# 0.09890605479166614
#%%No Kz function of DO modelling :

    
def do_one_deox_nokz(params, hypo_morphology_vriables_grid, temp_hypo_dox , temp_hypo_inital_cond,
                         initial_cond_sat , duration_repl, delta_t):
    
    jv, ja, scale_subdaily = params
    V_r, A_s, A_l, dz, nl = hypo_morphology_vriables_grid

    temp_hypo_inital_cond_and_deox =  np.concatenate((temp_hypo_inital_cond.reshape(1, -1), temp_hypo_dox), axis=0)#np.concatenate((temp_hypo_inital_cond , temp_hypo_dox ))
    temp_hypo_for_jz_correction = 0.5*(temp_hypo_inital_cond_and_deox[ :-1 , :] + temp_hypo_dox[: , :])  # in shape of (day , depth)
 
    
    initial_cond = C_satur(temp_hypo_inital_cond, initial_cond_sat)
    num_time_steps_subdaily = int(1 / scale_subdaily)
    #delta_t = scale_subdaily * np.tile(delta_t, (num_time_steps_subdaily, 1)).transpose().flatten()

    m = len(delta_t)
    
    #temp_hypo_for_jz_correction_subdaily = np.repeat(temp_hypo_for_jz_correction, num_time_steps_subdaily, axis=0)
    #temp_hypo_for_jz_correction_subdaily = temp_hypo_for_jz_correction_subdaily.T# now: (depth, date)
    
    
    C = np.zeros(( m+1 , nl))
    C[0, :] = initial_cond

    for i in range(0, m):#temp_hypo_for_jz_correction_subdaily
        
        C[i+1, :]= C[i, :] - delta_t[i] * (Theta_j(temp_hypo_for_jz_correction[i, :])) *(  (A_l / V_r) * ja   + jv )
        #print("Press Enter to continue...")
        #input()
        #print( C[i+1, :] ) 
        #print(C[i, :])
        #print( temp_hypo_for_jz_correction[i, :])  


    
    
    
    #C=C.T
    C = np.where(C < 0, 0, C)

    C_dox = C[1:, :]
    #num_days = (C.shape[0]-1) // num_time_steps_subdaily
    #C_dox_3d = np.reshape(C_dox[:num_days * num_time_steps_subdaily], (num_days, num_time_steps_subdaily, -1))
    #C_deox_daily_model = np.mean(C_dox_3d, axis=1)

    #C_hypo_full_satur = C_satur(temp_hypo_dox, 1)
    #C_deox_daily_model = np.where(C_deox_daily_model > C_hypo_full_satur, C_hypo_full_satur, C_deox_daily_model)

    C_dox_ave_model = np.dot(C_dox, V_r) / sum(V_r)
    
    Do_ave_end = C_dox_ave_model[-1]
    temp_ave_end = np.dot(temp_hypo_dox[-1, :], V_r) / sum(V_r)
    sat_end = Do_ave_end / C_satur(temp_ave_end, 1)
    #sat_end =(estimate_satur_percentage ( Do_ave_end , temp_ave_end , altitude_m=10 ))/100
        
      
   

    return C_dox, sat_end # C_deox_ave_model,


    


    
#%%do_one_deoxygenation_implicit_working

def Theta_j(temp):
    theta = 1.087
    return (theta ** (temp - 20))



#kz_hypo_deox_subdaily=  np.ones(temp_hypo_dox.shape)*1.4*10**-7([7*10**-6, 6*10**-6 , 5*10**-6 , 4*10**-6 , 3*10**-6 , 2*10**-6 , 1*10**-6])
#kz_hypo_deox_daily= np.zeros(temp_hypo_dox.shape)*1.4*10**-7([7*10**-6, 6*10**-6 , 5*10**-6 , 4*10**-6 , 3*10**-6 , 2*10**-6 , 1*10**-6])


def do_one_deox_implicit(params, hypo_morphology_vriables_grid, temp_hypo_dox , temp_hypo_inital_cond,
initial_cond_sat , duration_repl, delta_t, kz_hypo_deox_daily):

    jv, ja, scale_subdaily = params
    V_r, A_s, A_l, dz, nl = hypo_morphology_vriables_grid


    # average of 2 consequtive:
    temp_hypo_inital_cond_and_deox =  np.concatenate((temp_hypo_inital_cond.reshape(1, -1), temp_hypo_dox), axis=0)#np.concatenate((temp_hypo_inital_cond , temp_hypo_dox ))
    temp_hypo_for_jz_correction = 0.5*(temp_hypo_inital_cond_and_deox[ :-1 , :] + temp_hypo_dox[: , :])  # in shape of (day , depth)

    # on that special day:
    #temp_hypo_for_jz_correction= temp_hypo_dox.copy()
    
    
    
    initial_cond = C_satur(temp_hypo_inital_cond, initial_cond_sat)
    num_time_steps_subdaily = int(1 / scale_subdaily)
    delta_t = scale_subdaily * np.tile(delta_t, (num_time_steps_subdaily, 1)).transpose().flatten()

    m = len(delta_t)
    
    temp_hypo_for_jz_correction_subdaily = np.repeat(temp_hypo_for_jz_correction, num_time_steps_subdaily, axis=0)
    temp_hypo_for_jz_correction_subdaily = temp_hypo_for_jz_correction_subdaily.T# now: (depth, date)

    Factor_dig = np.zeros((nl, nl))

    kz_hypo_deox_subdaily = np.repeat(kz_hypo_deox_daily, num_time_steps_subdaily, axis=0)
    
    
    kz_hypo_deox_subdaily = (24 * 3600 * kz_hypo_deox_subdaily).T

    kz_hypo_surf_deox_subdaily = np.median(kz_hypo_deox_subdaily[0 , :-1])# we don't intrested in the last day 

        
    
    C = np.zeros((nl, m+1))
    C[:, 0] = initial_cond

    for j in range(1, m+1):
        
        
        
        
        
        Factor_dig=np.diag([ 1 + 0 +delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1, j-1]/(V_r[0]*dz),#+ delta_t[j]*A_s[0]*kz[0,j]/(dz*V_r[0])  , 
                            1+ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]) + delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                            1+ delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]) + delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                            1+ delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]) + delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                            1+ delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]) + delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                            1+ delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]) + delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5]),
                            1+ delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]) + 0 ] , 0)- \
                    np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(V_r[0]*dz) , 
                                delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                                delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                                delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                                delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                                delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5])] , 1)- \
                        np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]),
                                    delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]), 
                                    delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]),
                                    delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]),
                                    delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]),
                                    delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]) ] , -1)
                        
    
                        
                        
            
        #print("Press Enter to continue...")
        #input()
        #print(Factor_dig )                
                        
        b = C[:, j-1].copy()
        
        
        #boundry condition with variable kz in first layer ogf hypolimnion (14m )
        ##############b[0] = b[0] + (0.0989060) * delta_t[j-1] * A_s[0] *  kz_hypo_deox_subdaily[0, j-1] /(dz * V_r[0])
        
       
        
        #boundry condition with median value of kz_jp_fortnightly_indailytimestep_2D_2019_2022 # 5.1896413109621045e-06
        b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] * kz_hypo_surf_deox_subdaily) /(dz * V_r[0])
        
        #print("Press Enter to continue...")
        #input()
        #print(b )   


        ##################original test with variable theta
        knows=b - (delta_t[j-1] * Theta_j(temp_hypo_for_jz_correction_subdaily[:, j-1])* (  jv + (A_l / V_r) * ja  ))
        
        
        #attribution test # average hypolimnion temp 2019-2022 in deox:11.8896
        #attribution test # average hypolimnion temp in calibration 2020, 2021: 10.52547
        #attribution test # average onset hypolimnion temp in calibration 2020, 2021: 7.797193135190584
        #attribution test # average from onset untill the anoxia(0.5) happens in deppest layer 2020 , 2021: 9.806014555691542
        #attribution test # average from onset untill the hypoxia(2) happens in deppest layer  2020 , 2021: 9.460405011459684
        #knows=b - (delta_t[j-1] * Theta_j(9.460405011459684 )* (  jv + (A_l / V_r) * ja  ))
        
        
        
        #print("Press Enter to continue...")
        #input()
        #print(knows )   
        
        
        solution = np.linalg.solve(Factor_dig, knows)
       
        
        
        C[:, j] = solution
       
        C = np.where(C < 0, 0, C)
        #print("Press Enter to continue...")
        #input()
        #print(C[: , j] )   
        #plt.plot( solution , np.array([-14, -14.5, -15, -15.5, -16, -16.5, -17]) )
        #plt.show()
        

    C = np.where(C < 0, 0, C).T

    C_dox = C[1:, :]
    num_days = (C.shape[0]-1) // num_time_steps_subdaily
    C_dox_3d = np.reshape(C_dox[:num_days * num_time_steps_subdaily], (num_days, num_time_steps_subdaily, -1))
    C_deox_daily_model = np.mean(C_dox_3d, axis=1)

    C_hypo_full_satur = C_satur(temp_hypo_dox, 1)
    C_deox_daily_model = np.where(C_deox_daily_model > C_hypo_full_satur, C_hypo_full_satur, C_deox_daily_model)



    #count_satur_condition = np.count_nonzero(C_deox_daily_model == C_hypo_full_satur)
    satur_condition_array = np.where(C_deox_daily_model == C_hypo_full_satur, 1, 0)

    C_deox_ave_model = np.dot(C_deox_daily_model, V_r) / sum(V_r)
    
    Do_ave_end = C_deox_ave_model[-1]
    temp_ave_end = np.dot(temp_hypo_dox[-1, :], V_r) / sum(V_r)
    sat_end = Do_ave_end / C_satur(temp_ave_end, 1)
    #sat_end =(estimate_satur_percentage ( Do_ave_end , temp_ave_end , altitude_m=10 ))/100
        
    #print("Press Enter to continue...")
    #input()
    #print(sat_end )    
   

    return C_deox_daily_model, sat_end , satur_condition_array# C_deox_ave_model,



#%%do_model_comprehensive that covers the whole timeseries prediction 

def do_model_comprehensive(params, dens_diff_top_meta ,temp_surf, hypo_morphology_vriables_grid 
                           ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 ):
    
    DO_2D_hypo_deox_comp = np.full(temp_hypo_2D.shape, np.nan)
    temp_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    kz_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    full_sat_hypo_condition= np.full(temp_hypo_2D.shape, np.nan)
    df_deox_periods_info=find_deox_period ( dens_diff_top_meta , temp_surf )  
    
    for index, row in df_deox_periods_info.iterrows():
        
        index_deox_period_in_year=row['index_deox_period_in_year']
        temp_hypo_dox= temp_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
        temp_hypo_inital_cond= temp_hypo_2D[int(row['initial_cond_indices'])]
        duration_repl=row['replanishment_duration']
        deox_duration= row['deox_duration']
        delta_t=np.ones(deox_duration)# for this case study but it could not all 1 for other case study 

        #for jp it shoould put nan for other days:
        #kz_hypo_deox_daily=np.zeros (temp_hypo_dox.shape )#*kz_hypo_2D# # manually allocte for obsrvational years but for the future gotm simulation the kz vslues has indexs of +1 to the start_indices and end_indices 
        
        #for obs:
        kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
             
        
        #for gotm:
        #kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices'])+1 : int(row['end_indices'])+2]
         
        if index_deox_period_in_year==0:
            initial_cond_sat=1
            C_deox_daily_model, sat_end , condition_array=do_one_deox_implicit(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                             temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t,kz_hypo_deox_daily)   
            #C_deox_daily_model, sat_end= do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #                 temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t)
            
            
        else:
            
            
            increase_sat_repl = duration_repl * (replanishmnet_rate / 100)
        
            initial_cond_sat = sat_end + increase_sat_repl

            C_deox_daily_model, sat_end , condition_array =do_one_deox_implicit(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                     temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t,kz_hypo_deox_daily)
            #C_deox_daily_model, sat_end = do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #         temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t)
            
            
            
        
        DO_2D_hypo_deox_comp[int(row['start_indices']) : int(row['end_indices'])+1 ]=C_deox_daily_model   
        temp_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=temp_hypo_dox   
        kz_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=kz_hypo_deox_daily   
        #full_sat_hypo_condition[int(row['start_indices']) : int(row['end_indices'])+1 ]=condition_array
    
    
    return DO_2D_hypo_deox_comp , temp_2D_hypo_deox_comp , kz_2D_hypo_deox_comp# , full_sat_hypo_condition



#%%DO Modelling for GOTM GRIDS
def do_one_deox_implicit_gotm(params, hypo_morpho_vriables_gotm_grid, temp_hypo_dox , temp_hypo_inital_cond,
initial_cond_sat , duration_repl, delta_t, kz_hypo_deox_daily):# , temp_ave_hypo_2020_2021):#####9.299490575422336 rcp85 for same dates of onset to deep hypoxia  #####9.460405011459684):obs 2020 and 2021 from onset to first hypoxia#############, temp_ave_hypo_2020_2021):

    jv, ja, scale_subdaily = params
    V_r, A_s, A_l, dz, nl = hypo_morpho_vriables_gotm_grid


    # average of 2 consequtive:
    temp_hypo_inital_cond_and_deox =  np.concatenate((temp_hypo_inital_cond.reshape(1, -1), temp_hypo_dox), axis=0)#np.concatenate((temp_hypo_inital_cond , temp_hypo_dox ))
    temp_hypo_for_jz_correction = 0.5*(temp_hypo_inital_cond_and_deox[ :-1 , :] + temp_hypo_dox[: , :])  # in shape of (day , depth)

    # on that special day:
    ##########temp_hypo_for_jz_correction =temp_hypo_dox.copy()
    
    
    # original runs 
    initial_cond = C_satur(temp_hypo_inital_cond, initial_cond_sat)
    
    
    
    num_time_steps_subdaily = int(1 / scale_subdaily)
    delta_t = scale_subdaily * np.tile(delta_t, (num_time_steps_subdaily, 1)).transpose().flatten()

    m = len(delta_t)
    
    temp_hypo_for_jz_correction_subdaily = np.repeat(temp_hypo_for_jz_correction, num_time_steps_subdaily, axis=0)
    temp_hypo_for_jz_correction_subdaily = temp_hypo_for_jz_correction_subdaily.T# now: (depth, date)

    Factor_dig = np.zeros((nl, nl))

    kz_hypo_deox_subdaily = np.repeat(kz_hypo_deox_daily, num_time_steps_subdaily, axis=0)
    
    
    kz_hypo_deox_subdaily = (24 * 3600 * kz_hypo_deox_subdaily).T

    kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])
    
    C = np.zeros((nl, m+1))
    C[:, 0] = initial_cond

    for j in range(1, m+1):
        
        
        
        
        
        Factor_dig=np.diag([ 1 + 0+delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1, j-1]/(V_r[0]*dz),#- delta_t[j]*A_s[0]*kz[0,j]/(dz*V_r[0])  , 
                            1+ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]) + delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                            1+ delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]) + delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                            1+ delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]) + delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                            1+ delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]) + delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                            1+ delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]) + delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5]),
                            1+ delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]) + delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[6]),
                            1+ delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[7]) + delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[7]), 
                            1+ delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[8]) + delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[8]),
                            1+ delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[9]) + delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[9]), 
                            1+ delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[10]) + delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[10]),
                            1+ delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[11]) + delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[11]),
                            1+ delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[12]) + delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[12]),
                            1+ delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[13]) + 0 ] , 0)- \
                    np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(V_r[0]*dz) , 
                                delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                                delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                                delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                                delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                                delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5]),
                                delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[6]), 
                                delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[7]),
                                delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[8]),
                                delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[9]),
                                delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[10]),
                                delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[11]),
                                delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[12])] , 1)- \
                        np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]),
                                    delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]), 
                                    delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]),
                                    delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]),
                                    delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]),
                                    delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]),
                                    delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[7]),
                                    delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[8]),
                                    delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[9]),
                                    delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[10]),
                                    delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[11]),
                                    delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[12]),                                    
                                    delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[13]) ] , -1)
                        
    
                        
                        
            
        #print("Press Enter to continue...")
        #input()
        #print(Factor_dig )                
                        
        b = C[:, j-1].copy()
        ###########b[0] = b[0] + (0.0989060) * delta_t[j-1] * A_s[0] * kz_hypo_deox_subdaily[0, j-1] / (dz * V_r[0])
        
        b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
        
        #print("Press Enter to continue...")
        #input()
        #print(b )   
        
        
        #################original and variable theta
        knows=b - (delta_t[j-1] * Theta_j(temp_hypo_for_jz_correction_subdaily[:, j-1])* (  jv +(A_l / V_r) * ja  ))
        
        
        #############attribution test #with fixed theta of average hypolimnion temp 2019-2022 in deox:11.8896
        #############knows=b - (delta_t[j-1] * Theta_j(10.52547)* (  jv +(A_l / V_r) * ja  ))
        
        
        
        
        #############attribution test #with fixed theta of 9.460405011459684 (temp_hypo_ave_onset_deephypoxia)
        #############knows=b - (delta_t[j-1] * Theta_j(temp_ave_hypo_2020_2021)* (  jv +(A_l / V_r) * ja  ))
        

        
        
        #print("Press Enter to continue...")
        #input()
        #print(knows )   
        
        
        solution = np.linalg.solve(Factor_dig, knows)
       
        
        
        C[:, j] = solution
       
        C = np.where(C < 0, 0, C)
        
        

    C = np.where(C < 0, 0, C).T

    C_dox = C[1:, :]
    num_days = (C.shape[0]-1) // num_time_steps_subdaily
    C_dox_3d = np.reshape(C_dox[:num_days * num_time_steps_subdaily], (num_days, num_time_steps_subdaily, -1))
    C_deox_daily_model = np.mean(C_dox_3d, axis=1)

    C_hypo_full_satur = C_satur(temp_hypo_dox, 1)
    C_deox_daily_model = np.where(C_deox_daily_model > C_hypo_full_satur, C_hypo_full_satur, C_deox_daily_model)
    
    #count_satur_condition = np.count_nonzero(C_deox_daily_model == C_hypo_full_satur)
    satur_condition_array = np.where(C_deox_daily_model == C_hypo_full_satur, 1, 0)

    
    C_deox_ave_model = np.dot(C_deox_daily_model, V_r) / sum(V_r)
    
    Do_ave_end = C_deox_ave_model[-1]
    temp_ave_end = np.dot(temp_hypo_dox[-1, :], V_r) / sum(V_r)
    sat_end = Do_ave_end / C_satur(temp_ave_end, 1)
    #sat_end =(estimate_satur_percentage ( Do_ave_end , temp_ave_end , altitude_m=10 ))/100
        
    #print("Press Enter to continue...")
    #input()
    #print(sat_end )    
   

    return C_deox_daily_model, sat_end  ,  satur_condition_array#count_satur_condition , C_deox_ave_model,

#########==========================================================================
def do_model_comprehensive_gotm(params, dens_diff_top_meta ,temp_surf, hypo_morphology_vriables_grid ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 ):#,temp_ave_hypo_2020_2021, replanishmnet_rate= 2.7946 ):#=9.299490575422336: ave temp in RCPs of four model#9.460405011459684
                           
    
    DO_2D_hypo_deox_comp = np.full(temp_hypo_2D.shape, np.nan)
    temp_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    kz_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    full_sat_hypo_condition= np.full(temp_hypo_2D.shape, np.nan)
    df_deox_periods_info=find_deox_period ( dens_diff_top_meta , temp_surf)  
    
    for index, row in df_deox_periods_info.iterrows():
        
        index_deox_period_in_year=row['index_deox_period_in_year']
        temp_hypo_dox= temp_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
        temp_hypo_inital_cond= temp_hypo_2D[int(row['initial_cond_indices'])]
        duration_repl=row['replanishment_duration']
        deox_duration= row['deox_duration']
        delta_t=np.ones(deox_duration)# for this case study but it could not all 1 for other case study 

        #for jp it shoould put nan for other days:
        #kz_hypo_deox_daily=np.zeros (temp_hypo_dox.shape )#*kz_hypo_2D# # manually allocte for obsrvational years but for the future gotm simulation the kz vslues has indexs of +1 to the start_indices and end_indices 
        
        #for obs:
        #kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
             
        
        #for gotm:
        kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices'])+1 : int(row['end_indices'])+2]
         
        if index_deox_period_in_year==0:
            initial_cond_sat=1
            C_deox_daily_model, sat_end , condition_array=do_one_deox_implicit_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                             temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)   
            #C_deox_daily_model, sat_end= do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #                 temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t)
            
            
        else:
            
            
            increase_sat_repl = duration_repl * (replanishmnet_rate / 100)
        
            initial_cond_sat = sat_end + increase_sat_repl

            C_deox_daily_model, sat_end ,  condition_array =do_one_deox_implicit_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                     temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)
            #C_deox_daily_model, sat_end = do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #         temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t)
            
            
            
        
        DO_2D_hypo_deox_comp[int(row['start_indices']) : int(row['end_indices'])+1 ]=C_deox_daily_model   
        temp_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=temp_hypo_dox   
        kz_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=kz_hypo_deox_daily   
        full_sat_hypo_condition[int(row['start_indices']) : int(row['end_indices'])+1 ]=condition_array
    
    return DO_2D_hypo_deox_comp , temp_2D_hypo_deox_comp, kz_2D_hypo_deox_comp , full_sat_hypo_condition


#%%Mixing includ in DO prediction 
#temp_gfdl_his_hypo_TB

def mixing_incl_do_model_comprehensive_gotm(params, dens_diff_top_meta ,temp_surf, hypo_morphology_vriables_grid ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 ):#,temp_ave_hypo_2020_2021, replanishmnet_rate= 2.7946 ):#=9.299490575422336: ave temp in RCPs of four model#9.460405011459684
                           
    temp_2D_mixing_incl_comp =np.copy(temp_hypo_2D)    
    DO_2D_mixing_incl_comp = C_satur(temp_2D_mixing_incl_comp, 1)

    kz_2D_mixing_incl_comp =np.copy(kz_hypo_2D)
    full_sat_hypo_condition= np.full(temp_hypo_2D.shape, np.nan)
    df_deox_periods_info=find_deox_period ( dens_diff_top_meta , temp_surf)  
    
    for index, row in df_deox_periods_info.iterrows():
        
        index_deox_period_in_year=row['index_deox_period_in_year']
        temp_hypo_dox= temp_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
        temp_hypo_inital_cond= temp_hypo_2D[int(row['initial_cond_indices'])]
        duration_repl=row['replanishment_duration']
        deox_duration= row['deox_duration']
        delta_t=np.ones(deox_duration)# for this case study but it could not all 1 for other case study 

        #for jp it shoould put nan for other days:
        #kz_hypo_deox_daily=np.zeros (temp_hypo_dox.shape )#*kz_hypo_2D# # manually allocte for obsrvational years but for the future gotm simulation the kz vslues has indexs of +1 to the start_indices and end_indices 
        
        #for obs:
        #kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
             
        
        #for gotm:
        kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices'])+1 : int(row['end_indices'])+2]
         
        if index_deox_period_in_year==0:
            initial_cond_sat=1
            C_deox_daily_model, sat_end , condition_array=do_one_deox_implicit_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                             temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)   

        else:
            
            
            increase_sat_repl = duration_repl * (replanishmnet_rate / 100)
        
            initial_cond_sat = sat_end + increase_sat_repl
            
            
            #####repl###
            temp_repl=temp_hypo_2D[int(row['start_indices'])-int(row['replanishment_duration'])+1 : int(row['start_indices'])]
            
            sat_in_repl= np.zeros(temp_repl.shape)
            for i in range (temp_repl.shape[0] ):
                sat_in_repl[i, :]= sat_end+ (i+1)*replanishmnet_rate
                
            C_rep_daily=  C_satur(temp_repl, sat_in_repl/100)
            
            DO_2D_mixing_incl_comp[int(row['start_indices'])-int(row['replanishment_duration'])+1 : int(row['start_indices'])]=C_rep_daily
            ############
            
            C_deox_daily_model, sat_end ,  condition_array =do_one_deox_implicit_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                     temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)

            
        
        DO_2D_mixing_incl_comp[int(row['start_indices']) : int(row['end_indices'])+1 ]=C_deox_daily_model   
        
        
    return DO_2D_mixing_incl_comp , temp_2D_mixing_incl_comp, kz_2D_mixing_incl_comp 

#%% Function for rcp26 testing fixed values of DO 

def do_one_deox_implicit_gotm_rcp26_test(params, hypo_morpho_vriables_gotm_grid, temp_hypo_dox , temp_hypo_inital_cond,
initial_cond_sat , duration_repl, delta_t, kz_hypo_deox_daily):# , temp_ave_hypo_2020_2021):#####9.299490575422336 rcp85 for same dates of onset to deep hypoxia  #####9.460405011459684):obs 2020 and 2021 from onset to first hypoxia#############, temp_ave_hypo_2020_2021):

    jv, ja, scale_subdaily = params
    V_r, A_s, A_l, dz, nl = hypo_morpho_vriables_gotm_grid


    # average of 2 consequtive:
    temp_hypo_inital_cond_and_deox =  np.concatenate((temp_hypo_inital_cond.reshape(1, -1), temp_hypo_dox), axis=0)#np.concatenate((temp_hypo_inital_cond , temp_hypo_dox ))
    temp_hypo_for_jz_correction = 0.5*(temp_hypo_inital_cond_and_deox[ :-1 , :] + temp_hypo_dox[: , :])  # in shape of (day , depth)

    # on that special day:
    ##########temp_hypo_for_jz_correction =temp_hypo_dox.copy()
    
    
    # original runs 
    initial_cond = np.repeat(12.298 ,len(V_r) , axis=0)
    
    
    
    num_time_steps_subdaily = int(1 / scale_subdaily)
    delta_t = scale_subdaily * np.tile(delta_t, (num_time_steps_subdaily, 1)).transpose().flatten()

    m = len(delta_t)
    
    temp_hypo_for_jz_correction_subdaily = np.repeat(temp_hypo_for_jz_correction, num_time_steps_subdaily, axis=0)
    temp_hypo_for_jz_correction_subdaily = temp_hypo_for_jz_correction_subdaily.T# now: (depth, date)

    Factor_dig = np.zeros((nl, nl))

    kz_hypo_deox_subdaily = np.repeat(kz_hypo_deox_daily, num_time_steps_subdaily, axis=0)
    
    
    kz_hypo_deox_subdaily = (24 * 3600 * kz_hypo_deox_subdaily).T

    kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])
    
    C = np.zeros((nl, m+1))
    C[:, 0] = initial_cond

    for j in range(1, m+1):
        
        
        
        
        
        Factor_dig=np.diag([ 1 + 0+delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1, j-1]/(V_r[0]*dz),#- delta_t[j]*A_s[0]*kz[0,j]/(dz*V_r[0])  , 
                            1+ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]) + delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                            1+ delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]) + delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                            1+ delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]) + delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                            1+ delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]) + delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                            1+ delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]) + delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5]),
                            1+ delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]) + delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[6]),
                            1+ delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[7]) + delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[7]), 
                            1+ delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[8]) + delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[8]),
                            1+ delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[9]) + delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[9]), 
                            1+ delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[10]) + delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[10]),
                            1+ delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[11]) + delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[11]),
                            1+ delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[12]) + delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[12]),
                            1+ delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[13]) + 0 ] , 0)- \
                    np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(V_r[0]*dz) , 
                                delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                                delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                                delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                                delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                                delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5]),
                                delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[6]), 
                                delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[7]),
                                delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[8]),
                                delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[9]),
                                delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[10]),
                                delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[11]),
                                delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[12])] , 1)- \
                        np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]),
                                    delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]), 
                                    delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]),
                                    delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]),
                                    delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]),
                                    delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]),
                                    delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[7]),
                                    delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[8]),
                                    delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[9]),
                                    delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[10]),
                                    delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[11]),
                                    delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[12]),                                    
                                    delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[13]) ] , -1)
                        
    
                        
                        
            
        #print("Press Enter to continue...")
        #input()
        #print(Factor_dig )                
                        
        b = C[:, j-1].copy()
        ###########b[0] = b[0] + (0.0989060) * delta_t[j-1] * A_s[0] * kz_hypo_deox_subdaily[0, j-1] / (dz * V_r[0])
        
        b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
        
        #print("Press Enter to continue...")
        #input()
        #print(b )   
        
        
        #################original and variable theta
        knows=b - (delta_t[j-1] * Theta_j(temp_hypo_for_jz_correction_subdaily[:, j-1])* (  jv +(A_l / V_r) * ja  ))
        
        
        #############attribution test #with fixed theta of average hypolimnion temp 2019-2022 in deox:11.8896
        #############knows=b - (delta_t[j-1] * Theta_j(10.52547)* (  jv +(A_l / V_r) * ja  ))
        
        
        
        
        #############attribution test #with fixed theta of 9.460405011459684 (temp_hypo_ave_onset_deephypoxia)
        #############knows=b - (delta_t[j-1] * Theta_j(temp_ave_hypo_2020_2021)* (  jv +(A_l / V_r) * ja  ))
        

        
        
        #print("Press Enter to continue...")
        #input()
        #print(knows )   
        
        
        solution = np.linalg.solve(Factor_dig, knows)
       
        
        
        C[:, j] = solution
       
        C = np.where(C < 0, 0, C)
        
        

    C = np.where(C < 0, 0, C).T

    C_dox = C[1:, :]
    num_days = (C.shape[0]-1) // num_time_steps_subdaily
    C_dox_3d = np.reshape(C_dox[:num_days * num_time_steps_subdaily], (num_days, num_time_steps_subdaily, -1))
    C_deox_daily_model = np.mean(C_dox_3d, axis=1)

    C_hypo_full_satur = C_satur(temp_hypo_dox, 1)
    C_deox_daily_model = np.where(C_deox_daily_model > C_hypo_full_satur, C_hypo_full_satur, C_deox_daily_model)
    
    #count_satur_condition = np.count_nonzero(C_deox_daily_model == C_hypo_full_satur)
    satur_condition_array = np.where(C_deox_daily_model == C_hypo_full_satur, 1, 0)

    
    C_deox_ave_model = np.dot(C_deox_daily_model, V_r) / sum(V_r)
    
    Do_ave_end = C_deox_ave_model[-1]
    temp_ave_end = np.dot(temp_hypo_dox[-1, :], V_r) / sum(V_r)
    sat_end = Do_ave_end / C_satur(temp_ave_end, 1)
    #sat_end =(estimate_satur_percentage ( Do_ave_end , temp_ave_end , altitude_m=10 ))/100
        
    #print("Press Enter to continue...")
    #input()
    #print(sat_end )    
   

    return C_deox_daily_model, sat_end  ,  satur_condition_array#count_satur_condition , C_deox_ave_model,

#########==========================================================================
def do_model_comprehensive_gotm_rcp26_test(params, dens_diff_top_meta ,temp_surf, hypo_morphology_vriables_grid ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 ):#,temp_ave_hypo_2020_2021, replanishmnet_rate= 2.7946 ):#=9.299490575422336: ave temp in RCPs of four model#9.460405011459684
                           
    
    DO_2D_hypo_deox_comp = np.full(temp_hypo_2D.shape, np.nan)
    temp_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    kz_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    full_sat_hypo_condition= np.full(temp_hypo_2D.shape, np.nan)
    df_deox_periods_info=find_deox_period ( dens_diff_top_meta , temp_surf)  
    
    for index, row in df_deox_periods_info.iterrows():
        
        index_deox_period_in_year=row['index_deox_period_in_year']
        temp_hypo_dox= temp_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
        temp_hypo_inital_cond= temp_hypo_2D[int(row['initial_cond_indices'])]
        duration_repl=row['replanishment_duration']
        deox_duration= row['deox_duration']
        delta_t=np.ones(deox_duration)# for this case study but it could not all 1 for other case study 

        #for jp it shoould put nan for other days:
        #kz_hypo_deox_daily=np.zeros (temp_hypo_dox.shape )#*kz_hypo_2D# # manually allocte for obsrvational years but for the future gotm simulation the kz vslues has indexs of +1 to the start_indices and end_indices 
        
        #for obs:
        #kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
             
        
        #for gotm:
        kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices'])+1 : int(row['end_indices'])+2]
         
        if index_deox_period_in_year==0:
            initial_cond_sat=1
            C_deox_daily_model, sat_end , condition_array=do_one_deox_implicit_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                             temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)   
            #C_deox_daily_model, sat_end= do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #                 temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t)
            
            
        else:
            
            
            increase_sat_repl = duration_repl * (replanishmnet_rate / 100)
        
            initial_cond_sat = sat_end + increase_sat_repl

            C_deox_daily_model, sat_end ,  condition_array =do_one_deox_implicit_gotm_rcp26_test(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                     temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)
            #C_deox_daily_model, sat_end = do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #         temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t)
            
            
            
        
        DO_2D_hypo_deox_comp[int(row['start_indices']) : int(row['end_indices'])+1 ]=C_deox_daily_model   
        temp_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=temp_hypo_dox   
        kz_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=kz_hypo_deox_daily   
        full_sat_hypo_condition[int(row['start_indices']) : int(row['end_indices'])+1 ]=condition_array
    
    return DO_2D_hypo_deox_comp , temp_2D_hypo_deox_comp, kz_2D_hypo_deox_comp , full_sat_hypo_condition


#%%Mixing includ in DO prediction 
#temp_gfdl_his_hypo_TB

def mixing_incl_do_model_comprehensive_gotm_rcp26_test(params, dens_diff_top_meta ,temp_surf, hypo_morphology_vriables_grid ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 ):#,temp_ave_hypo_2020_2021, replanishmnet_rate= 2.7946 ):#=9.299490575422336: ave temp in RCPs of four model#9.460405011459684
                           
    temp_2D_mixing_incl_comp =np.copy(temp_hypo_2D)    
    DO_2D_mixing_incl_comp = C_satur(temp_2D_mixing_incl_comp, 1)

    kz_2D_mixing_incl_comp =np.copy(kz_hypo_2D)
    full_sat_hypo_condition= np.full(temp_hypo_2D.shape, np.nan)
    df_deox_periods_info=find_deox_period ( dens_diff_top_meta , temp_surf)  
    
    for index, row in df_deox_periods_info.iterrows():
        
        index_deox_period_in_year=row['index_deox_period_in_year']
        temp_hypo_dox= temp_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
        temp_hypo_inital_cond= temp_hypo_2D[int(row['initial_cond_indices'])]
        duration_repl=row['replanishment_duration']
        deox_duration= row['deox_duration']
        delta_t=np.ones(deox_duration)# for this case study but it could not all 1 for other case study 

        #for jp it shoould put nan for other days:
        #kz_hypo_deox_daily=np.zeros (temp_hypo_dox.shape )#*kz_hypo_2D# # manually allocte for obsrvational years but for the future gotm simulation the kz vslues has indexs of +1 to the start_indices and end_indices 
        
        #for obs:
        #kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
             
        
        #for gotm:
        kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices'])+1 : int(row['end_indices'])+2]
         
        if index_deox_period_in_year==0:
            initial_cond_sat=1
            C_deox_daily_model, sat_end , condition_array=do_one_deox_implicit_gotm_rcp26_test(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                             temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)   

        else:
            
            
            increase_sat_repl = duration_repl * (replanishmnet_rate / 100)
        
            initial_cond_sat = sat_end + increase_sat_repl

            #####repl
            temp_repl=temp_hypo_2D[int(row['start_indices'])-int(row['replanishment_duration'])+1 : int(row['start_indices'])]
            
            sat_in_repl= np.zeros(temp_repl.shape)
            for i in range (temp_repl.shape[0] ):
                sat_in_repl[i, :]= sat_end+ (i+1)*replanishmnet_rate
                
            C_rep_daily=  C_satur(temp_repl, sat_in_repl/100)
            
            DO_2D_mixing_incl_comp[int(row['start_indices'])-int(row['replanishment_duration'])+1 : int(row['start_indices'])]=C_rep_daily
            
            ######

            C_deox_daily_model, sat_end ,  condition_array =do_one_deox_implicit_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                     temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t,kz_hypo_deox_daily )#, temp_ave_hypo_2020_2021)

            
        
        DO_2D_mixing_incl_comp[int(row['start_indices']) : int(row['end_indices'])+1 ]=C_deox_daily_model   
        
    return DO_2D_mixing_incl_comp , temp_2D_mixing_incl_comp, kz_2D_mixing_incl_comp 



#%%DO Modelling for GOTM GRIDS but only with VHOD 
# used for definding management scenario 
def do_one_deox_implicit_VHOD_gotm(params, hypo_morpho_vriables_gotm_grid, temp_hypo_dox , temp_hypo_inital_cond,
initial_cond_sat , duration_repl, delta_t, kz_hypo_deox_daily ):#####9.299490575422336 rcp85 for same dates of onset to deep hypoxia  #####9.460405011459684):obs 2020 and 2021 from onset to first hypoxia#############, temp_ave_hypo_2020_2021):

    jz, scale_subdaily = params
    V_r, A_s, A_l, dz, nl = hypo_morpho_vriables_gotm_grid


    # average of 2 consequtive:
    temp_hypo_inital_cond_and_deox =  np.concatenate((temp_hypo_inital_cond.reshape(1, -1), temp_hypo_dox), axis=0)#np.concatenate((temp_hypo_inital_cond , temp_hypo_dox ))
    temp_hypo_for_jz_correction = 0.5*(temp_hypo_inital_cond_and_deox[ :-1 , :] + temp_hypo_dox[: , :])  # in shape of (day , depth)

    # on that special day:
    ##########temp_hypo_for_jz_correction =temp_hypo_dox.copy()
    
    
    # original runs 
    #initial_cond = C_satur(temp_hypo_inital_cond, initial_cond_sat)
    
    
    #######1. attribution test on increasemnet of initial condition with the slope* 80=0.262062
    #######initial_cond = C_satur(temp_hypo_inital_cond, initial_cond_sat)+0.262062# 0.262062is slope*80 years for attribution test of initial condition of RCP26
    
    initial_cond = np.repeat(12,len(V_r) , axis=0)
    
    num_time_steps_subdaily = int(1 / scale_subdaily)
    delta_t = scale_subdaily * np.tile(delta_t, (num_time_steps_subdaily, 1)).transpose().flatten()

    m = len(delta_t)
    
    temp_hypo_for_jz_correction_subdaily = np.repeat(temp_hypo_for_jz_correction, num_time_steps_subdaily, axis=0)
    temp_hypo_for_jz_correction_subdaily = temp_hypo_for_jz_correction_subdaily.T# now: (depth, date)

    Factor_dig = np.zeros((nl, nl))

    kz_hypo_deox_subdaily = np.repeat(kz_hypo_deox_daily, num_time_steps_subdaily, axis=0)
    
    
    kz_hypo_deox_subdaily = (24 * 3600 * kz_hypo_deox_subdaily).T

    kz_hypo_surf_deox_subdaily=np.median(kz_hypo_deox_subdaily[0 , :-1])
    
    C = np.zeros((nl, m+1))
    C[:, 0] = initial_cond

    for j in range(1, m+1):
        
        
        
        
        
        Factor_dig=np.diag([ 1 + 0+delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1, j-1]/(V_r[0]*dz),#- delta_t[j]*A_s[0]*kz[0,j]/(dz*V_r[0])  , 
                            1+ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]) + delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                            1+ delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]) + delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                            1+ delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]) + delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                            1+ delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]) + delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                            1+ delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]) + delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5]),
                            1+ delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]) + delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[6]),
                            1+ delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[7]) + delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[7]), 
                            1+ delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[8]) + delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[8]),
                            1+ delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[9]) + delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[9]), 
                            1+ delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[10]) + delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[10]),
                            1+ delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[11]) + delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[11]),
                            1+ delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[12]) + delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[12]),
                            1+ delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[13]) + 0 ] , 0)- \
                    np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(V_r[0]*dz) , 
                                delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[1]),
                                delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[2]), 
                                delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[3]),
                                delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[4]),
                                delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[5]),
                                delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[6]), 
                                delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[7]),
                                delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[8]),
                                delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[9]),
                                delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[10]),
                                delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[11]),
                                delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[12])] , 1)- \
                        np.diag([ delta_t[j-1]*A_s[1]*kz_hypo_deox_subdaily[1,j-1]/(dz*V_r[1]),
                                    delta_t[j-1]*A_s[2]*kz_hypo_deox_subdaily[2,j-1]/(dz*V_r[2]), 
                                    delta_t[j-1]*A_s[3]*kz_hypo_deox_subdaily[3,j-1]/(dz*V_r[3]),
                                    delta_t[j-1]*A_s[4]*kz_hypo_deox_subdaily[4,j-1]/(dz*V_r[4]),
                                    delta_t[j-1]*A_s[5]*kz_hypo_deox_subdaily[5,j-1]/(dz*V_r[5]),
                                    delta_t[j-1]*A_s[6]*kz_hypo_deox_subdaily[6,j-1]/(dz*V_r[6]),
                                    delta_t[j-1]*A_s[7]*kz_hypo_deox_subdaily[7,j-1]/(dz*V_r[7]),
                                    delta_t[j-1]*A_s[8]*kz_hypo_deox_subdaily[8,j-1]/(dz*V_r[8]),
                                    delta_t[j-1]*A_s[9]*kz_hypo_deox_subdaily[9,j-1]/(dz*V_r[9]),
                                    delta_t[j-1]*A_s[10]*kz_hypo_deox_subdaily[10,j-1]/(dz*V_r[10]),
                                    delta_t[j-1]*A_s[11]*kz_hypo_deox_subdaily[11,j-1]/(dz*V_r[11]),
                                    delta_t[j-1]*A_s[12]*kz_hypo_deox_subdaily[12,j-1]/(dz*V_r[12]),                                    
                                    delta_t[j-1]*A_s[13]*kz_hypo_deox_subdaily[13,j-1]/(dz*V_r[13]) ] , -1)
                        
    
                        
                        
            
        #print("Press Enter to continue...")
        #input()
        #print(Factor_dig )                
                        
        b = C[:, j-1].copy()
        ###########b[0] = b[0] + (0.0989060) * delta_t[j-1] * A_s[0] * kz_hypo_deox_subdaily[0, j-1] / (dz * V_r[0])
        
        b[0] = b[0] + (0.0989060 * delta_t[j-1] * A_s[0] *kz_hypo_surf_deox_subdaily) / (dz * V_r[0])
        
        #print("Press Enter to continue...")
        #input()
        #print(b )   
        
        
        #################original and variable theta
        knows=b - (delta_t[j-1] * Theta_j(temp_hypo_for_jz_correction_subdaily[:, j-1])* (  jz  ))
        
        
        #############attribution test #with fixed theta of average hypolimnion temp 2019-2022 in deox:11.8896
        #############knows=b - (delta_t[j-1] * Theta_j(10.52547)* (  jv +(A_l / V_r) * ja  ))
        
        
        
        
        #############attribution test #with fixed theta of 9.460405011459684 (temp_hypo_ave_onset_deephypoxia)
        #############knows=b - (delta_t[j-1] * Theta_j(temp_ave_hypo_2020_2021)* (  jv +(A_l / V_r) * ja  ))
        

        
        
        #print("Press Enter to continue...")
        #input()
        #print(knows )   
        
        
        solution = np.linalg.solve(Factor_dig, knows)
       
        
        
        C[:, j] = solution
       
        C = np.where(C < 0, 0, C)
        
        

    C = np.where(C < 0, 0, C).T

    C_dox = C[1:, :]
    num_days = (C.shape[0]-1) // num_time_steps_subdaily
    C_dox_3d = np.reshape(C_dox[:num_days * num_time_steps_subdaily], (num_days, num_time_steps_subdaily, -1))
    C_deox_daily_model = np.mean(C_dox_3d, axis=1)

    C_hypo_full_satur = C_satur(temp_hypo_dox, 1)
    C_deox_daily_model = np.where(C_deox_daily_model > C_hypo_full_satur, C_hypo_full_satur, C_deox_daily_model)
    
    #count_satur_condition = np.count_nonzero(C_deox_daily_model == C_hypo_full_satur)
    satur_condition_array = np.where(C_deox_daily_model == C_hypo_full_satur, 1, 0)

    
    C_deox_ave_model = np.dot(C_deox_daily_model, V_r) / sum(V_r)
    
    Do_ave_end = C_deox_ave_model[-1]
    temp_ave_end = np.dot(temp_hypo_dox[-1, :], V_r) / sum(V_r)
    sat_end = Do_ave_end / C_satur(temp_ave_end, 1)
    #sat_end =(estimate_satur_percentage ( Do_ave_end , temp_ave_end , altitude_m=10 ))/100
        
    #print("Press Enter to continue...")
    #input()
    #print(sat_end )    
   

    return C_deox_daily_model, sat_end  ,  satur_condition_array#count_satur_condition , C_deox_ave_model,

#########==========================================================================
def do_model_comprehensive_VHOD_gotm(params, dens_diff_top_meta ,temp_surf, hypo_morphology_vriables_grid ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 ):#=9.299490575422336: ave temp in RCPs of four model#9.460405011459684
                           
    
    DO_2D_hypo_deox_comp = np.full(temp_hypo_2D.shape, np.nan)
    temp_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    kz_2D_hypo_deox_comp =np.full(temp_hypo_2D.shape, np.nan)
    full_sat_hypo_condition= np.full(temp_hypo_2D.shape, np.nan)
    df_deox_periods_info=find_deox_period ( dens_diff_top_meta , temp_surf)  
    
    for index, row in df_deox_periods_info.iterrows():
        
        index_deox_period_in_year=row['index_deox_period_in_year']
        temp_hypo_dox= temp_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
        temp_hypo_inital_cond= temp_hypo_2D[int(row['initial_cond_indices'])]
        duration_repl=row['replanishment_duration']
        deox_duration= row['deox_duration']
        delta_t=np.ones(deox_duration)# for this case study but it could not all 1 for other case study 

        #for jp it shoould put nan for other days:
        #kz_hypo_deox_daily=np.zeros (temp_hypo_dox.shape )#*kz_hypo_2D# # manually allocte for obsrvational years but for the future gotm simulation the kz vslues has indexs of +1 to the start_indices and end_indices 
        
        #for obs:
        #kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
             
        
        #for gotm:
        kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices'])+1 : int(row['end_indices'])+2]
         
        if index_deox_period_in_year==0:
            initial_cond_sat=1
            C_deox_daily_model, sat_end , condition_array=do_one_deox_implicit_VHOD_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                             temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t,kz_hypo_deox_daily )   
            #C_deox_daily_model, sat_end= do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #                 temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t)
            
            
        else:
            
            
            increase_sat_repl = duration_repl * (replanishmnet_rate / 100)
        
            initial_cond_sat = sat_end + increase_sat_repl

            C_deox_daily_model, sat_end ,  condition_array =do_one_deox_implicit_VHOD_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                     temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t,kz_hypo_deox_daily )
            #C_deox_daily_model, sat_end = do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #         temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t)
            
            
            
        
        DO_2D_hypo_deox_comp[int(row['start_indices']) : int(row['end_indices'])+1 ]=C_deox_daily_model   
        temp_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=temp_hypo_dox   
        kz_2D_hypo_deox_comp [int(row['start_indices']) : int(row['end_indices'])+1 ]=kz_hypo_deox_daily   
        full_sat_hypo_condition[int(row['start_indices']) : int(row['end_indices'])+1 ]=condition_array
    
    return DO_2D_hypo_deox_comp , temp_2D_hypo_deox_comp, kz_2D_hypo_deox_comp , full_sat_hypo_condition


#%%mixing_incl

def mixing_incl_do_model_comprehensive_VHOD_gotm(params, dens_diff_top_meta ,temp_surf, hypo_morphology_vriables_grid ,temp_hypo_2D ,kz_hypo_2D , replanishmnet_rate= 2.7946 ):#=9.299490575422336: ave temp in RCPs of four model#9.460405011459684
                           
    temp_2D_mixing_incl_comp =np.copy(temp_hypo_2D)   
    
    DO_2D_mixing_incl_comp = C_satur(temp_2D_mixing_incl_comp, 1)
    
    kz_2D_mixing_incl_comp =np.copy(kz_hypo_2D)
    
    full_sat_hypo_condition= np.full(temp_hypo_2D.shape, np.nan)
    df_deox_periods_info=find_deox_period ( dens_diff_top_meta , temp_surf)  
    
    for index, row in df_deox_periods_info.iterrows():
        
        index_deox_period_in_year=row['index_deox_period_in_year']
        temp_hypo_dox= temp_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
        temp_hypo_inital_cond= temp_hypo_2D[int(row['initial_cond_indices'])]
        duration_repl=row['replanishment_duration']
        deox_duration= row['deox_duration']
        delta_t=np.ones(deox_duration)# for this case study but it could not all 1 for other case study 

        #for jp it shoould put nan for other days:
        #kz_hypo_deox_daily=np.zeros (temp_hypo_dox.shape )#*kz_hypo_2D# # manually allocte for obsrvational years but for the future gotm simulation the kz vslues has indexs of +1 to the start_indices and end_indices 
        
        #for obs:
        #kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices']) : int(row['end_indices'])+1]
             
        
        #for gotm:
        kz_hypo_deox_daily=  kz_hypo_2D[int(row['start_indices'])+1 : int(row['end_indices'])+2]
         
        if index_deox_period_in_year==0:
            initial_cond_sat=1
            C_deox_daily_model, sat_end , condition_array=do_one_deox_implicit_VHOD_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                             temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t,kz_hypo_deox_daily )   
            #C_deox_daily_model, sat_end= do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #                 temp_hypo_inital_cond, initial_cond_sat ,duration_repl,delta_t)
            
            
        else:
            
            
            increase_sat_repl = duration_repl * (replanishmnet_rate / 100)
        
            initial_cond_sat = sat_end + increase_sat_repl
            #####repl
            temp_repl=temp_hypo_2D[int(row['start_indices'])-int(row['replanishment_duration'])+1 : int(row['start_indices'])]
            
            sat_in_repl= np.zeros(temp_repl.shape)
            for i in range (temp_repl.shape[0] ):
                sat_in_repl[i, :]= sat_end+ (i+1)*replanishmnet_rate
                
            C_rep_daily=  C_satur(temp_repl, sat_in_repl/100)
            
            DO_2D_mixing_incl_comp[int(row['start_indices'])-int(row['replanishment_duration'])+1 : int(row['start_indices'])]=C_rep_daily
            
            
            ######
            C_deox_daily_model, sat_end ,  condition_array =do_one_deox_implicit_VHOD_gotm(params,hypo_morphology_vriables_grid, temp_hypo_dox,
                     temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t,kz_hypo_deox_daily )
            #C_deox_daily_model, sat_end = do_one_deox_nokz(params,hypo_morphology_vriables_grid, temp_hypo_dox,
            #         temp_hypo_inital_cond,initial_cond_sat,duration_repl,delta_t)
            

        DO_2D_mixing_incl_comp[int(row['start_indices']) : int(row['end_indices'])+1 ]=C_deox_daily_model 
        
    return DO_2D_mixing_incl_comp , temp_2D_mixing_incl_comp, kz_2D_mixing_incl_comp





#%% testing Ladwig 2021 Jz and with averaged alpha (0.515) #(0.1_0.16)= 0.515*ja+jv 


alpha_hypo_each = A_l_hypo/V_r_hypo# shape must be 7 
"""
#Out[496]: 
array([0.39252949, 0.38793103, 0.38793103, 0.38793103, 0.49196141,
       0.79746835, 0.81857451])
"""

#morphological ratioa
alpha_hypo_bulk = sum(A_l_hypo)/sum(V_r_hypo)#0.485098801425332

#average depth of hypolimnion 
Z_hypo_bulk = sum(V_r_hypo)/sum(A_l_hypo)#2.0614357262103504


#should be arround   for average
#(0.11_0.19)= 0.485*ja+jv # min:0.11 and maximum 0.19


# 0.01+0.485*1=0.495 Not approprite at all
# 0.485*0.1+0.3#0.3485 Not approprite at all

# 0.485*0.08+0.1#0.1388 #good 
# 0.485*0.1+0.1# 0.1485 #good

#2019_1: 0.161 (during the ideal deoxygenation period ) # 0.161 (untill the DO= 2 mg/L)
#2019_2: 0.1842 ,#0.2464
#2020_1: 0.1075 , # 0.1807
#2021_1: 0.1231 , # 0.1479
#2022_1: 0.1164 , # 0.1639

# analyses:

"""						
	Jz_from obs_no_kz_ideal deox	Jz_from_obs_ideal_deox_before DO<2				
2019_1	0.161	0.161				
2019_2	0.1842	0.2464				
2020_1	0.1075	0.1807		2020_1	0.1075	0.1807
2021_1	0.1231	0.1479		2021_1	0.1231	0.1479
2022_1	0.1164	0.1639		2022_1	0.1164	0.1639
Mean:	0.13844	0.17998		Mean:	0.115666667	0.164166667
Medien	0.1231	0.1639		Medien	0.1164	0.1639
STD	0.032715791	0.038923219		STD	0.007825812	0.016401626
Min	0.1075	0.1479			0.1075	0.1479
Max	0.1842	0.2464			0.1231	0.1807
"""


    

#%%temp_2D each year deoxygenation periods for calculation kz_jp

# apply for each year the function the requirement for calculating kz_JP
"""
#2018
#df_str_2018_1_14= df_str_2018_1_14.drop('Datetime', axis=1)

temp_daily_2D_2018_1 = two_D_array_from_df(
    df_str_2018_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2018_1_below135 = two_D_array_from_df(
    df_str_2018_1_14[df_str_2018_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 

temp_daily_2D_2018_1_hypo = two_D_array_from_df(
    df_str_2018_1_14[df_str_2018_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2018_1_meta = two_D_array_from_df(
    df_str_2018_1_14[df_str_2018_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 

#2018_2

#df_str_2018_2_14= df_str_2018_2_14.drop('Datetime', axis=1)

temp_daily_2D_2018_2 = two_D_array_from_df(
    df_str_2018_2_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2018_2_below135 = two_D_array_from_df(
    df_str_2018_2_14[df_str_2018_2_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2018_2_meta = two_D_array_from_df(
    df_str_2018_2_14[df_str_2018_2_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 

"""
###########====================Temp 2 D arrays included the last mixing day before start of deoxygenation period :
#2019_1
#df_str_2019_1_14= df_str_2019_1_14.drop('Datetime', axis=1)
"""
temp_daily_2D_2019_1 = two_D_array_from_df(
    df_str_2019_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2019_1_below135 = two_D_array_from_df(
    df_str_2019_1_14[df_str_2019_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2019_1_hypo = two_D_array_from_df(
    df_str_2019_1_14[df_str_2019_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2019_1_meta = two_D_array_from_df(
    df_str_2019_1_14[df_str_2019_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 



#2019_2
#df_str_2019_2_14= df_str_2019_2_14.drop('Datetime', axis=1)

temp_daily_2D_2019_2 = two_D_array_from_df(
    df_str_2019_2_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2019_2_below135 = two_D_array_from_df(
    df_str_2019_2_14[df_str_2019_2_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 

temp_daily_2D_2019_2_hypo = two_D_array_from_df(
    df_str_2019_2_14[df_str_2019_2_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 



temp_daily_2D_2019_2_meta = two_D_array_from_df(
    df_str_2019_2_14[df_str_2019_2_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 



#2020
#df_str_2020_1_14= df_str_2020_1_14.drop('Datetime', axis=1)

temp_daily_2D_2020_1 = two_D_array_from_df(
    df_str_2020_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2020_1_below135 = two_D_array_from_df(
    df_str_2020_1_14[df_str_2020_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 

temp_daily_2D_2020_1_hypo = two_D_array_from_df(
    df_str_2020_1_14[df_str_2020_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2020_1_meta = two_D_array_from_df(
    df_str_2020_1_14[df_str_2020_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 



#2021
#df_str_2021_1_14= df_str_2021_1_14.drop('Datetime', axis=1)

temp_daily_2D_2021_1 = two_D_array_from_df(
    df_str_2021_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2021_1_below135 = two_D_array_from_df(
    df_str_2021_1_14[df_str_2021_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 

temp_daily_2D_2021_1_hypo = two_D_array_from_df(
    df_str_2021_1_14[df_str_2021_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2021_1_meta = two_D_array_from_df(
    df_str_2021_1_14[df_str_2021_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 


#2022
#df_str_2022_1_14= df_str_2022_1_14.drop('Datetime', axis=1)

temp_daily_2D_2022_1 = two_D_array_from_df(
    df_str_2022_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2022_1_below135 = two_D_array_from_df(
    df_str_2022_1_14[df_str_2022_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2022_1_hypo = two_D_array_from_df(
    df_str_2022_1_14[df_str_2022_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2022_1_meta = two_D_array_from_df(
    df_str_2022_1_14[df_str_2022_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 


"""




#%%2 D array careting the deoxygenatiobn periods excluding day before deoxygenations

temp_daily_2D_2019_1 = two_D_array_from_df(
    df_str_nomixing_2019_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2019_1_below135 = two_D_array_from_df(
    df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2019_1_hypo = two_D_array_from_df(
    df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 

do_daily_2D_2019_2_hypo = two_D_array_from_df(
    df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m'] < -13.5], values_name='DO',index_name='Datetime') 

temp_daily_2D_2019_1_meta = two_D_array_from_df(
    df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 



#2019_2
#df_str_2019_2_14= df_str_2019_2_14.drop('Datetime', axis=1)

temp_daily_2D_2019_2 = two_D_array_from_df(
    df_str_nomixing_2019_2_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2019_2_below135 = two_D_array_from_df(
    df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2019_2_hypo = two_D_array_from_df(
    df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 

do_daily_2D_2019_1_hypo = two_D_array_from_df(
    df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m'] < -13.5], values_name='DO',index_name='Datetime') 

temp_daily_2D_2019_2_meta = two_D_array_from_df(
    df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 



#2020
#df_str_2020_1_14= df_str_2020_1_14.drop('Datetime', axis=1)

temp_daily_2D_2020_1 = two_D_array_from_df(
    df_str_nomixing_2020_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2020_1_below135 = two_D_array_from_df(
    df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2020_1_hypo = two_D_array_from_df(
    df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 

do_daily_2D_2020_1_hypo = two_D_array_from_df(
    df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m'] < -13.5], values_name='DO',index_name='Datetime') 

temp_daily_2D_2020_1_meta = two_D_array_from_df(
    df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 



#2021
#df_str_2021_1_14= df_str_2021_1_14.drop('Datetime', axis=1)

temp_daily_2D_2021_1 = two_D_array_from_df(
    df_str_nomixing_2021_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2021_1_below135 = two_D_array_from_df(
    df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2021_1_hypo = two_D_array_from_df(
    df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 

do_daily_2D_2021_1_hypo = two_D_array_from_df(
    df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m'] < -13.5], values_name='DO',index_name='Datetime') 


temp_daily_2D_2021_1_meta = two_D_array_from_df(
    df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 


#2022
#df_str_2022_1_14= df_str_2022_1_14.drop('Datetime', axis=1)

temp_daily_2D_2022_1 = two_D_array_from_df(
    df_str_nomixing_2022_1_14, values_name='Temp',index_name='Datetime')    

temp_daily_2D_2022_1_below135 = two_D_array_from_df(
    df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m'] < -13], values_name='Temp',index_name='Datetime') 


temp_daily_2D_2022_1_hypo = two_D_array_from_df(
    df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m'] < -13.5], values_name='Temp',index_name='Datetime') 

do_daily_2D_2022_1_hypo = two_D_array_from_df(
    df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m'] < -13.5], values_name='DO',index_name='Datetime') 


temp_daily_2D_2022_1_meta = two_D_array_from_df(
    df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m'] > -14], values_name='Temp',index_name='Datetime') 



#%% average of hypolimnion temp during the deoxygenation period:
    
np.mean(np.dot(temp_daily_2D_2019_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#10.954995464434026# 2019_1

temp_ave_onset_2019_1=np.mean(np.dot(temp_daily_2D_2019_1_hypo[0,:] , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#8.231300210560416
np.mean(np.dot(temp_daily_2D_2019_2_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#16.42006810009718# 2019_2


temp_ave_onset_2019_2=np.mean(np.dot(temp_daily_2D_2019_2_hypo[0,:] , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#16.47818553611921

np.mean(np.dot(temp_daily_2D_2020_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#11.261937807035133# 2020_1


temp_ave_onset_2020_1=np.mean(np.dot(temp_daily_2D_2020_1_hypo[0,:] , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#8.986218685887053

np.mean(np.dot(temp_daily_2D_2021_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#9.789005772604# 2021_1


temp_ave_onset_2021_1=np.mean(np.dot(temp_daily_2D_2021_1_hypo[0,:] , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#6.608167584494114

np.mean(np.dot(temp_daily_2D_2022_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#12.959545734296741# 2022_1


temp_ave_onset_2022_1=np.mean(np.dot(temp_daily_2D_2022_1_hypo[0,:] , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#10.579613432674657





temp_rep_2020_2021_onset=(temp_ave_onset_2021_1+temp_ave_onset_2020_1)/2# 7.797193135190584



temp_2D_deox_2years_calib=np.concatenate([temp_daily_2D_2020_1_hypo,
                               temp_daily_2D_2022_1_hypo], axis=0)


np.mean(np.dot(temp_2D_deox_2years_calib, np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#12.094260140304176



temp_2D_deox_2years_valid=np.concatenate([temp_daily_2D_2019_1_hypo,
                               temp_daily_2D_2019_2_hypo], axis=0)


np.mean(np.dot(temp_2D_deox_2years_valid, np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#13.77204321477586




temp_2D_deox_4years=np.concatenate([temp_daily_2D_2019_1_hypo,
                               temp_daily_2D_2019_2_hypo,
                               temp_daily_2D_2020_1_hypo,
                               temp_daily_2D_2021_1_hypo,
                               temp_daily_2D_2022_1_hypo], axis=0)





np.mean(np.dot(temp_2D_deox_4years, np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#11.889583898547674 # 2019-2022


#%% DO in hypo deoxygenation period 


np.mean(np.dot(do_daily_2D_2019_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#7.764672724013486# 2019_1
np.mean(np.dot(do_daily_2D_2019_2_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#2.7030647067288283# 2019_2
np.mean(np.dot(do_daily_2D_2020_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#3.0008606110520955# 2020_1
np.mean(np.dot(do_daily_2D_2021_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#4.5536647814022935# 2021_1
np.mean(np.dot(do_daily_2D_2022_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#3.4881162842922# 2022_1



do_2D_deox_4years=np.concatenate([do_daily_2D_2019_1_hypo,
                               do_daily_2D_2019_2_hypo,
                               do_daily_2D_2020_1_hypo,
                               do_daily_2D_2021_1_hypo,
                               do_daily_2D_2022_1_hypo], axis=0)




np.mean(np.dot(do_2D_deox_4years, np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
# 4.035914863046592

#%%Anoxia - thereshold 0.5
    
    
####first day when it is anoxia:    
index_anoxia_2020_1=np.where(do_daily_2D_2020_1_hypo[: , 6]<=0.5)
dateindex_anoxia_2020_1=index_anoxia_2020_1[0][0]#64

date_deepest_layer_anoxic_2020=df_str_nomixing_2020_1_14.index.unique()[first_index_anoxia_2020_1]
#Timestamp('2020-07-25 00:00:00')




index_anoxia_2021_1=np.where(do_daily_2D_2021_1_hypo[: , 6]<=0.5)
dateindex_anoxia_2021_1=index_anoxia_2021_1[0][0]#75

date_deepest_layer_anoxic_2021=df_str_nomixing_2021_1_14.index.unique()[first_index_anoxia_2021_1]
#Timestamp('2021-07-27 00:00:00')


index_anoxia_2022_1=np.where(do_daily_2D_2022_1_hypo[: , 6]<=0.5)
dateindex_anoxia_2022_1=index_anoxia_2022_1[0][0]#61

date_deepest_layer_anoxic_2022=df_str_nomixing_2022_1_14.index.unique()[first_index_anoxia_2022_1]
#Timestamp('2022-07-23 00:00:00')







#### all layers anoxia conditions 

index_anoxia_inalllayer_2020_1=np.where(np.all(do_daily_2D_2020_1_hypo <= 0.5, axis=1))[0]
dateindex_anoxia_inalllayer_2020_1=index_anoxia_inalllayer_2020_1[0]#67
date_all_layer_anoxic_2020= df_str_nomixing_2020_1_14.index.unique()[index_anoxia_inalllayer_2020_1[0]]
#Timestamp('2020-07-28 00:00:00')

index_anoxia_inalllayer_2021_1=np.where(np.all(do_daily_2D_2021_1_hypo <= 0.5, axis=1))[0]
dateindex_anoxia_inalllayer_2021_1=index_anoxia_inalllayer_2021_1[0]#81
index_all_layer_anoxic_2021= df_str_nomixing_2021_1_14.index.unique()[index_anoxia_inalllayer_2021_1[0]]
#Timestamp('2021-08-02 00:00:00')

index_anoxia_inalllayer_2022_1=np.where(np.all(do_daily_2D_2022_1_hypo <= 0.5, axis=1))[0]
dateindex_anoxia_inalllayer_2022_1=index_anoxia_inalllayer_2022_1[0]#68
index_all_layer_anoxic_2022= df_str_nomixing_2022_1_14.index.unique()[index_anoxia_inalllayer_2022_1[0]]
#Timestamp('2022-07-30 00:00:00')







####the first anoxia on average in whole hypolimnion 


do_ave_2020_1= pd.DataFrame(np.dot(do_daily_2D_2020_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
do_ave_2020_1= do_ave_2020_1.set_index(df_str_nomixing_2020_1_14.index.unique())

do_ave_2021_1=pd.DataFrame(np.dot(do_daily_2D_2021_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
do_ave_2021_1=do_ave_2021_1.set_index(df_str_nomixing_2021_1_14.index.unique())

do_ave_2022_1=pd.DataFrame(np.dot(do_daily_2D_2022_1_hypo , np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
do_ave_2022_1=do_ave_2022_1.set_index(df_str_nomixing_2022_1_14.index.unique())



index_of_first_anoxia_2020 = do_ave_2020_1[do_ave_2020_1 <= 0.5].idxmax()
#2022-07-27
index_of_first_anoxia_2021 = do_ave_2021_1[do_ave_2021_1 <= 0.5].idxmax()
#2021-08-01
index_of_first_anoxia_2022 = do_ave_2022_1[do_ave_2022_1 <= 0.5].idxmax()
#2022-07-27




#%% average hypolimnetic temp from onset untill anoxia 

# deepest layer anoxia for first time 
temp_ave_before_indeepestlayer_anoxia_2020=np.mean(np.dot( temp_daily_2D_2020_1_hypo[0:dateindex_anoxia_2020_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#10.32642052278787

temp_ave_before_indeepestlayer_anoxia_2021=np.mean(np.dot( temp_daily_2D_2021_1_hypo[0:dateindex_anoxia_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#9.285608588595213

#(2020 , 2021)->
temp_ave_before_indeepestlayer_anoxia_2020_2021=0.5*(temp_ave_before_indeepestlayer_anoxia_2020+temp_ave_before_indeepestlayer_anoxia_2021)
#9.806014555691542



temp_ave_before_indeepestlayer_anoxia_2022=np.mean(np.dot( temp_daily_2D_2022_1_hypo[0:dateindex_anoxia_2022_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#12.24953622032003






# all hypolimnion is anoxia

temp_ave_before_inalllayer_anoxia_2020=np.mean(np.dot( temp_daily_2D_2020_1_hypo[0:dateindex_anoxia_inalllayer_2020_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#10.394418156151351

temp_ave_before_inalllayer_anoxia_2021=np.mean(np.dot( temp_daily_2D_2021_1_hypo[0:dateindex_anoxia_inalllayer_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#9.381013337221262

#(2020 , 2021)->
temp_ave_before_inalllayer_anoxia_2020_2021=0.5*(temp_ave_before_inalllayer_anoxia_2020+temp_ave_before_inalllayer_anoxia_2021)
#9.887715746686307



temp_ave_before_inalllayer_anoxia_2022=np.mean(np.dot( temp_daily_2D_2022_1_hypo[0:dateindex_anoxia_inalllayer_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#12.594154826860523



#%%hypoxia 

####first day when it is hypoxia:    
index_hypoxia_2020_1=np.where(do_daily_2D_2020_1_hypo[: , 6]<=2)
dateindex_hypoxia_2020_1=index_hypoxia_2020_1[0][0]#41

date_deepest_layer_hypoxic_2020=df_str_nomixing_2020_1_14.index.unique()[dateindex_hypoxia_2020_1]
#Timestamp('2020-07-02 00:00:00')




index_hypoxia_2021_1=np.where(do_daily_2D_2021_1_hypo[: , 6]<=2)
dateindex_hypoxia_2021_1=index_hypoxia_2021_1[0][0]#63

date_deepest_layer_hypoxic_2021=df_str_nomixing_2021_1_14.index.unique()[dateindex_hypoxia_2021_1]
#Timestamp('2021-07-15 00:00:00')


index_hypoxia_2022_1=np.where(do_daily_2D_2022_1_hypo[: , 6]<=2)
dateindex_hypoxia_2022_1=index_hypoxia_2022_1[0][0]#50

date_deepest_layer_anoxic_2022=df_str_nomixing_2022_1_14.index.unique()[dateindex_hypoxia_2022_1]
#Timestamp('2022-07-12 00:00:00')







#### all layers hypoxia conditions 

index_hypoxia_inalllayer_2020_1=np.where(np.all(do_daily_2D_2020_1_hypo <= 2, axis=1))[0]
dateindex_hypoxia_inalllayer_2020_1=index_hypoxia_inalllayer_2020_1[0]#51
date_all_layer_hypoxic_2020= df_str_nomixing_2020_1_14.index.unique()[dateindex_hypoxia_inalllayer_2020_1]
#Timestamp('2020-07-12 00:00:00')

index_hypoxia_inalllayer_2021_1=np.where(np.all(do_daily_2D_2021_1_hypo <= 2, axis=1))[0]
dateindex_hypoxia_inalllayer_2021_1=index_hypoxia_inalllayer_2021_1[0]#68
index_all_layer_hypoxic_2021= df_str_nomixing_2021_1_14.index.unique()[dateindex_hypoxia_inalllayer_2021_1]
#Timestamp('2021-07-20 00:00:00')

index_hypoxia_inalllayer_2022_1=np.where(np.all(do_daily_2D_2022_1_hypo <= 2, axis=1))[0]
dateindex_hypoxia_inalllayer_2022_1=index_hypoxia_inalllayer_2022_1[0]#68
index_all_layer_hypoxic_2022= df_str_nomixing_2022_1_14.index.unique()[dateindex_hypoxia_inalllayer_2022_1]
#Timestamp('2022-07-16 00:00:00')





#%% average hypolimnetic temp from onset untill hypoxia 

# deepest layer hypoxia for first time 
temp_ave_before_indeepestlayer_hypoxia_2020=np.mean(np.dot( temp_daily_2D_2020_1_hypo[0:dateindex_hypoxia_2020_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#9.85690736820049

temp_prof_hypo_tohypoxia_2020=temp_daily_2D_2020_1_hypo[0:dateindex_hypoxia_2020_1+1 , :]

k_temp_prof_hypo_tohypoxia_2020=Theta_j(temp_prof_hypo_tohypoxia_2020)

datetime_deox_2020=df_str_nomixing_2020_1_14.index.unique()

ktemp_ave_before_indeepestlayer_hypoxia_2020=np.mean(np.dot(k_temp_prof_hypo_tohypoxia_2020, np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#0.4293490274443813

#age volume weighted nakonim
#9.83
"""
(np.dot( temp_daily_2D_2020_1_hypo[0:dateindex_hypoxia_2020_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum()).min()
#8.986218685887053
(np.dot( temp_daily_2D_2020_1_hypo[0:dateindex_hypoxia_2020_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum()).max()
#10.469350772054852
"""


temp_ave_before_indeepestlayer_hypoxia_2021=np.mean(np.dot( temp_daily_2D_2021_1_hypo[0:dateindex_hypoxia_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#9.06390265471888

temp_prof_hypo_tohypoxia_2021=temp_daily_2D_2021_1_hypo[0:dateindex_hypoxia_2021_1+1 , :]


k_temp_prof_hypo_tohypoxia_2021=Theta_j(temp_prof_hypo_tohypoxia_2021)

datetime_deox_2021=df_str_nomixing_2021_1_14.index.unique()

ktemp_ave_before_indeepestlayer_hypoxia_2021=np.mean(np.dot(k_temp_prof_hypo_tohypoxia_2021, np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#0.4034595860079587



#if duration also consider for getting ave of these two years :
    
(0.4293490274443813*41   +  0.4034595860079587*63)/(41+63)# 0.41366600042039453



#9.038
"""
(np.dot( temp_daily_2D_2021_1_hypo[0:dateindex_hypoxia_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum()).min()
#6.608167584494114
(np.dot( temp_daily_2D_2021_1_hypo[0:dateindex_hypoxia_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum()).max()
#10.462367184969226
"""






#(2020 , 2021)->
temp_ave_before_indeepestlayer_hypoxia_2020_2021=0.5*(temp_ave_before_indeepestlayer_hypoxia_2020+temp_ave_before_indeepestlayer_hypoxia_2021)
#9.460405011459684




Theta_j(temp_ave_before_indeepestlayer_hypoxia_2020)#0.4290623215836453

Theta_j(temp_ave_before_indeepestlayer_hypoxia_2021)#0.4015967403448328
Theta_j(9.460405011459684)# 0.41510243284372395


datetime_deox_2020_2021=np.concatenate([datetime_deox_2020[0:dateindex_hypoxia_2020_1+1] , datetime_deox_2021[0:dateindex_hypoxia_2021_1+1]])

k_temp_prof_hypo_tohypoxia_2020_2021=np.concatenate([k_temp_prof_hypo_tohypoxia_2020 , k_temp_prof_hypo_tohypoxia_2021])

k_temp_prof_hypo_tohypoxia_2020_2021= pd.DataFrame(k_temp_prof_hypo_tohypoxia_2020_2021 , index= datetime_deox_2020_2021 )


consecutive_dates = pd.date_range(start=k_temp_prof_hypo_tohypoxia_2020_2021.index.min(), end=k_temp_prof_hypo_tohypoxia_2020_2021.index.max(), freq='D')

df = k_temp_prof_hypo_tohypoxia_2020_2021.reindex(consecutive_dates)

temp_ave_before_indeepestlayer_hypoxia_2022=np.mean(np.dot( temp_daily_2D_2022_1_hypo[0:dateindex_hypoxia_2022_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#12.030407458387636






# all hypolimnion is hypoxia

temp_ave_before_inalllayer_hypoxia_2020=np.mean(np.dot( temp_daily_2D_2020_1_hypo[0:dateindex_hypoxia_inalllayer_2020_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#10.06271011136445

temp_ave_before_inalllayer_hypoxia_2021=np.mean(np.dot( temp_daily_2D_2021_1_hypo[0:dateindex_hypoxia_inalllayer_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#9.161976521946483

#(2020 , 2021)->
temp_ave_before_inalllayer_hypoxia_2020_2021=0.5*(temp_ave_before_inalllayer_hypoxia_2020+temp_ave_before_inalllayer_hypoxia_2021)
#9.612343316655465



temp_ave_before_inalllayer_hypoxia_2022=np.mean(np.dot( temp_daily_2D_2022_1_hypo[0:dateindex_hypoxia_inalllayer_2021_1+1 , :], np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']) )/  np.array(df_morphro[df_morphro ['Z_m']<-13.5]['V_r_m']).sum())
#12.365208365305957

#%%Observational AF 2019-2022


date_2019_1=df_str_nomixing_2019_1_14.index.unique()
do_daily_2D_2019_1_hypo

AF_2019_1=annual_anoxic_factor(do_daily_2D_2019_1_hypo, date_2019_1 , A_l, A0=23.67*10**6 , threshold=0.5)

#2019_1: 0

date_2019_2=df_str_nomixing_2019_2_14.index.unique()
do_daily_2D_2019_2_hypo

AF_2019_2=annual_anoxic_factor(do_daily_2D_2019_2_hypo, date_2019_2 , A_l, A0=23.67*10**6 , threshold=0.5)

#2019_2: 2.300275

date_2020_1=df_str_nomixing_2020_1_14.index.unique()
do_daily_2D_2020_1_hypo

AF_2020_1=annual_anoxic_factor(do_daily_2D_2020_1_hypo, date_2020_1 , A_l, A0=23.67*10**6 , threshold=0.5)

#2020:    6.079584


df_str_nomixing_2021_1_14

date_2021_1=df_str_nomixing_2021_1_14.index.unique()
do_daily_2D_2021_1_hypo

AF_2021_1=annual_anoxic_factor(do_daily_2D_2021_1_hypo, date_2021_1 , A_l, A0=23.67*10**6 , threshold=0.5)

#2021:    4.423215

df_str_nomixing_2022_1_14

date_2022_1=df_str_nomixing_2022_1_14.index.unique()
do_daily_2D_2022_1_hypo

AF_2022_1=annual_anoxic_factor(do_daily_2D_2022_1_hypo, date_2022_1 , A_l, A0=23.67*10**6 , threshold=0.5)

#2022:    5.747729

#%%  Plot of temp modifier
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 1.087**(x - 20)


# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 8))

x_values = np.linspace(5, 12)#(10.3595, 10.916, 100)

# Calculate corresponding y values using the function
y_values = f(x_values)

# Plot the function using scatter plot
ax.scatter(x_values, y_values, label='f(x) = 1.087^(x-20)')
ax.set_xlabel('Temperature [°C]')
ax.set_ylabel('Ktemp []')
ax.set_title('Jz temperature modifier')


# Save the figure with specified DPI
fig.savefig('jz_temp_modifier.png', dpi=300)
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Assuming k_temp_prof_hypo_tohypoxia_2020_2021 is your DataFrame
# Replace this with the actual DataFrame name


plt.figure(figsize=(10, 8))
# Set the y-axis value
y_value = 0.41366600042039453#:weighted by duration#0.41510243284372395

# Create a colormap ranging from red to blue
cmap = plt.get_cmap('RdBu_r')

# Normalize the data to the colormap range for each column
norm = mcolors.Normalize(vmin=df.min().min(), vmax=df.max().max())

# Plot each column separately
for col in df.columns:
    # Map the data values to the colormap range for the current column
    color_values = norm(df[col].values)
    # Convert the normalized values to RGBA color values
    colors = cmap(color_values)

    # Plot the line for the current column with the corresponding color
    for i in range(1, len(df)):
        plt.plot([df.index[i - 1], df.index[i]], [df[col].iloc[i - 1], df[col].iloc[i]], color=colors[i], label=f'Column {col}' if i == 1 else "")

# Plot the horizontal line for the y-axis value
plt.axhline(y=y_value, color='black', linestyle='--', label='ave temp 2020 and 2021 ')
plt.axhline(y=0.4293490274443813, color='black', linestyle='--', label='ave temp in 2020')

plt.axhline(y=0.4034595860079587, color='black', linestyle='--', label='ave temp in 2021')


# Set labels and legend
plt.ylabel('Ktemp []')

plt.xticks(rotation=45)

# Display the plot
plt.show()



#%% new definded Treference according average temp hypo durin 4 years 2019-2022;

"""
temphypoave=11.8896

Ja_inTref_temphypoave= Ja /(1.087)**(20-temphypoave)

Jv_inTref_temphypoave= Jv /(1.087)**(20-temphypoave)


1.087**(20-11.89)
# 1.9671463786758334


#calibated Ja and Jv should be devided by 
# 1.9671463786758334 this value to get the
 ja and jv in tempearture averaged in hypolimnion 
 then this new ja and jv should be applied for future tempaerture scnearios 
 
 
 #Question from Ian did I undrestand it well ????
 
 # calibation on  T reference= T  hypo average and 
 #then apply these new behavioural set of  Ja and Jv 
 #to future simulation of temp with 
 #new Temperature correction component which previously 
 #Tref=20 need to be changed into 11.889583898547674 
 


"""


#%% kz_bv: a function that only need 2-D array of temperature 
# just in case I need to analyse the N2 values 
# WOW incatreable all values are right 
# Brawo Mahtab!!!
#Hondzo, M., & Stefan, H. G. (1993). Lake water temperature simulation model. Journal of Hydraulic Engineering, 119(11), 1251-1273.

def kz_bv_easier(temp_2D_year ,  A0=23.67, g=9.81838509231682, dz=0.5, kz_min=1.4*10**-7 ):
    
    density_2D_year=Lab_Density(temp_2D_year)
    density_gradient_2D_year=np.diff(density_2D_year, axis=1)/density_2D_year[:, :-1]
    N2_2D_year=density_gradient_2D_year*g /dz# s-2
    kz_bv_2D_year = (8.17*10**-4*(A0)**0.56*(N2_2D_year)**-0.43)*10**-4 # cm2/s->m2/s
    
    
    ratio_of_kz_bv_nan=(kz_bv_2D_year[np.isnan(kz_bv_2D_year)].size)/(kz_bv_2D_year.size)
    
    kz_bv_2D_year[np.isnan(kz_bv_2D_year)] = kz_min # the nan values of th*is calculation was because of the density of the layer down wasnt bigger than layer above N2<0
    
    print( (kz_bv_2D_year[kz_bv_2D_year < kz_min].size)/(kz_bv_2D_year.size))# number of day and layer  with lower than minimum 
    
    kz_bv_2D_year[kz_bv_2D_year < kz_min] = kz_min 
    
    ratio_of_kz_bv_P_infinit= (kz_bv_2D_year[kz_bv_2D_year == np.inf].size)/(kz_bv_2D_year.size)
    
    kz_bv_2D_year[kz_bv_2D_year == np.inf] = kz_min # where 
    
    ratio_of_kz_bv_n_infinit=(kz_bv_2D_year[kz_bv_2D_year == -np.inf].size)/(kz_bv_2D_year.size)
    
    kz_bv_2D_year[kz_bv_2D_year == -np.inf] = kz_min     
    
    
    return (kz_bv_2D_year ,N2_2D_year)

#%% using this function for hypolimnion in different sttratification period 
# EXCLUDING mixing day 
# an extra layer is needed to calculate the kz bv for the hypolimnion layer 

#kz_bv_hypo_daily_2D_2018_1=kz_bv_easier(temp_daily_2D_2018_1_below135[1:, :])[0]
#kz_bv_hypo_daily_2D_2018_2=kz_bv_easier(temp_daily_2D_2018_2_below135[1:, :])[0]
kz_bv_hypo_daily_2D_2019_1=kz_bv_easier(temp_daily_2D_2019_1_below135)[0]
kz_bv_hypo_daily_2D_2019_2=kz_bv_easier(temp_daily_2D_2019_2_below135)[0]
kz_bv_hypo_daily_2D_2020_1=kz_bv_easier(temp_daily_2D_2020_1_below135)[0]
kz_bv_hypo_daily_2D_2021_1=kz_bv_easier(temp_daily_2D_2021_1_below135)[0]# mean: 2.8974071543614343e-05
kz_bv_hypo_daily_2D_2022_1=kz_bv_easier(temp_daily_2D_2022_1_below135)[0]# mean: 2.1454803504487075e-05



kz_bv_hypo_surf_daily_2019_1=kz_bv_hypo_daily_2D_2019_1[: , 0]
kz_bv_hypo_surf_daily_2019_2=kz_bv_hypo_daily_2D_2019_2[: , 0]
kz_bv_hypo_surf_daily_2020_1=kz_bv_hypo_daily_2D_2020_1[: , 0]
kz_bv_hypo_surf_daily_2021_1=kz_bv_hypo_daily_2D_2021_1[: , 0]
kz_bv_hypo_surf_daily_2022_1=kz_bv_hypo_daily_2D_2022_1[: , 0]

#%% analyse on the top to metalimnion  N2 values 


#N2_daily_2D_2018_1_meta=kz_bv_easier(temp_daily_2D_2018_1_meta[1:, :])[1]
#N2_daily_2D_2018_2_meta=kz_bv_easier(temp_daily_2D_2018_2_meta[1:, :])[1]
N2_daily_2D_2019_1_meta=kz_bv_easier(temp_daily_2D_2019_1_meta)[1]
N2_daily_2D_2019_2_meta=kz_bv_easier(temp_daily_2D_2019_2_meta)[1]
N2_daily_2D_2020_1_meta=kz_bv_easier(temp_daily_2D_2020_1_meta)[1]
N2_daily_2D_2021_1_meta=kz_bv_easier(temp_daily_2D_2021_1_meta)[1]
N2_daily_2D_2022_1_meta=kz_bv_easier(temp_daily_2D_2022_1_meta)[1]



def array_statistics(arr):
    stats = {
        'Minimum': np.min(arr),
        'Maximum': np.max(arr),
        'Mean': np.mean(arr),
        'Median': np.median(arr),
        'Standard Deviation': np.std(arr)
    }
    return stats



"""
array_statistics(N2_2D_2018_1_meta)
{'Minimum': -3.536972015201872e-05,
 'Maximum': 0.005158641271683832,
 'Mean': 0.00041692505472000496,
 'Standard Deviation': 0.0005843323925269766}
"""
array_statistics(N2_daily_2D_2019_1_meta)
{'Minimum': -3.536972015201872e-05,
 'Maximum': 0.005158641271683832,
 'Mean': 0.00041692505472000496,
 'Median': 0.000201151141887554,
 'Standard Deviation': 0.0005843323925269766}

array_statistics(N2_daily_2D_2019_2_meta)
{'Minimum': -9.467596706676743e-06,
 'Maximum': 0.0035892166339032074,
 'Mean': 0.0003827385405706419,
 'Median': 0.0001840168174775595,
 'Standard Deviation': 0.0005080164617527432}


array_statistics(N2_daily_2D_2020_1_meta)
{'Minimum': -5.6219196823994594e-05,
 'Maximum': 0.010366121823545415,
 'Mean': 0.0008591116284223339,
 'Median': 0.0004332825612084543,
 'Standard Deviation': 0.0011398837581481048}

array_statistics(N2_daily_2D_2021_1_meta)
{'Minimum': -1.544297134601543e-05,
 'Maximum': 0.016878467449612133,
 'Mean': 0.0010144736066292927,
 'Median': 0.0003251999551083453,
 'Standard Deviation': 0.0016916320764922823}


array_statistics(N2_daily_2D_2022_1_meta)
{'Minimum': -3.728256564207863e-05,
 'Maximum': 0.010643148616090274,
 'Mean': 0.0007535358377429021,
 'Median': 0.00031086040426409826,
 'Standard Deviation': 0.0010857223535679003}



N2_daily_meta_2D_2019_2022= np.concatenate((  N2_daily_2D_2019_1_meta, N2_daily_2D_2019_2_meta, N2_daily_2D_2020_1_meta , N2_daily_2D_2021_1_meta, N2_daily_2D_2022_1_meta), axis=0)
array_statistics(N2_daily_meta_2D_2019_2022)

{'Minimum': -5.6219196823994594e-05,
 'Maximum': 0.016878467449612133,
 'Mean': 0.0007648656612343532,
 'Median': 0.0002960368665661083,
 'Standard Deviation': 0.0012209917815601942}

#%% Maximum Brunt Väisälä equation or buoyancy frequency analysies 

max_buoy_freq_2019_1=np.max(N2_daily_2D_2019_1_meta , axis=1)

max_buoy_freq_2019_2=np.max(N2_daily_2D_2019_2_meta , axis=1)

max_buoy_freq_2020_1=np.max(N2_daily_2D_2020_1_meta , axis=1)

max_buoy_freq_2021_1=np.max(N2_daily_2D_2021_1_meta , axis=1)

max_buoy_freq_2022_1=np.max(N2_daily_2D_2022_1_meta , axis=1)


max_buoy_freq_2019_2022=np.concatenate(( max_buoy_freq_2019_1 , max_buoy_freq_2019_2 , max_buoy_freq_2020_1 , max_buoy_freq_2021_1 , max_buoy_freq_2022_1 ) , axis= 0)
array_statistics(max_buoy_freq_2019_2022)
{'Minimum': 9.094819096100535e-05,
 'Maximum': 0.016878467449612133,
 'Mean': 0.0034608153348793967,
 'Median': 0.002832310972096898,
 'Standard Deviation': 0.0027074619774298545}


#%% analyse of the hypolimnetic_Kz_bv values in each year separetly and one all togther  


"""
array_statistics(kz_bv_daily_2D_2018_1_below135)
{'Minimum': 3.989347927757573e-06,
 'Maximum': 7.016404771049086e-05,
 'Mean': 2.0807372091904288e-05,
 'Standard Deviation': 1.0717478010139569e-05}
"""


array_statistics(kz_bv_hypo_daily_2D_2019_1)
{'Minimum': 6.148294383271784e-06,
 'Maximum': 7.701204974517714e-05,
 'Mean': 2.4827682113209484e-05,
 'Median': 1.9832877945957757e-05,
 'Standard Deviation': 1.4335052968754895e-05}

array_statistics(kz_bv_hypo_daily_2D_2019_2)
{'Minimum': 6.881412467674149e-06,
 'Maximum': 4.621426460807479e-05,
 'Mean': 2.070606037229716e-05,
 'Median': 2.0479111230946788e-05,
 'Standard Deviation': 5.468705377959256e-06}



array_statistics(kz_bv_hypo_daily_2D_2020_1)
{'Minimum': 9.277543080660369e-06,
 'Maximum': 5.03115111173913e-05,
 'Mean': 2.5283029057280364e-05,
 'Median': 2.4280563077429418e-05,
 'Standard Deviation': 7.549309055544134e-06}


array_statistics(kz_bv_hypo_daily_2D_2021_1)
{'Minimum': 1.4361205597148112e-05,
 'Maximum': 8.197670147965065e-05,
 'Mean': 2.937110142602698e-05,
 'Median': 2.716310158964828e-05,
 'Standard Deviation': 8.74081117334427e-06}


array_statistics(kz_bv_hypo_daily_2D_2022_1)
{'Minimum': 7.01397825583537e-06,
 'Maximum': 5.387336595925476e-05,
 'Mean': 2.178502752007882e-05,
 'Median': 2.0880350643989115e-05,
 'Standard Deviation': 6.4422800936235465e-06}

####All togther analyses 

kz_bv_hypo_daily_2D_2019_2022= np.concatenate((  kz_bv_hypo_daily_2D_2019_1, kz_bv_hypo_daily_2D_2019_2, kz_bv_hypo_daily_2D_2020_1 , kz_bv_hypo_daily_2D_2021_1, kz_bv_hypo_daily_2D_2022_1), axis=0)
array_statistics(kz_bv_hypo_daily_2D_2019_2022)
{'Minimum': 6.148294383271784e-06,
 'Maximum': 8.197670147965065e-05,
 'Mean': 2.487784819771461e-05,
 'Median': 2.3434438298948343e-05,
 'Standard Deviation': 9.041695403029782e-06}

"""in compare to the 2018_2022 of simulation of GOTM it is one order of magnitute is larger :
array_statistics(kz_hypo_all)
Out[347]: 
{'Minimum': 9.405572427567677e-07,
 'Maximum': 0.00017870900046546012,
 'Mean': 7.195552494186133e-06,
 'Standard Deviation': 1.2481417929041973e-05} 
    
kz_bv_daily_2D_2018_2022=np.concatenate(( kz_bv_daily_2D_2018_1_below135 , kz_bv_daily_2D_2019_1_below135, kz_bv_daily_2D_2019_2_below135, kz_bv_daily_2D_2020_1_below135 , kz_bv_daily_2D_2021_1_below135, kz_bv_daily_2D_2022_1_below135), axis=0)
array_statistics(kz_bv_2D_2018_2022)
{'Minimum': 3.989347927757573e-06,
 'Maximum': 8.197670147965065e-05,
 'Mean': 2.384018674609893e-05,
 'Standard Deviation': 9.518395686109313e-06}"""   





#%% Updated version of calculation of Kz_jp 29.08.2023:
# According to this method the first day (in daily scale)
#and first layer kz are not possible to calculate 


#temp_daily_2D_str_y_n= temp_daily_2D_2019_1
full_prof_morphro_vriables_obsgrid= [np.array (df_morphro['V_r_m'][1:]) ,
                                     np.array(df_morphro['As_up_bndr_m'][1:]) ,
                                     np.array(df_morphro['Z_m'][1:]) , 
                                     0.5]
                                                                    
                                     
def kz_jp_easier (temp_daily_2D_str_y_n, dt , full_prof_morphro_vriables= full_prof_morphro_vriables_obsgrid, kz_min=1.4*10**-6 ): # , df_str_y_n_without_top_bed# temp_daily_2D_str_y_n in the shape of time* depth , dt should be in day 


    V_r, A_s, Z_m, dz = full_prof_morphro_vriables
    
    a=np.diff(temp_daily_2D_str_y_n[:, 1:], axis=0)/(dt[:, np.newaxis] * 24 * 3600) # temporal increase of temperature excluding the top most layer# temp_daily_2D_str_y_n[:, 1:] just for removing the extra column in axis=1 an doesn't count for time step  
    G=-1* (np.diff(temp_daily_2D_str_y_n, axis=1) /dz)[:-1, ]#vertical temperature gradient at upper boundary of box # same here the diff function is only apply to the column but for getting at the end the same size array the first row values in time axes (axis=0) has been removed 

    # at the end is one day and depth levl lower than tem-2D arry
    kz_jp= np.zeros([temp_daily_2D_str_y_n.shape[0]-1 , temp_daily_2D_str_y_n.shape[1]-1])
    for time in range (0 , temp_daily_2D_str_y_n.shape[0]-1):

        for index, value in enumerate(Z_m):
            

            kz_jp[time,index]= (np.dot(a[time, index:] , V_r[index:]))/ (G[time, index] * A_s[index])

    #kz_jp[kz_jp < kz_min] = kz_min 
    
    #kz_jp[np.isnan(kz_jp)] = kz_min # the nan values of th*is calculation was because of the density of the layer down wasnt bigger than layer above N2<0
    
    #kz_jp[kz_jp == np.inf] = kz_min 
    
    #kz_jp[kz_jp == -np.inf] = kz_min   
    
    return (kz_jp)
    

   

#%%producing period temp for whatever long that I want 7days, 14days, 30days 
# and the duration of it 


def calculate_period_average(data_slice):
    return np.mean(data_slice, axis=0)

def calculate_periodic_averages(temperature_data, days_per_period):
    num_days = len(temperature_data)
    num_periods = num_days // days_per_period
    remaining_days = num_days % days_per_period

    averages = np.array([])  # Initialize an empty array for averages
    duration_total = np.array([])
    
    for i in range(num_periods):
        start_day = i * days_per_period
        end_day = start_day + days_per_period
        avg_temp = calculate_period_average(temperature_data[start_day:end_day])
        averages = np.append(averages, avg_temp)  # Append to the averages array
        duration_total = np.append(duration_total, days_per_period)

    if remaining_days > 0:
        start_day = num_periods * days_per_period
        end_day = num_days
        avg_temp = calculate_period_average(temperature_data[start_day:end_day])
        averages = np.append(averages, avg_temp)
        duration_total = np.append(duration_total, remaining_days)
        
    averages = averages.reshape(-1, len(temperature_data[0]))  # Reshape to 2D array
    
    difference_between_periods =(duration_total[1:] + duration_total[:-1]) / 2 
    
    return averages, duration_total, difference_between_periods


#%%weekly, fortnightly, monthly average of tempearture_2D array 

#2018_1
"""
#weekly:7
temp_weekly_2D_2018_1 ,duration_weekly_total_2018_1 , difference_weekly_periods_2018_1 =calculate_periodic_averages(temp_daily_2D_2018_1[1:, :] ,7 )
#2_weekly:14
temp_fortnightly_2D_2018_1 ,duration_fortnightly_total_2018_1 , difference_fortnightly_periods_2018_1 =calculate_periodic_averages(temp_daily_2D_2018_1[1:, :] ,14 )
#monthly:30
temp_monthly_2D_2018_1 ,duration_monthly_total_2018_1 , difference_monthly_periods_2018_1 =calculate_periodic_averages(temp_daily_2D_2018_1[1:, :] ,30 )


#2018_2

#weekly:7
temp_weekly_2D_2018_2 ,duration_weekly_total_2018_2 , difference_weekly_periods_2018_2 =calculate_periodic_averages(temp_daily_2D_2018_2[1:, :] ,7 )
#2_weekly:14
temp_fortnightly_2D_2018_2 ,duration_fortnightly_total_2018_2 , difference_fortnightly_periods_2018_2 =calculate_periodic_averages(temp_daily_2D_2018_2[1:, :] ,14 )
#monthly:30
temp_monthly_2D_2018_2 ,duration_monthly_total_2018_2 , difference_monthly_periods_2018_2 =calculate_periodic_averages(temp_daily_2D_2018_2[1:, :] ,30 )
"""
#%%

#2019_1

#weekly:7
temp_weekly_2D_2019_1 ,duration_weekly_total_2019_1 , difference_weekly_periods_2019_1 =calculate_periodic_averages(temp_daily_2D_2019_1 ,7 )
#2_weekly:14
temp_fortnightly_2D_2019_1 ,duration_fortnightly_total_2019_1 , difference_fortnightly_periods_2019_1 =calculate_periodic_averages(temp_daily_2D_2019_1 ,14 )
#monthly:30
temp_monthly_2D_2019_1 ,duration_monthly_total_2019_1 , difference_monthly_periods_2019_1 =calculate_periodic_averages(temp_daily_2D_2019_1 ,30 )


#2019_2

#weekly:7
temp_weekly_2D_2019_2 ,duration_weekly_total_2019_2 , difference_weekly_periods_2019_2 =calculate_periodic_averages(temp_daily_2D_2019_2 ,7 )
#2_weekly:14
temp_fortnightly_2D_2019_2 ,duration_fortnightly_total_2019_2 , difference_fortnightly_periods_2019_2 =calculate_periodic_averages(temp_daily_2D_2019_2 ,14 )
#monthly:30
temp_monthly_2D_2019_2 ,duration_monthly_total_2019_2 , difference_monthly_periods_2019_2 =calculate_periodic_averages(temp_daily_2D_2019_2 ,30 )

    
#2020_1

#weekly:7
temp_weekly_2D_2020_1 ,duration_weekly_total_2020_1 , difference_weekly_periods_2020_1 =calculate_periodic_averages(temp_daily_2D_2020_1 ,7 )
#2_weekly:14
temp_fortnightly_2D_2020_1 ,duration_fortnightly_total_2020_1 , difference_fortnightly_periods_2020_1 =calculate_periodic_averages(temp_daily_2D_2020_1 ,14 )
#monthly:30
temp_monthly_2D_2020_1 ,duration_monthly_total_2020_1 , difference_monthly_periods_2020_1 =calculate_periodic_averages(temp_daily_2D_2020_1,30 )


#2021_1

#weekly:7
temp_weekly_2D_2021_1 ,duration_weekly_total_2021_1 , difference_weekly_periods_2021_1 =calculate_periodic_averages(temp_daily_2D_2021_1 ,7 )
#2_weekly:14
temp_fortnightly_2D_2021_1 ,duration_fortnightly_total_2021_1 , difference_fortnightly_periods_2021_1 =calculate_periodic_averages(temp_daily_2D_2021_1 ,14 )
#monthly:30
temp_monthly_2D_2021_1 ,duration_monthly_total_2021_1 , difference_monthly_periods_2021_1 =calculate_periodic_averages(temp_daily_2D_2021_1 ,30 )


#2022_1

#weekly:7
temp_weekly_2D_2022_1 ,duration_weekly_total_2022_1 , difference_weekly_periods_2022_1 =calculate_periodic_averages(temp_daily_2D_2022_1 ,7 )
#2_weekly:14
temp_fortnightly_2D_2022_1 ,duration_fortnightly_total_2022_1 , difference_fortnightly_periods_2022_1 =calculate_periodic_averages(temp_daily_2D_2022_1 ,14 )
#monthly:30
temp_monthly_2D_2022_1 ,duration_monthly_total_2022_1 , difference_monthly_periods_2022_1 =calculate_periodic_averages(temp_daily_2D_2022_1 ,30 )

#%% daily , weekly, fortnightly, monthly kz JP 2018
#2018:
"""
#2018_1
# full prof 
kz_jp_daily_2D_2018_1=kz_jp_easier(temp_daily_2D_2018_1, np.array([1]))
kz_jp_weekly_2D_2018_1=kz_jp_easier(temp_weekly_2D_2018_1, difference_weekly_periods_2018_1 )
kz_jp_fortnightly_2D_2018_1=kz_jp_easier(temp_fortnightly_2D_2018_1, difference_fortnightly_periods_2018_1 )
kz_jp_monthly_2D_2018_1=kz_jp_easier(temp_monthly_2D_2018_1, difference_monthly_periods_2018_1)

# hypolimnion
kz_jp_hypo_daily_2D_2018_1 = kz_jp_daily_2D_2018_1[: , 24:]# 24 is there for 13.5m instead of 23 because can not calculate the first layer values according to this method 
kz_jp_hypo_weekly_2D_2018_1 = kz_jp_weekly_2D_2018_1[: , 24:]
kz_jp_hypo_fortnightly_2D_2018_1 = kz_jp_fortnightly_2D_2018_1[: , 24:]
kz_jp_hypo_monthly_2D_2018_1 = kz_jp_monthly_2D_2018_1[: , 24:]

#2018_2

# full prof 
kz_jp_daily_2D_2018_2=kz_jp_easier(temp_daily_2D_2018_2, np.array([1]))
kz_jp_weekly_2D_2018_2=kz_jp_easier(temp_weekly_2D_2018_2, difference_weekly_periods_2018_2 )
kz_jp_fortnightly_2D_2018_2=kz_jp_easier(temp_fortnightly_2D_2018_2, difference_fortnightly_periods_2018_2 )
kz_jp_monthly_2D_2018_2=kz_jp_easier(temp_monthly_2D_2018_2, difference_monthly_periods_2018_2)

# hypolimnion
kz_jp_hypo_daily_2D_2018_2 = kz_jp_daily_2D_2018_2[: , 24:]
kz_jp_hypo_weekly_2D_2018_2 = kz_jp_weekly_2D_2018_2[: , 24:]
kz_jp_hypo_fortnightly_2D_2018_2 = kz_jp_fortnightly_2D_2018_2[: , 24:]
kz_jp_hypo_monthly_2D_2018_2 = kz_jp_monthly_2D_2018_2[: , 24:]
"""

#%%daily , weekly, fortnightly, monthly kz JP 2019_2022
#2019_1
# full prof 
kz_jp_daily_2D_2019_1=kz_jp_easier(temp_daily_2D_2019_1, np.array([1]))
kz_jp_weekly_2D_2019_1=kz_jp_easier(temp_weekly_2D_2019_1, difference_weekly_periods_2019_1 )
kz_jp_fortnightly_2D_2019_1=kz_jp_easier(temp_fortnightly_2D_2019_1, difference_fortnightly_periods_2019_1 )
kz_jp_monthly_2D_2019_1=kz_jp_easier(temp_monthly_2D_2019_1, difference_monthly_periods_2019_1)


# hypolimnion
kz_jp_hypo_daily_2D_2019_1 = kz_jp_daily_2D_2019_1[: , 25:]
kz_jp_hypo_weekly_2D_2019_1 = kz_jp_weekly_2D_2019_1[: , 25:]
kz_jp_hypo_fortnightly_2D_2019_1 = kz_jp_fortnightly_2D_2019_1[: , 25:]
kz_jp_hypo_monthly_2D_2019_1 = kz_jp_monthly_2D_2019_1[: , 25:]

#2019_2
# full prof 
kz_jp_daily_2D_2019_2=kz_jp_easier(temp_daily_2D_2019_2, np.array([1]))
kz_jp_weekly_2D_2019_2=kz_jp_easier(temp_weekly_2D_2019_2, difference_weekly_periods_2019_2 )
kz_jp_fortnightly_2D_2019_2=kz_jp_easier(temp_fortnightly_2D_2019_2, difference_fortnightly_periods_2019_2 )
kz_jp_monthly_2D_2019_2=kz_jp_easier(temp_monthly_2D_2019_2, difference_monthly_periods_2019_2)

# hypolimnion
kz_jp_hypo_daily_2D_2019_2 = kz_jp_daily_2D_2019_2[: , 25:]
kz_jp_hypo_weekly_2D_2019_2 = kz_jp_weekly_2D_2019_2[: , 25:]

# the only problem with using weekly was the las week of 2019_2 with kz of negetive 
# means decrease of temperature which makes sense 

kz_jp_hypo_weekly_2D_2019_2= np.where (kz_jp_hypo_weekly_2D_2019_2<1.4*10**-7, 1.4*10**-7 ,kz_jp_hypo_weekly_2D_2019_2 ) 

kz_jp_hypo_fortnightly_2D_2019_2 = kz_jp_fortnightly_2D_2019_2[: , 25:]
kz_jp_hypo_monthly_2D_2019_2 = kz_jp_monthly_2D_2019_2[: , 25:]

#2020_1
# full prof 
kz_jp_daily_2D_2020_1=kz_jp_easier(temp_daily_2D_2020_1, np.array([1]))
kz_jp_weekly_2D_2020_1=kz_jp_easier(temp_weekly_2D_2020_1, difference_weekly_periods_2020_1 )
kz_jp_fortnightly_2D_2020_1=kz_jp_easier(temp_fortnightly_2D_2020_1, difference_fortnightly_periods_2020_1 )
kz_jp_monthly_2D_2020_1=kz_jp_easier(temp_monthly_2D_2020_1, difference_monthly_periods_2020_1)

# hypolimnion
kz_jp_hypo_daily_2D_2020_1 = kz_jp_daily_2D_2020_1[: , 25:]
kz_jp_hypo_weekly_2D_2020_1 = kz_jp_weekly_2D_2020_1[: , 25:]
kz_jp_hypo_fortnightly_2D_2020_1 = kz_jp_fortnightly_2D_2020_1[: , 25:]
kz_jp_hypo_monthly_2D_2020_1 = kz_jp_monthly_2D_2020_1[: , 25:]

#2021_1
# full prof   
kz_jp_daily_2D_2021_1=kz_jp_easier(temp_daily_2D_2021_1, np.array([1]))
kz_jp_weekly_2D_2021_1=kz_jp_easier(temp_weekly_2D_2021_1, difference_weekly_periods_2021_1 )
kz_jp_fortnightly_2D_2021_1=kz_jp_easier(temp_fortnightly_2D_2021_1, difference_fortnightly_periods_2021_1 )
kz_jp_monthly_2D_2021_1=kz_jp_easier(temp_monthly_2D_2021_1, difference_monthly_periods_2021_1)
# hypolimnion
kz_jp_hypo_daily_2D_2021_1 = kz_jp_daily_2D_2021_1[: , 25:]
kz_jp_hypo_weekly_2D_2021_1 = kz_jp_weekly_2D_2021_1[: , 25:]
kz_jp_hypo_fortnightly_2D_2021_1 = kz_jp_fortnightly_2D_2021_1[: , 25:]
kz_jp_hypo_monthly_2D_2021_1 = kz_jp_monthly_2D_2021_1[: , 25:]   



#2022:
# full prof     
kz_jp_daily_2D_2022_1=kz_jp_easier(temp_daily_2D_2022_1, np.array([1]))
kz_jp_weekly_2D_2022_1=kz_jp_easier(temp_weekly_2D_2022_1, difference_weekly_periods_2022_1 )
kz_jp_fortnightly_2D_2022_1=kz_jp_easier(temp_fortnightly_2D_2022_1, difference_fortnightly_periods_2022_1 )
kz_jp_monthly_2D_2022_1=kz_jp_easier(temp_monthly_2D_2022_1, difference_monthly_periods_2022_1)

# hypolimnion
kz_jp_hypo_daily_2D_2022_1 = kz_jp_daily_2D_2022_1[: , 25:]
kz_jp_hypo_weekly_2D_2022_1 = kz_jp_weekly_2D_2022_1[: , 25:]
kz_jp_hypo_fortnightly_2D_2022_1 = kz_jp_fortnightly_2D_2022_1[: , 25:]
kz_jp_hypo_monthly_2D_2022_1 = kz_jp_monthly_2D_2022_1[: , 25:]

#%%daily , weekly, fortnightly, monthly kz bv 2019_2022
#==============Should work on it 
#2019_1
# full prof 
kz_bv_weekly_2D_2019_1=kz_bv_easier(temp_weekly_2D_2019_1)[0]#, difference_weekly_periods_2019_1 )
kz_bv_fortnightly_2D_2019_1=kz_bv_easier(temp_fortnightly_2D_2019_1)[0]
kz_bv_monthly_2D_2019_1=kz_bv_easier(temp_monthly_2D_2019_1)[0]

# hypolimnion
kz_bv_hypo_weekly_2D_2019_1 = kz_bv_easier(temp_weekly_2D_2019_1[:, 25:])[0]
kz_bv_hypo_fortnightly_2D_2019_1 = kz_bv_easier(temp_fortnightly_2D_2019_1[:, 25:])[0]
kz_bv_hypo_monthly_2D_2019_1 = kz_bv_easier(temp_monthly_2D_2019_1[:, 25:])[0]


#2019_2
# full prof 
kz_bv_weekly_2D_2019_2=kz_bv_easier(temp_weekly_2D_2019_2)[0]#, difference_weekly_periods_2019_2 )
kz_bv_fortnightly_2D_2019_2=kz_bv_easier(temp_fortnightly_2D_2019_2)[0]
kz_bv_monthly_2D_2019_2=kz_bv_easier(temp_monthly_2D_2019_2)[0]

# hypolimnion
kz_bv_hypo_weekly_2D_2019_2 = kz_bv_easier(temp_weekly_2D_2019_2[:, 25:])[0]
kz_bv_hypo_fortnightly_2D_2019_2 = kz_bv_easier(temp_fortnightly_2D_2019_2[:, 25:])[0]
kz_bv_hypo_monthly_2D_2019_2 = kz_bv_easier(temp_monthly_2D_2019_2[:, 25:])[0]

#2020_1
# full prof 
kz_bv_weekly_2D_2020_1=kz_bv_easier(temp_weekly_2D_2020_1)[0]#, difference_weekly_periods_2020_1 )
kz_bv_fortnightly_2D_2020_1=kz_bv_easier(temp_fortnightly_2D_2020_1)[0]
kz_bv_monthly_2D_2020_1=kz_bv_easier(temp_monthly_2D_2020_1)[0]

# hypolimnion
kz_bv_hypo_weekly_2D_2020_1 = kz_bv_easier(temp_weekly_2D_2020_1[:, 25:])[0]
kz_bv_hypo_fortnightly_2D_2020_1 = kz_bv_easier(temp_fortnightly_2D_2020_1[:, 25:])[0]
kz_bv_hypo_monthly_2D_2020_1 = kz_bv_easier(temp_monthly_2D_2020_1[:, 25:])[0]


#2021_1
kz_bv_weekly_2D_2021_1=kz_bv_easier(temp_weekly_2D_2021_1)[0]#, difference_weekly_periods_2021_1 )
kz_bv_fortnightly_2D_2021_1=kz_bv_easier(temp_fortnightly_2D_2021_1)[0]
kz_bv_monthly_2D_2021_1=kz_bv_easier(temp_monthly_2D_2021_1)[0]

# hypolimnion
kz_bv_hypo_weekly_2D_2021_1 = kz_bv_easier(temp_weekly_2D_2021_1[:, 25:])[0]
kz_bv_hypo_fortnightly_2D_2021_1 = kz_bv_easier(temp_fortnightly_2D_2021_1[:, 25:])[0]
kz_bv_hypo_monthly_2D_2021_1 = kz_bv_easier(temp_monthly_2D_2021_1[:, 25:])[0]


#2022_1
kz_bv_weekly_2D_2022_1=kz_bv_easier(temp_weekly_2D_2022_1)[0]#, difference_weekly_periods_2022_1 )
kz_bv_fortnightly_2D_2022_1=kz_bv_easier(temp_fortnightly_2D_2022_1)[0]
kz_bv_monthly_2D_2022_1=kz_bv_easier(temp_monthly_2D_2022_1)[0]

# hypolimnion
kz_bv_hypo_weekly_2D_2022_1 = kz_bv_easier(temp_weekly_2D_2022_1[:, 25:])[0]
kz_bv_hypo_fortnightly_2D_2022_1 = kz_bv_easier(temp_fortnightly_2D_2022_1[:, 25:])[0]
kz_bv_hypo_monthly_2D_2022_1 = kz_bv_easier(temp_monthly_2D_2022_1[:, 25:])[0]


#%% usage of daily estimation of kz :
    
    
kz_jp_hypo_daily_2D_2019_1[kz_jp_hypo_daily_2D_2019_1<1.4*10**-7]=1.4*10**-7    
kz_jp_hypo_daily_2D_2019_2[kz_jp_hypo_daily_2D_2019_2<1.4*10**-7]=1.4*10**-7   
kz_jp_hypo_daily_2D_2020_1[kz_jp_hypo_daily_2D_2020_1<1.4*10**-7]=1.4*10**-7     
kz_jp_hypo_daily_2D_2021_1[kz_jp_hypo_daily_2D_2021_1<1.4*10**-7]=1.4*10**-7   
kz_jp_hypo_daily_2D_2022_1[kz_jp_hypo_daily_2D_2022_1<1.4*10**-7]=1.4*10**-7   


kz_jp_hypo_daily_2D_2019_2022=np.concatenate((kz_jp_hypo_daily_2D_2019_1, kz_jp_hypo_daily_2D_2019_2,
                                           kz_jp_hypo_daily_2D_2020_1,kz_jp_hypo_daily_2D_2021_1,
                                           kz_jp_hypo_daily_2D_2022_1))

kz_jp_hypo_daily_2D_2019_1

kz_jp_hypo_daily_2D_2019_2

kz_jp_hypo_daily_2D_2020_1

kz_jp_hypo_daily_2D_2021_1

kz_jp_hypo_daily_2D_2022_1




array_statistics(kz_jp_hypo_daily_2D_2019_2022) 
{'Minimum': 1.3999999999999998e-07,
 'Maximum': 0.0008022413040939742,
 'Mean': 1.3481432603415191e-05,
 'Median': 4.349472434578609e-06,
 'Standard Deviation': 3.581426906895138e-05}

#%% Changing JP weekly to the size of daily timestep 
 
    
 
#2019_1:    
kz_jp_hypo_only_full_weekly_2D_2019_1=np.repeat(kz_jp_hypo_weekly_2D_2019_1[ :-1, :], 7, axis=0)
# Get the last row of kz_jp_hypo_weekly_2D_2019_1
last_row = kz_jp_hypo_weekly_2D_2019_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2019_1[-1]+ duration_weekly_total_2019_1[-2]
extra_rows_of_weekly_2D_2019_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_weekly_2D_2019_1
kz_jp_hypo_weekly_2D_2019_1_daily = np.vstack((kz_jp_hypo_only_full_weekly_2D_2019_1, extra_rows_of_weekly_2D_2019_1))    
    

#2019_2    
kz_jp_hypo_only_full_weekly_2D_2019_2=np.repeat(kz_jp_hypo_weekly_2D_2019_2[ :-1, :], 7, axis=0)
# Get the last row of kz_jp_hypo_weekly_2D_2019_2
last_row = kz_jp_hypo_weekly_2D_2019_2[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2019_2[-1]+duration_weekly_total_2019_2[-2]
extra_rows_of_weekly_2D_2019_2 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_weekly_2D_2019_2
kz_jp_hypo_weekly_2D_2019_2_daily = np.vstack((kz_jp_hypo_only_full_weekly_2D_2019_2, extra_rows_of_weekly_2D_2019_2))    
    
 
    
#2020_1:    
kz_jp_hypo_only_full_weekly_2D_2020_1=np.repeat(kz_jp_hypo_weekly_2D_2020_1[ :-1, :], 7, axis=0)
# Get the last row of kz_jp_hypo_weekly_2D_2020_1
last_row = kz_jp_hypo_weekly_2D_2020_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2020_1[-1]+duration_weekly_total_2020_1[-2]
extra_rows_of_weekly_2D_2020_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_weekly_2D_2020_1
kz_jp_hypo_weekly_2D_2020_1_daily = np.vstack((kz_jp_hypo_only_full_weekly_2D_2020_1, extra_rows_of_weekly_2D_2020_1))  

 
#2021_1:    
kz_jp_hypo_only_full_weekly_2D_2021_1=np.repeat(kz_jp_hypo_weekly_2D_2021_1[ :-1, :], 7, axis=0)
# Get the last row of kz_jp_hypo_weekly_2D_2021_1
last_row = kz_jp_hypo_weekly_2D_2021_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2021_1[-1]+duration_weekly_total_2021_1[-2]
extra_rows_of_weekly_2D_2021_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_weekly_2D_2021_1
kz_jp_hypo_weekly_2D_2021_1_daily = np.vstack((kz_jp_hypo_only_full_weekly_2D_2021_1, extra_rows_of_weekly_2D_2021_1))    

 
#2022_1:    
kz_jp_hypo_only_full_weekly_2D_2022_1=np.repeat(kz_jp_hypo_weekly_2D_2022_1[ :-1, :], 7, axis=0)
# Get the last row of kz_jp_hypo_weekly_2D_2022_1
last_row = kz_jp_hypo_weekly_2D_2022_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2022_1[-1]+duration_weekly_total_2022_1[-2]
extra_rows_of_weekly_2D_2022_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_weekly_2D_2022_1
kz_jp_hypo_weekly_2D_2022_1_daily = np.vstack((kz_jp_hypo_only_full_weekly_2D_2022_1, extra_rows_of_weekly_2D_2022_1))    

#%% doing the stratistical analyses after allocating each day values of kz from weekly estimated values 
#2019_2022 weekly 

kz_jp_weekly_indailytimestep_2D_2019_2022=np.concatenate((kz_jp_hypo_weekly_2D_2019_1_daily, kz_jp_hypo_weekly_2D_2019_2_daily,
                                           kz_jp_hypo_weekly_2D_2020_1_daily,kz_jp_hypo_weekly_2D_2021_1_daily,
                                           kz_jp_hypo_weekly_2D_2022_1_daily))


kz_jp_hypo_weekly_2D_2019_1_daily

kz_jp_hypo_weekly_2D_2019_2_daily

kz_jp_hypo_weekly_2D_2020_1_daily

kz_jp_hypo_weekly_2D_2021_1_daily

kz_jp_hypo_weekly_2D_2022_1_daily



array_statistics(kz_jp_weekly_indailytimestep_2D_2019_2022) 

"""
ratio of Kz_gotm to kz_jp_weekly_indailytimestep_2D_2019_2022: 
8.49043334584075e-06/8.125150143660237e-06
Out[1864]: 1.045

{'Minimum': 1.3999999999999998e-07,
 'Maximum': 0.00011788004741596368,
 'Mean': 8.49043334584075e-06,
 'Median': 4.848760232439378e-06,
 'Standard Deviation': 1.3530763302043578e-05}

"""



#%% usage of fortnightly is better excluding 2018(more spefically 2018_2 but 2018-1 saturation level was about 120% ) excluding 2018 88%:
 
    
 
#2019_1:    
kz_jp_hypo_only_full_fortnightly_2D_2019_1=np.repeat(kz_jp_hypo_fortnightly_2D_2019_1[ :-1, :], 14, axis=0)
# Get the last row of kz_jp_hypo_fortnightly_2D_2019_1
last_row = kz_jp_hypo_fortnightly_2D_2019_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2019_1[-1]+ duration_fortnightly_total_2019_1[-2]
extra_rows_of_fortnightly_2D_2019_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_fortnightly_2D_2019_1
kz_jp_hypo_fortnightly_2D_2019_1_daily = np.vstack((kz_jp_hypo_only_full_fortnightly_2D_2019_1, extra_rows_of_fortnightly_2D_2019_1))    
kz_jp_hypo_fortnightly_2D_2019_1_daily[kz_jp_hypo_fortnightly_2D_2019_1_daily< 1.4*10**-7]= 1.4*10**-7        

#2019_2    
kz_jp_hypo_only_full_fortnightly_2D_2019_2=np.repeat(kz_jp_hypo_fortnightly_2D_2019_2[ :-1, :], 14, axis=0)
# Get the last row of kz_jp_hypo_fortnightly_2D_2019_2
last_row = kz_jp_hypo_fortnightly_2D_2019_2[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2019_2[-1]+duration_fortnightly_total_2019_2[-2]
extra_rows_of_fortnightly_2D_2019_2 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_fortnightly_2D_2019_2
kz_jp_hypo_fortnightly_2D_2019_2_daily = np.vstack((kz_jp_hypo_only_full_fortnightly_2D_2019_2, extra_rows_of_fortnightly_2D_2019_2))    
kz_jp_hypo_fortnightly_2D_2019_2_daily[kz_jp_hypo_fortnightly_2D_2019_2_daily< 1.4*10**-7]= 1.4*10**-7    
 
    
#2020_1:    
kz_jp_hypo_only_full_fortnightly_2D_2020_1=np.repeat(kz_jp_hypo_fortnightly_2D_2020_1[ :-1, :], 14, axis=0)
# Get the last row of kz_jp_hypo_fortnightly_2D_2020_1
last_row = kz_jp_hypo_fortnightly_2D_2020_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2020_1[-1]+duration_fortnightly_total_2020_1[-2]
extra_rows_of_fortnightly_2D_2020_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_fortnightly_2D_2020_1
kz_jp_hypo_fortnightly_2D_2020_1_daily = np.vstack((kz_jp_hypo_only_full_fortnightly_2D_2020_1, extra_rows_of_fortnightly_2D_2020_1))  
kz_jp_hypo_fortnightly_2D_2020_1_daily[kz_jp_hypo_fortnightly_2D_2020_1_daily< 1.4*10**-7]= 1.4*10**-7
 
#2021_1:    
kz_jp_hypo_only_full_fortnightly_2D_2021_1=np.repeat(kz_jp_hypo_fortnightly_2D_2021_1[ :-1, :], 14, axis=0)
# Get the last row of kz_jp_hypo_fortnightly_2D_2021_1
last_row = kz_jp_hypo_fortnightly_2D_2021_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2021_1[-1]+duration_fortnightly_total_2021_1[-2]
extra_rows_of_fortnightly_2D_2021_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_fortnightly_2D_2021_1
kz_jp_hypo_fortnightly_2D_2021_1_daily = np.vstack((kz_jp_hypo_only_full_fortnightly_2D_2021_1, extra_rows_of_fortnightly_2D_2021_1))    
kz_jp_hypo_fortnightly_2D_2021_1_daily[kz_jp_hypo_fortnightly_2D_2021_1_daily< 1.4*10**-7]= 1.4*10**-7
 
#2022_1:    
kz_jp_hypo_only_full_fortnightly_2D_2022_1=np.repeat(kz_jp_hypo_fortnightly_2D_2022_1[ :-1, :], 14, axis=0)
# Get the last row of kz_jp_hypo_fortnightly_2D_2022_1
last_row = kz_jp_hypo_fortnightly_2D_2022_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2022_1[-1]+duration_fortnightly_total_2022_1[-2]
extra_rows_of_fortnightly_2D_2022_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_fortnightly_2D_2022_1
kz_jp_hypo_fortnightly_2D_2022_1_daily = np.vstack((kz_jp_hypo_only_full_fortnightly_2D_2022_1, extra_rows_of_fortnightly_2D_2022_1))    
kz_jp_hypo_fortnightly_2D_2022_1_daily[kz_jp_hypo_fortnightly_2D_2022_1_daily< 1.4*10**-7]= 1.4*10**-7 
  


#%% doing the stratistical analyses after allocating each day values of kz from fortnightly estimated values 
#2019_2022 fortnightly 

kz_jp_fortnightly_indailytimestep_2D_2019_2022=np.concatenate((kz_jp_hypo_fortnightly_2D_2019_1_daily, kz_jp_hypo_fortnightly_2D_2019_2_daily,
                                           kz_jp_hypo_fortnightly_2D_2020_1_daily,kz_jp_hypo_fortnightly_2D_2021_1_daily,
                                           kz_jp_hypo_fortnightly_2D_2022_1_daily))

array_statistics(kz_jp_fortnightly_indailytimestep_2D_2019_2022) 
{'Minimum': 1.3999999999999998e-07,
 'Maximum': 6.388749719463389e-05,
 'Mean': 8.018570554666706e-06,
 'Median': 5.428489549272845e-06,
 'Standard Deviation': 1.0610202372886593e-05}
"""
8.018570554666706e-06/8.125150143660237e-06= 0.9868827545203345

in the same order of magnitude 

array_statistics(kz_hypo_all) in gotm simulation:
Out[347]: 
{'Minimum': 9.405572427567677e-07,
 'Maximum': 0.00017870900046546012,
 'Mean': 8.125150143660237e-06,
 'Standard Deviation': 1.2481417929041973e-05}

"""

kz_jp_fortnightly_indailytimestep_2D_2019_2022[: , 0]


#%%testing the normality of boundry condition for fornightly Kz in first layer of hypolimnion 
# kz_jp_fortnightly_indailytimestep_2D_2019_2022[: , 0] 
# I am going to apply for each deoxygenation period 
# instead of one value #?#?# for future is going to be same 


#kz_jp_hypo_fortnightly_2D_2019_1_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2019_2_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2020_1_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2021_1_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2022_1_daily[: , 0]




      
#plotting the histogram 
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))

# Plot the distribution histogram
sns.histplot(np.array(kz_jp_fortnightly_indailytimestep_2D_2019_2022[: , 0]), kde=True, color='grey', edgecolor='black', ax=ax1)#color='blue'
ax1.get_lines()[0].set_color('red') 
ax1.set_xlabel('Fortnighly JP Kz [m$^{2}$ s$^{-1}$]')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution Plot')

# Plot the Q-Q plot
stats.probplot(np.array(kz_jp_fortnightly_indailytimestep_2D_2019_2022[: , 0]), dist="norm", plot=ax2)
ax2.set_title("Q-Q Plot")

# Modify the color of points in the Q-Q plot
ax2.get_lines()[0].set_markerfacecolor('grey')  # Set marker face color
ax2.get_lines()[0].set_markeredgecolor('grey')  # Set marker edge color
ax2.set_ylabel('Sample quantiles')
ax2.set_xlabel('Normal theorical quantiles')
# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('normality_test_kz_JP_fortnighly_in14mlayer.png', dpi= 300)



#%%Plot for paper boundry condition and inital condition concentartion diffeerences 



boundry_condition= df_str_nomixing_2019_2022[df_str_nomixing_2019_2022['Z_m']==-13.5]['DO'] - df_str_nomixing_2019_2022[df_str_nomixing_2019_2022['Z_m']==-14]['DO']

      
#plotting the histogram 
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6), sharey=True )

# Plot the distribution histogram
sns.histplot(np.array(boundry_condition), kde=True, color='grey', edgecolor='black', ax=ax1)#color='blue'
ax1.get_lines()[0].set_color('red') 
ax1.set_xlabel('Concentration difference [mg L$^{-1}$]', fontsize=14)
ax1.set_ylabel('Frequency', fontsize=16)
#ax1.set_title('Distribution Plot')
ax1.set_ylim([0, 30])
ax1.tick_params(axis='both', which='major', labelsize=14)
# Plot the distribution histogram
# Add subtitle 'a' to ax1
ax1.text(0.98, 0.98, '(a)', transform=ax1.transAxes, fontsize=14, fontweight='bold', va='top', ha='right')



sns.histplot(np.array(kz_jp_fortnightly_indailytimestep_2D_2019_2022[: , 0]), kde=True, color='grey', edgecolor='black', ax=ax2)#color='blue'
ax2.get_lines()[0].set_color('red') 
ax2.set_xlabel('Fortnighly K$_{z}$ [m$^{2}$ s$^{-1}$]', fontsize=14)
ax2.set_ylabel('Frequency', fontsize=16)
#ax2.set_title('Distribution Plot')
ax2.set_ylim([0, 100])
ax2.tick_params(axis='both', which='major', labelsize=14)
ax2.set_xscale('log')
# Adjust layout
plt.tight_layout()
# Add subtitle 'b' to ax2
ax2.text(0.98, 0.98, '(b)', transform=ax2.transAxes, fontsize=14, fontweight='bold', va='top', ha='right')

# Save the figure
plt.savefig('normality_test_boundry_condition_kz_median.png', dpi= 300)


#%%the right-skewed or positive skewed distribution plot 
#kz_jp_hypo_fortnightly_2D_2019_1_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2019_2_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2020_1_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2021_1_daily[: , 0]
#kz_jp_hypo_fortnightly_2D_2022_1_daily[: , 0]


#===========the Shapiro–Wilk test is used for testing normality.
from scipy.stats import shapiro

# Perform the Shapiro-Wilk test
stat, p_value = shapiro(np.array(kz_jp_fortnightly_indailytimestep_2D_2019_2022[: , 0]))

# Print the results
print(f"Shapiro-Wilk Test Statistic: {stat}, p-value: {p_value}")
if p_value > 0.05:
    print("The data appears to be normally distributed.")
else:
    print("The data does not appear to be normally distributed.")
    
    
#The data does not appear to be normally distributed for each deoxygenation period with all the 
# if the Shapiro_wilk statictic was 1-> normal distributed 
# if p_value was grater than 0.05 it is going to be normal 


#2019_2022:
#Shapiro-Wilk Test Statistic: 0.4702215790748596, p-value: 4.543592029143324e-33
#The data does not appear to be normally distributed.    
    
    


"""
#2019_1# kz_jp_hypo_fortnightly_2D_2019_1_daily
kz_jp_fortnightly_indailytimestep_2D_2019_1
Shapiro-Wilk Test Statistic: 0.6054048538208008, p-value: 5.19891796280092e-10
The data does not appear to be normally distributed.

#2019_2:
Shapiro-Wilk Test Statistic: 0.5651365518569946, p-value: 6.117539808059291e-11
The data does not appear to be normally distributed.

#2020:
Shapiro-Wilk Test Statistic: 0.8517363667488098, p-value: 7.473804686242147e-09
The data does not appear to be normally distributed.    

#2021:
Shapiro-Wilk Test Statistic: 0.6179895401000977, p-value: 2.8470619653877312e-15
The data does not appear to be normally distributed.    

#2022:
Shapiro-Wilk Test Statistic: 0.8154951333999634, p-value: 6.661300400168102e-10
The data does not appear to be normally distributed.    
"""
#%%Kz-jp_monthly all years analyses:
    
"""
kz_jp_monthly_2D_2018_2022= np.concatenate((  kz_jp_hypo_monthly_2D_2018_1, kz_jp_hypo_monthly_2D_2018_2, kz_jp_hypo_monthly_2D_2019_1, kz_jp_hypo_monthly_2D_2019_2, kz_jp_hypo_monthly_2D_2020_1 , kz_jp_hypo_monthly_2D_2021_1, kz_jp_hypo_monthly_2D_2022_1), axis=0)
array_statistics(kz_jp_monthly_2D_2018_2022) 

{'Minimum': 3.926455078901615e-07,
 'Maximum': 2.0210951399119342e-05,
 'Mean': 4.6696209683945835e-06,
 'Standard Deviation': 2.9722639025522714e-06}

"""


kz_jp_monthly_2D_2019_2022= np.concatenate((  kz_jp_hypo_monthly_2D_2019_1, kz_jp_hypo_monthly_2D_2019_2, kz_jp_hypo_monthly_2D_2020_1 , kz_jp_hypo_monthly_2D_2021_1, kz_jp_hypo_monthly_2D_2022_1), axis=0)
array_statistics(kz_jp_monthly_2D_2019_2022)    
"""
{'Minimum': 4.33249044186465e-07,
 'Maximum': 1.4736562288328243e-05,
 'Mean': 6.6148120509904696e-06,
 'Median': 5.225979826623323e-06,
 'Standard Deviation': 3.5080999550703654e-06}

in the same order of magnitude 

array_statistics(kz_hypo_all) in gotm simulation:
Out[347]: 
{'Minimum': 9.405572427567677e-07,
 'Maximum': 0.00017870900046546012,
 'Mean': 8.125150143660237e-06,
 'Standard Deviation': 1.2481417929041973e-05}

"""


 
#2019_1:    
kz_jp_hypo_only_full_monthly_2D_2019_1=np.repeat(kz_jp_hypo_monthly_2D_2019_1[ :-1, :], 30, axis=0)
# Get the last row of kz_jp_hypo_monthly_2D_2019_1
last_row = kz_jp_hypo_monthly_2D_2019_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2019_1[-1]+ duration_monthly_total_2019_1[-2]
extra_rows_of_monthly_2D_2019_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_monthly_2D_2019_1
kz_jp_hypo_monthly_2D_2019_1_daily = np.vstack((kz_jp_hypo_only_full_monthly_2D_2019_1, extra_rows_of_monthly_2D_2019_1))    
kz_jp_hypo_monthly_2D_2019_1_daily[kz_jp_hypo_monthly_2D_2019_1_daily< 1.4*10**-7]= 1.4*10**-7        

#2019_2    
kz_jp_hypo_only_full_monthly_2D_2019_2=np.repeat(kz_jp_hypo_monthly_2D_2019_2[ :-1, :], 30, axis=0)
# Get the last row of kz_jp_hypo_monthly_2D_2019_2
last_row = kz_jp_hypo_monthly_2D_2019_2[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2019_2[-1]+duration_monthly_total_2019_2[-2]
extra_rows_of_monthly_2D_2019_2 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_monthly_2D_2019_2
kz_jp_hypo_monthly_2D_2019_2_daily = np.vstack((kz_jp_hypo_only_full_monthly_2D_2019_2, extra_rows_of_monthly_2D_2019_2))    
kz_jp_hypo_monthly_2D_2019_2_daily[kz_jp_hypo_monthly_2D_2019_2_daily< 1.4*10**-7]= 1.4*10**-7    
 
    
#2020_1:    
kz_jp_hypo_only_full_monthly_2D_2020_1=np.repeat(kz_jp_hypo_monthly_2D_2020_1[ :-1, :], 30, axis=0)
# Get the last row of kz_jp_hypo_monthly_2D_2020_1
last_row = kz_jp_hypo_monthly_2D_2020_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2020_1[-1]+duration_monthly_total_2020_1[-2]
extra_rows_of_monthly_2D_2020_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_monthly_2D_2020_1
kz_jp_hypo_monthly_2D_2020_1_daily = np.vstack((kz_jp_hypo_only_full_monthly_2D_2020_1, extra_rows_of_monthly_2D_2020_1))  
kz_jp_hypo_monthly_2D_2020_1_daily[kz_jp_hypo_monthly_2D_2020_1_daily< 1.4*10**-7]= 1.4*10**-7
 
#2021_1:    
kz_jp_hypo_only_full_monthly_2D_2021_1=np.repeat(kz_jp_hypo_monthly_2D_2021_1[ :-1, :], 30, axis=0)
# Get the last row of kz_jp_hypo_monthly_2D_2021_1
last_row = kz_jp_hypo_monthly_2D_2021_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2021_1[-1]+duration_monthly_total_2021_1[-2]
extra_rows_of_monthly_2D_2021_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_monthly_2D_2021_1
kz_jp_hypo_monthly_2D_2021_1_daily = np.vstack((kz_jp_hypo_only_full_monthly_2D_2021_1, extra_rows_of_monthly_2D_2021_1))    
kz_jp_hypo_monthly_2D_2021_1_daily[kz_jp_hypo_monthly_2D_2021_1_daily< 1.4*10**-7]= 1.4*10**-7
 
#2022_1:    
kz_jp_hypo_only_full_monthly_2D_2022_1=np.repeat(kz_jp_hypo_monthly_2D_2022_1[ :-1, :], 30, axis=0)
# Get the last row of kz_jp_hypo_monthly_2D_2022_1
last_row = kz_jp_hypo_monthly_2D_2022_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2022_1[-1]+duration_monthly_total_2022_1[-2]
extra_rows_of_monthly_2D_2022_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_jp_hypo_only_full_monthly_2D_2022_1
kz_jp_hypo_monthly_2D_2022_1_daily = np.vstack((kz_jp_hypo_only_full_monthly_2D_2022_1, extra_rows_of_monthly_2D_2022_1))    
kz_jp_hypo_monthly_2D_2022_1_daily[kz_jp_hypo_monthly_2D_2022_1_daily< 1.4*10**-7]= 1.4*10**-7 
  


kz_jp_monthly_indailytimestep_2D_2019_2022=np.concatenate((kz_jp_hypo_monthly_2D_2019_1_daily, kz_jp_hypo_monthly_2D_2019_2_daily,
                                           kz_jp_hypo_monthly_2D_2020_1_daily,kz_jp_hypo_monthly_2D_2021_1_daily,
                                           kz_jp_hypo_monthly_2D_2022_1_daily))


array_statistics(kz_jp_monthly_indailytimestep_2D_2019_2022) 



{'Minimum': 4.33249044186465e-07,
 'Maximum': 1.4736562288328243e-05,
 'Mean': 6.325114811101496e-06,
 'Median': 5.115136073736642e-06,
 'Standard Deviation': 3.5756705387789404e-06}

 6.325114811101496e-06/8.125150143660237e-06= 0.77
"""
in the same order of magnitude 

array_statistics(kz_hypo_all) in gotm simulation:
Out[347]: 
{'Minimum': 9.405572427567677e-07,
 'Maximum': 0.00017870900046546012,
 'Mean': 8.125150143660237e-06,
 'Standard Deviation': 1.2481417929041973e-05}

"""
#%%
#results of daily bv_2019_2022:
{'Minimum': 6.148294383271784e-06,
 'Maximum': 8.197670147965065e-05,
 'Mean': 2.5075520976021956e-05,
 'Standard Deviation': 9.07323094054095e-06}


#%%============================Kz bv correction and making them in daily scale size:
    
 
    
kz_bv_hypo_daily_2D_2019_1[kz_bv_hypo_daily_2D_2019_1<1.4*10**-7]=1.4*10**-7    
kz_bv_hypo_daily_2D_2019_2[kz_bv_hypo_daily_2D_2019_2<1.4*10**-7]=1.4*10**-7   
kz_bv_hypo_daily_2D_2020_1[kz_bv_hypo_daily_2D_2020_1<1.4*10**-7]=1.4*10**-7     
kz_bv_hypo_daily_2D_2021_1[kz_bv_hypo_daily_2D_2021_1<1.4*10**-7]=1.4*10**-7   
kz_bv_hypo_daily_2D_2022_1[kz_bv_hypo_daily_2D_2022_1<1.4*10**-7]=1.4*10**-7   


kz_bv_hypo_daily_2D_2019_2022=np.concatenate((kz_bv_hypo_daily_2D_2019_1, kz_bv_hypo_daily_2D_2019_2,
                                           kz_bv_hypo_daily_2D_2020_1,kz_bv_hypo_daily_2D_2021_1,
                                           kz_bv_hypo_daily_2D_2022_1))

kz_bv_hypo_daily_2D_2019_1

kz_bv_hypo_daily_2D_2019_2

kz_bv_hypo_daily_2D_2020_1

kz_bv_hypo_daily_2D_2021_1

kz_bv_hypo_daily_2D_2022_1




array_statistics(kz_bv_hypo_daily_2D_2019_2022) 
{'Minimum': 6.148294383271784e-06,
 'Maximum': 8.197670147965065e-05,
 'Mean': 2.487784819771461e-05,
 'Median': 2.3434438298948343e-05,
 'Standard Deviation': 9.041695403029782e-06}



#%% Changing bv weekly to the size of daily timestep 

 
#2019_1:    
kz_bv_hypo_only_full_weekly_2D_2019_1=np.repeat(kz_bv_hypo_weekly_2D_2019_1[ :-1, :], 7, axis=0)
# Get the last row of kz_bv_hypo_weekly_2D_2019_1
last_row = kz_bv_hypo_weekly_2D_2019_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2019_1[-1]#+ duration_weekly_total_2019_1[-2]
extra_rows_of_weekly_2D_2019_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_weekly_2D_2019_1
kz_bv_hypo_weekly_2D_2019_1_daily = np.vstack((kz_bv_hypo_only_full_weekly_2D_2019_1, extra_rows_of_weekly_2D_2019_1))    
    

#2019_2    
kz_bv_hypo_only_full_weekly_2D_2019_2=np.repeat(kz_bv_hypo_weekly_2D_2019_2[ :-1, :], 7, axis=0)
# Get the last row of kz_bv_hypo_weekly_2D_2019_2
last_row = kz_bv_hypo_weekly_2D_2019_2[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2019_2[-1]#+duration_weekly_total_2019_2[-2]
extra_rows_of_weekly_2D_2019_2 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_weekly_2D_2019_2
kz_bv_hypo_weekly_2D_2019_2_daily = np.vstack((kz_bv_hypo_only_full_weekly_2D_2019_2, extra_rows_of_weekly_2D_2019_2))    
    
 
    
#2020_1:    
kz_bv_hypo_only_full_weekly_2D_2020_1=np.repeat(kz_bv_hypo_weekly_2D_2020_1[ :-1, :], 7, axis=0)
# Get the last row of kz_bv_hypo_weekly_2D_2020_1
last_row = kz_bv_hypo_weekly_2D_2020_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2020_1[-1]#+duration_weekly_total_2020_1[-2]
extra_rows_of_weekly_2D_2020_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_weekly_2D_2020_1
kz_bv_hypo_weekly_2D_2020_1_daily = np.vstack((kz_bv_hypo_only_full_weekly_2D_2020_1, extra_rows_of_weekly_2D_2020_1))  

 
#2021_1:    
kz_bv_hypo_only_full_weekly_2D_2021_1=np.repeat(kz_bv_hypo_weekly_2D_2021_1[ :-1, :], 7, axis=0)
# Get the last row of kz_bv_hypo_weekly_2D_2021_1
last_row = kz_bv_hypo_weekly_2D_2021_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2021_1[-1]#+duration_weekly_total_2021_1[-2]
extra_rows_of_weekly_2D_2021_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_weekly_2D_2021_1
kz_bv_hypo_weekly_2D_2021_1_daily = np.vstack((kz_bv_hypo_only_full_weekly_2D_2021_1, extra_rows_of_weekly_2D_2021_1))    

 
#2022_1:    
kz_bv_hypo_only_full_weekly_2D_2022_1=np.repeat(kz_bv_hypo_weekly_2D_2022_1[ :-1, :], 7, axis=0)
# Get the last row of kz_bv_hypo_weekly_2D_2022_1
last_row = kz_bv_hypo_weekly_2D_2022_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_weekly_total_2022_1[-1]#+duration_weekly_total_2022_1[-2]
extra_rows_of_weekly_2D_2022_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_weekly_2D_2022_1
kz_bv_hypo_weekly_2D_2022_1_daily = np.vstack((kz_bv_hypo_only_full_weekly_2D_2022_1, extra_rows_of_weekly_2D_2022_1))    

#%% doing the stratistical analyses after allocating each day values of kz_bv from weekly estimated values 
#2019_2022 weekly 

kz_bv_weekly_indailytimestep_2D_2019_2022=np.concatenate((kz_bv_hypo_weekly_2D_2019_1_daily, kz_bv_hypo_weekly_2D_2019_2_daily,
                                           kz_bv_hypo_weekly_2D_2020_1_daily,kz_bv_hypo_weekly_2D_2021_1_daily,
                                           kz_bv_hypo_weekly_2D_2022_1_daily))


kz_bv_hypo_weekly_2D_2019_1_daily

kz_bv_hypo_weekly_2D_2019_2_daily

kz_bv_hypo_weekly_2D_2020_1_daily

kz_bv_hypo_weekly_2D_2021_1_daily

kz_bv_hypo_weekly_2D_2022_1_daily



array_statistics(kz_bv_weekly_indailytimestep_2D_2019_2022)    
{'Minimum': 6.881412467674149e-06,
 'Maximum': 4.8498149571717705e-05,
 'Mean': 2.3762483843523217e-05,
 'Median': 2.2551120280954943e-05,
 'Standard Deviation': 7.23035307034051e-06}


ratio of Kz_gotm to kz_jp_weekly_indailytimestep_2D_2019_2022: 
2.3762483843523217e-05/8.125150143660237e-06    #2.9245593525510705
 

#%% Changing bv fortnightly to the size of daily timestep 

 
#2019_1:    
kz_bv_hypo_only_full_fortnightly_2D_2019_1=np.repeat(kz_bv_hypo_fortnightly_2D_2019_1[ :-1, :], 14, axis=0)
# Get the last row of kz_bv_hypo_fortnightly_2D_2019_1
last_row = kz_bv_hypo_fortnightly_2D_2019_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2019_1[-1]#+ duration_fortnightly_total_2019_1[-2]
extra_rows_of_fortnightly_2D_2019_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_fortnightly_2D_2019_1
kz_bv_hypo_fortnightly_2D_2019_1_daily = np.vstack((kz_bv_hypo_only_full_fortnightly_2D_2019_1, extra_rows_of_fortnightly_2D_2019_1))    
    

#2019_2    
kz_bv_hypo_only_full_fortnightly_2D_2019_2=np.repeat(kz_bv_hypo_fortnightly_2D_2019_2[ :-1, :], 14, axis=0)
# Get the last row of kz_bv_hypo_fortnightly_2D_2019_2
last_row = kz_bv_hypo_fortnightly_2D_2019_2[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2019_2[-1]#+duration_fortnightly_total_2019_2[-2]
extra_rows_of_fortnightly_2D_2019_2 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_fortnightly_2D_2019_2
kz_bv_hypo_fortnightly_2D_2019_2_daily = np.vstack((kz_bv_hypo_only_full_fortnightly_2D_2019_2, extra_rows_of_fortnightly_2D_2019_2))    
    
 
    
#2020_1:    
kz_bv_hypo_only_full_fortnightly_2D_2020_1=np.repeat(kz_bv_hypo_fortnightly_2D_2020_1[ :-1, :], 14, axis=0)
# Get the last row of kz_bv_hypo_fortnightly_2D_2020_1
last_row = kz_bv_hypo_fortnightly_2D_2020_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2020_1[-1]#+duration_fortnightly_total_2020_1[-2]
extra_rows_of_fortnightly_2D_2020_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_fortnightly_2D_2020_1
kz_bv_hypo_fortnightly_2D_2020_1_daily = np.vstack((kz_bv_hypo_only_full_fortnightly_2D_2020_1, extra_rows_of_fortnightly_2D_2020_1))  

 
#2021_1:    
kz_bv_hypo_only_full_fortnightly_2D_2021_1=np.repeat(kz_bv_hypo_fortnightly_2D_2021_1[ :-1, :], 14, axis=0)
# Get the last row of kz_bv_hypo_fortnightly_2D_2021_1
last_row = kz_bv_hypo_fortnightly_2D_2021_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2021_1[-1]#+duration_fortnightly_total_2021_1[-2]
extra_rows_of_fortnightly_2D_2021_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_fortnightly_2D_2021_1
kz_bv_hypo_fortnightly_2D_2021_1_daily = np.vstack((kz_bv_hypo_only_full_fortnightly_2D_2021_1, extra_rows_of_fortnightly_2D_2021_1))    

 
#2022_1:    
kz_bv_hypo_only_full_fortnightly_2D_2022_1=np.repeat(kz_bv_hypo_fortnightly_2D_2022_1[ :-1, :], 14, axis=0)
# Get the last row of kz_bv_hypo_fortnightly_2D_2022_1
last_row = kz_bv_hypo_fortnightly_2D_2022_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_fortnightly_total_2022_1[-1]#+duration_fortnightly_total_2022_1[-2]
extra_rows_of_fortnightly_2D_2022_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_fortnightly_2D_2022_1
kz_bv_hypo_fortnightly_2D_2022_1_daily = np.vstack((kz_bv_hypo_only_full_fortnightly_2D_2022_1, extra_rows_of_fortnightly_2D_2022_1))    

#%% doing the stratistical analyses after allocating each day values of kz_bv from fortnightly estimated values 
#2019_2022 fortnightly 

kz_bv_fortnightly_indailytimestep_2D_2019_2022=np.concatenate((kz_bv_hypo_fortnightly_2D_2019_1_daily, kz_bv_hypo_fortnightly_2D_2019_2_daily,
                                           kz_bv_hypo_fortnightly_2D_2020_1_daily,kz_bv_hypo_fortnightly_2D_2021_1_daily,
                                           kz_bv_hypo_fortnightly_2D_2022_1_daily))


kz_bv_hypo_fortnightly_2D_2019_1_daily

kz_bv_hypo_fortnightly_2D_2019_2_daily

kz_bv_hypo_fortnightly_2D_2020_1_daily

kz_bv_hypo_fortnightly_2D_2021_1_daily

kz_bv_hypo_fortnightly_2D_2022_1_daily



array_statistics(kz_bv_fortnightly_indailytimestep_2D_2019_2022)    

"""
{'Minimum': 1.0200708153488151e-05,
 'Maximum': 4.408071207088372e-05,
 'Mean': 2.347507590562005e-05,
 'Median': 2.237108819487262e-05,
 'Standard Deviation': 7.065294521797009e-06}
"""
 
#%% Changing bv monthly to the size of daily timestep 

 
#2019_1:    
kz_bv_hypo_only_full_monthly_2D_2019_1=np.repeat(kz_bv_hypo_monthly_2D_2019_1[ :-1, :], 30, axis=0)
# Get the last row of kz_bv_hypo_monthly_2D_2019_1
last_row = kz_bv_hypo_monthly_2D_2019_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2019_1[-1]#+ duration_monthly_total_2019_1[-2]
extra_rows_of_monthly_2D_2019_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_monthly_2D_2019_1
kz_bv_hypo_monthly_2D_2019_1_daily = np.vstack((kz_bv_hypo_only_full_monthly_2D_2019_1, extra_rows_of_monthly_2D_2019_1))    
    

#2019_2    
kz_bv_hypo_only_full_monthly_2D_2019_2=np.repeat(kz_bv_hypo_monthly_2D_2019_2[ :-1, :], 30, axis=0)
# Get the last row of kz_bv_hypo_monthly_2D_2019_2
last_row = kz_bv_hypo_monthly_2D_2019_2[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2019_2[-1]#+duration_monthly_total_2019_2[-2]
extra_rows_of_monthly_2D_2019_2 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_monthly_2D_2019_2
kz_bv_hypo_monthly_2D_2019_2_daily = np.vstack((kz_bv_hypo_only_full_monthly_2D_2019_2, extra_rows_of_monthly_2D_2019_2))    
    
 
    
#2020_1:    
kz_bv_hypo_only_full_monthly_2D_2020_1=np.repeat(kz_bv_hypo_monthly_2D_2020_1[ :-1, :], 30, axis=0)
# Get the last row of kz_bv_hypo_monthly_2D_2020_1
last_row = kz_bv_hypo_monthly_2D_2020_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2020_1[-1]#+duration_monthly_total_2020_1[-2]
extra_rows_of_monthly_2D_2020_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_monthly_2D_2020_1
kz_bv_hypo_monthly_2D_2020_1_daily = np.vstack((kz_bv_hypo_only_full_monthly_2D_2020_1, extra_rows_of_monthly_2D_2020_1))  

 
#2021_1:    
kz_bv_hypo_only_full_monthly_2D_2021_1=np.repeat(kz_bv_hypo_monthly_2D_2021_1[ :-1, :], 30, axis=0)
# Get the last row of kz_bv_hypo_monthly_2D_2021_1
last_row = kz_bv_hypo_monthly_2D_2021_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2021_1[-1]#+duration_monthly_total_2021_1[-2]
extra_rows_of_monthly_2D_2021_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_monthly_2D_2021_1
kz_bv_hypo_monthly_2D_2021_1_daily = np.vstack((kz_bv_hypo_only_full_monthly_2D_2021_1, extra_rows_of_monthly_2D_2021_1))    

 
#2022_1:    
kz_bv_hypo_only_full_monthly_2D_2022_1=np.repeat(kz_bv_hypo_monthly_2D_2022_1[ :-1, :], 30, axis=0)
# Get the last row of kz_bv_hypo_monthly_2D_2022_1
last_row = kz_bv_hypo_monthly_2D_2022_1[-1]
# Repeat the last row to reach the desired size
size_of_repeat= duration_monthly_total_2022_1[-1]#+duration_monthly_total_2022_1[-2]
extra_rows_of_monthly_2D_2022_1 = np.tile(last_row,(int(size_of_repeat) , 1))  # Repeat the last row
# Stack the extra rows on top of kz_bv_hypo_only_full_monthly_2D_2022_1
kz_bv_hypo_monthly_2D_2022_1_daily = np.vstack((kz_bv_hypo_only_full_monthly_2D_2022_1, extra_rows_of_monthly_2D_2022_1))    

#%% doing the stratistical analyses after allocating each day values of kz_bv from monthly estimated values 
#2019_2022 monthly 

kz_bv_monthly_indailytimestep_2D_2019_2022=np.concatenate((kz_bv_hypo_monthly_2D_2019_1_daily, kz_bv_hypo_monthly_2D_2019_2_daily,
                                           kz_bv_hypo_monthly_2D_2020_1_daily,kz_bv_hypo_monthly_2D_2021_1_daily,
                                           kz_bv_hypo_monthly_2D_2022_1_daily))


kz_bv_hypo_monthly_2D_2019_1_daily

kz_bv_hypo_monthly_2D_2019_2_daily

kz_bv_hypo_monthly_2D_2020_1_daily

kz_bv_hypo_monthly_2D_2021_1_daily

kz_bv_hypo_monthly_2D_2022_1_daily



array_statistics(kz_bv_monthly_indailytimestep_2D_2019_2022)    

"""
{'Minimum': 1.1523050679083947e-05,
 'Maximum': 3.804793662768807e-05,
 'Mean': 2.2717133239885043e-05,
 'Median': 2.177214901845072e-05,
 'Standard Deviation': 5.790560301637319e-06}
"""    
#%% timestep and deltat:
    
"""
#2018_1
time_steps_2018_1 = df_str_2018_1_14.index.unique()

deltat_2018_1 = np.append(0, np.diff(df_str_2018_1_14.index.unique()) / np.timedelta64(1, 'D'))# perfect :1
"""        


#2019_1
#df_str_2019_1_14=df_str_nomixing_2019_1_14.set_index ('Datetime')

time_steps_2019_1 = df_str_nomixing_2019_1_14.index.unique()

deltat_2019_1 = np.append(0, np.diff(df_str_nomixing_2019_1_14.index.unique()) / np.timedelta64(1, 'D'))# perfect :1
        
 
#2019_2
#df_str_2019_2_14=df_str_nomixing_2019_2_14.set_index ('Datetime')

time_steps_2019_2 = df_str_nomixing_2019_2_14.index.unique()

deltat_2019_2 = np.append(0, np.diff(df_str_nomixing_2019_2_14.index.unique()) / np.timedelta64(1, 'D'))# perfect :1
         
    
  
#2020_1
#df_str_2020_1_14=df_str_nomixing_2020_1_14.set_index ('Datetime')

time_steps_2020_1 = df_str_nomixing_2020_1_14.index.unique()

deltat_2020_1 = np.append(0, np.diff(df_str_nomixing_2020_1_14.index.unique()) / np.timedelta64(1, 'D'))# perfect :1


#2021_1
#df_str_2021_1_14=df_str_nomixing_2021_1_14.set_index ('Datetime')

time_steps_2021_1 = df_str_nomixing_2021_1_14.index.unique()

deltat_2021_1 = np.append(0, np.diff(df_str_nomixing_2021_1_14.index.unique()) / np.timedelta64(1, 'D'))# perfect :1
    
#2022_1
#df_str_2022_1_14=df_str_nomixing_2022_1_14.set_index ('Datetime')

time_steps_2022_1 = df_str_nomixing_2022_1_14.index.unique()

deltat_2022_1 = np.append(0, np.diff(df_str_nomixing_2022_1_14.index.unique()) / np.timedelta64(1, 'D'))# perfect :1
 
#%%depth_levels
# -13.5 has been definded for adding boundry condition
depth_levels = np.arange(-13.5, -17.5, -0.5) 



#%%Essentail requirements of bathymetry for hypolimnion:

V_r = df_str_nomixing_2020_1_14[(df_str_nomixing_2020_1_14.index == min(
    df_str_nomixing_2020_1_14.index)) & (df_str_nomixing_2020_1_14['Z_m'] < -13.5)]['V_r_m']
A_l = df_str_nomixing_2020_1_14[(df_str_nomixing_2020_1_14.index == min(
    df_str_nomixing_2020_1_14.index)) & (df_str_nomixing_2020_1_14['Z_m'] < -13.5)]['A_l_m']
A_s = df_str_nomixing_2020_1_14[(df_str_nomixing_2020_1_14.index == min(
    df_str_nomixing_2020_1_14.index)) & (df_str_nomixing_2020_1_14['Z_m'] < -13.5)]['As_up_bndr_m']
dz = 0.5
# movegahati
#dz = (df_str_2years_14[(df_str_2years_14.index == min(
#    df_str_2019_2_14.index)) & (df_str_2years_14['Z_m'] < -13.5)]['dZ_m_down'])



A_s=np.array(A_s)
V_r=np.array(V_r)
dz=np.array(dz)
A_l=np.array(A_l)
nl=np.shape(A_s)[0]

hypo_morphology_vriables_obs_grid= [V_r, A_s, A_l, dz, nl ]


#%%esseional inputs for using the comprehensive function of DO simulation for 
# calibration and validation 


params= [0.1 , 0.1 , 1]
dens_diff_top_135_2019_2022
hypo_morphology_vriables_obs_grid


daily_prof_Temp_DO_morpho_2019_2022= daily_prof_Temp_DO_morpho_5years[daily_prof_Temp_DO_morpho_5years.index.year!=2018]
    
temp_2D_2019_2022_fullprof=two_D_array_from_df(daily_prof_Temp_DO_morpho_2019_2022, 'Temp')
    
temp_2D_2019_2022_hypoprof=two_D_array_from_df(daily_prof_Temp_DO_morpho_2019_2022[daily_prof_Temp_DO_morpho_2019_2022['Z_m']<-13.5] , 'Temp')
#(838, 7)
#
daily_hypo_prof_Temp_DO_morpho_2019_2022=daily_prof_Temp_DO_morpho_2019_2022[daily_prof_Temp_DO_morpho_2019_2022['Z_m+']>13.5]


#%%placing the kz in dataframes of str_hypo
"""
df_hypo_str_2019_1_14=df_str_2019_1_14[df_str_2019_1_14['Z_m+']>13.5]
df_hypo_str_2019_2_14=df_str_2019_2_14[df_str_2019_2_14['Z_m+']>13.5]
df_hypo_str_2020_1_14=df_str_2020_1_14[df_str_2020_1_14['Z_m+']>13.5]
df_hypo_str_2021_1_14=df_str_2021_1_14[df_str_2021_1_14['Z_m+']>13.5]
df_hypo_str_2022_1_14=df_str_2022_1_14[df_str_2022_1_14['Z_m+']>13.5]
"""


#placing the kz in dataframes of str_nomixing 

df_hypo_str_nomixing_2019_1_14=df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m+']>13.5]
df_hypo_str_nomixing_2019_2_14=df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m+']>13.5]
df_hypo_str_nomixing_2020_1_14=df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m+']>13.5]
df_hypo_str_nomixing_2021_1_14=df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m+']>13.5]
df_hypo_str_nomixing_2022_1_14=df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m+']>13.5]



# adding daily [JP] :

df_hypo_str_nomixing_2019_1_14['kz_jp_daily']= np.append(  kz_jp_hypo_daily_2D_2019_1[0 ,:], np.ravel(kz_jp_hypo_daily_2D_2019_1) )# np.flatten()
df_hypo_str_nomixing_2019_2_14['kz_jp_daily']= np.append(  kz_jp_hypo_daily_2D_2019_2[0 ,:],  np.ravel(kz_jp_hypo_daily_2D_2019_2)  )# np.flatten()
df_hypo_str_nomixing_2020_1_14['kz_jp_daily']= np.append(  kz_jp_hypo_daily_2D_2020_1[0 ,:], np.ravel(kz_jp_hypo_daily_2D_2020_1) )# np.flatten()
df_hypo_str_nomixing_2021_1_14['kz_jp_daily']= np.append(  kz_jp_hypo_daily_2D_2021_1[0 ,:]  , np.ravel(kz_jp_hypo_daily_2D_2021_1) )# np.flatten()
df_hypo_str_nomixing_2022_1_14['kz_jp_daily']=  np.append(  kz_jp_hypo_daily_2D_2022_1[0 ,:]  , np.ravel(kz_jp_hypo_daily_2D_2022_1) )# np.flatten()




# adding weekly to data frame [JP] 
df_hypo_str_nomixing_2019_1_14['kz_jp_weekly']= np.ravel(kz_jp_hypo_weekly_2D_2019_1_daily)# np.flatten()
df_hypo_str_nomixing_2019_2_14['kz_jp_weekly']= np.ravel(kz_jp_hypo_weekly_2D_2019_2_daily) # np.flatten()
df_hypo_str_nomixing_2020_1_14['kz_jp_weekly']= np.ravel(kz_jp_hypo_weekly_2D_2020_1_daily)# np.flatten()
df_hypo_str_nomixing_2021_1_14['kz_jp_weekly']= np.ravel(kz_jp_hypo_weekly_2D_2021_1_daily)# np.flatten()
df_hypo_str_nomixing_2022_1_14['kz_jp_weekly']= np.ravel(kz_jp_hypo_weekly_2D_2022_1_daily) # np.flatten()



#adding the kz_fortnightly [JP]

df_hypo_str_nomixing_2019_1_14['kz_jp_fortnightly']= np.ravel(kz_jp_hypo_fortnightly_2D_2019_1_daily) # np.flatten()
df_hypo_str_nomixing_2019_2_14['kz_jp_fortnightly']= np.ravel(kz_jp_hypo_fortnightly_2D_2019_2_daily) # np.flatten()
df_hypo_str_nomixing_2020_1_14['kz_jp_fortnightly']= np.ravel(kz_jp_hypo_fortnightly_2D_2020_1_daily) # np.flatten()
df_hypo_str_nomixing_2021_1_14['kz_jp_fortnightly']= np.ravel(kz_jp_hypo_fortnightly_2D_2021_1_daily) # np.flatten()
df_hypo_str_nomixing_2022_1_14['kz_jp_fortnightly']= np.ravel(kz_jp_hypo_fortnightly_2D_2022_1_daily)# np.flatten()



#adding the kz_monthly [JP]

df_hypo_str_nomixing_2019_1_14['kz_jp_monthly']= np.ravel(kz_jp_hypo_monthly_2D_2019_1_daily)# np.flatten()
df_hypo_str_nomixing_2019_2_14['kz_jp_monthly']= np.ravel(kz_jp_hypo_monthly_2D_2019_2_daily) # np.flatten()
df_hypo_str_nomixing_2020_1_14['kz_jp_monthly']= np.ravel(kz_jp_hypo_monthly_2D_2020_1_daily) # np.flatten()
df_hypo_str_nomixing_2021_1_14['kz_jp_monthly']= np.ravel(kz_jp_hypo_monthly_2D_2021_1_daily) # np.flatten()
df_hypo_str_nomixing_2022_1_14['kz_jp_monthly']= np.ravel(kz_jp_hypo_monthly_2D_2022_1_daily) # np.flatten()





# adding daily bv daily:
    
df_hypo_str_nomixing_2019_1_14['kz_bv_daily']= np.ravel(kz_bv_hypo_daily_2D_2019_1)
df_hypo_str_nomixing_2019_2_14['kz_bv_daily']= np.ravel(kz_bv_hypo_daily_2D_2019_2)
df_hypo_str_nomixing_2020_1_14['kz_bv_daily']= np.ravel(kz_bv_hypo_daily_2D_2020_1)
df_hypo_str_nomixing_2021_1_14['kz_bv_daily']= np.ravel(kz_bv_hypo_daily_2D_2021_1)
df_hypo_str_nomixing_2022_1_14['kz_bv_daily']= np.ravel(kz_bv_hypo_daily_2D_2022_1)





# adding weekly to data frame [bv] 
df_hypo_str_nomixing_2019_1_14['kz_bv_weekly']= np.ravel(kz_bv_hypo_weekly_2D_2019_1_daily)# np.flatten()
df_hypo_str_nomixing_2019_2_14['kz_bv_weekly']= np.ravel(kz_bv_hypo_weekly_2D_2019_2_daily) # np.flatten()
df_hypo_str_nomixing_2020_1_14['kz_bv_weekly']= np.ravel(kz_bv_hypo_weekly_2D_2020_1_daily)# np.flatten()
df_hypo_str_nomixing_2021_1_14['kz_bv_weekly']= np.ravel(kz_bv_hypo_weekly_2D_2021_1_daily)# np.flatten()
df_hypo_str_nomixing_2022_1_14['kz_bv_weekly']= np.ravel(kz_bv_hypo_weekly_2D_2022_1_daily) # np.flatten()



#adding the kz_fortnightly [bv]

df_hypo_str_nomixing_2019_1_14['kz_bv_fortnightly']= np.ravel(kz_bv_hypo_fortnightly_2D_2019_1_daily) # np.flatten()
df_hypo_str_nomixing_2019_2_14['kz_bv_fortnightly']= np.ravel(kz_bv_hypo_fortnightly_2D_2019_2_daily) # np.flatten()
df_hypo_str_nomixing_2020_1_14['kz_bv_fortnightly']= np.ravel(kz_bv_hypo_fortnightly_2D_2020_1_daily) # np.flatten()
df_hypo_str_nomixing_2021_1_14['kz_bv_fortnightly']= np.ravel(kz_bv_hypo_fortnightly_2D_2021_1_daily) # np.flatten()
df_hypo_str_nomixing_2022_1_14['kz_bv_fortnightly']= np.ravel(kz_bv_hypo_fortnightly_2D_2022_1_daily)# np.flatten()



#adding the kz_monthly [bv]

df_hypo_str_nomixing_2019_1_14['kz_bv_monthly']= np.ravel(kz_bv_hypo_monthly_2D_2019_1_daily)# np.flatten()
df_hypo_str_nomixing_2019_2_14['kz_bv_monthly']= np.ravel(kz_bv_hypo_monthly_2D_2019_2_daily) # np.flatten()
df_hypo_str_nomixing_2020_1_14['kz_bv_monthly']= np.ravel(kz_bv_hypo_monthly_2D_2020_1_daily) # np.flatten()
df_hypo_str_nomixing_2021_1_14['kz_bv_monthly']= np.ravel(kz_bv_hypo_monthly_2D_2021_1_daily) # np.flatten()
df_hypo_str_nomixing_2022_1_14['kz_bv_monthly']= np.ravel(kz_bv_hypo_monthly_2D_2022_1_daily) # np.flatten()




#pd.concat 2019-2022:
    
df_hypo_str_nomixing_2019_2022 = pd.concat([df_hypo_str_nomixing_2019_1_14 ,df_hypo_str_nomixing_2019_2_14, df_hypo_str_nomixing_2020_1_14, df_hypo_str_nomixing_2021_1_14 , df_hypo_str_nomixing_2022_1_14])

df_hypo_str_nomixing_2019_2022


######


array_statistics(df_hypo_str_nomixing_2019_2022['kz_jp_daily'])
{'Minimum': 1.3999999999999998e-07,
 'Maximum': 0.0008022413040939742,
 'Mean': 1.342960512475161e-05,
 'Median': 4.243938976559392e-06,
 'Standard Deviation': 3.564835181896268e-05}

array_statistics(df_hypo_str_nomixing_2019_2022['kz_jp_weekly'])

{'Minimum': 1.3999999999999998e-07,
 'Maximum': 0.00011788004741596368,
 'Mean': 8.490433345840648e-06,
 'Median': 4.848760232439378e-06,
 'Standard Deviation': 1.3530763302043626e-05}

array_statistics(df_hypo_str_nomixing_2019_2022['kz_jp_fortnightly'])
{'Minimum': 1.3999999999999998e-07,
 'Maximum': 6.388749719463389e-05,
 'Mean': 8.01857055466666e-06,
 'Median': 5.428489549272845e-06,
 'Standard Deviation': 1.0610202372886578e-05}


array_statistics(df_hypo_str_nomixing_2019_2022['kz_jp_monthly'])
{'Minimum': 4.33249044186465e-07,
 'Maximum': 1.4736562288328243e-05,
 'Mean': 6.310533149151138e-06,
 'Median': 5.115136073736642e-06,
 'Standard Deviation': 3.5760236182215043e-06}




array_statistics(df_hypo_str_nomixing_2019_2022['kz_bv_daily'])
{'Minimum': 6.148294383271784e-06,
 'Maximum': 8.197670147965065e-05,
 'Mean': 2.487784819771466e-05,
 'Median': 2.3434438298948343e-05,
 'Standard Deviation': 9.04169540302978e-06}



array_statistics(df_hypo_str_nomixing_2019_2022['kz_bv_weekly'])
{'Minimum': 6.881412467674149e-06,
 'Maximum': 4.8498149571717705e-05,
 'Mean': 2.3762483843523153e-05,
 'Median': 2.2551120280954943e-05,
 'Standard Deviation': 7.230353070340474e-06}


array_statistics(df_hypo_str_nomixing_2019_2022['kz_bv_fortnightly'])
{'Minimum': 1.0200708153488151e-05,
 'Maximum': 4.408071207088372e-05,
 'Mean': 2.3475075905620085e-05,
 'Median': 2.237108819487262e-05,
 'Standard Deviation': 7.065294521796977e-06}

array_statistics(df_hypo_str_nomixing_2019_2022['kz_bv_monthly'])
{'Minimum': 1.1523050679083947e-05,
 'Maximum': 3.804793662768807e-05,
 'Mean': 2.2717133239885125e-05,
 'Median': 2.177214901845072e-05,
 'Standard Deviation': 5.790560301637321e-06}

#%%
"""
###### in 14m : mean and median of kz bv
df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_fortnightly'].mean()
Out[927]: 1.994101501934587e-05

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_fortnightly'].median()
Out[928]: 1.9753505887323303e-05

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_monthly'].median()
Out[929]: 1.944984825941897e-05

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_monthly'].mean()
Out[930]: 1.9371642952928367e-05

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_weekly'].mean()
Out[931]: 2.0138174606577416e-05

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_weekly'].median()
Out[932]: 2.0091869887746702e-05

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_daily'].median()
Out[933]: 2.0687894950055338e-05

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_bv_daily'].mean()
Out[934]: 2.13291534492191e-05


#=============mean and median of kz JP
df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_fortnightly'].mean()
Out[927]: 7.714418334122528e-06

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_fortnightly'].median()
Out[928]: 5.1896413109621045e-06

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_monthly'].median()
Out[929]: 4.741352519356788e-06

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_monthly'].mean()
Out[930]:6.230675015413336e-06

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_weekly'].mean()
Out[931]: 8.384010270459521e-06

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_weekly'].median()
Out[932]: 4.098422626400289e-06

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_daily'].median()
Out[933]: 3.4822333151284235e-06

df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022['Z_m+']==14]['kz_jp_daily'].mean()
Out[934]: 1.5819006992457068e-05
"""

#%%Plotting different calculation of eddy diffusivity  

"""    
df_hypo_str_nomixing_2019_2022 = pd.concat([df_hypo_str_nomixing_2019_1_14 ,df_hypo_str_nomixing_2019_2_14, df_hypo_str_nomixing_2020_1_14, df_hypo_str_nomixing_2021_1_14 , df_hypo_str_nomixing_2022_1_14])

df_hypo_str_nomixing_2019_2022




#['kz_jp_daily']
#['kz_jp_weekly']
#['kz_jp_fortnightly']
#['kz_jp_monthly']



#['kz_bv_daily']
#['kz_bv_weekly']
#['kz_bv_fortnightly']
#['kz_bv_monthly']


import matplotlib.colors as colors


#function needed: 
kz_hypo_deox_daily   =two_D_array_from_df( df_hypo_str_nomixing_2019_2022 , 
                                          values_name='kz_jp_daily',index_name='Datetime')

#datetime: 
datetime_nomixing_2019_2022=df_hypo_str_nomixing_2019_2022.index.unique()
 

# Assuming you have a 2D array with shape (n, m), and Z_hypo_TB_Erk and formatted_time_series as described
n, m = kz_hypo_deox_daily.shape
Z_hypo = np.array([-14, -14.5, -15, -15.5, -16, -16.5, -17])


# Create a meshgrid for the contour plot
X, Y = np.meshgrid(datetime_nomixing_2019_2022, Z_hypo)


data = kz_hypo_deox_daily

# Calculate the logarithmic levels
min_val = data.min()
max_val = data.max()
num_levels = 10  # Adjust this as needed

# Create the contour plot with logarithmic levels
plt.figure(figsize=(15, 10))
#contour = plt.contourf(X, Y, data, levels=np.linspace(min_val, max_val, num_levels), cmap='rainbow')
contour = plt.contourf(X, Y, data, levels=np.logspace(np.log10(min_val), np.log10(max_val), num_levels), cmap='rainbow', norm=colors.LogNorm())



# Add labels and title
plt.ylabel('Depth [m]')
plt.title('Kz daily JP profile during deoxygen period_2022')

# Add a colorbar
colorbar = plt.colorbar(contour, format='%.0e')  # Use scientific notation format
colorbar.set_label('Kz [m2 s-1]') 

plt.xticks(rotation=45)
#plt.savefig('kz_jp_daily_profile_during_deoxygen_period_2019_2022.png' , dpi=300)
"""


#%%putting the kz in 2D arry for simulation of DO 
 

df_bas= daily_hypo_prof_Temp_DO_morpho_2019_2022.reset_index().copy()
df_sub= df_hypo_str_nomixing_2019_2022.reset_index().copy()



merged_df= df_bas.merge(df_sub[['Datetime', 'Z_m+', 'kz_jp_daily', 'kz_jp_weekly', 'kz_jp_fortnightly' ,'kz_jp_monthly' ,  'kz_bv_daily' ,'kz_bv_weekly', 'kz_bv_fortnightly' ,'kz_bv_monthly' ]], left_on=['Datetime', 'Z_m+'], right_on=['Datetime', 'Z_m+'], how='left')


#########

#saving the merged_df 
merged_df.to_csv('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/claculated_kz_for_2019_2022_in DO df/merged_df.csv', index=False)

############
# Fill NaN values with 1 in 'kz_weekly' and 'kz_fortnightly'# ba harch por konam mored nadare badan hazf misheeee

merged_df['kz_jp_daily'].fillna(0, inplace=True)
merged_df['kz_jp_weekly'].fillna(0, inplace=True)
merged_df['kz_jp_fortnightly'].fillna(0, inplace=True)
merged_df['kz_jp_monthly'].fillna(0, inplace=True)

merged_df['kz_bv_daily'].fillna(0, inplace=True)
merged_df['kz_bv_weekly'].fillna(0, inplace=True)
merged_df['kz_bv_fortnightly'].fillna(0, inplace=True)
merged_df['kz_bv_monthly'].fillna(0, inplace=True)

#================kz JP  in 2-D array
kz_jp_daily_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_jp_daily',index_name='Datetime') 

kz_jp_weekly_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_jp_weekly',index_name='Datetime')    # (838, 7)


kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_jp_fortnightly',index_name='Datetime')   # (838, 7)


kz_jp_monthly_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_jp_monthly',index_name='Datetime') 

#=================kz BV  in 2-D array
kz_bv_daily_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_bv_daily',index_name='Datetime') 

kz_bv_weekly_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_bv_weekly',index_name='Datetime')    # (838, 7)


kz_bv_fortnightly_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_bv_fortnightly',index_name='Datetime')   # (838, 7)


kz_bv_monthly_hypo_2D_insize_obs_2019_2022 =two_D_array_from_df(
    merged_df, values_name='kz_bv_monthly',index_name='Datetime') 

#%% try for just one combination of Ja and Jv 
"""
DO_prof_2D_model_obstime , temp_str_prof_2D_obstime ,kz_str_prof_2D_obstime , day_with_full_sat =do_model_comprehensive([0.38, 0.09 , 1], dens_diff_top_135_2019_2022 ,temp_surf_1m_2019_2022, hypo_morphology_vriables_obs_grid 
                           ,temp_2D_2019_2022_hypoprof , kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022, replanishmnet_rate= 2.7946 )#kz_weekly_hypo_2D_insize_obs_2019_2022 
"""

#%%Hypolimnetic average

def hypolimnetic_ave(C, Vr, time_series):
    C_ave=np.dot (C , Vr) / sum (Vr)
    C_ave_indexed=pd.Series(C_ave, index=pd.to_datetime(time_series))
    return (C_ave_indexed) 




#%%calibration for RMSE of hypolimnetic average
    
"""    
# model daily average in hypolimnion     
time_series= daily_hypo_prof_Temp_DO_morpho_2019_2022.index.unique()    
Vr= V_r.copy()    
    
DO_hypo_ave_model_2019_2022=hypolimnetic_ave(DO_prof_2D_model_obstime, Vr, time_series).dropna()
    


# obs_ave_hypo:
# df_hypo_str_2019_2022['DO']    

df_str_nomixing_2019_2022=pd.concat([df_str_nomixing_2019_1_14 , df_str_nomixing_2019_2_14 , df_str_nomixing_2020_1_14 , df_str_nomixing_2021_1_14 , df_str_nomixing_2022_1_14 ])

df_hypo_str_nomixing_2019_2022=df_str_nomixing_2019_2022[df_str_nomixing_2019_2022['Z_m+']> 13.5]

DO_obs_str_hypo_2D_2019_2022=two_D_array_from_df(
    df_hypo_str_nomixing_2019_2022, values_name='DO',index_name='Datetime')    

DO_hypo_ave_obs_2019_2022=hypolimnetic_ave(DO_obs_str_hypo_2D_2019_2022, Vr, df_str_nomixing_2019_2022.index.unique() )      
"""

#%%
DO_obs_str_hypo_2D_2019_2022=two_D_array_from_df(
df_hypo_str_nomixing_2019_2022, values_name='DO',index_name='Datetime') #2D_obs   

#%%calibration 2020-2021
from sklearn.metrics import mean_squared_error
import math
#pip install hydroeval
from hydroeval import evaluator, nse



#dens_diff_top_135_2019_2022
#hypo_morphology_vriables_obs_grid


def calibration_2020_2021 (params ):
    jv, ja , scale_subdaily=params
    
    time_series= daily_hypo_prof_Temp_DO_morpho_2019_2022.index.unique()    
    Vr= V_r.copy()    
    
    DO_prof_2D_model_obstime_2019_2022  =do_model_comprehensive(params, dens_diff_top_135_2019_2022, temp_surf_1m_2019_2022 , hypo_morphology_vriables_obs_grid 
                           ,temp_2D_2019_2022_hypoprof , kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022 , replanishmnet_rate= 2.7946 )[0]
    ##np.ones(kz_jp_daily_hypo_2D_insize_obs_2019_2022.shape)*8*10**-5 
    
    #kz_jp_daily_hypo_2D_insize_obs_2019_2022  
    #kz_jp_weekly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_monthly_hypo_2D_insize_obs_2019_2022 
    
    
    #kz_bv_daily_hypo_2D_insize_obs_2019_2022 
    #kz_bv_weekly_hypo_2D_insize_obs_2019_2022 
    ############kz_bv_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_bv_monthly_hypo_2D_insize_obs_2019_2022 
    
    #model_2D
    df_DO_2D_model_2019_2022=pd.DataFrame(DO_prof_2D_model_obstime_2019_2022).set_index(time_series)
    df_DO_2D_model_2020_2021= df_DO_2D_model_2019_2022[(df_DO_2D_model_2019_2022.index.year == 2020)|(df_DO_2D_model_2019_2022.index.year == 2021)].dropna()
    
    DO_model_2D_2020_2021=np.array(df_DO_2D_model_2020_2021)#2D_model 
    
    #obs_2D:
    df_str_nomixing_2020_2021=pd.concat([df_str_nomixing_2020_1_14 , df_str_nomixing_2021_1_14  ])
    df_hypo_str_nomixing_2020_2021=df_str_nomixing_2020_2021[df_str_nomixing_2020_2021['Z_m+']> 13.5]
    
    
    DO_obs_str_hypo_2D_2020_2021=two_D_array_from_df(
    df_hypo_str_nomixing_2020_2021, values_name='DO',index_name='Datetime') #2D_obs   
    
    
    
    
    #condition_2020_or_2021 = (time_series.year == 2020) | (time_series.year == 2021)
    #indices_2020_or_2021 = time_series.get_indexer(time_series[condition_2020_or_2021])
    
    
    #model_ave
    DO_hypo_ave_model_2019_2022=hypolimnetic_ave(DO_prof_2D_model_obstime_2019_2022, Vr, time_series).dropna()
    DO_ave_model_2020_2021=DO_hypo_ave_model_2019_2022[(DO_hypo_ave_model_2019_2022.index.year == 2020)|(DO_hypo_ave_model_2019_2022.index.year == 2021)]#ave_model
                                
    #obs_ave
    DO_hypo_ave_obs_2019_2022=hypolimnetic_ave(DO_obs_str_hypo_2D_2019_2022, Vr, df_str_nomixing_2019_2022.index.unique() )      
    DO_hypo_ave_obs_2020_2021=DO_hypo_ave_obs_2019_2022[(DO_hypo_ave_obs_2019_2022.index.year == 2020)|(DO_hypo_ave_obs_2019_2022.index.year == 2021)]#ave_obs
     
    
    MSE_prof = mean_squared_error(DO_model_2D_2020_2021 , DO_obs_str_hypo_2D_2020_2021)
    
    NSE_prof = evaluator(nse, DO_model_2D_2020_2021.flatten(), DO_obs_str_hypo_2D_2020_2021.flatten())

    # For each corresponding pair of predicted and observed DO profiles, calculate the squared difference.
    #Sum up all these squared differences.
    #Divide the sum by the total number of data points (which is the number of profiles in this case) to get the average squared difference, i.e., the mean squared error.
    RMSE_prof=math.sqrt(MSE_prof)
    
    MSE_prof_0 = mean_squared_error(DO_model_2D_2020_2021[: , 0] , DO_obs_str_hypo_2D_2020_2021[: , 0])
    RMSE_prof_0=math.sqrt(MSE_prof_0)
    
    MSE_prof_1 = mean_squared_error(DO_model_2D_2020_2021[: , 1] , DO_obs_str_hypo_2D_2020_2021[: , 1])
    RMSE_prof_1=math.sqrt(MSE_prof_1)
    
    MSE_prof_2 = mean_squared_error(DO_model_2D_2020_2021[: , 2] , DO_obs_str_hypo_2D_2020_2021[: , 2])
    RMSE_prof_2=math.sqrt(MSE_prof_2)

    NSE_prof_2=evaluator(nse, DO_model_2D_2020_2021[: , 2], DO_obs_str_hypo_2D_2020_2021[: , 2])



    MSE_prof_3 = mean_squared_error(DO_model_2D_2020_2021[: , 3] , DO_obs_str_hypo_2D_2020_2021[: , 3])
    RMSE_prof_3=math.sqrt(MSE_prof_3)
        
    
    MSE_prof_4 = mean_squared_error(DO_model_2D_2020_2021[: , 4] , DO_obs_str_hypo_2D_2020_2021[: , 4])
    RMSE_prof_4=math.sqrt(MSE_prof_4)

    MSE_prof_5 = mean_squared_error(DO_model_2D_2020_2021[: , 5] , DO_obs_str_hypo_2D_2020_2021[: , 5])
    RMSE_prof_5=math.sqrt(MSE_prof_5)
    
    MSE_prof_6 = mean_squared_error(DO_model_2D_2020_2021[: , 6] , DO_obs_str_hypo_2D_2020_2021[: , 6])
    RMSE_prof_6=math.sqrt(MSE_prof_6)
        
    
    
    MSE_ave = mean_squared_error(DO_ave_model_2020_2021, DO_hypo_ave_obs_2020_2021)
    RMSE_ave=math.sqrt(MSE_ave)
    
    NSE_ave = evaluator(nse, DO_ave_model_2020_2021, DO_hypo_ave_obs_2020_2021)


    return (RMSE_ave , RMSE_prof , RMSE_prof_0, RMSE_prof_1 , 
            RMSE_prof_2 , RMSE_prof_3 , RMSE_prof_4 , RMSE_prof_5,
            RMSE_prof_6, NSE_ave, NSE_prof, NSE_prof_2 )   





#%%validation 2022
from sklearn.metrics import mean_squared_error
import math
#dens_diff_top_135_2019_2022
#hypo_morphology_vriables_obs_grid


def validation_2022 (params ):
    jv, ja , scale_subdaily=params
    
    time_series= daily_hypo_prof_Temp_DO_morpho_2019_2022.index.unique()    
    Vr= V_r.copy()    
    
    DO_prof_2D_model_obstime_2019_2022  =do_model_comprehensive(params, dens_diff_top_135_2019_2022, temp_surf_1m_2019_2022 , hypo_morphology_vriables_obs_grid 
                           ,temp_2D_2019_2022_hypoprof , kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022, replanishmnet_rate= 2.7946 )[0]#kz_weekly_hypo_2D_insize_obs_2019_2022 
    
    
    ##np.ones(kz_jp_daily_hypo_2D_insize_obs_2019_2022.shape)*8*10**-5 
    
    #kz_jp_daily_hypo_2D_insize_obs_2019_2022  
    #kz_jp_weekly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_monthly_hypo_2D_insize_obs_2019_2022 
    
    
    #kz_bv_daily_hypo_2D_insize_obs_2019_2022 
    #kz_bv_weekly_hypo_2D_insize_obs_2019_2022 
    #kz_bv_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_bv_monthly_hypo_2D_insize_obs_2019_2022 
    
    
    

    #model_2D
    df_DO_2D_model_2019_2022=pd.DataFrame(DO_prof_2D_model_obstime_2019_2022).set_index(time_series)
    df_DO_2D_model_2022= df_DO_2D_model_2019_2022[(df_DO_2D_model_2019_2022.index.year == 2022)].dropna()
    
    DO_model_2D_2022=np.array(df_DO_2D_model_2022)#2D_model 
    
    #obs_2D:
    df_str_nomixing_2022= df_str_nomixing_2022_1_14
    df_hypo_str_nomixing_2022=df_str_nomixing_2022[df_str_nomixing_2022['Z_m+']> 13.5]
    
    
    DO_obs_str_hypo_2D_2022=two_D_array_from_df(
    df_hypo_str_nomixing_2022, values_name='DO',index_name='Datetime') #2D_obs   
    
    
    
    
    #condition_2020_or_2021 = (time_series.year == 2020) | (time_series.year == 2021)
    #indices_2020_or_2021 = time_series.get_indexer(time_series[condition_2020_or_2021])
    
    
    #model_ave
    DO_hypo_ave_model_2019_2022=hypolimnetic_ave(DO_prof_2D_model_obstime_2019_2022, Vr, time_series).dropna()
    DO_ave_model_2022=DO_hypo_ave_model_2019_2022[DO_hypo_ave_model_2019_2022.index.year == 2022]#ave_model
                                
    #obs_ave
    DO_hypo_ave_obs_2019_2022=hypolimnetic_ave(DO_obs_str_hypo_2D_2019_2022, Vr, df_str_nomixing_2019_2022.index.unique() )      
    DO_hypo_ave_obs_2022=DO_hypo_ave_obs_2019_2022[DO_hypo_ave_obs_2019_2022.index.year == 2022]#ave_obs
     
    
    MSE_prof = mean_squared_error(DO_model_2D_2022 , DO_obs_str_hypo_2D_2022)
    # For each corresponding pair of predicted and observed DO profiles, calculate the squared difference.
    #Sum up all these squared differences.
    #Divide the sum by the total number of data points (which is the number of profiles in this case) to get the average squared difference, i.e., the mean squared error.
    RMSE_prof=math.sqrt(MSE_prof)
    NSE_prof= evaluator(nse, DO_model_2D_2022.flatten(), DO_obs_str_hypo_2D_2022.flatten())

    MSE_prof_0 = mean_squared_error(DO_model_2D_2022[: , 0] , DO_obs_str_hypo_2D_2022[: , 0])
    RMSE_prof_0=math.sqrt(MSE_prof_0)
    
    MSE_prof_1 = mean_squared_error(DO_model_2D_2022[: , 1] , DO_obs_str_hypo_2D_2022[: , 1])
    RMSE_prof_1=math.sqrt(MSE_prof_1)
    
    MSE_prof_2 = mean_squared_error(DO_model_2D_2022[: , 2] , DO_obs_str_hypo_2D_2022[: , 2])
    RMSE_prof_2=math.sqrt(MSE_prof_2)

    NSE_prof_2= evaluator(nse, DO_model_2D_2022[: , 2], DO_obs_str_hypo_2D_2022[: , 2])



    MSE_prof_3 = mean_squared_error(DO_model_2D_2022[: , 3] , DO_obs_str_hypo_2D_2022[: , 3])
    RMSE_prof_3=math.sqrt(MSE_prof_3)
        
    
    MSE_prof_4 = mean_squared_error(DO_model_2D_2022[: , 4] , DO_obs_str_hypo_2D_2022[: , 4])
    RMSE_prof_4=math.sqrt(MSE_prof_4)

    MSE_prof_5 = mean_squared_error(DO_model_2D_2022[: , 5] , DO_obs_str_hypo_2D_2022[: , 5])
    RMSE_prof_5=math.sqrt(MSE_prof_5)
    
    MSE_prof_6 = mean_squared_error(DO_model_2D_2022[: , 6] , DO_obs_str_hypo_2D_2022[: , 6])
    RMSE_prof_6=math.sqrt(MSE_prof_6)
        
    
    
    MSE_ave = mean_squared_error(DO_ave_model_2022, DO_hypo_ave_obs_2022)
    RMSE_ave=math.sqrt(MSE_ave)
    
    NSE_ave= evaluator(nse, DO_ave_model_2022, DO_hypo_ave_obs_2022)


    return (RMSE_ave , RMSE_prof , RMSE_prof_0, RMSE_prof_1 , 
            RMSE_prof_2 , RMSE_prof_3 , RMSE_prof_4 , RMSE_prof_5,
            RMSE_prof_6 , NSE_ave, NSE_prof, NSE_prof_2 )   




#%%validation_2019
#params=[0.1, 1, 1]
def validation_2019 (params ):
    jv, ja , scale_subdaily=params
    
    time_series= daily_hypo_prof_Temp_DO_morpho_2019_2022.index.unique()    
    Vr= V_r.copy()    
    
    DO_prof_2D_model_obstime_2019_2022  =do_model_comprehensive(params, dens_diff_top_135_2019_2022 ,temp_surf_1m_2019_2022, hypo_morphology_vriables_obs_grid 
                           ,temp_2D_2019_2022_hypoprof , kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022, replanishmnet_rate= 2.7946 )[0]#kz_weekly_hypo_2D_insize_obs_2019_2022 
    
    
    
    ##np.ones(kz_jp_daily_hypo_2D_insize_obs_2019_2022.shape)*8*10**-5 
    
    #kz_jp_daily_hypo_2D_insize_obs_2019_2022  
    #kz_jp_weekly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_monthly_hypo_2D_insize_obs_2019_2022 
    
    
    #kz_bv_daily_hypo_2D_insize_obs_2019_2022 
    #kz_bv_weekly_hypo_2D_insize_obs_2019_2022 
    #kz_bv_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_bv_monthly_hypo_2D_insize_obs_2019_2022 
    
    
    

    
    #model_2D
    df_DO_2D_model_2019_2022=pd.DataFrame(DO_prof_2D_model_obstime_2019_2022).set_index(time_series)
    df_DO_2D_model_2019= df_DO_2D_model_2019_2022[df_DO_2D_model_2019_2022.index.year == 2019].dropna()
    
    DO_model_2D_2019=np.array(df_DO_2D_model_2019)#2D_model 
    
    #obs_2D:
    df_str_nomixing_2019=pd.concat([df_str_nomixing_2019_1_14 , df_str_nomixing_2019_2_14  ])
    df_hypo_str_nomixing_2019=df_str_nomixing_2019[df_str_nomixing_2019['Z_m+']> 13.5]
    
    
    DO_obs_str_hypo_2D_2019=two_D_array_from_df(
    df_hypo_str_nomixing_2019, values_name='DO',index_name='Datetime') #2D_obs   
    
    
    
    
    #condition_2020_or_2021 = (time_series.year == 2020) | (time_series.year == 2021)
    #indices_2020_or_2021 = time_series.get_indexer(time_series[condition_2020_or_2021])
    
    
    #model_ave
    DO_hypo_ave_model_2019_2022=hypolimnetic_ave(DO_prof_2D_model_obstime_2019_2022, Vr, time_series).dropna()
    DO_ave_model_2019=DO_hypo_ave_model_2019_2022[DO_hypo_ave_model_2019_2022.index.year == 2019]#ave_model
                                
    #obs_ave
    DO_hypo_ave_obs_2019_2022=hypolimnetic_ave(DO_obs_str_hypo_2D_2019_2022, Vr, df_str_nomixing_2019_2022.index.unique() )      
    DO_hypo_ave_obs_2019=DO_hypo_ave_obs_2019_2022[DO_hypo_ave_obs_2019_2022.index.year == 2019]#ave_obs
     
    
    MSE_prof = mean_squared_error(DO_model_2D_2019 , DO_obs_str_hypo_2D_2019)
    # For each corresponding pair of predicted and observed DO profiles, calculate the squared difference.
    #Sum up all these squared differences.
    #Divide the sum by the total number of data points (which is the number of profiles in this case) to get the average squared difference, i.e., the mean squared error.
    RMSE_prof=math.sqrt(MSE_prof)
    NSE_prof= evaluator(nse, DO_model_2D_2019.flatten(), DO_obs_str_hypo_2D_2019.flatten())

    
    MSE_prof_0 = mean_squared_error(DO_model_2D_2019[: , 0] , DO_obs_str_hypo_2D_2019[: , 0])
    RMSE_prof_0=math.sqrt(MSE_prof_0)
    
    MSE_prof_1 = mean_squared_error(DO_model_2D_2019[: , 1] , DO_obs_str_hypo_2D_2019[: , 1])
    RMSE_prof_1=math.sqrt(MSE_prof_1)
    
    MSE_prof_2 = mean_squared_error(DO_model_2D_2019[: , 2] , DO_obs_str_hypo_2D_2019[: , 2])
    RMSE_prof_2=math.sqrt(MSE_prof_2)
    NSE_prof_2 = evaluator(nse, DO_model_2D_2019[: , 2], DO_obs_str_hypo_2D_2019[: , 2])


    MSE_prof_3 = mean_squared_error(DO_model_2D_2019[: , 3] , DO_obs_str_hypo_2D_2019[: , 3])
    RMSE_prof_3=math.sqrt(MSE_prof_3)
        
    
    MSE_prof_4 = mean_squared_error(DO_model_2D_2019[: , 4] , DO_obs_str_hypo_2D_2019[: , 4])
    RMSE_prof_4=math.sqrt(MSE_prof_4)

    MSE_prof_5 = mean_squared_error(DO_model_2D_2019[: , 5] , DO_obs_str_hypo_2D_2019[: , 5])
    RMSE_prof_5=math.sqrt(MSE_prof_5)
    
    MSE_prof_6 = mean_squared_error(DO_model_2D_2019[: , 6] , DO_obs_str_hypo_2D_2019[: , 6])
    RMSE_prof_6=math.sqrt(MSE_prof_6)
        
    
    
    MSE_ave = mean_squared_error(DO_ave_model_2019, DO_hypo_ave_obs_2019)
    RMSE_ave=math.sqrt(MSE_ave)
    NSE_ave = evaluator(nse, DO_ave_model_2019, DO_hypo_ave_obs_2019)
    
    return (RMSE_ave , RMSE_prof , RMSE_prof_0, RMSE_prof_1 , 
            RMSE_prof_2 , RMSE_prof_3 , RMSE_prof_4 , RMSE_prof_5,
            RMSE_prof_6, NSE_ave, NSE_prof, NSE_prof_2 )  

#%%all years calibration calibration_2019_2022

def calibration_2019_2022 (params ):
    jv, ja , scale_subdaily=params
    
    time_series= daily_hypo_prof_Temp_DO_morpho_2019_2022.index.unique()    
    Vr= V_r.copy()    
    
    DO_prof_2D_model_obstime_2019_2022  =do_model_comprehensive(params, dens_diff_top_135_2019_2022 ,temp_surf_1m_2019_2022, hypo_morphology_vriables_obs_grid 
                           ,temp_2D_2019_2022_hypoprof , kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022 , replanishmnet_rate= 2.7946 )[0]
    ##np.ones(kz_jp_daily_hypo_2D_insize_obs_2019_2022.shape)*8*10**-5 
    
    #kz_jp_daily_hypo_2D_insize_obs_2019_2022  
    #kz_jp_weekly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_jp_monthly_hypo_2D_insize_obs_2019_2022 
    
    
    #kz_bv_daily_hypo_2D_insize_obs_2019_2022 
    #kz_bv_weekly_hypo_2D_insize_obs_2019_2022 
    #kz_bv_fortnightly_hypo_2D_insize_obs_2019_2022 
    #kz_bv_monthly_hypo_2D_insize_obs_2019_2022 
    
    #model_2D
    df_DO_2D_model_2019_2022=pd.DataFrame(DO_prof_2D_model_obstime_2019_2022).set_index(time_series).dropna()
    

    DO_model_2D_2019_2022=np.array(df_DO_2D_model_2019_2022)#2D_model 
    
    #obs_2D:
    df_str_nomixing_2019_2022=pd.concat([df_str_nomixing_2019_1_14 , df_str_nomixing_2019_2_14, df_str_nomixing_2020_1_14 , df_str_nomixing_2021_1_14 , df_str_nomixing_2022_1_14 ])
    df_hypo_str_nomixing_2019_2022=df_str_nomixing_2019_2022[df_str_nomixing_2019_2022['Z_m+']> 13.5]
    
    
    DO_obs_str_hypo_2D_2019_2022=two_D_array_from_df(
    df_hypo_str_nomixing_2019_2022, values_name='DO',index_name='Datetime') #2D_obs   
    
    
    
    
    #condition_2020_or_2021 = (time_series.year == 2020) | (time_series.year == 2021)
    #indices_2020_or_2021 = time_series.get_indexer(time_series[condition_2020_or_2021])
    
    
    #model_ave
    DO_hypo_ave_model_2019_2022=hypolimnetic_ave(DO_prof_2D_model_obstime_2019_2022, Vr, time_series).dropna()
    DO_ave_model_2019_2022=DO_hypo_ave_model_2019_2022#ave_model
                                
    #obs_ave
    DO_hypo_ave_obs_2019_2022=hypolimnetic_ave(DO_obs_str_hypo_2D_2019_2022, Vr, df_str_nomixing_2019_2022.index.unique() ) .dropna()     
    DO_hypo_ave_obs_2019_2022=DO_hypo_ave_obs_2019_2022#ave_obs
     
    
    MSE_prof = mean_squared_error(DO_model_2D_2019_2022 , DO_obs_str_hypo_2D_2019_2022)
    # For each corresponding pair of predicted and observed DO profiles, calculate the squared difference.
    #Sum up all these squared differences.
    #Divide the sum by the total number of data points (which is the number of profiles in this case) to get the average squared difference, i.e., the mean squared error.
    RMSE_prof=math.sqrt(MSE_prof)
    
    NSE_prof = evaluator(nse,DO_model_2D_2019_2022.flatten() , DO_obs_str_hypo_2D_2019_2022.flatten())

    
    MSE_prof_0 = mean_squared_error(DO_model_2D_2019_2022[: , 0] , DO_obs_str_hypo_2D_2019_2022[: , 0])
    RMSE_prof_0=math.sqrt(MSE_prof_0)
    
    MSE_prof_1 = mean_squared_error(DO_model_2D_2019_2022[: , 1] , DO_obs_str_hypo_2D_2019_2022[: , 1])
    RMSE_prof_1=math.sqrt(MSE_prof_1)
    
    MSE_prof_2 = mean_squared_error(DO_model_2D_2019_2022[: , 2] , DO_obs_str_hypo_2D_2019_2022[: , 2])
    RMSE_prof_2=math.sqrt(MSE_prof_2)

    NSE_prof_2 = evaluator(nse,DO_model_2D_2019_2022[: , 2] , DO_obs_str_hypo_2D_2019_2022[: , 2])


    MSE_prof_3 = mean_squared_error(DO_model_2D_2019_2022[: , 3] , DO_obs_str_hypo_2D_2019_2022[: , 3])
    RMSE_prof_3=math.sqrt(MSE_prof_3)
        
    
    MSE_prof_4 = mean_squared_error(DO_model_2D_2019_2022[: , 4] , DO_obs_str_hypo_2D_2019_2022[: , 4])
    RMSE_prof_4=math.sqrt(MSE_prof_4)

    MSE_prof_5 = mean_squared_error(DO_model_2D_2019_2022[: , 5] , DO_obs_str_hypo_2D_2019_2022[: , 5])
    RMSE_prof_5=math.sqrt(MSE_prof_5)
    
    MSE_prof_6 = mean_squared_error(DO_model_2D_2019_2022[: , 6] , DO_obs_str_hypo_2D_2019_2022[: , 6])
    RMSE_prof_6=math.sqrt(MSE_prof_6)
        
    
    
    MSE_ave = mean_squared_error(DO_ave_model_2019_2022, DO_hypo_ave_obs_2019_2022)
    RMSE_ave=math.sqrt(MSE_ave)
    
    NSE_ave = evaluator(nse,DO_ave_model_2019_2022, DO_hypo_ave_obs_2019_2022)

    return (RMSE_ave , RMSE_prof , RMSE_prof_0, RMSE_prof_1 , 
            RMSE_prof_2 , RMSE_prof_3 , RMSE_prof_4 , RMSE_prof_5,
            RMSE_prof_6, NSE_ave, NSE_prof, NSE_prof_2 )  


#%% calculation of different combination of Ja and Jv:
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
   
#   calibartion function : calibration_2020_2021
#   validation functions  :  validation_2022, validation_2019

import numpy as np
import matplotlib.pyplot as plt

# Assuming you have already defined the function calibration_implicit_2019_2020()

# Define the parameter ranges and number of points
param1_name = 'J$_{V}$ [g m$^{-3}$ d$^{-1}$]'
param2_name = 'J$_{A}$ [g m$^{-2}$ d$^{-1}$]'

"""
num_points1 =10#84 #with 0.01 interval 
num_points2 =20#169 #with 0.01 interval

jv_min, jv_max = 0.001, 0.85#with no_kz: 0.47#0, 0.85#0.467 maxium all #0.222 meso trophic # minimum all 0.01
ja_min, ja_max = 0.001, 1.7 #with no kz:  0.45#0, 1.7 #1.7 maximum in meso # 2.7maxium all(two eutrophic)# minimum all 0.1

# Create arrays of parameter values spanning the ranges from min_val to max_val for both parameters
param1_values = np.linspace(jv_min, jv_max, num_points1)
param2_values = np.linspace(ja_min, ja_max, num_points2)
"""

jv_min, jv_max = 0.001, 0.84#with no_kz: 0.47#0, 0.84#0.467 maxium all #0.222 meso trophic in VHOD lipa # minimum all 0.01
ja_min, ja_max = 0.001, 1.7 #with no kz:  0.45#0, 1.7 #1.7 maximum in meso # 2.7maxium all(two eutrophic)# minimum all 0.1

num_points1 =len(np.arange(jv_min, jv_max+0.1 , 0.1))
num_points2 =len(np.arange(ja_min , ja_max+0.1 , 0.1))

param1_values = np.arange(jv_min, jv_max+0.1 , 0.1)
param2_values = np.arange(ja_min , ja_max+0.1 , 0.1)


# Calculate the output of the model at each parameter combination
#RMSE
rmse_calib_ave = np.zeros((num_points1, num_points2))
rmse_calib_prof = np.zeros((num_points1, num_points2))

rmse_valid_2022_ave= np.zeros((num_points1, num_points2))
rmse_valid_2022_prof= np.zeros((num_points1, num_points2))

rmse_valid_2019_ave= np.zeros((num_points1, num_points2))
rmse_valid_2019_prof= np.zeros((num_points1, num_points2))

#NSE

nse_calib_ave = np.zeros((num_points1, num_points2))
nse_calib_prof = np.zeros((num_points1, num_points2))

nse_valid_2022_ave= np.zeros((num_points1, num_points2))
nse_valid_2022_prof= np.zeros((num_points1, num_points2))

nse_valid_2019_ave= np.zeros((num_points1, num_points2))
nse_valid_2019_prof= np.zeros((num_points1, num_points2))

data_calib_2020_2021 = {'Jv': [], 'Ja': [],
                        'rmse_ave_calib': [], 'nse_ave_calib': [], 
                        'rmse_prof_calib': [] ,'nse_prof_calib': [], 
                        'rmse_ave_valid_2022':[] , 'nse_ave_valid_2022':[] ,
                        'rmse_prof_valid_2022':[] , 'nse_prof_valid_2022':[] ,
                        'rmse_ave_valid_2019':[], 'nse_ave_valid_2019':[],
                        'rmse_prof_valid_2019':[], 'nse_prof_valid_2019':[]}#, 'rmse_ave_cal_all':[], 'rmse_prof_cal_all':[]}

for i, p1 in enumerate(param1_values):
    for j, p2 in enumerate(param2_values):
        rmse_calib_ave[i, j] = calibration_2020_2021([p1, p2, 1])[0]##validation_2022 , validation_2019
        rmse_calib_prof[i, j]  = calibration_2020_2021([p1, p2, 1])[1]
          
        nse_calib_ave[i, j]  =calibration_2020_2021([p1, p2, 1])[9]
        nse_calib_prof[i, j]  = calibration_2020_2021([p1, p2, 1])[10]
        
        # Append the values to the data lists
        data_calib_2020_2021['Jv'].append(p1)
        data_calib_2020_2021['Ja'].append(p2)
        
        data_calib_2020_2021['rmse_ave_calib'].append(rmse_calib_ave[i, j] )
        data_calib_2020_2021['rmse_prof_calib'].append(rmse_calib_prof[i, j] )
        
        data_calib_2020_2021['nse_ave_calib'].append(nse_calib_ave[i, j] )
        data_calib_2020_2021['nse_prof_calib'].append(nse_calib_prof[i, j] )
        
        
        
        rmse_valid_2022_ave[i, j] = validation_2022([p1, p2, 1])[0]
        rmse_valid_2022_prof[i, j] = validation_2022([p1, p2, 1])[1]
        
        nse_valid_2022_ave[i, j] = validation_2022([p1, p2, 1])[9]
        nse_valid_2022_prof[i, j] = validation_2022([p1, p2, 1])[10]
        
        
        data_calib_2020_2021['rmse_ave_valid_2022'].append(rmse_valid_2022_ave[i, j] )
        data_calib_2020_2021['rmse_prof_valid_2022'].append(rmse_valid_2022_prof[i, j] )
        
        data_calib_2020_2021['nse_ave_valid_2022'].append(nse_valid_2022_ave[i, j] )
        data_calib_2020_2021['nse_prof_valid_2022'].append(nse_valid_2022_prof[i, j] )
        
        
        rmse_valid_2019_ave[i, j] = validation_2019([p1, p2, 1])[0]
        rmse_valid_2019_prof[i, j] = validation_2019([p1, p2, 1])[1]

        nse_valid_2019_ave[i, j] = validation_2019([p1, p2, 1])[9]
        nse_valid_2019_prof[i, j] = validation_2019([p1, p2, 1])[10]

        
        data_calib_2020_2021['rmse_ave_valid_2019'].append(rmse_valid_2019_ave[i, j] )
        data_calib_2020_2021['rmse_prof_valid_2019'].append(rmse_valid_2019_prof[i, j] )        
        
        data_calib_2020_2021['nse_ave_valid_2019'].append(nse_valid_2019_ave[i, j] )
        data_calib_2020_2021['nse_prof_valid_2019'].append(nse_valid_2019_prof[i, j] )        
        
 
        
# Create a DataFrame from the data
df_calib_2020_2021 = pd.DataFrame(data_calib_2020_2021)

df_calib_2020_2021['VHOD']= df_calib_2020_2021['Jv']+0.4851*df_calib_2020_2021['Ja']
df_calib_2020_2021['AHOD']= df_calib_2020_2021['Ja']+df_calib_2020_2021['Jv']/0.4851


#df_calib_2020_2021.to_csv('df_calib_and_valid_results_interval1e_1.csv', index=False)


# Create meshgrid for param1_values and param2_values
param2_mesh, param1_mesh = np.meshgrid(param2_values, param1_values)  # Swapped order for meshgrid



#%% Find the minimum value and its corresponding parameter values
#rmse_ave
min_index_ave = np.unravel_index(np.argmin(rmse_calib_ave), rmse_calib_ave.shape)
min_jv_ave, min_ja_ave = param1_mesh[min_index_ave], param2_mesh[min_index_ave]
min_value_ave = rmse_calib_ave[min_index_ave]
#rmse_prof
min_index_prof = np.unravel_index(np.argmin(rmse_calib_prof), rmse_calib_prof.shape)
min_jv_prof, min_ja_prof = param1_mesh[min_index_prof], param2_mesh[min_index_prof]
min_value_prof = rmse_calib_prof[min_index_prof]


#%%rmse_calib_ave_2020_2021
#Create a filled contour plot with a color map_Calibration plot of hypolimnetic average RMSE 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, rmse_calib_ave,  levels=np.arange(0, 10, 1), cmap='RdYlGn_r')
plt.colorbar(contourf_plot, label='Deep-water DO average RMSE [mg L$^{-1}$]', format='%.0f')# 1f
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, rmse_calib_ave, levels=np.arange(0, 10, 1), colors='black')# np.arange(0, 8.9 , 0.8)
plt.clabel(contour_lines, inline=True, fontsize=20, fmt='%.0f')

# Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_ave, min_ja_ave, 'ro', label=f'Minimum Value: {min_value_ave:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_ave[0]]:.3f}\nMinimum Ja: {param2_values[min_index_ave[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel('J$_{V}$ [g m$^{-3}$ d$^{-1}$]', fontsize=22)
plt.ylabel('J$_{A}$ [g m$^{-2}$ d$^{-1}$]', fontsize=22)


# Set x and y tick intervals
plt.xticks(np.arange(0.1, 0.85, 0.1))
plt.yticks(np.arange(0.2, 1.7, 0.2))

# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

#plt.savefig("calibration_rmse_hypo_ave_2020_2021_without_kz_180combination_1e_1interval_JAJV_variabletheta.png", dpi=300)


# Save the plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("calibration_rmse_hypo_ave_2020_2021_kz_jp_fortnightly_180combination_1e_1interval_JAJV_mediankzhyposurfbnd_variabletheta.png", dpi=300)

#plt.savefig("calibration_rmse_hypo_ave_2020_2021_kz_jp_fortnightly_180combination_1e_1interval_JAJV_mediankzhyposurfbnd_fixedtheta_on_onset_temp.png", dpi=300)


#plt.savefig("calibration_rmse_hypo_ave_2020_2021_kz_jp_fortnightly_180combination_1e_1interval_JAJV_mediankzhyposurfbnd_fixedtheta_on_aveonsettodeephypoxia_temp_notaveragetemp.png", dpi=300)

#plt.savefig("calibration_rmse_hypo_ave_2020_2021_kz_jp_fortnightly_180combination_1e_1interval_JAJV_mediankzhyposurfbnd_fixedtheta_on_temp_onset_to_deephypoxia.png", dpi=300)



#%%color scatter plot 
"""
plt.scatter(param1_mesh, param2_mesh, c=rmse_calib_ave, cmap='viridis')  # 'viridis' is just an example colormap
plt.colorbar()
"""
#%%rmse_calib_prof_2020_2021

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt


# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, rmse_calib_prof, levels=np.arange(0, 10, 1), cmap='RdYlGn_r')
plt.colorbar(contourf_plot, label='Deep-water DO profile RMSE [mg L$^{-1}$]', format='%.0f')# 
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, rmse_calib_prof, levels=np.arange(0, 10, 1), colors='black')
plt.clabel(contour_lines, inline=True, fontsize=20, fmt='%.0f')

#Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_prof, min_ja_prof, 'ro', label=f'Minimum Value: {min_value_prof:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_prof[0]]:.3f}\nMinimum Ja: {param2_values[min_index_prof[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel('J$_{V}$ [g m$^{-3}$ d$^{-1}$]', fontsize=22)
plt.ylabel('J$_{A}$ [g m$^{-2}$ d$^{-1}$]', fontsize=22)




# Set x and y tick intervals
plt.xticks(np.arange(0.1, 0.85, 0.1))
plt.yticks(np.arange(0.2, 1.7, 0.2))

# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

# Save the plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("calibration_rmse_hypo_prof_2020_2021_kz_jp_fortnightly_180combination_1e_1interval_JAJV.png", dpi=300)
plt.show()


#%%nse_calib_prof_2020_2021

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt


# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, nse_calib_prof, levels=np.arange(-4, 1.1, 0.1), cmap='RdYlGn')
plt.colorbar(contourf_plot, label='Deep-water DO profile NSE []', format='%.1f')# 
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, nse_calib_prof, levels=np.arange(-4, 1.1, 0.1), colors='black')
plt.clabel(contour_lines, inline=True, fontsize=20, fmt='%.1f')

#Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_prof, min_ja_prof, 'ro', label=f'Minimum Value: {min_value_prof:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_prof[0]]:.3f}\nMinimum Ja: {param2_values[min_index_prof[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel('J$_{V}$ [g m$^{-3}$ d$^{-1}$]', fontsize=22)
plt.ylabel('J$_{A}$ [g m$^{-2}$ d$^{-1}$]', fontsize=22)




# Set x and y tick intervals
plt.xticks(np.arange(0.1, 0.85, 0.1))
plt.yticks(np.arange(0.2, 1.7, 0.2))

# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

# Save the plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("calibration_nse_hypo_prof_2020_2021_kz_jp_fortnightly_180combination_1e_1interval_JAJV.png", dpi=300)
plt.show()



#%%Subplots of calibartion in RMSE and NSE for paper:
    
    
import os
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

# Create a figure and axes for the subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))  # 1 row, 2 columns

# Set the working directory
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')

# Plot 1: RMSE
contourf_plot1 = axes[0].contourf(param1_mesh, param2_mesh, rmse_calib_prof, levels=np.arange(0, 10, 1), cmap='RdYlGn_r')
colorbar1 = plt.colorbar(contourf_plot1, ax=axes[0], label='Deep-water DO profile RMSE [mg L$^{-1}$]', format='%.0f')
contour_lines1 = axes[0].contour(param1_mesh, param2_mesh, rmse_calib_prof, levels=np.arange(0, 10, 1), colors='black')
axes[0].clabel(contour_lines1, inline=True, fontsize=20, fmt='%.0f')
axes[0].set_xlabel('J$_{V}$ [g m$^{-3}$ d$^{-1}$]')
axes[0].set_ylabel('J$_{A}$ [g m$^{-2}$ d$^{-1}$]')
axes[0].set_xticks(np.arange(0.1, 0.85, 0.1))
axes[0].set_yticks(np.arange(0.2, 1.7, 0.2))

# Plot 2: NSE
contourf_plot2 = axes[1].contourf(param1_mesh, param2_mesh, nse_calib_prof, levels=np.arange(-4, 1.1, 0.1), cmap='RdYlGn')
colorbar2 = plt.colorbar(contourf_plot2, ax=axes[1], label='Deep-water DO profile NSE []', format='%.1f')
contour_lines2 = axes[1].contour(param1_mesh, param2_mesh, nse_calib_prof, levels=np.arange(-4, 1.1, 0.1), colors='black')
axes[1].clabel(contour_lines2, inline=True, fontsize=20, fmt='%.1f')
axes[1].set_xlabel('J$_{V}$ [g m$^{-3}$ d$^{-1}$]')
axes[1].set_ylabel('J$_{A}$ [g m$^{-2}$ d$^{-1}$]')
axes[1].set_xticks(np.arange(0.1, 0.85, 0.1))
axes[1].set_yticks(np.arange(0.2, 1.7, 0.2))

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("calibration_rmse_nse_comparison_2020_2021.png", dpi=300)
plt.show()



#%%rmse_valid_2022_prof
#Create a filled contour plot with a color map_Calibration plot of hypolimnetic average RMSE 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, rmse_valid_2022_prof,  levels=np.arange(0, 10, 1), cmap='RdYlGn_r')
plt.colorbar(contourf_plot, label='Deep-water DO profile RMSE [mg L$^{-1}$]', format='%.0f')# 
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, rmse_valid_2022_prof, levels=np.arange(0, 10, 1), colors='black')
plt.clabel(contour_lines, inline=True, fontsize=20, fmt='%.0f')

# Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_ave, min_ja_ave, 'ro', label=f'Minimum Value: {min_value_ave:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_ave[0]]:.3f}\nMinimum Ja: {param2_values[min_index_ave[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel(param1_name, fontsize=22)
plt.ylabel(param2_name, fontsize=22)


# Set x and y tick intervals
plt.xticks(np.arange(0.1, 0.85, 0.1))
plt.yticks(np.arange(0.2, 1.7, 0.2))


# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

# Save the plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("validation_rmse_hypo_prof_2022_kz_jp_fortnightly_180comb_mediankzhyposurfbnd_fixedtheta_on_onset_temp_notaveragetemp.png", dpi=300)
plt.show()


#%%rmse_valid_2022_ave
#Create a filled contour plot with a color map_Calibration plot of hypolimnetic average RMSE 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, rmse_valid_2022_ave,  levels=np.arange(0, 10, 1), cmap='RdYlGn_r')
plt.colorbar(contourf_plot, label='Deep-water DO average RMSE [mg L$^{-1}$]', format='%.0f')# 
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, rmse_valid_2022_ave, levels=np.arange(0, 10, 1), colors='black')
plt.clabel(contour_lines, inline=True, fontsize=20, fmt='%.0f')

# Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_ave, min_ja_ave, 'ro', label=f'Minimum Value: {min_value_ave:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_ave[0]]:.3f}\nMinimum Ja: {param2_values[min_index_ave[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel(param1_name, fontsize=22)
plt.ylabel(param2_name, fontsize=22)


# Set x and y tick intervals
plt.xticks(np.arange(0.1, 0.85, 0.1))
plt.yticks(np.arange(0.2, 1.7, 0.2))


# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

# Save the plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("validation_rmse_hypo_ave_2022_kz_jp_fortnightly_180comb_mediankzhyposurfbnd_fixedtheta_on_onset_temp.png", dpi=300)
plt.show()


#%%rmse_valid_2019_prof
#Create a filled contour plot with a color map_Calibration plot of hypolimnetic average RMSE 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, rmse_valid_2019_prof,  levels=np.arange(0, 10, 1), cmap='RdYlGn_r')
plt.colorbar(contourf_plot, label='Deep-water DO profile RMSE [mg L$^{-1}$]', format='%.0f')# 
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, rmse_valid_2019_prof, levels=np.arange(0, 10, 1), colors='black')
plt.clabel(contour_lines, inline=True, fontsize=20, fmt='%.0f')

# Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_ave, min_ja_ave, 'ro', label=f'Minimum Value: {min_value_ave:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_ave[0]]:.3f}\nMinimum Ja: {param2_values[min_index_ave[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel(param1_name, fontsize=22)
plt.ylabel(param2_name, fontsize=22)


# Set x and y tick intervals
plt.xticks(np.arange(0.1, 0.85, 0.1))
plt.yticks(np.arange(0.2, 1.7, 0.2))


# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

# Save the plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("validation_rmse_hypo_prof_2019_kz_jp_fortnightly_180comb_mediankzhyposurfbnd_fixedtheta_on_onset_temp.png", dpi=300)
plt.show()


#%%rmse_valid_2019_ave
#Create a filled contour plot with a color map_Calibration plot of hypolimnetic average RMSE 

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, rmse_valid_2019_ave,  levels=np.arange(0, 10, 1), cmap='RdYlGn_r')
plt.colorbar(contourf_plot, label='Deep-water DO average RMSE [mg L$^{-1}$]', format='%.0f')# 
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, rmse_valid_2019_ave, levels=np.arange(0, 10, 1), colors='black')
plt.clabel(contour_lines, inline=True, fontsize=20, fmt='%.0f')

# Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_ave, min_ja_ave, 'ro', label=f'Minimum Value: {min_value_ave:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_ave[0]]:.3f}\nMinimum Ja: {param2_values[min_index_ave[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel(param1_name, fontsize=22)
plt.ylabel(param2_name, fontsize=22)


# Set x and y tick intervals
plt.xticks(np.arange(0.1, 0.85, 0.1))
plt.yticks(np.arange(0.2, 1.7, 0.2))


# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

# Save the plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("validation_rmse_hypo_ave_2019_kz_jp_fortnightly_180comb_mediankzhyposurfbnd_fixedtheta_on_onset_temp.png", dpi=300)
plt.show()





#%%rmse_calib_prof_all
#Create a filled contour plot with a color map_Calibration plot of hypolimnetic average RMSE 
"""
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 18

plt.figure(figsize=(12, 10))

contourf_plot = plt.contourf(param1_mesh, param2_mesh, rmse_cal_all_prof,  levels=np.arange(0, 20, 1), cmap='RdYlGn_r')
plt.colorbar(contourf_plot, label='RMSE hypolemnetic profile [g m$^{-3}$]', format='%.2f')# 
#profile# # hypolemnetic average
# Add contour lines with output values as labels
contour_lines = plt.contour(param1_mesh, param2_mesh, rmse_cal_all_prof, levels=np.arange(0, 20, 1), colors='black')
plt.clabel(contour_lines, inline=True, fontsize=12, fmt='%.3f')

# Plot the minimum value with a red dot and add a legend (moved outside of the plot)
#plt.plot(min_jv_ave, min_ja_ave, 'ro', label=f'Minimum Value: {min_value_ave:.3f}', markersize=20) 
#plt.legend(loc='upper right', bbox_to_anchor=(1.2,-0.03))

# Add the values of JA and Jv at the bottom right of the plot
#plt.text(0.95, 0.05, f'Minimum Jv: {param1_values[min_index_ave[0]]:.3f}\nMinimum Ja: {param2_values[min_index_ave[1]]:.3f}',
#         ha='right', va='bottom', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Set x and y-axis label text formatting and size
plt.xlabel(param1_name, fontsize=18)
plt.ylabel(param2_name, fontsize=18)

# Uncomment the following line if you want to set a title for the plot
# plt.title('Contour Plot with Color Map and Contour Labels', fontsize=20)

# Uncomment the following line if you want to show grid lines in the plot
# plt.grid(True)

# Save the plot with a specified dpi (dots per inch) for higher resolution
#plt.savefig("calibration_rmse_hypo_ave_2020_2021_kz_jp_fortnightly_no_min_indicted.png", dpi=300)
plt.show()
"""

#%%


df_calib_2020_2021['VHOD']= df_calib_2020_2021['Jv']+0.4851*df_calib_2020_2021['Ja']


#df_calib_2020_2021[df_calib_2020_2021['rmse_prof_cal_all']<2]

#df_calib_2020_2021[df_calib_2020_2021['rmse_prof_cal_all']<1.5]

#%%ploting to calibration of 2020-2021 together 
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(26, 10))

# Plot 1 - Calibration Average
contourf_plot_ave = axs[0].contourf(param1_mesh, param2_mesh, rmse_calib_ave,  levels=np.arange(0, 10, 1), cmap='RdYlGn_r')#levels=20, cmap='viridis')
axs[0].set_xlabel(param1_name, fontsize=22)
axs[0].set_ylabel(param2_name, fontsize=22)
axs[0].set_title('Calibration of hypolimnetic average', fontsize=22)
axs[0].set_xticks(np.arange(0.1, 0.85, 0.1))
axs[0].set_yticks(np.arange(0.2, 1.7, 0.2))


# Plot 2 - Calibration Profile
contourf_plot_prof = axs[1].contourf(param1_mesh, param2_mesh, rmse_calib_prof,  levels=np.arange(0, 10, 1), cmap='RdYlGn_r')#levels=20, cmap='viridis')
axs[1].set_xlabel(param1_name, fontsize=22)
axs[1].set_ylabel(param2_name, fontsize=22)
axs[1].set_title('Calibration of profile' , fontsize=22)
axs[1].set_xticks(np.arange(0.1, 0.85, 0.1))
axs[1].set_yticks(np.arange(0.2, 1.7, 0.2))
axs[1].set_xticks(np.arange(0.1, 0.85, 0.1))
axs[1].set_yticks(np.arange(0.2, 1.7, 0.2))

# using only one color basr that works for both:
cbar = fig.colorbar(contourf_plot_prof, ax=axs, ticks=np.arange(0, 10, 1) , label='RMSE [mg L$^{-1}$]', format='%.1f')
#axs[1].set_clabel(cbar, inline=True, fontsize=20, fmt='%.0f')

# Add colorbars
#if I want to have seperate colorabr foer each garph:
#fig.colorbar(contourf_plot_ave, ax=axs[0], label='RMSE hypolimnetic average [g m$^{-3}$]', format='%.2f')
#fig.colorbar(contourf_plot_prof, ax=axs[1], label='RMSE hypolimnion profile [g m$^{-3}$]', format='%.2f')



# Save the combined plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("combined_calibration_subplots_rmse_ave_prof_180combinations_13nov_fortnightly_daily_kzhyposurfbnd_fixedtheta_on_temp_onset_to_deephypoxia.png", dpi=300)
            #fixedtheta_on_onset_temp_notavetemp.png", dpi=300)

# Show the combined plot
plt.show()



#%%Validation_ prof_and ave _2022_2019

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final')
import matplotlib.pyplot as plt

# Set the default font family and size for the plot
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 22

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(26, 20))

# Plot 1 - Validation Average 2019
contourf_plot_ave_2019 = axs[0, 0].contourf(param1_mesh, param2_mesh, rmse_valid_2019_ave,levels=np.arange(0, 10, 1), cmap='RdYlGn_r')#levels=20, cmap='viridis')
axs[0, 0].set_xlabel(param1_name, fontsize=22)
axs[0, 0].set_ylabel(param2_name, fontsize=22)
axs[0, 0].set_title('Validation of hypolimnion average in 2019')
axs[0, 0].set_xticks(np.arange(0.1, 0.85, 0.1))
axs[0, 0].set_yticks(np.arange(0.2, 1.7, 0.2))


# Plot 2 - Validation Profile 2019
contourf_plot_prof_2019 = axs[0, 1].contourf(param1_mesh, param2_mesh, rmse_valid_2019_prof, levels=np.arange(0, 10, 1), cmap='RdYlGn_r')#levels=20, cmap='viridis')
axs[0, 1].set_xlabel(param1_name, fontsize=22)
axs[0, 1].set_ylabel(param2_name, fontsize=22)
axs[0, 1].set_title('Validation of profile in 2019')
axs[0, 1].set_xticks(np.arange(0.1, 0.85, 0.1))
axs[0, 1].set_yticks(np.arange(0.2, 1.7, 0.2))
# Plot 3 - Validation Average 2022
contourf_plot_ave_2022 = axs[1, 0].contourf(param1_mesh, param2_mesh, rmse_valid_2022_ave, levels=np.arange(0, 10,1), cmap='RdYlGn_r')#levels=20, cmap='viridis')
axs[1, 0].set_xlabel(param1_name, fontsize=22)
axs[1, 0].set_ylabel(param2_name, fontsize=22)
axs[1, 0].set_title('Validation of hypolimnion average in 2022')
axs[1, 0].set_xticks(np.arange(0.1, 0.85, 0.1))
axs[1, 0].set_yticks(np.arange(0.2, 1.7, 0.2))



# Plot 4 - Validation Profile 2022
contourf_plot_prof_2022 = axs[1, 1].contourf(param1_mesh, param2_mesh, rmse_valid_2022_prof,levels=np.arange(0, 10, 1), cmap='RdYlGn_r')#levels=20, cmap='viridis')
axs[1, 1].set_xlabel(param1_name, fontsize=22)
axs[1, 1].set_ylabel(param2_name, fontsize=22)
axs[1, 1].set_title('Validation of profile in 2022')
axs[1, 1].set_xticks(np.arange(0.1, 0.85, 0.1))
axs[1, 1].set_yticks(np.arange(0.2, 1.7, 0.2))

# using only one color basr that works for both:
cbar = fig.colorbar(contourf_plot_prof_2022, ax=axs, ticks=np.arange(0, 10, 1) , label='RMSE [mg L$^{-1}$]', format='%.2f')


# Add colorbars
#if I want to have seperate colorabr foer each garph:
#fig.colorbar(contourf_plot_ave_2019, ax=axs[0 , 0], label='RMSE hypolimnetic average [g m$^{-3}$]', format='%.2f')
#fig.colorbar(contourf_plot_prof_2019, ax=axs[0, 1], label='RMSE hypolimnion profile [g m$^{-3}$]', format='%.2f')
#fig.colorbar(contourf_plot_ave_2022, ax=axs[1 , 0], label='RMSE hypolimnetic average [g m$^{-3}$]', format='%.2f')
#fig.colorbar(contourf_plot_prof_2022, ax=axs[1, 1], label='RMSE hypolimnion profile [g m$^{-3}$]', format='%.2f')




# Adjust layout
#plt.tight_layout()

# Save the combined plot with a specified dpi (dots per inch) for higher resolution
plt.savefig("combined_validation_2022_2019_rmse_ave_prof_180comb_13nov_fortnightly_daily_kzhypo_fixedtheta_on_temp_onset_to_deephypoxia.png", dpi=300)
            #_fixedtheta_on_onset_tempnotavetemp.png", dpi=300)

# Show the combined plot
plt.show()


#%%create winner dataframe according to the threshold accepatble:
os.chdir ('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/Calibration&Validation/Final/')
    
    
rmse_ave_threshold= 1
rmse_prof_threshold= 1
alpha_hypo_bulk= sum(A_l)/sum(V_r)

df_winner_of_rmses= df_calib_2020_2021[(df_calib_2020_2021['rmse_ave_calib']<rmse_ave_threshold) &
                              (df_calib_2020_2021['rmse_prof_calib']<rmse_prof_threshold)].reset_index()


df_winner_of_rmses['VHOD']= df_winner_of_rmses['Jv']+ df_winner_of_rmses['Ja']* alpha_hypo_bulk
df_winner_of_rmses['AHOD']= df_winner_of_rmses['Ja']+ df_winner_of_rmses['Jv']/ alpha_hypo_bulk

df_winner_of_rmses['weights']= df_winner_of_rmses['nse_prof_calib']


df_winner_of_all= df_winner_of_rmses[(0.04 <= df_winner_of_rmses['VHOD']) & (df_winner_of_rmses['VHOD'] <= 0.85) & (0.1 <= df_winner_of_rmses['VHOD']) & (df_winner_of_rmses['VHOD'] <= 1.7)]

df_winner_of_rmses.shape[0]==df_winner_of_all.shape[0]


array_statistics(df_winner_of_rmses['Ja'])
"""
{'Minimum': 0.001,
 'Maximum': 1.201,
 'Mean': 0.526,
 'Median': 0.451,
 'Standard Deviation': 0.37831864876053894}

"""




array_statistics(df_winner_of_rmses['Jv'])
"""
{'Minimum': 0.001,
 'Maximum': 0.6010000000000001,
 'Mean': 0.30100000000000005,
 'Median': 0.30100000000000005,
 'Standard Deviation': 0.18027756377319948}

"""







array_statistics(df_winner_of_rmses['nse_prof_calib'])
"""
{'Minimum': 0.9270812144579561,
 'Maximum': 0.9585766086905319,
 'Mean': 0.9483508171976625,
 'Median': 0.9506832550993326,
 'Standard Deviation': 0.01017822552888244}
"""

array_statistics(df_winner_of_rmses['nse_ave_calib'])
"""
{'Minimum': 0.9298344382501709,
 'Maximum': 0.9609733053973699,
 'Mean': 0.9507247429114758,
 'Median': 0.9530211575051071,
 'Standard Deviation': 0.010139414254586795}
"""
array_statistics(df_winner_of_rmses['nse_prof_valid_2022'])
"""
{'Minimum': 0.7833588739348931,
 'Maximum': 0.9355407892640419,
 'Mean': 0.8508225375296072,
 'Median': 0.8641824420810631,
 'Standard Deviation': 0.05234887698641877}
"""



array_statistics(df_winner_of_rmses['nse_prof_valid_2019'])
"""
{'Minimum': 0.5747866629148446,
 'Maximum': 0.8257557588066148,
 'Mean': 0.6921514670957719,
 'Median': 0.7117582490329195,
 'Standard Deviation': 0.08471682124799908}
"""

array_statistics(df_winner_of_rmses.rmse_ave_calib)
"""

{'Minimum': 0.7263755776752052,
 'Maximum': 0.9739627609904125,
 'Mean': 0.812073669805315,
 'Median': 0.796899746490416,
 'Standard Deviation': 0.08193471032606475}


"""

array_statistics(df_winner_of_rmses.rmse_prof_calib)
"""

{'Minimum': 0.747297558631095,
 'Maximum': 0.9914948235720811,
 'Mean': 0.8306322262737873,
 'Median': 0.8153692570657196,
 'Standard Deviation': 0.07977335684851095}

"""

array_statistics(df_winner_of_rmses['rmse_prof_valid_2022'])
"""
{'Minimum': 0.8883641158447992,
 'Maximum': 1.6286170157580189,
 'Mean': 1.3280398874237749,
 'Median': 1.2894704470609204,
 'Standard Deviation': 0.2504562737371172}
"""



array_statistics(df_winner_of_rmses['rmse_prof_valid_2019'])
"""
{'Minimum': 1.4582665336890523,
 'Maximum': 2.2780388764483566,
 'Mean': 1.9188639037793718,
 'Median': 1.8755178079906538,
 'Standard Deviation': 0.2739687633304157}
"""


array_statistics(df_winner_of_rmses['rmse_ave_valid_2022'])
"""
{'Minimum': 0.8942752088736534,
 'Maximum': 1.6585627711995738,
 'Mean': 1.3430510469192396,
 'Median': 1.3109077416309332,
 'Standard Deviation': 0.2553879776392145}
"""



array_statistics(df_winner_of_rmses['rmse_ave_valid_2019'])
"""
{'Minimum': 1.462096218520619,
 'Maximum': 2.321685271080065,
 'Mean': 1.9441427851065736,
 'Median': 1.9043720517381182,
 'Standard Deviation': 0.2872780368685993}
"""





# Select the 20 smallest values from column 'A'
#nsmallest_rmse_prof_calib = df_winner_of_rmses.nsmallest(20, 'rmse_prof_calib')


array_statistics(df_winner_of_rmses['VHOD'])
"""
{'Minimum': 0.49552461937155823,
 'Maximum': 0.6014850988014254,
 'Mean': 0.5561619695497246,
 'Median': 0.5485048590864918,
 'Standard Deviation': 0.03603236818318885}

"""
array_statistics(df_winner_of_rmses['AHOD'])

"""
{'Minimum': 1.0214921535893158,
 'Maximum': 1.2399228714524209,
 'Mean': 1.1464921535893153,
 'Median': 1.130707512520868,
 'Standard Deviation': 0.07427841107279064}
"""


# even for 100 combination it didin't add any criteria 1103 selection from 10000 combinations 
"""
df_winner_of_rmses['Jv'].mean()
Out[694]:0.30100000000000005 # fortnightly_jp , median bnd #org #temp two consequtive days
0.31864705882352945# monthly_jp, daily bnd 
0.25100000000000006# fixed theta
0.30100000000000005 #fixedtheta_on_onset_temp
0.2152857142857143fixed theta on temp of ave from onset to deep hypoxia 
0.30100000000000005# vartehta# org# temp no average

df_winner_of_rmses['Jv'].median ()
Out[700]: 0.30100000000000005# fortnightly_jp , median bnd 
0.30100000000000005# monthly_jp, daily bnd 
#0.251# fixed theta
0.30100000000000005#fixedtheta_on_onset_temp
0.201fixed theta on temp of ave from onset to deep hypoxia 
0.30100000000000005

df_winner_of_rmses['Ja'].mean()
Out[695]: 0.5260000000000001# fortnightly_jp , median bnd 
0.5892352941176471# monthly_jp, daily bnd 
0.501# fixed theta
0.6509999999999999#fixedtheta_on_onset_temp
0.6867142857142857fixed theta on temp of ave from onset to deep hypoxia 
0.5260000000000001

df_winner_of_rmses['Ja'].median()
Out[701]:0.451# fortnightly_jp , median bnd 
0.501# monthly_jp, daily bnd 
0.5010000000000001# fixed theta
0.651#fixedtheta_on_onset_temp
0.7fixed theta on temp of ave from onset to deep hypoxia 
0.451
"""

#df_winner_of_rmses['Jv'].median()+ df_winner_of_rmses['Ja'].median()* alpha_hypo_bulk
#0.5197795594428247= 0.52

#0.4940344995140914 fixed theta
#0.54 fixed theta on temp of ave from onset to deep hypoxia 
rmse_ave_valid_2022=np.array ([])
rmse_prof_valid_2022=np.array ([])
rmse_ave_valid_2019=np.array ([])
rmse_prof_valid_2019=np.array ([])

rmse_15m_2020_2021=np.array ([])
rmse_15m_2022=np.array ([])
rmse_15m_2019= np.array ([])

rmse_15m_2019_2022= np.array ([])


for i , j in zip (df_winner_of_all['Jv'] , df_winner_of_all['Ja']):
    #2022
    rmse_ave_valid_2022=np.append(rmse_ave_valid_2022 , validation_2022([i , j , 1])[0]  )
    rmse_prof_valid_2022=np.append(rmse_prof_valid_2022 , validation_2022([i , j , 1])[1]  )
    #2019
    rmse_ave_valid_2019=np.append(rmse_ave_valid_2019 , validation_2019([i , j , 1])[0]  )
    rmse_prof_valid_2019=np.append(rmse_prof_valid_2019 , validation_2019([i , j , 1])[1]  )
    
    #2020-201-15m -error 
    rmse_15m_2020_2021=  np.append(rmse_15m_2020_2021 , calibration_2020_2021([i , j , 1])[4]  )
    
    #2022-15m -error 
    rmse_15m_2022=  np.append(rmse_15m_2022 , validation_2022([i , j , 1])[4]  )
    
    #2019-15m -error 
    rmse_15m_2019=  np.append(rmse_15m_2019 , validation_2019([i , j , 1])[4]  )
    
    # all togther error in 15m depth 
    rmse_15m_2019_2022=  np.append(rmse_15m_2019_2022 , calibration_2019_2022 ([i , j , 1])[4]  )



#error in projecting 15m depth 

array_statistics(rmse_15m_2020_2021)
"""
{'Minimum': 0.7189397323952371,
 'Maximum': 0.9665415750621301,
 'Mean': 0.8091660298163599,
 'Median': 0.7927144148817458,
 'Standard Deviation': 0.08052224296769767}
"""
array_statistics(rmse_15m_2022)
"""
{'Minimum': 0.9019560213737577,
 'Maximum': 1.6977105315133196,
 'Mean': 1.354049873282355,
 'Median': 1.3382533122303204,
 'Standard Deviation': 0.2565087688784369}
"""

array_statistics(rmse_15m_2019)
"""
{'Minimum': 1.5045505860932507,
 'Maximum': 2.4523447984419473,
 'Mean': 2.0150219465223262,
 'Median': 2.001612643363529,
 'Standard Deviation': 0.30229305513417715}
"""

array_statistics(rmse_15m_2019_2022)
"""
{'Minimum': 1.10408683710638,
 'Maximum': 1.5965984628661516,
 'Mean': 1.3281529020691907,
 'Median': 1.2872514709917096,
 'Standard Deviation': 0.1673607597865355}
"""

df_winner_of_all['rmse_ave_valid_2022']=rmse_ave_valid_2022
df_winner_of_all['rmse_prof_valid_2022']=rmse_prof_valid_2022

df_winner_of_all['rmse_ave_valid_2019']=rmse_ave_valid_2019
df_winner_of_all['rmse_prof_valid_2019']=rmse_prof_valid_2019

df_winner_of_all['rmse_ave_calib']
df_winner_of_all['rmse_prof_calib']


#Calibbration 
"""
df_winner_of_all['rmse_ave_calib'].min()
0.7263718436924939# fortnightly_jp , median bnd 
0.8117563385252649# monthly_jp, daily bnd 
0.8668546947944715 # fixed theta
0.867807156103522
0.7271952314024646# vartehta# org# temp no average
0.86324927031771# fixed teatha in from onset to deep hypoxia in 2020 and 2021

df_winner_of_all['rmse_ave_calib'].max()
0.9739627609904125# fortnightly_jp , median bnd 
0.9855694926693002# monthly_jp, daily bnd 
0.880618481311082# fixed theta
0.9512425541993941
0.965539588121853
0.9791357692294809

df_winner_of_all['rmse_prof_calib'].min()
0.747297558631095# fortnightly_jp , median bnd 
0.8165796715813117# monthly_jp, daily bnd 
0.8868435684580246# fixed theta
0.8927545161886296
0.747994673605712
0.8861396788446766

df_winner_of_all['rmse_prof_calib'].max()
0.9914948235720811# fortnightly_jp , median bnd 
0.9950668930039842# monthly_jp, daily bnd 
0.8960442009608494# fixed theta
0.9704341010985565
0.9832505359004461
0.9994975745766782
"""


# validation 
"""
#min()
rmse_ave_valid_2022.min()
0.8942752088736534
0.42969856983453664
0.31281854204577236# fixed theta
0.2406969499424058
0.9036976792559621# vartehta# org# temp no average
0.33586015083540116

rmse_prof_valid_2022.min()
0.8883641158447992
0.4610738973714439
0.36753270081275763# fixed theta
0.28835570706826813
0.8974221427804361
0.38764036640844096

rmse_ave_valid_2019.min()
1.462096218520619
 1.3600493773812752
0.6139994388641854# fixed theta
0.5868837014384208
1.4750570773350862
0.6330500057826702

rmse_prof_valid_2019.min()
1.4582665336890523
1.4085974770568601
0.6967637279656145# fixed theta
0.6867751093465961
1.4700911606686595
0.7113031343240029

#max()
rmse_ave_valid_2022.max()
1.6585627711995738
1.5810740570625952
0.46172166393944725# fixed theta
0.6115086412570047
1.667002490761852
0.7373846789394799

rmse_prof_valid_2022.max()
1.6286170157580189
0.4741212531241763# fixed theta
0.6127580839128555
1.636962628985096
0.758457984790449


rmse_ave_valid_2019.max()
2.321685271080065
0.7591100079277566# fixed theta
0.9393733474218565
2.341795510868876
1.1133424432276247

rmse_prof_valid_2019.max()
2.2780388764483566
0.8335295169170798# fixed theta
0.9729299627082334
2.2975867477105583
1.1380205871183113





"""

#df_winner_of_all.to_csv('df_winner_of_all_180combinations_nokz.csv', index=False)


df_winner_of_all.to_csv('df_winner_of_all_180combinations_interval1e_1.csv', index=False)

#df_winner_of_all.to_csv('df_winner_of_all_180combinations_interval1e_1_fixedtheta_on_onset_temp.csv', index=False)

#df_winner_of_all.to_csv('df_winner_of_all_180combinations_interval1e_1_fixedtheta_on_notavetemp.csv', index=False)

#df_winner_of_all.to_csv('df_winner_of_all_180combinations_interval1e_1_fixedtheta_on_avetemp_fromonset_todeephypoxia.csv', index=False)

#%% calibartion results for nokz 

"""

array_statistics(df_winner_of_rmses['Ja'])
Out[1511]: 
{'Minimum': 0.001,
 'Maximum': 0.501,
 'Mean': 0.25099999999999995,
 'Median': 0.251,
 'Standard Deviation': 0.17078251276599332}

array_statistics(df_winner_of_rmses['Jv'])
Out[1512]: 
{'Minimum': 0.201,
 'Maximum': 0.401,
 'Mean': 0.301,
 'Median': 0.30100000000000005,
 'Standard Deviation': 0.08164965809277261}

array_statistics(df_winner_of_rmses['nse_prof_calib'])
Out[1513]: 
{'Minimum': 0.9279826871161726,
 'Maximum': 0.950420557185202,
 'Mean': 0.9410470794567786,
 'Median': 0.9455712226806471,
 'Standard Deviation': 0.009082840482966835}

array_statistics(df_winner_of_rmses['nse_ave_calib'])
Out[1514]: 
{'Minimum': 0.952256626988216,
 'Maximum': 0.9644106528378039,
 'Mean': 0.9560906882700347,
 'Median': 0.9544218586720516,
 'Standard Deviation': 0.004113689303994757}

array_statistics(df_winner_of_rmses['nse_prof_valid_2022'])
Out[1515]: 
{'Minimum': 0.8799081049186562,
 'Maximum': 0.9490828116409199,
 'Mean': 0.914858581653712,
 'Median': 0.9134246642111856,
 'Standard Deviation': 0.03108279759927347}

array_statistics(df_winner_of_rmses['nse_prof_valid_2019'])
Out[1516]: 
{'Minimum': 0.6814444667743935,
 'Maximum': 0.8279120982514022,
 'Mean': 0.756253684425992,
 'Median': 0.7572764157591356,
 'Standard Deviation': 0.06655927411173808}

array_statistics(df_winner_of_rmses.rmse_ave_calib)
Out[1517]: 
{'Minimum': 0.6936499505409108,
 'Maximum': 0.8034093800465172,
 'Mean': 0.769575529637141,
 'Median': 0.7849800468769101,
 'Standard Deviation': 0.03722279622843376}

array_statistics(df_winner_of_rmses.rmse_prof_calib)
Out[1518]: 
{'Minimum': 0.8175636212125572,
 'Maximum': 0.985346989805088,
 'Mean': 0.8889539242777552,
 'Median': 0.8565959545164812,
 'Standard Deviation': 0.06738459498105588}

array_statistics(df_winner_of_rmses['rmse_prof_valid_2022'])
Out[1519]: 
{'Minimum': 0.7895519723268565,
 'Maximum': 1.2125659393589348,
 'Mean': 1.0031219797899515,
 'Median': 1.0172030295628725,
 'Standard Deviation': 0.19014393850474465}

array_statistics(df_winner_of_rmses['rmse_prof_valid_2019'])
Out[1520]: 
{'Minimum': 1.449215138511891,
 'Maximum': 1.9717428239399581,
 'Mean': 1.7082848451156423,
 'Median': 1.710058665554045,
 'Standard Deviation': 0.2377671970293214}

array_statistics(df_winner_of_rmses['rmse_ave_valid_2022'])
Out[1521]: 
{'Minimum': 0.6297699534803997,
 'Maximum': 1.1931825936608584,
 'Mean': 0.9188456295488406,
 'Median': 0.9113394743398369,
 'Standard Deviation': 0.20740457656462485}

array_statistics(df_winner_of_rmses['rmse_ave_valid_2019'])
Out[1522]: 
{'Minimum': 1.3955470184166954,
 'Maximum': 2.0054819340059042,
 'Mean': 1.6931748690355874,
 'Median': 1.6696192000152514,
 'Standard Deviation': 0.250830108044743}

array_statistics(df_winner_of_rmses['VHOD'])
Out[1523]: 
{'Minimum': 0.39552461937155814,
 'Maximum': 0.44999497894395857,
 'Mean': 0.42275979915775835,
 'Median': 0.42275979915775835,
 'Standard Deviation': 0.0243766965980431}

array_statistics(df_winner_of_rmses['AHOD'])
Out[1524]: 
{'Minimum': 0.8153485809682806,
 'Maximum': 0.9276357262103506,
 'Mean': 0.8714921535893158,
 'Median': 0.8714921535893156,
 'Standard Deviation': 0.050250993254196366}
"""

#%%calibartion results for nokz  OLD 

"""
######without kz, ja,jv and VHOD
array_statistics(df_winner_of_all['Jv'])
{'Minimum': 0.201,
 'Maximum': 0.401,
 'Mean': 0.301,
 'Median': 0.30100000000000005,
 'Standard Deviation': 0.08164965809277261}

array_statistics(df_winner_of_all['Ja'])
{'Minimum': 0.001,
 'Maximum': 0.501,
 'Mean': 0.25099999999999995,
 'Median': 0.251,
 'Standard Deviation': 0.17078251276599332}

array_statistics(df_winner_of_all['VHOD'])
{'Minimum': 0.39552461937155814,
 'Maximum': 0.44999497894395857,
 'Mean': 0.42275979915775835,
 'Median': 0.42275979915775835,
 'Standard Deviation': 0.0243766965980431}


"""
"""
#####With kz ja, jv and vhod 
array_statistics(df_winner_of_all['Jv'])
Out[1176]: 
{'Minimum': 0.001,
 'Maximum': 0.6010000000000001,
 'Mean': 0.301,
 'Median': 0.301,
 'Standard Deviation': 0.18027756377319948}

array_statistics(df_winner_of_all['Ja'])
Out[1177]: 
{'Minimum': 0.001,
 'Maximum': 1.201,
 'Mean': 0.5260000000000001,
 'Median': 0.451,
 'Standard Deviation': 0.37831864876053894}

array_statistics(df_winner_of_all['VHOD'])
Out[1178]: 
{'Minimum': 0.4955246193715582,
 'Maximum': 0.6014850988014254,
 'Mean': 0.5561619695497246,
 'Median': 0.5485048590864918,
 'Standard Deviation': 0.036032368183188855}






"""
"""
#### with kz error 
df_winner_of_all.rmse_prof_calib.mean()
Out[1175]: 0.8306322262737872 
df_winner_of_all.rmse_prof_valid_2022.mean()
Out[1174]: 1.3280398874237747
df_winner_of_all.rmse_prof_valid_2019.mean()
Out[1173]: 1.9188639037793718

#### with no kz 
df_winner_of_all.rmse_prof_calib.mean()
Out[1169]: 0.8889539242777552
df_winner_of_all.rmse_prof_valid_2022.mean()
Out[1170]: 1.0031219797899515
df_winner_of_all.rmse_prof_valid_2019.mean()
Out[1171]: 1.7082848451156423 
"""



#%%If we wanted the performance of the model in layer 15m 

rmse_15m_calib=np.array ([])
rmse_15m_valid_2022=np.array ([])
rmse_15m_valid_2019=np.array ([])

nse_15m_calib=np.array ([])
nse_15m_valid_2022=np.array ([])
nse_15m_valid_2019=np.array ([])



for i , j in zip (df_winner_of_all['Jv'] , df_winner_of_all['Ja']):
    #rmse
    rmse_15m_calib=np.append(rmse_15m_calib , calibration_2020_2021 ([i , j , 1])[-1]  )
    rmse_15m_valid_2022=np.append(rmse_15m_valid_2022 , validation_2022([i , j , 1])[-1]  )
    rmse_15m_valid_2019=np.append(rmse_15m_valid_2019 , validation_2019([i , j , 1])[-1]  )
    
    #nse
    nse_15m_calib=np.append(nse_15m_calib , calibration_2020_2021 ([i , j , 1])[-1]  )
    nse_15m_valid_2022=np.append(nse_15m_valid_2022 , validation_2022([i , j , 1])[-1]  )
    nse_15m_valid_2019=np.append(nse_15m_valid_2019 , validation_2019([i , j , 1])[-1]  )


array_statistics(rmse_15m_calib)
{'Minimum': 0.9313923105241111,
 'Maximum': 0.9620408319180972,
 'Mean': 0.9514391187390885,
 'Median': 0.9538423059384893,
 'Standard Deviation': 0.009788790727882739}

array_statistics(rmse_15m_valid_2022)
{'Minimum': 0.7695010136349366,
 'Maximum': 0.9349402397065235,
 'Mean': 0.8481120333412753,
 'Median': 0.8567506209469464,
 'Standard Deviation': 0.054022339139298776}



array_statistics(rmse_15m_valid_2019)
{'Minimum': 0.5041883826960576,
 'Maximum': 0.813376116122341,
 'Mean': 0.6577219670211268,
 'Median': 0.669637101047925,
 'Standard Deviation': 0.09936663764925635}




array_statistics(nse_15m_calib)
{'Minimum': 0.9313923105241111,
 'Maximum': 0.9620408319180972,
 'Mean': 0.9514391187390885,
 'Median': 0.9538423059384893,
 'Standard Deviation': 0.009788790727882739}




array_statistics(nse_15m_valid_2022)
{'Minimum': 0.7695010136349366,
 'Maximum': 0.9349402397065235,
 'Mean': 0.8481120333412753,
 'Median': 0.8567506209469464,
 'Standard Deviation': 0.054022339139298776}



array_statistics(nse_15m_valid_2019)
{'Minimum': 0.5041883826960576,
 'Maximum': 0.813376116122341,
 'Mean': 0.6577219670211268,
 'Median': 0.669637101047925,
 'Standard Deviation': 0.09936663764925635}




#%% Answer to question about which depth has higher error :
    
results = []

for jv, ja in zip(df_winner_of_all['Jv'], df_winner_of_all['Ja']):
    result = calibration_2020_2021([jv, ja, 1])[2:]
    results.append(result)
    
results    
#%% Saving the results of different combination of ja and jv without weighting 
    
      
#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/outputs_prof_2019_2022_from_calibrated_JAJV')
 

#variable theta   
os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_1e_01_interval/')

#fixed theta
#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta_on_onset_temp/')

#varthemp_theta_ but not ave temp 
#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_org_notavetempthea/')

#fixed theata at temp from onset to deep hypoxia 
#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta_on_avetemp_onset_to_deephypoxia/')



#fixed theata for calib at temp from onset to deep hypoxia but var ktemp 
#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta_on_avetemp_onset_to_deephypoxia_varktemp/')




weights= df_winner_of_all['nse_prof_calib']#1- (df_winner_of_all['rmse_prof_calib'])#*df_winner_of_all['rmse_ave_calib'])
df_winner_of_all['weights']= weights# RMSE normalized between 0-1



for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    p3 = row['weights']
    
    header_values = {'Jv': p1, 'Ja': p2 , 'weights': p3 }
    header_df = pd.DataFrame([header_values])
    
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    result_do , result_temp , result_kz , result_sat = do_model_comprehensive([p1, p2 , 1], dens_diff_top_135_2019_2022 ,temp_surf_1m_2019_2022, hypo_morphology_vriables_obs_grid 
                           ,temp_2D_2019_2022_hypoprof , kz_jp_fortnightly_hypo_2D_insize_obs_2019_2022, replanishmnet_rate= 2.7946 )

    
    ###########################DO dataframe 
    # Create a DataFrame for result
    result_do = pd.DataFrame(result_do, columns=[f'{depth}m' for depth in np.arange(-14 , -17.5 , -0.5)])

    # Add a column for dates
    result_do.insert(0, 'Datetime', dens_diff_top_135_2019_2022.index)  # Replace 'your_date_array' with your actual date array

    # Define the filename_do
    filename_do = f'DO_prof_2019_2022_Jv_{Jv_name}_Ja_{Ja_name}_e_1_interval_bndr_cond_median_kzfirstlayerhypo_nottempave.csv'

    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(filename_do, index=False)


    # Save the result to a CSV file
    do_result = pd.DataFrame(result_do)  # Create a DataFrame for result
    do_result.to_csv(filename_do,mode='a', index=False, na_rep='NaN')  

    ###########################saturation dataframe 
    # Create a DataFrame for result
    result_sat = pd.DataFrame(result_sat, columns=[f'{depth}m' for depth in np.arange(-14 , -17.5 , -0.5)])

    # Add a column for dates
    result_sat.insert(0, 'Datetime', dens_diff_top_135_2019_2022.index)  # Replace 'your_date_array' with your actual date array
    
    # Define the filename
    filename_sat = f'sat_prof_2019_2022_Jv_{Jv_name}_Ja_{Ja_name}_e_1_interval_bndr_cond_median_kzfirstlayerhyp_nottempave.csv'

    # add jv, ja and weights values in the first row 
    header_df = pd.DataFrame([header_values])
    header_df.to_csv(filename_sat, index=False)


    # Save the result to a CSV file
    sat_result = pd.DataFrame(result_sat)  # Create a DataFrame for result
    sat_result.to_csv(filename_sat,mode='a', index=False, na_rep='NaN')  


result_temp=  pd.DataFrame(result_temp, columns=[f'{depth}m' for depth in np.arange(-14 , -17.5 , -0.5)])
result_temp.insert(0, 'Datetime', dens_diff_top_135_2019_2022.index)  # Replace 'your_date_array' with your actual date array
# Define the filename
filename_temp = f'temp_prof_2019_2022.csv'
temp_result = pd.DataFrame(result_temp)  # Create a DataFrame for result
temp_result.to_csv(filename_temp, index=False, na_rep='NaN') 

result_kz=  pd.DataFrame(result_kz, columns=[f'{depth}m' for depth in np.arange(-14 , -17.5 , -0.5)])
result_kz.insert(0, 'Datetime', dens_diff_top_135_2019_2022.index)  # Replace 'your_date_array' with your actual date array
# Define the filename
filename_kz = f'kz_prof_2019_2022.csv'
kz_result = pd.DataFrame(result_kz)  # Create a DataFrame for result
kz_result.to_csv(filename_kz, index=False, na_rep='NaN')  



#%%How to read through all these dataframe:
"""  
#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/outputs_prof_2019_2022_from_calibrated_JAJV')

os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_1e_01_interval/')


# model daily average in hypolimnion     
time_series= daily_hypo_prof_Temp_DO_morpho_2019_2022.index.unique()    
Vr= V_r.copy()  
# observation timeseries   
DO_obs_hypolimnetic_ave_2019_2022=np.dot (two_D_array_from_df(df_hypo_str_nomixing_2019_2022, values_name='DO',index_name='Datetime') , V_r)/sum(V_r)

#======================================Serveal scatter timeseries plots

plt.figure(figsize=(20, 10))

all_output= pd.DataFrame([])
# Iterate through the rows
for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']

    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    # Define the filename
    filename = f'DO_prof_2019_2022_Jv_{Jv_name}_Ja_{Ja_name}_e_1_interval_bnd_condition_kzfirstlayerhypo.csv'

    # Read the CSV file
    df_result = pd.read_csv(filename, header=None, na_values=['NaN'])      

    output = hypolimnetic_ave(df_result, Vr, time_series)
    
    all_output = pd.concat([all_output, output], axis=1)
    
    plt.scatter(output.index, output.values, marker='o', s=100, label='Jv: {}, Ja: {}'.format(Jv_name, Ja_name))
    



plt.scatter (df_hypo_str_nomixing_2019_2022.index.unique() ,DO_obs_hypolimnetic_ave_2019_2022 , color= 'k' , label= 'Obs')


plt.ylabel('Hypolimnetic DO average [g m$^{-3}$]')
#plt.title('Time Series Data')   
#plt.legend()  

plt.savefig("scatter_plot_of_hypolimnetic_DO_ave_obs_JvJa_2019_2022_bnd_condition_kzfirstlayerhypo.png", dpi=300)
"""
#%% fill_between plots:
"""
#===========================2019_2022: calibartion and 2 validation periods 

all_output.index = pd.to_datetime(all_output.index)

plt.figure(figsize=(20, 10))
plt.fill_between( all_output.index , all_output.min(axis=1) , all_output.max(axis=1), color='red', alpha=0.4 , label= 'Model range')
plt.scatter(df_hypo_str_nomixing_2019_2022.index.unique() ,DO_obs_hypolimnetic_ave_2019_2022 , color= 'k' , label= 'Obs')

plt.ylabel('Hypolimnetic DO average [g m$^{-3}$]')
plt.legend()


#plt.savefig("fillbetween_hypolimnetic_DO_ave_obs_JvJa_2019_2022.png", dpi=300)
#================================2020_2021: calibartion period 
#subseting data according their dates 
filterd_df_obs= df_hypo_str_nomixing_2019_2022[(df_hypo_str_nomixing_2019_2022.index.year==2020) |  (df_hypo_str_nomixing_2019_2022.index.year==2021)]
filterd_DO_obs_2D=np.dot (two_D_array_from_df(filterd_df_obs, values_name='DO',index_name='Datetime') , V_r)/sum(V_r)

filterd_df_model= all_output[(all_output.index.year==2020) | (all_output.index.year==2021)]
#ploting 

plt.figure(figsize=(12, 10))
plt.fill_between( filterd_df_model.index , filterd_df_model.min(axis=1) , filterd_df_model.max(axis=1), color='red', alpha=0.4 , label= 'Model range')
plt.scatter(filterd_df_obs.index.unique() ,filterd_DO_obs_2D , color= 'k' , label= 'Obs')

plt.ylabel('Hypolimnetic DO average [g m$^{-3}$]')
plt.xticks(rotation=45)

plt.legend(loc='upper center')

#plt.savefig("fillbetween_hypolimnetic_DO_ave_obs_JvJa_Calib_period_2020_2021.png", dpi=300)

#================================2022: 1st valibartion period 
#subseting data according their dates 
filterd_df_obs= df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022.index.year==2022]
filterd_DO_obs_2D=np.dot (two_D_array_from_df(filterd_df_obs, values_name='DO',index_name='Datetime') , V_r)/sum(V_r)

filterd_df_model= all_output[all_output.index.year==2022]
#ploting 

plt.figure(figsize=(12, 10))
plt.fill_between( filterd_df_model.index , filterd_df_model.min(axis=1) , filterd_df_model.max(axis=1), color='red', alpha=0.4 , label= 'Model range')
plt.scatter(filterd_df_obs.index.unique() ,filterd_DO_obs_2D , color= 'k' , label= 'Obs')

plt.ylabel('Hypolimnetic DO average [g m$^{-3}$]')
plt.xticks(rotation=45)

plt.legend(loc='upper center')

#plt.savefig("fillbetween_hypolimnetic_DO_ave_obs_JvJa_valid1_2022.png", dpi=300)

#================================2019: 2nd valibartion period 
#subseting data according their dates 
filterd_df_obs= df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022.index.year==2019]
filterd_DO_obs_2D=np.dot (two_D_array_from_df(filterd_df_obs, values_name='DO',index_name='Datetime') , V_r)/sum(V_r)

filterd_df_model= all_output[all_output.index.year==2019]
#ploting 

plt.figure(figsize=(12, 10))
plt.fill_between( filterd_df_model.index , filterd_df_model.min(axis=1) , filterd_df_model.max(axis=1), color='red', alpha=0.4 , label= 'Model range')
plt.scatter(filterd_df_obs.index.unique() ,filterd_DO_obs_2D , color= 'k' , label= 'Obs')

plt.ylabel('Hypolimnetic DO average [g m$^{-3}$]')
plt.xticks(rotation=45)

plt.legend(loc='upper center')

#plt.savefig("fillbetween_hypolimnetic_DO_ave_obs_JvJa_valid2_2019.png", dpi=300)

#==========================All years in subplots 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Your code for 2020 calibration period
filterd_df_obs_2020 = df_hypo_str_nomixing_2019_2022[(df_hypo_str_nomixing_2019_2022.index.year==2020)]
filterd_DO_obs_2D_2020 = np.dot(two_D_array_from_df(filterd_df_obs_2020, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2020 = all_output[(all_output.index.year==2020)]


# Your code for 2021 calibration period
filterd_df_obs_2021 = df_hypo_str_nomixing_2019_2022[(df_hypo_str_nomixing_2019_2022.index.year==2021)]
filterd_DO_obs_2D_2021 = np.dot(two_D_array_from_df(filterd_df_obs_2021, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2021 = all_output[(all_output.index.year==2021)]



# Your code for 2022 validation
filterd_df_obs_2022 = df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022.index.year==2022]
filterd_DO_obs_2D_2022 = np.dot(two_D_array_from_df(filterd_df_obs_2022, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2022 = all_output[all_output.index.year==2022]

# Your code for 2019 validation
filterd_df_obs_2019 = df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022.index.year==2019]
filterd_DO_obs_2D_2019 = np.dot(two_D_array_from_df(filterd_df_obs_2019, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2019 = all_output[all_output.index.year==2019]

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(18, 15))

# Plot for 2020_2021 calibration period
axes[0, 0].fill_between(filterd_df_model_2020.index, filterd_df_model_2020.min(axis=1), filterd_df_model_2020.max(axis=1), color='red', alpha=0.4, label='Model range')
axes[0, 0].scatter(filterd_df_obs_2020.index.unique(), filterd_DO_obs_2D_2020, color='k', label='Obs')
axes[0, 0].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]')
axes[0, 0].legend(loc='upper center')
axes[0, 0].set_title('Calibration 2020 ')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot for 2020_2021 calibration period
axes[0, 1].fill_between(filterd_df_model_2021.index, filterd_df_model_2021.min(axis=1), filterd_df_model_2021.max(axis=1), color='red', alpha=0.4, label='Model range')
axes[0, 1].scatter(filterd_df_obs_2021.index.unique(), filterd_DO_obs_2D_2021, color='k', label='Obs')
axes[0, 1].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]')
axes[0, 1].legend(loc='upper center')
axes[0, 1].set_title('Calibration 2021')
axes[0, 1].tick_params(axis='x', rotation=45)

# Plot for 2019 validation
axes[1, 0].fill_between(filterd_df_model_2019.index, filterd_df_model_2019.min(axis=1), filterd_df_model_2019.max(axis=1), color='blue', alpha=0.4, label='Model range')
axes[1, 0].scatter(filterd_df_obs_2019.index.unique(), filterd_DO_obs_2D_2019, color='k', label='Obs')
axes[1, 0].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]')
axes[1, 0].legend(loc='upper center')
axes[1, 0].set_title('Validation 2019')
axes[1, 0].tick_params(axis='x', rotation=45)
# Plot for 2022 validation
axes[1, 1].fill_between(filterd_df_model_2022.index, filterd_df_model_2022.min(axis=1), filterd_df_model_2022.max(axis=1), color='blue', alpha=0.4, label='Model range')
axes[1, 1].scatter(filterd_df_obs_2022.index.unique(), filterd_DO_obs_2D_2022, color='k', label='Obs')
axes[1, 1].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]')
axes[1, 1].legend(loc='upper center')
axes[1, 1].set_title('Validation 2022')
axes[1, 1].tick_params(axis='x', rotation=45)
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("subplots_hypolimnetic_DO_ave_obs_seperatly_each_year.png", dpi=300)
plt.show()
"""
#%%same but this time with GLUE 

#%%1.
#https://notebook.community/JamesSample/enviro_mod_notes/notebooks/07_GLUE

#Using just the behavioural parameter sets, we rank the model output 
#and calculate weighted quantiles to produce the desired CDF
#cumulative distribution function (cdf) 


def weighted_quantiles(values, quantiles, sample_weight=None):
    """ Modified from 
        http://stackoverflow.com/questions/21844024/weighted-percentile-using-numpy     
        NOTE: quantiles should be in [0, 1]
        
        values         array with data
        quantiles      array with desired quantiles
        sample_weight  array of weights (the same length as `values`)

        Returns array with computed quantiles.
    """
    # Convert to arrays
    values = np.array(values)
    quantiles = np.array(quantiles)
    
    
    # Assign equal weights if necessary
    if sample_weight is None:
        sample_weight = np.ones(len(values))
        
    # Otherwise use specified weights
    sample_weight = np.array(sample_weight)
    
    # Check quantiles specified OK
    assert np.all(quantiles >= 0) and np.all(quantiles <= 1), 'quantiles should be in [0, 1]'

    # Sort 
    sorter = np.argsort(values)
    values = values[sorter]
    sample_weight = sample_weight[sorter]

    # Compute weighted quantiles
    weighted_quantiles = (np.cumsum(sample_weight) - 0.5 * sample_weight)#/np.sum(sample_weight)
    weighted_quantiles /= np.sum(sample_weight)
    
    return np.interp(quantiles, weighted_quantiles, values)
#%%
"""
import numpy as np

def weighted_percentile(data, weights, perc):
    """
    perc : percentile in [0-1]!
    """
    ix = np.argsort(data)
    data = data[ix] # sort data
    weights = weights[ix] # sort weights
    cdf = (np.cumsum(weights) - 0.5 * weights) / np.sum(weights) # 'like' a CDF function
    return np.interp(perc, cdf, data)

"""
#%%2.

   
#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/outputs_prof_2019_2022_from_calibrated_JAJV')

#os.chdir('C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta_on_onset_temp/')


weights= df_winner_of_all['nse_prof_calib']#*df_winner_of_all['rmse_ave_calib'])
df_winner_of_all['weights']= weights# RMSE normalized between 0-1




#variable theta 
#directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_1e_01_interval'

#varthemp_theta_ but not ave temp 
#directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_org_notavetempthea/'



#fixed theta

#directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta/'

#directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta_on_onset_temp/'

# fixed theta both in calibration and simulation

directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta_on_avetemp_onset_to_deephypoxia/'


#fixed theta ja and jv but simulation based on variable theta 

#directory= 'C:/Users/mahta/OneDrive/Documents/Chapter_1_PhD_py_codes_results/outputs/Erken/output_prof_2019_2022_from_calibrated_JVJA_fixedtheta_on_avetemp_onset_to_deephypoxia_varktemp/'



os.chdir(directory)
# observation timeseries   
DO_obs_hypolimnetic_ave_2019_2022=np.dot (two_D_array_from_df(df_hypo_str_nomixing_2019_2022, values_name='DO',index_name='Datetime') , V_r)/sum(V_r)
all_output= pd.DataFrame([])

all_C_profile_depth0= pd.DataFrame([])
all_C_profile_depth1= pd.DataFrame([])
all_C_profile_depth2= pd.DataFrame([])
all_C_profile_depth3= pd.DataFrame([])
all_C_profile_depth4= pd.DataFrame([])
all_C_profile_depth5= pd.DataFrame([])
all_C_profile_depth6= pd.DataFrame([])
# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_2019_2022"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr = V_r  
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        output = hypolimnetic_ave(C, Vr, time_series)
        
        all_output = pd.concat([all_output, output], axis=1)
        
        
        C_df0= pd.DataFrame(C[:, 0])
        all_C_profile_depth0= pd.concat([all_C_profile_depth0, C_df0], axis=1)
        
        C_df1= pd.DataFrame(C[:, 1])
        all_C_profile_depth1= pd.concat([all_C_profile_depth1, C_df1], axis=1)
        
        C_df2= pd.DataFrame(C[:, 2])
        all_C_profile_depth2= pd.concat([all_C_profile_depth2, C_df2], axis=1)
        
        C_df3= pd.DataFrame(C[:, 3])
        all_C_profile_depth3= pd.concat([all_C_profile_depth3, C_df3], axis=1)
        
        C_df4= pd.DataFrame(C[:, 4])
        all_C_profile_depth4= pd.concat([all_C_profile_depth4, C_df4], axis=1)
        
        C_df5= pd.DataFrame(C[:, 5])
        all_C_profile_depth5= pd.concat([all_C_profile_depth5, C_df5], axis=1)
        
        C_df6= pd.DataFrame(C[:, 6])
        all_C_profile_depth6= pd.concat([all_C_profile_depth6, C_df6], axis=1)
        
        
"""
all_output= pd.DataFrame([])
# Iterate through the rows
for index, row in df_winner_of_all.iterrows():
    p1 = row['Jv']
    p2 = row['Ja']
    weight= row['weights']
    # Round Ja and Jv to 3 decimal places
    Jv_name = round(p1, 3)
    Ja_name = round(p2, 3)

    # Define the filename
    filename = f'DO_prof_2019_2022_Jv_{Jv_name}_Ja_{Ja_name}_e_1_interval_bnd_cond_kzfirstlayerhypo.csv'

    # Read the CSV file
    df_result = pd.read_csv(filename, header=None, na_values=['NaN'])      

    output = hypolimnetic_ave(df_result, Vr, time_series)
    
    all_output = pd.concat([all_output, output], axis=1)
"""    
#%%Glue of hypolimnetic average 


weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_output.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
#%% in one plot all but not in subplot 
"""
#plotting 
fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)
#plt.fill_between(time_series, glue_df['2.5%'], glue_df['97.5%'], color='r', alpha=0.4)
#plt.plot(time_series, glue_df['50%'], 'r-', label='Estimated')
ax=plt.fill_between(time_series, glue_df['5%'], glue_df['95%'], color='r', alpha=0.4 ,  label= '5-95% model bound')
ax=plt.plot(time_series, glue_df['50%'], 'k--', label='Median prediction', alpha=0.9 )

ax=plt.scatter (df_hypo_str_nomixing_2019_2022.index.unique() ,DO_obs_hypolimnetic_ave_2019_2022 , color= 'k' , label= 'Observation')
ax=plt.ylabel('Hypolimnetic DO average [g m$^{-3}$]')
ax=plt.xticks(rotation=45)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2))   
#plt.title('GLUE')
fig.savefig("GLUE_Timeseries_hypolimnetic_DO_14combinationJaJv_ave_obs_alltogther_2019_2022_bnd_condition_kzfirstlayerhypo.png", dpi=300)
"""
#%%



#fixed theta in both calib and simulation 


glue_df.mean()
Out[2893]: 
5%     3.565083
50%    3.903408
95%    4.000170
dtype: float64





#fixed theta in calib but vartheta in simulation 

glue_df.mean()
Out[2871]: 
5%     3.861066
50%    3.926873
95%    4.033086
dtype: float64



#fixed theta in both calib and simulation 






#==========================All years in subplots 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


glue_df_indexed= glue_df.set_index(time_series)

glue_df_indexed_fix= glue_df.set_index(time_series)


# Your code for 2020 calibration period
filterd_df_obs_2020 = df_hypo_str_nomixing_2019_2022[(df_hypo_str_nomixing_2019_2022.index.year==2020)]
filterd_DO_obs_2D_2020 = np.dot(two_D_array_from_df(filterd_df_obs_2020, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2020 = glue_df_indexed[(glue_df_indexed.index.year==2020)]

filterd_df_model_2020.mean()
Out[2918]: 
5%     3.29186
50%    3.60758
95%    3.68809
dtype: float64



filterd_df_model_2020_fix =glue_df_indexed_fix[(glue_df_indexed_fix.index.year==2020)]
filterd_df_model_2020_fix.mean()
Out[2917]: 
5%     3.459622
50%    3.622241
95%    3.688090
dtype: float64



#fixed theta- var  
#3.622241-3.462730=0.15951099999999974


# Your code for 2021 calibration period
filterd_df_obs_2021 = df_hypo_str_nomixing_2019_2022[(df_hypo_str_nomixing_2019_2022.index.year==2021)]
filterd_DO_obs_2D_2021 = np.dot(two_D_array_from_df(filterd_df_obs_2021, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2021 = glue_df_indexed[(glue_df_indexed.index.year==2021)]
#var mean
5%     4.204132
50%    4.381786
95%    4.468543



# fixed mean 
filterd_df_model_2021_fix =glue_df_indexed_fix[(glue_df_indexed_fix.index.year==2021)]
5%     3.833510
50%    4.014646
95%    4.099187


#fixed theta- var  
filterd_df_model_2021_fix.mean()- filterd_df_model_2021.mean()
5%    -0.370622
50%   -0.367141
95%   -0.369356
dtype: float64



# Your code for 2022 validation
filterd_df_obs_2022 = df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022.index.year==2022]
filterd_DO_obs_2D_2022 = np.dot(two_D_array_from_df(filterd_df_obs_2022, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2022 = glue_df_indexed[(glue_df_indexed.index.year==2022)]

#
Out[2924]: 
5%     2.553180
50%    2.656489
95%    2.704601
dtype: float64






# fixed mean 
filterd_df_model_2022_fix =glue_df_indexed_fix[(glue_df_indexed_fix.index.year==2022)]
filterd_df_model_2022_fix.mean()
Out[2921]: 
5%     3.140458
50%    3.278716
95%    3.340337
dtype: float64


#fixed theta- var  
filterd_df_model_2022_fix.mean()- filterd_df_model_2022.mean()

5%     0.587278
50%    0.622228
95%    0.635737
dtype: float64



# Your code for 2019 validation
filterd_df_obs_2019 = df_hypo_str_nomixing_2019_2022[df_hypo_str_nomixing_2019_2022.index.year==2019]
filterd_DO_obs_2D_2019 = np.dot(two_D_array_from_df(filterd_df_obs_2019, values_name='DO', index_name='Datetime'), V_r) / sum(V_r)
filterd_df_model_2019 = glue_df_indexed[(glue_df_indexed.index.year==2019)]

filterd_df_model_2019.mean()
5%     3.832555
50%    3.999029
95%    4.085196
dtype: float64


# fixed mean 
filterd_df_model_2019_fix =glue_df_indexed_fix[(glue_df_indexed_fix.index.year==2019)]
filterd_df_model_2019_fix.mean()
Out[2921]: 
5%     4.575146
50%    4.808309
95%    4.915808
dtype: float64


#fixed theta- var  
filterd_df_model_2019_fix.mean()- filterd_df_model_2019.mean()
5%     0.742591
50%    0.809279
95%    0.830612
dtype: float64



#%% average of annually 

#fixed theta in both calib and simu : 3.930977948694309

#fixed in calibration vartheta in simu :3.625008584646753

#fixed - var:  0.3059693640475558

#%%================== Create subplots

fig, axes = plt.subplots(2, 2, figsize=(20, 22))
# Plot for 2020_2021 calibration period
axes[0, 0].fill_between(filterd_df_model_2020.index, filterd_df_model_2020['5%'], filterd_df_model_2020['95%'], color='red', alpha=0.4, label='5-95% model bound')
axes[0, 0].plot(filterd_df_model_2020.index, filterd_df_model_2020['50%'], 'k--', label='Median model', alpha=0.9 )
axes[0, 0].scatter(filterd_df_obs_2020.index.unique(), filterd_DO_obs_2D_2020, color='k', label='Obs')
axes[0, 0].set_ylabel('Deep-water DO average [mg L$^{-1}$]' , fontsize= 32 )
#axes[0, 0].legend(loc='upper center')
axes[0,0].set_ylim([0 , 12.5])
axes[0, 0].set_title('(a) Calibration 2020 ', fontsize='32')
axes[0, 0].tick_params(axis='x', rotation=45)


# Plot for 2020_2021 calibration period
axes[0, 1].fill_between(filterd_df_model_2021.index, filterd_df_model_2021['5%'], filterd_df_model_2021['95%'], color='red', alpha=0.4)#, label='5-95% model bound'
axes[0, 1].plot(filterd_df_model_2021.index, filterd_df_model_2021['50%'], 'k--', alpha=0.9 )#, label='Median model'
axes[0, 1].scatter(filterd_df_obs_2021.index.unique(), filterd_DO_obs_2D_2021, color='k')#, label='Obs'
#axes[0, 1].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]' , fontsize= 32 )
#axes[0, 1].legend(loc='upper center')
axes[0, 1].set_ylim([0 , 12.5])
axes[0, 1].set_title('(b) Calibration 2021 ', fontsize='32')
axes[0, 1].tick_params(axis='x', rotation=45)

# Plot for 2019 validation
axes[1, 0].fill_between(filterd_df_model_2019.index, filterd_df_model_2019['5%'], filterd_df_model_2019['95%'], color='red', alpha=0.4)#, label='5-95% model bound'
axes[1, 0].plot(filterd_df_model_2019.index, filterd_df_model_2019['50%'], 'k--', alpha=0.9 )#, label='Median model'
axes[1, 0].scatter(filterd_df_obs_2019.index.unique(), filterd_DO_obs_2D_2019, color='k')#, label='Obs'
axes[1, 0].set_ylabel('Deep-water DO average [mg L$^{-1}$]' , fontsize= 32 )
#axes[1, 0].legend(loc='upper center')
axes[1, 0].set_ylim([0 , 12.5])
axes[1, 0].set_title('(c) Validation 2019 ', fontsize='32')
axes[1, 0].tick_params(axis='x', rotation=45)


# Plot for 2022 validation
axes[1, 1].fill_between(filterd_df_model_2022.index, filterd_df_model_2022['5%'], filterd_df_model_2022['95%'], color='red', alpha=0.4)#, label='5-95% model bound'
axes[1, 1].plot(filterd_df_model_2022.index, filterd_df_model_2022['50%'], 'k--',  alpha=0.9 )#,label='Median model'
axes[1, 1].scatter(filterd_df_obs_2022.index.unique(), filterd_DO_obs_2D_2022, color='k')#, label='Obs'
#axes[1, 1].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]' , fontsize= 32 )
#axes[1, 1].legend(loc='upper center')
axes[1, 1].set_title('(d) Validation 2022 ', fontsize='32')
axes[1, 1].set_ylim([0 , 12.5])
axes[1 , 1].tick_params(axis='x', rotation=45)


#axes[0, 0].legend(bbox_to_anchor=(1.5, -1.5), fontsize= 40)
#fig.legend( bbox_to_anchor=(0.7, 0) , fontsize= 40) 
# Add a common legend
fig.legend(['90% CI', 'Median model', 'Obs'], bbox_to_anchor=(0.5, 0.1), loc='upper center', fontsize=38  , ncol=3)

# Adjust layout and save the plot
for ax in axes.flatten():
    ax.tick_params(axis='both', labelsize=30)

plt.tight_layout() 
plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin to make space for the legend
 
plt.savefig("subplots_glumethod_hypolimnetic_DO_ave_obs_seperatly_each_year_bnd_condition_kzfirstlayerhypo_median_jp_fortnightly_fixedtheta_temponsettodeephypoxia.png", dpi=300)
plt.show()


#%%Profile Validation 
#%%glue for each layer seperately 
weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_profile_depth0.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df_profile_depth0 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_profile_depth0= glue_df_profile_depth0.set_index(time_series)

# Glue for each layer seperately 
weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_profile_depth1.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df_profile_depth1 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_profile_depth1= glue_df_profile_depth1.set_index(time_series)


# Glue for each layer seperately 
weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_profile_depth2.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df_profile_depth2 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_profile_depth2= glue_df_profile_depth2.set_index(time_series)


# Glue for each layer seperately 
weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_profile_depth3.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df_profile_depth3 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_profile_depth3= glue_df_profile_depth3.set_index(time_series)

# Glue for each layer seperately 
weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_profile_depth4.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df_profile_depth4 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_profile_depth4= glue_df_profile_depth4.set_index(time_series)

# Glue for each layer seperately 
weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_profile_depth5.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df_profile_depth5 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_profile_depth5= glue_df_profile_depth5.set_index(time_series)


# Glue for each layer seperately 
weights= df_winner_of_all['weights']

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_C_profile_depth6.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df_profile_depth6 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])

glue_df_profile_depth6= glue_df_profile_depth6.set_index(time_series)




#%% 1st of Jun and July profiles 

#depth
df_hypo_str_nomixing_2019_2022['Z_m+'].unique()
#array([14. , 14.5, 15. , 15.5, 16. , 16.5, 17. ])

#obs 
df_hypo_str_nomixing_2019_2022.loc['2022-06-01']['DO']

df_hypo_str_nomixing_2019_2022.loc['2021-06-01']['DO']

#df_hypo_str_nomixing_2019_2022.loc['2019-06-01']['DO']# khoobe performance model dar in tarikh


import matplotlib.pyplot as plt
import pandas as pd

# Assuming df_hypo_str_nomixing_2019_2022 is your DataFrame


depths_prof = df_hypo_str_nomixing_2019_2022['Z_m+'].unique()


# Sample data for 2022-06-01
data_2022_06_01 = df_hypo_str_nomixing_2019_2022.loc['2022-06-01']['DO']


# Sample data for 2021-06-01
data_2021_06_01 = df_hypo_str_nomixing_2019_2022.loc['2021-06-01']['DO']




"""



# Plotting
plt.figure(figsize=(12, 10))


# Plot for 2022-06-01
plt.scatter(data_2022_06_01, depths_prof, marker='o', label='Obs-2022-06-01', color= 'k')

plt.plot(do_glue_50_2022_06_01, depths_prof, marker='o', label='Median model' , color= 'red')

plt.fill_betweenx(depths_prof, do_glue_5_2022_06_01, do_glue_95_2022_06_01, color='red', alpha=0.4, label='5-95% model bound')



# Customize plot
plt.xlabel('DO [g m-3]') 
plt.ylabel('Depth [m]')

plt.xticks([8, 8.5, 9, 9.5, 10])

plt.gca().invert_yaxis()

plt.legend(loc= 'upper left')





plt.figure(figsize=(12, 10))


# Plot for 2021-06-01
plt.scatter( data_2021_06_01, depths_prof, marker='o',label='Obs-2021-06-01', color= 'k')


plt.plot(do_glue_50_2021_06_01, depths_prof, marker='o', label='Median model' , color= 'red')


plt.fill_betweenx(depths_prof, do_glue_5_2021_06_01, do_glue_95_2021_06_01, color='red', alpha=0.4, label='5-95% model bound')

# Customize plot
plt.xlabel('DO [g m-3]') 
plt.ylabel('Depth [m]')

plt.xticks([8, 8.5, 9, 9.5, 10])

plt.gca().invert_yaxis()

plt.legend(loc= 'lower right')

"""













#2022-06-01
do_glue_5_2022_06_01=np.array([glue_df_profile_depth0.loc['2022-06-01']['5%'] , glue_df_profile_depth1.loc['2022-06-01']['5%'] , glue_df_profile_depth2.loc['2022-06-01']['5%'] , glue_df_profile_depth3.loc['2022-06-01']['5%'] , 
glue_df_profile_depth4.loc['2022-06-01']['5%'] , glue_df_profile_depth5.loc['2022-06-01']['5%'] , glue_df_profile_depth6.loc['2022-06-01']['5%']])


do_glue_50_2022_06_01=np.array([glue_df_profile_depth0.loc['2022-06-01']['50%'] , glue_df_profile_depth1.loc['2022-06-01']['50%'] , glue_df_profile_depth2.loc['2022-06-01']['50%'] , glue_df_profile_depth3.loc['2022-06-01']['50%'] , 
glue_df_profile_depth4.loc['2022-06-01']['50%'] , glue_df_profile_depth5.loc['2022-06-01']['50%'] , glue_df_profile_depth6.loc['2022-06-01']['50%']])


do_glue_95_2022_06_01=np.array([glue_df_profile_depth0.loc['2022-06-01']['95%'] , glue_df_profile_depth1.loc['2022-06-01']['95%'] , glue_df_profile_depth2.loc['2022-06-01']['95%'] , glue_df_profile_depth3.loc['2022-06-01']['95%'] , 
glue_df_profile_depth4.loc['2022-06-01']['95%'] , glue_df_profile_depth5.loc['2022-06-01']['95%'] , glue_df_profile_depth6.loc['2022-06-01']['95%']])


#2021-06-01
do_glue_5_2021_06_01=np.array([glue_df_profile_depth0.loc['2021-06-01']['5%'] , glue_df_profile_depth1.loc['2021-06-01']['5%'] , glue_df_profile_depth2.loc['2021-06-01']['5%'] , glue_df_profile_depth3.loc['2021-06-01']['5%'] , 
glue_df_profile_depth4.loc['2021-06-01']['5%'] , glue_df_profile_depth5.loc['2021-06-01']['5%'] , glue_df_profile_depth6.loc['2021-06-01']['5%']])


do_glue_50_2021_06_01=np.array([glue_df_profile_depth0.loc['2021-06-01']['50%'] , glue_df_profile_depth1.loc['2021-06-01']['50%'] , glue_df_profile_depth2.loc['2021-06-01']['50%'] , glue_df_profile_depth3.loc['2021-06-01']['50%'] , 
glue_df_profile_depth4.loc['2021-06-01']['50%'] , glue_df_profile_depth5.loc['2021-06-01']['50%'] , glue_df_profile_depth6.loc['2021-06-01']['50%']])


do_glue_95_2021_06_01=np.array([glue_df_profile_depth0.loc['2021-06-01']['95%'] , glue_df_profile_depth1.loc['2021-06-01']['95%'] , glue_df_profile_depth2.loc['2021-06-01']['95%'] , glue_df_profile_depth3.loc['2021-06-01']['95%'] , 
glue_df_profile_depth4.loc['2021-06-01']['95%'] , glue_df_profile_depth5.loc['2021-06-01']['95%'] , glue_df_profile_depth6.loc['2021-06-01']['95%']])



#1st July:
    
data_2022_07_01=df_hypo_str_nomixing_2019_2022.loc['2022-07-01']['DO']
data_2021_07_01=df_hypo_str_nomixing_2019_2022.loc['2021-07-01']['DO']



#2022-07-01
do_glue_5_2022_07_01=np.array([glue_df_profile_depth0.loc['2022-07-01']['5%'] , glue_df_profile_depth1.loc['2022-07-01']['5%'] , glue_df_profile_depth2.loc['2022-07-01']['5%'] , glue_df_profile_depth3.loc['2022-07-01']['5%'] , 
glue_df_profile_depth4.loc['2022-07-01']['5%'] , glue_df_profile_depth5.loc['2022-07-01']['5%'] , glue_df_profile_depth6.loc['2022-07-01']['5%']])


do_glue_50_2022_07_01=np.array([glue_df_profile_depth0.loc['2022-07-01']['50%'] , glue_df_profile_depth1.loc['2022-07-01']['50%'] , glue_df_profile_depth2.loc['2022-07-01']['50%'] , glue_df_profile_depth3.loc['2022-07-01']['50%'] , 
glue_df_profile_depth4.loc['2022-07-01']['50%'] , glue_df_profile_depth5.loc['2022-07-01']['50%'] , glue_df_profile_depth6.loc['2022-07-01']['50%']])


do_glue_95_2022_07_01=np.array([glue_df_profile_depth0.loc['2022-07-01']['95%'] , glue_df_profile_depth1.loc['2022-07-01']['95%'] , glue_df_profile_depth2.loc['2022-07-01']['95%'] , glue_df_profile_depth3.loc['2022-07-01']['95%'] , 
glue_df_profile_depth4.loc['2022-07-01']['95%'] , glue_df_profile_depth5.loc['2022-07-01']['95%'] , glue_df_profile_depth6.loc['2022-07-01']['95%']])


#2021-07-01
do_glue_5_2021_07_01=np.array([glue_df_profile_depth0.loc['2021-07-01']['5%'] , glue_df_profile_depth1.loc['2021-07-01']['5%'] , glue_df_profile_depth2.loc['2021-07-01']['5%'] , glue_df_profile_depth3.loc['2021-07-01']['5%'] , 
glue_df_profile_depth4.loc['2021-07-01']['5%'] , glue_df_profile_depth5.loc['2021-07-01']['5%'] , glue_df_profile_depth6.loc['2021-07-01']['5%']])


do_glue_50_2021_07_01=np.array([glue_df_profile_depth0.loc['2021-07-01']['50%'] , glue_df_profile_depth1.loc['2021-07-01']['50%'] , glue_df_profile_depth2.loc['2021-07-01']['50%'] , glue_df_profile_depth3.loc['2021-07-01']['50%'] , 
glue_df_profile_depth4.loc['2021-07-01']['50%'] , glue_df_profile_depth5.loc['2021-07-01']['50%'] , glue_df_profile_depth6.loc['2021-07-01']['50%']])


do_glue_95_2021_07_01=np.array([glue_df_profile_depth0.loc['2021-07-01']['95%'] , glue_df_profile_depth1.loc['2021-07-01']['95%'] , glue_df_profile_depth2.loc['2021-07-01']['95%'] , glue_df_profile_depth3.loc['2021-07-01']['95%'] , 
glue_df_profile_depth4.loc['2021-07-01']['95%'] , glue_df_profile_depth5.loc['2021-07-01']['95%'] , glue_df_profile_depth6.loc['2021-07-01']['95%']])

    






"""

# Plotting
plt.figure(figsize=(12, 10))


# Plot for 2022-06-01
plt.scatter(data_2022_07_01, depths_prof, marker='o', label='Obs-2022-07-01', color= 'k')

plt.plot(do_glue_50_2022_07_01, depths_prof, marker='o', label='Median model' , color= 'red')

plt.fill_betweenx(depths_prof, do_glue_5_2022_07_01, do_glue_95_2022_07_01, color='red', alpha=0.4, label='5-95% model bound')



# Customize plot
plt.xlabel('DO [g m-3]') 
plt.ylabel('Depth [m]')

plt.xticks([2 , 3 , 4 , 5 , 6])

plt.gca().invert_yaxis()

plt.legend(loc= 'lower right')





plt.figure(figsize=(12, 10))


# Plot for 2021-06-01
plt.scatter( data_2021_07_01, depths_prof, marker='o',label='Obs-2021-07-01', color= 'k')


plt.plot(do_glue_50_2021_07_01, depths_prof, marker='o', label='Median model' , color= 'red')


plt.fill_betweenx(depths_prof, do_glue_5_2021_07_01, do_glue_95_2021_07_01, color='red', alpha=0.4, label='5-95% model bound')

# Customize plot
plt.xlabel('DO [g m-3]') 
plt.ylabel('Depth [m]')

plt.xticks([2 , 3 , 4 , 5 , 6])

plt.gca().invert_yaxis()

plt.legend(loc= 'upper left')
"""
#%%plotiing the profiles 




import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))#  sharey=True)

# Plot for 2022-06-01
axes[0, 1].scatter(data_2022_06_01, depths_prof, marker='o', color='k', label='Obs')
axes[0, 1].plot(do_glue_50_2022_06_01, depths_prof, marker='o', color='red', label='Median model')
axes[0, 1].fill_betweenx(depths_prof, do_glue_5_2022_06_01, do_glue_95_2022_06_01, color='red', alpha=0.4)
axes[0, 1].set_xlabel('DO [mg L$^{-1}$]')
axes[0, 1].set_ylabel('Depth [m]')
axes[0, 1].set_xticks([8, 8.5, 9, 9.5, 10])
axes[0, 1].invert_yaxis()
axes[0, 1].set_title('(b) Validation 2022-06-01')

# Plot for 2021-06-01
axes[0, 0].scatter(data_2021_06_01, depths_prof, marker='o', color='k')
axes[0, 0].plot(do_glue_50_2021_06_01, depths_prof, marker='o', color='red')
axes[0, 0].fill_betweenx(depths_prof, do_glue_5_2021_06_01, do_glue_95_2021_06_01, color='red', alpha=0.4)
axes[0, 0].set_xlabel('DO [mg L$^{-1}$]')
axes[0, 0].set_ylabel('Depth [m]')
axes[0, 0].set_xticks([8, 8.5, 9, 9.5, 10])
axes[0, 0].invert_yaxis()
axes[0, 0].set_title('(a) Calibration 2021-06-01')

# Plot for 2022-07-01
axes[1, 1].scatter(data_2022_07_01, depths_prof, marker='o', color='k')
axes[1, 1].plot(do_glue_50_2022_07_01, depths_prof, marker='o', color='red')
axes[1, 1].fill_betweenx(depths_prof, do_glue_5_2022_07_01, do_glue_95_2022_07_01, color='red', alpha=0.4)
axes[1, 1].set_xlabel('DO [mg L$^{-1}$]')
axes[1, 1].set_ylabel('Depth [m]')
axes[1, 1].set_xticks([2, 3, 4, 5, 6])
axes[1, 1].invert_yaxis()
axes[1, 1].set_title('(d) Validation 2022-07-01')

# Plot for 2021-07-01
axes[1, 0].scatter(data_2021_07_01, depths_prof, marker='o', color='k')
axes[1, 0].plot(do_glue_50_2021_07_01, depths_prof, marker='o', color='red')
axes[1, 0].fill_betweenx(depths_prof, do_glue_5_2021_07_01, do_glue_95_2021_07_01, color='red', alpha=0.4)
axes[1, 0].set_xlabel('DO [mg L$^{-1}$]')
axes[1, 0].set_ylabel('Depth [m]')
axes[1, 0].set_xticks([2, 3, 4, 5, 6])
axes[1, 0].invert_yaxis()
axes[1, 0].set_title('(c) Calibration 2021-07-01')


# Create a single legend for the entire figure

fig.legend(['Obs', 'Median model', '5-95% model bound'], loc='lower center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=3)


# Adjust layout to prevent clipping of labels
plt.tight_layout()


# Save the combined plot as an image file (e.g., PNG, PDF, etc.)
plt.savefig('performace_profile_plots_2021_2022_fixedtheta_tempfromonsettodeephypoxia.png', bbox_inches='tight')



#%%plots of daily average variation and calibartion/validation profiles togther in one plot  


# Create a  2x4 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(30,  12))

# Plot for 2020_2021 calibration period
axes[0, 0].fill_between(filterd_df_model_2020.index.dayofyear, filterd_df_model_2020['5%'], filterd_df_model_2020['95%'], color='red', alpha=0.4, label='5-95% model bound')
axes[0, 0].plot(filterd_df_model_2020.index.dayofyear, filterd_df_model_2020['50%'], 'k--', label='Median model', alpha=0.9 )
axes[0, 0].scatter(filterd_df_obs_2020.index.unique().dayofyear, filterd_DO_obs_2D_2020, color='k', label='Obs')
axes[0, 0].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]' )#, fontsize= 14 )
#axes[0, 0].set_xlabel('Julian day' )#, fontsize= 14 )
#axes[0, 0].legend(loc='upper center')
axes[0,0].set_ylim([0 , 12.5])
axes[0, 0].set_title('(a) Calibration 2020 ')#, fontsize='32')
#axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].set_xlim([120 , 260])

# Plot for 2020_2021 calibration period
axes[0, 1].fill_between(filterd_df_model_2021.index.dayofyear, filterd_df_model_2021['5%'], filterd_df_model_2021['95%'], color='red', alpha=0.4)#, label='5-95% model bound'
axes[0, 1].plot(filterd_df_model_2021.index.dayofyear, filterd_df_model_2021['50%'], 'k--', alpha=0.9 )#, label='Median model'
axes[0, 1].scatter(filterd_df_obs_2021.index.unique().dayofyear, filterd_DO_obs_2D_2021, color='k')#, label='Obs'
#axes[0, 1].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]' , fontsize= 32 )
#axes[0, 1].legend(loc='upper center')
axes[0, 1].set_ylim([0 , 12.5])
axes[0, 1].set_title('(b) Calibration 2021 ')#, fontsize='32')
#axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].set_xlim([120 , 260])

# Plot for 2019 validation
axes[1, 0].fill_between(filterd_df_model_2019.index.dayofyear, filterd_df_model_2019['5%'], filterd_df_model_2019['95%'], color='red', alpha=0.4)#, label='5-95% model bound'
axes[1, 0].plot(filterd_df_model_2019.index.dayofyear, filterd_df_model_2019['50%'], 'k--', alpha=0.9 )#, label='Median model'
axes[1, 0].scatter(filterd_df_obs_2019.index.unique().dayofyear, filterd_DO_obs_2D_2019, color='k')#, label='Obs'
axes[1, 0].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]')# , fontsize= 14 )
#axes[1, 0].legend(loc='upper center')
axes[1, 0].set_ylim([0 , 12.5])
axes[1, 0].set_title('(c) Validation 2019 ')#, fontsize='32')
axes[1, 0].set_xlabel('Julian day' )
#axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].set_xlim([120 , 260])

# Plot for 2022 validation
axes[1, 1].fill_between(filterd_df_model_2022.index.dayofyear, filterd_df_model_2022['5%'], filterd_df_model_2022['95%'], color='red', alpha=0.4)#, label='5-95% model bound'
axes[1, 1].plot(filterd_df_model_2022.index.dayofyear, filterd_df_model_2022['50%'], 'k--',  alpha=0.9 )#,label='Median model'
axes[1, 1].scatter(filterd_df_obs_2022.index.unique().dayofyear, filterd_DO_obs_2D_2022, color='k')#, label='Obs'
#axes[1, 1].set_ylabel('Hypolimnetic DO average [g m$^{-3}$]' , fontsize= 32 )
#axes[1, 1].legend(loc='upper center')
axes[1, 1].set_xlabel('Julian day' )
axes[1, 1].set_title('(d) Validation 2022')#, fontsize='32')
axes[1, 1].set_ylim([0 , 12.5])
#axes[1 , 1].tick_params(axis='x', rotation=45)
axes[1, 1].set_xlim([120 , 260])

# First set of plots
axes[0,  2].scatter(data_2022_06_01, depths_prof, marker='o', color='k', label='Obs')
axes[0,  2].plot(do_glue_50_2022_06_01, depths_prof, marker='o', color='red', label='Median model')
axes[0,  2].fill_betweenx(depths_prof, do_glue_5_2022_06_01, do_glue_95_2022_06_01, color='red', alpha=0.4)
#axes[0,  2].set_xlabel('DO [g m$^{-3}$]')
axes[0,  2].set_ylabel('Depth [m]')
axes[0,  2].set_xticks([8,  8.5,  9,  9.5,  10])
axes[0,  2].invert_yaxis()
axes[0,  2].set_title('(e) Validation 2022-06-01')

axes[0,  3].scatter(data_2021_06_01, depths_prof, marker='o', color='k')
axes[0,  3].plot(do_glue_50_2021_06_01, depths_prof, marker='o', color='red')
axes[0,  3].fill_betweenx(depths_prof, do_glue_5_2021_06_01, do_glue_95_2021_06_01, color='red', alpha=0.4)
#axes[0,  3].set_xlabel('DO [g m$^{-3}$]')
axes[0,  3].set_ylabel('Depth [m]')
axes[0,  3].set_xticks([8,  8.5,  9,  9.5,  10])
axes[0,  3].invert_yaxis()
axes[0,  3].set_title('(f) Calibration 2021-06-01')

axes[1,  2].scatter(data_2022_07_01, depths_prof, marker='o', color='k')
axes[1,  2].plot(do_glue_50_2022_07_01, depths_prof, marker='o', color='red')
axes[1,  2].fill_betweenx(depths_prof, do_glue_5_2022_07_01, do_glue_95_2022_07_01, color='red', alpha=0.4)
axes[1,  2].set_xlabel('DO [g m$^{-3}$]')
axes[1,  2].set_ylabel('Depth [m]')
axes[1,  2].set_xticks([2,  3,  4,  5,  6])
axes[1,  2].invert_yaxis()
axes[1,  2].set_title('(g) Validation 2022-07-01')

axes[1,  3].scatter(data_2021_07_01, depths_prof, marker='o', color='k')
axes[1,  3].plot(do_glue_50_2021_07_01, depths_prof, marker='o', color='red')
axes[1,  3].fill_betweenx(depths_prof, do_glue_5_2021_07_01, do_glue_95_2021_07_01, color='red', alpha=0.4)
axes[1,  3].set_xlabel('DO [g m$^{-3}$]')
axes[1,  3].set_ylabel('Depth [m]')
axes[1,  3].set_xticks([2,  3,  4,  5,  6])
axes[1,  3].invert_yaxis()
axes[1,  3].set_title('(h) Calibration 2021-07-01')

# Adjust layout to add padding around each subplot
plt.subplots_adjust(left=0.05, bottom=0.01, right=0.95, top=0.9, wspace=0.3, hspace=0.3)


fig.legend(['5-95% model bound', 'Median','Obs' ], loc='lower center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=3, fontsize='25')


# Adjust layout to prevent clipping of labels
plt.tight_layout()


# Save the combined plot as an image file (e.g., PNG, PDF, etc.)
plt.savefig('performace_profile_plots_calib_vali_ave_daily.png', bbox_inches='tight')








#%%Old manusript with GLUE:















"""0.05 and 7 days
({'2018_1': {'A_day_before_strart_index': Timestamp('2018-05-12 00:00:00'),
   'end_index': Timestamp('2018-06-13 00:00:00'),
   'duration of stratification period': Timedelta('32 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 6.671372556959292,
   'DO_full_sat_day_before_onset': 12.2353441538835,
   'mean_SSI_full_str': SSI    122.8286
   dtype: float64,
   'variance_SSI_full_str': SSI    1829.051017
   dtype: float64,
   'std_SSI_full_str': SSI    42.767406
   dtype: float64,
   'mean_SSI_epi_str': SSI    104.229824
   dtype: float64,
   'variance_SSI_epi_str': SSI    1379.382594
   dtype: float64,
   'std_SSI_epi_str': SSI    37.14004
   dtype: float64,
   'mean_SI_full_str': SI_full    103971.898536
   dtype: float64,
   'variance_SI_full_str': SI_full    128.315002
   dtype: float64,
   'std_SI_full_str': SI_full    11.327621
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45574.862088
   dtype: float64,
   'variance_SI_epi_str': SI_epi    41.297597
   dtype: float64,
   'std_SI_epi_str': SI_epi    6.426321
   dtype: float64},
  '2018_2': {'A_day_before_strart_index': Timestamp('2018-06-20 00:00:00'),
   'end_index': Timestamp('2018-09-05 00:00:00'),
   'duration of stratification period': Timedelta('77 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 11.992754697116942,
   'DO_full_sat_day_before_onset': 10.779906688163914,
   'mean_SSI_full_str': SSI    111.906062
   dtype: float64,
   'variance_SSI_full_str': SSI    5532.174185
   dtype: float64,
   'std_SSI_full_str': SSI    74.378587
   dtype: float64,
   'mean_SSI_epi_str': SSI    85.753602
   dtype: float64,
   'variance_SSI_epi_str': SSI    4477.023135
   dtype: float64,
   'std_SSI_epi_str': SSI    66.910561
   dtype: float64,
   'mean_SI_full_str': SI_full    103898.172265
   dtype: float64,
   'variance_SI_full_str': SI_full    660.154594
   dtype: float64,
   'std_SI_full_str': SI_full    25.693474
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45536.553277
   dtype: float64,
   'variance_SI_epi_str': SI_epi    130.53396
   dtype: float64,
   'std_SI_epi_str': SI_epi    11.425146
   dtype: float64},
  '2019_1': {'A_day_before_strart_index': Timestamp('2019-06-02 00:00:00'),
   'end_index': Timestamp('2019-06-28 00:00:00'),
   'duration of stratification period': Timedelta('25 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 10.720450275348234,
   'DO_full_sat_day_before_onset': 11.09919463600633,
   'mean_SSI_full_str': SSI    63.317907
   dtype: float64,
   'variance_SSI_full_str': SSI    377.246325
   dtype: float64,
   'std_SSI_full_str': SSI    19.42283
   dtype: float64,
   'mean_SSI_epi_str': SSI    45.222788
   dtype: float64,
   'variance_SSI_epi_str': SSI    299.35761
   dtype: float64,
   'std_SSI_epi_str': SSI    17.301954
   dtype: float64,
   'mean_SI_full_str': SI_full    103935.093433
   dtype: float64,
   'variance_SI_full_str': SI_full    258.181431
   dtype: float64,
   'std_SI_full_str': SI_full    16.068025
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45555.632525
   dtype: float64,
   'variance_SI_epi_str': SI_epi    106.336917
   dtype: float64,
   'std_SI_epi_str': SI_epi    10.311979
   dtype: float64},
  '2019_2': {'A_day_before_strart_index': Timestamp('2019-07-17 00:00:00'),
   'end_index': Timestamp('2019-08-27 00:00:00'),
   'duration of stratification period': Timedelta('40 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 16.449014010366053,
   'DO_full_sat_day_before_onset': 9.779387017996175,
   'mean_SSI_full_str': SSI    57.479799
   dtype: float64,
   'variance_SSI_full_str': SSI    859.582447
   dtype: float64,
   'std_SSI_full_str': SSI    29.318637
   dtype: float64,
   'mean_SSI_epi_str': SSI    45.059291
   dtype: float64,
   'variance_SSI_epi_str': SSI    771.461896
   dtype: float64,
   'std_SSI_epi_str': SSI    27.775203
   dtype: float64,
   'mean_SI_full_str': SI_full    103879.212531
   dtype: float64,
   'variance_SI_full_str': SI_full    20.693551
   dtype: float64,
   'std_SI_full_str': SI_full    4.549016
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45534.572718
   dtype: float64,
   'variance_SI_epi_str': SI_epi    8.983171
   dtype: float64,
   'std_SI_epi_str': SI_epi    2.997194
   dtype: float64},
  '2020_1': {'A_day_before_strart_index': Timestamp('2020-05-26 00:00:00'),
   'end_index': Timestamp('2020-09-03 00:00:00'),
   'duration of stratification period': Timedelta('100 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 9.497663184321347,
   'DO_full_sat_day_before_onset': 11.422093541761889,
   'mean_SSI_full_str': SSI    127.355842
   dtype: float64,
   'variance_SSI_full_str': SSI    3319.801384
   dtype: float64,
   'std_SSI_full_str': SSI    57.617718
   dtype: float64,
   'mean_SSI_epi_str': SSI    101.103219
   dtype: float64,
   'variance_SSI_epi_str': SSI    2630.357363
   dtype: float64,
   'std_SSI_epi_str': SSI    51.28701
   dtype: float64,
   'mean_SI_full_str': SI_full    103933.080549
   dtype: float64,
   'variance_SI_full_str': SI_full    449.730956
   dtype: float64,
   'std_SI_full_str': SI_full    21.206861
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45554.365973
   dtype: float64,
   'variance_SI_epi_str': SI_epi    150.237602
   dtype: float64,
   'std_SI_epi_str': SI_epi    12.257145
   dtype: float64},
  '2021_1': {'A_day_before_strart_index': Timestamp('2021-05-29 00:00:00'),
   'end_index': Timestamp('2021-08-26 00:00:00'),
   'duration of stratification period': Timedelta('89 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 8.488165559874744,
   'DO_full_sat_day_before_onset': 11.7013604513593,
   'mean_SSI_full_str': SSI    186.653401
   dtype: float64,
   'variance_SSI_full_str': SSI    5428.443413
   dtype: float64,
   'std_SSI_full_str': SSI    73.677971
   dtype: float64,
   'mean_SSI_epi_str': SSI    156.080971
   dtype: float64,
   'variance_SSI_epi_str': SSI    4306.493318
   dtype: float64,
   'std_SSI_epi_str': SSI    65.623878
   dtype: float64,
   'mean_SI_full_str': SI_full    103936.515536
   dtype: float64,
   'variance_SI_full_str': SI_full    276.892577
   dtype: float64,
   'std_SI_full_str': SI_full    16.640089
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45555.606998
   dtype: float64,
   'variance_SI_epi_str': SI_epi    90.634594
   dtype: float64,
   'std_SI_epi_str': SI_epi    9.52022
   dtype: float64},
  '2022_1': {'A_day_before_strart_index': Timestamp('2022-06-03 00:00:00'),
   'end_index': Timestamp('2022-08-30 00:00:00'),
   'duration of stratification period': Timedelta('88 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 11.47261405355793,
   'DO_full_sat_day_before_onset': 10.908458841504888,
   'mean_SSI_full_str': SSI    114.08853
   dtype: float64,
   'variance_SSI_full_str': SSI    1709.480768
   dtype: float64,
   'std_SSI_full_str': SSI    41.345868
   dtype: float64,
   'mean_SSI_epi_str': SSI    88.070212
   dtype: float64,
   'variance_SSI_epi_str': SSI    1327.082879
   dtype: float64,
   'std_SSI_epi_str': SSI    36.429149
   dtype: float64,
   'mean_SI_full_str': SI_full    103912.102764
   dtype: float64,
   'variance_SI_full_str': SI_full    324.816805
   dtype: float64,
   'std_SI_full_str': SI_full    18.022675
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45544.720601
   dtype: float64,
   'variance_SI_epi_str': SI_epi    105.533757
   dtype: float64,
   'std_SI_epi_str': SI_epi    10.272962
   dtype: float64}},
 'df_str_2022_1_14')


"""
deoygenation_duration_calival=[(2019, 65) , (2020, 99) , (2021 , 88) , (2022, 87)]
# without the data of year 2018
filtered_data = dens_diff_top_135[dens_diff_top_135.index.year != 2018]   
find_dod_periods_densdiff(filtered_data, threshold=-0.2, concequetive_day=7)    
"""   
(({'2019_1': {'A_day_before_strart_index': Timestamp('2019-05-14 00:00:00'),#117.091916
   'end_index': Timestamp('2019-06-30 00:00:00'),
   'duration of stratification period': Timedelta('47 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 8.30642938127632,
   'DO_full_sat_day_before_onset': 11.752915115399531,
   'mean_SSI_full_str': SSI    53.119384
   dtype: float64,
   'variance_SSI_full_str': SSI    664.165802
   dtype: float64,
   'std_SSI_full_str': SSI    25.771414
   dtype: float64,
   'mean_SSI_epi_str': SSI    39.304517
   dtype: float64,
   'variance_SSI_epi_str': SSI    446.234451
   dtype: float64,
   'std_SSI_epi_str': SSI    21.124262
   dtype: float64,
   'mean_SI_full_str': SI_full    103952.117296
   dtype: float64,
   'variance_SI_full_str': SI_full    698.184254
   dtype: float64,
   'std_SI_full_str': SI_full    26.423176
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45565.280389
   dtype: float64,
   'variance_SI_epi_str': SI_epi    235.807314
   dtype: float64,
   'std_SI_epi_str': SI_epi    15.356019
   dtype: float64},
  '2019_2': {'A_day_before_strart_index': Timestamp('2019-07-11 00:00:00'),
   'end_index': Timestamp('2019-08-30 00:00:00'),
   'duration of stratification period': Timedelta('50 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 16.41464542166073,
   'DO_full_sat_day_before_onset': 9.786472668365272,
   'mean_SSI_full_str': SSI    51.53901
   dtype: float64,
   'variance_SSI_full_str': SSI    924.054707
   dtype: float64,
   'std_SSI_full_str': SSI    30.398268
   dtype: float64,
   'mean_SSI_epi_str': SSI    40.16335
   dtype: float64,
   'variance_SSI_epi_str': SSI    777.29663
   dtype: float64,
   'std_SSI_epi_str': SSI    27.88004
   dtype: float64,
   'mean_SI_full_str': SI_full    103880.438023
   dtype: float64,
   'variance_SI_full_str': SI_full    37.603067
   dtype: float64,
   'std_SI_full_str': SI_full    6.132134
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45535.315213
   dtype: float64,
   'variance_SI_epi_str': SI_epi    17.472112
   dtype: float64,
   'std_SI_epi_str': SI_epi    4.179966
   dtype: float64},
  '2020_1': {'A_day_before_strart_index': Timestamp('2020-05-21 00:00:00'),
   'end_index': Timestamp('2020-09-03 00:00:00'),
   'duration of stratification period': Timedelta('105 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 9.02348490983695,
   'DO_full_sat_day_before_onset': 11.551791647447587,
   'mean_SSI_full_str': SSI    121.888005
   dtype: float64,
   'variance_SSI_full_str': SSI    3760.936371
   dtype: float64,
   'std_SSI_full_str': SSI    61.326474
   dtype: float64,
   'mean_SSI_epi_str': SSI    96.768589
   dtype: float64,
   'variance_SSI_epi_str': SSI    2881.90043
   dtype: float64,
   'std_SSI_epi_str': SSI    53.683335
   dtype: float64,
   'mean_SI_full_str': SI_full    103935.583306
   dtype: float64,
   'variance_SI_full_str': SI_full    553.92269
   dtype: float64,
   'std_SI_full_str': SI_full    23.535562
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45555.841571
   dtype: float64,
   'variance_SI_epi_str': SI_epi    186.724464
   dtype: float64,
   'std_SI_epi_str': SI_epi    13.664716
   dtype: float64},
  '2021_1': {'A_day_before_strart_index': Timestamp('2021-05-12 00:00:00'),
   'end_index': Timestamp('2021-08-27 00:00:00'),
   'duration of stratification period': Timedelta('107 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 6.633627847964584,
   'DO_full_sat_day_before_onset': 12.246891602462926,
   'mean_SSI_full_str': SSI    160.528654
   dtype: float64,
   'variance_SSI_full_str': SSI    7960.616731
   dtype: float64,
   'std_SSI_full_str': SSI    89.222288
   dtype: float64,
   'mean_SSI_epi_str': SSI    134.220868
   dtype: float64,
   'variance_SSI_epi_str': SSI    5997.000482
   dtype: float64,
   'std_SSI_epi_str': SSI    77.440303
   dtype: float64,
   'mean_SI_full_str': SI_full    103945.611773
   dtype: float64,
   'variance_SI_full_str': SI_full    663.609712
   dtype: float64,
   'std_SI_full_str': SI_full    25.760623
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45560.825705
   dtype: float64,
   'variance_SI_epi_str': SI_epi    216.962467
   dtype: float64,
   'std_SI_epi_str': SI_epi    14.729646
   dtype: float64},
  '2022_1': {'A_day_before_strart_index': Timestamp('2022-05-22 00:00:00'),
   'end_index': Timestamp('2022-08-31 00:00:00'),
   'duration of stratification period': Timedelta('101 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 10.63836005830904,
   'DO_full_sat_day_before_onset': 11.120366792046608,
   'mean_SSI_full_str': SSI    101.902138
   dtype: float64,
   'variance_SSI_full_str': SSI    2500.806167
   dtype: float64,
   'std_SSI_full_str': SSI    50.008061
   dtype: float64,
   'mean_SSI_epi_str': SSI    78.434275
   dtype: float64,
   'variance_SSI_epi_str': SSI    1787.187045
   dtype: float64,
   'std_SSI_epi_str': SSI    42.275135
   dtype: float64,
   'mean_SI_full_str': SI_full    103918.573956
   dtype: float64,
   'variance_SI_full_str': SI_full    614.664752
   dtype: float64,
   'std_SI_full_str': SI_full    24.792433
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45548.384097
   dtype: float64,
   'variance_SI_epi_str': SI_epi    198.822625
   dtype: float64,
   'std_SI_epi_str': SI_epi    14.100448
   dtype: float64}},
 'df_str_2022_1_14')
"""

#After on if needed few more analyses could be added 


# find it in excel named: 'satartification_with_density_or_SSI_2018_2022.xlsx'



#%%testing different threshold and concequetive day 
find_dod_periods_densdiff (dens_diff_top_135 , threshold=-0.05, concequetive_day=7)

2018_1': {'A_day_before_strart_index': Timestamp('2018-05-08 00:00:00'),#127.2455448

   'end_index': Timestamp('2018-09-05 00:00:00'),

'2019_1': {'A_day_before_strart_index': Timestamp('2019-05-11 00:00:00'),
  'end_index': Timestamp('2019-07-01 00:00:00'),

'2019_2': {'A_day_before_strart_index': Timestamp('2019-07-11 00:00:00'),
 'end_index': Timestamp('2019-08-30 00:00:00'),

  '2020_1': {'A_day_before_strart_index': Timestamp('2020-05-20 00:00:00'),#91.36189556

  'end_index': Timestamp('2020-09-03 00:00:00'),

  '2021_1': {'A_day_before_strart_index': Timestamp('2021-05-10 00:00:00'),#98.50387277

   'end_index': Timestamp('2021-08-27 00:00:00'),
  '2022_1': {'A_day_before_strart_index': Timestamp('2022-05-21 00:00:00'),# 101.3671003

   'end_index': Timestamp('2022-09-06 00:00:00'),
#%%the result of  threshold=-0.025, concequetive_day=7
#find_dod_periods_densdiff (dens_diff_top_135 , threshold=-0.025, concequetive_day=7)
Out[707]: 
({'2018_1': {'A_day_before_strart_index': Timestamp('2018-05-08 00:00:00'),
   'end_index': Timestamp('2018-09-05 00:00:00'),
   'duration of stratification period': Timedelta('120 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 6.430899650865637,
   'DO_full_sat_day_before_onset': 12.309243070316194,
   'mean_SSI_full_str': SSI    112.101206
   dtype: float64,
   'variance_SSI_full_str': SSI    4512.716737
   dtype: float64,
   'std_SSI_full_str': SSI    67.176757
   dtype: float64,
   'mean_SSI_epi_str': SSI    88.735639
   dtype: float64,
   'variance_SSI_epi_str': SSI    3626.046534
   dtype: float64,
   'std_SSI_epi_str': SSI    60.216663
   dtype: float64,
   'mean_SI_full_str': SI_full    103924.270418
   dtype: float64,
   'variance_SI_full_str': SI_full    1740.964148
   dtype: float64,
   'std_SI_full_str': SI_full    41.724862
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45549.993672
   dtype: float64,
   'variance_SI_epi_str': SI_epi    445.110034
   dtype: float64,
   'std_SI_epi_str': SI_epi    21.097631
   dtype: float64},
  '2019_1': {'A_day_before_strart_index': Timestamp('2019-05-10 00:00:00'),
   'end_index': Timestamp('2019-07-01 00:00:00'),
   'duration of stratification period': Timedelta('52 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 8.061209642587194,
   'DO_full_sat_day_before_onset': 11.823115577991738,
   'mean_SSI_full_str': SSI    49.546811
   dtype: float64,
   'variance_SSI_full_str': SSI    758.518499
   dtype: float64,
   'std_SSI_full_str': SSI    27.541215
   dtype: float64,
   'mean_SSI_epi_str': SSI    36.581077
   dtype: float64,
   'variance_SSI_epi_str': SSI    486.880271
   dtype: float64,
   'std_SSI_epi_str': SSI    22.065364
   dtype: float64,
   'mean_SI_full_str': SI_full    103954.543454
   dtype: float64,
   'variance_SI_full_str': SI_full    804.187366
   dtype: float64,
   'std_SI_full_str': SI_full    28.358198
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45566.688119
   dtype: float64,
   'variance_SI_epi_str': SI_epi    271.235303
   dtype: float64,
   'std_SI_epi_str': SI_epi    16.469223
   dtype: float64},
  '2019_2': {'A_day_before_strart_index': Timestamp('2019-07-09 00:00:00'),
   'end_index': Timestamp('2019-08-30 00:00:00'),
   'duration of stratification period': Timedelta('52 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 15.954165856818918,
   'DO_full_sat_day_before_onset': 9.88228711203726,
   'mean_SSI_full_str': SSI    49.746618
   dtype: float64,
   'variance_SSI_full_str': SSI    968.855452
   dtype: float64,
   'std_SSI_full_str': SSI    31.126443
   dtype: float64,
   'mean_SSI_epi_str': SSI    38.699166
   dtype: float64,
   'variance_SSI_epi_str': SSI    801.002498
   dtype: float64,
   'std_SSI_epi_str': SSI    28.301988
   dtype: float64,
   'mean_SI_full_str': SI_full    103881.00614
   dtype: float64,
   'variance_SI_full_str': SI_full    44.341778
   dtype: float64,
   'std_SI_full_str': SI_full    6.658962
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45535.667271
   dtype: float64,
   'variance_SI_epi_str': SI_epi    19.904162
   dtype: float64,
   'std_SI_epi_str': SI_epi    4.461408
   dtype: float64},
  '2020_1': {'A_day_before_strart_index': Timestamp('2020-05-19 00:00:00'),
   'end_index': Timestamp('2020-09-03 00:00:00'),
   'duration of stratification period': Timedelta('107 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 8.96445419261179,
   'DO_full_sat_day_before_onset': 11.56811939241706,
   'mean_SSI_full_str': SSI    119.687895
   dtype: float64,
   'variance_SSI_full_str': SSI    3944.79541
   dtype: float64,
   'std_SSI_full_str': SSI    62.807606
   dtype: float64,
   'mean_SSI_epi_str': SSI    95.016179
   dtype: float64,
   'variance_SSI_epi_str': SSI    2989.285078
   dtype: float64,
   'std_SSI_epi_str': SSI    54.674355
   dtype: float64,
   'mean_SI_full_str': SI_full    103936.571406
   dtype: float64,
   'variance_SI_full_str': SI_full    594.827284
   dtype: float64,
   'std_SI_full_str': SI_full    24.389081
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45556.424542
   dtype: float64,
   'variance_SI_epi_str': SI_epi    201.07685
   dtype: float64,
   'std_SI_epi_str': SI_epi    14.180157
   dtype: float64},
  '2021_1': {'A_day_before_strart_index': Timestamp('2021-05-10 00:00:00'),
   'end_index': Timestamp('2021-08-27 00:00:00'),
   'duration of stratification period': Timedelta('109 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 6.64506168340352,
   'DO_full_sat_day_before_onset': 12.243391560238605,
   'mean_SSI_full_str': SSI    157.646631
   dtype: float64,
   'variance_SSI_full_str': SSI    8258.933247
   dtype: float64,
   'std_SSI_full_str': SSI    90.878673
   dtype: float64,
   'mean_SSI_epi_str': SSI    131.80927
   dtype: float64,
   'variance_SSI_epi_str': SSI    6198.113604
   dtype: float64,
   'std_SSI_epi_str': SSI    78.728099
   dtype: float64,
   'mean_SI_full_str': SI_full    103946.670041
   dtype: float64,
   'variance_SI_full_str': SI_full    711.349672
   dtype: float64,
   'std_SI_full_str': SI_full    26.671139
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45561.431197
   dtype: float64,
   'variance_SI_epi_str': SI_epi    232.595945
   dtype: float64,
   'std_SI_epi_str': SI_epi    15.251097
   dtype: float64},
  '2022_1': {'A_day_before_strart_index': Timestamp('2022-05-21 00:00:00'),
   'end_index': Timestamp('2022-09-07 00:00:00'),
   'duration of stratification period': Timedelta('109 days 00:00:00'),
   'temp_hypo_ave_on_day_before_onset': 10.494206754130223,
   'DO_full_sat_day_before_onset': 11.15771837896792,
   'mean_SSI_full_str': SSI    95.620211
   dtype: float64,
   'variance_SSI_full_str': SSI    2818.681439
   dtype: float64,
   'std_SSI_full_str': SSI    53.091256
   dtype: float64,
   'mean_SSI_epi_str': SSI    73.000133
   dtype: float64,
   'variance_SSI_epi_str': SSI    2029.219904
   dtype: float64,
   'std_SSI_epi_str': SSI    45.046863
   dtype: float64,
   'mean_SI_full_str': SI_full    103918.043764
   dtype: float64,
   'variance_SI_full_str': SI_full    615.751421
   dtype: float64,
   'std_SI_full_str': SI_full    24.814339
   dtype: float64,
   'mean_SI_epi_str': SI_epi    45548.120129
   dtype: float64,
   'variance_SI_epi_str': SI_epi    199.59501
   dtype: float64,
   'std_SI_epi_str': SI_epi    14.12781
   dtype: float64}},
 'df_str_2022_1_14')

"""

#%% add density difference analyse:
   
"""    
diff_density_top_bottom=density_2D_full_2018_2022[: , 32]   - density_2D_full_2018_2022[: , 0] 
    
diff_density_top_epi =density_2D_epi_2018_2022[: , 25] -   density_2D_epi_2018_2022[: , 0] 
    
    
SSI_full_sat_hypo_2018_2022['diff_density_top_bottom']= diff_density_top_bottom 
SSI_full_sat_hypo_2018_2022['diff_density_top_epi']= diff_density_top_epi     
    


density_bottom_2018_2022= density_2D_full_2018_2022[: , 32]
density_epi_2018_2022= density_2D_epi_2018_2022[: , 25]

N2_top_bottom_2018_2022=9.81*diff_density_top_bottom/(density_bottom_2018_2022*17.75)
N2_epi_bottom_2018_2022=9.81*diff_density_top_epi/(density_epi_2018_2022*17.75)
"""
#%%stratification SSI

"""
def find_stratification_periods_SSI(SSI_daily_epi_2018_2022_indexed ,SSI_daily_full_2018_2022_indexed ):

    
    subset_indices = {}
   

    #hypo_sat_ave = df[df['Z_m'] < -13.5].groupby('Datetime')['DO_sat'].mean()
    #hypo_sat_ave = (df[df['Z_m'] < -13.5].groupby('Datetime').apply(lambda x: np.average(x['DO_sat'], weights=x['V_r_m']))).rename('Volume Weighted Average')
    #hypo_sat_ave.index =pd.to_datetime(SSI_top_to_135_indexed.index)
    
    
        
    for year in range(SSI_daily_epi_2018_2022_indexed.index.year.min(), SSI_daily_epi_2018_2022_indexed.index.year.max()+1):
        year_data = SSI_daily_epi_2018_2022_indexed.loc[SSI_daily_epi_2018_2022_indexed.index.year == year]
        consecutive_true5 = (year_data > 30).rolling(window=5, min_periods=5, center=False).sum() == 5
        consecutive_true5=consecutive_true5.shift(-5)# the last 5 values in the new series will be NaN
        
        diffs = consecutive_true5.diff()
        
        starts = diffs.where((diffs == 1))
        starts = starts.dropna()
        
        ends = diffs.where((diffs == -1))
        ends = ends.dropna()
        
        if len(starts)==0:
            starts= diffs[diffs.index== diffs.index.min() ]
        
        if len(ends)==0:
            ends= diffs[diffs.index== diffs.index.max() ]
        
        length= (ends.index- starts.index).days
        
        starts= starts[length> 10] 
        ends= ends[length> 10]
        
        for i, (start_index, end_index) in enumerate(zip(starts.index, ends.index)):
               
               # change the mixing day to the last available day before onset of deoxygenation 
               #latest_date = df[df['Datetime'] < start_index]['Datetime'].max()
               
               
               year_subset= SSI_daily_epi_2018_2022_indexed.loc[ start_index: end_index]#- pd.Timedelta(days=1) 
               #year_subset=year_subset.reset_index(drop=True)
               ave_SSI_top_to_bottom_str= SSI_daily_epi_2018_2022_indexed[ start_index+ pd.Timedelta(days=1) :end_index].mean()
               ave_SSI_top_to_135_str=SSI_daily_epi_2018_2022_indexed[ start_index+ pd.Timedelta(days=1) :end_index].mean()
                 
                           
               var_name = f'df_str_{year}_{i+1}_14'# next time make str to deoxy
               globals()[var_name] = year_subset
               subset_name = f"{year}_{i+1}"# 
               subset_indices[subset_name] = {'A_day_before_strart_index': start_index,
                                              'end_index': end_index  , 
                                              'duration of stratification period' : end_index-(start_index+ pd.Timedelta(days=1) ),
                                              'ave_SSI_top_to_bottom_str': ave_SSI_top_to_bottom_str,
                                              'ave_SSI_top_to_135_str' : ave_SSI_top_to_135_str}
               
               
    return subset_indices, var_name  
""" 
#%%
"""
daily_prof_Temp_DO_morpho_5years= pd.concat ([ daily_prof_Temp_DO_morpho_2018  ,  daily_prof_Temp_DO_morpho_2019,
            daily_prof_Temp_DO_morpho_2020 , daily_prof_Temp_DO_morpho_2021, 
            daily_prof_Temp_DO_morpho_2022])


daily_prof_Temp_DO_morpho_5years= daily_prof_Temp_DO_morpho_5years.set_index (['Datetime'])
"""
       
        
#%%stratification density difference_SSI_
"""  
SSI_full_sat_hypo_2018_2022['diff_density_top_epi']    
    
    
    
def find_stratification_periods_densitydiff(SSI_full_sat_hypo_2018_2022):
    
    
    subset_indices = {}
   
    
    diff_density_top_to_135_indexed = SSI_full_sat_hypo_2018_2022['diff_density_top_epi']

    #hypo_sat_ave = SSI_full_sat_hypo_2018_2022['DO_sat_ave_hypo_daily']
   
    
        
    for year in range(SSI_full_sat_hypo_2018_2022.index.year.min(), SSI_full_sat_hypo_2018_2022.index.year.max()+1):
        year_data = SSI_full_sat_hypo_2018_2022.loc[SSI_full_sat_hypo_2018_2022.index.year == year].diff_density_top_epi
        consecutive_true5 = (year_data >= 0.01).rolling(window=5, min_periods=5, center=False).sum() == 5
        consecutive_true5=consecutive_true5.shift(-5)# the last 5 values in the new series will be NaN
        
        diffs = consecutive_true5.diff()
        
        starts = diffs.where((diffs == 1))
        starts = starts.dropna()
        
        ends = diffs.where((diffs == -1))
        ends = ends.dropna()
        
        if len(starts)==0:
            starts= diffs[diffs.index== diffs.index.min() ]
        
        if len(ends)==0:
            ends= diffs[diffs.index== diffs.index.max() ]
        
        length= (ends.index- starts.index).days
        
        starts= starts[length> 10] 
        ends= ends[length> 10]
        
        for i, (start_index, end_index) in enumerate(zip(starts.index, ends.index)):
               
               # change the mixing day to the last available day before onset of deoxygenation 
               #latest_date = df[df['Datetime'] < start_index]['Datetime'].max()
               
               year_subset= daily_prof_Temp_DO_morpho_5years.loc[ start_index: end_index]#- pd.Timedelta(days=1) 
               
               index_subst=SSI_full_sat_hypo_2018_2022.loc[ start_index: end_index]#.DO_sat_ave_hypo_daily 
               
                           
               var_name = f'df_str_{year}_{i+1}_14'# next time make str to deoxy
               globals()[var_name] = year_subset
               subset_name = f"{year}_{i+1}"# 
               subset_indices[subset_name] = {'A_day_before_strart_index': start_index,
                                              'end_index': end_index  , 
                                              'duration of stratification period' : end_index-(start_index+ pd.Timedelta(days=1) ),
                                              'ave_hypo_sat_onset': index_subst['DO_sat_ave_hypo_daily'][0],
                                              'ave_hypo_sat_offset': index_subst['DO_sat_ave_hypo_daily'][-1]
                                              }
                                              
               
               
    return subset_indices, var_name  
            
"""      
    
#%%subset_indices:
   
# thrershold of 0.01 Kg/m3    
     
find_stratification_periods_densitydiff(SSI_full_sat_hypo_2018_2022)    
    
"""     #0.01    
({'2018_1': {'A_day_before_strart_index': Timestamp('2018-05-08 00:00:00'),
   'end_index': Timestamp('2018-09-07 00:00:00'),
   'duration of stratification period': Timedelta('121 days 00:00:00'),
   'ave_hypo_sat_onset': 125.62179534247562,
   'ave_hypo_sat_offset': 5.682218375445416},
  '2019_1': {'A_day_before_strart_index': Timestamp('2019-05-09 00:00:00'),
   'end_index': Timestamp('2019-07-04 00:00:00'),
   'duration of stratification period': Timedelta('55 days 00:00:00'),
   'ave_hypo_sat_onset': 100.368025186265,
   'ave_hypo_sat_offset': 33.52360058309038},
  '2019_2': {'A_day_before_strart_index': Timestamp('2019-07-09 00:00:00'),
   'end_index': Timestamp('2019-09-01 00:00:00'),
   'duration of stratification period': Timedelta('53 days 00:00:00'),
   'ave_hypo_sat_onset': 66.6425577691394,
   'ave_hypo_sat_offset': 11.039411645610626},
  '2020_1': {'A_day_before_strart_index': Timestamp('2020-05-17 00:00:00'),
   'end_index': Timestamp('2020-09-05 00:00:00'),
   'duration of stratification period': Timedelta('110 days 00:00:00'),
   'ave_hypo_sat_onset': 95.67782393909945,
   'ave_hypo_sat_offset': 8.269483587085627},
  '2021_1': {'A_day_before_strart_index': Timestamp('2021-05-10 00:00:00'),
   'end_index': Timestamp('2021-08-29 00:00:00'),
   'duration of stratification period': Timedelta('110 days 00:00:00'),
   'ave_hypo_sat_onset': 98.8026912590433,
   'ave_hypo_sat_offset': 9.534698601662889},
  '2022_1': {'A_day_before_strart_index': Timestamp('2022-05-18 00:00:00'),
   'end_index': Timestamp('2022-09-09 00:00:00'),
   'duration of stratification period': Timedelta('113 days 00:00:00'),
   'ave_hypo_sat_onset': 108.56157704351583,
   'ave_hypo_sat_offset': 23.449546620235395}},
 'df_str_2022_1_14')
"""   




"""
({'2018_1': {'A_day_before_strart_index': Timestamp('2018-05-08 00:00:00'),
   'end_index': Timestamp('2018-09-07 00:00:00'),
   'duration of stratification period': Timedelta('121 days 00:00:00'),
   'ave_hypo_sat_onset': 125.62179534247562,
   'ave_hypo_sat_offset': 5.682218375445416},
  '2019_1': {'A_day_before_strart_index': Timestamp('2019-06-01 00:00:00'),
   'end_index': Timestamp('2019-06-30 00:00:00'),
   'duration of stratification period': Timedelta('28 days 00:00:00'),
   'ave_hypo_sat_onset': 83.99111327070511,
   'ave_hypo_sat_offset': 33.32747481759144},
  '2019_2': {'A_day_before_strart_index': Timestamp('2019-07-16 00:00:00'),
   'end_index': Timestamp('2019-08-29 00:00:00'),
   'duration of stratification period': Timedelta('43 days 00:00:00'),
   'ave_hypo_sat_onset': 77.73053139509771,
   'ave_hypo_sat_offset': 7.266491874527588},
  '2020_1': {'A_day_before_strart_index': Timestamp('2020-05-23 00:00:00'),
   'end_index': Timestamp('2020-09-05 00:00:00'),
   'duration of stratification period': Timedelta('104 days 00:00:00'),
   'ave_hypo_sat_onset': 85.20305879494656,
   'ave_hypo_sat_offset': 8.269483587085627},
  '2021_1': {'A_day_before_strart_index': Timestamp('2021-05-27 00:00:00'),
   'end_index': Timestamp('2021-08-29 00:00:00'),
   'duration of stratification period': Timedelta('93 days 00:00:00'),
   'ave_hypo_sat_onset': 89.98253239390995,
   'ave_hypo_sat_offset': 9.534698601662889},
  '2022_1': {'A_day_before_strart_index': Timestamp('2022-05-23 00:00:00'),
   'end_index': Timestamp('2022-09-02 00:00:00'),
   'duration of stratification period': Timedelta('101 days 00:00:00'),
   'ave_hypo_sat_onset': 102.02348113054747,
   'ave_hypo_sat_offset': 12.679855307202248}},
 'df_str_2022_1_14')
"""


"""#0.05

({'2018_1': {'A_day_before_strart_index': Timestamp('2018-05-08 00:00:00'),
   'end_index': Timestamp('2018-09-07 00:00:00'),
   'duration of stratification period': Timedelta('121 days 00:00:00'),
   'ave_hypo_sat_onset': 125.62179534247562,
   'ave_hypo_sat_offset': 5.682218375445416},
  '2019_1': {'A_day_before_strart_index': Timestamp('2019-05-14 00:00:00'),
   'end_index': Timestamp('2019-07-02 00:00:00'),
   'duration of stratification period': Timedelta('48 days 00:00:00'),
   'ave_hypo_sat_onset': 96.29262390670554,
   'ave_hypo_sat_offset': 42.357214123744725},
  '2019_2': {'A_day_before_strart_index': Timestamp('2019-07-11 00:00:00'),
   'end_index': Timestamp('2019-09-01 00:00:00'),
   'duration of stratification period': Timedelta('51 days 00:00:00'),
   'ave_hypo_sat_onset': 81.98801641291438,
   'ave_hypo_sat_offset': 11.039411645610626},
  '2020_1': {'A_day_before_strart_index': Timestamp('2020-05-21 00:00:00'),
   'end_index': Timestamp('2020-09-05 00:00:00'),
   'duration of stratification period': Timedelta('106 days 00:00:00'),
   'ave_hypo_sat_onset': 89.9450435968038,
   'ave_hypo_sat_offset': 8.269483587085627},
  '2021_1': {'A_day_before_strart_index': Timestamp('2021-05-12 00:00:00'),
   'end_index': Timestamp('2021-08-29 00:00:00'),
   'duration of stratification period': Timedelta('108 days 00:00:00'),
   'ave_hypo_sat_onset': 94.52078217795054,
   'ave_hypo_sat_offset': 9.534698601662889},
  '2022_1': {'A_day_before_strart_index': Timestamp('2022-05-22 00:00:00'),
   'end_index': Timestamp('2022-09-02 00:00:00'),
   'duration of stratification period': Timedelta('102 days 00:00:00'),
   'ave_hypo_sat_onset': 103.63556122448979,
   'ave_hypo_sat_offset': 12.679855307202248}},
 'df_str_2022_1_14')
"""
"""  



#%%splitting years for calibration and validation

According Ana s paper the stroger stratification periods have lower error good for calibrtion  
threshod of 3500 J/m2 for ave_SSI_top_to_135_str
large numbers (Validation): [4633, 3599] =>  [2021 , 2020 ] ->1.53 prof andx average  
Small numbers (Calibration ): [2862, 1400, 3257] =>   [2019 , 2018, 2022 ]-> error 1.12 rmse prof


2018: medium  (3500>>3000) 
2019: Light  (<3000)
2020: strong (>3000)

2021: storng (>3000)
2022: light  (<3000)
    
#Results according to this comparstion we can declear that for both 
#validation and calibration we have storng and light stratification
# : calibrasation :2018-2020 and validation of 2021 ,and 2022C_2018_2020_2022


df_str_2018_1_below14.N2.mean()*10**4
Out[102]: 3.5469403304826623

df_str_2019_1_below14.N2.mean()*10**4
Out[96]: 3.133525052237382

df_str_2019_2_below14.N2.mean()*10**4
Out[95]: 2.9014310999738813

df_str_2020_1_below14.N2.mean()*10**4
Out[97]: 1.4063809608524527
##stability numbers
df_str_2021_1_below14.N2.mean()*10**4
Out[99]: 0.8775486487962024

df_str_2022_1_below14.N2.mean()*10**4
Out[98]: 2.347779259284746


#% N2>10**-4
sum(df_str_2018_1_below14.N2>10**-4) , sum(df_str_2018_1_below14.N2>10**-4)*100/len(df_str_2018_1_below14.N2)
Out[140]: (620, 72)


sum(df_str_2019_below14.N2>10**-4) , sum(df_str_2019_below14.N2>10**-4)*100/len(df_str_2019_below14.N2)
Out[134]: (557, 71)


sum(df_str_2020_1_below14.N2>10**-4) , sum(df_str_2020_1_below14.N2>10**-4)*100/len(df_str_2020_1_below14.N2)
Out[122]: (421, 53)


sum(df_str_2021_1_below14.N2>10**-4) , sum(df_str_2021_1_below14.N2>10**-4)*100/len(df_str_2021_1_below14.N2)
Out[120]: 267 , 34%


sum(df_str_2022_1_below14.N2>10**-4) , sum(df_str_2022_1_below14.N2>10**-4)*100/len(df_str_2022_1_below14.N2)

Out[121]: 606 , 75%




#%%this function also works for dataframe with several years:
    


#commented because startification period selection were updated with density diff        
#find_stratification_periods(daily_prof_Temp_DO_morpho_5years)     


# Assuming SSI_top_to_135_5years_data is your NumPy array data
#SSI_top_to_135_5years_data=calculate_SSI_top_to_135_daily(daily_prof_Temp_DO_morpho_5years)



#%%apply the function of two D temp with one loop 

# Define the list of years
years = ['2018_1', '2019_1', '2019_2', '2020_1', '2021_1', '2022_1']

# Initialize dictionaries to store the results
temp_daily_2D = {}
temp_daily_2D_below135 = {}

# Apply the function for each year
for year in years:
    # Remove 'Datetime' column from the dataframe
    df = globals()['df_str_' + year + '_14'].drop('Datetime', axis=1)
    
    # Apply the function for all values and values below -13
    temp_daily_2D[year] = two_D_array_from_df(df, values_name='Temp', index_name='Datetime')
    temp_daily_2D_below135[year] = two_D_array_from_df(df[df['Z_m'] < -13], values_name='Temp', index_name='Datetime')




#%%calculation of kz_bv with the old method


def updated_daily_df_str_kz_bv(df_str_y_n, g=9.81838509231682, A0=23.67, kz_min=1.4*10**-7):

    if 'Datetime' in df_str_y_n.columns:

        daily_date = df_str_y_n['Datetime'].unique()

    elif 'Datetime_start' in df_str_y_n.columns:

        daily_date = df_str_y_n['Datetime_start'].unique()

    dz_d = np.array([])  # downward dz-for bv method dz
    dz_u = np.array([])  # upward dz -for jp method
    # har ki ba balaeish faghat sath zero no bala
    density_diff_down_daily = np.array([])

    for i in daily_date:

        density_each_day = np.array(
            df_str_y_n[df_str_y_n['Datetime'] == i]['density2'])

    #density_each_day= df_str_y_n. groupby('Datetime') ['Density2'].apply(np.array)

        for j in range(len(density_each_day)):  # for kz in upper boundry of each layer
            if j == 0:
                density_column_2 = 0

            else:

                density_column_2 = (
                    density_each_day[j] - density_each_day[j-1])

            density_diff_down_daily = np.append(
                density_diff_down_daily, density_column_2)

        Z_m = np.array(df_str_y_n[df_str_y_n['Datetime'] == i]['Z_m'])

        for k in range(len(Z_m)):  # har ki ba balaeish faghat sath zero no bala

            if k == len(Z_m)-1:
                Z_m_column_d = np.nan

            else:
                Z_m_column_d = Z_m[k] - Z_m[k+1]

            if k == 0:
                Z_m_column_u = np.nan
            else:
                Z_m_column_u = (Z_m[k-1] - Z_m[k])

            dz_d = np.append(dz_d, Z_m_column_d)
            dz_u = np.append(dz_u, Z_m_column_u)

    df_str_y_n['dZ_m_down'] = dz_d
    # I need this column for jp method but not for bv
    df_str_y_n['dZ_m_up'] = dz_u
    # negetive must be
    df_str_y_n['Density_diff_down'] = density_diff_down_daily

    df_str_y_n['N2'] = (df_str_y_n['Density_diff_down']/df_str_y_n['dZ_m_up']
                           )*(g/df_str_y_n['density2'])  # N2 in unites of s-2

    # *10**-4 for cm**2/s to m**2/s
    df_str_y_n['kz_bv_daily'] = (
        8.17*10**-4*(A0)**0.56*(df_str_y_n['N2'])**-0.43)*10**-4

    # m1 the not surface and bottom values are reported as na values density difference in reverse of the physical laws (bacause of the measurement problems or something unexpected happen)
    m1 = (df_str_y_n['Z_m'] > -17) & (df_str_y_n['Z_m']
                                      < 0) & ((df_str_y_n['kz_bv_daily']).isna())
    df_str_y_n.loc[m1, 'kz_bv_daily'] = df_str_y_n.loc[m1,
                                                       'kz_bv_daily'].fillna(kz_min)

    # m2 for water surface and the lake bed and the layer above (Z_m==0 and Z_m==-17 , Z_m==-21 ):
    m2 = np.logical_or(df_str_y_n['Z_m'] <= -17, df_str_y_n['Z_m'] == 0)
    df_str_y_n.loc[m2, 'kz_bv_daily'] = df_str_y_n.loc[m2,
                                                       'kz_bv_daily'].replace([np.inf, -np.inf], np.nan)

    # m3 other values that assigned to (np.inf , -np.inf) must be replace to minimum values because of density difference 0
    df_str_y_n.loc[:, 'kz_bv_daily'].replace(
        [np.inf, -np.inf], kz_min, inplace=True)

    return (df_str_y_n)

#try bv daily function

df_str_2018_1_14 = updated_daily_df_str_kz_bv(df_str_2018_1_14.reset_index())
df_str_2018_2_14 = updated_daily_df_str_kz_bv(df_str_2018_2_14.reset_index())
df_str_2019_1_14 = updated_daily_df_str_kz_bv(df_str_2019_1_14.reset_index())#
df_str_2019_2_14 = updated_daily_df_str_kz_bv(df_str_2019_2_14.reset_index())#
df_str_2020_1_14 = updated_daily_df_str_kz_bv(df_str_2020_1_14.reset_index())#
df_str_2021_1_14 = updated_daily_df_str_kz_bv(df_str_2021_1_14.reset_index())#
df_str_2022_1_14 = updated_daily_df_str_kz_bv(df_str_2022_1_14.reset_index())#


#%%kz-jp-daily_old version of calculation encoding:

def kz_jp(df_str_y_n_without_top_bed, temp_daily_2D_str_y_n):

    df_str_y_n_without_top_bed = df_str_y_n_without_top_bed.reset_index()

    if 'Datetime' in df_str_y_n_without_top_bed.columns:
        df_str_y_n_without_top_bed['Datetime'] = pd.to_datetime(
            df_str_y_n_without_top_bed['Datetime'])
        day_number_diff_str_y_n = np.diff(df_str_y_n_without_top_bed['Datetime'].unique()).astype('timedelta64[D]') / np.timedelta64(1, 'D')
        #np.append(0, np.diff(df_str_y_n_without_top_bed['Datetime'].unique(
        #))).astype('timedelta64[D]') / np.timedelta64(1, 'D')

    elif 'Datetime_start' in df_str_y_n_without_top_bed.columns:
        df_str_y_n_without_top_bed['Datetime_start'] = pd.to_datetime(
            df_str_y_n_without_top_bed['Datetime_start'])
        df_str_y_n_without_top_bed['Datetime_end'] = pd.to_datetime(
            df_str_y_n_without_top_bed['Datetime_end'])
        # df_str_y_n_without_top_bed['Datetime_end']=pd.to_datetime(df_str_y_n_without_top_bed['Datetime_end'])
        day_number_diff_str_y_n = np.diff(df_str_y_n_without_top_bed['Datetime_start'].unique(
        )).astype('timedelta64[D]') / np.timedelta64(1, 'D')
        

    a = np.zeros(temp_daily_2D_str_y_n[1: , :].shape)
    G = np.zeros(temp_daily_2D_str_y_n[1: , :].shape)
    K_paeen = np.zeros(temp_daily_2D_str_y_n[1: , :].shape)
    K_bala_each = np.zeros(temp_daily_2D_str_y_n[1: , :].shape)

    # stands for 0:35 the total profile and 15 is indicato of dz_m_up
    
    dZ_m_down = np.array(df_str_y_n_without_top_bed.iloc[0:(
        temp_daily_2D_str_y_n.shape[1])]['dZ_up_bndr_down'])
    V_r = np.array(df_str_y_n_without_top_bed.iloc[0:(
        temp_daily_2D_str_y_n.shape[1])]['V_r_m'])
    A_m = np.array(df_str_y_n_without_top_bed.iloc[0:(
        temp_daily_2D_str_y_n.shape[1])]['As_up_bndr_m'])

    for i in range(1, temp_daily_2D_str_y_n.shape[0]):  # i stands for time#56
       
        for j in range(1, temp_daily_2D_str_y_n.shape[1]): # j stands for layers#33

            a[i, j] = (temp_daily_2D_str_y_n[i, j] - temp_daily_2D_str_y_n[i-1, j])/(day_number_diff_str_y_n[i]*24*3600)
            G[i, j] = (temp_daily_2D_str_y_n[i, j-1] - temp_daily_2D_str_y_n[i, j])/(dZ_m_down[j-1])

            K_bala_each[i, j] = a[i, j]*V_r[j]
            K_paeen[i, j] = 1/(G[i, j]*A_m[j])

    K_bala_cul =np.zeros(temp_daily_2D_str_y_n.shape)
    # i stands for time # for each day
    for i in range(1, temp_daily_2D_str_y_n.shape[0]):
        # j stands for layers
        for j in range(1, temp_daily_2D_str_y_n.shape[1]):
            K_bala_cul[i, 1:] = (np.cumsum(K_bala_each[i, 1:][::-1])[::-1])

    K_jp_daily_y_n = K_bala_cul*K_paeen

    return (K_jp_daily_y_n)




#%% apply the Kz_Jp function for each stratification period seperately : 
#for the first layer an the day before stratification are 0
   

   
   
#2018
kz_jp_daily_2018_1 = kz_jp(
    df_str_2018_1_14, temp_daily_2D_2018_1)    

#2019_1
kz_jp_daily_2019_1 = kz_jp(
    df_str_2019_1_14, temp_daily_2D_2019_1)        
    
#2019_2
kz_jp_daily_2019_2 = kz_jp(
    df_str_2019_2_14, temp_daily_2D_2019_2)     

#2020
kz_jp_daily_2020_1 = kz_jp(
    df_str_2020_1_14, temp_daily_2D_2020_1)    


#2021
kz_jp_daily_2021_1 = kz_jp(
    df_str_2021_1_14, temp_daily_2D_2021_1)    
   
#2022
kz_jp_daily_2022_1 = kz_jp(
    df_str_2022_1_14, temp_daily_2D_2022_1)    


#%%Application of Kz_JP_daily function using a loop 

"""
# Define the list of years
years = ['2018_1', '2019_1', '2019_2', '2020_1', '2021_1', '2022_1']

# Initialize dictionaries to store the results
kz_jp_daily = {}

# Apply the function for each year
for year in years:
    # Remove 'Datetime' column from the dataframe
    df = globals()['df_str_' + year + '_14'].drop('Datetime', axis=1)
    
    # Get the corresponding temp 2D array for the year
    temp_2D_array = temp_daily_2D[year]
    
    # Apply the kz_jp function
    kz_jp_result = kz_jp(df, temp_2D_array)
    
    # Store the results in the dictionary
    kz_jp_daily[year] = kz_jp_result

# Now, you have the Kz_jp_daily results for each year stored in the kz_jp_daily dictionary.
# You can access the results for each year using indexing, e.g., kz_jp_daily['2018_1'] for 2018_1, kz_jp_daily['2019_1'] for 2019_1, and so on.
"""
#%%put in the dataframe:
"""
replacement_value=1.4*10**-7#m2/s
# Define the list of years
years = ['2018_1', '2019_1', '2019_2', '2020_1', '2021_1', '2022_1']

# Iterate over each year
for year in years:
    # Remove 'Datetime' column from the dataframe
    df = globals()['df_str_' + year + '_14']#.drop('Datetime', axis=1)
    
    df['Date']= df.index
    # Get the corresponding temp 2D array for the year
    temp_2D_array = temp_daily_2D[year]
    
    # Apply the kz_jp function
    kz_jp_result = kz_jp(df, temp_2D_array)
    
    # Put the kz_jp_daily values in the dataframe
    df['kz_jp_daily'] = kz_jp_result.flatten()
    
    # Replace NaN, infinite, and values lower than 1.4e-7
    df.loc[np.logical_or((df['Z_m'] == -1), (df['Date'] == df['Date'].min())), 'kz_jp_daily'] = np.nan
    df.loc[:, 'kz_jp_daily'] = df.loc[:, 'kz_jp_daily'].fillna(replacement_value)
    df.loc[df.loc[:, 'kz_jp_daily'] < replacement_value, 'kz_jp_daily'] = replacement_value
    df.loc[:, 'kz_jp_daily'].replace([np.inf, -np.inf], replacement_value, inplace=True)
    
    # Update the modified dataframe back to the global namespace
    globals()['df_str_' + year + '_14'] = df
    
    # Get the kz_jp_daily values below -13
    kz_jp_daily_below135 = two_D_array_from_df(df[df['Z_m'] < -13], values_name='kz_jp_daily' , index_name='Datetime')

   
    # Store the kz_jp_daily_below135 values in a dictionary
    kz_jp_daily_below135[year] = kz_jp_daily_below135
"""


#%another try 
"""
replacement_value = 1.4e-7  # Define the replacement value

# Define the list of years
years = ['2018_1', '2019_1', '2019_2', '2020_1', '2021_1', '2022_1']

# Initialize dictionaries to store the results
kz_jp_daily = {}
kz_jp_daily_below135 = {}

# Iterate over each year
for year in years:
    # Remove 'Datetime' column from the dataframe
    df = globals()['df_str_' + year + '_14'].copy()

    df['Date'] = df.index

    # Get the corresponding temp 2D array for the year
    temp_2D_array = temp_daily_2D[year]

    # Apply the kz_jp function
    kz_jp_result = kz_jp(df, temp_2D_array)

    # Put the kz_jp_daily values in the dataframe
    df['kz_jp_daily'] = kz_jp_result.flatten()

    # Replace NaN, infinite, and values lower than 1.4e-7
    df.loc[np.logical_or((df['Z_m'] == -1), (df['Date'] == df['Date'].min())), 'kz_jp_daily'] = np.nan
    df.loc[:, 'kz_jp_daily'] = df.loc[:, 'kz_jp_daily'].fillna(replacement_value)
    df.loc[df.loc[:, 'kz_jp_daily'] < replacement_value, 'kz_jp_daily'] = replacement_value
    df.loc[:, 'kz_jp_daily'].replace([np.inf, -np.inf], replacement_value, inplace=True)

    # Update the modified dataframe back to the global namespace
    globals()['df_str_' + year + '_14'] = df

    # Get the kz_jp_daily values below -13
    kz_jp_daily_below135_values = two_D_array_from_df(df[df['Z_m'] < -13], values_name='kz_jp_daily', index_name='Datetime')

    # Store the kz_jp_daily values in a dictionary
    kz_jp_daily[year] = kz_jp_result
    kz_jp_daily_below135[year] = kz_jp_daily_below135_values

    # Place kz_jp_daily in the dataframe
    globals()['df_str_' + year + '_14']['kz_jp_daily'] = kz_jp_daily[year].flatten()
    globals()['df_str_' + year + '_14'].loc[np.logical_or((globals()['df_str_' + year + '_14']['Z_m'] == -1),
                                                          (globals()['df_str_' + year + '_14']['Date'] == globals()['df_str_' + year + '_14']['Date'].min())),
                                             'kz_jp_daily'] = np.nan

    globals()['df_str_' + year + '_below14'] = globals()['df_str_' + year + '_14'][globals()['df_str_' + year + '_14']['Z_m'] <= -14]

    globals()['df_str_' + year + '_14'].loc[:, 'kz_jp_daily'] = globals()['df_str_' + year + '_14'].loc[:, 'kz_jp_daily'].fillna(replacement_value)
    globals()['df_str_' + year + '_14'].loc[(globals()['df_str_' + year + '_14'].loc[:, 'kz_jp_daily'] < replacement_value), 'kz_jp_daily'] = replacement_value

    globals()['df_str_' + year + '_14'].loc[:, 'kz_jp_daily'].replace([np.inf, -np.inf], replacement_value, inplace=True)

    kz_jp_daily_below135[year] = two_D_array_from_df(globals()['df_str_' + year + '_14'][globals()['df_str_' + year + '_14']['Z_m'] < -13], values_name='kz_jp_daily')
"""

#%% becuse the above process didn't work so I am going to implemnet it seperately: 
#%%2018_1 placing kz_jp in dataframe 
# the day before stratificatuion and the first layer kz values which previously were shown as 0
# here were replaced by the nan values  
# but of course when I cahnge them into  the two d arry it dos not show it and the
# size of dates were reduced by 1 day because of it

df_str_2018_1_14= df_str_2018_1_14.set_index('Datetime')
df_str_2018_1_14['kz_jp_daily'] = (kz_jp_daily_2018_1.flatten())
df_str_2018_1_14.loc[np.logical_or((df_str_2018_1_14['Z_m'] == -1) , (
    df_str_2018_1_14.index == df_str_2018_1_14.index.min())), 'kz_jp_daily'] = np.nan


df_str_2018_1_below14 = df_str_2018_1_14[df_str_2018_1_14['Z_m'] <= -14]


# kz_jp_daily
replacement_value = 1.4e-7


#df_str_2018_1_14.loc[:, 'kz_jp_daily'] = df_str_2018_1_14.loc[:, 'kz_jp_daily'].fillna(replacement_value)
df_str_2018_1_14.loc[(df_str_2018_1_14.loc[:,'kz_jp_daily'] < replacement_value), 'kz_jp_daily'] = replacement_value



df_str_2018_1_14.loc[:, 'kz_jp_daily'].replace(
        [np.inf, -np.inf], replacement_value, inplace=True)

# kz values daily excluding the estimation for mixing day 
kz_jp_2018_1_daily_below135 = two_D_array_from_df(
    df_str_2018_1_14[df_str_2018_1_14['Z_m'] < -13], values_name='kz_jp_daily')

#%%2019_1 placing kz_jp in dataframe 

df_str_2019_1_14= df_str_2019_1_14.set_index('Datetime')
df_str_2019_1_14['kz_jp_daily'] = (kz_jp_daily_2019_1.flatten())
df_str_2019_1_14.loc[np.logical_or((df_str_2019_1_14['Z_m'] == -1) , (
    df_str_2019_1_14.index ==df_str_2019_1_14.index.min())), 'kz_jp_daily'] = np.nan


df_str_2019_1_below14 = df_str_2019_1_14[df_str_2019_1_14['Z_m'] <= -14]


# kz_jp_daily
replacement_value = 1.4e-7

#df_str_2019_1_14.loc[:, 'kz_jp_daily'] = df_str_2019_1_14.loc[:, 'kz_jp_daily'].fillna(replacement_value)
df_str_2019_1_14.loc[(df_str_2019_1_14.loc[:,'kz_jp_daily'] < replacement_value), 'kz_jp_daily'] = replacement_value



df_str_2019_1_14.loc[:, 'kz_jp_daily'].replace(
        [np.inf, -np.inf], replacement_value, inplace=True)


kz_jp_2019_1_daily_below135 = two_D_array_from_df(
    df_str_2019_1_14[df_str_2019_1_14['Z_m'] < -13], values_name='kz_jp_daily')

#%%2019_2 placing kz_jp in dataframe 

df_str_2019_2_14= df_str_2019_2_14.set_index('Datetime')
df_str_2019_2_14['kz_jp_daily'] = (kz_jp_daily_2019_2.flatten())
df_str_2019_2_14.loc[np.logical_or((df_str_2019_2_14['Z_m'] == -1) , (
    df_str_2019_2_14.index ==df_str_2019_2_14.index.min())), 'kz_jp_daily'] = np.nan


df_str_2019_2_below14 = df_str_2019_2_14[df_str_2019_2_14['Z_m'] <= -14]


# kz_jp_daily
replacement_value = 1.4e-7

#df_str_2019_2_14.loc[:, 'kz_jp_daily'] = df_str_2019_2_14.loc[:, 'kz_jp_daily'].fillna(replacement_value)
df_str_2019_2_14.loc[(df_str_2019_2_14.loc[:,'kz_jp_daily'] < replacement_value), 'kz_jp_daily'] = replacement_value



df_str_2019_2_14.loc[:, 'kz_jp_daily'].replace(
        [np.inf, -np.inf], replacement_value, inplace=True)


kz_jp_2019_2_daily_below135 = two_D_array_from_df(
    df_str_2019_2_14[df_str_2019_2_14['Z_m'] < -13], values_name='kz_jp_daily')


#%%2020_1 placing kz_jp in dataframe 

df_str_2020_1_14= df_str_2020_1_14.set_index('Datetime')
df_str_2020_1_14['kz_jp_daily'] = (kz_jp_daily_2020_1.flatten())
df_str_2020_1_14.loc[np.logical_or((df_str_2020_1_14['Z_m'] == -1) , (
    df_str_2020_1_14.index ==df_str_2020_1_14.index.min())), 'kz_jp_daily'] = np.nan


df_str_2020_1_below14 = df_str_2020_1_14[df_str_2020_1_14['Z_m'] <= -14]


# kz_jp_daily
replacement_value = 1.4e-7

#df_str_2020_1_14.loc[:, 'kz_jp_daily'] = df_str_2020_1_14.loc[:, 'kz_jp_daily'].fillna(replacement_value)
df_str_2020_1_14.loc[(df_str_2020_1_14.loc[:,'kz_jp_daily'] < replacement_value), 'kz_jp_daily'] = replacement_value



df_str_2020_1_14.loc[:, 'kz_jp_daily'].replace(
        [np.inf, -np.inf], replacement_value, inplace=True)


kz_jp_2020_1_daily_below135 = two_D_array_from_df(
    df_str_2020_1_14[df_str_2020_1_14['Z_m'] < -13], values_name='kz_jp_daily')
#%%2021_1 placing kz_jp in dataframe 

df_str_2021_1_14= df_str_2021_1_14.set_index('Datetime')
df_str_2021_1_14['kz_jp_daily'] = (kz_jp_daily_2021_1.flatten())
df_str_2021_1_14.loc[np.logical_or((df_str_2021_1_14['Z_m'] == -1) , (
    df_str_2021_1_14.index ==df_str_2021_1_14.index.min())), 'kz_jp_daily'] = np.nan


df_str_2021_1_below14 = df_str_2021_1_14[df_str_2021_1_14['Z_m'] <= -14]


# kz_jp_daily
replacement_value = 1.4e-7

#df_str_2021_1_14.loc[:, 'kz_jp_daily'] = df_str_2021_1_14.loc[:, 'kz_jp_daily'].fillna(replacement_value)
df_str_2021_1_14.loc[(df_str_2021_1_14.loc[:,'kz_jp_daily'] < replacement_value), 'kz_jp_daily'] = replacement_value



df_str_2021_1_14.loc[:, 'kz_jp_daily'].replace(
        [np.inf, -np.inf], replacement_value, inplace=True)


kz_jp_2021_1_daily_below135 = two_D_array_from_df(
    df_str_2021_1_14[df_str_2021_1_14['Z_m'] < -13], values_name='kz_jp_daily')

#%%2022_1 placing kz_jp in dataframe 

df_str_2022_1_14= df_str_2022_1_14.set_index('Datetime')
df_str_2022_1_14['kz_jp_daily'] = (kz_jp_daily_2022_1.flatten())
df_str_2022_1_14.loc[np.logical_or((df_str_2022_1_14['Z_m'] == -1) , (
    df_str_2022_1_14.index ==df_str_2022_1_14.index.min())), 'kz_jp_daily'] = np.nan


df_str_2022_1_below14 = df_str_2022_1_14[df_str_2022_1_14['Z_m'] <= -14]


# kz_jp_daily
replacement_value = 1.4e-7

#df_str_2022_1_14.loc[:, 'kz_jp_daily'] = df_str_2022_1_14.loc[:, 'kz_jp_daily'].fillna(replacement_value)
df_str_2022_1_14.loc[(df_str_2022_1_14.loc[:,'kz_jp_daily'] < replacement_value), 'kz_jp_daily'] = replacement_value



df_str_2022_1_14.loc[:, 'kz_jp_daily'].replace(
        [np.inf, -np.inf], replacement_value, inplace=True)


kz_jp_2022_1_daily_below135 = two_D_array_from_df(
    df_str_2022_1_14[df_str_2022_1_14['Z_m'] < -13], values_name='kz_jp_daily')


#%%



array_statistics(kz_jp_2018_1_daily_below135)
{'Minimum': 1.4e-07,
 'Maximum': 0.0001222864257961385,
 'Mean': 9.247315121410153e-06,
 'Standard Deviation': 1.7160799930291082e-05}


array_statistics(kz_jp_2019_1_daily_below135)
{'Minimum': 1.4e-07,
 'Maximum': 0.00043358919020489807,
 'Mean': 1.8701129228773942e-05,
 'Standard Deviation': 4.246631620981847e-05}

array_statistics(kz_jp_2019_2_daily_below135)
{'Minimum': 1.4e-07,
 'Maximum': 0.00012931555327433362,
 'Mean': 7.5064710573664845e-06,
 'Standard Deviation': 1.548640597644614e-05}

array_statistics(kz_jp_2020_1_daily_below135)
{'Minimum': 1.4e-07,
 'Maximum': 0.00012018379229318715,
 'Mean': 9.530357059597863e-06,
 'Standard Deviation': 1.3523009146613104e-05}

array_statistics(kz_jp_2021_1_daily_below135)
{'Minimum': 1.4e-07,
 'Maximum': 0.00029822146920638955,
 'Mean': 1.301655448600919e-05,
 'Standard Deviation': 2.6009151597212713e-05}


array_statistics(kz_jp_2022_1_daily_below135)
{'Minimum': 1.4e-07,
 'Maximum': 0.00012359012593969116,
 'Mean': 8.957749717654002e-06,
 'Standard Deviation': 1.4781114802410221e-05}


####All togther analyses 

kz_jp_2D_2019_2022_daily= np.concatenate((  kz_jp_2019_1_daily_below135, kz_jp_2019_2_daily_below135, kz_jp_2020_1_daily_below135 , kz_jp_2021_1_daily_below135, kz_jp_2022_1_daily_below135), axis=0)
array_statistics(kz_jp_2D_2019_2022_daily)
{'Minimum': 1.4e-07,
 'Maximum': 0.00043358919020489807,
 'Mean': 1.1133503951502094e-05,
 'Standard Deviation': 2.306573996536815e-05}


kz_jp_2D_2018_2022_daily=np.concatenate(( kz_jp_2018_1_daily_below135 ,  kz_jp_2019_1_daily_below135, kz_jp_2019_2_daily_below135, kz_jp_2020_1_daily_below135 , kz_jp_2021_1_daily_below135, kz_jp_2022_1_daily_below135), axis=0)
array_statistics(kz_jp_2D_2018_2022_daily)
{'Minimum': 1.4e-07,
 'Maximum': 0.00043358919020489807,
 'Mean': 1.0713610325015198e-05,
 'Standard Deviation': 2.1903542266210495e-05}


a = np.where(kz_fortnightly_hypo_2D_insize_obs_2019_2022, 100, np.nan)



kz_fortnightly_hypo_2D_insize_obs_2019_2022













#%%weekly_monthly dataframe:

def weekly_monthly_df(df_str_y_n_without_top_bed):

    df_str_y_n_without_top_bed['Datetime'] = pd.to_datetime(
        df_str_y_n_without_top_bed['Datetime'], errors='coerce')

    df_str_y_n_without_top_bed['week_num'] = df_str_y_n_without_top_bed['Datetime'].dt.week
    df_str_y_n_without_top_bed['month_num'] = df_str_y_n_without_top_bed['Datetime'].dt.month
    df_str_y_n_without_top_bed['Z_m+'] = df_str_y_n_without_top_bed['Z_m']*-1

    df_weekly_str_y_n_without_top_bed = df_str_y_n_without_top_bed.groupby(
        ['week_num', 'Z_m+'])[ 'Temp', 'DO', 'DO_sat', 'density2', 'Z_m',
               'thikness', 'dZ_m_up', 'dZ_up_bndr_down', 'V_r_m', 'A_l_m', 'As_up_bndr_m',
               'As_lo_bndr_m',  'kz_jp_daily'].mean()#'moment_0_13.5', 'mass_0_13.5'"

    df_weekly_str_y_n_without_top_bed['density2'] = Lab_Density(
        df_weekly_str_y_n_without_top_bed['Temp'])
    df_weekly_str_y_n_without_top_bed['Datetime_start'] = df_str_y_n_without_top_bed.groupby(
        ['week_num', 'Z_m+'])['Datetime'].min()
    df_weekly_str_y_n_without_top_bed['Datetime_end'] = df_str_y_n_without_top_bed.groupby(
        ['week_num', 'Z_m+'])['Datetime'].max()
    # remove the weeks with less avaiable data of 3 days
    df_weekly_str_y_n_without_top_bed.drop(df_weekly_str_y_n_without_top_bed[(
        df_weekly_str_y_n_without_top_bed['Datetime_end'] - df_weekly_str_y_n_without_top_bed['Datetime_start']) < np.timedelta64(3, 'D')].index,  inplace=True)

    df_monthly_str_y_n_without_top_bed = df_str_y_n_without_top_bed.groupby(
        ['month_num', 'Z_m+'])[ 'Temp', 'DO', 'DO_sat', 'density2', 'Z_m',
               'thikness',  'dZ_m_up', 'dZ_up_bndr_down', 'V_r_m', 'A_l_m', 'As_up_bndr_m',
               'As_lo_bndr_m', 'kz_jp_daily'].mean()#'moment_0_13.5', 'mass_0_13.5'"
    df_monthly_str_y_n_without_top_bed['density2'] = Lab_Density(
        df_monthly_str_y_n_without_top_bed['Temp'])
    df_monthly_str_y_n_without_top_bed['Datetime_start'] = df_str_y_n_without_top_bed.groupby(
        ['month_num', 'Z_m+'])['Datetime'].min()
    df_monthly_str_y_n_without_top_bed['Datetime_end'] = df_str_y_n_without_top_bed.groupby(
        ['month_num', 'Z_m+'])['Datetime'].max()
    # removing the months with less avaiable data of 14 days
    df_monthly_str_y_n_without_top_bed.drop(df_monthly_str_y_n_without_top_bed[(
        df_monthly_str_y_n_without_top_bed['Datetime_end'] - df_monthly_str_y_n_without_top_bed['Datetime_start']) < np.timedelta64(14, 'D')].index,  inplace=True)

    # removing the index of month_ or week_num and Z_m+ to column:
    df_weekly_str_y_n_without_top_bed = df_weekly_str_y_n_without_top_bed.reset_index(level=[
                                                                                      0, 1])

    df_monthly_str_y_n_without_top_bed = df_monthly_str_y_n_without_top_bed.reset_index(level=[
                                                                                        0, 1])

    return (df_weekly_str_y_n_without_top_bed, df_monthly_str_y_n_without_top_bed)

#%%apply the weekly and month df function 

#2018
df_str_2018_1_14=df_str_2018_1_14.reset_index(drop= False)

weekly_prof_2018_1, monthly_prof_2018_1 = weekly_monthly_df(
    df_str_2018_1_14)



#2019_1
df_str_2019_1_14=df_str_2019_1_14.reset_index(drop= False)

weekly_prof_2019_1, monthly_prof_2019_1 = weekly_monthly_df(
    df_str_2019_1_14)


#2019_2
df_str_2019_2_14=df_str_2019_2_14.reset_index(drop= False)

weekly_prof_2019_2, monthly_prof_2019_2 = weekly_monthly_df(
    df_str_2019_2_14)


#2020
df_str_2020_1_14=df_str_2020_1_14.reset_index(drop= False)

weekly_prof_2020_1, monthly_prof_2020_1 = weekly_monthly_df(
    df_str_2020_1_14)


#2021
df_str_2021_1_14=df_str_2021_1_14.reset_index(drop= False)

weekly_prof_2021_1, monthly_prof_2021_1 = weekly_monthly_df(
    df_str_2021_1_14)


#2022
df_str_2022_1_14=df_str_2022_1_14.reset_index(drop= False)

weekly_prof_2022_1, monthly_prof_2022_1 = weekly_monthly_df(
    df_str_2022_1_14)


#%%kz_jp in weekly and monthly scales:

    
#2018_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2018_1 = two_D_array_from_df(
    weekly_prof_2018_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2018_1 = two_D_array_from_df(
    monthly_prof_2018_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly
# but for that weekly and monthly we can use the first week/ month 
# because it has different tempaerture 

kz_jp_weekly_2018_1 = kz_jp(
    weekly_prof_2018_1, temp_weekly_2D_2018_1)
kz_jp_monthly_2018_1 = kz_jp(
    monthly_prof_2018_1, temp_monthly_2D_2018_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2018_1['kz_jp_weekly'] = (kz_jp_weekly_2018_1.flatten())
weekly_prof_2018_1.loc[np.logical_or((weekly_prof_2018_1['Z_m+'] == 1) , (
    weekly_prof_2018_1['Datetime_start'] == weekly_prof_2018_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2018_1['kz_jp_monthly'] = (kz_jp_monthly_2018_1.flatten())
monthly_prof_2018_1.loc[np.logical_or((monthly_prof_2018_1['Z_m+'] == 1) , (
    monthly_prof_2018_1['Datetime_start'] == monthly_prof_2018_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan
        

    
#2019_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2019_1 = two_D_array_from_df(
    weekly_prof_2019_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2019_1 = two_D_array_from_df(
    monthly_prof_2019_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2019_1 = kz_jp(
    weekly_prof_2019_1, temp_weekly_2D_2019_1)
kz_jp_monthly_2019_1 = kz_jp(
    monthly_prof_2019_1, temp_monthly_2D_2019_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2019_1['kz_jp_weekly'] = (kz_jp_weekly_2019_1.flatten())
weekly_prof_2019_1.loc[np.logical_or((weekly_prof_2019_1['Z_m+'] == 1) , (
    weekly_prof_2019_1['Datetime_start'] == weekly_prof_2019_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2019_1['kz_jp_monthly'] = (kz_jp_monthly_2019_1.flatten())
monthly_prof_2019_1.loc[np.logical_or((monthly_prof_2019_1['Z_m+'] == 1) , (
    monthly_prof_2019_1['Datetime_start'] == monthly_prof_2019_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan
    

    
#2019_2
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2019_2 = two_D_array_from_df(
    weekly_prof_2019_2, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2019_2 = two_D_array_from_df(
    monthly_prof_2019_2, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2019_2 = kz_jp(
    weekly_prof_2019_2, temp_weekly_2D_2019_2)
kz_jp_monthly_2019_2 = kz_jp(
    monthly_prof_2019_2, temp_monthly_2D_2019_2)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2019_2['kz_jp_weekly'] = (kz_jp_weekly_2019_2.flatten())
weekly_prof_2019_2.loc[np.logical_or((weekly_prof_2019_2['Z_m+'] == 1) , (
    weekly_prof_2019_2['Datetime_start'] == weekly_prof_2019_2['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2019_2['kz_jp_monthly'] = (kz_jp_monthly_2019_2.flatten())
monthly_prof_2019_2.loc[np.logical_or((monthly_prof_2019_2['Z_m+'] == 1) , (
    monthly_prof_2019_2['Datetime_start'] == monthly_prof_2019_2['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan
    



#2020_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2020_1 = two_D_array_from_df(
    weekly_prof_2020_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2020_1 = two_D_array_from_df(
    monthly_prof_2020_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2020_1 = kz_jp(
    weekly_prof_2020_1, temp_weekly_2D_2020_1)
kz_jp_monthly_2020_1 = kz_jp(
    monthly_prof_2020_1, temp_monthly_2D_2020_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2020_1['kz_jp_weekly'] = (kz_jp_weekly_2020_1.flatten())
weekly_prof_2020_1.loc[np.logical_or((weekly_prof_2020_1['Z_m+'] == 1) , (
    weekly_prof_2020_1['Datetime_start'] == weekly_prof_2020_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2020_1['kz_jp_monthly'] = (kz_jp_monthly_2020_1.flatten())
monthly_prof_2020_1.loc[np.logical_or((monthly_prof_2020_1['Z_m+'] == 1) , (
    monthly_prof_2020_1['Datetime_start'] == monthly_prof_2020_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan
     
    
#2021_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2021_1 = two_D_array_from_df(
    weekly_prof_2021_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2021_1 = two_D_array_from_df(
    monthly_prof_2021_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2021_1 = kz_jp(
    weekly_prof_2021_1, temp_weekly_2D_2021_1)
kz_jp_monthly_2021_1 = kz_jp(
    monthly_prof_2021_1, temp_monthly_2D_2021_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2021_1['kz_jp_weekly'] = (kz_jp_weekly_2021_1.flatten())
weekly_prof_2021_1.loc[np.logical_or((weekly_prof_2021_1['Z_m+'] == 1) , (
    weekly_prof_2021_1['Datetime_start'] == weekly_prof_2021_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2021_1['kz_jp_monthly'] = (kz_jp_monthly_2021_1.flatten())
monthly_prof_2021_1.loc[np.logical_or((monthly_prof_2021_1['Z_m+'] == 1) , (
    monthly_prof_2021_1['Datetime_start'] == monthly_prof_2021_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan
        

#2022_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2022_1 = two_D_array_from_df(
    weekly_prof_2022_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2022_1 = two_D_array_from_df(
    monthly_prof_2022_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2022_1 = kz_jp(
    weekly_prof_2022_1, temp_weekly_2D_2022_1)
kz_jp_monthly_2022_1 = kz_jp(
    monthly_prof_2022_1, temp_monthly_2D_2022_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2022_1['kz_jp_weekly'] = (kz_jp_weekly_2022_1.flatten())
weekly_prof_2022_1.loc[np.logical_or((weekly_prof_2022_1['Z_m+'] == 1) , (
    weekly_prof_2022_1['Datetime_start'] == weekly_prof_2022_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2022_1['kz_jp_monthly'] = (kz_jp_monthly_2022_1.flatten())
monthly_prof_2022_1.loc[np.logical_or((monthly_prof_2022_1['Z_m+'] == 1) , (
    monthly_prof_2022_1['Datetime_start'] == monthly_prof_2022_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan
    

# %%Kz_bv_weekly_monthly:
# input and output are both df_str_y_n_without_top_bed, but only work for weekly or monthly
# as the rindex definded based on week-num or month_num


def kz_bv_monthly_weekly_df(df_str_y_n_without_top_bed, g=9.81838509231682, A0=23.67, kz_min=1.4*10**-7):

    if 'week_num' in df_str_y_n_without_top_bed.columns:

        index_based = 'week_num'

    elif 'month_num' in df_str_y_n_without_top_bed.columns:

        index_based = 'month_num'

    Density_2D_str_y_n = two_D_array_from_df(
        df_str_y_n_without_top_bed, values_name='density2', index_name=index_based, column_name='Z_m+')

    #Density_diff_down_2D_str_y_n = np.diff(
    #    Density_2D_str_y_n, append=np.full((Density_2D_str_y_n.shape[0], 1), np.nan))

    Density_diff_down_2D_str_y_n = np.diff(
    Density_2D_str_y_n, axis=1, prepend=np.full((Density_2D_str_y_n.shape[0], 1), np.nan))


    # >0 book baraye hamin manfie khate badi ro hazf karadm
    df_str_y_n_without_top_bed['Density_diff_down'] = Density_diff_down_2D_str_y_n.flatten(
    )

    df_str_y_n_without_top_bed['N2'] = (df_str_y_n_without_top_bed['Density_diff_down'] /
                                        df_str_y_n_without_top_bed['dZ_m_up'])*(g/df_str_y_n_without_top_bed['density2'])  # N2 in unites of s2

    df_str_y_n_without_top_bed['kz_bv'] = (8.17*10**-4*(A0)**0.56*(
        df_str_y_n_without_top_bed['N2'])**-0.43)*10**-4  # *10**-4 for cm**2/s to m**2/s

    # m1 the not surface and bottom values are reported as na values density difference in reverse of the physical laws (bacause of the measurement problems or something unexpected happen)
    m1 = (df_str_y_n_without_top_bed['Z_m+'] < 17) & (
        df_str_y_n_without_top_bed['Z_m+'] > 0) & ((df_str_y_n_without_top_bed['kz_bv']).isna())
    df_str_y_n_without_top_bed.loc[m1, 'kz_bv'] = df_str_y_n_without_top_bed.loc[m1, 'kz_bv'].fillna(
        kz_min)

    # m2 for water surface and the lake bed and the layer above (Z_m==0 and Z_m==-17 , Z_m==-21 ):
    m2 = df_str_y_n_without_top_bed['Z_m+'] == 17
    df_str_y_n_without_top_bed.loc[m2, 'kz_bv'] = df_str_y_n_without_top_bed.loc[m2, 'kz_bv'].replace([
                                                                                                      np.inf, -np.inf], np.nan)

    # m3 other values that assigned to (np.inf , -np.inf) must be replace to minimum values because of density difference 0
    df_str_y_n_without_top_bed.loc[:, 'kz_bv'].replace(
        [np.inf, -np.inf], kz_min, inplace=True)

    return (df_str_y_n_without_top_bed)

# %%Using the kz_bv_monthly_weekly_df function for producing new dtaframe:


# weekly
weekly_prof_2018_1 ,monthly_prof_2018_1  = kz_bv_monthly_weekly_df( weekly_prof_2018_1) , kz_bv_monthly_weekly_df( monthly_prof_2018_1)

weekly_prof_2019_1 ,monthly_prof_2019_1  = kz_bv_monthly_weekly_df( weekly_prof_2019_1) , kz_bv_monthly_weekly_df( monthly_prof_2019_1)

weekly_prof_2019_2 ,monthly_prof_2019_2  = kz_bv_monthly_weekly_df( weekly_prof_2019_2) , kz_bv_monthly_weekly_df( monthly_prof_2019_2)

weekly_prof_2020_1 ,monthly_prof_2020_1  = kz_bv_monthly_weekly_df( weekly_prof_2020_1) , kz_bv_monthly_weekly_df( monthly_prof_2020_1)

weekly_prof_2021_1 ,monthly_prof_2021_1  = kz_bv_monthly_weekly_df( weekly_prof_2021_1) , kz_bv_monthly_weekly_df( monthly_prof_2021_1)

weekly_prof_2022_1 ,monthly_prof_2022_1  = kz_bv_monthly_weekly_df( weekly_prof_2022_1) , kz_bv_monthly_weekly_df( monthly_prof_2022_1)





#%%placing monthly and weekly method in daily dataframe:
    

def set_monthly_or_weekly_df_in_daily(dataframe_input, dataframe_target, column_name_target, timescale_name):
    dataframe_input = dataframe_input.reset_index()
    dataframe_input = dataframe_input.set_index('Datetime_start')

    # use pivot_table() to pivot the DataFrame to a single day and columns under the name of depth
    dataframe_input_pivoted = dataframe_input.pivot_table(
        values=column_name_target, index=dataframe_input.index, columns='Z_m+', dropna=False)

    dataframe_input_reindexed = dataframe_input_pivoted.reindex(
        dataframe_target.index.unique(), method='ffill')
    # use melt() to transform the pivoted DataFrame back to the original format

    df_unpivoted = dataframe_input_reindexed.reset_index().melt(
        id_vars='Datetime', var_name='Z_m+', value_name=column_name_target)

    df_unpivoted = df_unpivoted.sort_values(
        ['Datetime', 'Z_m+'], ascending=[True, True])

    # return (np.array(df_unpivoted[column_name_target]))
    dataframe_target[f'{column_name_target}_{timescale_name}'] = np.array(
        df_unpivoted[column_name_target])

    return (dataframe_target)
    
#%%using the function above for setting monthly and weekly kz in daily dataframe 

#2018_1
df_str_2018_1_14['Datetime']=pd.to_datetime(df_str_2018_1_14['Datetime'])
df_str_2018_1_14= df_str_2018_1_14.set_index('Datetime') 

weekly_prof_2018_1['Datetime_start']= pd.to_datetime(weekly_prof_2018_1['Datetime_start'])
weekly_prof_2018_1['Datetime_end']= pd.to_datetime(weekly_prof_2018_1['Datetime_end'])


df_str_2018_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2018_1, df_str_2018_1_14,  'kz_jp_weekly', 'weekly')

df_str_2018_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2018_1, df_str_2018_1_14,  'kz_jp_monthly', 'monthly')

df_str_2018_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2018_1, df_str_2018_1_14,  'kz_bv', 'weekly')

df_str_2018_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2018_1, df_str_2018_1_14,  'kz_bv', 'monthly')


 
#2019_1
df_str_2019_1_14['Datetime']=pd.to_datetime(df_str_2019_1_14['Datetime'])
df_str_2019_1_14= df_str_2019_1_14.set_index('Datetime') 

weekly_prof_2019_1['Datetime_start']= pd.to_datetime(weekly_prof_2019_1['Datetime_start'])
weekly_prof_2019_1['Datetime_end']= pd.to_datetime(weekly_prof_2019_1['Datetime_end'])


df_str_2019_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2019_1, df_str_2019_1_14,  'kz_jp_weekly', 'weekly')

df_str_2019_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2019_1, df_str_2019_1_14,  'kz_jp_monthly', 'monthly')

df_str_2019_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2019_1, df_str_2019_1_14,  'kz_bv', 'weekly')

df_str_2019_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2019_1, df_str_2019_1_14,  'kz_bv', 'monthly')
 
#2019_2
df_str_2019_2_14['Datetime']=pd.to_datetime(df_str_2019_2_14['Datetime'])
df_str_2019_2_14= df_str_2019_2_14.set_index('Datetime') 

weekly_prof_2019_2['Datetime_start']= pd.to_datetime(weekly_prof_2019_2['Datetime_start'])
weekly_prof_2019_2['Datetime_end']= pd.to_datetime(weekly_prof_2019_2['Datetime_end'])


df_str_2019_2_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2019_2, df_str_2019_2_14,  'kz_jp_weekly', 'weekly')

df_str_2019_2_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2019_2, df_str_2019_2_14,  'kz_jp_monthly', 'monthly')


df_str_2019_2_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2019_2, df_str_2019_2_14,  'kz_bv', 'weekly')

df_str_2019_2_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2019_2, df_str_2019_2_14,  'kz_bv', 'monthly')
 
#2020_1
df_str_2020_1_14['Datetime']=pd.to_datetime(df_str_2020_1_14['Datetime'])
df_str_2020_1_14= df_str_2020_1_14.set_index('Datetime') 

weekly_prof_2020_1['Datetime_start']= pd.to_datetime(weekly_prof_2020_1['Datetime_start'])
weekly_prof_2020_1['Datetime_end']= pd.to_datetime(weekly_prof_2020_1['Datetime_end'])


df_str_2020_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2020_1, df_str_2020_1_14,  'kz_jp_weekly', 'weekly')

df_str_2020_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2020_1, df_str_2020_1_14,  'kz_jp_monthly', 'monthly')

df_str_2020_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2020_1, df_str_2020_1_14,  'kz_bv', 'weekly')

df_str_2020_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2020_1, df_str_2020_1_14,  'kz_bv', 'monthly')

 
#2021_1
df_str_2021_1_14['Datetime']=pd.to_datetime(df_str_2021_1_14['Datetime'])
df_str_2021_1_14= df_str_2021_1_14.set_index('Datetime') 

weekly_prof_2021_1['Datetime_start']= pd.to_datetime(weekly_prof_2021_1['Datetime_start'])
weekly_prof_2021_1['Datetime_end']= pd.to_datetime(weekly_prof_2021_1['Datetime_end'])


df_str_2021_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2021_1, df_str_2021_1_14,  'kz_jp_weekly', 'weekly')

df_str_2021_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2021_1, df_str_2021_1_14,  'kz_jp_monthly', 'monthly')

df_str_2021_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2021_1, df_str_2021_1_14,  'kz_bv', 'weekly')

df_str_2021_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2021_1, df_str_2021_1_14,  'kz_bv', 'monthly')

#2022_1
df_str_2022_1_14['Datetime']=pd.to_datetime(df_str_2022_1_14['Datetime'])
df_str_2022_1_14= df_str_2022_1_14.set_index('Datetime') 

weekly_prof_2022_1['Datetime_start']= pd.to_datetime(weekly_prof_2022_1['Datetime_start'])
weekly_prof_2022_1['Datetime_end']= pd.to_datetime(weekly_prof_2022_1['Datetime_end'])


df_str_2022_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2022_1, df_str_2022_1_14,  'kz_jp_weekly', 'weekly')

df_str_2022_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2022_1, df_str_2022_1_14,  'kz_jp_monthly', 'monthly')


df_str_2022_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2022_1, df_str_2022_1_14,  'kz_bv', 'weekly')

df_str_2022_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2022_1, df_str_2022_1_14,  'kz_bv', 'monthly')





"""################SHOULD BE DELETED : IT IS THE SAME ABOVE 
#%%kz_jp in weekly and monthly scales:

 
#2018_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2018_1 = two_D_array_from_df(
    weekly_prof_2018_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2018_1 = two_D_array_from_df(
    monthly_prof_2018_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2018_1 = kz_jp(
    weekly_prof_2018_1, temp_weekly_2D_2018_1)
kz_jp_monthly_2018_1 = kz_jp(
    monthly_prof_2018_1, temp_monthly_2D_2018_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2018_1['kz_jp_weekly'] = (kz_jp_weekly_2018_1.flatten())
weekly_prof_2018_1.loc[np.logical_or((weekly_prof_2018_1['Z_m+'] == 1) , (
    weekly_prof_2018_1['Datetime_start'] == weekly_prof_2018_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2018_1['kz_jp_monthly'] = (kz_jp_monthly_2018_1.flatten())
monthly_prof_2018_1.loc[np.logical_or((monthly_prof_2018_1['Z_m+'] == 1) , (
    monthly_prof_2018_1['Datetime_start'] == monthly_prof_2018_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan


#2019_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2019_1 = two_D_array_from_df(
    weekly_prof_2019_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2019_1 = two_D_array_from_df(
    monthly_prof_2019_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2019_1 = kz_jp(
    weekly_prof_2019_1, temp_weekly_2D_2019_1)
kz_jp_monthly_2019_1 = kz_jp(
    monthly_prof_2019_1, temp_monthly_2D_2019_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2019_1['kz_jp_weekly'] = (kz_jp_weekly_2019_1.flatten())
weekly_prof_2019_1.loc[np.logical_or((weekly_prof_2019_1['Z_m+'] == 1) , (
    weekly_prof_2019_1['Datetime_start'] == weekly_prof_2019_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2019_1['kz_jp_monthly'] = (kz_jp_monthly_2019_1.flatten())
monthly_prof_2019_1.loc[np.logical_or((monthly_prof_2019_1['Z_m+'] == 1) , (
    monthly_prof_2019_1['Datetime_start'] == monthly_prof_2019_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan



#2019_2
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2019_2 = two_D_array_from_df(
    weekly_prof_2019_2, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2019_2 = two_D_array_from_df(
    monthly_prof_2019_2, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2019_2 = kz_jp(
    weekly_prof_2019_2, temp_weekly_2D_2019_2)
kz_jp_monthly_2019_2 = kz_jp(
    monthly_prof_2019_2, temp_monthly_2D_2019_2)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2019_2['kz_jp_weekly'] = (kz_jp_weekly_2019_2.flatten())
weekly_prof_2019_2.loc[np.logical_or((weekly_prof_2019_2['Z_m+'] == 1) , (
    weekly_prof_2019_2['Datetime_start'] == weekly_prof_2019_2['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2019_2['kz_jp_monthly'] = (kz_jp_monthly_2019_2.flatten())
monthly_prof_2019_2.loc[np.logical_or((monthly_prof_2019_2['Z_m+'] == 1) , (
    monthly_prof_2019_2['Datetime_start'] == monthly_prof_2019_2['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan




#2020_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2020_1 = two_D_array_from_df(
    weekly_prof_2020_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2020_1 = two_D_array_from_df(
    monthly_prof_2020_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2020_1 = kz_jp(
    weekly_prof_2020_1, temp_weekly_2D_2020_1)
kz_jp_monthly_2020_1 = kz_jp(
    monthly_prof_2020_1, temp_monthly_2D_2020_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2020_1['kz_jp_weekly'] = (kz_jp_weekly_2020_1.flatten())
weekly_prof_2020_1.loc[np.logical_or((weekly_prof_2020_1['Z_m+'] == 1) , (
    weekly_prof_2020_1['Datetime_start'] == weekly_prof_2020_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2020_1['kz_jp_monthly'] = (kz_jp_monthly_2020_1.flatten())
monthly_prof_2020_1.loc[np.logical_or((monthly_prof_2020_1['Z_m+'] == 1) , (
    monthly_prof_2020_1['Datetime_start'] == monthly_prof_2020_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan



#2021_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2021_1 = two_D_array_from_df(
    weekly_prof_2021_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2021_1 = two_D_array_from_df(
    monthly_prof_2021_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2021_1 = kz_jp(
    weekly_prof_2021_1, temp_weekly_2D_2021_1)
kz_jp_monthly_2021_1 = kz_jp(
    monthly_prof_2021_1, temp_monthly_2D_2021_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2021_1['kz_jp_weekly'] = (kz_jp_weekly_2021_1.flatten())
weekly_prof_2021_1.loc[np.logical_or((weekly_prof_2021_1['Z_m+'] == 1) , (
    weekly_prof_2021_1['Datetime_start'] == weekly_prof_2021_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2021_1['kz_jp_monthly'] = (kz_jp_monthly_2021_1.flatten())
monthly_prof_2021_1.loc[np.logical_or((monthly_prof_2021_1['Z_m+'] == 1) , (
    monthly_prof_2021_1['Datetime_start'] == monthly_prof_2021_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan
    

    
#2022_1
# 2_D arrays for kz_jp
# weekly
temp_weekly_2D_2022_1 = two_D_array_from_df(
    weekly_prof_2022_1, values_name='Temp', index_name='week_num', column_name='Z_m+')
temp_monthly_2D_2022_1 = two_D_array_from_df(
    monthly_prof_2022_1, values_name='Temp', index_name='month_num', column_name='Z_m+')


# Using function kz_jp calculatinfg kz_jp_weekly and kz_jp_monthly:

kz_jp_weekly_2022_1 = kz_jp(
    weekly_prof_2022_1, temp_weekly_2D_2022_1)
kz_jp_monthly_2022_1 = kz_jp(
    monthly_prof_2022_1, temp_monthly_2D_2022_1)

# Placing the weekly and monthly kz_JP into the df_str_without_top_bed

# weekly
weekly_prof_2022_1['kz_jp_weekly'] = (kz_jp_weekly_2022_1.flatten())
weekly_prof_2022_1.loc[np.logical_or((weekly_prof_2022_1['Z_m+'] == 1) , (
    weekly_prof_2022_1['Datetime_start'] == weekly_prof_2022_1['Datetime_start'].min())), 'kz_jp_weekly'] = np.nan

# monthly
monthly_prof_2022_1['kz_jp_monthly'] = (kz_jp_monthly_2022_1.flatten())
monthly_prof_2022_1.loc[np.logical_or((monthly_prof_2022_1['Z_m+'] == 1) , (
    monthly_prof_2022_1['Datetime_start'] == monthly_prof_2022_1['Datetime_start'].min())), 'kz_jp_monthly'] = np.nan


#%%placing monthly and weekly method in daily dataframe:
    

def set_monthly_or_weekly_df_in_daily(dataframe_input, dataframe_target, column_name_target, timescale_name):
    dataframe_input = dataframe_input.reset_index()
    dataframe_input = dataframe_input.set_index('Datetime_start')

    # use pivot_table() to pivot the DataFrame to a single day and columns under the name of depth
    dataframe_input_pivoted = dataframe_input.pivot_table(
        values=column_name_target, index=dataframe_input.index, columns='Z_m+', dropna=False)

    dataframe_input_reindexed = dataframe_input_pivoted.reindex(
        dataframe_target.index.unique(), method='ffill')
    # use melt() to transform the pivoted DataFrame back to the original format

    df_unpivoted = dataframe_input_reindexed.reset_index().melt(
        id_vars='Datetime', var_name='Z_m+', value_name=column_name_target)

    df_unpivoted = df_unpivoted.sort_values(
        ['Datetime', 'Z_m+'], ascending=[True, True])

    # return (np.array(df_unpivoted[column_name_target]))
    dataframe_target[f'{column_name_target}_{timescale_name}'] = np.array(
        df_unpivoted[column_name_target])

    return (dataframe_target)
    
#%%using the function above 
 

#2018_1
weekly_prof_2018_1['Datetime_start']= pd.to_datetime(weekly_prof_2018_1['Datetime_start'])
weekly_prof_2018_1['Datetime_end']= pd.to_datetime(weekly_prof_2018_1['Datetime_end'])


df_str_2018_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2018_1, df_str_2018_1_14,  'kz_jp_weekly', 'weekly')

df_str_2018_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2018_1, df_str_2018_1_14,  'kz_jp_monthly', 'monthly')


#2019_1
weekly_prof_2019_1['Datetime_start']= pd.to_datetime(weekly_prof_2019_1['Datetime_start'])
weekly_prof_2019_1['Datetime_end']= pd.to_datetime(weekly_prof_2019_1['Datetime_end'])


df_str_2019_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2019_1, df_str_2019_1_14,  'kz_jp_weekly', 'weekly')

df_str_2019_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2019_1, df_str_2019_1_14,  'kz_jp_monthly', 'monthly')

#2019_2
weekly_prof_2019_2['Datetime_start']= pd.to_datetime(weekly_prof_2019_2['Datetime_start'])
weekly_prof_2019_2['Datetime_end']= pd.to_datetime(weekly_prof_2019_2['Datetime_end'])


df_str_2019_2_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2019_2, df_str_2019_2_14,  'kz_jp_weekly', 'weekly')

df_str_2019_2_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2019_2, df_str_2019_2_14,  'kz_jp_monthly', 'monthly')
 
#2020_1
weekly_prof_2020_1['Datetime_start']= pd.to_datetime(weekly_prof_2020_1['Datetime_start'])
weekly_prof_2020_1['Datetime_end']= pd.to_datetime(weekly_prof_2020_1['Datetime_end'])


df_str_2020_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2020_1, df_str_2020_1_14,  'kz_jp_weekly', 'weekly')

df_str_2020_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2020_1, df_str_2020_1_14,  'kz_jp_monthly', 'monthly')


#2021_1
weekly_prof_2021_1['Datetime_start']= pd.to_datetime(weekly_prof_2021_1['Datetime_start'])
weekly_prof_2021_1['Datetime_end']= pd.to_datetime(weekly_prof_2021_1['Datetime_end'])


df_str_2021_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2021_1, df_str_2021_1_14,  'kz_jp_weekly', 'weekly')

df_str_2021_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2021_1, df_str_2021_1_14,  'kz_jp_monthly', 'monthly') 


#2022_1
weekly_prof_2022_1['Datetime_start']= pd.to_datetime(weekly_prof_2022_1['Datetime_start'])
weekly_prof_2022_1['Datetime_end']= pd.to_datetime(weekly_prof_2022_1['Datetime_end'])


df_str_2022_1_14 = set_monthly_or_weekly_df_in_daily(
    weekly_prof_2022_1, df_str_2022_1_14,  'kz_jp_weekly', 'weekly')

df_str_2022_1_14 = set_monthly_or_weekly_df_in_daily(
    monthly_prof_2022_1, df_str_2022_1_14,  'kz_jp_monthly', 'monthly')
"""
# %% craeting 2 D arry from kz values of monthly or weekly for modelling coing:

#'kz_jp_monthly_monthly','kz_jp_weekly_weekly'

replacement_value = 1.4e-7



#2018_1
# 3. 'kz_jp_monthly_monthly':
df_str_2018_1_14.loc[:, 'kz_jp_monthly_monthly'] = df_str_2018_1_14.loc[:,'kz_jp_monthly_monthly'].fillna(replacement_value)
                                                                                  
df_str_2018_1_14.loc[(df_str_2018_1_14.loc[:, 'kz_jp_monthly_monthly']
                           < replacement_value), 'kz_jp_monthly_monthly'] = replacement_value

kz_jp_monthly_below135_2018_1 = two_D_array_from_df(
    df_str_2018_1_14[df_str_2018_1_14['Z_m'] < -13], values_name='kz_jp_monthly_monthly')


# 4. 'kz_jp_weekly_weekly':
df_str_2018_1_14.loc[:, 'kz_jp_weekly_weekly'] = df_str_2018_1_14.loc[:,
                                                                                'kz_jp_weekly_weekly'].fillna(replacement_value)
df_str_2018_1_14.loc[(df_str_2018_1_14.loc[:, 'kz_jp_weekly_weekly']
                           < replacement_value), 'kz_jp_weekly_weekly'] = replacement_value

kz_jp_weekly_below135_2018_1 = two_D_array_from_df(
    df_str_2018_1_14[df_str_2018_1_14['Z_m'] < -13], values_name='kz_jp_weekly_weekly')

kz_jp_weekly_below135_2018_1.mean()#5.774523175227538e-06


#2019_1
# 3. 'kz_jp_monthly_monthly':
df_str_2019_1_14.loc[:, 'kz_jp_monthly_monthly'] = df_str_2019_1_14.loc[:,
                                                                                  'kz_jp_monthly_monthly'].fillna(replacement_value)
df_str_2019_1_14.loc[(df_str_2019_1_14.loc[:, 'kz_jp_monthly_monthly']
                           < replacement_value), 'kz_jp_monthly_monthly'] = replacement_value

kz_jp_monthly_below135_2019_1 = two_D_array_from_df(
    df_str_2019_1_14[df_str_2019_1_14['Z_m'] < -13], values_name='kz_jp_monthly_monthly')


# 4. 'kz_jp_weekly_weekly':
df_str_2019_1_14.loc[:, 'kz_jp_weekly_weekly'] = df_str_2019_1_14.loc[:,
                                                                                'kz_jp_weekly_weekly'].fillna(replacement_value)
df_str_2019_1_14.loc[(df_str_2019_1_14.loc[:, 'kz_jp_weekly_weekly']
                           < replacement_value), 'kz_jp_weekly_weekly'] = replacement_value

kz_jp_weekly_below135_2019_1 = two_D_array_from_df(
    df_str_2019_1_14[df_str_2019_1_14['Z_m'] < -13], values_name='kz_jp_weekly_weekly')

kz_jp_weekly_below135_2019_1.mean()#8.412065308877426e-06


#2019_2
# 3. 'kz_jp_monthly_monthly':
df_str_2019_2_14.loc[:, 'kz_jp_monthly_monthly'] = df_str_2019_2_14.loc[:,
                                                                                  'kz_jp_monthly_monthly'].fillna(replacement_value)
df_str_2019_2_14.loc[(df_str_2019_2_14.loc[:, 'kz_jp_monthly_monthly']
                           < replacement_value), 'kz_jp_monthly_monthly'] = replacement_value

kz_jp_monthly_below135_2019_2 = two_D_array_from_df(
    df_str_2019_2_14[df_str_2019_2_14['Z_m'] < -13], values_name='kz_jp_monthly_monthly')


# 4. 'kz_jp_weekly_weekly':
df_str_2019_2_14.loc[:, 'kz_jp_weekly_weekly'] = df_str_2019_2_14.loc[:,
                                                                                'kz_jp_weekly_weekly'].fillna(replacement_value)
df_str_2019_2_14.loc[(df_str_2019_2_14.loc[:, 'kz_jp_weekly_weekly']
                           < replacement_value), 'kz_jp_weekly_weekly'] = replacement_value

kz_jp_weekly_below135_2019_2 = two_D_array_from_df(
    df_str_2019_2_14[df_str_2019_2_14['Z_m'] < -13], values_name='kz_jp_weekly_weekly')

kz_jp_weekly_below135_2019_2.mean()#1.7026696432920164e-06

#2020_1
# 3. 'kz_jp_monthly_monthly':
df_str_2020_1_14.loc[:, 'kz_jp_monthly_monthly'] = df_str_2020_1_14.loc[:,
                                                                                  'kz_jp_monthly_monthly'].fillna(replacement_value)
df_str_2020_1_14.loc[(df_str_2020_1_14.loc[:, 'kz_jp_monthly_monthly']
                           < replacement_value), 'kz_jp_monthly_monthly'] = replacement_value

kz_jp_monthly_below135_2020_1 = two_D_array_from_df(
    df_str_2020_1_14[df_str_2020_1_14['Z_m'] < -13], values_name='kz_jp_monthly_monthly')


# 4. 'kz_jp_weekly_weekly':
df_str_2020_1_14.loc[:, 'kz_jp_weekly_weekly'] = df_str_2020_1_14.loc[:,
                                                                                'kz_jp_weekly_weekly'].fillna(replacement_value)
df_str_2020_1_14.loc[(df_str_2020_1_14.loc[:, 'kz_jp_weekly_weekly']
                           < replacement_value), 'kz_jp_weekly_weekly'] = replacement_value

kz_jp_weekly_below135_2020_1 = two_D_array_from_df(
    df_str_2020_1_14[df_str_2020_1_14['Z_m'] < -13], values_name='kz_jp_weekly_weekly')

kz_jp_weekly_below135_2020_1.mean()#6.097586304958716e-06
kz_jp_monthly_below135_2020_1.mean()#6.899298066328019e-06



#2021_1
# 3. 'kz_jp_monthly_monthly':
df_str_2021_1_14.loc[:, 'kz_jp_monthly_monthly'] = df_str_2021_1_14.loc[:,
                                                                                  'kz_jp_monthly_monthly'].fillna(replacement_value)
df_str_2021_1_14.loc[(df_str_2021_1_14.loc[:, 'kz_jp_monthly_monthly']
                           < replacement_value), 'kz_jp_monthly_monthly'] = replacement_value

kz_jp_monthly_below135_2021_1 = two_D_array_from_df(
    df_str_2021_1_14[df_str_2021_1_14['Z_m'] < -13], values_name='kz_jp_monthly_monthly')


# 4. 'kz_jp_weekly_weekly':
df_str_2021_1_14.loc[:, 'kz_jp_weekly_weekly'] = df_str_2021_1_14.loc[:,
                                                                                'kz_jp_weekly_weekly'].fillna(replacement_value)
df_str_2021_1_14.loc[(df_str_2021_1_14.loc[:, 'kz_jp_weekly_weekly']
                           < replacement_value), 'kz_jp_weekly_weekly'] = replacement_value

kz_jp_weekly_below135_2021_1 = two_D_array_from_df(
    df_str_2021_1_14[df_str_2021_1_14['Z_m'] < -13], values_name='kz_jp_weekly_weekly')

kz_jp_weekly_below135_2021_1.mean()#7.5739331184346555e-06



#2022_1
# 3. 'kz_jp_monthly_monthly':
df_str_2022_1_14.loc[:, 'kz_jp_monthly_monthly'] = df_str_2022_1_14.loc[:,
                                                                                  'kz_jp_monthly_monthly'].fillna(replacement_value)
df_str_2022_1_14.loc[(df_str_2022_1_14.loc[:, 'kz_jp_monthly_monthly']
                           < replacement_value), 'kz_jp_monthly_monthly'] = replacement_value

kz_jp_monthly_below135_2022_1 = two_D_array_from_df(
    df_str_2022_1_14[df_str_2022_1_14['Z_m'] < -13], values_name='kz_jp_monthly_monthly')


# 4. 'kz_jp_weekly_weekly':
df_str_2022_1_14.loc[:, 'kz_jp_weekly_weekly'] = df_str_2022_1_14.loc[:,
                                                                                'kz_jp_weekly_weekly'].fillna(replacement_value)
df_str_2022_1_14.loc[(df_str_2022_1_14.loc[:, 'kz_jp_weekly_weekly']
                           < replacement_value), 'kz_jp_weekly_weekly'] = replacement_value

kz_jp_weekly_below135_2022_1 = two_D_array_from_df(
    df_str_2022_1_14[df_str_2022_1_14['Z_m'] < -13], values_name='kz_jp_weekly_weekly')

kz_jp_weekly_below135_2022_1.mean()#4.6033504169537265e-06




#%%one year modelling_onlyJs but not kz:
 """for testing   
#C_2019_1 , C_ave_2019_1 =do_oneyear_Jz(params ,inital_cond=inital_coulmn_2019_1, deltat=deltat_2019_1, temp=temp_daily_2D_2019_1_below135)
inital_cond=inital_coulmn_2019_1
deltat=deltat_2019_1
temp=temp_daily_2D_2019_1_below135#(48, 8)
#temp= temp_daily_2D_2019_1_hypo# (48, 7)
params=[0.1, 0.3, 1]     
 """   


def do_oneyear_Jz(params, inital_cond, deltat , temp ):
    jv, ja, scale_subdaily=params
    deltat=deltat[1:]
    #temp= temp[: , 1:]
    n=7
    num_time_steps_subdaily =int( 1/scale_subdaily)  
    deltat=scale_subdaily*np.tile(deltat, (num_time_steps_subdaily, 1)).transpose().flatten()
    m=len(deltat) #332daily  
    temp_subdaily: np.ndarray = np.repeat(temp, num_time_steps_subdaily, axis=0)
    deltaz=0.5#0.5
    #As=A_s[1:] 
    #Vr= V_r[1:]
    #Al= A_l[1:]
    

    def Theta_j(temp):  
        theta = 1.087
        return (theta** (temp-20))
    
    #temp_meta=temp_subdaily[:, 0]
    #C_meta =np.array(C_satur (temp_meta , 0.7))
    temp=temp_subdaily[:, 1:].T #with temp=temp_daily_2D_2019_1_below135#(48, 8)#temp_subdaily.T with temp= temp_daily_2D_2019_1_hypo# (48, 7)
    lhs=inital_cond#- deltat[0] *( (Al/Vr) * ja*Theta_j(temp[:,0]) + jv *Theta_j(temp[:,0]))#+ C_meta[0]*deltat[0]*A_s[1]*kz[1, 0]/(V_r[1]*deltaz)
    C=np.zeros((n,m+1))# depth ,time 
    C[:,0]=lhs

    for j in range(1, m+1):# m=len(deltat)
        
            
            C[:, j]= C[: , j-1]- deltat[j-1]*Theta_j(0.5*temp[: , j-1]+0.5*temp[: , j])*(jv + ja * (A_l[1:]/V_r[1:]))
       
 
    C_ddp =C[:, 1:]   
    num_days = C_ddp.shape[1] // num_time_steps_subdaily
    #C_3d in shape of day number , subdaily number , each layer
    C_3d = C_ddp.reshape(n, num_days, num_time_steps_subdaily)
    # Now you can extract the last value from each subdaily group
    #C_daily_str = C_3d[:, :, -1]# depth, time 
    # geting average on the time steps scale 
    C_daily_str = np.mean(C_3d, axis=2)

    C_f = np.where(C_daily_str < 0, 0, C_daily_str).T    
    

    DO_ave_model=np.dot(C_f, V_r[1:])/ sum(V_r[1:]) 
    
    #print (DO_ave_model)
    return (C_f , DO_ave_model)  



#%%one year modelling implicit method:



def do_oneyear_implicit(params, temp , kz_array , initial_cond, deltat ):
    
    deltat=deltat[1:]
    temp_jz_correction =(temp[1:, :]+temp[:-1, :])/2 # removing the day before onset 
    
    kz_array=kz_array[1: , :]# doesn't need any more 
    
    
    jv, ja, scale_subdaily=params
    n=7
    num_time_steps_subdaily =int( 1/scale_subdaily)  
    deltat=scale_subdaily*np.tile(deltat, (num_time_steps_subdaily, 1)).transpose().flatten()
    m=len(deltat) #315  
    temp_subdaily: np.ndarray = np.repeat(temp_jz_correction, num_time_steps_subdaily, axis=0)
    deltaz=0.5#0.5
    #As=A_s[1:] 
    #Vr= V_r[1:]
    #Al= A_l[1:]
    
    
    kz=np.repeat(kz_array, num_time_steps_subdaily, axis=0)
    kz=(24*3600*kz).T

    def Theta_j(temp):  #Weber et al, 2017
        theta = 1.087
        return (theta** (temp-20))
    
    #temp_meta=temp_subdaily[:, 0]
    #C_meta =np.array(C_satur (temp_meta , 0.7))
    temp=temp_subdaily[: , 1:].T#!!!!????
    lhs=initial_cond#- deltat[0] *( (Al/Vr) * ja*Theta_j(temp[:,0]) + jv *Theta_j(temp[:,0]))#+ C_meta[0]*deltat[0]*A_s[1]*kz[1, 0]/(V_r[1]*deltaz)
    C=np.zeros((n,m+1))#depth,  time 
    C[:,0]=lhs

    for j in range(0, m):

        Factor_dig_m=np.diag([ 1- 0 - delta_t[j]*A_s[2]*kz[2, j]/(V_r[1]*dz),#+ delta_t[j]*A_s[1]*kz[1,j]/(dz*V_r[1])  , 
                 1- delta_t[j]*A_s[2]*kz[2,j]/(dz*V_r[2]) - delta_t[j]*A_s[3]*kz[3,j]/(dz*V_r[2]),
                 1- delta_t[j]*A_s[3]*kz[3,j]/(dz*V_r[3]) - delta_t[j]*A_s[4]*kz[4,j]/(dz*V_r[3]), 
                 1- delta_t[j]*A_s[4]*kz[4,j]/(dz*V_r[4]) - delta_t[j]*A_s[5]*kz[5,j]/(dz*V_r[4]),
                 1- delta_t[j]*A_s[5]*kz[5,j]/(dz*V_r[5]) - delta_t[j]*A_s[6]*kz[6,j]/(dz*V_r[5]),
                 1- delta_t[j]*A_s[6]*kz[6,j]/(dz*V_r[6]) - delta_t[j]*A_s[7]*kz[7,j]/(dz*V_r[6]),
                 1- delta_t[j]*A_s[7]*kz[7,j]/(dz*V_r[7]) + 0 ] , 0)+ \
         np.diag([ delta_t[j]*A_s[2]*kz[2,j]/(V_r[2]*dz) , 
                     delta_t[j]*A_s[3]*kz[3,j]/(dz*V_r[3]),
                     delta_t[j]*A_s[4]*kz[4,j]/(dz*V_r[4]), 
                     delta_t[j]*A_s[5]*kz[5,j]/(dz*V_r[5]),
                     delta_t[j]*A_s[6]*kz[6,j]/(dz*V_r[6]),
                     delta_t[j]*A_s[7]*kz[7,j]/(dz*V_r[7])] , 1)+ \
             np.diag([ delta_t[j]*A_s[2]*kz[2,j]/(dz*V_r[1]),
                         +delta_t[j]*A_s[3]*kz[3,j]/(dz*V_r[2]), 
                         +delta_t[j]*A_s[4]*kz[4,j]/(dz*V_r[3]),
                         +delta_t[j]*A_s[5]*kz[5,j]/(dz*V_r[4]),
                         +delta_t[j]*A_s[6]*kz[6,j]/(dz*V_r[5]),
                         +delta_t[j]*A_s[7]*kz[7,j]/(dz*V_r[6]) ] , -1)
                
    
    
        b=C[:,j-1].copy()
        b[0]= b[0]+(0.08)*deltat[j]*A_s[1]*kz[1,j]/(deltaz*V_r[1])# C[0=layer 13.5m ]-C[1=layer 14m]=0.1
        solution= np.linalg.solve(Factor_dig , b-deltat[j]*( (A_l[1:]/V_r[1:]) * ja*Theta_j(temp[:,j]) + jv *Theta_j(temp[:,j])))
        #if I want to correct based on the tempaerture of averaged in between two days:
        #solution= np.linalg.solve(Factor_dig , b-deltat[j]*( (Al/Vr) * ja*Theta_j((temp[:,j] +temp[: , j-1])/2) + jv *Theta_j((temp[:,j] +temp[: , j-1])/2)))
            
        C[:,j]=solution
 
    C = np.where(C < 0, 0, C).T   
    num_days = C.shape[0] // num_time_steps_subdaily
    #C_3d in shape of day number , subdaily number , each layer
    C_3d = np.reshape(C[:num_days*num_time_steps_subdaily], (num_days, num_time_steps_subdaily, -1))

    # Take mean along second dimension to get DO_profile_daily
    #C_daily in shape of day number ,each layer
    C_daily = np.mean(C_3d, axis=1) 
    #print (C_daily)
    #C_daily= np.concatenate(( initial_cond.reshape(1, -1),C_daily ))
    #last_index_day=np.arange(num_time_steps_subdaily-1, C.shape[0], num_time_steps_subdaily)
    #C_daily =C[last_index_day]
    
    
    DO_ave_model=np.dot(C_daily, Vr)/ sum(Vr) 
    #print (DO_ave_model)
    return (C_daily , DO_ave_model)  



#%%rewrite the implicit method in the way it can be flexiable with the size of the matrix n for the depth variation 

"""    
C_2019_1 , C_ave_2019_1 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_fortnightly_2D_2019_1_daily,  initial_cond=inital_coulmn_2019_1
                     , deltat=deltat_2019_1 , temp=temp_daily_2D_2019_1_below135 )#kz_jp_hypo_weekly_2D_2019_1_daily #kz_jp_hypo_daily_2D_2019_1(? a day lower )

    
initial_cond=inital_coulmn_2019_1 
kz_array=kz_jp_hypo_fortnightly_2D_2019_1_daily
deltat=deltat_2019_1
temp=temp_daily_2D_2019_1_below135
params=[0.3, 0.1, 1/2]
"""




def do_one_stratification_implicit(params, kz_array, initial_cond, deltat, temp):
    
    deltat=deltat[1:]
    temp_jz_correction =(temp[1:, :]+temp[:-1, :])/2 # removing the day before onset 
    #kz_array=kz_array[: , 1:]
    
    
    jv, ja, scale_subdaily = params
    n = 7
    num_time_steps_subdaily = int(1 / scale_subdaily)
    deltat = scale_subdaily * np.tile(deltat, (num_time_steps_subdaily, 1)).transpose().flatten()
    m = len(deltat)  
    temp_subdaily = np.repeat(temp_jz_correction, num_time_steps_subdaily, axis=0)
    deltaz = 0.5
    #As= A_s[1:]
    #Vr = V_r[1:]
    #Al = A_l[1:]
    depth_levels = 7#len(As)
    Factor_dig = np.zeros((depth_levels, depth_levels))

    
    kz = np.repeat(kz_array, num_time_steps_subdaily, axis=0)
    kz = (24 * 3600 * kz).T

    def Theta_j(temp):
        theta = 1.087
        return theta ** (temp - 20)

    temp = temp_subdaily[:, 1:].T#excluding the 13.5m layer
    lhs = initial_cond#is there for day before onset# - deltat[0] * ((Al / Vr) * ja * Theta_j(temp[:, 0]) + jv * Theta_j(temp[:, 0]))

    C = np.zeros((n, m+1))# m+1 because I want to have day before onset as well in this array 
    C[:, 0] = lhs
    
    for j in range(0, m):#time
    
    
        for i in range(depth_levels):#n 
            if i == 0:
                Factor_dig[i, i] = 1 + deltat[j] * A_s[i + 2] * kz[i + 2, j] / (V_r[i+1] * deltaz)
                Factor_dig[i, i + 1] = -deltat[j] * A_s[i + 2] * kz[i + 2, j] / (V_r[i+1] * deltaz)
            elif i == depth_levels - 1:#i==6
                Factor_dig[i, i] = 1 + deltat[j] * A_s[i+1] * kz[i+1, j] / (V_r[i+1] * deltaz)
                Factor_dig[i, i - 1] = -deltat[j] * A_s[i+1] * kz[i+1, j] / (V_r[i+1] * deltaz)
            else:
                Factor_dig[i, i] = 1 + deltat[j] * A_s[i+1] * kz[i+1, j] / (V_r[i+1] * deltaz) + deltat[j] * A_s[i + 2] * kz[i + 2, j] / (deltaz * V_r[i+1])
                Factor_dig[i, i - 1] = -deltat[j] * A_s[i+1] * kz[i+1, j] / (V_r[i+1] * deltaz)
                Factor_dig[i, i + 1] = -deltat[j] * A_s[i+2] * kz[i+2, j] / (deltaz * V_r[i+1])

    
    
        b = C[:, j ].copy()
        b[0] = b[0] + (0.08) * deltat[j] * A_s[1] * kz[1, j] / (deltaz * V_r[1])
        solution = np.linalg.solve(Factor_dig, b - deltat[j] * ((A_l[1:] / V_r[1:]) * ja * Theta_j(temp[:,j]) + jv * Theta_j(temp[:,j])))
        C[:, j+1] = solution
        
        #print("Press Enter to continue...")
        #input()
        #print( C[:, j])
        
        
    #print (C)    
    C = np.where(C < 0, 0, C).T# time , depth
    
    num_days = (C.shape[0]-1) // num_time_steps_subdaily
    
    C_ddp=C[1:, :]
    C_3d = np.reshape(C_ddp [:num_days * num_time_steps_subdaily], (num_days, num_time_steps_subdaily, -1))
    #C_3d should be in size of num_days , num_time_steps_subdaily , depth_length
    C_daily = np.mean(C_3d, axis=1)#C_3d[:, -1, :]


    #C_daily= np.concatenate(( initial_cond.reshape(1, -1),C_daily ))# note that initial_cond is equal to C[0, :] and it doesnt make sense for calibration perpous to be included 
    #print("Press Enter to continue...")
    #input()
    #print(C_daily)
    DO_ave_model = np.dot(C_daily, V_r[1:]) / sum(V_r[1:])

    return C_daily, DO_ave_model

#%%

hypo_morphology_vriables_grid = V_r[1:], A_s[1:], A_l[1:], 0.5, 7 
#A_s, V_r,A_l, and kz_array have 8 demention for depth size which is 1+depth_hypo 
# they also have the information of layer 13.5m 
# but in terms of size Kz_array only definded for deoxygenation period 

delta_t= deltat_2019_1[1:]




#%%DO below14
# including a day before onset values 
df_str_2018_1_14_below14= df_str_2018_1_14[df_str_2018_1_14['Z_m']<-13.5]
df_str_2019_1_14_below14= df_str_2019_1_14[df_str_2019_1_14['Z_m']<-13.5]
df_str_2019_2_14_below14= df_str_2019_2_14[df_str_2019_2_14['Z_m']<-13.5]
df_str_2020_1_14_below14= df_str_2020_1_14[df_str_2020_1_14['Z_m']<-13.5]
df_str_2021_1_14_below14= df_str_2021_1_14[df_str_2021_1_14['Z_m']<-13.5]
df_str_2022_1_14_below14= df_str_2022_1_14[df_str_2022_1_14['Z_m']<-13.5]



# including a day before onset values 
df_str_nomixing_2018_1_14_below14= df_str_nomixing_2018_1_14[df_str_nomixing_2018_1_14['Z_m']<-13.5]
df_str_nomixing_2019_1_14_below14= df_str_nomixing_2019_1_14[df_str_nomixing_2019_1_14['Z_m']<-13.5]
df_str_nomixing_2019_2_14_below14= df_str_nomixing_2019_2_14[df_str_nomixing_2019_2_14['Z_m']<-13.5]
df_str_nomixing_2020_1_14_below14= df_str_nomixing_2020_1_14[df_str_nomixing_2020_1_14['Z_m']<-13.5]
df_str_nomixing_2021_1_14_below14= df_str_nomixing_2021_1_14[df_str_nomixing_2021_1_14['Z_m']<-13.5]
df_str_nomixing_2022_1_14_below14= df_str_nomixing_2022_1_14[df_str_nomixing_2022_1_14['Z_m']<-13.5]



#%%
def do_obs_weighted_ave(do_obs, V , datetime_3years):
    return ((do_obs * V).groupby(datetime_3years)).sum() / ((V).groupby(datetime_3years)).sum() 



#%% COMPARING TWO FUNCTIONS : resuts the same : 
params=[0.01, 1.136, 1]
    

C_2020_1 , C_ave_2020_1 =do_one_stratification_implicit([0.01 , 1.136 , 1/24] , kz_array=kz_jp_hypo_weekly_2D_2020_1_daily, initial_cond=inital_coulmn_2020_1
                     , deltat=deltat_2020_1 , temp=temp_daily_2D_2020_1_below135 )


C_2020_1_a , C_ave_2020_1_a =do_oneyear_implicit([0.01 , 1.136 , 1/24] , kz_array=kz_jp_weekly_profile_2020_1, initial_cond=inital_coulmn_2020_1
                     , deltat=deltat_2020_1 , temp=temp_daily_2D_2020_1_below135 )


C_2020_1== C_2020_1_a
C_ave_2020_1==C_ave_2020_1_a
#yes there are the same at any timestep 





# daily testing the function 
import numpy as np
from scipy.linalg import solve

coefficients= np.array ([ [0.96202, 0.03798, 0, 0, 0, 0, 0],
                         [0.06246, 0.884464, 0.053076, 0, 0, 0, 0],
                         [0, 0.053076, 0.903234, 0.04369, 0, 0, 0],
                         [0, 0, 0.04369, 0.922, 0.034307, 0, 0],
                         [0, 0, 0, 0.05118, 0.90954, 0.03928, 0],
                         [0, 0, 0, 0, 0.077322, 0.86465, 0.0580302],
                         [0, 0, 0, 0, 0, 0.019803, 0.980197] ])

constants=[11.3421, 11.358716, 11.36945, 11.38074, 11.3448, 11.21643, 11.218977]
C_day1=solve(coefficients, constants)

print (C_day1)
array([11.34142114, 11.35929529, 11.36941527, 11.38250426, 11.34874271,
       11.20437856, 11.21927193])
      
      
#answer of function of coding :
        
11.35189502, 11.35883667, 11.36931369, 11.37904443, 11.34212216,
 11.22512848, 11.21909488        
        
 
    
#every 8 hours 
params=[0.01 , 1.136 , 1/3]
 
[11.4707230, 11.4791198, 11.4895497, 11.5002086,
        11.4949572, 11.4595781, 11.4663958]  






#hourly 
params=[0.01, 1.136, 1/24]

[11.4373190, 11.4452626, 11.4557473, 11.4664439,
 11.4524375, 11.3919987, 11.3967630]
  




#first day of future str 


coefficients= np.array ([ [-27.50043, 28.50043, 0, 0, 0, 0, 0],
                         [46.86601, -91.214877, 45.348867, 0, 0, 0, 0],
                         [0, 45.348867,-87.618517, 43.26965, 0, 0, 0],
                         [0, 0, 43.26965, -82.909191, 40.639541, 0, 0],
                         [0, 0, 0, 60.63263, -114.6468299, 55.0141999, 0],
                         [0, 0, 0, 0, 108.287444,-224.791921, 117.504477],
                         [0, 0, 0, 0, 0, 40.09872, -39.09872] ])

constants=[9.56764, 12.84467, 12.845596, 12.84631676, 12.8148755, 12.721347, 12.714973]
C_day1=solve(coefficients, constants)

#answer 
array([12.17265046, 12.08124796, 12.00362203, 11.94172473, 11.89808048,
       11.86664368, 11.84494656])

















#%%Function of valibrastion with 2019-2020
from sklearn.metrics import mean_squared_error
import math

#params=[0.01, 1.15 , 1]

def calibration_implicit_2019_2020 (params ):
    jv, ja , scale_subdaily=params
    
   
    #C_2018_1 , C_ave_2018_1 =do_one_stratification_implicit(params , kz_array=kz_jp_weekly_profile_2018_1 ,  initial_cond=inital_coulmn_2018_1
    #                    , deltat=deltat_2018_1 , temp=temp_daily_2D_2018_1_below135 )
    C_2019_1 , C_ave_2019_1 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_weekly_2D_2019_1_daily,  initial_cond=inital_coulmn_2019_1
                        , deltat=deltat_2019_1 , temp=temp_daily_2D_2019_1_below135 )#kz_jp_hypo_fortnightly_2D_2019_1_daily#kz_jp_hypo_weekly_2D_2019_1_daily #kz_jp_hypo_daily_2D_2019_1(? a day lower )
    
    temp_hypo_ave_end_2019_1=np.dot (temp_daily_2D_2019_1_below135[-1 , 1:] ,  V_r[1:])/sum( V_r[1:])
    
    last_day_sat_2019_1= C_ave_2019_1[-1 ]/C_satur(temp_hypo_ave_end_2019_1, 1)
    
    est_repl_duartion_2019_2= (min(df_str_2019_2_14.index)- max(df_str_2019_1_14.index)).days

    repl_increase_do_sat_2019_2= (est_repl_duartion_2019_2*2.7861/100) #3.4902# 2.7861

    est_sat_onset_2019_2= repl_increase_do_sat_2019_2+ last_day_sat_2019_1

    #inital_coulmn_2019_2= C_satur(temp_coulmn_2019_2 , est_sat_onset_2019_2 )
    
    inital_coulmn_2019_2= C_satur(temp_coulmn_2019_2 , 1)
    
    C_2019_2 , C_ave_2019_2 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_weekly_2D_2019_2_daily, initial_cond=inital_coulmn_2019_2
                        , deltat=deltat_2019_2 , temp=temp_daily_2D_2019_2_below135 )#kz_jp_hypo_weekly_2D_2019_2_daily ,kz_jp_hypo_fortnightly_2D_2019_2_daily,kz_jp_hypo_daily_2D_2019_2
   # C_2020_1 , C_ave_2020_1 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_fortnightly_2D_2020_1_daily, initial_cond=inital_coulmn_2020_1
   #                     , deltat=deltat_2020_1 , temp=temp_daily_2D_2020_1_below135 )#kz_jp_hypo_weekly_2D_2020_1_daily# kz_jp_hypo_daily_2D_2020_1# kz_jp_hypo_fortnightly_2D_2020_1_daily
   # C_2021_1 , C_ave_2021_1 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_fortnightly_2D_2021_1_daily, initial_cond=inital_coulmn_2021_1
   #                    , deltat=deltat_2021_1 , temp=temp_daily_2D_2021_1_below135 )#kz_jp_hypo_weekly_2D_2021_1_daily,kz_jp_hypo_fortnightly_2D_2021_1_daily, kz_jp_hypo_daily_2D_2021_1
    #C_2022_1 , C_ave_2022_1 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_fortnightly_2D_2022_1_daily, initial_cond=inital_coulmn_2022_1
   #                     , deltat=deltat_2022_1 , temp=temp_daily_2D_2022_1_below135 )#kz_jp_hypo_weekly_2D_2022_1_daily,kz_jp_hypo_fortnightly_2D_2022_1_daily, kz_jp_hypo_daily_2D_2022_1
    """
    C_2019_1 , C_ave_2019_1 =do_oneyear_Jz(params ,inital_cond=inital_coulmn_2019_1, deltat=deltat_2019_1, temp=temp_daily_2D_2019_1_below135)
    C_2019_2 , C_ave_2019_2 =do_oneyear_Jz(params ,inital_cond=inital_coulmn_2019_2, deltat=deltat_2019_2, temp=temp_daily_2D_2019_2_below135)
    C_2020_1 , C_ave_2020_1 =do_oneyear_Jz(params ,inital_cond=inital_coulmn_2020_1, deltat=deltat_2020_1, temp=temp_daily_2D_2020_1_below135)
    C_2021_1 , C_ave_2021_1 =do_oneyear_Jz(params ,inital_cond=inital_coulmn_2021_1, deltat=deltat_2021_1,temp=temp_daily_2D_2021_1_below135)
    C_2022_1 , C_ave_2022_1 =do_oneyear_Jz(params ,inital_cond=inital_coulmn_2022_1, deltat=deltat_2022_1 ,temp=temp_daily_2D_2022_1_below135)
    """                    

    #if I do not consider the first day before onset for calibration 
    #C_2019_2020=np.concatenate((C_2019_1[1:,] , C_2019_2[1:,]  ,  C_2020_1[1:,]  , C_2021_1[1:,]  , C_2022_1[1:,]  ))##,   , C_2019_1 , C_2019_2 , C_2019_1 , C_2019_2 ,np.concatenate((C_2018_1, C_2019_1 , C_2019_2 ,C_2020_1,C_2021_1,  C_2022_1 ))#   , , , C_2022_1 #   , C_2021_1 , C_2022_1))# axis=1
    #C_ave_2019_2020= np.concatenate ([C_ave_2019_1[1:], C_ave_2019_2[1:], C_ave_2020_1[1:] ,C_ave_2021_1[1:], C_ave_2022_1[1:]  ])# ,,,,C_ave_2022_1,  ,,C_ave_2019_1,  C_ave_2019_2 ,np.concatenate ([C_ave_2018_1, C_ave_2019_1,  C_ave_2019_2 ,C_ave_2020_1,  C_ave_2021_1,C_ave_2022_1])#  , ,  ,   ,  
    
    #df_str_2019_2020_below14=pd.concat([df_str_nomixing_2019_1_14_below14, df_str_nomixing_2019_2_14_below14, df_str_nomixing_2020_1_14_below14, df_str_nomixing_2021_1_14_below14 , df_str_nomixing_2022_1_14_below14])
    
    C_2019_2020=np.concatenate(( C_2019_1 , C_2019_2   ))##, C_2020_1 , , C_2021_1  C_2022_1,   , C_2019_1 , C_2019_2 , C_2019_1 , C_2019_2 ,np.concatenate((C_2018_1, C_2019_1 , C_2019_2 ,C_2020_1,C_2021_1,  C_2022_1 ))#   , , , C_2022_1 #   , C_2021_1 , C_2022_1))# axis=1
    C_ave_2019_2020= np.concatenate ([C_ave_2019_1, C_ave_2019_2])#, C_ave_2020_1  ,C_ave_2021_1, C_ave_2022_1 ,,,,C_ave_2022_1,  ,,C_ave_2019_1,  C_ave_2019_2 ,np.concatenate ([C_ave_2018_1, C_ave_2019_1,  C_ave_2019_2 ,C_ave_2020_1,  C_ave_2021_1,C_ave_2022_1])#  , ,  ,   ,  
   
    #dataframes below includ the day before onsets:
    #df_str_2019_2020_below14=pd.concat([df_str_2019_1_14_below14 , df_str_2019_2_14_below14 ]) #,df_str_2020_1_14_below14, df_str_2021_1_14_below14 , df_str_2022_1_14_below14 , , #df_str_2019_1_14_below14 , df_str_2019_2_14_below14 ,pd.concat([ df_str_2018_1_14_below14 , df_str_2019_1_14_below14 , df_str_2019_2_14_below14 , df_str_2020_1_14_below14,df_str_2021_1_14_below14, df_str_2022_1_14_below14  ]) #,   , , df_str_2022_1_14_below14  ,,
   
    #dataframes below exclud the day before onsets:
    df_str_2019_2020_below14=pd.concat([df_str_nomixing_2019_1_14_below14, df_str_nomixing_2019_2_14_below14 ])#, df_str_nomixing_2020_1_14_below14, df_str_nomixing_2021_1_14_below14, df_str_nomixing_2022_1_14_below14
    
    
    DO_prof_obs=two_D_array_from_df(df_str_2019_2020_below14 , 'DO' )
    DO_ave_obs= do_obs_weighted_ave(df_str_2019_2020_below14['DO'], df_str_2019_2020_below14['V_r_m'], df_str_2019_2020_below14.index)
    
    MSE_prof = mean_squared_error(C_2019_2020 , DO_prof_obs)
    # For each corresponding pair of predicted and observed DO profiles, calculate the squared difference.
    #Sum up all these squared differences.
    #Divide the sum by the total number of data points (which is the number of profiles in this case) to get the average squared difference, i.e., the mean squared error.
    RMSE_prof=math.sqrt(MSE_prof)
    
    MSE_ave = mean_squared_error(C_ave_2019_2020, DO_ave_obs)
    RMSE_ave=math.sqrt(MSE_ave)

    return (RMSE_ave , RMSE_prof , C_ave_2019_2020 , C_2019_2020 , DO_ave_obs)   



#%%Function of validation with 2021
from sklearn.metrics import mean_squared_error
import math


def validation_implicit_2021 (params ):
    jv, ja , scale_subdaily=params
    
    C_2020_1 , C_ave_2020_1 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_fortnightly_2D_2020_1_daily, initial_cond=inital_coulmn_2020_1
                                                            , deltat=deltat_2020_1 , temp=temp_daily_2D_2020_1_below135 )#kz_jp_hypo_weekly_2D_2021_1_daily,kz_jp_hypo_fortnightly_2D_2021_1_daily, kz_jp_hypo_daily_2D_2021_1
    
    C_2021= C_2020_1# axis=1
    
    C_ave_2021=  C_ave_2020_1
    
    
    df_str_2021_below14= df_str_2020_1_14_below14.copy()
    #C_2022_1 , C_ave_2022_1 =do_one_stratification_implicit(params , kz_array=kz_jp_hypo_weekly_2D_2022_1_daily, initial_cond=inital_coulmn_2022_1
    #                                                        , deltat=deltat_2022_1 , temp=temp_daily_2D_2022_1_below135 )#kz_jp_hypo_weekly_2D_2022_1_daily,kz_jp_hypo_fortnightly_2D_2022_1_daily, kz_jp_hypo_daily_2D_2022_1
                  
    #C_2021= C_2022_1# axis=1
    
    #C_ave_2021=  C_ave_2022_1
    
    #df_str_2021_below14= df_str_2022_1_14_below14.copy()
    

   
    DO_prof_obs=two_D_array_from_df(df_str_2021_below14 , 'DO' )
    DO_ave_obs= do_obs_weighted_ave(df_str_2021_below14['DO'], df_str_2021_below14['V_r_m'], df_str_2021_below14.index)
    
    MSE_prof = mean_squared_error(C_2021 , DO_prof_obs)
    RMSE_prof=math.sqrt(MSE_prof)
    
    MSE_ave = mean_squared_error(C_ave_2021, DO_ave_obs)
    RMSE_ave=math.sqrt(MSE_ave)

    return (RMSE_ave , RMSE_prof , C_ave_2021 , C_2021 , DO_ave_obs)   



#%%calibration timeseries 


C_2020_2021_ave_model_calib=calibration_implicit_2019_2020([min_jv, min_ja, 1])[2]
C_2020_2021_ave_obs= calibration_implicit_2019_2020([min_jv, min_ja, 1])[4]




time_index= C_2020_2021_ave_obs.index
model_results= C_2020_2021_ave_model_calib
observed_values= C_2020_2021_ave_obs



plt.figure(figsize=(12, 10))
# Plotting the model results as dots
plt.scatter(time_index, model_results, label='Model Results', color='blue')

# Plotting the observed values as dots
plt.scatter(time_index, observed_values, label='Observed Values', color='red')



# Adding labels and legend
plt.ylabel('Hypolimnetic DO average[mg/L]')
plt.legend()

# Show the plot
plt.show()


#%%validation timesries 

print (validation_implicit_2021 ([min_jv, min_ja, 1] )[1])

C_2022_ave_model_validation=validation_implicit_2021 ([min_jv, min_ja, 1] )[2]
C_2022_ave_obs_validation=validation_implicit_2021 ([min_jv, min_ja, 1] )[4]



time_index= C_2022_ave_obs_validation.index
model_results= C_2022_ave_model_validation
observed_values= C_2022_ave_obs_validation



plt.figure(figsize=(12, 10))
# Plotting the model results as dots
plt.scatter(time_index, model_results, label='Model Results', color='blue')

# Plotting the observed values as dots
plt.scatter(time_index, observed_values, label='Observed Values', color='red')



# Adding labels and legend
plt.ylabel('Hypolimnetic DO average[mg/L]')
plt.legend()

# Show the plot
plt.show()

#%%hypolimnetic_anoxic_factor


def hypolimnetic_anoxic_factor(C_y_n, depth ,  time_y_n  , A_sediment_prof,
                               threshold=0.5, A0=23.67*10**6 , time_subset=None, 
                               depth_subset=None):# unite of d y-1
    
    # Step 1: Find the indices that correspond to the relevant depth and time periods
    depth_indices = np.where(np.isin(depth, depth_subset))[0] if depth_subset is not None else None
    time_indices = np.where(np.isin(time_y_n, time_subset))[0] if time_subset is not None else None

    # Step 2: Subset the array based on depth_subset and time_subset
    if depth_indices is not None:
        C_y_n = C_y_n[:, depth_indices]
        A_sediment_prof= A_sediment_prof[depth_indices ]
    if time_indices is not None:
        C_y_n = C_y_n[time_indices]
        
        
    subset_array = C_y_n  # You can update this based on your depth_subset and time_subset criteria

    # Step 2: Apply the threshold to constrain the array values
    constrained_array = np.where(subset_array < threshold, 1, 0)

    # Step 3: Multiply each element in the constrained array by the relevant sediment area for each layer
    # Step 4: Sum the products obtained in step 3 for each layer
    hypolimnetic_anoxic_factor_daily = np.dot(constrained_array , ((A_sediment_prof/ A0)))


    # Step 5: Divide the sum from step 4 by the fixed surface area to get the hypolimnetic anoxic factor
  
    hypolimnetic_anoxic_factor_daily_indexed = pd.DataFrame({'hypolimnetic_anoxic_factor_daily': hypolimnetic_anoxic_factor_daily}, index=time_y_n)

    annual_hypolimnetic_anoxic_factor = hypolimnetic_anoxic_factor_daily_indexed.index.year
    annual_hypolimnetic_anoxic_factor = hypolimnetic_anoxic_factor_daily_indexed.groupby(annual_hypolimnetic_anoxic_factor).sum()

    return annual_hypolimnetic_anoxic_factor


#the anoxic factor for each observed year


#model_2019_1

hypolimnetic_anoxic_factor(C_y_n=C_2019_1, depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2019_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0(threshold= 0.5)#0((threshold= 2))

#obs_2019_1
DO_prof_obs_2019_1=two_D_array_from_df(df_str_2019_1_14_below14 , 'DO' )


hypolimnetic_anoxic_factor(C_y_n=DO_prof_obs_2019_1 , depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2019_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0(threshold= 0.5)#0((threshold= 2))




#model_2019_2
hypolimnetic_anoxic_factor(C_y_n=C_2019_2, depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2019_2_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0.597909(threshold= 0.5)#0.662548(threshold= 2)

#obs
DO_prof_obs_2019_2=two_D_array_from_df(df_str_2019_2_14_below14 , 'DO' )


hypolimnetic_anoxic_factor(C_y_n=DO_prof_obs_2019_2 , depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2019_2_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0.372624#0.468631


#model_2020
hypolimnetic_anoxic_factor(C_y_n=C_2020_1, depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2020_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0.807985#0.904943
#obs
DO_prof_obs_2020_1=two_D_array_from_df(df_str_2020_1_14_below14 , 'DO' )


hypolimnetic_anoxic_factor(C_y_n=DO_prof_obs_2020_1 , depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2020_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0.758555#0.953422

#model_2021
hypolimnetic_anoxic_factor(C_y_n=C_2021_1, depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2021_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#-> 0.614068# 0.727186
#obs
DO_prof_obs_2021_1=two_D_array_from_df(df_str_2021_1_14_below14 , 'DO' )


hypolimnetic_anoxic_factor(C_y_n=DO_prof_obs_2021_1 , depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2021_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0.558935# 0.678707


#model_2022
hypolimnetic_anoxic_factor(C_y_n=C_2022_1, depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2022_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#-> 0.937262#  1.018061

#obs
DO_prof_obs_2022_1=two_D_array_from_df(df_str_2022_1_14_below14 , 'DO' )


hypolimnetic_anoxic_factor(C_y_n=DO_prof_obs_2022_1 , depth=depth_levels[1:].copy()
                           ,  time_y_n =(df_str_2022_1_14_below14.index.unique()).copy()
                           , A_sediment_prof=A_l[1:], threshold=2, A0=23.67*10**6 
                           , depth_subset=-16)#0.665399# 0.743346


anoxic_factor_obs=[(2019 , 0.33),(2020, 0.71), (2021 , 0.42), (2022, 0.52)]
hypoxic_factor_obs= [ (2019 ,0.47 ), (2020 ,0.95), (2021, 0.68), (2022, 0.74)]


anoxic_factor_calibval=[(2019 , 0.597909),(2020,0.807985), (2021 , 0.614068), (2022, 0.937262)]
hypoxic_factor_calibval= [ (2019 ,0.662548 ), (2020 ,0.904943), (2021, 0.727186), (2022, 1.018061)]

"""
glue_df_annual_anoxic_factor_rcp85[(glue_df_annual_anoxic_factor_rcp85.index > 2018) & (glue_df_annual_anoxic_factor_rcp85.index<2023)]
Out[1531]: 
                5%       50%       95%
Datetime                              
2019      3.226963  5.021617  8.258585
2020      3.029551  5.579669  9.856759
2021      2.048412  7.875364  9.763056
2022      4.814570  6.583660  8.011451

glue_df_annual_anoxic_factor_rcp26[(glue_df_annual_anoxic_factor_rcp26.index > 2018) & (glue_df_annual_anoxic_factor_rcp26.index<2023)]
Out[1532]: 
                5%       50%       95%
Datetime                              
2019      3.058328  6.415716  8.187143
2020      4.746438  7.158522  8.888696
2021      3.526748  5.976680  9.779772
2022      4.834647  7.332271  9.353958

glue_df_annual_anoxic_factor_rcp60[(glue_df_annual_anoxic_factor_rcp60.index > 2018) & (glue_df_annual_anoxic_factor_rcp60.index<2023)]
Out[1533]: 
                5%       50%       95%
Datetime                              
2019      5.037123  6.802513  8.300345
2020      3.643018  6.268299  9.013193
2021      4.639605  6.196040  7.421201
2022      4.001072  7.954331  8.963711
"""

#%%
def hypolimnetic_hypoxia_duration(data , datetime_index, threshold=2):
    # Convert the index to datetime if it's not already
    data.index = pd.to_datetime(data.index)
    
    # Filter the data based on the threshold
    below_threshold = data[data< threshold]
    
    # Group by year and count the number of days below threshold
    count_per_year = below_threshold.groupby(below_threshold.index.year)['ave_hypo_do'].count()
    
    return count_per_year





#2019_1_obs: 
DO_ave_obs_2019_1= do_obs_weighted_ave(df_str_2019_1_14_below14['DO'], df_str_2019_1_14_below14['V_r_m'], df_str_2019_1_14_below14.index)
count_per_obs_year_2019_1= DO_ave_obs_2019_1[DO_ave_obs_2019_1<2].count()#0
count_per_obs_year_2019_1= DO_ave_obs_2019_1[DO_ave_obs_2019_1<0.5].count()#0
Jul_Aug_obs_DO_ave_year_2019_1= np.mean(DO_ave_obs_2019_1[(DO_ave_obs_2019_1.index.month> 6)&(DO_ave_obs_2019_1.index.month<8)])
#nan

#2019_2:
DO_ave_obs_2019_2= do_obs_weighted_ave(df_str_2019_2_14_below14['DO'], df_str_2019_2_14_below14['V_r_m'], df_str_2019_2_14_below14.index)
count_per_obs_year_2019_2= DO_ave_obs_2019_2[DO_ave_obs_2019_2<2].count()#25
count_per_obs_year_2019_2= DO_ave_obs_2019_2[DO_ave_obs_2019_2<0.5].count()#13
Jul_Aug_obs_DO_ave_year_2019_2= np.mean(DO_ave_obs_2019_2[(DO_ave_obs_2019_2.index.month> 6)&(DO_ave_obs_2019_2.index.month<8)])
#5.430675572058178

#2020_obs: 
DO_ave_obs_2020_1= do_obs_weighted_ave(df_str_2020_1_14_below14['DO'], df_str_2020_1_14_below14['V_r_m'], df_str_2020_1_14_below14.index)

count_per_obs_year_2020_1= DO_ave_obs_2020_1[DO_ave_obs_2020_1<2].count()#55
count_per_obs_year_2020_1= DO_ave_obs_2020_1[DO_ave_obs_2020_1<0.5].count()#39
Jul_Aug_obs_DO_ave_year_2020_1= np.mean(DO_ave_obs_2020_1[(DO_ave_obs_2020_1.index.month> 6)&(DO_ave_obs_2020_1.index.month<8)])
#1.394143846937668


#2021_obs: 
DO_ave_obs_2021_1= do_obs_weighted_ave(df_str_2021_1_14_below14['DO'], df_str_2021_1_14_below14['V_r_m'], df_str_2021_1_14_below14.index)

count_per_obs_year_2021_1= DO_ave_obs_2021_1[DO_ave_obs_2021_1<2].count()#41
count_per_obs_year_2021_1= DO_ave_obs_2021_1[DO_ave_obs_2021_1<0.5].count()#27
Jul_Aug_obs_DO_ave_year_2021_1= np.mean(DO_ave_obs_2021_1[(DO_ave_obs_2021_1.index.month> 6)&(DO_ave_obs_2021_1.index.month<8)])
#2.3606301327145838

# obs_2022: 
DO_ave_obs_2022_1= do_obs_weighted_ave(df_str_2022_1_14_below14['DO'], df_str_2022_1_14_below14['V_r_m'], df_str_2022_1_14_below14.index)

count_per_obs_year_2022_1= DO_ave_obs_2022_1[DO_ave_obs_2022_1<2].count()#48
count_per_obs_year_2022_1= DO_ave_obs_2022_1[DO_ave_obs_2022_1<0.5].count()#36
Jul_Aug_obs_DO_ave_year_2022_1= np.mean(DO_ave_obs_2022_1[(DO_ave_obs_2022_1.index.month> 6)&(DO_ave_obs_2022_1.index.month<8)])
#1.9010069759763801


below_threshold = np.all(DO_prof_obs_2019_2 < 0.5, axis=1)

# Count the number of days where the condition is met
number_of_days = np.sum(below_threshold)
[10 , 33 , 24, 33]# 100

#anoxic duartion: 
[13, 39, 27, 26]

#full-anoxia_duration 
"""
glue_len_anoxia_full_prof_inyear_rcp26[(glue_len_anoxia_full_prof_inyear_rcp26.index>2018)&(glue_len_anoxia_full_prof_inyear_rcp26.index<2023)]
                 5%   50%   95%
Datetime                       
2019      20.510072  45.602675   59.0
2020      42.290880  58.000000   99.0
2021      48.008359  84.039887  106.0
2022      34.260078  52.515292   68.0


glue_len_anoxia_full_prof_inyear_rcp60[(glue_len_anoxia_full_prof_inyear_rcp60.index>2018)&(glue_len_anoxia_full_prof_inyear_rcp60.index<2023)]
                 5%   50%   95%
Datetime                       
2019      37.019642  54.0  98.0
2020      24.643778  44.0  65.0
2021      33.003697  44.0  53.0
2022      27.758318  57.0  65.0
glue_len_anoxia_full_prof_inyear_rcp85[(glue_len_anoxia_full_prof_inyear_rcp85.index>2018)&(glue_len_anoxia_full_prof_inyear_rcp85.index<2023)]
                 5%   50%   95%
Datetime                       
2019      22.525459  35.502509   59.288065
2020      20.760476  50.071853  127.000000
2021      13.267187  57.000000   70.289823
2022      34.056119  47.000000   58.000000
"""

########DO in Jul-Aug
#observation : [1.394143846937668, 2.3606301327145838, 1.9010069759763801]
#average of 1.8852603185428773-> Seems more closer to RCP6.0 withthe average of 1.050510 in thoses years in Jul-Auguest 

"""
glue_df_Jul_Aug_hypolimnetic_ave_rcp26[(glue_df_Jul_Aug_hypolimnetic_ave_rcp26.index>2018)&(glue_df_Jul_Aug_hypolimnetic_ave_rcp26.index<2023)]

                5%       50%       95%
Datetime                              
2019      0.201976  0.790041  3.686771
2020      0.048906  0.722317  1.996113
2021      0.039659  1.254856  3.501521
2022      0.000000  0.645085  1.702271

glue_df_Jul_Aug_hypolimnetic_ave_rcp26[(glue_df_Jul_Aug_hypolimnetic_ave_rcp26.index>2019)&(glue_df_Jul_Aug_hypolimnetic_ave_rcp26.index<2023)].mean()
Out[1624]: 
5%     0.029522
50%    0.874086
95%    2.399968
dtype: float64


glue_df_Jul_Aug_hypolimnetic_ave_rcp60[(glue_df_Jul_Aug_hypolimnetic_ave_rcp60.index>2018)&(glue_df_Jul_Aug_hypolimnetic_ave_rcp60.index<2023)]

                5%       50%       95%
Datetime                              
2019      0.188258  0.652683  1.680859
2020      0.222251  1.343094  3.260655
2021      0.447228  1.317433  2.015958
2022      0.000191  0.491003  1.888039

glue_df_Jul_Aug_hypolimnetic_ave_rcp60[(glue_df_Jul_Aug_hypolimnetic_ave_rcp60.index>2019)&(glue_df_Jul_Aug_hypolimnetic_ave_rcp60.index<2023)].mean()
Out[1625]: 
5%     0.223223
50%    1.050510
95%    2.388217
dtype: float64



glue_df_Jul_Aug_hypolimnetic_ave_rcp85[(glue_df_Jul_Aug_hypolimnetic_ave_rcp85.index>2018)&(glue_df_Jul_Aug_hypolimnetic_ave_rcp85.index<2023)]

                5%       50%       95%
Datetime                              
2019      0.171752  1.968567  3.564397
2020      0.003001  1.248606  4.466077
2021      0.014438  0.364424  5.365936
2022      0.315091  0.925448  1.620153


glue_df_Jul_Aug_hypolimnetic_ave_rcp85[(glue_df_Jul_Aug_hypolimnetic_ave_rcp85.index>2019)&(glue_df_Jul_Aug_hypolimnetic_ave_rcp85.index<2023)].mean()
Out[1625]: 
5%     0.110843
50%    0.846159
95%    3.817389
dtype: float64
"""





#%%3. Justification of timestep choosing:
    
#   calibartion function : calibration_implicit_2019_2020
#   validation function : validation_implicit_2021
    

import numpy as np
import matplotlib.pyplot as plt

# Assuming you have already defined the function calibration_implicit_2019_2020()

# Define the parameter ranges and number of points
param1_name = "Jv [g m$^{-3}$ d$^{-1}$]"
param2_name = "Ja [g m$^{-2}$ d$^{-1}$]"
num_points =10
jv_min, jv_max = 0.01, 0.5#0.467 maxium all #0.222 meso trophic # minimum all 0.01
ja_min, ja_max = 0.1, 2 #1.7 maximum in meso # 2.7maxium all(two eutrophic)# minimum all 0.1



# Create arrays of parameter values spanning the ranges from min_val to max_val for both parameters
param1_values = np.linspace(jv_min, jv_max, num_points)
param2_values = np.linspace(ja_min, ja_max, num_points)
param3_values= np.array ([1 , 1/12 , 1/24, 1/(24*60), 1/(24*60*60)])


# Calculate the output of the model at each parameter combination
output_values = np.zeros((num_points, num_points , len (param3_values)))
for i, p1 in enumerate(param1_values):
    for j, p2 in enumerate(param2_values):
        for f, p3 in enumerate(param3_values):
            output_values[i, j , f] = calibration_implicit_2019_2020([p1, p2, p3])[1]


rmse_prof_y=np.min(output_values, axis=(0, 1))
timestep_x= param3_values

plt.plot(timestep_x ,rmse_prof_y )




#%%4. Create a plot for justification of timestep of 1 day
plt.figure(figsize=(8, 6))  # Set the figure size (width, height)
plt.plot(timestep_x, rmse_prof_y, color='blue',  linestyle='-', linewidth=2)

# Add labels and title
plt.xlabel('Timestep [d]', fontsize=16)
plt.ylabel('Minimum RMSE Profile [g m$^{-3}$]', fontsize=16)


# Set font size for tick labels
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# Save the figure with specified settings
plt.savefig('justification_of_timestep_va_minimum_rmse_plot.png', dpi=300, bbox_inches='tight')  # Save with 300 DPI and tight layout

# Show the plot
plt.show()




#%% GLUE method:
    
#   calibartion function : calibration_implicit_2019_2020
#   validation function : validation_implicit_2021    
    
    
rmse_max = 1#threshold for nash_sutcliff coeffient
num_points = 100# number of sampleing

jv_min, jv_max = 0.01, 0.25 #now#before:0.5#0.467 maxium all #0.222 meso trophic # minimum all 0.01
ja_min, ja_max = 0.1, 2 #1.7 maximum in meso # 2.7maxium all(two eutrophic)# minimum all 0.1


jv_linspace = np.linspace(jv_min, jv_max , num_points)# #np.random.uniform(low=jv_min, high=jv_max , size=n_samp)
ja_linspace = np.linspace(ja_min, ja_max , num_points)##np.random.uniform(low=ja_min, high=ja_max, size=n_samp)


jv_s, ja_s= np.meshgrid (jv_linspace , ja_linspace)

jv_s=jv_s.flatten()
ja_s=ja_s.flatten()
  
def run_glue(jv_s, ja_s, n_s,rmse_max):
    """ Run GLUE analysis.
        Uses RMSE_profile() to estimate performance and returns
        dataframes containing all "behavioural" parameter sets and
        associated model output.
    """
    output_values
    # Store output
    out_params = []
    sims_ave = []
    #jv_selected=[]
    #ja_selected=[]
    #sims_prof=[]
    #wholermse=[]
    # Loop over param sets
    for idx in range(len(jv_s)):
        params = [jv_s[idx], ja_s[idx] , 1]

        # Calculate Nash-Sutcliffe
        #rmse, sim , sim_prof = RMSE_ave_and_prof(params)[1]
        sim_ave= calibration_implicit_2019_2020(params)[2]
        rmse_prof = calibration_implicit_2019_2020(params)[1]
        #wholermse.append (calibration_implicit_2019_2020(params)[1])
        # Store if "behavioural" with RMSE<= rme-max
        if rmse_prof <= rmse_max:
            params.append(rmse_prof)
            out_params.append(params)
            sims_ave.append(sim_ave)
            #jv_selected.append(jv_s[idx])
            #ja_selected.append(ja_s[idx])
            #sims_prof.append(sim_prof)

    # Build df
    params_df = pd.DataFrame(data=out_params, 
                             columns=['jv', 'ja', 'timescale',  'rmse_prof'])

    assert len(params_df) > 0, 'No behavioural parameter sets found.'

    # Number of behavioural sets
    print( 'Found %s behavioural sets out of %s runs.' % (len(params_df), len(jv_s)))

    # DF of behavioural simulations
    sims_df = pd.DataFrame(data=sims_ave)
    
    #sims_prof_df= pd.DataFrame(data=sims_prof)
    
    return params_df, sims_df  #,  jv_selected , ja_selected, wholermse 

#%%run glue function:
params_df, sims_df = run_glue(jv_s, ja_s, len(jv_s), rmse_max)
    
# Save params_df to a CSV file
params_df.to_csv('GLUE_params_results_only_meso.csv', index=False)

# Save sims_df to a CSV file
sims_df.to_csv('GLUE_sims_results_only_meso.csv', index=False)    
#%%function of weighting 

def weighted_quantiles(values, quantiles, sample_weight=None):
    """ Modified from 
        http://stackoverflow.com/questions/21844024/weighted-percentile-using-numpy     
        NOTE: quantiles should be in [0, 1]
        
        values         array with data
        quantiles      array with desired quantiles
        sample_weight  array of weights (the same length as `values`)

        Returns array with computed quantiles.
    """
    # Convert to arrays
    values = np.array(values)
    quantiles = np.array(quantiles)
    
    
    # Assign equal weights if necessary
    if sample_weight is None:
        sample_weight = np.ones(len(values))
        
    # Otherwise use specified weights
    sample_weight = np.array(sample_weight)
    
    # Check quantiles specified OK
    assert np.all(quantiles >= 0) and np.all(quantiles <= 1), 'quantiles should be in [0, 1]'

    # Sort 
    sorter = np.argsort(values)
    values = values[sorter]
    sample_weight = sample_weight[sorter]

    # Compute weighted quantiles
    weighted_quantiles = np.cumsum(sample_weight) - 0.5 * sample_weight
    weighted_quantiles /= np.sum(sample_weight)
    
    return np.interp(quantiles, weighted_quantiles, values)

def glue_coverage(glue_df):
    """ Prints coverage from GLUE analysis.
    """
    # Add observations to df
    #glue_df['obs'] = y

    # Are obs within CI?
    glue_df['In_CI'] = ((glue_df['2.5%'] < glue_df['obs']) & 
                        (glue_df['97.5%'] > glue_df['obs']))

    # Coverage
    cov = 100.*glue_df['In_CI'].sum()/len(glue_df)

    return( round (cov , 2) ) 
    
#%% ploting the ave_daily of behavioural sets:

import matplotlib.dates as mdates
    
def plot_glue(params_df, sims_df):
    """ Plot median simulation and confidence intervals for GLUE.
    """
    # Get weighted quantiles for each point in x from behavioural simulations
    # weight should be in range of [0, 1] so the RMSE values should be 
    # so slected RMSE for those behavioural sets should be normalized
    #normalized based on maximum and minimum RMSE in this range
    
    #NS:weights =1 -( (params_df['rmse']- MIN_RMSE )/(MAX_RMSE- MIN_RMSE))   
    
    ###NS: weights =1 -( (params_df['rmse']- min(params_df['rmse']) )/(max(params_df['rmse'])- min(params_df['rmse'])))
    weights =abs(1 -params_df['rmse_prof'])
    params_df['weights']= weights# RMSE normalized between 0-1
    quants = [0.025, 0.5, 0.975]



    # List to store output
    out = []
   
    # Loop over each day (?) # shouldn't be over the behavioural set
    for col in sims_df.columns:
        values = sims_df[col]
        out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df = pd.DataFrame(data=out, columns=['2.5%', '50%', '97.5%'])
    obs= calibration_implicit_2019_2020([1 , 1 , 1])[4]
    x= time_steps= calibration_implicit_2019_2020([1 , 1 , 1])[4].index   
    glue_df=glue_df.set_index(x)#x
 
    
    glue_df['obs']=  obs  #y
  
    # So anytime we want to draw a line plot without connections in certain points we subset them and draw them alone
    Y=[glue_df[df_str_2019_1_14.index.min(): df_str_2019_1_14.index.max() ] ,
       glue_df[df_str_2019_2_14.index.min(): df_str_2019_2_14.index.max() ] ,
       glue_df[df_str_2020_1_14.index.min(): df_str_2020_1_14.index.max() ]]
       
 

    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))
    y_min = min([0 for y in Y])
    y_max = max([13 for y in Y])
    for k, _ in enumerate(Y):
        # Convert DatetimeIndex object to string
        #date_str = Y.index.strftime('%m/%d/%Y')
        #datetime_objs = [datetime.datetime.strptime(date, '%m/%d/%Y') for date in date_str]
        #Y.index= datetime_objs
        ax = axs.flatten()[k]  # get the current axis from the flattened array
        ax.plot(Y[k].index, Y[k]['obs'], 'bo', label='obs', alpha=0.5)
        ax.fill_between(Y[k].index, Y[k]['2.5%'], Y[k]['97.5%'], color='r', alpha=0.3)
        ax.plot(Y[k].index, Y[k]['50%'], 'r-', label='mid_model')
        ax.tick_params(axis='x', labelrotation=-45)
        if k in [0, 2]:
            ax.set_ylabel('Hypolimnietic DO average [mg.m-3]')
        ax.set_ylim(y_min, y_max)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.subplots_adjust(hspace=0.5)   
    fig.legend(labels=['obs', '95% confidence interval', 'median simulation'], loc='upper center', bbox_to_anchor=(0.5, 0.97))
    fig.suptitle('RMSE prof ave profile, %s behavioural sets out of %s, result in %%%s coverage'  % (len(params_df), len(ja_s) , glue_coverage(glue_df) ))   
    fig.savefig('GLUE_100X100_rmse_prof_threshold_1.png', bbox='tight' , dpi= 300)  
    fig.show()
    

    return glue_df
#%%
   
glue_df = plot_glue(params_df, sims_df)   

params_df.jv.mean()
# 0.1286328530906843

params_df.ja.mean()
# 0.9026455472238619
 
    
#%%validation using behavioural sets  


whole_rmse_valid=[]
sims_ave_valid=[]
JV_behavioural, JA_behavioural = params_df.jv , params_df.ja
params_df
for idx in range(len(JV_behavioural)):
    
    params = [JV_behavioural[idx], JA_behavioural[idx] , 1]

    # Calculate Nash-Sutcliffe
    #rmse, sim , sim_prof = RMSE_ave_and_prof(params)[1]
    sim_ave_valid= validation_implicit_2021(params)[2]
    whole_rmse_valid.append (validation_implicit_2021(params)[1])
    
    sims_ave_valid.append(sim_ave_valid)


#add the rmse of validation years to params dataframe:
params_df['rmse_prof_valid']=whole_rmse_valid


sims_df_valid = pd.DataFrame(data=sims_ave_valid)



########
def plot_glue_validation(params_df, sims_df):
    """ Plot median simulation and confidence intervals for GLUE.
    """
    # Get weighted quantiles for each point in x from behavioural simulations
    # weight should be in range of [0, 1] so the RMSE values should be 
    # so slected RMSE for those behavioural sets should be normalized
    #normalized based on maximum and minimum RMSE in this range
    
    #NS:weights =1 -( (params_df['rmse']- MIN_RMSE )/(MAX_RMSE- MIN_RMSE))   
    
    ###NS: weights =1 -( (params_df['rmse']- min(params_df['rmse']) )/(max(params_df['rmse'])- min(params_df['rmse'])))
    weights =1 -params_df['rmse_prof']
    params_df['weights']= weights# RMSE normalized between 0-1
    quants = [0.025, 0.5, 0.975]



    # List to store output
    out = []
   
    # Loop over each day (?) # shouldn't be over the behavioural set
    for col in sims_df.columns:
        values = sims_df[col]
        out.append(weighted_quantiles(values, quants, sample_weight=weights))

    # Build df
    glue_df = pd.DataFrame(data=out, columns=['2.5%', '50%', '97.5%'])
    obs= validation_implicit_2021([1 , 1 , 1])[4]
    x= time_steps= validation_implicit_2021([1 , 1 , 1])[4].index   
    glue_df=glue_df.set_index(x)#x
 
    
    glue_df['obs']=  obs  #y
  
    # So anytime we want to draw a line plot without connections in certain points we subset them and draw them alone
    Y=[glue_df[df_str_2021_1_14.index.min():df_str_2021_1_14.index.max() ] ]#,
       #glue_df[df_str_2022_1_14.index.min(): df_str_2022_1_14.index.max() ] ]
       
 

    fig, ax = plt.subplots(1,1 , figsize=(10, 10))
    for k, _ in enumerate(Y):

        ax.plot(Y[k].index, Y[k]['obs'], 'bo' , label='obs' , alpha=0.5)
        ax.fill_between(Y[k].index, Y[k]['2.5%'], Y[k]['97.5%'], color='r', alpha=0.3)
        ax.plot(Y[k].index, Y[k]['50%'], 'r-', label='mid_model')
        
    ax.set_title('"Uncertainty Analysis based on GLUE Method- RMSE_profile_1"')    
    ax.tick_params(axis='x', labelrotation=-45)
    ax.set_ylabel('Hypolimnietic DO average [mg.m-3]')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # set the date forma
    fig.legend(labels=['obs' , '95% confidence interval', 'median simulation' ],  loc= 'upper center', bbox_to_anchor = (0.5, 1))
    ax.set_title('RMSE hypo profile<1, %s behavioural sets out of %s' % (len(params_df), len(ja_s)))   
    fig.savefig('GLUE_100X100_rmse_prof_threshold_1_only_meso_range_validation_2021', bbox='tight' , dpi= 300)  

    fig.show()



    return glue_df , params_df
#%%Validation_results
    
glue_df ,params_df  = plot_glue_validation(params_df, sims_df_valid)    

#%%savingg results +Validation_rmse_prof columns 
# Save params_df to a CSV file
params_df.to_csv('GLUE_params_results_only_meso_added_rmse_validation.csv', index=False)

# Save sims_df to a CSV file
sims_df.to_csv('GLUE_sims_results_only_meso_validation.csv', index=False)   


#%%































#%%
import matplotlib.pyplot as plt
import numpy as np

# Generate the scatter plot
fig, ax = plt.subplots(figsize=(20, 20))
scatter = ax.scatter(x, y, c=data, cmap='viridis')
plt.colorbar(scatter, label="Data Values")

# Add text annotation for each point
for i in range(len(x)):
    for j in range(len(y)):
        ax.text(x[j, i], y[j, i], f"{data[j, i]:.2f}", color='black', ha='center', va='center')

# Set plot labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot of Data")

# Show the plot
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np

# Your data
x, y = np.meshgrid(param1_values, param2_values)
data = output_values[:, :, 0]

# Generate the contour plot
plt.figure(figsize=(10, 8))
contour = plt.contourf(x, y, data, levels=100, cmap='viridis')  # Use any colormap you prefer
plt.colorbar(contour, label="Data Values")

# Add text annotation for each contour level
for level in contour.levels:
    idx = np.where(data == level)  # Find indices where data matches the contour level
    for i in range(len(idx[0])):
        plt.text(x[idx[0][i], idx[1][i]], y[idx[0][i], idx[1][i]], f"{level:.2f}", color='black',
                 ha='center', va='center')

# Find the minimum value and its location
min_value = np.nanmin(data)
min_index = np.unravel_index(np.nanargmin(data), data.shape)

# Add red point at the minimum value location
plt.scatter(param1_values[min_index[0]], param2_values[min_index[1]], color='red', marker='o', s=100)#, label="Minimum Value")

# Set plot labels
plt.xlabel("Jv [g m$^{-3}$ d$^{-1}$]")
plt.ylabel("Ja [g m$^{-2}$ d$^{-1}$]")
plt.title("Contour Plot of Data")

# Show the plot
#plt.legend()
plt.show()


    

#%% couture map plot starting from min values of rmse
data = output_values[:, :, t]
plt.rcParams.update({'font.size': 26})

plt.figure(figsize=(10, 8))
# Create the x and y arrays for the contour plot
x, y = np.meshgrid(param1_values, param2_values)
levels = np.linspace(np.nanmin(data), np.nanmax(data), 11)
# Plot the contour plot
# plt.subplot(4, 5, t+1)
contour = plt.contourf(x, y, data, levels=levels)
#plt.colorbar(contour, label="DO Profile RMSE [g m$^{-3}$]", ticks=np.arange(np.nanmin(data), np.nanmax(data) + 1))
plt.clim(np.nanmin(data), np.nanmax(data))
# plt.title("Timestep = {}[d]".format(p3_value))
plt.xlabel("Jv [g m$^{-3}$ d$^{-1}$]")
plt.ylabel("Ja [g m$^{-2}$ d$^{-1}$]")

# Save the figure with higher dpi for better quality
#plt.savefig("kz_jp_weekly_calibration_rmse_prof_.png", dpi=300)
plt.show()




#%%

import matplotlib.pyplot as plt

data = output_values[:, :, t]
plt.rcParams.update({'font.size': 26})

plt.figure(figsize=(10, 8))

# Create the x and y arrays for the contour plot
x, y = np.meshgrid(param1_values, param2_values)

# Define the contour levels
levels = 11
cmap = plt.get_cmap('jet')

# Plot the contour plot
contour_plot = plt.contourf(x, y, data, levels=levels, cmap=cmap)
plt.colorbar(contour_plot, label="DO Profile RMSE [g m$^{-3}$]")

plt.xlabel("Jv [g m$^{-3}$ d$^{-1}$]")
plt.ylabel("Ja [g m$^{-2}$ d$^{-1}$]")

# Save the figure with higher dpi for better quality
# plt.savefig("kz_jp_weekly_calibration_rmse_prof_.png", dpi=300)
plt.show()

#%% ploting results of clibrastion 
data = output_values[:, :, t]
plt.rcParams.update({'font.size': 26})

plt.figure(figsize=(10, 8))
# Create the x and y arrays for the contour plot
x, y = np.meshgrid(param1_values, param2_values)
levels = np.linspace(0, np.nanmax(data), 11)
# Plot the contour plot
# plt.subplot(4, 5, t+1)
plt.contourf(x, y, data, levels=levels)
plt.colorbar(label="DO Profile RMSE [g m$^{-3}$]", ticks=np.arange(0, np.nanmax(data) + 1))
# plt.title("Timestep = {}[d]".format(p3_value))
plt.xlabel("Jv [g m$^{-3}$ d$^{-1}$]")
plt.ylabel("Ja [g m$^{-2}$ d$^{-1}$]")

# Save the figure with higher dpi for better quality
#plt.savefig("kz_jp_weekly_calibration_rmse_prof_.png", dpi=300)
plt.show()