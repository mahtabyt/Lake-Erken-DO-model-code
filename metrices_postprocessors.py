# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:41:23 2023

@author: mahta
"""
import numpy as np
#C has demintion like (time*layer number) e.g....C_2021_1
hypo_morpho_vriables_gotm_grid = [
    np.array([1160000., 1160000., 1160000., 1160000., 395000., 395000., 395000., 395000., 41750., 41750., 41750., 41750., 1500., 1500.]),
    np.array([3220000., 2770000., 2320000., 1870000., 1420000., 1105000., 790000., 475000., 160000., 122500., 85000., 47500., 10000., 5000.]),
    np.array([450000., 450000., 450000., 450000., 315000., 315000., 315000., 315000., 37500., 37500., 37500., 37500., 5000., 5000.]),
    0.5,
    14
]




#%%annual_deox_duration 

def annual_deox_duration (df_deox_period):
    
    an_deox_duration=df_deox_period.groupby(df_deox_period['start_dates'].dt.year)['deox_duration'].sum()
    
    return (an_deox_duration)


#%% number of polimic years 

def count_polymictic (df):
    polimictic_years_num=df[df['index_deox_period_in_year']==1]['index_deox_period_in_year'].sum()
    return(polimictic_years_num)


#%%annual_deox_duarion

def annual_deox_duarion (df_deox):
    deox_duarion=df_deox.groupby('year').sum()['deox_duration']
    return (deox_duarion)


#%%Hypolimnetic average

def hypolimnetic_ave(C, Vr, time_series):
    C_ave=np.dot (C , Vr) / sum (Vr)
    C_ave_indexed=pd.Series(C_ave, index=pd.to_datetime(time_series))
    return (C_ave_indexed) 



def annual_hypolimnetic_ave(C, Vr, time_series):
    C_ave=np.dot (C , Vr) / sum (Vr)
    C_ave_indexed=pd.Series(C_ave, index=pd.to_datetime(time_series))
    C_annual_ave_indexed=C_ave_indexed.groupby(C_ave_indexed.index.year).mean()
    # Convert the Series to DataFrame
    C_annual_ave_indexed = C_annual_ave_indexed.to_frame(name='annual_do')
    return (C_annual_ave_indexed) 


"""
def monthly_hypolimnetic_ave(C, Vr, time_series):
    C_ave=np.dot (C , Vr) / sum (Vr)
    C_ave_indexed=pd.Series(C_ave, index=pd.to_datetime(time_series))
    C_ave_indexed.dropna(inplace=True)
    C_monthly_ave_indexed=C_ave_indexed.groupby(C_ave_indexed.index.month).mean()
    # Convert the Series to DataFrame
    C_monthly_ave_indexed = C_monthly_ave_indexed.to_frame(name='monthly_do')
    return (C_monthly_ave_indexed) 
"""


def monthly_hypolimnetic_ave (C, Vr, time_series ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    C_ave_indexed_year_month=C_ave_indexed.groupby([C_ave_indexed.index.year, C_ave_indexed.index.month ]).mean() 
    table_of_C_ave=C_ave_indexed_year_month.unstack()
    return (table_of_C_ave)

def Jul_Aug_hypolimnetic_ave(C, Vr, time_series):
    
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    C_ave_indexed.dropna(inplace=True)
    C_ave_daily_Jul_Aug=C_ave_indexed[(C_ave_indexed.index.month>6)&(C_ave_indexed.index.month<9)]
    C_ave_Jul_Aug=C_ave_daily_Jul_Aug.groupby(C_ave_daily_Jul_Aug.index.year).mean()
    # Convert the Series to DataFrame
    C_ave_Jul_Aug = C_ave_Jul_Aug.to_frame(name='Jul_Agu_do')

    return (C_ave_Jul_Aug)


def May_Sep_hypolimnetic_ave(C, Vr, time_series):
    
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    C_ave_indexed.dropna(inplace=True)
    C_ave_daily_May_Sep=C_ave_indexed[(C_ave_indexed.index.month>4)&(C_ave_indexed.index.month<10)]
    C_ave_May_Sep=C_ave_daily_May_Sep.groupby(C_ave_daily_May_Sep.index.year).mean()
    # Convert the Series to DataFrame
    C_ave_May_Sep = C_ave_May_Sep.to_frame(name='May_Sep_do')

    return (C_ave_May_Sep)

def Apr_Oct_hypolimnetic_ave(C, Vr, time_series):
    
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    C_ave_indexed.dropna(inplace=True)
    C_ave_daily_Apr_Oct=C_ave_indexed[(C_ave_indexed.index.month>3)&(C_ave_indexed.index.month<10)]
    C_ave_Apr_Oct=C_ave_daily_Apr_Oct.groupby(C_ave_daily_Apr_Oct.index.year).mean()
    # Convert the Series to DataFrame
    C_ave_Apr_Oct = C_ave_Apr_Oct.to_frame(name='Apr_Oct_do')

    return (C_ave_Apr_Oct)


def May_Nov_hypolimnetic_ave(C, Vr, time_series):
    
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    C_ave_indexed.dropna(inplace=True)
    C_ave_daily_May_Nov=C_ave_indexed[(C_ave_indexed.index.month>4)&(C_ave_indexed.index.month<11)]
    C_ave_May_Nov=C_ave_daily_May_Nov.groupby(C_ave_daily_May_Nov.index.year).mean()
    # Convert the Series to DataFrame
    C_ave_May_Nov = C_ave_May_Nov.to_frame(name='May_Nov_do')

    return (C_ave_May_Nov)


def May_Oct_hypolimnetic_ave(C, Vr, time_series):
    
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    C_ave_indexed.dropna(inplace=True)
    C_ave_daily_May_Oct=C_ave_indexed[(C_ave_indexed.index.month>4)&(C_ave_indexed.index.month<10)]
    C_ave_May_Oct=C_ave_daily_May_Oct.groupby(C_ave_daily_May_Oct.index.year).mean()
    # Convert the Series to DataFrame
    C_ave_May_Oct = C_ave_May_Oct.to_frame(name='May_Oct_do')

    return (C_ave_May_Oct)




def summer_hypolimnetic_ave(C, Vr, time_series):
    
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    C_ave_indexed.dropna(inplace=True)
    C_ave_daily_summer=C_ave_indexed[(C_ave_indexed.index.month>5)&(C_ave_indexed.index.month<9)]
    C_ave_summer=C_ave_daily_summer.groupby(C_ave_daily_summer.index.year).mean()

    # Convert the Series to DataFrame
    C_ave_summer = C_ave_summer.to_frame(name='summer_do')
    

    return (C_ave_summer)





#%%estimate DO saturation percentage:

def C_satur(temp, percent, altitude_m=10 ): # altitude in km for lake erken was 10/1000
    altitude_km = altitude_m/1000 
    P = np.exp(5.25 * np.log(1 - altitude_km/44.3))
    t = temp
    T = 273.15 + t
    teta = 0.000975 - (t*1.426*10**-5) + ((t**2)*6.436*10**-8)
    Pwv = 11.8571 - (3840.70/T)-(216961/T**2)
    C_star =np.exp(7.7117 - 1.31403 * np.log(t+45.93))
    return percent*(C_star * P*(((1-(Pwv/P))*(1-teta*P))/((1-Pwv)*(1-teta))))      

def estimate_satur_percentage ( C , temp , altitude_m=10 ):# it gives the satuartion percentage 70 instaed of 0.7 
        est_satur=(C/C_satur (temp , 1))*100
        return (est_satur)
    

#%%anoxia condition for each day 

def aonxia_condition (C, Vr, time_series, threshold=0.5):# number of anoxic day with hypolimentoc average below certain level
    C_ave_indexed= hypolimnetic_ave (C , Vr , time_series)
    anoxic_cond= (C_ave_indexed<=threshold )*1
    return (anoxic_cond)



def hypoxia_condition (C, Vr, time_series, threshold=2):# number of hypoxic day with hypolimentoc average below certain level
    C_ave_indexed= hypolimnetic_ave (C , Vr , time_series)
    hypoxic_cond= (C_ave_indexed<=threshold )*1
    return (hypoxic_cond)


#%%Duration of anoxia or hypoxia in each yaer 
""" 
#in direct :
def annual_anoxia_duration (C, Vr, time_series, threshold=0.5 ):
    anoxic_meet = aonxia_condition(C , Vr , time_series,  threshold=0.5 )     
    annual_anoxia_dur= anoxic_meet.groupby(anoxic_meet.index.year).sum()
    return (annual_anoxia_dur)



