# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 04:29:07 2023

@author: mahta
"""

#%% annual anoxia duration_his

all_annual_Adur_his=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_his = pd.concat([all_annual_Adur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_his = pd.concat([all_annual_Adur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_his = pd.concat([all_annual_Adur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_his = pd.concat([all_annual_Adur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_Adur_his

anova_annual_Adur_his=annova_uncertainity(all_annual_Adur_his)

anova_annual_Adur_his.describe().loc['mean', :]
"""
GCMs             70.794808
param            28.169022
interaction       1.036169
GCMs/param        5.244952
year           1933.000000
Name: mean, dtype: float64
"""


anova_annual_Adur_his.describe().loc['std', :]
"""
GCMs           18.640629
param          18.331257
interaction     0.849029
GCMs/param      6.766538
year           42.001984
"""





#%% GLUE method on all_annual_Adur_his 
          

        
#all_annual_Adur_his= all_annual_Adur_his.set_index(all_annual_Adur_his['Datetime'])


# annual anoxia duration  
timeseries_year_his= all_annual_Adur_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_Adur_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_his=glue_df_annual_anoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxia_duration_his.csv')
        




#%% annual anoxia duration_rcp26

all_annual_Adur_rcp26=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp26 = pd.concat([all_annual_Adur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp26 = pd.concat([all_annual_Adur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp26 = pd.concat([all_annual_Adur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp26 = pd.concat([all_annual_Adur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_Adur_rcp26

anova_annual_Adur_rcp26=annova_uncertainity(all_annual_Adur_rcp26)

anova_annual_Adur_rcp26.describe().loc['mean', :]
"""
GCMs             67.750144
param            31.429108
interaction       0.820748
GCMs/param        3.576351
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_Adur_rcp26.describe().loc['std', :]
"""
GCMs           19.517556
param          19.142427
interaction     0.704613
GCMs/param      3.554716
year           27.279418
Name: std, dtype: float64
"""
#80 years:
anova_annual_80years_Adur_rcp26=annova_uncertainity(all_annual_Adur_rcp26[all_annual_Adur_rcp26.index>2019])


anova_annual_80years_Adur_rcp26.describe().loc['mean', :]
"""
GCMs             69.319597
param            29.892117
interaction       0.788287
GCMs/param        3.796300
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_Adur_rcp26.describe().loc['std', :]

"""

GCMs           18.469094
param          18.182648
interaction     0.636894
GCMs/param      3.735713
year           23.237900
Name: std, dtype: float64

"""


#%% GLUE method on all_annual_Adur_rcp26 
          

        
#all_annual_Adur_rcp26= all_annual_Adur_rcp26.set_index(all_annual_Adur_rcp26['Datetime'])


# annual anoxia duration  
timeseries_year_rcp26= all_annual_Adur_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_Adur_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxia_duration_rcp26.csv')
        

#%%%RCP6.0

#%% annual anoxia duration_rcp60

all_annual_Adur_rcp60=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp60 = pd.concat([all_annual_Adur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp60 = pd.concat([all_annual_Adur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp60 = pd.concat([all_annual_Adur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp60 = pd.concat([all_annual_Adur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_Adur_rcp60

anova_annual_Adur_rcp60=annova_uncertainity(all_annual_Adur_rcp60)

anova_annual_Adur_rcp60.describe().loc['mean', :]
"""
GCMs             72.224828
param            26.844518
interaction       0.930654
GCMs/param        5.034500
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_Adur_rcp60.describe().loc['std', :]
"""
GCMs           19.023038
param          18.397571
interaction     0.960231
GCMs/param      5.058178
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_Adur_rcp60=annova_uncertainity(all_annual_Adur_rcp60[all_annual_Adur_rcp60.index>2019])


anova_annual_80years_Adur_rcp60.describe().loc['mean', :]
"""
GCMs             72.193104
param            26.868151
interaction       0.938745
GCMs/param        4.841212
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_Adur_rcp60.describe().loc['std', :]

"""
GCMs           19.400557
param          18.749461
interaction     0.992036
GCMs/param      4.547039
year           23.237900
Name: std, dtype: float64

"""



#%% GLUE method on all_annual_Adur_rcp60 
          

        
#all_annual_Adur_rcp60= all_annual_Adur_rcp60.set_index(all_annual_Adur_rcp60['Datetime'])


# annual anoxia duration  
timeseries_year_rcp60= all_annual_Adur_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_Adur_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxia_duration_rcp60.csv')
        

#%%RCP8.5


#%% annual anoxia duration_rcp85

