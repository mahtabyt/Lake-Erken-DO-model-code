# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:57:39 2024

@author: mahya344
"""
#pip install netCDF4

#%%#########################Morphological data 
#%%

#import    
import os    
import pandas as pd    
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





#%%####################Desnsity function
#%%
  
def Lab_Density(Temp):
    return (999.842594+6.793952*10**-2*Temp-9.095290*10**-3*Temp**2 + 1.001685*10**-4*Temp**3-1.120083*10**-6 * Temp**4+6.536332 * 10**-9*Temp**5)
       

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

#%%deox onset, offset and duration 
    
def start_dates_Jday (df_deox):
    start_jday=df_deox.groupby('year').min()['start_dates_Jday']
    return (start_jday)
    
def end_dates_Jday (df_deox):
    end_jday=df_deox.groupby('year').max()['end_dates_Jday']
    return (end_jday)

#%%annual_deox_duarion

def annual_deox_duarion (df_deox):
    deox_duarion=df_deox.groupby('year').sum()['deox_duration']
    return (deox_duarion)


    
#%%DO Modelling for GOTM GRIDS
    
#%%Initial functions of the model 

#%% function of DO satuareted and theta_j:
    
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


def Theta_j(temp):
    theta = 1.087
    return (theta ** (temp - 20))










#%%
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
#%%for GLUE
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



#%%#%%startistical analysing for finding trendline 
"""
1. Autocorrelation test= durbin_watson 
2. MK test for prooving is there any trend
 ( if the data is not autocorrelated so original MK ,
  if autocorrelated using modified MK (Hamed and Rao Modified MK Test))
3. Slope and intercepts were estimated based on the Sens estimator
"""

import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson


def autocorr_MK_org_modif_sens_slope_test (df_timeseries_dataset , p_value_confidence=0.05):
    dw_statistic=durbin_watson(df_timeseries_dataset)
    if dw_statistic==2:
        
        results=mk.original_test(df_timeseries_dataset, alpha=p_value_confidence)
        autocorr_type='non autocorrelated'

    else :
        #hamed_rao_modification_test
        results_hr=mk.hamed_rao_modification_test(df_timeseries_dataset, alpha=p_value_confidence)
        #yue_wang_modification_test
        results_yw=mk.yue_wang_modification_test(df_timeseries_dataset, alpha=p_value_confidence)
        #pre_whitening_modification_test
        results_wh=mk.pre_whitening_modification_test(df_timeseries_dataset, alpha=p_value_confidence)
        
        results=results_hr 
        
        
        if 0<dw_statistic<2:
            autocorr_type='positively autocorrelated'
        elif 2<dw_statistic<4:    
            autocorr_type='negetively autocorrelated'
        
        
    trend= results.trend
    p_value= results.p
    
    if trend=='no trend':
        sens_slope=0
        sens_intercept= 0
    else:
        sens_slope= results.slope
        sens_intercept= results.intercept
    
    return (dw_statistic, autocorr_type ,trend , p_value , sens_slope , sens_intercept )



#%%what if we are intersted to see the slope even the sens slopes said it is 'no trend'

import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson

def autocorr_MK_org_modif_sens_slope_test_allslopes (df_timeseries_dataset , p_value_confidence=0.05):
    dw_statistic=durbin_watson(df_timeseries_dataset)
    if dw_statistic==2:
        
        results=mk.original_test(df_timeseries_dataset, alpha=p_value_confidence)
        autocorr_type='non autocorrelated'

    else :
        #hamed_rao_modification_test
        results_hr=mk.hamed_rao_modification_test(df_timeseries_dataset, alpha=p_value_confidence)
        #yue_wang_modification_test
        results_yw=mk.yue_wang_modification_test(df_timeseries_dataset, alpha=p_value_confidence)
        #pre_whitening_modification_test
        results_wh=mk.pre_whitening_modification_test(df_timeseries_dataset, alpha=p_value_confidence)
        
        results=results_hr 
        
        
        if 0<dw_statistic<2:
            autocorr_type='positively autocorrelated'
        elif 2<dw_statistic<4:    
            autocorr_type='negetively autocorrelated'
            
        else:
            autocorr_type='nan'
        
        
    trend= results.trend
    p_value= results.p
    
    sens_slope= results.slope
    sens_intercept= results.intercept
    
    return (dw_statistic, autocorr_type ,trend , p_value , sens_slope , sens_intercept , np.median(df_timeseries_dataset ))








#%%Reading the winner Ja and Jv ready for apply :
   
"""    
####################with variable theta:    
# Define the file path
file_path = 'C:/small_array_working_area/Mahtab/py_codes_yt_DO_model/Calibration&Validation/Final/df_winner_of_all_180combinations_interval1e_1.csv'
# Read the Excel file
df_winner_of_all = pd.read_csv(file_path)

df_winner_of_all['weights']
"""

#%%a function for doing the normal test , median/mean , confidence interval and slope of slope 

from scipy.stats import shapiro
import scipy.stats as stats

def stats_for_slopes_CI95(data_series , alpha_shapiro=0.05 , bootstrap_samples= 1000): 
    
    # Assuming slope_trends_temp is your array
    statistic_shapiro, p_value_shapiro = shapiro(data_series)
    

    
    # Interpret the results
    if p_value_shapiro > alpha_shapiro:
        #print("The data looks Gaussian (normally distributed)")
        
        # Calculate the mean slope
        mean_slope = np.mean(data_series)
        
        # Calculate the standard error
        std_error = np.std(np.gradient(data_series)) / np.sqrt(len(data_series))
        
        # Calculate the 95% confidence intervals
        z_score = stats.norm.ppf(0.975)  # for 95% confidence interval
        confidence_interval = z_score * std_error
        
        lower_bound = mean_slope - confidence_interval
        upper_bound = mean_slope + confidence_interval
        
        #print("Mean Slope:", mean_slope)
        #print("95% Confidence Intervals:", lower_bound, "to", upper_bound)
        rep_slope = mean_slope 
        rep='normal_mean'
        
    else:
        #print("The data does not look Gaussian (not normally distributed)")   
        
        median_slope = np.median(data_series)
        # Bootstrap method for confidence intervals
        # You can adjust this number based on your data
        bootstrap_slopes = np.zeros(bootstrap_samples)
        
        for i in range(bootstrap_samples):
            bootstrap_data = np.random.choice(data_series, size=len(data_series), replace=True)
            bootstrap_slopes[i] = np.median(np.gradient(bootstrap_data))
        
        # Calculate the confidence intervals
        lower_percentile = 2.5
        upper_percentile = 97.5
        lower_bound = np.percentile(bootstrap_slopes, lower_percentile)
        upper_bound = np.percentile(bootstrap_slopes, upper_percentile)
        
        #print("Median Slope:", median_slope)
        #print(f"{lower_percentile}% - {upper_percentile}% Confidence Intervals:", lower_bound, "to", upper_bound)
        
        rep_slope= median_slope
        rep='notnormal-median'
        
    mean_slope = np.mean(data_series)
    median_slope = np.median(data_series)    
    return ('statistic_shapiro',statistic_shapiro, 'p_value_shapiro',  p_value_shapiro , 'lower_bound',   lower_bound ,  'rep_slope',rep , rep_slope, 'upper_bound', upper_bound , 'slope of gradient',  autocorr_MK_org_modif_sens_slope_test_allslopes(data_series) , 'mean_slope:' , mean_slope , 'median_slope:' , median_slope)
        
        