def annual_hypoxia_duration (C, Vr, time_series, threshold=2 ):
    hpoxic_meet = hypoxia_condition(C , Vr , time_series,  threshold=2 )     
    annual_hypoxia_dur= hpoxic_meet.groupby(hpoxic_meet.index.year).sum()
    return (annual_hypoxia_dur)
"""

#direct:
    
def annual_anoxia_duration (C ,  time_series,Vr, threshold=0.5 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    anoxic_meet = (C_ave_indexed<=threshold )*1     
    annual_anoxia_dur= anoxic_meet.groupby(anoxic_meet.index.year).sum()
    # Convert the Series to DataFrame
    annual_anoxia_dur = annual_anoxia_dur.to_frame(name='annual_adur')
    return (annual_anoxia_dur)



def annual_hypoxia_duration (C , time_series,Vr,  threshold=2 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    hpoxic_meet =(C_ave_indexed<=threshold )*1      
    annual_hypoxia_dur= hpoxic_meet.groupby(hpoxic_meet.index.year).sum()
    annual_hypoxia_dur=annual_hypoxia_dur.to_frame(name='annual_hdur')
    return (annual_hypoxia_dur)    


#direct May_Sep


def May_Sep_anoxia_duration(C,   time_series,Vr , threshold=0.5 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    anoxic_meet = (C_ave_indexed<=threshold )*1     
    May_Sep_anoxia_meet= anoxic_meet[(anoxic_meet.index.month>4)&(anoxic_meet.index.month<10)]
    May_Sep_anoxia_dur=May_Sep_anoxia_meet.groupby(May_Sep_anoxia_meet.index.year).sum()
    May_Sep_anoxia_dur=May_Sep_anoxia_dur.to_frame(name='May_Sep_adur')
    
    return (May_Sep_anoxia_dur)



def May_Sep_hypoxia_duration (C, time_series,Vr,  threshold=2 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    hpoxic_meet =(C_ave_indexed<=threshold )*1      
    May_Sep_hypoxia_meet= hpoxic_meet[(hpoxic_meet.index.month>4)&(hpoxic_meet.index.month<10)]
    May_Sep_hypoxia_dur=May_Sep_hypoxia_meet.groupby(May_Sep_hypoxia_meet.index.year).sum()    
    May_Sep_hypoxia_dur=May_Sep_hypoxia_dur.to_frame(name='May_Sep_hdur')
    
    return (May_Sep_hypoxia_dur)    




def Apr_Oct_anoxia_duration(C,   time_series,Vr , threshold=0.5 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    anoxic_meet = (C_ave_indexed<=threshold )*1     
    Apr_Oct_anoxia_meet= anoxic_meet[(anoxic_meet.index.month>3)&(anoxic_meet.index.month<10)]
    Apr_Oct_anoxia_dur=Apr_Oct_anoxia_meet.groupby(Apr_Oct_anoxia_meet.index.year).sum()
    Apr_Oct_anoxia_dur=Apr_Oct_anoxia_dur.to_frame(name='Apr_Oct_adur')
    
    return (Apr_Oct_anoxia_dur)



def Apr_Oct_hypoxia_duration (C, time_series,Vr,  threshold=2 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    hpoxic_meet =(C_ave_indexed<=threshold )*1      
    Apr_Oct_hypoxia_meet= hpoxic_meet[(hpoxic_meet.index.month>3)&(hpoxic_meet.index.month<10)]
    Apr_Oct_hypoxia_dur=Apr_Oct_hypoxia_meet.groupby(Apr_Oct_hypoxia_meet.index.year).sum()    
    Apr_Oct_hypoxia_dur=Apr_Oct_hypoxia_dur.to_frame(name='Apr_Oct_hdur')
    
    return (Apr_Oct_hypoxia_dur)    

#Summer period 
def summer_anoxia_duration (C,  time_series,Vr,  threshold=0.5 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    anoxic_meet = (C_ave_indexed<=threshold )*1     
    summer_anoxia_meet= anoxic_meet[(anoxic_meet.index.month>5) & (anoxic_meet.index.month<9)]
    summer_anoxia_dur=summer_anoxia_meet.groupby(summer_anoxia_meet.index.year).sum()
    summer_anoxia_dur=summer_anoxia_dur.to_frame(name='summer_adur')
    
    return (summer_anoxia_dur)



def summer_hypoxia_duration(C, time_series,Vr,  threshold=2 ):
    C_ave_indexed=hypolimnetic_ave(C, Vr, time_series)
    hpoxic_meet =(C_ave_indexed<=threshold )*1      
    summer_hypoxia_meet= hpoxic_meet[(hpoxic_meet.index.month>5) & (hpoxic_meet.index.month<9)]
    summer_hypoxia_dur=summer_hypoxia_meet.groupby(summer_hypoxia_meet.index.year).sum()
    summer_hypoxia_dur=summer_hypoxia_dur.to_frame(name='summer_hdur')
    
    return (summer_hypoxia_dur)   




#%%plotting the monthly changes of each year

def monthly_table_of_anoxia_duartion (C, time_series, Vr, threshold=0.5 ):
    anoxic_meet = aonxia_condition(C , Vr , time_series,  threshold=0.5 )
    anoxic_duartion_year_month=anoxic_meet.groupby([anoxic_meet.index.year, anoxic_meet.index.month ]).sum() 
    table_of_anoxia_duartion=anoxic_duartion_year_month.unstack()
    return (table_of_anoxia_duartion)


def monthly_table_of_hypoxia_duartion (C, time_series, Vr, threshold=2):
    hypoxic_meet = hypoxia_condition(C , Vr , time_series,  threshold=2 )
    hypoxic_duartion_year_month=hypoxic_meet.groupby([hypoxic_meet.index.year, hypoxic_meet.index.month ]).sum() 
    table_of_hypoxia_duartion=hypoxic_duartion_year_month.unstack()
    return (table_of_hypoxia_duartion)





#%% finding the first day of anoxioc or hypoxic condition date and dayofyaer

def first_and_last_anoxioc_day_inyear (C, Vr, time_series, threshold=0.5):
    C_ave_indexed= hypolimnetic_ave (C , Vr , time_series)
    anoxic_cond= (C_ave_indexed<=threshold )
    anoxic_meet=C_ave_indexed[anoxic_cond]
    
    first_anoxia_day=anoxic_meet.groupby(anoxic_meet.index.year).apply(lambda x: x.index[0])
    
    last_anoxia_day=anoxic_meet.groupby(anoxic_meet.index.year).apply(lambda x: x.index[-1])

    return (first_anoxia_day , first_anoxia_day.dt.dayofyear, 
            last_anoxia_day , last_anoxia_day.dt.dayofyear)
            




def first_and_last_hypoxioc_day_inyear (C, Vr, time_series, threshold=2):
    C_ave_indexed= hypolimnetic_ave (C , Vr , time_series)
    hypoxic_cond= (C_ave_indexed<=threshold )
    hypoxic_meet=C_ave_indexed[hypoxic_cond]
    
    first_hypoxia_day=hypoxic_meet.groupby(hypoxic_meet.index.year).apply(lambda x: x.index[0])
    
    last_hypoxia_day=hypoxic_meet.groupby(hypoxic_meet.index.year).apply(lambda x: x.index[-1])


    return (first_hypoxia_day , first_hypoxia_day.dt.dayofyear ,
            last_hypoxia_day , last_hypoxia_day.dt.dayofyear)











#%%for attribution test of ktemp the date of first hypoxia  


def firstdeephypoxiadate_jday_tempave_DOave(temp, C, Vr, time_series, threshold=2):
    hypoxia_threshold=threshold
    C_indexed= pd.DataFrame(C , index= time_series)
    temp_indexed= pd.DataFrame(temp , index= time_series)
    
    onset_index_per_year=C_indexed.groupby(C_indexed.index.year).apply(lambda x: x.first_valid_index())
    # Use groupby to group by year and find the index of the minimum value in each group
    C_filtered_by_thereshold= C_indexed[C_indexed.iloc[: , -1]<= hypoxia_threshold].iloc[: , -1]
    threshold_index_per_year = C_filtered_by_thereshold.groupby(C_filtered_by_thereshold.index.year).idxmax()#C_indexed[: , -1] try .any() as well 
    
    offset_index_per_year=C_indexed.groupby(C_indexed.index.year).apply(lambda x: x.last_valid_index())
       
    
    if offset_index_per_year.shape!=threshold_index_per_year.shape:
        threshold_index_per_year=threshold_index_per_year.combine_first(offset_index_per_year)
  
    
    
    # Create an empty list to store the subsets for each year
    C_subsets_per_year = np.array([])
    temp_subsets_per_year = np.array([])

    
    # Iterate through each year and extract the subset
    for  onset_index, threshold_index , offset_index in zip(onset_index_per_year, threshold_index_per_year , offset_index_per_year):
        C_subset_for_year =np.mean(hypolimnetic_ave( C_indexed.loc[onset_index:threshold_index] , Vr,  C_indexed.loc[onset_index:threshold_index].index ) )
        C_subsets_per_year=np.append( C_subset_for_year,C_subsets_per_year)
        
        
        
        temp_subset_for_year =np.mean(hypolimnetic_ave( temp_indexed.loc[onset_index:threshold_index] , Vr,temp_indexed.loc[onset_index:threshold_index].index ) )
        temp_subsets_per_year=np.append( temp_subset_for_year,temp_subsets_per_year)
        
        
        
        
    C_ave_onset_to_thereshold= pd.DataFrame(C_subsets_per_year, index=onset_index_per_year.index)
    temp_ave_onset_to_thereshold= pd.DataFrame(temp_subsets_per_year, index=onset_index_per_year.index)
    threshold_jday=threshold_index_per_year.dt.dayofyear 
    
    
    
    return(threshold_jday, temp_ave_onset_to_thereshold , C_ave_onset_to_thereshold)
    
    
    
#%%Jday and temp ave on onsets and offsets of each year

def temp_ave_onset_offset( temp , Vr, time_series):
    
    temp_indexed= pd.DataFrame(temp , index= time_series)
    
    onset_index_per_year=temp_indexed.groupby(temp_indexed.index.year).apply(lambda x: x.first_valid_index())
    offset_index_per_year=temp_indexed.groupby(temp_indexed.index.year).apply(lambda x: x.last_valid_index())
      
    temp_ave_onset_index_per_year=hypolimnetic_ave( temp_indexed.loc[onset_index_per_year] , Vr , onset_index_per_year)
    temp_ave_offset_index_per_year=hypolimnetic_ave( temp_indexed.loc[offset_index_per_year] , Vr , offset_index_per_year)

    onset_jday=onset_index_per_year.dt.dayofyear
    offset_jday=offset_index_per_year.dt.dayofyear    
    
    temp_ave_offset_index_per_year.index=temp_ave_offset_index_per_year.index.year
    temp_ave_onset_index_per_year.index=temp_ave_onset_index_per_year.index.year
    
    
    return(temp_ave_onset_index_per_year , temp_ave_offset_index_per_year , onset_jday ,  offset_jday)

#%%AI 

import numpy as np
import pandas as pd

def first_anoxic_prof_inyear(C, Vr, time_series, threshold=0.5):
    max_C = np.max(C, axis=1)
    all_full_anoxia_date = time_series[max_C < threshold]
    
    # Group by year and find the minimum date for each year
    first_annual_full_anoxic_date = all_full_anoxia_date.groupby(all_full_anoxia_date.dt.year).min().fillna(0)
    
    # Fill missing years with 0
    min_year = time_series.min().year
    max_year = time_series.max().year
    all_years = np.arange(min_year, max_year + 1)
    
    for year in all_years:
        if year not in first_annual_full_anoxic_date.index:
            first_annual_full_anoxic_date[year] = 0
    
    # Sort the index
    first_annual_full_anoxic_date.sort_index(inplace=True)
    
    return first_annual_full_anoxic_date

# Example usage:
# result = first_anoxic_prof_inyear(C, Vr, time_series)


#%%the first and last day of each anoxic period 
#with full profile hypoxic or anoxic 

import numpy as np
import pandas as pd

def first_last_len_anoxic_prof_inyear(C, Vr, time_series, threshold=0.5):
    max_C = np.max(C, axis=1)
    all_full_anoxia_date = time_series[max_C < threshold]
    
    # Group by year and find the minimum date for each year
    first_annual_full_anoxic_date = all_full_anoxia_date.groupby(all_full_anoxia_date.dt.year).min().fillna(0)
    first_annual_full_anoxic_jday = all_full_anoxia_date.dt.dayofyear.groupby(all_full_anoxia_date.dt.year).min().fillna(0)
    
    # Group by year and find the maximum date for each year
    last_annual_full_anoxic_date = all_full_anoxia_date.groupby(all_full_anoxia_date.dt.year).max().fillna(0)
    last_annual_full_anoxic_jday = all_full_anoxia_date.dt.dayofyear.groupby(all_full_anoxia_date.dt.year).max().fillna(0)
    
    # Create a list of all years present in the data
    all_years = pd.to_datetime(time_series).dt.year.unique()
    len_annual_full_anoxic= pd.DataFrame(index=all_years, columns=['len_full'])
    len_annual_full_anoxic.index.name= 'Datetime'
    # Ensure all years have an entry, filling missing years with 0
    for year in all_years:
        if year not in first_annual_full_anoxic_date.index:
            first_annual_full_anoxic_date[year] = 0
            first_annual_full_anoxic_jday[year] = 0
            
        if year not in last_annual_full_anoxic_date.index:
            last_annual_full_anoxic_date[year] = 0
            last_annual_full_anoxic_jday[year] = 0
           
            
        len_annual_full_anoxic.loc[year] = last_annual_full_anoxic_jday.loc[year] - first_annual_full_anoxic_jday.loc[year] + 1


    
    # Sort the indices
    #first_annual_full_anoxic_date.sort_index(inplace=True)
    #first_annual_full_anoxic_jday.sort_index(inplace=True)
    #last_annual_full_anoxic_date.sort_index(inplace=True)
    #last_annual_full_anoxic_jday.sort_index(inplace=True)
    #len_annual_full_anoxic.sort_index(inplace=True)

    #make dataframe 
    first_annual_full_anoxic_jday=first_annual_full_anoxic_jday.to_frame(name='first_jday_full')
    last_annual_full_anoxic_jday=last_annual_full_anoxic_jday.to_frame(name='last_jday_full')

    
    return (first_annual_full_anoxic_date, first_annual_full_anoxic_jday, 
            last_annual_full_anoxic_date, last_annual_full_anoxic_jday,
            len_annual_full_anoxic)

    

#%%the first and last day of each anoxic period 
#with deep hypoxic or anoxic 

import numpy as np
import pandas as pd

def first_last_len_anoxic_deep_inyear(C, Vr, time_series, threshold=0.5):
    deep_C = C[:,-1 ]
    all_deep_anoxia_date = time_series[deep_C < threshold]
    
    # Group by year and find the minimum date for each year
    first_annual_deep_anoxic_date = all_deep_anoxia_date.groupby(all_deep_anoxia_date.dt.year).min().fillna(0)
    first_annual_deep_anoxic_jday = all_deep_anoxia_date.dt.dayofyear.groupby(all_deep_anoxia_date.dt.year).min().fillna(0)
    
    # Group by year and find the maximum date for each year
    last_annual_deep_anoxic_date = all_deep_anoxia_date.groupby(all_deep_anoxia_date.dt.year).max().fillna(0)
    last_annual_deep_anoxic_jday = all_deep_anoxia_date.dt.dayofyear.groupby(all_deep_anoxia_date.dt.year).max().fillna(0)
    
    # Create a list of all years present in the data
    all_years = pd.to_datetime(time_series).dt.year.unique()
    
    len_annual_deep_anoxic= pd.DataFrame(index=all_years, columns=['len_deep'])
    len_annual_deep_anoxic.index.name = 'Datetime'
    # Ensure all years have an entry, filling missing years with 0
    for year in all_years:
        if year not in first_annual_deep_anoxic_date.index:
            first_annual_deep_anoxic_date[year] = 0
            first_annual_deep_anoxic_jday[year] = 0

        if year not in last_annual_deep_anoxic_date.index:
            last_annual_deep_anoxic_date[year] = 0
            last_annual_deep_anoxic_jday[year] = 0
        
        len_annual_deep_anoxic.loc[year]=last_annual_deep_anoxic_jday.loc[year]-first_annual_deep_anoxic_jday.loc[year]
        
            
            
        
    
   
    # Sort the indices
    #first_annual_deep_anoxic_date.sort_index(inplace=True)
    #first_annual_deep_anoxic_jday.sort_index(inplace=True)
    #last_annual_deep_anoxic_date.sort_index(inplace=True)
    #last_annual_deep_anoxic_jday.sort_index(inplace=True)
    #len_annual_deep_anoxic.sort_index(inplace=True)
    
    #make dataframe 
    first_annual_deep_anoxic_jday=first_annual_deep_anoxic_jday.to_frame(name='first_jday_deep')
    last_annual_deep_anoxic_jday=last_annual_deep_anoxic_jday.to_frame(name='last_jday_deep')
    first_annual_deep_anoxic_date= first_annual_deep_anoxic_date.to_frame(name='first_date_deep')
    last_annual_deep_anoxic_date=last_annual_deep_anoxic_date.to_frame(name='last_date_deep')
    
    return (first_annual_deep_anoxic_date, first_annual_deep_anoxic_jday, 
            last_annual_deep_anoxic_date, last_annual_deep_anoxic_jday,
            len_annual_deep_anoxic)
 
#%% ave DO/temp from onset till hypoxia 

#temp and C from deoxy periods 

def ave_before_deep_anoxia(temp , C, Vr, time_series, threshold):
    
    C_indexed=pd.DataFrame(data=C , index=time_series)
    
    temp_indexed=pd.DataFrame(data=temp , index=time_series)
    
    C_indexed.dropna(inplace=True)
    
    all_deoxy_date = C_indexed.index
    
    start_year=C_indexed.groupby(all_deoxy_date.year).apply(lambda x: x.first_valid_index())    
    end_year=C_indexed.groupby(all_deoxy_date.year).apply(lambda x: x.last_valid_index())  
    
    temp_indexed.dropna(inplace=True)
    
    
    
    # Create a list of all years present in the data
    all_years = pd.to_datetime(time_series).dt.year.unique()
    

    offset_anoxia=first_last_len_anoxic_deep_inyear(C, Vr, time_series, threshold)[0]
    #offset_anoxia=offset_anoxia.replace(0, np.nan)
    ave_temp_till_deep_anoxic= pd.DataFrame(index=all_years, columns=['temp_till_deep'])
    ave_C_till_deep_anoxic= pd.DataFrame(index=all_years, columns=['C_till_deep'])
    
    for  onset, offset_an , offset in zip(start_year,offset_anoxia, end_year ):
       
        temp_subset_for_year = temp_indexed.loc[onset:offset_an]
        C_subset_for_year = C_indexed.loc[onset:offset_an]
        
        ave_temp_till_deep_anoxic.loc[onset.index]=pd.Series(np.dot (temp_subset_for_year , Vr) / sum (Vr), index=onset.index)
        ave_C_till_deep_anoxic.loc[onset.index]=pd.Series(np.dot (C_subset_for_year , Vr) / sum (Vr), index=onset.index)
        

    return ave_temp_till_deep_anoxic , ave_C_till_deep_anoxic



#%% ave DO/temp from onset till hypoxia 

def calculate_average_until_condition(df_do_daily_ave_indexed, hypoxia_threshold=2):
    
    
    
    onset_index_per_year=df_do_daily_ave_indexed.groupby(df_do_daily_ave_indexed['Datetime'].dt.year)['Hypolimnetic_Ave'].apply(lambda x: x.first_valid_index())    
    # Use groupby to group by year and find the index of the minimum value in each group
    threshold_index_per_year = df_do_daily_ave_indexed[df_do_daily_ave_indexed['Hypolimnetic_Ave'] <= hypoxia_threshold].groupby(df_do_daily_ave_indexed['Datetime'].dt.year)['Hypolimnetic_Ave'].idxmax()
    
    offset_index_per_year=df_do_daily_ave_indexed.groupby(df_do_daily_ave_indexed['Datetime'].dt.year)['Hypolimnetic_Ave'].apply(lambda x: x.last_valid_index())  
       
     
    if offset_index_per_year.shape!=threshold_index_per_year.shape:
        threshold_index_per_year=threshold_index_per_year.combine_first(offset_index_per_year)
  
        
     
    # Create an empty list to store the subsets for each year
    subsets_per_year = np.array([])
    
    # Iterate through each year and extract the subset
    for  onset_index, threshold_index in zip(onset_index_per_year, threshold_index_per_year):
        subset_for_year = df_do_daily_ave_indexed.loc[onset_index:threshold_index].mean()
        subsets_per_year=np.append( subset_for_year,subsets_per_year)
        
    df_subsets_per_year= pd.DataFrame(subsets_per_year, index=onset_index_per_year.index)
   
    return df_subsets_per_year








#%% AF anf HF
#1.Annual Variability can be decleared in a range between lakes with 
##different hypsographic( indictor of different shap could be morphometric ratio
##, measured as z/(A**0.5) (m km–1) the average depth (z) to the square root of the surface area (A) of the water bod
#2. between ja and jv for mangment 
#3. between scenarios 
#4. between Climatic index (e.g. Pacific Northwest Index (PNI) in Nurburg 1988)
#e.g. ranged from 72–118 d yr–1 AF and 102–215 d yr–1 HF
# 5. Fish Species Richness( cold water spices are more sensible in the hypolimnion over summer but in winter due to the fish kill )
# 6.Internal Load Calculation  (Internal load = Release rate  * AFsum) (look at the tabel 1 in Nurburg 1988)

# these factor can related to the duration of stratification easily and investigate the correlation 


def anoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=0.5):
    
    C_2D_anoxia_cond = np.where(C < threshold, 1, 0)                          
    anoxic_sediment_ratio = C_2D_anoxia_cond * ((Al/ A0).T)

    anoxic_factor_for_each_day=np.sum(anoxic_sediment_ratio, axis=1)
    
    anoxic_factor_for_each_day_indexed=pd.Series(anoxic_factor_for_each_day, index=pd.to_datetime(time_series))
    
    return (anoxic_factor_for_each_day_indexed)
    


def monthly_table_of_anoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=0.5):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_year_month= anoxic_factor_for_each_day_indexed.groupby([anoxic_factor_for_each_day_indexed.index.year, anoxic_factor_for_each_day_indexed.index.month ]).sum() 
    table_of_anoxia_factor=anoxic_factor_year_month.unstack()
    return (table_of_anoxia_factor)




def May_Sep_anoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=0.5):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_May_Sep_for_each_day_indexed=anoxic_factor_for_each_day_indexed[(anoxic_factor_for_each_day_indexed.index.month>4)&(anoxic_factor_for_each_day_indexed.index.month<10)]
    anoxic_factor_annual_May_Sep= anoxic_factor_May_Sep_for_each_day_indexed.groupby(anoxic_factor_May_Sep_for_each_day_indexed.index.year).sum() 
    # Convert the Series to DataFrame
    anoxic_factor_annual_May_Sep = anoxic_factor_annual_May_Sep.to_frame(name='May_Sep_af')
    return (anoxic_factor_annual_May_Sep)



def May_Sep_hypoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=2):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_May_Sep_for_each_day_indexed=anoxic_factor_for_each_day_indexed[(anoxic_factor_for_each_day_indexed.index.month>4)&(anoxic_factor_for_each_day_indexed.index.month<10)]
    anoxic_factor_annual_May_Sep= anoxic_factor_May_Sep_for_each_day_indexed.groupby(anoxic_factor_May_Sep_for_each_day_indexed.index.year).sum() 
    # Convert the Series to DataFrame
    anoxic_factor_annual_May_Sep = anoxic_factor_annual_May_Sep.to_frame(name='May_Sep_hf')
    return (anoxic_factor_annual_May_Sep)


def Apr_Oct_anoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=0.5):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_Apr_Oct_for_each_day_indexed=anoxic_factor_for_each_day_indexed[(anoxic_factor_for_each_day_indexed.index.month>3)&(anoxic_factor_for_each_day_indexed.index.month<10)]
    anoxic_factor_annual_Apr_Oct= anoxic_factor_Apr_Oct_for_each_day_indexed.groupby(anoxic_factor_Apr_Oct_for_each_day_indexed.index.year).sum() 
    # Convert the Series to DataFrame
    anoxic_factor_annual_Apr_Oct = anoxic_factor_annual_Apr_Oct.to_frame(name='Apr_Oct_af')
    return (anoxic_factor_annual_Apr_Oct)



def Apr_Oct_hypoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=2):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_Apr_Oct_for_each_day_indexed=anoxic_factor_for_each_day_indexed[(anoxic_factor_for_each_day_indexed.index.month>3)&(anoxic_factor_for_each_day_indexed.index.month<10)]
    anoxic_factor_annual_Apr_Oct= anoxic_factor_Apr_Oct_for_each_day_indexed.groupby(anoxic_factor_Apr_Oct_for_each_day_indexed.index.year).sum() 
    # Convert the Series to DataFrame
    anoxic_factor_annual_Apr_Oct = anoxic_factor_annual_Apr_Oct.to_frame(name='Apr_Oct_hf')
    return (anoxic_factor_annual_Apr_Oct)








def summer_anoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=0.5):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_summer_for_each_day_indexed=anoxic_factor_for_each_day_indexed[(anoxic_factor_for_each_day_indexed.index.month>5)&(anoxic_factor_for_each_day_indexed.index.month<9)]
    anoxic_factor_annual_summer= anoxic_factor_summer_for_each_day_indexed.groupby(anoxic_factor_summer_for_each_day_indexed.index.year).sum() 
    # Convert the Series to DataFrame
    anoxic_factor_annual_summer = anoxic_factor_annual_summer.to_frame(name='summer_af')
    return (anoxic_factor_annual_summer)



def summer_hypoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=2):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_summer_for_each_day_indexed=anoxic_factor_for_each_day_indexed[(anoxic_factor_for_each_day_indexed.index.month>5)&(anoxic_factor_for_each_day_indexed.index.month<9)]
    anoxic_factor_annual_summer= anoxic_factor_summer_for_each_day_indexed.groupby(anoxic_factor_summer_for_each_day_indexed.index.year).sum() 
    anoxic_factor_annual_summer = anoxic_factor_annual_summer.to_frame(name='summer_hf')
    return (anoxic_factor_annual_summer)





def annual_anoxic_factor (C, time_series, Al, A0=23.67*10**6 , threshold=0.5):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_for_each_year= anoxic_factor_for_each_day_indexed.groupby(anoxic_factor_for_each_day_indexed.index.year).sum() 
    # Convert the Series to DataFrame
    anoxic_factor_for_each_year = anoxic_factor_for_each_year.to_frame(name='annual_anoxic_factor')
    
    return (anoxic_factor_for_each_year)



def annual_hypoxic_factor (C, time_series, Al, A0=23.67*10**6 , threshold=2):
    anoxic_factor_for_each_day_indexed=anoxic_factor(C, time_series, Al, A0 , threshold)
    anoxic_factor_for_each_year= anoxic_factor_for_each_day_indexed.groupby(anoxic_factor_for_each_day_indexed.index.year).sum() 
    # Convert the Series to DataFrame
    anoxic_factor_for_each_year = anoxic_factor_for_each_year.to_frame(name='annual_hf')
    
    return (anoxic_factor_for_each_year)





#%%


def hypoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=2):
    
    C_2D_hypoxia_cond = np.where(C < threshold, 1, 0)        
                  
    hypoxic_sediment_ratio = C_2D_hypoxia_cond * ((Al/ A0).T)

    hypoxic_factor_for_each_day=np.sum(hypoxic_sediment_ratio, axis=1)
    
    hypoxic_factor_for_each_day_indexed=pd.Series(hypoxic_factor_for_each_day, index=pd.to_datetime(time_series))
    
    return (hypoxic_factor_for_each_day_indexed )



def monthly_table_of_hypoxic_factor(C, time_series, Al, A0=23.67*10**6 , threshold=2):
    hypoxic_factor_for_each_day_indexed=hypoxic_factor(C, time_series, Al, A0 , threshold)
    hypoxic_factor_year_month= hypoxic_factor_for_each_day_indexed.groupby([hypoxic_factor_for_each_day_indexed.index.year, hypoxic_factor_for_each_day_indexed.index.month ]).sum() 
    table_of_hypoxia_duartion=hypoxic_factor_year_month.unstack()
    return (table_of_hypoxia_duartion)







#%% oxygen_depletion_rate
#decreasing dissolved oxygen (DO) concentrations before the onset of anoxia
# I assume where it meets 0 for all 
# ladwert 2017

def hypolimnetic_ave(C, Vr, time_series):
    C_ave=np.dot (C , Vr) / sum (Vr)
    C_ave_indexed=pd.Series(C_ave, index=pd.to_datetime(time_series))
    return (C_ave_indexed) 

#%AI

def oxygen_depletion_rate_ineach_deox_prof(C, Vr, time_series, threshold=2):
    
    C_ave_indexed= hypolimnetic_ave(C, Vr, time_series)
    
    C_ave_nonan_indexed=C_ave_indexed.dropna()
       
    annual_first_deoxygenation_date=C_ave_nonan_indexed.groupby(C_ave_nonan_indexed.index.year).apply(lambda x: x.index[0])
    
    hypoxic_cond = (C_ave_indexed <= threshold)
    #hypoxic_meet = C_ave_indexed[hypoxic_cond]
    timeseries_hypoxic_meet= time_series[hypoxic_cond.values]
    first_hypoxia_day= timeseries_hypoxic_meet.groupby(timeseries_hypoxic_meet.dt.year).min().fillna(0)
    
    
    all_years = pd.to_datetime(time_series).dt.year.unique()
    hypoxic_depletion_rate = pd.DataFrame(index=all_years, columns=['dep_rate'])
    hypoxic_depletion_rate.index.name = "Datetime"
    
    
    for year in all_years:
        if year not in first_hypoxia_day.index:
            hypoxic_depletion_rate.loc[year, 'dep_rate'] = 0
            deltat_first_hypoxic_deox_periods=0
        else:
            #deltat_first_hypoxic_deox_periods = (first_hypoxia_day[year] - annual_first_deoxygenation_date[year]).days

            deltat_first_hypoxic_deox_periods = (first_hypoxia_day[year] - annual_first_deoxygenation_date[year]).days

            df_annual_C_ave_first_deox = np.array(C_ave_indexed[annual_first_deoxygenation_date[year]])
            
            diff_C_first_deox_hypox = df_annual_C_ave_first_deox- np.array(
                C_ave_indexed[first_hypoxia_day[year]])

            hypoxic_depletion_rate.loc[year, 'dep_rate'] = diff_C_first_deox_hypox / deltat_first_hypoxic_deox_periods
            
    hypoxic_depletion_rate['dep_rate'] = pd.to_numeric(hypoxic_depletion_rate['dep_rate'], errors='coerce')
    #hypoxic_depletion_rate.index = pd.to_datetime(hypoxic_depletion_rate.index)
    return hypoxic_depletion_rate





#%%#OLD

"""
def oxygen_depletion_rate_ineach_deox_prof(C, Vr, time_series, threshold= 2):
    
    C_ave_indexed= hypolimnetic_ave(C, Vr, time_series)
    
    C_ave_nonan_indexed=C_ave_indexed.dropna()
    
    annual_first_deoxygenation_date=C_ave_nonan_indexed.groupby(C_ave_nonan_indexed.index.year).apply(lambda x: x.index[0])
    
    
    #onset concentration
    df_annual_C_ave_first_deox=pd.DataFrame(np.array(C_ave_indexed [annual_first_deoxygenation_date]))  
    #onset date
    df_annual_C_ave_first_deox= df_annual_C_ave_first_deox.set_index(annual_first_deoxygenation_date.dt.year)
    

    hypoxic_cond= (C_ave_indexed<=threshold )
    hypoxic_meet=C_ave_indexed[hypoxic_cond]
    
    first_hypoxia_day=hypoxic_meet.groupby(hypoxic_meet.index.year).apply(lambda x: x.index[0])
    
    # Create a list of all years present in the data
    all_years = pd.to_datetime(time_series).dt.year.unique()
    hypoxic_depletion_rate= pd.DataFrame(index=all_years, columns=['dep_rate'])
    hypoxic_depletion_rate.index.name = "Datetime"
    deltat_first_hypoxic_deox_periods= pd.DataFrame(index=all_years)
    diff_C_first_deox_hypox= pd.DataFrame(index=all_years)
    # Ensure all years have an entry, filling missing years with 0
    for year in all_years:
        if year not in first_hypoxia_day.index:
            hypoxic_depletion_rate.loc[year, 'dep_rate'] = 0
            
        else:
                
       
            deltat_first_hypoxic_deox_periods[year]=(first_hypoxia_day[year]-annual_first_deoxygenation_date[year]).days
            
            
            
            diff_C_first_deox_hypox[year]=df_annual_C_ave_first_deox[df_annual_C_ave_first_deox.index==year]- np.array(C_ave_indexed [first_hypoxia_day[year]]) 
             
            hypoxic_depletion_rate.loc[year, 'dep_rate']= diff_C_first_deox_hypox[year]/deltat_first_hypoxic_deox_periods[year]
             
            
    return (hypoxic_depletion_rate ,  deltat_first_hypoxic_deox_periods)