all_annual_Adur_rcp85=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp85 = pd.concat([all_annual_Adur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp85 = pd.concat([all_annual_Adur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp85 = pd.concat([all_annual_Adur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        all_annual_Adur_rcp85 = pd.concat([all_annual_Adur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_Adur_rcp85

anova_annual_Adur_rcp85=annova_uncertainity(all_annual_Adur_rcp85)

anova_annual_Adur_rcp85.describe().loc['mean', :]
"""
GCMs             81.111633
param            18.137212
interaction       0.751155
GCMs/param        7.789564
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_Adur_rcp85.describe().loc['std', :]
"""
GCMs           14.358204
param          13.722475
interaction     0.823996
GCMs/param      6.502858
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_Adur_rcp85=annova_uncertainity(all_annual_Adur_rcp85[all_annual_Adur_rcp85.index>2019])


anova_annual_80years_Adur_rcp85.describe().loc['mean', :]
"""
GCMs             81.615746
param            17.615484
interaction       0.768770
GCMs/param        8.271687
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_Adur_rcp85.describe().loc['std', :]

"""
GCMs           14.535742
param          13.812473
interaction     0.868265
GCMs/param      6.842409
year           23.237900
Name: std, dtype: float64
"""





#%% GLUE method on all_annual_Adur_rcp85 
          

        
#all_annual_Adur_rcp85= all_annual_Adur_rcp85.set_index(all_annual_Adur_rcp85['Datetime'])


# annual anoxia duration  
timeseries_year_rcp85= all_annual_Adur_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_Adur_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxia_duration_rcp85.csv')
        


#%%Plot of Anova test on his_all_annual_Adur_rcps

######his_annual_adur

#years
contributions_annual_Adur_his_years=anova_annual_Adur_his['year']
#GCMs
gcm_contributions_annual_Adur_his= anova_annual_Adur_his['GCMs']
#Param
param_contributions_annual_Adur_his=anova_annual_Adur_his['param']
#interaction
interact_contributions_annual_Adur_his =anova_annual_Adur_his['interaction']



######rcp26

#years
contributions_annual_Adur_rcp26_years=anova_annual_Adur_rcp26['year']
#GCMs
gcm_contributions_annual_Adur_rcp26 = anova_annual_Adur_rcp26['GCMs']
#Param
param_contributions_annual_Adur_rcp26 =anova_annual_Adur_rcp26['param']
#interaction
interact_contributions_annual_Adur_rcp26 =anova_annual_Adur_rcp26['interaction']

######rcp60

#years
contributions_annual_Adur_rcp60_years=anova_annual_Adur_rcp60['year']
#GCMs
gcm_contributions_annual_Adur_rcp60 = anova_annual_Adur_rcp60['GCMs']
#Param
param_contributions_annual_Adur_rcp60 =anova_annual_Adur_rcp60['param']
#interaction
interact_contributions_annual_Adur_rcp60 =anova_annual_Adur_rcp60['interaction']




######rcp85

#years
contributions_annual_Adur_rcp85_years=anova_annual_Adur_rcp85['year']
#GCMs
gcm_contributions_annual_Adur_rcp85 = anova_annual_Adur_rcp85['GCMs']
#Param
param_contributions_annual_Adur_rcp85 =anova_annual_Adur_rcp85['param']
#interaction
interact_contributions_annual_Adur_rcp85 =anova_annual_Adur_rcp85['interaction']




######Plotting:

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     


import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(2, 2, figsize=(20, 10), sharey=True)

# Define data for each subplot (assuming you have defined your data earlier)

# Subplot for his
axs[0, 0].fill_between(contributions_annual_Adur_his_years, 0, gcm_contributions_annual_Adur_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_Adur_his_years, gcm_contributions_annual_Adur_his , gcm_contributions_annual_Adur_his + param_contributions_annual_Adur_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_Adur_his_years, gcm_contributions_annual_Adur_his  + param_contributions_annual_Adur_his, gcm_contributions_annual_Adur_his + param_contributions_annual_Adur_his + interact_contributions_annual_Adur_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('His', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(1861, 2005)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)


# Subplot for rcp26
axs[0, 1].fill_between(contributions_annual_Adur_rcp26_years, 0, gcm_contributions_annual_Adur_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_Adur_rcp26_years, gcm_contributions_annual_Adur_rcp26, gcm_contributions_annual_Adur_rcp26 + param_contributions_annual_Adur_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_Adur_rcp26_years, gcm_contributions_annual_Adur_rcp26 + param_contributions_annual_Adur_rcp26, gcm_contributions_annual_Adur_rcp26 + param_contributions_annual_Adur_rcp26 + interact_contributions_annual_Adur_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1, 0].fill_between(contributions_annual_Adur_rcp60_years, 0, gcm_contributions_annual_Adur_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_Adur_rcp60_years, gcm_contributions_annual_Adur_rcp60, gcm_contributions_annual_Adur_rcp60 + param_contributions_annual_Adur_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_Adur_rcp60_years, gcm_contributions_annual_Adur_rcp60 + param_contributions_annual_Adur_rcp60, gcm_contributions_annual_Adur_rcp60 + param_contributions_annual_Adur_rcp60 + interact_contributions_annual_Adur_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[1, 1].fill_between(contributions_annual_Adur_rcp85_years, 0, gcm_contributions_annual_Adur_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_Adur_rcp85_years, gcm_contributions_annual_Adur_rcp85, gcm_contributions_annual_Adur_rcp85 + param_contributions_annual_Adur_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_Adur_rcp85_years, gcm_contributions_annual_Adur_rcp85 + param_contributions_annual_Adur_rcp85, gcm_contributions_annual_Adur_rcp85 + param_contributions_annual_Adur_rcp85 + interact_contributions_annual_Adur_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('RCP8.5', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in annual anoxia duration [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.73, 0.06), fontsize=22, ncol=3)


# Save the plot
plt.savefig('uncertainty_annual_anoxia_duration_his_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()




#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_annual_Adur_rcp26_years=anova_annual_Adur_rcp26[anova_annual_Adur_rcp26.year>2019].year
#gcms
gcm_contributions_80years_annual_Adur_rcp26 = anova_annual_Adur_rcp26[anova_annual_Adur_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_annual_Adur_rcp26 =anova_annual_Adur_rcp26[anova_annual_Adur_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_annual_Adur_rcp26 =anova_annual_Adur_rcp26[anova_annual_Adur_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_annual_Adur_rcp60_years=anova_annual_Adur_rcp60[anova_annual_Adur_rcp60.year>2019].year
#gcms
gcm_contributions_80years_annual_Adur_rcp60 = anova_annual_Adur_rcp60[anova_annual_Adur_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_annual_Adur_rcp60 =anova_annual_Adur_rcp60[anova_annual_Adur_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_annual_Adur_rcp60 =anova_annual_Adur_rcp60[anova_annual_Adur_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_annual_Adur_rcp85_years=anova_annual_Adur_rcp85[anova_annual_Adur_rcp85.year>2019].year
#gcms
gcm_contributions_80years_annual_Adur_rcp85 = anova_annual_Adur_rcp85[anova_annual_Adur_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_annual_Adur_rcp85 =anova_annual_Adur_rcp85[anova_annual_Adur_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_annual_Adur_rcp85 =anova_annual_Adur_rcp85[anova_annual_Adur_rcp85.year>2019]['interaction']


######Plotting:
# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path)     
    
    

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(24, 5), sharey=True)

# Define data for each subplot (assuming you have defined your data earlier)

# Subplot for rcp26
axs[0].fill_between(contributions_80years_annual_Adur_rcp26_years, 0, gcm_contributions_80years_annual_Adur_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_Adur_rcp26_years, gcm_contributions_80years_annual_Adur_rcp26, gcm_contributions_80years_annual_Adur_rcp26 + param_contributions_80years_annual_Adur_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_Adur_rcp26_years, gcm_contributions_80years_annual_Adur_rcp26 + param_contributions_80years_annual_Adur_rcp26, gcm_contributions_80years_annual_Adur_rcp26 + param_contributions_80years_annual_Adur_rcp26 + interact_contributions_80years_annual_Adur_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_annual_Adur_rcp60_years, 0, gcm_contributions_80years_annual_Adur_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_Adur_rcp60_years, gcm_contributions_80years_annual_Adur_rcp60, gcm_contributions_80years_annual_Adur_rcp60 + param_contributions_80years_annual_Adur_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_Adur_rcp60_years, gcm_contributions_80years_annual_Adur_rcp60 + param_contributions_80years_annual_Adur_rcp60, gcm_contributions_80years_annual_Adur_rcp60 + param_contributions_80years_annual_Adur_rcp60 + interact_contributions_80years_annual_Adur_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_annual_Adur_rcp85_years, 0, gcm_contributions_80years_annual_Adur_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_Adur_rcp85_years, gcm_contributions_80years_annual_Adur_rcp85, gcm_contributions_80years_annual_Adur_rcp85 + param_contributions_80years_annual_Adur_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_Adur_rcp85_years, gcm_contributions_80years_annual_Adur_rcp85 + param_contributions_80years_annual_Adur_rcp85, gcm_contributions_80years_annual_Adur_rcp85 + param_contributions_80years_annual_Adur_rcp85 + interact_contributions_80years_annual_Adur_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in\n annual anoxia duration [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.70, 0.06), fontsize=22 , ncol=3)



# Save the plot
plt.savefig('uncertainty_annual_anoxia_duration_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()









#%%monthly_table_of_anoxia_duartion

#%%monthly_table_of_anoxia_duartion_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%monthly_table_of_anoxia_duartion_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 

#%%monthly_table_of_anoxia_duartion_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_table_of_anoxia_duartion_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%%monthly_table_of_anoxia_duartion_hadgem_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 
#%%monthly_table_of_anoxia_duartion_hadgem_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_anoxia_duartion_hadgem_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
   
#%%monthly_table_of_anoxia_duartion_hadgem_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl

#%%monthly_table_of_anoxia_duartion_ipsl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_table_of_anoxia_duartion_ipsl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_anoxia_duartion_ipsl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%%monthly_table_of_anoxia_duartion_ipsl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
#%%monthly_table_of_anoxia_duartion_miroc_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
 
#%%monthly_table_of_anoxia_duartion_miroc_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_anoxia_duartion_miroc_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%%monthly_table_of_anoxia_duartion_miroc_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%sorting the indexs_annual_anoxia_duration 

glue_df_annual_anoxia_duration_his= glue_df_annual_anoxia_duration_his.sort_index()
glue_df_annual_anoxia_duration_rcp26= glue_df_annual_anoxia_duration_rcp26.sort_index()
glue_df_annual_anoxia_duration_rcp60= glue_df_annual_anoxia_duration_rcp60.sort_index()
glue_df_annual_anoxia_duration_rcp85= glue_df_annual_anoxia_duration_rcp85.sort_index()








#%%Plotting and analyses 



#%%########annual anoxia duration 

#%%ploting annual anoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['5%'], glue_df_annual_anoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['5%'], glue_df_annual_anoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['5%'], glue_df_annual_anoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['5%'], glue_df_annual_anoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Annual anoxia duration [d year $^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)#)   
fig.savefig("GLUE_Timeseries_annual_anoxia_duration.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_anoxia_duration_his['50%'])#36.913480290681775
np.mean(glue_df_annual_anoxia_duration_rcp26['50%'])#50.94331527912199
np.mean(glue_df_annual_anoxia_duration_rcp60['50%'])#55.23571819419276
np.mean(glue_df_annual_anoxia_duration_rcp85['50%'])#59.251978053765946

#%%anoxia_duration 30 yerars from each scenarios compare 



#Anomaly 
# baseline [1976-2005]
glue_base_annual_anoxia_duration_his=glue_df_annual_anoxia_duration_his[1975 < glue_df_annual_anoxia_duration_his.index]['50%']
annual_anoxia_duration_ref=np.mean(glue_base_annual_anoxia_duration_his)
#39.01394626296544


#near future [2030-2059]

glue_near_future_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26[(2029 < glue_df_annual_anoxia_duration_rcp26.index) & (glue_df_annual_anoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxia_duration_rcp26)
# 51.39036263577087
glue_near_future_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60[(2029 < glue_df_annual_anoxia_duration_rcp60.index) & (glue_df_annual_anoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxia_duration_rcp60)
# 52.051383699232375
glue_near_future_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85[(2029 < glue_df_annual_anoxia_duration_rcp85.index) & (glue_df_annual_anoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxia_duration_rcp85)
# 55.29349591259866

 
#Distant future [2070-2099]

glue_distant_future_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26[(2069 < glue_df_annual_anoxia_duration_rcp26.index) & (glue_df_annual_anoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_anoxia_duration_rcp26)
#52.15269420023649
glue_distant_future_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60[(2069 < glue_df_annual_anoxia_duration_rcp60.index) & (glue_df_annual_anoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_anoxia_duration_rcp60)
#63.836200506838665
glue_distant_future_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85[(2069 < glue_df_annual_anoxia_duration_rcp85.index) & (glue_df_annual_anoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_anoxia_duration_rcp85)
#72.37474187222797
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_anoxia_duration_his)
(0.058036189035261934,
 'positively autocorrelated',
 'increasing',
 0.01584310385808063,
 0.3076923076923077,
 34.290838047406915)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxia_duration_rcp26)
(0.02576640999957476,
 'positively autocorrelated',
 'no trend',
 0.16795155926741323,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxia_duration_rcp60)
(0.013060833974088573,
 'positively autocorrelated',
 'increasing',
 0.0026674112192179855,
 0.3333333333333333,
 47.666666666666664)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxia_duration_rcp85)
(0.020759079078481818,
 'positively autocorrelated',
 'increasing',
 0.005222214215088394,
 0.3699458986455131,
 49.63578446964006)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxia_duration_rcp26)
(0.021420574673772227,
 'positively autocorrelated',
 'no trend',
 0.25241607972826063,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxia_duration_rcp60)
(0.014062694900608859,
 'positively autocorrelated',
 'no trend',
 0.5548692736246672,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxia_duration_rcp85)
(0.01696677763319998,
 'positively autocorrelated',
 'increasing',
 0.03209713226201405,
 0.375,
 68.0625)





#%% 80 years from 2020 for annual_anoxia_duration


glue_80years_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26[2019 < glue_df_annual_anoxia_duration_rcp26.index]

glue_80years_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60[2019 < glue_df_annual_anoxia_duration_rcp60.index]

glue_80years_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85[2019 < glue_df_annual_anoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxia_duration_rcp26[glue_80years_annual_anoxia_duration_rcp26.index<2030]['50%'])
49.701546340129

#rcp6.0
np.mean(glue_80years_annual_anoxia_duration_rcp60[glue_80years_annual_anoxia_duration_rcp60.index<2030]['50%'])
49.5

#rcp8.5
np.mean(glue_80years_annual_anoxia_duration_rcp85[glue_80years_annual_anoxia_duration_rcp85.index<2030]['50%'])
49.6

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxia_duration_rcp26[glue_80years_annual_anoxia_duration_rcp26.index>2079]['50%'])
52.60304886899373

#rcp6.0
np.mean(glue_80years_annual_anoxia_duration_rcp60[glue_80years_annual_anoxia_duration_rcp60.index>2079]['50%'])
64.42704697657547

#rcp8.5
np.mean(glue_80years_annual_anoxia_duration_rcp85[glue_80years_annual_anoxia_duration_rcp85.index>2079]['50%'])
73.43302252468429

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp26['50%'])
(0.02731978280929722,
 'positively autocorrelated',
 'no trend',
 0.11077716737435672,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp60['50%'])
(0.015356080761850164,
 'positively autocorrelated',
 'increasing',
 4.583000645652646e-13,
 0.25925925925925924,
 45.75925925925926)

autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp85['50%'])
(0.019338985605904226,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.40008454654648684,
 45.196660411413774)



#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_his['50%'])
(0.08325982849800144,
 'positively autocorrelated',
 'no trend',
 0.06537537383706771,
 0,
 0)
#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp26['50%'])
(0.02686833590780329,
 'positively autocorrelated',
 'increasing',
 0.0027641779817251244,
 0.06870673100163874,
 47.8051370084238)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp60['50%'])
(0.018171938148639964,
 'positively autocorrelated',
 'increasing',
 4.440892098500626e-16,
 0.24,
 43.84)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp85['50%'])
(0.02048855231620791,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.39705882352941174,
 39.536764705882355)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 






 
#%%anoxia_duration_Anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index)].index.astype(float),
                      glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index)]['5%'] - annual_anoxia_duration_ref,
                      glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index) ]['95%'] - annual_anoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index) ].index.astype(float),
            glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index)]['50%'] - annual_anoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['5%']-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp26['95%']-annual_anoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['50%']-annual_anoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['5%']-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp60['95%']-annual_anoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['50%']-annual_anoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['5%']-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp85['95%']-annual_anoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['50%']-annual_anoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of annual anoxia duration [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol= 4)  
fig.savefig("GLUE_Timeseries_annual_anoxia_duration_Anomaly.png",  dpi=300, bbox_inches='tight')

#%%################################
###############################


#%%anoxia duration 80 years with trendline 




os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_annual_anoxia_duration_rcp26.index.astype(float), glue_80years_annual_anoxia_duration_rcp26['5%'], glue_80years_annual_anoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_annual_anoxia_duration_rcp26.index.astype(float), glue_80years_annual_anoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
ax=plt.plot([2020, 2021] , [14, 14], color='white' , label=' ')

trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp26['50%'])



ax=plt.fill_between(glue_80years_annual_anoxia_duration_rcp60.index.astype(float), glue_80years_annual_anoxia_duration_rcp60['5%'], glue_80years_annual_anoxia_duration_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_annual_anoxia_duration_rcp60.index.astype(float), glue_80years_annual_anoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp60['50%'])
ax=plt.text(2020, 8, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value <0.0001', color='orange', fontsize= 20 )

ax=plt.plot(glue_80years_annual_anoxia_duration_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3 , label='RCP6.0 trendline')


ax=plt.fill_between(glue_80years_annual_anoxia_duration_rcp85.index.astype(float), glue_80years_annual_anoxia_duration_rcp85['5%'], glue_80years_annual_anoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_annual_anoxia_duration_rcp85.index.astype(float), glue_80years_annual_anoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp85['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value <0.0001', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_annual_anoxia_duration_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3  , label='RCP8.5 trendline')



ax=plt.ylabel('Annual anoxia duration [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.2), fontsize=22 , ncol= 3)   
fig.savefig("GLUE_Timeseries_80years_annual_anoxia_duration_trendline.png",  dpi=300, bbox_inches='tight')




#%%Anlyses on the RCP2.6 with constant inital condition as 12.298 mg/L

#annual Adur
#gfdl

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_initialcond_attribution"

all_annual_Adur_rcp26_test= pd.DataFrame([])
all_weights= np.array([])



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0] 
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr , threshold=0.5)

        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)

        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
        
#hadgem

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_initialcond_attribution"





# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0] 
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr , threshold=0.5)

        
        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
       
        
#ipsl

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_initialcond_attribution"





# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0] 
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr , threshold=0.5)
   
        
        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
       
        
#miroc

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_initialcond_attribution"




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0] 
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr , threshold=0.5)
 
        
        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        

    
    

#%% GLUE of testing rcp26 scenarios for annual
all_annual_Adur_rcp26_test

all_annual_Adur_rcp26



diff_base_test_annual_Adur_rcp26= pd.DataFrame(np.array(all_annual_Adur_rcp26)-np.array(all_annual_Adur_rcp26_test))



all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_annual_Adur_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_annual_Adur_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_annual_Adur_rcp26=glue_diff_base_test_annual_Adur_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_annual_Adur_rcp26=glue_diff_base_test_annual_Adur_rcp26.sort_index()
glue_diff_base_test_annual_Adur_rcp26_80years=glue_diff_base_test_annual_Adur_rcp26[glue_diff_base_test_annual_Adur_rcp26.index>2019]



#%% analysing the difference of baseline scenarios and test with fixed inital condition 

#%%annual Adur

#decreaseing trend testing the initial condition effect 
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_Adur_rcp26_80years['50%'])
(2.0507104786004224,
 'negetively autocorrelated',
 'decreasing',
 0.027742077741620186,
 -0.010639121252663454,
 -0.07888327831675129)




#%%
all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_Adur_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_annual_Adur_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_annual_Adur_rcp26_test=glue_annual_Adur_rcp26_test.set_index(timeseries_year_rcp26)    
glue_annual_Adur_rcp26_test=glue_annual_Adur_rcp26_test.sort_index()
glue_annual_Adur_rcp26_test_80years=glue_annual_Adur_rcp26_test[glue_annual_Adur_rcp26_test.index>2019]



#%% is there any trendline over 80 years in RCP26 test scenario?
"""
Yes for annual Adur 
"""

#%% annual Adur
# effect of increasement in length of stratification is obvious 
autocorr_MK_org_modif_sens_slope_test(glue_annual_Adur_rcp26_test_80years['50%'])
(0.027614230829879908,
 'positively autocorrelated',
 'increasing',
 0.016793158201951597,
 0.058823529411764705,
 49.6764705882353)

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_annual_Adur_rcp26_test_80years.index.astype(float), glue_annual_Adur_rcp26_test_80years['5%'], glue_annual_Adur_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_annual_Adur_rcp26_test_80years.index.astype(float), glue_annual_Adur_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )


trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_annual_Adur_rcp26_test_80years['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_annual_Adur_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Annual anoxia duration of  RCP2.6\n with fixed inital condition [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22 , ncol= 2)#)   
fig.savefig("test_initalcondition_fixed_annual_Adur_80years_rcp26.png",  dpi=300, bbox_inches='tight')


#%%for paper both plot of diff and test of Apr_Oct rcp26 in one plot 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Create figure and axes for subplots
fig, axs = plt.subplots(1, 2, figsize=(25, 10))

# Plot for the first subplot
ax = axs[1]
ax.fill_between(glue_diff_base_test_annual_Adur_rcp26_80years.index,
                glue_diff_base_test_annual_Adur_rcp26_80years['5%'],
                glue_diff_base_test_annual_Adur_rcp26_80years['95%'],
                color='green', alpha=0.2, label='90% CI')
ax.plot(glue_diff_base_test_annual_Adur_rcp26_80years.index,
        glue_diff_base_test_annual_Adur_rcp26_80years['50%'],
        'green', label='Median', alpha=0.9, linewidth=3)

# Add trendline
trendline_rcp26_1 = autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_Adur_rcp26_80years['50%'])
#ax.text(0.95, 0.95, '(b)', transform=ax.transAxes, fontsize=22,
#        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 4, f'y = {trendline_rcp26_1[-2]:.3f}x + {trendline_rcp26_1[-1]:.3f}, p-value = {trendline_rcp26_1[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_diff_base_test_annual_Adur_rcp26_80years.index.astype(float),
        trendline_rcp26_1[-2] * np.arange(80) + trendline_rcp26_1[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3, label= 'Trendline')

# Set labels for the first subplot
ax.set_ylabel('Annual anoxia duration of RCP2.6 \n difference between fixed initial condition \n and original scenario in deep part  [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_diff_base_test_annual_Adur_rcp26_80years.index)
ax.set_xticklabels(glue_diff_base_test_annual_Adur_rcp26_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Plot for the second subplot
ax = axs[0]
ax.fill_between(glue_annual_Adur_rcp26_test_80years.index,
                glue_annual_Adur_rcp26_test_80years['5%'],
                glue_annual_Adur_rcp26_test_80years['95%'],
                color='green', alpha=0.2)#, label='90% CI')
ax.plot(glue_annual_Adur_rcp26_test_80years.index,
        glue_annual_Adur_rcp26_test_80years['50%'].astype(float),
        'green', alpha=0.9, linewidth=3)# label='Median',

# Add trendline
trendline_rcp26_0 = autocorr_MK_org_modif_sens_slope_test(glue_annual_Adur_rcp26_test_80years['50%'])
#ax.text(0.95, 0.95, '(a)', transform=ax.transAxes, fontsize=22,
#        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 80, f'y = {trendline_rcp26_0[-2]:.3f}x + {trendline_rcp26_0[-1]:.3f}, p-value = {trendline_rcp26_0[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_annual_Adur_rcp26_test_80years.index,
        trendline_rcp26_0[-2] * np.arange(80) + trendline_rcp26_0[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)

# Set labels for the second subplot
ax.set_ylabel('Annual anoxia duration of RCP2.6 with\n fixed initial condition in deep part [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_annual_Adur_rcp26_test_80years.index)
ax.set_xticklabels(glue_annual_Adur_rcp26_test_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Add a single legend for both subplots in the center bottom
#fig.legend(loc='lower center', fontsize=22, ncol=3)
fig.legend(loc='lower center', fontsize=22, ncol=3, bbox_to_anchor=(0.5, -0.05))
plt.tight_layout()


plt.savefig("atttest_difference_test_initalcondition_fixed_annual_Adur_80years_rcp26.png",  dpi=300, bbox_inches='tight')


















#%% ###########OLD
#%%Anlyses on the RCP2.6 with constant inital condition as 12.298 mg/L

#annual/May_Sep/Summer anoxia duration
#gfdl

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_initialcond_fixedintercpt_attribution"

all_annual_Adur_rcp26_test= pd.DataFrame([])
all_May_Sep_Adur_rcp26_test= pd.DataFrame([])
all_summer_Adur_rcp26_test= pd.DataFrame([])
all_weights= np.array([])



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_May_Sep =May_Sep_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_summer =summer_anoxia_duration (C, time_series, Vr, threshold=0.5)
        
        
        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)
        all_May_Sep_Adur_rcp26_test= pd.concat([all_May_Sep_Adur_rcp26_test , result_May_Sep], axis=1)
        all_summer_Adur_rcp26_test= pd.concat([all_summer_Adur_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_adur'])
        
        
        # Save the result May_Sep to a new CSV file
        result_May_Sep_filename = f'May_Sep_Adur_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Sep_filename))#, index=False)
       

        result_May_Sep.to_csv(os.path.join(directory, result_May_Sep_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_adur'])
    
        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_Adur_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_adur'])
    
        
#hadgem

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_initialcond_fixedintercpt_attribution"





# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_May_Sep =May_Sep_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_summer =summer_anoxia_duration (C, time_series, Vr, threshold=0.5)
        
        
        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)
        all_May_Sep_Adur_rcp26_test= pd.concat([all_May_Sep_Adur_rcp26_test , result_May_Sep], axis=1)
        all_summer_Adur_rcp26_test= pd.concat([all_summer_Adur_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_adur'])
        
        
        # Save the result May_Sep to a new CSV file
        result_May_Sep_filename = f'May_Sep_Adur_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Sep_filename))#, index=False)
       

        result_May_Sep.to_csv(os.path.join(directory, result_May_Sep_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_adur'])
    
        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_Adur_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_adur'])
    
        
#ipsl

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_initialcond_fixedintercpt_attribution"





# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_May_Sep =May_Sep_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_summer =summer_anoxia_duration (C, time_series, Vr, threshold=0.5)
        
        
        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)
        all_May_Sep_Adur_rcp26_test= pd.concat([all_May_Sep_Adur_rcp26_test , result_May_Sep], axis=1)
        all_summer_Adur_rcp26_test= pd.concat([all_summer_Adur_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_adur'])
        
        
        # Save the result May_Sep to a new CSV file
        result_May_Sep_filename = f'May_Sep_Adur_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Sep_filename))#, index=False)
       

        result_May_Sep.to_csv(os.path.join(directory, result_May_Sep_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_adur'])
    
        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_Adur_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_adur'])
    
        
#miroc

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_initialcond_fixedintercpt_attribution"




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        Vr= hypo_morpho_vriables_gotm_grid[0]
        # Apply the  function
        result_annual =annual_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_May_Sep =May_Sep_anoxia_duration (C, time_series, Vr, threshold=0.5)
        result_summer =summer_anoxia_duration (C, time_series, Vr, threshold=0.5)
        
        
        all_annual_Adur_rcp26_test = pd.concat([all_annual_Adur_rcp26_test , result_annual], axis=1)
        all_May_Sep_Adur_rcp26_test= pd.concat([all_May_Sep_Adur_rcp26_test , result_May_Sep], axis=1)
        all_summer_Adur_rcp26_test= pd.concat([all_summer_Adur_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_Adur_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_adur'])
        
        
        # Save the result May_Sep to a new CSV file
        result_May_Sep_filename = f'May_Sep_Adur_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Sep_filename))#, index=False)
       

        result_May_Sep.to_csv(os.path.join(directory, result_May_Sep_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_adur'])
    
        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_Adur_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_adur'])
    
    
    
    
    
    
    
    
        
#%% GLUE of testing rcp26 scenarios for annual/May_Sep/Summer anoxia duration
all_annual_Adur_rcp26_test
all_May_Sep_Adur_rcp26_test
all_summer_Adur_rcp26_test

all_annual_Adur_rcp26
all_May_Sep_Adur_rcp26
all_summer_Adur_rcp26


diff_base_test_annual_Adur_rcp26= pd.DataFrame(np.array(all_annual_Adur_rcp26)-np.array(all_annual_Adur_rcp26_test))

diff_base_test_May_Sep_Adur_rcp26= pd.DataFrame(np.array(all_May_Sep_Adur_rcp26)-np.array(all_May_Sep_Adur_rcp26_test))

diff_base_test_summer_Adur_rcp26= pd.DataFrame(np.array(all_summer_Adur_rcp26)-np.array(all_summer_Adur_rcp26_test))



all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_annual_Adur_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_annual_Adur_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_annual_Adur_rcp26=glue_diff_base_test_annual_Adur_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_annual_Adur_rcp26=glue_diff_base_test_annual_Adur_rcp26.sort_index()
glue_diff_base_test_annual_Adur_rcp26_80years=glue_diff_base_test_annual_Adur_rcp26[glue_diff_base_test_annual_Adur_rcp26.index>2019]


# May_Sep DO hypolimnion 
timeseries_year_rcp26= all_May_Sep_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_May_Sep_Adur_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_May_Sep_Adur_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_May_Sep_Adur_rcp26=glue_diff_base_test_May_Sep_Adur_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_May_Sep_Adur_rcp26=glue_diff_base_test_May_Sep_Adur_rcp26.sort_index()
glue_diff_base_test_May_Sep_Adur_rcp26_80years=glue_diff_base_test_May_Sep_Adur_rcp26[glue_diff_base_test_May_Sep_Adur_rcp26.index>2019]

# summer DO hypolimnion 
timeseries_year_rcp26= all_summer_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_summer_Adur_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_summer_Adur_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_summer_Adur_rcp26=glue_diff_base_test_summer_Adur_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_summer_Adur_rcp26=glue_diff_base_test_summer_Adur_rcp26.sort_index()
glue_diff_base_test_summer_Adur_rcp26_80years=glue_diff_base_test_summer_Adur_rcp26[glue_diff_base_test_summer_Adur_rcp26.index>2019]


#%% analysing the difference of baseline scenarios and test with fixed inital condition 

#%%Annual anoxia duration

autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_summer_Adur_rcp26_80years['50%'])
(0.7556963877764784,
 'positively autocorrelated',
 'no trend',
 0.38167289783888103,
 0,
 0)

#%%May_Sep anoxia duration


autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_May_Sep_Adur_rcp26['50%'])
(0.7133311686522206,
 'positively autocorrelated',
 'no trend',
 0.5265123417676232,
 0,
 0)

#%%sunmmer AF


autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_summer_Adur_rcp26['50%'])
(0.7033728682865076,
 'positively autocorrelated',
 'no trend',
 0.5088060152190437,
 0,
 0)









#%%
all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_Adur_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_annual_Adur_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_annual_Adur_rcp26_test=glue_annual_Adur_rcp26_test.set_index(timeseries_year_rcp26)    
glue_annual_Adur_rcp26_test=glue_annual_Adur_rcp26_test.sort_index()
glue_annual_Adur_rcp26_test_80years=glue_annual_Adur_rcp26_test[glue_annual_Adur_rcp26_test.index>2019]


# May_Sep DO hypolimnion 
timeseries_year_rcp26= all_May_Sep_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_Adur_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_May_Sep_Adur_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_May_Sep_Adur_rcp26_test=glue_May_Sep_Adur_rcp26_test.set_index(timeseries_year_rcp26)    
glue_May_Sep_Adur_rcp26_test=glue_May_Sep_Adur_rcp26_test.sort_index()
glue_May_Sep_Adur_rcp26_test_80years=glue_May_Sep_Adur_rcp26_test[glue_May_Sep_Adur_rcp26_test.index>2019]

# summer DO hypolimnion 
timeseries_year_rcp26= all_summer_Adur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_Adur_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_summer_Adur_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_summer_Adur_rcp26_test=glue_summer_Adur_rcp26_test.set_index(timeseries_year_rcp26)    
glue_summer_Adur_rcp26_test=glue_summer_Adur_rcp26_test.sort_index()
glue_summer_Adur_rcp26_test_80years=glue_summer_Adur_rcp26_test[glue_summer_Adur_rcp26_test.index>2019]


#%% is there any trendline over 80 years in RCP26 test scenario?
"""
Yes for Annual anoxia duration and May_Sep 
but no for summer 
"""

#%% Annual anoxia duration
autocorr_MK_org_modif_sens_slope_test(glue_annual_Adur_rcp26_test_80years['50%'])
(0.020094656965566497,
 'positively autocorrelated',
 'increasing',
 0.00038027721833899797,
 0.08695652173913043,
 50.56521739130435)

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_annual_Adur_rcp26_test_80years.index.astype(float), glue_annual_Adur_rcp26_test_80years['5%'], glue_annual_Adur_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_annual_Adur_rcp26_test_80years.index.astype(float), glue_annual_Adur_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_annual_Adur_rcp26_test_80years['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_annual_Adur_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Anoxia duration in deoxygenation period of RCP2.6 with fixed inital condition [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("test_initalcondition_fixed_annual_Anoxia_dur_80years_rcp26.png",  dpi=300, bbox_inches='tight')



#%% May_Sep_adur 


autocorr_MK_org_modif_sens_slope_test(glue_May_Sep_Adur_rcp26_test_80years['50%'])
(0.020094656965566497,
 'positively autocorrelated',
 'increasing',
 0.00038027721833899797,
 0.08695652173913043,
 50.56521739130435)


os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_May_Sep_Adur_rcp26_test_80years.index.astype(float), glue_May_Sep_Adur_rcp26_test_80years['5%'], glue_May_Sep_Adur_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_May_Sep_Adur_rcp26_test_80years.index.astype(float), glue_May_Sep_Adur_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_May_Sep_Adur_rcp26_test_80years['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_May_Sep_Adur_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Anoxia duration in May-Sep of RCP2.6 with fixed inital condition [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("test_initalcondition_fixed_May_Sep_Anoxia_dur_80years_rcp26.png",  dpi=300, bbox_inches='tight')










#%% Summer anoxia duration

autocorr_MK_org_modif_sens_slope_test(glue_summer_Adur_rcp26_test_80years['50%'])

(0.013333728118060268,
 'positively autocorrelated',
 'no trend',
 0.07910446959150863,
 0,
 0)









#%%%%%%%%======================
#============OLD
#############
#%% Annual anoxia duration_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                

#%% May_Sep anoxia duration_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#%% May_Sep anoxia duration_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                


                


#%%monthly_table_of_anoxia_duartion_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                










#%%monthly_table_of_anoxia_duartion_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%% Annual anoxia duration_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                

#%% May_Sep anoxia duration_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_hadgem_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#%% May_Sep anoxia duration_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                


                


#%%monthly_table_of_anoxia_duartion_hadgem_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                










#%%monthly_table_of_anoxia_duartion_hadgem_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_hadgem_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl
#%% Annual anoxia duration_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                

#%% May_Sep anoxia duration_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_ipsl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#%% May_Sep anoxia duration_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                


                


#%%monthly_table_of_anoxia_duartion_ipsl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                










#%%monthly_table_of_anoxia_duartion_ipsl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_ipsl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%miroc 
#%% Annual anoxia duration_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                

#%% May_Sep anoxia duration_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_miroc_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
#%% May_Sep anoxia duration_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                


                


#%%monthly_table_of_anoxia_duartion_miroc_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                










#%%monthly_table_of_anoxia_duartion_miroc_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                
#%% May_Sep anoxia duration_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = May_Sep_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_anoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_anoxia_duration'])
        
                
#%% summer anoxia duration_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = summer_anoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_anoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_anoxia_duration'])
        
                




#%%monthly_table_of_anoxia_duartion_miroc_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duartion_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his_annual_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_annual_anoxia_duration_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_his = pd.concat([all_annual_anoxia_duration_his , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_his = pd.concat([all_annual_anoxia_duration_his , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_his = pd.concat([all_annual_anoxia_duration_his , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_his = pd.concat([all_annual_anoxia_duration_his , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        
all_annual_anoxia_duration_his= all_annual_anoxia_duration_his.set_index(annual_anoxia_duration['year'])


# annual anoxia duration  
timeseries_year_his= all_annual_anoxia_duration_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_his=glue_df_annual_anoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxia_duration_his.csv')


#%%rcp26_annual_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_annual_anoxia_duration_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp26 = pd.concat([all_annual_anoxia_duration_rcp26 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp26 = pd.concat([all_annual_anoxia_duration_rcp26 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp26 = pd.concat([all_annual_anoxia_duration_rcp26 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp26 = pd.concat([all_annual_anoxia_duration_rcp26 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        

all_annual_anoxia_duration_rcp26= all_annual_anoxia_duration_rcp26.set_index(annual_anoxia_duration['year'])

# annual anoxia duration  
timeseries_year_rcp26= all_annual_anoxia_duration_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxia_duration_rcp26.csv')


#%%rcp60_annual_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_annual_anoxia_duration_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp60 = pd.concat([all_annual_anoxia_duration_rcp60 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp60 = pd.concat([all_annual_anoxia_duration_rcp60 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp60 = pd.concat([all_annual_anoxia_duration_rcp60 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp60 = pd.concat([all_annual_anoxia_duration_rcp60 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        

all_annual_anoxia_duration_rcp60= all_annual_anoxia_duration_rcp60.set_index(annual_anoxia_duration['year'])

# annual anoxia duration  
timeseries_year_rcp60= all_annual_anoxia_duration_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxia_duration_rcp60.csv')

#%%rcp85_annual_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_annual_anoxia_duration_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp85 = pd.concat([all_annual_anoxia_duration_rcp85 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp85 = pd.concat([all_annual_anoxia_duration_rcp85 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp85 = pd.concat([all_annual_anoxia_duration_rcp85 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration.index)
        
        all_annual_anoxia_duration_rcp85 = pd.concat([all_annual_anoxia_duration_rcp85 , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        
all_annual_anoxia_duration_rcp85= all_annual_anoxia_duration_rcp85.set_index(annual_anoxia_duration['year'])


# annual anoxia duration  
timeseries_year_rcp85= all_annual_anoxia_duration_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxia_duration_rcp85.csv')




#%%sorting the indexs_annual_anoxia_duration 

glue_df_annual_anoxia_duration_his= glue_df_annual_anoxia_duration_his.sort_index()
glue_df_annual_anoxia_duration_rcp26= glue_df_annual_anoxia_duration_rcp26.sort_index()
glue_df_annual_anoxia_duration_rcp60= glue_df_annual_anoxia_duration_rcp60.sort_index()
glue_df_annual_anoxia_duration_rcp85= glue_df_annual_anoxia_duration_rcp85.sort_index()


#%% May_Sep anoxia duration
#%%his_May_Sep_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_May_Sep_anoxia_duration_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_his = pd.concat([all_May_Sep_anoxia_duration_his , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_his = pd.concat([all_May_Sep_anoxia_duration_his , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_his = pd.concat([all_May_Sep_anoxia_duration_his , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_his = pd.concat([all_May_Sep_anoxia_duration_his , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        
        
all_May_Sep_anoxia_duration_his= all_May_Sep_anoxia_duration_his.set_index(May_Sep_anoxia_duration['year'])


# May_Sep anoxia duration  
timeseries_year_his= all_May_Sep_anoxia_duration_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_anoxia_duration_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_anoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_anoxia_duration_his=glue_df_May_Sep_anoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_anoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxia_duration_his.csv')


#%%rcp26_May_Sep_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_May_Sep_anoxia_duration_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp26 = pd.concat([all_May_Sep_anoxia_duration_rcp26 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp26 = pd.concat([all_May_Sep_anoxia_duration_rcp26 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp26 = pd.concat([all_May_Sep_anoxia_duration_rcp26 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp26 = pd.concat([all_May_Sep_anoxia_duration_rcp26 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        
        

all_May_Sep_anoxia_duration_rcp26= all_May_Sep_anoxia_duration_rcp26.set_index(May_Sep_anoxia_duration['year'])

# May_Sep anoxia duration  
timeseries_year_rcp26= all_May_Sep_anoxia_duration_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_anoxia_duration_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_anoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_anoxia_duration_rcp26=glue_df_May_Sep_anoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxia_duration_rcp26.csv')


#%%rcp60_May_Sep_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_May_Sep_anoxia_duration_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp60 = pd.concat([all_May_Sep_anoxia_duration_rcp60 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp60 = pd.concat([all_May_Sep_anoxia_duration_rcp60 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp60 = pd.concat([all_May_Sep_anoxia_duration_rcp60 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp60 = pd.concat([all_May_Sep_anoxia_duration_rcp60 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        
        

all_May_Sep_anoxia_duration_rcp60= all_May_Sep_anoxia_duration_rcp60.set_index(May_Sep_anoxia_duration['year'])

# May_Sep anoxia duration  
timeseries_year_rcp60= all_May_Sep_anoxia_duration_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_anoxia_duration_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_anoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_anoxia_duration_rcp60=glue_df_May_Sep_anoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxia_duration_rcp60.csv')

#%%rcp85_May_Sep_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_May_Sep_anoxia_duration_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp85 = pd.concat([all_May_Sep_anoxia_duration_rcp85 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp85 = pd.concat([all_May_Sep_anoxia_duration_rcp85 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp85 = pd.concat([all_May_Sep_anoxia_duration_rcp85 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_anoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_anoxia_duration=May_Sep_anoxia_duration.set_index(May_Sep_anoxia_duration.index)
        
        all_May_Sep_anoxia_duration_rcp85 = pd.concat([all_May_Sep_anoxia_duration_rcp85 , May_Sep_anoxia_duration['May_Sep_anoxia_duration']], axis=1)
        
        
        
        
all_May_Sep_anoxia_duration_rcp85= all_May_Sep_anoxia_duration_rcp85.set_index(May_Sep_anoxia_duration['year'])


# May_Sep anoxia duration  
timeseries_year_rcp85= all_May_Sep_anoxia_duration_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_anoxia_duration_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_anoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_anoxia_duration_rcp85=glue_df_May_Sep_anoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxia_duration_rcp85.csv')



#%%sorting the indexs_May_Sep_anoxia_duration 

glue_df_May_Sep_anoxia_duration_his= glue_df_May_Sep_anoxia_duration_his.sort_index()
glue_df_May_Sep_anoxia_duration_rcp26= glue_df_May_Sep_anoxia_duration_rcp26.sort_index()
glue_df_May_Sep_anoxia_duration_rcp60= glue_df_May_Sep_anoxia_duration_rcp60.sort_index()
glue_df_May_Sep_anoxia_duration_rcp85= glue_df_May_Sep_anoxia_duration_rcp85.sort_index()



#%%===== summer anoxia duration Glue dataframe 

#%%his_summer_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_summer_anoxia_duration_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_his = pd.concat([all_summer_anoxia_duration_his , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_his = pd.concat([all_summer_anoxia_duration_his , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_his = pd.concat([all_summer_anoxia_duration_his , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_his = pd.concat([all_summer_anoxia_duration_his , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        
        
all_summer_anoxia_duration_his= all_summer_anoxia_duration_his.set_index(summer_anoxia_duration['year'])


# summer anoxia duration  
timeseries_year_his= all_summer_anoxia_duration_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_anoxia_duration_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_anoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_anoxia_duration_his=glue_df_summer_anoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_anoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxia_duration_his.csv')


#%%rcp26_summer_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_summer_anoxia_duration_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp26 = pd.concat([all_summer_anoxia_duration_rcp26 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp26 = pd.concat([all_summer_anoxia_duration_rcp26 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp26 = pd.concat([all_summer_anoxia_duration_rcp26 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp26 = pd.concat([all_summer_anoxia_duration_rcp26 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        
        

all_summer_anoxia_duration_rcp26= all_summer_anoxia_duration_rcp26.set_index(summer_anoxia_duration['year'])

# summer anoxia duration  
timeseries_year_rcp26= all_summer_anoxia_duration_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_anoxia_duration_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_anoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_anoxia_duration_rcp26=glue_df_summer_anoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxia_duration_rcp26.csv')


#%%rcp60_summer_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_summer_anoxia_duration_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp60 = pd.concat([all_summer_anoxia_duration_rcp60 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp60 = pd.concat([all_summer_anoxia_duration_rcp60 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp60 = pd.concat([all_summer_anoxia_duration_rcp60 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp60 = pd.concat([all_summer_anoxia_duration_rcp60 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        
        

all_summer_anoxia_duration_rcp60= all_summer_anoxia_duration_rcp60.set_index(summer_anoxia_duration['year'])

# summer anoxia duration  
timeseries_year_rcp60= all_summer_anoxia_duration_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_anoxia_duration_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_anoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_anoxia_duration_rcp60=glue_df_summer_anoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxia_duration_rcp60.csv')

#%%rcp85_summer_anoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_summer_anoxia_duration_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp85 = pd.concat([all_summer_anoxia_duration_rcp85 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp85 = pd.concat([all_summer_anoxia_duration_rcp85 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp85 = pd.concat([all_summer_anoxia_duration_rcp85 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_anoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_anoxia_duration=summer_anoxia_duration.set_index(summer_anoxia_duration.index)
        
        all_summer_anoxia_duration_rcp85 = pd.concat([all_summer_anoxia_duration_rcp85 , summer_anoxia_duration['summer_anoxia_duration']], axis=1)
        
        
        
        
all_summer_anoxia_duration_rcp85= all_summer_anoxia_duration_rcp85.set_index(summer_anoxia_duration['year'])


# summer anoxia duration  
timeseries_year_rcp85= all_summer_anoxia_duration_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_anoxia_duration_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_anoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_anoxia_duration_rcp85=glue_df_summer_anoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxia_duration_rcp85.csv')


#%%sorting the indexs_summer_anoxia_duration 

glue_df_summer_anoxia_duration_his= glue_df_summer_anoxia_duration_his.sort_index()
glue_df_summer_anoxia_duration_rcp26= glue_df_summer_anoxia_duration_rcp26.sort_index()
glue_df_summer_anoxia_duration_rcp60= glue_df_summer_anoxia_duration_rcp60.sort_index()
glue_df_summer_anoxia_duration_rcp85= glue_df_summer_anoxia_duration_rcp85.sort_index()













#%%Plotting and analyses 



#%%########annual anoxia duration 

#%%ploting annual anoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['5%'], glue_df_annual_anoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['5%'], glue_df_annual_anoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['5%'], glue_df_annual_anoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['5%'], glue_df_annual_anoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anoxia duration per each deoxygenation period [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_annual_anoxia_duration.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_anoxia_duration_his['50%'])#6.077082662821386
np.mean(glue_df_annual_anoxia_duration_rcp26['50%'])#7.992767795524755
np.mean(glue_df_annual_anoxia_duration_rcp60['50%'])#8.585258963812871
np.mean(glue_df_annual_anoxia_duration_rcp85['50%'])#9.156680524881311

#%%anoxia_duration 30 yerars from each scenarios compare 



#Anomaly 
# baseline [1976-2005]
glue_base_annual_anoxia_duration_his=glue_df_annual_anoxia_duration_his[1975 < glue_df_annual_anoxia_duration_his.index]['50%']
annual_anoxia_duration_ref=np.mean(glue_base_annual_anoxia_duration_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26[(2029 < glue_df_annual_anoxia_duration_rcp26.index) & (glue_df_annual_anoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxia_duration_rcp26)
# 8.070525139552648
glue_near_future_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60[(2029 < glue_df_annual_anoxia_duration_rcp60.index) & (glue_df_annual_anoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxia_duration_rcp60)
# 8.107889314159742
glue_near_future_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85[(2029 < glue_df_annual_anoxia_duration_rcp85.index) & (glue_df_annual_anoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_anoxia_duration_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26[(2069 < glue_df_annual_anoxia_duration_rcp26.index) & (glue_df_annual_anoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_anoxia_duration_rcp26)
#8.153608896799094
glue_distant_future_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60[(2069 < glue_df_annual_anoxia_duration_rcp60.index) & (glue_df_annual_anoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_anoxia_duration_rcp60)
#9.787975473676404
glue_distant_future_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85[(2069 < glue_df_annual_anoxia_duration_rcp85.index) & (glue_df_annual_anoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_anoxia_duration_rcp85)
#10.985644903398574
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_anoxia_duration_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxia_duration_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxia_duration_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_anoxia_duration_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxia_duration_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxia_duration_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_anoxia_duration_rcp85)
(0.014499198182054042,
 'positively autocorrelated',
 'increasing',
 0.026946782463489027,
 0.05377923636923881,
 10.323144222989352)






#%% 80 years from 2020 for annual_anoxia_duration


glue_80years_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26[2019 < glue_df_annual_anoxia_duration_rcp26.index]

glue_80years_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60[2019 < glue_df_annual_anoxia_duration_rcp60.index]

glue_80years_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85[2019 < glue_df_annual_anoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxia_duration_rcp26[glue_80years_annual_anoxia_duration_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_annual_anoxia_duration_rcp60[glue_80years_annual_anoxia_duration_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_annual_anoxia_duration_rcp85[glue_80years_annual_anoxia_duration_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_anoxia_duration_rcp26[glue_80years_annual_anoxia_duration_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_annual_anoxia_duration_rcp60[glue_80years_annual_anoxia_duration_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_annual_anoxia_duration_rcp85[glue_80years_annual_anoxia_duration_rcp85.index>2079]['50%'])
11.160292464667199

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)



autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_anoxia_duration_rcp85['50%'])
(0.015711631920486826,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05742827331247126,
 7.128166722990812)





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp85['50%'])
(0.01670964657273115,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05615663487366421,
 6.386209763383056)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxia_duration_Anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index)].index.astype(float),
                      glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index)]['5%'] - annual_anoxia_duration_ref,
                      glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index) ]['95%'] - annual_anoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index) ].index.astype(float),
            glue_df_annual_anoxia_duration_his[(1960 < glue_df_annual_anoxia_duration_his.index)]['50%'] - annual_anoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['5%']-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp26['95%']-annual_anoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['50%']-annual_anoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['5%']-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp60['95%']-annual_anoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['50%']-annual_anoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['5%']-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp85['95%']-annual_anoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['50%']-annual_anoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of annual anoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_annual_anoxia_duration_Anomaly.png",  dpi=300, bbox_inches='tight')











#%%===========May-Sep average of anoxia duration


#%%ploting May_Sep anoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_his.index.astype(float), glue_df_May_Sep_anoxia_duration_his['5%'], glue_df_May_Sep_anoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_May_Sep_anoxia_duration_his.index.astype(float), glue_df_May_Sep_anoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp26['5%'], glue_df_May_Sep_anoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_May_Sep_anoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp60['5%'], glue_df_May_Sep_anoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Sep_anoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp85['5%'], glue_df_May_Sep_anoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Sep_anoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anoxia duration May-Sep [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_May_Sep_anoxia_duration.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_May_Sep_anoxia_duration_his['50%'])#6.077082662821386
np.mean(glue_df_May_Sep_anoxia_duration_rcp26['50%'])#7.992767795524755
np.mean(glue_df_May_Sep_anoxia_duration_rcp60['50%'])#8.585258963812871
np.mean(glue_df_May_Sep_anoxia_duration_rcp85['50%'])#9.149586881905822

#%%anoxia_duration 30 yerars from each scenarios compare 



#Anomaly 
# baseline [1976-2005]
glue_base_May_Sep_anoxia_duration_his=glue_df_May_Sep_anoxia_duration_his[1975 < glue_df_May_Sep_anoxia_duration_his.index]['50%']
May_Sep_anoxia_duration_ref=np.mean(glue_base_May_Sep_anoxia_duration_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_May_Sep_anoxia_duration_rcp26=glue_df_May_Sep_anoxia_duration_rcp26[(2029 < glue_df_May_Sep_anoxia_duration_rcp26.index) & (glue_df_May_Sep_anoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_May_Sep_anoxia_duration_rcp26)
# 8.070525139552648
glue_near_future_May_Sep_anoxia_duration_rcp60=glue_df_May_Sep_anoxia_duration_rcp60[(2029 < glue_df_May_Sep_anoxia_duration_rcp60.index) & (glue_df_May_Sep_anoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_May_Sep_anoxia_duration_rcp60)
# 8.107889314159742
glue_near_future_May_Sep_anoxia_duration_rcp85=glue_df_May_Sep_anoxia_duration_rcp85[(2029 < glue_df_May_Sep_anoxia_duration_rcp85.index) & (glue_df_May_Sep_anoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_May_Sep_anoxia_duration_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_May_Sep_anoxia_duration_rcp26=glue_df_May_Sep_anoxia_duration_rcp26[(2069 < glue_df_May_Sep_anoxia_duration_rcp26.index) & (glue_df_May_Sep_anoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_May_Sep_anoxia_duration_rcp26)
#8.153608896799094
glue_distant_future_May_Sep_anoxia_duration_rcp60=glue_df_May_Sep_anoxia_duration_rcp60[(2069 < glue_df_May_Sep_anoxia_duration_rcp60.index) & (glue_df_May_Sep_anoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_May_Sep_anoxia_duration_rcp60)
#9.787975473676404
glue_distant_future_May_Sep_anoxia_duration_rcp85=glue_df_May_Sep_anoxia_duration_rcp85[(2069 < glue_df_May_Sep_anoxia_duration_rcp85.index) & (glue_df_May_Sep_anoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_May_Sep_anoxia_duration_rcp85)
#10.963418155408705
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_May_Sep_anoxia_duration_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Sep_anoxia_duration_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Sep_anoxia_duration_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Sep_anoxia_duration_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Sep_anoxia_duration_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Sep_anoxia_duration_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Sep_anoxia_duration_rcp85)
(0.014377923696788013,
 'positively autocorrelated',
 'increasing',
 0.0322801899241516,
 0.04781875151369361,
 10.409571253394757)






#%% 80 years from 2020 for May_Sep_anoxia_duration


glue_80years_May_Sep_anoxia_duration_rcp26=glue_df_May_Sep_anoxia_duration_rcp26[2019 < glue_df_May_Sep_anoxia_duration_rcp26.index]

glue_80years_May_Sep_anoxia_duration_rcp60=glue_df_May_Sep_anoxia_duration_rcp60[2019 < glue_df_May_Sep_anoxia_duration_rcp60.index]

glue_80years_May_Sep_anoxia_duration_rcp85=glue_df_May_Sep_anoxia_duration_rcp85[2019 < glue_df_May_Sep_anoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Sep_anoxia_duration_rcp26[glue_80years_May_Sep_anoxia_duration_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_May_Sep_anoxia_duration_rcp60[glue_80years_May_Sep_anoxia_duration_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_May_Sep_anoxia_duration_rcp85[glue_80years_May_Sep_anoxia_duration_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Sep_anoxia_duration_rcp26[glue_80years_May_Sep_anoxia_duration_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_May_Sep_anoxia_duration_rcp60[glue_80years_May_Sep_anoxia_duration_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_May_Sep_anoxia_duration_rcp85[glue_80years_May_Sep_anoxia_duration_rcp85.index>2079]['50%'])
11.12826268210691

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_anoxia_duration_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_anoxia_duration_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_anoxia_duration_rcp85['50%'])
(0.015654880429522035,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05661191309631117,
 7.160412951529136)

#%%plotting May_Sep anoxia duration over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_May_Sep_anoxia_duration_rcp26.index.astype(float), glue_80years_May_Sep_anoxia_duration_rcp26['5%'], glue_80years_May_Sep_anoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_May_Sep_anoxia_duration_rcp26.index.astype(float), glue_80years_May_Sep_anoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_May_Sep_anoxia_duration_rcp60.index.astype(float), glue_80years_May_Sep_anoxia_duration_rcp60['5%'], glue_80years_May_Sep_anoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_May_Sep_anoxia_duration_rcp60.index.astype(float), glue_80years_May_Sep_anoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_anoxia_duration_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_May_Sep_anoxia_duration_rcp85.index.astype(float), glue_80years_May_Sep_anoxia_duration_rcp85['5%'], glue_80years_May_Sep_anoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_May_Sep_anoxia_duration_rcp85.index.astype(float), glue_80years_May_Sep_anoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_anoxia_duration_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('Anoxia duration in May_Sep [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_May_Sep_anoxia_duration.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_anoxia_duration_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_anoxia_duration_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)


#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_anoxia_duration_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_anoxia_duration_rcp85['50%'])
(0.016659625265317696,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05578367086692144,
 6.403552589696595)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxia_duration_Anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_his[(1960 < glue_df_May_Sep_anoxia_duration_his.index)].index.astype(float),
                      glue_df_May_Sep_anoxia_duration_his[(1960 < glue_df_May_Sep_anoxia_duration_his.index)]['5%'] - May_Sep_anoxia_duration_ref,
                      glue_df_May_Sep_anoxia_duration_his[(1960 < glue_df_May_Sep_anoxia_duration_his.index) ]['95%'] - May_Sep_anoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_May_Sep_anoxia_duration_his[(1960 < glue_df_May_Sep_anoxia_duration_his.index) ].index.astype(float),
            glue_df_May_Sep_anoxia_duration_his[(1960 < glue_df_May_Sep_anoxia_duration_his.index)]['50%'] - May_Sep_anoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp26['5%']-May_Sep_anoxia_duration_ref, glue_df_May_Sep_anoxia_duration_rcp26['95%']-May_Sep_anoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Sep_anoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp26['50%']-May_Sep_anoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp60['5%']-May_Sep_anoxia_duration_ref, glue_df_May_Sep_anoxia_duration_rcp60['95%']-May_Sep_anoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Sep_anoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp60['50%']-May_Sep_anoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Sep_anoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp85['5%']-May_Sep_anoxia_duration_ref, glue_df_May_Sep_anoxia_duration_rcp85['95%']-May_Sep_anoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Sep_anoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_anoxia_duration_rcp85['50%']-May_Sep_anoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of anoxia duration in May-Sep [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_May_Sep_anoxia_duration_Anomaly.png",  dpi=300, bbox_inches='tight')













#%%===========summer average of anoxia duration


#%%########summer anoxia duration 

#%%ploting summer anoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_anoxia_duration_his.index.astype(float), glue_df_summer_anoxia_duration_his['5%'], glue_df_summer_anoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_summer_anoxia_duration_his.index.astype(float), glue_df_summer_anoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_summer_anoxia_duration_rcp26.index.astype(float), glue_df_summer_anoxia_duration_rcp26['5%'], glue_df_summer_anoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_summer_anoxia_duration_rcp26.index.astype(float), glue_df_summer_anoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_summer_anoxia_duration_rcp60.index.astype(float), glue_df_summer_anoxia_duration_rcp60['5%'], glue_df_summer_anoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_anoxia_duration_rcp60.index.astype(float), glue_df_summer_anoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_anoxia_duration_rcp85.index.astype(float), glue_df_summer_anoxia_duration_rcp85['5%'], glue_df_summer_anoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_anoxia_duration_rcp85.index.astype(float), glue_df_summer_anoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anoxia duration in summer [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_summer_anoxia_duration.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_summer_anoxia_duration_his['50%'])#5.7419538116211175
np.mean(glue_df_summer_anoxia_duration_rcp26['50%'])#7.164633836912792
np.mean(glue_df_summer_anoxia_duration_rcp60['50%'])#7.660016638342764
np.mean(glue_df_summer_anoxia_duration_rcp85['50%'])#7.798265277646058

#%%anoxia_duration 30 yerars from each scenarios compare 



#Anomaly 
# baseline [1976-2005]
glue_base_summer_anoxia_duration_his=glue_df_summer_anoxia_duration_his[1975 < glue_df_summer_anoxia_duration_his.index]['50%']
summer_anoxia_duration_ref=np.mean(glue_base_summer_anoxia_duration_his)
#5.830216997377137


#near future [2030-2059]

glue_near_future_summer_anoxia_duration_rcp26=glue_df_summer_anoxia_duration_rcp26[(2029 < glue_df_summer_anoxia_duration_rcp26.index) & (glue_df_summer_anoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_summer_anoxia_duration_rcp26)
# 7.189791199644448
glue_near_future_summer_anoxia_duration_rcp60=glue_df_summer_anoxia_duration_rcp60[(2029 < glue_df_summer_anoxia_duration_rcp60.index) & (glue_df_summer_anoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_summer_anoxia_duration_rcp60)
# 7.408290028941934
glue_near_future_summer_anoxia_duration_rcp85=glue_df_summer_anoxia_duration_rcp85[(2029 < glue_df_summer_anoxia_duration_rcp85.index) & (glue_df_summer_anoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_summer_anoxia_duration_rcp85)
# 7.577321792421727

 
#Distant future [2070-2099]

glue_distant_future_summer_anoxia_duration_rcp26=glue_df_summer_anoxia_duration_rcp26[(2069 < glue_df_summer_anoxia_duration_rcp26.index) & (glue_df_summer_anoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_summer_anoxia_duration_rcp26)
#7.182315856408658
glue_distant_future_summer_anoxia_duration_rcp60=glue_df_summer_anoxia_duration_rcp60[(2069 < glue_df_summer_anoxia_duration_rcp60.index) & (glue_df_summer_anoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_summer_anoxia_duration_rcp60)
#8.404224632950019
glue_distant_future_summer_anoxia_duration_rcp85=glue_df_summer_anoxia_duration_rcp85[(2069 < glue_df_summer_anoxia_duration_rcp85.index) & (glue_df_summer_anoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_summer_anoxia_duration_rcp85)
#8.844476856722357
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_summer_anoxia_duration_his)
(0.03384344872449237,
 'positively autocorrelated',
 'no trend',
 0.2389927879015219,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_anoxia_duration_rcp26)
(0.017426799559486894,
 'positively autocorrelated',
 'no trend',
 0.2686642304239091,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_anoxia_duration_rcp60)
(0.011027838419972513,
 'positively autocorrelated',
 'no trend',
 0.08039114754218035,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_anoxia_duration_rcp85)

(0.010531400508757774,
 'positively autocorrelated',
 'increasing',
 0.0053825476031263975,
 0.0337942438328447,
 7.0319428173255965)


#Distant future [2070-2099]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_anoxia_duration_rcp26)
(0.007455597611559313,
 'positively autocorrelated',
 'increasing',
 0.011479484705922305,
 0.03254964585051723,
 6.704083850293537)
#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_anoxia_duration_rcp60)
(0.005218209926031563,
 'positively autocorrelated',
 'no trend',
 0.7752944295177846,
 0,
 0)
#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_anoxia_duration_rcp85)
(0.011260089055346817,
 'positively autocorrelated',
 'no trend',
 0.2844114676220473,
 0,
 0)





#%% 80 years from 2020 for summer_anoxia_duration


glue_80years_summer_anoxia_duration_rcp26=glue_df_summer_anoxia_duration_rcp26[2019 < glue_df_summer_anoxia_duration_rcp26.index]

glue_80years_summer_anoxia_duration_rcp60=glue_df_summer_anoxia_duration_rcp60[2019 < glue_df_summer_anoxia_duration_rcp60.index]

glue_80years_summer_anoxia_duration_rcp85=glue_df_summer_anoxia_duration_rcp85[2019 < glue_df_summer_anoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_anoxia_duration_rcp26[glue_80years_summer_anoxia_duration_rcp26.index<2030]['50%'])
7.236131611808827

#rcp6.0
np.mean(glue_80years_summer_anoxia_duration_rcp60[glue_80years_summer_anoxia_duration_rcp60.index<2030]['50%'])
7.0480838080216754

#rcp8.5
np.mean(glue_80years_summer_anoxia_duration_rcp85[glue_80years_summer_anoxia_duration_rcp85.index<2030]['50%'])
6.92973720099211

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_anoxia_duration_rcp26[glue_80years_summer_anoxia_duration_rcp26.index>2079]['50%'])
7.284732847455828

#rcp6.0
np.mean(glue_80years_summer_anoxia_duration_rcp60[glue_80years_summer_anoxia_duration_rcp60.index>2079]['50%'])
8.376808940760498

#rcp8.5
np.mean(glue_80years_summer_anoxia_duration_rcp85[glue_80years_summer_anoxia_duration_rcp85.index>2079]['50%'])
8.902897713112784

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_anoxia_duration_rcp26['50%'])
(0.012431261551918694,
 'positively autocorrelated',
 'no trend',
 0.4722909038902814,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_anoxia_duration_rcp60['50%'])
(0.009054412557226742,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.021466406502838986,
 6.936654760438897)


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_anoxia_duration_rcp85['50%'])
(0.012767144112602902,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031086674796400225,
 6.7697952941890875)



#%%plotting summer anoxia duration over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_summer_anoxia_duration_rcp26.index.astype(float), glue_80years_summer_anoxia_duration_rcp26['5%'], glue_80years_summer_anoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_summer_anoxia_duration_rcp26.index.astype(float), glue_80years_summer_anoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_summer_anoxia_duration_rcp60.index.astype(float), glue_80years_summer_anoxia_duration_rcp60['5%'], glue_80years_summer_anoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_summer_anoxia_duration_rcp60.index.astype(float), glue_80years_summer_anoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_anoxia_duration_rcp60['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_summer_anoxia_duration_rcp85.index.astype(float), glue_80years_summer_anoxia_duration_rcp85['5%'], glue_80years_summer_anoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_summer_anoxia_duration_rcp85.index.astype(float), glue_80years_summer_anoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_anoxia_duration_rcp85['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('Anoxia duration in summer [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_summer_anoxia_duration.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire scenario

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_anoxia_duration_his['50%'])
(0.050102399473259764,
 'positively autocorrelated',
 'no trend',
 0.15346389188435516,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_anoxia_duration_rcp26['50%'])
(0.011480536925277993,
 'positively autocorrelated',
 'increasing',
 0.030392451085676786,
 0.0039129273367328335,
 6.963469344761228)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_anoxia_duration_rcp60['50%'])
(0.010198727721089741,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.02131982928372496,
 6.689481345978918)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_anoxia_duration_rcp85['50%'])
(0.014688565156364046,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031748328950495945,
 6.343632396381782)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxia_duration_Anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_anoxia_duration_his[(1960 < glue_df_summer_anoxia_duration_his.index)].index.astype(float),
                      glue_df_summer_anoxia_duration_his[(1960 < glue_df_summer_anoxia_duration_his.index)]['5%'] - summer_anoxia_duration_ref,
                      glue_df_summer_anoxia_duration_his[(1960 < glue_df_summer_anoxia_duration_his.index) ]['95%'] - summer_anoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_summer_anoxia_duration_his[(1960 < glue_df_summer_anoxia_duration_his.index) ].index.astype(float),
            glue_df_summer_anoxia_duration_his[(1960 < glue_df_summer_anoxia_duration_his.index)]['50%'] - summer_anoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_summer_anoxia_duration_rcp26.index.astype(float), glue_df_summer_anoxia_duration_rcp26['5%']-summer_anoxia_duration_ref, glue_df_summer_anoxia_duration_rcp26['95%']-summer_anoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_anoxia_duration_rcp26.index.astype(float), glue_df_summer_anoxia_duration_rcp26['50%']-summer_anoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_summer_anoxia_duration_rcp60.index.astype(float), glue_df_summer_anoxia_duration_rcp60['5%']-summer_anoxia_duration_ref, glue_df_summer_anoxia_duration_rcp60['95%']-summer_anoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_anoxia_duration_rcp60.index.astype(float), glue_df_summer_anoxia_duration_rcp60['50%']-summer_anoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_anoxia_duration_rcp85.index.astype(float), glue_df_summer_anoxia_duration_rcp85['5%']-summer_anoxia_duration_ref, glue_df_summer_anoxia_duration_rcp85['95%']-summer_anoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_anoxia_duration_rcp85.index.astype(float), glue_df_summer_anoxia_duration_rcp85['50%']-summer_anoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of anoxia duration in summer [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_summer_anoxia_duration_Anomaly.png",  dpi=300, bbox_inches='tight')










#%%
####################################old one
############################################
############################################

#%% Annual anoxia duration_gfdl_his
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duartion_gfdl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_gfdl_rcp26
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_gfdl_rcp26

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_gfdl_rcp60
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_gfdl_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_gfdl_rcp85
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_gfdl_rcp85

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in gfdl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxia duration_hadgem_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_hadgem_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_hadgem_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_hadgem_rcp26

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_hadgem_rcp60
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_hadgem_rcp60

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_hadgem_rcp85
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_hadgem_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in hadgem rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxia duration_ipsl_his
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_ipsl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_ipsl_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_ipsl_rcp26

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_ipsl_rcp60
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_ipsl_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_ipsl_rcp85
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_ipsl_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_miroc_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_miroc_his

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_his_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxia duration_miroc_rcp26
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_miroc_rcp26

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxia duration_miroc_rcp60
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_miroc_rcp60

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxia duration_miroc_rcp85
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = annual_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_anoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_anoxia_duration'])
        
                


#%%monthly_table_of_anoxia_duration_miroc_rcp85

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jv_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_anoxia_duration function
        result = monthly_table_of_anoxia_duration(C, time_series,Vr, threshold=0.5)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'



all_annual_anoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        


# annual anoxia duration  
timeseries_year_his= all_annual_anoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_his=glue_df_annual_anoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxia_duration_his.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_fixedtheta/glue_df_anoxia_duration_his.csv')



####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_calibinfixedtheta_simuvartheta/glue_df_anoxia_duration_his.csv')

#%%rcp26


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_calibinfixedtheta_simuvartheta'



all_annual_anoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_fixedthetaincalib_simurcp26temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        


# annual anoxia duration  
timeseries_year_rcp26= all_annual_anoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxia_duration_rcp26.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxia_duration_rcp26.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#########glue_df_annual_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxia_duration_rcp26.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxia_duration_rcp26.csv')



#%%rcp60


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_calibinfixedtheta_simuvartheta'



all_annual_anoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_fixedthetaincalib_simurcp60temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        


# annual anoxia duration  
timeseries_year_rcp60= all_annual_anoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxia_duration_rcp60.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxia_duration_rcp60.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#########glue_df_annual_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxia_duration_rcp60.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxia_duration_rcp60.csv')



#%%rcp85


# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_calibinfixedtheta_simuvartheta'



all_annual_anoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'


######## fixed theta both in calib and simulation 
######## directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedtheta'


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#######directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_fixedthetaincalib_simurcp85temp20202021'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_anoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_anoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_anoxia_duration=annual_anoxia_duration.set_index(annual_anoxia_duration['year'])
        
        all_annual_anoxia_duration = pd.concat([all_annual_anoxia_duration , annual_anoxia_duration['annual_anoxia_duration']], axis=1)
        
        
        
        


# annual anoxia duration  
timeseries_year_rcp85= all_annual_anoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_anoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_anoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxia_duration_rcp85.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxia_duration_rcp85.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#########glue_df_annual_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxia_duration_rcp85.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_anoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxia_duration_rcp85.csv')


#%%#######fixed theta:
    
#######glue_df_annual_anoxia_duration_his_fixedtheta=  glue_df_annual_anoxia_duration_his.copy()

glue_df_annual_anoxia_duration_his= glue_df_annual_anoxia_duration_his_fixedtheta.copy()

#######glue_df_annual_anoxia_duration_rcp26_fixedtheta=  glue_df_annual_anoxia_duration_rcp26.copy()

glue_df_annual_anoxia_duration_rcp26= glue_df_annual_anoxia_duration_rcp26_fixedtheta.copy()

#######glue_df_annual_anoxia_duration_rcp60_fixedtheta=  glue_df_annual_anoxia_duration_rcp60.copy()

glue_df_annual_anoxia_duration_rcp60= glue_df_annual_anoxia_duration_rcp60_fixedtheta.copy()

#######glue_df_annual_anoxia_duration_rcp85_fixedtheta=  glue_df_annual_anoxia_duration_rcp85.copy()

glue_df_annual_anoxia_duration_rcp85= glue_df_annual_anoxia_duration_rcp85_fixedtheta.copy()



#%%_vartheta

glue_df_annual_anoxia_duration_his_vartheta= glue_df_annual_anoxia_duration_his.copy()



glue_df_annual_anoxia_duration_rcp26_vartheta= glue_df_annual_anoxia_duration_rcp26.copy()


glue_df_annual_anoxia_duration_rcp60_vartheta= glue_df_annual_anoxia_duration_rcp60.copy()


glue_df_annual_anoxia_duration_rcp85_vartheta= glue_df_annual_anoxia_duration_rcp85.copy()


#%%difference of Vartheta model and fixed theta 


diff_median_annual_anoxia_duration_vartheta_fixedtheta_his=glue_df_annual_anoxia_duration_his_vartheta['50%']-glue_df_annual_anoxia_duration_his['50%']
np.mean(diff_median_annual_anoxia_duration_vartheta_fixedtheta_his)
-1.521539830552154

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxia_duration_vartheta_fixedtheta_his)
(0.4102745697759908,
 'positively autocorrelated',
 'no trend',
 0.08641995700155558,
 0,
 0)




diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp26=glue_df_annual_anoxia_duration_rcp26_vartheta['50%']-glue_df_annual_anoxia_duration_rcp26['50%']
np.mean(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp26)
-2.3009426195783225
autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp26)

(0.2471291056619972,
 'positively autocorrelated',
 'no trend',
 0.5406757306713583,
 0,
 0)



diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp60=glue_df_annual_anoxia_duration_rcp60_vartheta['50%']-glue_df_annual_anoxia_duration_rcp60['50%']
np.mean(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp60)
-1.3593195664094877

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp60)
(0.45142216245912026,
 'positively autocorrelated',
 'no trend',
 0.24575216426645285,
 0,
 0)



diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp85=glue_df_annual_anoxia_duration_rcp85_vartheta['50%']-glue_df_annual_anoxia_duration_rcp85['50%']
np.mean(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp85)
-1.8403265395237618

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp85)
(0.4311903996849538,
 'positively autocorrelated',
 'no trend',
 0.05029548584424548,
 0,
 0)


#Plot the difference of median

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.plot(diff_median_annual_anoxia_duration_vartheta_fixedtheta_his.index, diff_median_annual_anoxia_duration_vartheta_fixedtheta_his, 'grey', label='His median', alpha=1, linewidth=3 )


ax=plt.plot(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp26.index, diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp26, 'green', label='RCP2.6 median', alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp60.index, diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp60, 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp85.index, diff_median_annual_anoxia_duration_vartheta_fixedtheta_rcp85, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )



ax=plt.ylabel('Difference of fixed and variable Ktemp assumption in simulating annual anoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(-4, 3, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22)


####### test with fixed theta in calibration but variable for GOTM simulation 
fig.savefig("GLUE_Timeseries_hypolimnetic_DO_6combinationJaJv_ave_obs_4models_diff_fixed_var_theta.png", dpi=300, bbox_inches='tight')




#%% first 10 years 2020-2029

#rcp26
glue_df_annual_anoxia_duration_median_1st_10years_rcp26=glue_df_annual_anoxia_duration_rcp26[(2019<glue_df_annual_anoxia_duration_rcp26.index) & (glue_df_annual_anoxia_duration_rcp26.index<2030)]['50%']
np.mean(glue_df_annual_anoxia_duration_median_1st_10years_rcp26)
#7.470031426050075

glue_df_annual_anoxia_duration_median_1st_10years_rcp26_vartheta=glue_df_annual_anoxia_duration_rcp26_vartheta[(2019<glue_df_annual_anoxia_duration_rcp26_vartheta.index) & (glue_df_annual_anoxia_duration_rcp26_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_anoxia_duration_median_1st_10years_rcp26_vartheta)
#5.655030434919324


#rcp60

glue_df_annual_anoxia_duration_median_1st_10years_rcp60=glue_df_annual_anoxia_duration_rcp60[(2019<glue_df_annual_anoxia_duration_rcp60.index) & (glue_df_annual_anoxia_duration_rcp60.index<2030)]['50%']
np.mean(glue_df_annual_anoxia_duration_median_1st_10years_rcp60)
#7.077280785340525



glue_df_annual_anoxia_duration_median_1st_10years_rcp60_vartheta=glue_df_annual_anoxia_duration_rcp60_vartheta[(2019<glue_df_annual_anoxia_duration_rcp60_vartheta.index) & (glue_df_annual_anoxia_duration_rcp60_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_anoxia_duration_median_1st_10years_rcp60_vartheta)
#5.442294872796134

#rcp85

glue_df_annual_anoxia_duration_median_1st_10years_rcp85=glue_df_annual_anoxia_duration_rcp85[(2019<glue_df_annual_anoxia_duration_rcp85.index) & (glue_df_annual_anoxia_duration_rcp85.index<2030)]['50%']
np.mean(glue_df_annual_anoxia_duration_median_1st_10years_rcp85)
#6.80621601212993

glue_df_annual_anoxia_duration_median_1st_10years_rcp85_vartheta=glue_df_annual_anoxia_duration_rcp85_vartheta[(2019<glue_df_annual_anoxia_duration_rcp85_vartheta.index) & (glue_df_annual_anoxia_duration_rcp85_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_anoxia_duration_median_1st_10years_rcp85_vartheta)
#5.589130553716512

#%%last 10 years 2090-2099

#rcp26
glue_df_annual_anoxia_duration_median_last_10years_rcp26=glue_df_annual_anoxia_duration_rcp26[glue_df_annual_anoxia_duration_rcp26.index>2089]['50%']
np.mean(glue_df_annual_anoxia_duration_median_last_10years_rcp26)
#8.613753815447875

glue_df_annual_anoxia_duration_median_last_10years_rcp26_vartheta=glue_df_annual_anoxia_duration_rcp26_vartheta[glue_df_annual_anoxia_duration_rcp26_vartheta.index>2089]['50%']
np.mean(glue_df_annual_anoxia_duration_median_last_10years_rcp26_vartheta)
#5.99974215818178

#rcp60
glue_df_annual_anoxia_duration_median_last_10years_rcp60=glue_df_annual_anoxia_duration_rcp60[glue_df_annual_anoxia_duration_rcp60.index>2089]['50%']
np.mean(glue_df_annual_anoxia_duration_median_last_10years_rcp60)
#8.840670784774442

glue_df_annual_anoxia_duration_median_last_10years_rcp60_vartheta=glue_df_annual_anoxia_duration_rcp60_vartheta[glue_df_annual_anoxia_duration_rcp60_vartheta.index>2089]['50%']
np.mean(glue_df_annual_anoxia_duration_median_last_10years_rcp60_vartheta)
#7.461205289215991
#rcp85
glue_df_annual_anoxia_duration_median_last_10years_rcp85=glue_df_annual_anoxia_duration_rcp85[glue_df_annual_anoxia_duration_rcp85.index>2089]['50%']
np.mean(glue_df_annual_anoxia_duration_median_last_10years_rcp85)
#10.848450635366076

glue_df_annual_anoxia_duration_median_last_10years_rcp85_vartheta=glue_df_annual_anoxia_duration_rcp85_vartheta[glue_df_annual_anoxia_duration_rcp85_vartheta.index>2089]['50%']
np.mean(glue_df_annual_anoxia_duration_median_last_10years_rcp85_vartheta)
#9.225106418152142

#%% 100 years for rcps 

#rcp26

#fixed theta
glue_df_annual_anoxia_duration_4models_100years_rcp26=pd.concat([glue_df_annual_anoxia_duration_his[glue_df_annual_anoxia_duration_his.index>1999] , glue_df_annual_anoxia_duration_rcp26])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxia_duration_4models_100years_rcp26 ['50%'])  

(0.03233165257593502,
 'positively autocorrelated',
 'increasing',
 1.235052435877293e-07,
 0.0121937938499866,
 7.255097746966682)





#Var theta
glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta=pd.concat([glue_df_annual_anoxia_duration_his_vartheta[glue_df_annual_anoxia_duration_his_vartheta.index>1999] , glue_df_annual_anoxia_duration_rcp26_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta ['50%'])  

(0.03955505915646442,
 'positively autocorrelated',
 'increasing',
 0.0006010992236442636,
 0.010497984593900105,
 5.030834333984101)



#rcp60

#fixed theta
glue_df_annual_anoxia_duration_4models_100years_rcp60=pd.concat([glue_df_annual_anoxia_duration_his[glue_df_annual_anoxia_duration_his.index>1999] , glue_df_annual_anoxia_duration_rcp60])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxia_duration_4models_100years_rcp60 ['50%'])  
(0.02795672807292709,
 'positively autocorrelated',
 'increasing',
 2.220446049250313e-16,
 0.0332750689583886,
 5.986757230735907)




#Var theta
glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta=pd.concat([glue_df_annual_anoxia_duration_his_vartheta[glue_df_annual_anoxia_duration_his_vartheta.index>1999] , glue_df_annual_anoxia_duration_rcp60_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta ['50%'])  
(0.029177475988549587,
 'positively autocorrelated',
 'increasing',
 2.970956813896919e-13,
 0.03420571640423424,
 4.397863069746866)


#rcp85

#fixed theta
glue_df_annual_anoxia_duration_4models_100years_rcp85=pd.concat([glue_df_annual_anoxia_duration_his[glue_df_annual_anoxia_duration_his.index>1999] , glue_df_annual_anoxia_duration_rcp85])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxia_duration_4models_100years_rcp85 ['50%'])  
(0.031072004914250547,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05455817956023478,
 5.832292270455436)




#Var theta
glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta=pd.concat([glue_df_annual_anoxia_duration_his_vartheta[glue_df_annual_anoxia_duration_his_vartheta.index>1999] , glue_df_annual_anoxia_duration_rcp85_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta ['50%'])  

(0.035580951696717295,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05165045008766002,
 3.9207344560109947)

#%% trendline sen's slope 

autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_his['50%']) 

Out[1243]: 
(0.08861134396877238,
 'positively autocorrelated',
 'no trend',
 0.10192618852194646,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_his_vartheta['50%']) 

(0.1383412609645987,
 'positively autocorrelated',
 'no trend',
 0.31072008139962315,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp26['50%']) 
(0.03379118006876991,
 'positively autocorrelated',
 'increasing',
 6.908279212325397e-05,
 0.010564337601135008,
 7.4785025189153735)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp26_vartheta['50%']) 
(0.039507716688300144,
 'positively autocorrelated',
 'increasing',
 0.022504355893704142,
 0.008218111766768784,
 5.1831384217248875)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp60['50%']) 
(0.028720309370685593,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.03880652178553318,
 5.88161432295651)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp60_vartheta['50%']) 
(0.028883853368500165,
 'positively autocorrelated',
 'increasing',
 7.286293790542686e-10,
 0.033514404467106934,
 4.616452079764355)


autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp85['50%']) 
(0.03167796451466309,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.059792750353943616,
 5.873773932605548)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_rcp85_vartheta['50%']) 
(0.03389759807269532,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05300685412619691,
 4.1760561507416)



#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%Annual anoxia duration 

#Vartheta

#########original test with variable theta:
#########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/')


######## fixed theta both in calib and simulation 
########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/')


###### test with fixed theta in calibration a temp ave hypo in GCMs in 2020 2021
######os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/')


####### test with fixed theta in calibration but variable for GOTM simulation 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/')


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


#ax=plt.fill_between(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['5%'], glue_df_annual_anoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta['5%'], glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_4models_100years_rcp26_vartheta['50%'])
ax=plt.text(2020, 10, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta['5%'], glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_4models_100years_rcp60_vartheta['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta['5%'], glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_4models_100years_rcp85_vartheta['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxia duration per each deoxygenation period [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxia_duration_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


#%%fixed theta




#########original test with variable theta:
#########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/')


######## fixed theta both in calib and simulation 
########os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/')


###### test with fixed theta in calibration a temp ave hypo in GCMs in 2020 2021
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/')


####### test with fixed theta in calibration but variable for GOTM simulation 
######os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/')


import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


#ax=plt.fill_between(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['5%'], glue_df_annual_anoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_anoxia_duration_his.index.astype(float), glue_df_annual_anoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_anoxia_duration_4models_100years_rcp26.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp26['5%'], glue_df_annual_anoxia_duration_4models_100years_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_4models_100years_rcp26.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_4models_100years_rcp26['50%'])
ax=plt.text(2020, 15, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_anoxia_duration_4models_100years_rcp60.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp60['5%'], glue_df_annual_anoxia_duration_4models_100years_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_4models_100years_rcp60.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_4models_100years_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_anoxia_duration_4models_100years_rcp85.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp85['5%'], glue_df_annual_anoxia_duration_4models_100years_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_4models_100years_rcp85.index.astype(float), glue_df_annual_anoxia_duration_4models_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_anoxia_duration_4models_100years_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxia duration per each deoxygenation period [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxia_duration_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
# original # fixed gcm temp in 2020 and 2021
np.mean(glue_df_annual_anoxia_duration_his['50%'])#5.118056494914366# 5.371846482897608
np.mean(glue_df_annual_anoxia_duration_rcp26['50%'])#7.009871810216667# 7.960074150018018
np.mean(glue_df_annual_anoxia_duration_rcp60['50%'])#7.599031745432739# 7.661889247294462
np.mean(glue_df_annual_anoxia_duration_rcp85['50%'])#8.15444840073441#8.680607289244922

np.mean(glue_df_annual_anoxia_duration_his_vartheta['50%'])#3.8503066523454508
np.mean(glue_df_annual_anoxia_duration_rcp26_vartheta['50%'])#5.659131530439698
np.mean(glue_df_annual_anoxia_duration_rcp60_vartheta['50%'])#6.302569680884974
np.mean(glue_df_annual_anoxia_duration_rcp85_vartheta['50%'])#6.840280749721157



#%%anoxia_duration 30 yerars from each scenarios compare 


#Sorting the glue dataframe according to the index (year)

glue_df_annual_anoxia_duration_his=glue_df_annual_anoxia_duration_his.sort_index()

glue_df_annual_anoxia_duration_rcp26=glue_df_annual_anoxia_duration_rcp26.sort_index()

glue_df_annual_anoxia_duration_rcp60=glue_df_annual_anoxia_duration_rcp60.sort_index()

glue_df_annual_anoxia_duration_rcp85=glue_df_annual_anoxia_duration_rcp85.sort_index()





#Anomaly 

# baseline [1976-2005]
annual_anoxia_duration_ref=glue_df_annual_anoxia_duration_his[1975 < glue_df_annual_anoxia_duration_his.index]['50%'].mean()

#5.410877320721374
#5.914740063212032


#near future [2030-2059] 

glue_df_annual_anoxia_duration_rcp26[(2029 < glue_df_annual_anoxia_duration_rcp26.index) & (glue_df_annual_anoxia_duration_rcp26.index < 2060)]['50%'].mean()
# 7.072947718287684
# 7.950218353351354
glue_df_annual_anoxia_duration_rcp60[(2029 < glue_df_annual_anoxia_duration_rcp60.index) & (glue_df_annual_anoxia_duration_rcp60.index < 2060)]['50%'].mean()
# 7.156265572954701
# 7.139975067233944

glue_df_annual_anoxia_duration_rcp85[(2029 < glue_df_annual_anoxia_duration_rcp85.index) & (glue_df_annual_anoxia_duration_rcp85.index < 2060)]['50%'].mean()
# 7.630745663516447
# 8.223867040126178
 
#Distant future [2070-2099]

glue_df_annual_anoxia_duration_rcp26[(2069 < glue_df_annual_anoxia_duration_rcp26.index) & (glue_df_annual_anoxia_duration_rcp26.index < 2100)]['50%'].mean()
#7.17035474380281
#8.221226628944514


glue_df_annual_anoxia_duration_rcp60[(2069 < glue_df_annual_anoxia_duration_rcp60.index) & (glue_df_annual_anoxia_duration_rcp60.index < 2100)]['50%'].mean()
#8.781804641713899
#8.984771173520228

glue_df_annual_anoxia_duration_rcp85[(2069 < glue_df_annual_anoxia_duration_rcp85.index) & (glue_df_annual_anoxia_duration_rcp85.index < 2100)]['50%'].mean()
#7.630745663516447
# 10.612461480324987



#%%anoxia_duration_Anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_anoxia_duration_his[1975 < glue_df_annual_anoxia_duration_his.index].index.astype(float),
                      glue_df_annual_anoxia_duration_his[1975 < glue_df_annual_anoxia_duration_his.index]['5%'].astype(float) - annual_anoxia_duration_ref,
                      glue_df_annual_anoxia_duration_his[1975 < glue_df_annual_anoxia_duration_his.index ]['95%'].astype(float) - annual_anoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_anoxia_duration_his[(1975 < glue_df_annual_anoxia_duration_his.index) ].index.astype(float),
            glue_df_annual_anoxia_duration_his[(1975 < glue_df_annual_anoxia_duration_his.index)]['50%'].astype(float) - annual_anoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['5%'].astype(float)-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp26['95%'].astype(float)-annual_anoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp26.index.astype(float), glue_df_annual_anoxia_duration_rcp26['50%'].astype(float)-annual_anoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['5%'].astype(float)-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp60['95%'].astype(float)-annual_anoxia_duration_ref, color='b', alpha=0.27 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp60.index.astype(float), glue_df_annual_anoxia_duration_rcp60['50%'].astype(float)-annual_anoxia_duration_ref, 'b', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['5%'].astype(float)-annual_anoxia_duration_ref, glue_df_annual_anoxia_duration_rcp85['95%'].astype(float)-annual_anoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_anoxia_duration_rcp85.index.astype(float), glue_df_annual_anoxia_duration_rcp85['50%'].astype(float)-annual_anoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of anoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_anoxia_duration_Anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