"""    
  



#%% selected_dayofyear_DO_profile_ave  

 
def selected_dayofyear_DO_profile_ave( C , Vr ,time_series , selected_month , selected_day ):
   
    date_selective_indexes=time_series[(time_series.dt.month == selected_month) & (time_series.dt.day ==selected_day )].index
    date_selective=time_series[(time_series.dt.month == selected_month) & (time_series.dt.day ==selected_day )]
   
    
    prof_selected_day= C[date_selective_indexes , :]
    
    ave_selected_day= np.dot(prof_selected_day , Vr)/sum(Vr)
    
    
    data_selected_day= { 'date_selective':date_selective, 
           'ave_selected_day':ave_selected_day}
    
    df_selected_day=pd.DataFrame(data_selected_day)

    
    return df_selected_day ,prof_selected_day 
    


#%%fall_turnover_date
# Nurburge 1988, 92 lakes are evaluated this formulaR2 =0.47,p < 0.0001
# Julian day of the year;
# T, average July–August temperature at ca. 1 m above the bottom at the deepest location of the lake (Cº) 
# z, mean depth, i.e., lake volume/lake surface area (m)
# Log (fall turnover date) = 2.62 – 0.116 log (T) + 0.042 log (z) – 0.002 Latitude
""" 
import datetime
import math
import numpy as np



def fall_turnover_date ( temp , time_series , Vr,  lat= 59, V0=21.349*10**7  , A0=23.67*10**6 ):# unit in number Julian day 
    
    z_mean= V0/A0
    
    all_years_julian_day_end_date=np.array([])
    years= np.array([])
    months= np.array([])
    days= np.array([])
    for year in range(time_series.dt.year.min(), time_series.dt.year.max() + 1):
       
        
        selected_year_time_series= time_series[time_series.dt.year== year]
        
        date_1st_jul=selected_year_time_series[(selected_year_time_series.dt.month == 7) & (selected_year_time_series.dt.day == 1)]
        
        index_1st_jul=date_1st_jul.index[0]
        

        date_31th_Aug=selected_year_time_series[(selected_year_time_series.dt.month == 8) & (selected_year_time_series.dt.day == 31)]
        
        index_31th_Aug=date_31th_Aug.index[0]        
    
        temp_ave_Jul_Aug_1m_above_the_bottom = np.average(temp[int(index_1st_jul): int(index_31th_Aug)+1 ,  -2])
        
        fall_turnover_J_day=10**(2.62 - 0.116* math.log10(temp_ave_Jul_Aug_1m_above_the_bottom) + 0.042 *math.log10(z_mean) - 0.002 *lat)
        
        
        # Round the Julian day to the nearest integer
        rounded_julian_day = np.round(fall_turnover_J_day)
        
        # Calculate the date from the rounded Julian day
        date = datetime.datetime.fromordinal(int(rounded_julian_day) + 1721425)
        
        # Extract month and day of the month
        month = date.month
        day = date.day
        
        
        all_years_julian_day_end_date=np.append( all_years_julian_day_end_date, rounded_julian_day)
        years = np.append(years, year)
        months = np.append(months, month)
        days = np.append(days, day)
    
    
    return years ,months , days,  all_years_julian_day_end_date 
    
  
#%%testing estimation of offset of startification period 

years_rcp60 , months_rcp60, days_rcp60, estimated_end_jday_rcp60=fall_turnover_date ( temp , time_series , Vr,  lat= 59, V0=21.349*10**7  , A0=23.67*10**6 )
    
plt.plot(years_rcp60, estimated_end_jday_rcp60)

"""  
#%% Anaerobic duration according to Labrie et al 2023
# hich chize jadidi nadre hamoon anoxic factor (hata sade tar choon hypsographic info ro nadere)
# has subset shode vase har layer seperately:
    

def anearobic_duration_annually( C , time_series, threshold= 0.5):
    
    C_prof_indexed= pd.DataFrame(data= C, index=time_series)

    anoxia_prof_meet_01=(C_prof_indexed<= threshold)*1
    
    AD=anoxia_prof_meet_01.groupby(anoxia_prof_meet_01.index.year).sum()

    return AD

    
    