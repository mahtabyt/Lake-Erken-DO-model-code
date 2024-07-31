# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 04:29:07 2023

@author: mahta
"""

#%% annual hypoxia duration_his

all_annual_hdur_his=pd.DataFrame([])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_his = pd.concat([all_annual_hdur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_his = pd.concat([all_annual_hdur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_his = pd.concat([all_annual_hdur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_his = pd.concat([all_annual_hdur_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_hdur_his

anova_annual_hdur_his=annova_uncertainity(all_annual_hdur_his)

anova_annual_hdur_his.describe().loc['mean', :]
"""
GCMs             71.629075
param            27.282377
interaction       1.088549
GCMs/param        5.336607
year           1933.000000
Name: mean, dtype: float64
"""


anova_annual_hdur_his.describe().loc['std', :]
"""
GCMs           17.815858
param          17.383630
interaction     0.950015
GCMs/param      6.524989
year           42.001984
Name: std, dtype: float64

"""





#%% GLUE method on all_annual_hdur_his 
          

        
#all_annual_hdur_his= all_annual_hdur_his.set_index(all_annual_hdur_his['Datetime'])


# annual hypoxia duration  
timeseries_year_his= all_annual_hdur_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hdur_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_his=glue_df_annual_hypoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_hypoxic_duration_his.csv')
        




#%% annual hypoxia duration_rcp26

all_annual_hdur_rcp26=pd.DataFrame([])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp26 = pd.concat([all_annual_hdur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp26 = pd.concat([all_annual_hdur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp26 = pd.concat([all_annual_hdur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp26 = pd.concat([all_annual_hdur_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_hdur_rcp26

anova_annual_hdur_rcp26=annova_uncertainity(all_annual_hdur_rcp26)

anova_annual_hdur_rcp26.describe().loc['mean', :]
"""
GCMs             68.701710
param            30.395931
interaction       0.902358
GCMs/param        3.697585
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_hdur_rcp26.describe().loc['std', :]
"""
GCMs           18.906199
param          18.434134
interaction     0.805739
GCMs/param      3.432151
year           27.279418
Name: std, dtype: float64
"""
#80 years:
anova_annual_80years_hdur_rcp26=annova_uncertainity(all_annual_hdur_rcp26[all_annual_hdur_rcp26.index>2019])


anova_annual_80years_hdur_rcp26.describe().loc['mean', :]
"""
GCMs             70.132202
param            29.008386
interaction       0.859413
GCMs/param        3.901525
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_hdur_rcp26.describe().loc['std', :]

"""

GCMs           17.723589
param          17.370031
interaction     0.715712
GCMs/param      3.593114
year           23.237900
Name: std, dtype: float64

"""


#%% GLUE method on all_annual_hdur_rcp26 
          

        
#all_annual_hdur_rcp26= all_annual_hdur_rcp26.set_index(all_annual_hdur_rcp26['Datetime'])


# annual hypoxia duration  
timeseries_year_rcp26= all_annual_hdur_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hdur_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_hypoxic_duration_rcp26.csv')
        


#%%%RCP6.0

#%% annual hypoxia duration_rcp60

all_annual_hdur_rcp60=pd.DataFrame([])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp60 = pd.concat([all_annual_hdur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp60 = pd.concat([all_annual_hdur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp60 = pd.concat([all_annual_hdur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp60 = pd.concat([all_annual_hdur_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_hdur_rcp60

anova_annual_hdur_rcp60=annova_uncertainity(all_annual_hdur_rcp60)

anova_annual_hdur_rcp60.describe().loc['mean', :]
"""
GCMs             73.321664
param            25.723127
interaction       0.955209
GCMs/param        5.557851
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_hdur_rcp60.describe().loc['std', :]
"""
GCMs           19.049433
param          18.328722
interaction     1.043564
GCMs/param      6.134211
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_hdur_rcp60=annova_uncertainity(all_annual_hdur_rcp60[all_annual_hdur_rcp60.index>2019])


anova_annual_80years_hdur_rcp60.describe().loc['mean', :]
"""
GCMs             73.368531
param            25.649147
interaction       0.982322
GCMs/param        5.360287
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_hdur_rcp60.describe().loc['std', :]

"""
GCMs           19.490510
param          18.723044
interaction     1.086170
GCMs/param      5.497319
year           23.237900
Name: std, dtype: float64

"""



#%% GLUE method on all_annual_hdur_rcp60 
          

        
#all_annual_hdur_rcp60= all_annual_hdur_rcp60.set_index(all_annual_hdur_rcp60['Datetime'])


# annual hypoxia duration  
timeseries_year_rcp60= all_annual_hdur_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hdur_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_hypoxic_duration_rcp60.csv')
        


#%%RCP8.5


#%% annual hypoxia duration_rcp85

all_annual_hdur_rcp85=pd.DataFrame([])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp85 = pd.concat([all_annual_hdur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp85 = pd.concat([all_annual_hdur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp85 = pd.concat([all_annual_hdur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        all_annual_hdur_rcp85 = pd.concat([all_annual_hdur_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        

#%%Uncertainity partitioning on all_annual_hdur_rcp85

anova_annual_hdur_rcp85=annova_uncertainity(all_annual_hdur_rcp85)

anova_annual_hdur_rcp85.describe().loc['mean', :]
"""
GCMs             82.752718
param            16.498399
interaction       0.748882
GCMs/param        8.759830
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_hdur_rcp85.describe().loc['std', :]
"""
GCMs           13.531400
param          12.895358
interaction     0.840931
GCMs/param      7.054099
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_hdur_rcp85=annova_uncertainity(all_annual_hdur_rcp85[all_annual_hdur_rcp85.index>2019])


anova_annual_80years_hdur_rcp85.describe().loc['mean', :]
"""
GCMs             83.245636
param            15.999441
interaction       0.754923
GCMs/param        9.306850
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_hdur_rcp85.describe().loc['std', :]

"""
GCMs           13.742162
param          13.022495
interaction     0.879187
GCMs/param      7.400782
year           23.237900
Name: std, dtype: float64
"""





#%% GLUE method on all_annual_hdur_rcp85 
          

        
#all_annual_hdur_rcp85= all_annual_hdur_rcp85.set_index(all_annual_hdur_rcp85['Datetime'])


# annual hypoxia duration  
timeseries_year_rcp85= all_annual_hdur_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hdur_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_hypoxic_duration_rcp85.csv')
        






#%%Plot of Anova test on all_annual_hdur_rcps_his


######his_annual_hdur

#years
contributions_annual_hdur_his_years=anova_annual_hdur_his['year']
#GCMs
gcm_contributions_annual_hdur_his= anova_annual_hdur_his['GCMs']
#Param
param_contributions_annual_hdur_his=anova_annual_hdur_his['param']
#interaction
interact_contributions_annual_hdur_his =anova_annual_hdur_his['interaction']



# the whole RCPs years


######rcp26

#years
contributions_annual_hdur_rcp26_years=anova_annual_hdur_rcp26['year']
#GCMs
gcm_contributions_annual_hdur_rcp26 = anova_annual_hdur_rcp26['GCMs']
#Param
param_contributions_annual_hdur_rcp26 =anova_annual_hdur_rcp26['param']
#interaction
interact_contributions_annual_hdur_rcp26 =anova_annual_hdur_rcp26['interaction']

######rcp60

#years
contributions_annual_hdur_rcp60_years=anova_annual_hdur_rcp60['year']
#GCMs
gcm_contributions_annual_hdur_rcp60 = anova_annual_hdur_rcp60['GCMs']
#Param
param_contributions_annual_hdur_rcp60 =anova_annual_hdur_rcp60['param']
#interaction
interact_contributions_annual_hdur_rcp60 =anova_annual_hdur_rcp60['interaction']




######rcp85

#years
contributions_annual_hdur_rcp85_years=anova_annual_hdur_rcp85['year']
#GCMs
gcm_contributions_annual_hdur_rcp85 = anova_annual_hdur_rcp85['GCMs']
#Param
param_contributions_annual_hdur_rcp85 =anova_annual_hdur_rcp85['param']
#interaction
interact_contributions_annual_hdur_rcp85 =anova_annual_hdur_rcp85['interaction']




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
axs[0, 0].fill_between(contributions_annual_hdur_his_years, 0, gcm_contributions_annual_hdur_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_hdur_his_years, gcm_contributions_annual_hdur_his , gcm_contributions_annual_hdur_his + param_contributions_annual_hdur_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_hdur_his_years, gcm_contributions_annual_hdur_his  + param_contributions_annual_hdur_his, gcm_contributions_annual_hdur_his + param_contributions_annual_hdur_his + interact_contributions_annual_hdur_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('His', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(1861, 2005)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)
# Subplot for rcp26
axs[0, 1].fill_between(contributions_annual_hdur_rcp26_years, 0, gcm_contributions_annual_hdur_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_hdur_rcp26_years, gcm_contributions_annual_hdur_rcp26, gcm_contributions_annual_hdur_rcp26 + param_contributions_annual_hdur_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_hdur_rcp26_years, gcm_contributions_annual_hdur_rcp26 + param_contributions_annual_hdur_rcp26, gcm_contributions_annual_hdur_rcp26 + param_contributions_annual_hdur_rcp26 + interact_contributions_annual_hdur_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1, 0].fill_between(contributions_annual_hdur_rcp60_years, 0, gcm_contributions_annual_hdur_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_hdur_rcp60_years, gcm_contributions_annual_hdur_rcp60, gcm_contributions_annual_hdur_rcp60 + param_contributions_annual_hdur_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_hdur_rcp60_years, gcm_contributions_annual_hdur_rcp60 + param_contributions_annual_hdur_rcp60, gcm_contributions_annual_hdur_rcp60 + param_contributions_annual_hdur_rcp60 + interact_contributions_annual_hdur_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 0].set_title('RCP6.0', fontsize=20)
axs[1, 0].set_ylim(0,100)
axs[1, 0].set_xlim(2006, 2099)
axs[1, 0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[1, 1].fill_between(contributions_annual_hdur_rcp85_years, 0, gcm_contributions_annual_hdur_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_hdur_rcp85_years, gcm_contributions_annual_hdur_rcp85, gcm_contributions_annual_hdur_rcp85 + param_contributions_annual_hdur_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 1].fill_between(contributions_annual_hdur_rcp85_years, gcm_contributions_annual_hdur_rcp85 + param_contributions_annual_hdur_rcp85, gcm_contributions_annual_hdur_rcp85 + param_contributions_annual_hdur_rcp85 + interact_contributions_annual_hdur_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1, 1].set_title('RCP8.5', fontsize=20)
axs[1, 1].set_ylim(0,100)
axs[1, 1].set_xlim(2006, 2099)
axs[1, 1].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in annual hypoxia duration [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.75, 0.06), fontsize=22, ncol=3)


# Save the plot
plt.savefig('uncertainty_annual_hypoxia_duration_allyears_rcps_his.png', dpi=300, bbox_inches='tight')

plt.show()




#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_annual_hdur_rcp26_years=anova_annual_hdur_rcp26[anova_annual_hdur_rcp26.year>2019].year
#gcms
gcm_contributions_80years_annual_hdur_rcp26 = anova_annual_hdur_rcp26[anova_annual_hdur_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_annual_hdur_rcp26 =anova_annual_hdur_rcp26[anova_annual_hdur_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_annual_hdur_rcp26 =anova_annual_hdur_rcp26[anova_annual_hdur_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_annual_hdur_rcp60_years=anova_annual_hdur_rcp60[anova_annual_hdur_rcp60.year>2019].year
#gcms
gcm_contributions_80years_annual_hdur_rcp60 = anova_annual_hdur_rcp60[anova_annual_hdur_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_annual_hdur_rcp60 =anova_annual_hdur_rcp60[anova_annual_hdur_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_annual_hdur_rcp60 =anova_annual_hdur_rcp60[anova_annual_hdur_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_annual_hdur_rcp85_years=anova_annual_hdur_rcp85[anova_annual_hdur_rcp85.year>2019].year
#gcms
gcm_contributions_80years_annual_hdur_rcp85 = anova_annual_hdur_rcp85[anova_annual_hdur_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_annual_hdur_rcp85 =anova_annual_hdur_rcp85[anova_annual_hdur_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_annual_hdur_rcp85 =anova_annual_hdur_rcp85[anova_annual_hdur_rcp85.year>2019]['interaction']


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
axs[0].fill_between(contributions_80years_annual_hdur_rcp26_years, 0, gcm_contributions_80years_annual_hdur_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_hdur_rcp26_years, gcm_contributions_80years_annual_hdur_rcp26, gcm_contributions_80years_annual_hdur_rcp26 + param_contributions_80years_annual_hdur_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_hdur_rcp26_years, gcm_contributions_80years_annual_hdur_rcp26 + param_contributions_80years_annual_hdur_rcp26, gcm_contributions_80years_annual_hdur_rcp26 + param_contributions_80years_annual_hdur_rcp26 + interact_contributions_80years_annual_hdur_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_annual_hdur_rcp60_years, 0, gcm_contributions_80years_annual_hdur_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_hdur_rcp60_years, gcm_contributions_80years_annual_hdur_rcp60, gcm_contributions_80years_annual_hdur_rcp60 + param_contributions_80years_annual_hdur_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_hdur_rcp60_years, gcm_contributions_80years_annual_hdur_rcp60 + param_contributions_80years_annual_hdur_rcp60, gcm_contributions_80years_annual_hdur_rcp60 + param_contributions_80years_annual_hdur_rcp60 + interact_contributions_80years_annual_hdur_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_annual_hdur_rcp85_years, 0, gcm_contributions_80years_annual_hdur_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_hdur_rcp85_years, gcm_contributions_80years_annual_hdur_rcp85, gcm_contributions_80years_annual_hdur_rcp85 + param_contributions_80years_annual_hdur_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_hdur_rcp85_years, gcm_contributions_80years_annual_hdur_rcp85 + param_contributions_80years_annual_hdur_rcp85, gcm_contributions_80years_annual_hdur_rcp85 + param_contributions_80years_annual_hdur_rcp85 + interact_contributions_80years_annual_hdur_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in\nannual hypoxia duration [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.65, 0.06), fontsize=22, ncol=3)



# Save the plot
plt.savefig('uncertainty_annual_hypoxia_duration_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()
















































#%%monthly_table_of_hypoxia_duartion

#%%monthly_table_of_hypoxia_duartion_gfdl_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%monthly_table_of_hypoxia_duartion_gfdl_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 

#%%monthly_table_of_hypoxia_duartion_gfdl_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_table_of_hypoxia_duartion_gfdl_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%%monthly_table_of_hypoxia_duartion_hadgem_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 
#%%monthly_table_of_hypoxia_duartion_hadgem_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_hypoxia_duartion_hadgem_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
   
#%%monthly_table_of_hypoxia_duartion_hadgem_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl

#%%monthly_table_of_hypoxia_duartion_ipsl_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_table_of_hypoxia_duartion_ipsl_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_hypoxia_duartion_ipsl_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%%monthly_table_of_hypoxia_duartion_ipsl_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
#%%monthly_table_of_hypoxia_duartion_miroc_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
 
#%%monthly_table_of_hypoxia_duartion_miroc_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_table_of_hypoxia_duartion_miroc_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%%monthly_table_of_hypoxia_duartion_miroc_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%sorting the indexs_annual_hypoxia_duration 

glue_df_annual_hypoxia_duration_his= glue_df_annual_hypoxia_duration_his.sort_index()
glue_df_annual_hypoxia_duration_rcp26= glue_df_annual_hypoxia_duration_rcp26.sort_index()
glue_df_annual_hypoxia_duration_rcp60= glue_df_annual_hypoxia_duration_rcp60.sort_index()
glue_df_annual_hypoxia_duration_rcp85= glue_df_annual_hypoxia_duration_rcp85.sort_index()














#%%Plotting and analyses 



#%%########annual hypoxia duration 


#%%ploting annual hypoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['5%'], glue_df_annual_hypoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['5%'], glue_df_annual_hypoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['5%'], glue_df_annual_hypoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['5%'], glue_df_annual_hypoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Annual hypoxia duration [d year $^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)#)   
fig.savefig("GLUE_Timeseries_annual_hypoxia_duration.png",  dpi=300, bbox_inches='tight')



#%%

#differences betwen hypoxia duration and anoxia duartion is about 7 days 

#%%
np.mean(glue_df_annual_hypoxia_duration_his['50%'])#44.35975344945829
np.mean(glue_df_annual_hypoxia_duration_rcp26['50%'])#58.53537155343995
np.mean(glue_df_annual_hypoxia_duration_rcp60['50%'])#62.7700914040588
np.mean(glue_df_annual_hypoxia_duration_rcp85['50%'])#66.97532944047045

#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_annual_hypoxia_duration_his=glue_df_annual_hypoxia_duration_his[1975 < glue_df_annual_hypoxia_duration_his.index]['50%']
annual_hypoxia_duration_ref=np.mean(glue_base_annual_hypoxia_duration_his)
#46.32979124213759


#near future [2030-2059]

glue_near_future_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26[(2029 < glue_df_annual_hypoxia_duration_rcp26.index) & (glue_df_annual_hypoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypoxia_duration_rcp26)
#59.08965611136435
glue_near_future_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60[(2029 < glue_df_annual_hypoxia_duration_rcp60.index) & (glue_df_annual_hypoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypoxia_duration_rcp60)
# 59.253934301739335
glue_near_future_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85[(2029 < glue_df_annual_hypoxia_duration_rcp85.index) & (glue_df_annual_hypoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypoxia_duration_rcp85)
# 62.82651023129089

 
#Distant future [2070-2099]

glue_distant_future_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26[(2069 < glue_df_annual_hypoxia_duration_rcp26.index) & (glue_df_annual_hypoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypoxia_duration_rcp26)
#59.75560662737457
glue_distant_future_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60[(2069 < glue_df_annual_hypoxia_duration_rcp60.index) & (glue_df_annual_hypoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_hypoxia_duration_rcp60)
#71.32403782702637
glue_distant_future_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85[(2069 < glue_df_annual_hypoxia_duration_rcp85.index) & (glue_df_annual_hypoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypoxia_duration_rcp85)
#80.47546466743418
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_hypoxia_duration_his)
(0.04292612358029116,
 'positively autocorrelated',
 'increasing',
 0.010604342608411255,
 0.3333333333333333,
 41.72938061105683)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypoxia_duration_rcp26)
(0.01655491069329564,
 'positively autocorrelated',
 'no trend',
 0.1378830110332092,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypoxia_duration_rcp60)
(0.007739794736168487,
 'positively autocorrelated',
 'increasing',
 0.001133841233766697,
 0.36,
 53.78)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypoxia_duration_rcp85)
(0.014214069149027566,
 'positively autocorrelated',
 'increasing',
 0.0031628336945630497,
 0.41022365844011816,
 56.551756952618284)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypoxia_duration_rcp26)
(0.014687962585561666,
 'positively autocorrelated',
 'no trend',
 0.2302867280170715,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypoxia_duration_rcp60)
(0.010195029863748884,
 'positively autocorrelated',
 'no trend',
 0.3807626767196113,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypoxia_duration_rcp85)
(0.012260374655715897,
 'positively autocorrelated',
 'increasing',
 0.01442793828522837,
 0.4268385938213249,
 75.8108403895908)




#%% 80 years from 2020 for annual_hypoxia_duration


glue_80years_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26[2019 < glue_df_annual_hypoxia_duration_rcp26.index]

glue_80years_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60[2019 < glue_df_annual_hypoxia_duration_rcp60.index]

glue_80years_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85[2019 < glue_df_annual_hypoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypoxia_duration_rcp26[glue_80years_annual_hypoxia_duration_rcp26.index<2030]['50%'])
57.21206483671531

#rcp6.0
np.mean(glue_80years_annual_hypoxia_duration_rcp60[glue_80years_annual_hypoxia_duration_rcp60.index<2030]['50%'])
57.75125823397521

#rcp8.5
np.mean(glue_80years_annual_hypoxia_duration_rcp85[glue_80years_annual_hypoxia_duration_rcp85.index<2030]['50%'])
57.45647010721878

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypoxia_duration_rcp26[glue_80years_annual_hypoxia_duration_rcp26.index>2079]['50%'])
60.25806676572004

#rcp6.0
np.mean(glue_80years_annual_hypoxia_duration_rcp60[glue_80years_annual_hypoxia_duration_rcp60.index>2079]['50%'])
72.02707706269837

#rcp8.5
np.mean(glue_80years_annual_hypoxia_duration_rcp85[glue_80years_annual_hypoxia_duration_rcp85.index>2079]['50%'])
81.71319700115126

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp26['50%'])
(0.01853263099128573,
 'positively autocorrelated',
 'no trend',
 0.0952173401599774,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp60['50%'])
(0.00998885108307725,
 'positively autocorrelated',
 'increasing',
 4.907185768843192e-14,
 0.25806451612903225,
 52.806451612903224)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp85['50%'])
(0.01369461628867701,
 'positively autocorrelated',
 'increasing',
 1.4144241333724494e-13,
 0.41523947750362844,
 52.598040638606676)




#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_his['50%'])
(0.05064191212235622,
 'positively autocorrelated',
 'no trend',
 0.17768042143094953,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp26['50%'])
(0.019629686451140698,
 'positively autocorrelated',
 'increasing',
 0.005482501592342981,
 0.06884971804899856,
 54.98962090381836)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp60['50%'])
(0.018449842285520147,
 'positively autocorrelated',
 'increasing',
 0.0016710815479368257,
 0.06735155585618892,
 54.868152652687215)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp85['50%'])
(0.01480074097241337,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.4090909090909091,
 46.97727272727273)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%hypoxic_duration_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index)].index.astype(float),
                      glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index)]['5%'] - annual_hypoxia_duration_ref,
                      glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index) ]['95%'] - annual_hypoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index) ].index.astype(float),
            glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index)]['50%'] - annual_hypoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['5%']-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp26['95%']-annual_hypoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['50%']-annual_hypoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['5%']-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp60['95%']-annual_hypoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['50%']-annual_hypoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['5%']-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp85['95%']-annual_hypoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['50%']-annual_hypoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of annual hypoxia duration [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_annual_hypoxia_duration_anomaly.png",  dpi=300, bbox_inches='tight')


#%%80 years plotting 


os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_annual_hypoxia_duration_rcp26.index.astype(float), glue_80years_annual_hypoxia_duration_rcp26['5%'], glue_80years_annual_hypoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_annual_hypoxia_duration_rcp26.index.astype(float), glue_80years_annual_hypoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
ax=plt.plot([2020, 2021] , [14, 14], color='white' , label=' ')

ax=plt.fill_between(glue_80years_annual_hypoxia_duration_rcp60.index.astype(float), glue_80years_annual_hypoxia_duration_rcp60['5%'], glue_80years_annual_hypoxia_duration_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_annual_hypoxia_duration_rcp60.index.astype(float), glue_80years_annual_hypoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp60['50%'])
ax=plt.text(2020, 15, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f},  p-value <0.0001', color='orange', fontsize= 20 )

ax=plt.plot(glue_80years_annual_anoxia_duration_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='orange', alpha=0.9, linewidth=3 , label='RCP6.0 trendline')



ax=plt.fill_between(glue_80years_annual_hypoxia_duration_rcp85.index.astype(float), glue_80years_annual_hypoxia_duration_rcp85['5%'], glue_80years_annual_hypoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_annual_hypoxia_duration_rcp85.index.astype(float), glue_80years_annual_hypoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp85['50%'])
ax=plt.text(2020, 10, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},   p-value <0.0001', color='r', fontsize= 20 )

ax=plt.plot(glue_80years_annual_anoxia_duration_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3  , label='RCP8.5 trendline')



ax=plt.ylabel('Annual hypoxia duration [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.2), fontsize=22, ncol=3)#)   
fig.savefig("GLUE_Timeseries_80years_annual_hypoxia_duration_trendline.png",  dpi=300, bbox_inches='tight')




#%%Anlyses on the RCP2.6 with constant inital condition as 12.298 mg/L

#annual hdur
#gfdl

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_initialcond_attribution"

all_annual_hdur_rcp26_test= pd.DataFrame([])
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
        result_annual =annual_hypoxia_duration (C, time_series, Vr , threshold=2)

        all_annual_hdur_rcp26_test = pd.concat([all_annual_hdur_rcp26_test , result_annual], axis=1)

        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_hdur_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
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
        result_annual =annual_hypoxia_duration (C, time_series, Vr , threshold=2)

        
        all_annual_hdur_rcp26_test = pd.concat([all_annual_hdur_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_hdur_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
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
        result_annual =annual_hypoxia_duration (C, time_series, Vr , threshold=2)
   
        
        all_annual_hdur_rcp26_test = pd.concat([all_annual_hdur_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_hdur_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
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
        result_annual =annual_hypoxia_duration (C, time_series, Vr , threshold=2)
 
        
        all_annual_hdur_rcp26_test = pd.concat([all_annual_hdur_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_hdur_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        

#%% GLUE of testing rcp26 scenarios for annual
all_annual_hdur_rcp26_test

all_annual_hdur_rcp26



diff_base_test_annual_hdur_rcp26= pd.DataFrame(np.array(all_annual_hdur_rcp26)-np.array(all_annual_hdur_rcp26_test))



all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_hdur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_annual_hdur_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_annual_hdur_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_annual_hdur_rcp26=glue_diff_base_test_annual_hdur_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_annual_hdur_rcp26=glue_diff_base_test_annual_hdur_rcp26.sort_index()
glue_diff_base_test_annual_hdur_rcp26_80years=glue_diff_base_test_annual_hdur_rcp26[glue_diff_base_test_annual_hdur_rcp26.index>2019]



#%% analysing the difference of baseline scenarios and test with fixed inital condition 

#%%annual hdur

#decreaseing trend testing the initial condition effect 
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_hdur_rcp26_80years['50%'])
(2.1390576660858924,
 'negetively autocorrelated',
 'decreasing',
 0.007633874866402435,
 -0.010638297872340332,
 -0.07635548062451342)




#%%
all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_hdur_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hdur_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_annual_hdur_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_annual_hdur_rcp26_test=glue_annual_hdur_rcp26_test.set_index(timeseries_year_rcp26)    
glue_annual_hdur_rcp26_test=glue_annual_hdur_rcp26_test.sort_index()
glue_annual_hdur_rcp26_test_80years=glue_annual_hdur_rcp26_test[glue_annual_hdur_rcp26_test.index>2019]



#%% is there any trendline over 80 years in RCP26 test scenario?
"""
Yes for annual hdur 
"""

#%% annual hdur
# effect of increasement in length of stratification is obvious 
autocorr_MK_org_modif_sens_slope_test(glue_annual_hdur_rcp26_test_80years['50%'])
(0.020342339835026535,
 'positively autocorrelated',
 'increasing',
 0.01932503016647824,
 0.06063280514209179,
 56.60500419688737)

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_annual_hdur_rcp26_test_80years.index.astype(float), glue_annual_hdur_rcp26_test_80years['5%'], glue_annual_hdur_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_annual_hdur_rcp26_test_80years.index.astype(float), glue_annual_hdur_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )


trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_annual_hdur_rcp26_test_80years['50%'])
ax=plt.text(2020, 20, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_annual_hdur_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Annual hypoxia duration of  RCP2.6\n with fixed inital condition [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22 , ncol= 2)#)   
fig.savefig("test_initalcondition_fixed_annual_hdur_80years_rcp26.png",  dpi=300, bbox_inches='tight')


#%%for paper both plot of diff and test of Apr_Oct rcp26 in one plot 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Create figure and axes for subplots
fig, axs = plt.subplots(1, 2, figsize=(25, 10))

# Plot for the first subplot
ax = axs[1]
ax.fill_between(glue_diff_base_test_annual_hdur_rcp26_80years.index,
                glue_diff_base_test_annual_hdur_rcp26_80years['5%'],
                glue_diff_base_test_annual_hdur_rcp26_80years['95%'],
                color='green', alpha=0.2, label='90% CI')
ax.plot(glue_diff_base_test_annual_hdur_rcp26_80years.index,
        glue_diff_base_test_annual_hdur_rcp26_80years['50%'],
        'green', label='Median', alpha=0.9, linewidth=3)

# Add trendline
trendline_rcp26_1 = autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_hdur_rcp26_80years['50%'])
#ax.text(0.95, 0.95, '(b)', transform=ax.transAxes, fontsize=22,
#        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 4, f'y = {trendline_rcp26_1[-2]:.3f}x + {trendline_rcp26_1[-1]:.3f}, p-value = {trendline_rcp26_1[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_diff_base_test_annual_hdur_rcp26_80years.index.astype(float),
        trendline_rcp26_1[-2] * np.arange(80) + trendline_rcp26_1[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3, label= 'Trendline')

# Set labels for the first subplot
ax.set_ylabel('Annual anoxia duration of RCP2.6 \n difference between fixed initial condition \n and original scenario in deep part  [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_diff_base_test_annual_hdur_rcp26_80years.index)
ax.set_xticklabels(glue_diff_base_test_annual_hdur_rcp26_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Plot for the second subplot
ax = axs[0]
ax.fill_between(glue_annual_hdur_rcp26_test_80years.index,
                glue_annual_hdur_rcp26_test_80years['5%'],
                glue_annual_hdur_rcp26_test_80years['95%'],
                color='green', alpha=0.2)#, label='90% CI')
ax.plot(glue_annual_hdur_rcp26_test_80years.index,
        glue_annual_hdur_rcp26_test_80years['50%'].astype(float),
        'green', alpha=0.9, linewidth=3)# label='Median',

# Add trendline
trendline_rcp26_0 = autocorr_MK_org_modif_sens_slope_test(glue_annual_hdur_rcp26_test_80years['50%'])
#ax.text(0.95, 0.95, '(a)', transform=ax.transAxes, fontsize=22,
#        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 80, f'y = {trendline_rcp26_0[-2]:.3f}x + {trendline_rcp26_0[-1]:.3f}, p-value = {trendline_rcp26_0[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_annual_hdur_rcp26_test_80years.index,
        trendline_rcp26_0[-2] * np.arange(80) + trendline_rcp26_0[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)

# Set labels for the second subplot
ax.set_ylabel('Annual hypoxia duration of RCP2.6 with\n fixed initial condition in deep part [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_annual_hdur_rcp26_test_80years.index)
ax.set_xticklabels(glue_annual_hdur_rcp26_test_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Add a single legend for both subplots in the center bottom
#fig.legend(loc='lower center', fontsize=22, ncol=3)
fig.legend(loc='lower center', fontsize=22, ncol=3, bbox_to_anchor=(0.5, -0.05))
plt.tight_layout()


plt.savefig("atttest_difference_test_initalcondition_fixed_annual_hdur_80years_rcp26.png",  dpi=300, bbox_inches='tight')    
    
     
    
    
    

#%%%%%%%%======================
#============OLD
#############
#%% Annual hypoxia duration_gfdl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                

#%% May_Sep hypoxia duration_gfdl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_gfdl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_gfdl_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_gfdl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
#%% May_Sep hypoxia duration_gfdl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_gfdl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                


                


#%%monthly_table_of_hypoxia_duartion_gfdl_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_gfdl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_gfdl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_gfdl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                










#%%monthly_table_of_hypoxia_duartion_gfdl_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_gfdl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_gfdl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_gfdl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_gfdl_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%% Annual hypoxia duration_hadgem_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                

#%% May_Sep hypoxia duration_hadgem_his
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_hadgem_his
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_hadgem_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_hadgem_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
#%% May_Sep hypoxia duration_hadgem_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_hadgem_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                


                


#%%monthly_table_of_hypoxia_duartion_hadgem_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_hadgem_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_hadgem_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_hadgem_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                










#%%monthly_table_of_hypoxia_duartion_hadgem_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_hadgem_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_hadgem_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_hadgem_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_hadgem_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl
#%% Annual hypoxia duration_ipsl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                

#%% May_Sep hypoxia duration_ipsl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_ipsl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_ipsl_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_ipsl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
#%% May_Sep hypoxia duration_ipsl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_ipsl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                


                


#%%monthly_table_of_hypoxia_duartion_ipsl_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_ipsl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_ipsl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_ipsl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                










#%%monthly_table_of_hypoxia_duartion_ipsl_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_ipsl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_ipsl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_ipsl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_ipsl_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%miroc 
#%% Annual hypoxia duration_miroc_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                

#%% May_Sep hypoxia duration_miroc_his
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_miroc_his
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_miroc_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_miroc_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
#%% May_Sep hypoxia duration_miroc_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_miroc_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                


                


#%%monthly_table_of_hypoxia_duartion_miroc_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_miroc_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_miroc_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_miroc_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                










#%%monthly_table_of_hypoxia_duartion_miroc_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_miroc_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                
#%% May_Sep hypoxia duration_miroc_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = May_Sep_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Sep_hypoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Sep_hypoxia_duration'])
        
                
#%% summer hypoxia duration_miroc_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = summer_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypoxia_duration'])
        
                




#%%monthly_table_of_hypoxia_duartion_miroc_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_hypoxia_duartion(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_hypoxia_duartion_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his_annual_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_annual_hypoxia_duration_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_his = pd.concat([all_annual_hypoxia_duration_his , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_his = pd.concat([all_annual_hypoxia_duration_his , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_his = pd.concat([all_annual_hypoxia_duration_his , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_his = pd.concat([all_annual_hypoxia_duration_his , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        
all_annual_hypoxia_duration_his= all_annual_hypoxia_duration_his.set_index(annual_hypoxia_duration['year'])


# annual hypoxia duration  
timeseries_year_his= all_annual_hypoxia_duration_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_his=glue_df_annual_hypoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_hypoxic_duration_his.csv')


#%%rcp26_annual_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_annual_hypoxia_duration_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp26 = pd.concat([all_annual_hypoxia_duration_rcp26 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp26 = pd.concat([all_annual_hypoxia_duration_rcp26 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp26 = pd.concat([all_annual_hypoxia_duration_rcp26 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp26 = pd.concat([all_annual_hypoxia_duration_rcp26 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        

all_annual_hypoxia_duration_rcp26= all_annual_hypoxia_duration_rcp26.set_index(annual_hypoxia_duration['year'])

# annual hypoxia duration  
timeseries_year_rcp26= all_annual_hypoxia_duration_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_hypoxic_duration_rcp26.csv')


#%%rcp60_annual_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_annual_hypoxia_duration_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp60 = pd.concat([all_annual_hypoxia_duration_rcp60 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp60 = pd.concat([all_annual_hypoxia_duration_rcp60 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp60 = pd.concat([all_annual_hypoxia_duration_rcp60 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp60 = pd.concat([all_annual_hypoxia_duration_rcp60 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        

all_annual_hypoxia_duration_rcp60= all_annual_hypoxia_duration_rcp60.set_index(annual_hypoxia_duration['year'])

# annual hypoxia duration  
timeseries_year_rcp60= all_annual_hypoxia_duration_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_hypoxic_duration_rcp60.csv')

#%%rcp85_annual_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_annual_hypoxia_duration_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp85 = pd.concat([all_annual_hypoxia_duration_rcp85 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp85 = pd.concat([all_annual_hypoxia_duration_rcp85 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp85 = pd.concat([all_annual_hypoxia_duration_rcp85 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration.index)
        
        all_annual_hypoxia_duration_rcp85 = pd.concat([all_annual_hypoxia_duration_rcp85 , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        
all_annual_hypoxia_duration_rcp85= all_annual_hypoxia_duration_rcp85.set_index(annual_hypoxia_duration['year'])


# annual hypoxia duration  
timeseries_year_rcp85= all_annual_hypoxia_duration_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_hypoxic_duration_rcp85.csv')




#%%sorting the indexs_annual_hypoxia_duration 

glue_df_annual_hypoxia_duration_his= glue_df_annual_hypoxia_duration_his.sort_index()
glue_df_annual_hypoxia_duration_rcp26= glue_df_annual_hypoxia_duration_rcp26.sort_index()
glue_df_annual_hypoxia_duration_rcp60= glue_df_annual_hypoxia_duration_rcp60.sort_index()
glue_df_annual_hypoxia_duration_rcp85= glue_df_annual_hypoxia_duration_rcp85.sort_index()


#%% May_Sep hypoxia duration
#%%his_May_Sep_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_May_Sep_hypoxia_duration_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_his = pd.concat([all_May_Sep_hypoxia_duration_his , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_his = pd.concat([all_May_Sep_hypoxia_duration_his , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_his = pd.concat([all_May_Sep_hypoxia_duration_his , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_his = pd.concat([all_May_Sep_hypoxia_duration_his , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        
        
all_May_Sep_hypoxia_duration_his= all_May_Sep_hypoxia_duration_his.set_index(May_Sep_hypoxia_duration['year'])


# May_Sep hypoxia duration  
timeseries_year_his= all_May_Sep_hypoxia_duration_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_hypoxia_duration_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_hypoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_hypoxia_duration_his=glue_df_May_Sep_hypoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_hypoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_hypoxic_duration_his.csv')


#%%rcp26_May_Sep_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_May_Sep_hypoxia_duration_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp26 = pd.concat([all_May_Sep_hypoxia_duration_rcp26 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp26 = pd.concat([all_May_Sep_hypoxia_duration_rcp26 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp26 = pd.concat([all_May_Sep_hypoxia_duration_rcp26 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp26 = pd.concat([all_May_Sep_hypoxia_duration_rcp26 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        
        

all_May_Sep_hypoxia_duration_rcp26= all_May_Sep_hypoxia_duration_rcp26.set_index(May_Sep_hypoxia_duration['year'])

# May_Sep hypoxia duration  
timeseries_year_rcp26= all_May_Sep_hypoxia_duration_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_hypoxia_duration_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_hypoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_hypoxia_duration_rcp26=glue_df_May_Sep_hypoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_hypoxic_duration_rcp26.csv')


#%%rcp60_May_Sep_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_May_Sep_hypoxia_duration_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp60 = pd.concat([all_May_Sep_hypoxia_duration_rcp60 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp60 = pd.concat([all_May_Sep_hypoxia_duration_rcp60 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp60 = pd.concat([all_May_Sep_hypoxia_duration_rcp60 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp60 = pd.concat([all_May_Sep_hypoxia_duration_rcp60 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        
        

all_May_Sep_hypoxia_duration_rcp60= all_May_Sep_hypoxia_duration_rcp60.set_index(May_Sep_hypoxia_duration['year'])

# May_Sep hypoxia duration  
timeseries_year_rcp60= all_May_Sep_hypoxia_duration_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_hypoxia_duration_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_hypoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_hypoxia_duration_rcp60=glue_df_May_Sep_hypoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_hypoxic_duration_rcp60.csv')

#%%rcp85_May_Sep_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_May_Sep_hypoxia_duration_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp85 = pd.concat([all_May_Sep_hypoxia_duration_rcp85 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp85 = pd.concat([all_May_Sep_hypoxia_duration_rcp85 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp85 = pd.concat([all_May_Sep_hypoxia_duration_rcp85 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Sep_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Sep_hypoxia_duration=May_Sep_hypoxia_duration.set_index(May_Sep_hypoxia_duration.index)
        
        all_May_Sep_hypoxia_duration_rcp85 = pd.concat([all_May_Sep_hypoxia_duration_rcp85 , May_Sep_hypoxia_duration['May_Sep_hypoxia_duration']], axis=1)
        
        
        
        
all_May_Sep_hypoxia_duration_rcp85= all_May_Sep_hypoxia_duration_rcp85.set_index(May_Sep_hypoxia_duration['year'])


# May_Sep hypoxia duration  
timeseries_year_rcp85= all_May_Sep_hypoxia_duration_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Sep_hypoxia_duration_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Sep_hypoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Sep_hypoxia_duration_rcp85=glue_df_May_Sep_hypoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Sep_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_hypoxic_duration_rcp85.csv')



#%%sorting the indexs_May_Sep_hypoxia_duration 

glue_df_May_Sep_hypoxia_duration_his= glue_df_May_Sep_hypoxia_duration_his.sort_index()
glue_df_May_Sep_hypoxia_duration_rcp26= glue_df_May_Sep_hypoxia_duration_rcp26.sort_index()
glue_df_May_Sep_hypoxia_duration_rcp60= glue_df_May_Sep_hypoxia_duration_rcp60.sort_index()
glue_df_May_Sep_hypoxia_duration_rcp85= glue_df_May_Sep_hypoxia_duration_rcp85.sort_index()



#%%===== summer hypoxia duration Glue dataframe 

#%%his_summer_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_summer_hypoxia_duration_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_his = pd.concat([all_summer_hypoxia_duration_his , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_his = pd.concat([all_summer_hypoxia_duration_his , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_his = pd.concat([all_summer_hypoxia_duration_his , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_his = pd.concat([all_summer_hypoxia_duration_his , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        
        
all_summer_hypoxia_duration_his= all_summer_hypoxia_duration_his.set_index(summer_hypoxia_duration['year'])


# summer hypoxia duration  
timeseries_year_his= all_summer_hypoxia_duration_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypoxia_duration_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypoxia_duration_his=glue_df_summer_hypoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_hypoxic_duration_his.csv')


#%%rcp26_summer_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_summer_hypoxia_duration_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp26 = pd.concat([all_summer_hypoxia_duration_rcp26 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp26 = pd.concat([all_summer_hypoxia_duration_rcp26 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp26 = pd.concat([all_summer_hypoxia_duration_rcp26 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp26 = pd.concat([all_summer_hypoxia_duration_rcp26 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        
        

all_summer_hypoxia_duration_rcp26= all_summer_hypoxia_duration_rcp26.set_index(summer_hypoxia_duration['year'])

# summer hypoxia duration  
timeseries_year_rcp26= all_summer_hypoxia_duration_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypoxia_duration_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypoxia_duration_rcp26=glue_df_summer_hypoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_hypoxic_duration_rcp26.csv')


#%%rcp60_summer_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_summer_hypoxia_duration_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp60 = pd.concat([all_summer_hypoxia_duration_rcp60 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp60 = pd.concat([all_summer_hypoxia_duration_rcp60 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp60 = pd.concat([all_summer_hypoxia_duration_rcp60 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp60 = pd.concat([all_summer_hypoxia_duration_rcp60 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        
        

all_summer_hypoxia_duration_rcp60= all_summer_hypoxia_duration_rcp60.set_index(summer_hypoxia_duration['year'])

# summer hypoxia duration  
timeseries_year_rcp60= all_summer_hypoxia_duration_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypoxia_duration_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypoxia_duration_rcp60=glue_df_summer_hypoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_hypoxic_duration_rcp60.csv')

#%%rcp85_summer_hypoxia_duration


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_summer_hypoxia_duration_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp85 = pd.concat([all_summer_hypoxia_duration_rcp85 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp85 = pd.concat([all_summer_hypoxia_duration_rcp85 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp85 = pd.concat([all_summer_hypoxia_duration_rcp85 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypoxia_duration=summer_hypoxia_duration.set_index(summer_hypoxia_duration.index)
        
        all_summer_hypoxia_duration_rcp85 = pd.concat([all_summer_hypoxia_duration_rcp85 , summer_hypoxia_duration['summer_hypoxia_duration']], axis=1)
        
        
        
        
all_summer_hypoxia_duration_rcp85= all_summer_hypoxia_duration_rcp85.set_index(summer_hypoxia_duration['year'])


# summer hypoxia duration  
timeseries_year_rcp85= all_summer_hypoxia_duration_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypoxia_duration_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypoxia_duration_rcp85=glue_df_summer_hypoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_hypoxic_duration_rcp85.csv')


#%%sorting the indexs_summer_hypoxia_duration 

glue_df_summer_hypoxia_duration_his= glue_df_summer_hypoxia_duration_his.sort_index()
glue_df_summer_hypoxia_duration_rcp26= glue_df_summer_hypoxia_duration_rcp26.sort_index()
glue_df_summer_hypoxia_duration_rcp60= glue_df_summer_hypoxia_duration_rcp60.sort_index()
glue_df_summer_hypoxia_duration_rcp85= glue_df_summer_hypoxia_duration_rcp85.sort_index()













#%%Plotting and analyses 



#%%########annual hypoxia duration 

#%%ploting annual hypoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['5%'], glue_df_annual_hypoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['5%'], glue_df_annual_hypoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['5%'], glue_df_annual_hypoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['5%'], glue_df_annual_hypoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypoxia duration per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_annual_hypoxia_duration.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_hypoxia_duration_his['50%'])#6.077082662821386
np.mean(glue_df_annual_hypoxia_duration_rcp26['50%'])#7.992767795524755
np.mean(glue_df_annual_hypoxia_duration_rcp60['50%'])#8.585258963812871
np.mean(glue_df_annual_hypoxia_duration_rcp85['50%'])#9.156680524881311

#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_annual_hypoxia_duration_his=glue_df_annual_hypoxia_duration_his[1975 < glue_df_annual_hypoxia_duration_his.index]['50%']
annual_hypoxia_duration_ref=np.mean(glue_base_annual_hypoxia_duration_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26[(2029 < glue_df_annual_hypoxia_duration_rcp26.index) & (glue_df_annual_hypoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypoxia_duration_rcp26)
# 8.070525139552648
glue_near_future_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60[(2029 < glue_df_annual_hypoxia_duration_rcp60.index) & (glue_df_annual_hypoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypoxia_duration_rcp60)
# 8.107889314159742
glue_near_future_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85[(2029 < glue_df_annual_hypoxia_duration_rcp85.index) & (glue_df_annual_hypoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypoxia_duration_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26[(2069 < glue_df_annual_hypoxia_duration_rcp26.index) & (glue_df_annual_hypoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypoxia_duration_rcp26)
#8.153608896799094
glue_distant_future_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60[(2069 < glue_df_annual_hypoxia_duration_rcp60.index) & (glue_df_annual_hypoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_hypoxia_duration_rcp60)
#9.787975473676404
glue_distant_future_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85[(2069 < glue_df_annual_hypoxia_duration_rcp85.index) & (glue_df_annual_hypoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypoxia_duration_rcp85)
#10.985644903398574
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_hypoxia_duration_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypoxia_duration_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypoxia_duration_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypoxia_duration_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypoxia_duration_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypoxia_duration_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypoxia_duration_rcp85)
(0.014499198182054042,
 'positively autocorrelated',
 'increasing',
 0.026946782463489027,
 0.05377923636923881,
 10.323144222989352)






#%% 80 years from 2020 for annual_hypoxia_duration


glue_80years_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26[2019 < glue_df_annual_hypoxia_duration_rcp26.index]

glue_80years_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60[2019 < glue_df_annual_hypoxia_duration_rcp60.index]

glue_80years_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85[2019 < glue_df_annual_hypoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypoxia_duration_rcp26[glue_80years_annual_hypoxia_duration_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_annual_hypoxia_duration_rcp60[glue_80years_annual_hypoxia_duration_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_annual_hypoxia_duration_rcp85[glue_80years_annual_hypoxia_duration_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypoxia_duration_rcp26[glue_80years_annual_hypoxia_duration_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_annual_hypoxia_duration_rcp60[glue_80years_annual_hypoxia_duration_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_annual_hypoxia_duration_rcp85[glue_80years_annual_hypoxia_duration_rcp85.index>2079]['50%'])
11.160292464667199

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)



autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypoxia_duration_rcp85['50%'])
(0.015711631920486826,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05742827331247126,
 7.128166722990812)





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp85['50%'])
(0.01670964657273115,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05615663487366421,
 6.386209763383056)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%hypoxic_duration_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index)].index.astype(float),
                      glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index)]['5%'] - annual_hypoxia_duration_ref,
                      glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index) ]['95%'] - annual_hypoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index) ].index.astype(float),
            glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index)]['50%'] - annual_hypoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['5%']-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp26['95%']-annual_hypoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['50%']-annual_hypoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['5%']-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp60['95%']-annual_hypoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['50%']-annual_hypoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['5%']-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp85['95%']-annual_hypoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['50%']-annual_hypoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of annual hypoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_annual_hypoxia_duration_anomaly.png",  dpi=300, bbox_inches='tight')











#%%===========May-Sep average of hypoxic afctor 


#%%ploting May_Sep hypoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_his.index.astype(float), glue_df_May_Sep_hypoxia_duration_his['5%'], glue_df_May_Sep_hypoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_May_Sep_hypoxia_duration_his.index.astype(float), glue_df_May_Sep_hypoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp26['5%'], glue_df_May_Sep_hypoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_May_Sep_hypoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp60['5%'], glue_df_May_Sep_hypoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Sep_hypoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp85['5%'], glue_df_May_Sep_hypoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Sep_hypoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypoxia duration May-Sep [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_May_Sep_hypoxia_duration.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_May_Sep_hypoxia_duration_his['50%'])#6.077082662821386
np.mean(glue_df_May_Sep_hypoxia_duration_rcp26['50%'])#7.992767795524755
np.mean(glue_df_May_Sep_hypoxia_duration_rcp60['50%'])#8.585258963812871
np.mean(glue_df_May_Sep_hypoxia_duration_rcp85['50%'])#9.149586881905822

#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_May_Sep_hypoxia_duration_his=glue_df_May_Sep_hypoxia_duration_his[1975 < glue_df_May_Sep_hypoxia_duration_his.index]['50%']
May_Sep_hypoxia_duration_ref=np.mean(glue_base_May_Sep_hypoxia_duration_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_May_Sep_hypoxia_duration_rcp26=glue_df_May_Sep_hypoxia_duration_rcp26[(2029 < glue_df_May_Sep_hypoxia_duration_rcp26.index) & (glue_df_May_Sep_hypoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_May_Sep_hypoxia_duration_rcp26)
# 8.070525139552648
glue_near_future_May_Sep_hypoxia_duration_rcp60=glue_df_May_Sep_hypoxia_duration_rcp60[(2029 < glue_df_May_Sep_hypoxia_duration_rcp60.index) & (glue_df_May_Sep_hypoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_May_Sep_hypoxia_duration_rcp60)
# 8.107889314159742
glue_near_future_May_Sep_hypoxia_duration_rcp85=glue_df_May_Sep_hypoxia_duration_rcp85[(2029 < glue_df_May_Sep_hypoxia_duration_rcp85.index) & (glue_df_May_Sep_hypoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_May_Sep_hypoxia_duration_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_May_Sep_hypoxia_duration_rcp26=glue_df_May_Sep_hypoxia_duration_rcp26[(2069 < glue_df_May_Sep_hypoxia_duration_rcp26.index) & (glue_df_May_Sep_hypoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_May_Sep_hypoxia_duration_rcp26)
#8.153608896799094
glue_distant_future_May_Sep_hypoxia_duration_rcp60=glue_df_May_Sep_hypoxia_duration_rcp60[(2069 < glue_df_May_Sep_hypoxia_duration_rcp60.index) & (glue_df_May_Sep_hypoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_May_Sep_hypoxia_duration_rcp60)
#9.787975473676404
glue_distant_future_May_Sep_hypoxia_duration_rcp85=glue_df_May_Sep_hypoxia_duration_rcp85[(2069 < glue_df_May_Sep_hypoxia_duration_rcp85.index) & (glue_df_May_Sep_hypoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_May_Sep_hypoxia_duration_rcp85)
#10.963418155408705
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_May_Sep_hypoxia_duration_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Sep_hypoxia_duration_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Sep_hypoxia_duration_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Sep_hypoxia_duration_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Sep_hypoxia_duration_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Sep_hypoxia_duration_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Sep_hypoxia_duration_rcp85)
(0.014377923696788013,
 'positively autocorrelated',
 'increasing',
 0.0322801899241516,
 0.04781875151369361,
 10.409571253394757)






#%% 80 years from 2020 for May_Sep_hypoxia_duration


glue_80years_May_Sep_hypoxia_duration_rcp26=glue_df_May_Sep_hypoxia_duration_rcp26[2019 < glue_df_May_Sep_hypoxia_duration_rcp26.index]

glue_80years_May_Sep_hypoxia_duration_rcp60=glue_df_May_Sep_hypoxia_duration_rcp60[2019 < glue_df_May_Sep_hypoxia_duration_rcp60.index]

glue_80years_May_Sep_hypoxia_duration_rcp85=glue_df_May_Sep_hypoxia_duration_rcp85[2019 < glue_df_May_Sep_hypoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Sep_hypoxia_duration_rcp26[glue_80years_May_Sep_hypoxia_duration_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_May_Sep_hypoxia_duration_rcp60[glue_80years_May_Sep_hypoxia_duration_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_May_Sep_hypoxia_duration_rcp85[glue_80years_May_Sep_hypoxia_duration_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Sep_hypoxia_duration_rcp26[glue_80years_May_Sep_hypoxia_duration_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_May_Sep_hypoxia_duration_rcp60[glue_80years_May_Sep_hypoxia_duration_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_May_Sep_hypoxia_duration_rcp85[glue_80years_May_Sep_hypoxia_duration_rcp85.index>2079]['50%'])
11.12826268210691

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_hypoxia_duration_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_hypoxia_duration_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_hypoxia_duration_rcp85['50%'])
(0.015654880429522035,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05661191309631117,
 7.160412951529136)

#%%plotting May_Sep hypoxia duration over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_May_Sep_hypoxia_duration_rcp26.index.astype(float), glue_80years_May_Sep_hypoxia_duration_rcp26['5%'], glue_80years_May_Sep_hypoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_May_Sep_hypoxia_duration_rcp26.index.astype(float), glue_80years_May_Sep_hypoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_May_Sep_hypoxia_duration_rcp60.index.astype(float), glue_80years_May_Sep_hypoxia_duration_rcp60['5%'], glue_80years_May_Sep_hypoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_May_Sep_hypoxia_duration_rcp60.index.astype(float), glue_80years_May_Sep_hypoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_hypoxia_duration_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_May_Sep_hypoxia_duration_rcp85.index.astype(float), glue_80years_May_Sep_hypoxia_duration_rcp85['5%'], glue_80years_May_Sep_hypoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_May_Sep_hypoxia_duration_rcp85.index.astype(float), glue_80years_May_Sep_hypoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Sep_hypoxia_duration_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('Hypoxia duration in May_Sep [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_May_Sep_hypoxia_duration.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_hypoxia_duration_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_hypoxia_duration_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)


#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_hypoxia_duration_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Sep_hypoxia_duration_rcp85['50%'])
(0.016659625265317696,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05578367086692144,
 6.403552589696595)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%hypoxic_duration_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_his[(1975 < glue_df_May_Sep_hypoxia_duration_his.index)].index.astype(float),
                      glue_df_May_Sep_hypoxia_duration_his[(1975 < glue_df_May_Sep_hypoxia_duration_his.index)]['5%'] - May_Sep_hypoxia_duration_ref,
                      glue_df_May_Sep_hypoxia_duration_his[(1975 < glue_df_May_Sep_hypoxia_duration_his.index) ]['95%'] - May_Sep_hypoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_May_Sep_hypoxia_duration_his[(1975 < glue_df_May_Sep_hypoxia_duration_his.index) ].index.astype(float),
            glue_df_May_Sep_hypoxia_duration_his[(1975 < glue_df_May_Sep_hypoxia_duration_his.index)]['50%'] - May_Sep_hypoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp26['5%']-May_Sep_hypoxia_duration_ref, glue_df_May_Sep_hypoxia_duration_rcp26['95%']-May_Sep_hypoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Sep_hypoxia_duration_rcp26.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp26['50%']-May_Sep_hypoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp60['5%']-May_Sep_hypoxia_duration_ref, glue_df_May_Sep_hypoxia_duration_rcp60['95%']-May_Sep_hypoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Sep_hypoxia_duration_rcp60.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp60['50%']-May_Sep_hypoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Sep_hypoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp85['5%']-May_Sep_hypoxia_duration_ref, glue_df_May_Sep_hypoxia_duration_rcp85['95%']-May_Sep_hypoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Sep_hypoxia_duration_rcp85.index.astype(float), glue_df_May_Sep_hypoxia_duration_rcp85['50%']-May_Sep_hypoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of hypoxia duration in May-Sep [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_May_Sep_hypoxia_duration_anomaly.png",  dpi=300, bbox_inches='tight')













#%%===========summer average of hypoxic afctor 


#%%########summer hypoxia duration 

#%%ploting summer hypoxia duration 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypoxia_duration_his.index.astype(float), glue_df_summer_hypoxia_duration_his['5%'], glue_df_summer_hypoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_summer_hypoxia_duration_his.index.astype(float), glue_df_summer_hypoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_summer_hypoxia_duration_rcp26.index.astype(float), glue_df_summer_hypoxia_duration_rcp26['5%'], glue_df_summer_hypoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_summer_hypoxia_duration_rcp26.index.astype(float), glue_df_summer_hypoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_summer_hypoxia_duration_rcp60.index.astype(float), glue_df_summer_hypoxia_duration_rcp60['5%'], glue_df_summer_hypoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypoxia_duration_rcp60.index.astype(float), glue_df_summer_hypoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypoxia_duration_rcp85.index.astype(float), glue_df_summer_hypoxia_duration_rcp85['5%'], glue_df_summer_hypoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypoxia_duration_rcp85.index.astype(float), glue_df_summer_hypoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypoxia duration in summer [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_summer_hypoxia_duration.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_summer_hypoxia_duration_his['50%'])#5.7419538116211175
np.mean(glue_df_summer_hypoxia_duration_rcp26['50%'])#7.164633836912792
np.mean(glue_df_summer_hypoxia_duration_rcp60['50%'])#7.660016638342764
np.mean(glue_df_summer_hypoxia_duration_rcp85['50%'])#7.798265277646058

#%%hypoxic_duration 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_summer_hypoxia_duration_his=glue_df_summer_hypoxia_duration_his[1975 < glue_df_summer_hypoxia_duration_his.index]['50%']
summer_hypoxia_duration_ref=np.mean(glue_base_summer_hypoxia_duration_his)
#5.830216997377137


#near future [2030-2059]

glue_near_future_summer_hypoxia_duration_rcp26=glue_df_summer_hypoxia_duration_rcp26[(2029 < glue_df_summer_hypoxia_duration_rcp26.index) & (glue_df_summer_hypoxia_duration_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypoxia_duration_rcp26)
# 7.189791199644448
glue_near_future_summer_hypoxia_duration_rcp60=glue_df_summer_hypoxia_duration_rcp60[(2029 < glue_df_summer_hypoxia_duration_rcp60.index) & (glue_df_summer_hypoxia_duration_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypoxia_duration_rcp60)
# 7.408290028941934
glue_near_future_summer_hypoxia_duration_rcp85=glue_df_summer_hypoxia_duration_rcp85[(2029 < glue_df_summer_hypoxia_duration_rcp85.index) & (glue_df_summer_hypoxia_duration_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypoxia_duration_rcp85)
# 7.577321792421727

 
#Distant future [2070-2099]

glue_distant_future_summer_hypoxia_duration_rcp26=glue_df_summer_hypoxia_duration_rcp26[(2069 < glue_df_summer_hypoxia_duration_rcp26.index) & (glue_df_summer_hypoxia_duration_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypoxia_duration_rcp26)
#7.182315856408658
glue_distant_future_summer_hypoxia_duration_rcp60=glue_df_summer_hypoxia_duration_rcp60[(2069 < glue_df_summer_hypoxia_duration_rcp60.index) & (glue_df_summer_hypoxia_duration_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_summer_hypoxia_duration_rcp60)
#8.404224632950019
glue_distant_future_summer_hypoxia_duration_rcp85=glue_df_summer_hypoxia_duration_rcp85[(2069 < glue_df_summer_hypoxia_duration_rcp85.index) & (glue_df_summer_hypoxia_duration_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypoxia_duration_rcp85)
#8.844476856722357
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_summer_hypoxia_duration_his)
(0.03384344872449237,
 'positively autocorrelated',
 'no trend',
 0.2389927879015219,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypoxia_duration_rcp26)
(0.017426799559486894,
 'positively autocorrelated',
 'no trend',
 0.2686642304239091,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypoxia_duration_rcp60)
(0.011027838419972513,
 'positively autocorrelated',
 'no trend',
 0.08039114754218035,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypoxia_duration_rcp85)

(0.010531400508757774,
 'positively autocorrelated',
 'increasing',
 0.0053825476031263975,
 0.0337942438328447,
 7.0319428173255965)


#Distant future [2070-2099]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypoxia_duration_rcp26)
(0.007455597611559313,
 'positively autocorrelated',
 'increasing',
 0.011479484705922305,
 0.03254964585051723,
 6.704083850293537)
#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypoxia_duration_rcp60)
(0.005218209926031563,
 'positively autocorrelated',
 'no trend',
 0.7752944295177846,
 0,
 0)
#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypoxia_duration_rcp85)
(0.011260089055346817,
 'positively autocorrelated',
 'no trend',
 0.2844114676220473,
 0,
 0)





#%% 80 years from 2020 for summer_hypoxia_duration


glue_80years_summer_hypoxia_duration_rcp26=glue_df_summer_hypoxia_duration_rcp26[2019 < glue_df_summer_hypoxia_duration_rcp26.index]

glue_80years_summer_hypoxia_duration_rcp60=glue_df_summer_hypoxia_duration_rcp60[2019 < glue_df_summer_hypoxia_duration_rcp60.index]

glue_80years_summer_hypoxia_duration_rcp85=glue_df_summer_hypoxia_duration_rcp85[2019 < glue_df_summer_hypoxia_duration_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypoxia_duration_rcp26[glue_80years_summer_hypoxia_duration_rcp26.index<2030]['50%'])
7.236131611808827

#rcp6.0
np.mean(glue_80years_summer_hypoxia_duration_rcp60[glue_80years_summer_hypoxia_duration_rcp60.index<2030]['50%'])
7.0480838080216754

#rcp8.5
np.mean(glue_80years_summer_hypoxia_duration_rcp85[glue_80years_summer_hypoxia_duration_rcp85.index<2030]['50%'])
6.92973720099211

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypoxia_duration_rcp26[glue_80years_summer_hypoxia_duration_rcp26.index>2079]['50%'])
7.284732847455828

#rcp6.0
np.mean(glue_80years_summer_hypoxia_duration_rcp60[glue_80years_summer_hypoxia_duration_rcp60.index>2079]['50%'])
8.376808940760498

#rcp8.5
np.mean(glue_80years_summer_hypoxia_duration_rcp85[glue_80years_summer_hypoxia_duration_rcp85.index>2079]['50%'])
8.902897713112784

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypoxia_duration_rcp26['50%'])
(0.012431261551918694,
 'positively autocorrelated',
 'no trend',
 0.4722909038902814,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypoxia_duration_rcp60['50%'])
(0.009054412557226742,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.021466406502838986,
 6.936654760438897)


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypoxia_duration_rcp85['50%'])
(0.012767144112602902,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031086674796400225,
 6.7697952941890875)



#%%plotting summer hypoxia duration over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_summer_hypoxia_duration_rcp26.index.astype(float), glue_80years_summer_hypoxia_duration_rcp26['5%'], glue_80years_summer_hypoxia_duration_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_summer_hypoxia_duration_rcp26.index.astype(float), glue_80years_summer_hypoxia_duration_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_summer_hypoxia_duration_rcp60.index.astype(float), glue_80years_summer_hypoxia_duration_rcp60['5%'], glue_80years_summer_hypoxia_duration_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_summer_hypoxia_duration_rcp60.index.astype(float), glue_80years_summer_hypoxia_duration_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypoxia_duration_rcp60['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_summer_hypoxia_duration_rcp85.index.astype(float), glue_80years_summer_hypoxia_duration_rcp85['5%'], glue_80years_summer_hypoxia_duration_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_summer_hypoxia_duration_rcp85.index.astype(float), glue_80years_summer_hypoxia_duration_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypoxia_duration_rcp85['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('Hypoxia duration in summer [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_summer_hypoxia_duration.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire scenario

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypoxia_duration_his['50%'])
(0.050102399473259764,
 'positively autocorrelated',
 'no trend',
 0.15346389188435516,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypoxia_duration_rcp26['50%'])
(0.011480536925277993,
 'positively autocorrelated',
 'increasing',
 0.030392451085676786,
 0.0039129273367328335,
 6.963469344761228)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypoxia_duration_rcp60['50%'])
(0.010198727721089741,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.02131982928372496,
 6.689481345978918)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypoxia_duration_rcp85['50%'])
(0.014688565156364046,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031748328950495945,
 6.343632396381782)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%hypoxic_duration_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypoxia_duration_his[(1975 < glue_df_summer_hypoxia_duration_his.index)].index.astype(float),
                      glue_df_summer_hypoxia_duration_his[(1975 < glue_df_summer_hypoxia_duration_his.index)]['5%'] - summer_hypoxia_duration_ref,
                      glue_df_summer_hypoxia_duration_his[(1975 < glue_df_summer_hypoxia_duration_his.index) ]['95%'] - summer_hypoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_summer_hypoxia_duration_his[(1975 < glue_df_summer_hypoxia_duration_his.index) ].index.astype(float),
            glue_df_summer_hypoxia_duration_his[(1975 < glue_df_summer_hypoxia_duration_his.index)]['50%'] - summer_hypoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_summer_hypoxia_duration_rcp26.index.astype(float), glue_df_summer_hypoxia_duration_rcp26['5%']-summer_hypoxia_duration_ref, glue_df_summer_hypoxia_duration_rcp26['95%']-summer_hypoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypoxia_duration_rcp26.index.astype(float), glue_df_summer_hypoxia_duration_rcp26['50%']-summer_hypoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_summer_hypoxia_duration_rcp60.index.astype(float), glue_df_summer_hypoxia_duration_rcp60['5%']-summer_hypoxia_duration_ref, glue_df_summer_hypoxia_duration_rcp60['95%']-summer_hypoxia_duration_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypoxia_duration_rcp60.index.astype(float), glue_df_summer_hypoxia_duration_rcp60['50%']-summer_hypoxia_duration_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypoxia_duration_rcp85.index.astype(float), glue_df_summer_hypoxia_duration_rcp85['5%']-summer_hypoxia_duration_ref, glue_df_summer_hypoxia_duration_rcp85['95%']-summer_hypoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypoxia_duration_rcp85.index.astype(float), glue_df_summer_hypoxia_duration_rcp85['50%']-summer_hypoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of hypoxia duration in summer [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_summer_hypoxia_duration_anomaly.png",  dpi=300, bbox_inches='tight')










#%%
####################################old one
############################################
############################################

#%% Annual hypoxia duration_gfdl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_hypoxia_duartion_gfdl_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_gfdl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_gfdl_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_gfdl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_gfdl_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_gfdl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_gfdl_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual hypoxia duration_hadgem_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_hadgem_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_hadgem_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_hadgem_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_hadgem_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_hadgem_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_hadgem_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_hadgem_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual hypoxia duration_ipsl_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_ipsl_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_ipsl_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_ipsl_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_ipsl_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_ipsl_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_ipsl_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_ipsl_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_miroc_his
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_miroc_his

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual hypoxia duration_miroc_rcp26
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_miroc_rcp26

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual hypoxia duration_miroc_rcp60
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_miroc_rcp60

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual hypoxia duration_miroc_rcp85
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
        
        # Apply the annual_hypoxia_duration function
        result = annual_hypoxia_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypoxia_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypoxia_duration'])
        
                


#%%monthly_table_of_anpoxic_duration_miroc_rcp85

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
        
        # Apply the annual_hypoxia_duration function
        result = monthly_table_of_anpoxic_duration(C, time_series,Vr, threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_table_of_anpoxic_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
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



all_annual_hypoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        


# annual hypoxia duration  
timeseries_year_his= all_annual_hypoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_his=glue_df_annual_hypoxia_duration_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_hypoxic_duration_his.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_fixedtheta/glue_df_hypoxic_duration_his.csv')



####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypoxia_duration_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_calibinfixedtheta_simuvartheta/glue_df_hypoxic_duration_his.csv')

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



all_annual_hypoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        


# annual hypoxia duration  
timeseries_year_rcp26= all_annual_hypoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_hypoxic_duration_rcp26.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_hypoxic_duration_rcp26.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#########glue_df_annual_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_hypoxic_duration_rcp26.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypoxia_duration_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_hypoxic_duration_rcp26.csv')



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



all_annual_hypoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        


# annual hypoxia duration  
timeseries_year_rcp60= all_annual_hypoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_hypoxic_duration_rcp60.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_hypoxic_duration_rcp60.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#########glue_df_annual_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_hypoxic_duration_rcp60.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypoxia_duration_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_hypoxic_duration_rcp60.csv')



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



all_annual_hypoxia_duration= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypoxia_duration_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypoxia_duration = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypoxia_duration=annual_hypoxia_duration.set_index(annual_hypoxia_duration['year'])
        
        all_annual_hypoxia_duration = pd.concat([all_annual_hypoxia_duration , annual_hypoxia_duration['annual_hypoxia_duration']], axis=1)
        
        
        
        


# annual hypoxia duration  
timeseries_year_rcp85= all_annual_hypoxia_duration.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypoxia_duration.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypoxia_duration_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_hypoxic_duration_rcp85.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_hypoxic_duration_rcp85.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#########glue_df_annual_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_hypoxic_duration_rcp85.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypoxia_duration_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_hypoxic_duration_rcp85.csv')


#%%#######fixed theta:
    
#######glue_df_annual_hypoxia_duration_his_fixedtheta=  glue_df_annual_hypoxia_duration_his.copy()

glue_df_annual_hypoxia_duration_his= glue_df_annual_hypoxia_duration_his_fixedtheta.copy()

#######glue_df_annual_hypoxia_duration_rcp26_fixedtheta=  glue_df_annual_hypoxia_duration_rcp26.copy()

glue_df_annual_hypoxia_duration_rcp26= glue_df_annual_hypoxia_duration_rcp26_fixedtheta.copy()

#######glue_df_annual_hypoxia_duration_rcp60_fixedtheta=  glue_df_annual_hypoxia_duration_rcp60.copy()

glue_df_annual_hypoxia_duration_rcp60= glue_df_annual_hypoxia_duration_rcp60_fixedtheta.copy()

#######glue_df_annual_hypoxia_duration_rcp85_fixedtheta=  glue_df_annual_hypoxia_duration_rcp85.copy()

glue_df_annual_hypoxia_duration_rcp85= glue_df_annual_hypoxia_duration_rcp85_fixedtheta.copy()



#%%_vartheta

glue_df_annual_hypoxia_duration_his_vartheta= glue_df_annual_hypoxia_duration_his.copy()



glue_df_annual_hypoxia_duration_rcp26_vartheta= glue_df_annual_hypoxia_duration_rcp26.copy()


glue_df_annual_hypoxia_duration_rcp60_vartheta= glue_df_annual_hypoxia_duration_rcp60.copy()


glue_df_annual_hypoxia_duration_rcp85_vartheta= glue_df_annual_hypoxia_duration_rcp85.copy()


#%%difference of Vartheta model and fixed theta 


diff_median_annual_hypoxia_duration_vartheta_fixedtheta_his=glue_df_annual_hypoxia_duration_his_vartheta['50%']-glue_df_annual_hypoxia_duration_his['50%']
np.mean(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_his)
-1.521539830552154

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_his)
(0.4102745697759908,
 'positively autocorrelated',
 'no trend',
 0.08641995700155558,
 0,
 0)




diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp26=glue_df_annual_hypoxia_duration_rcp26_vartheta['50%']-glue_df_annual_hypoxia_duration_rcp26['50%']
np.mean(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp26)
-2.3009426195783225
autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp26)

(0.2471291056619972,
 'positively autocorrelated',
 'no trend',
 0.5406757306713583,
 0,
 0)



diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp60=glue_df_annual_hypoxia_duration_rcp60_vartheta['50%']-glue_df_annual_hypoxia_duration_rcp60['50%']
np.mean(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp60)
-1.3593195664094877

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp60)
(0.45142216245912026,
 'positively autocorrelated',
 'no trend',
 0.24575216426645285,
 0,
 0)



diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp85=glue_df_annual_hypoxia_duration_rcp85_vartheta['50%']-glue_df_annual_hypoxia_duration_rcp85['50%']
np.mean(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp85)
-1.8403265395237618

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp85)
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


ax=plt.plot(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_his.index, diff_median_annual_hypoxia_duration_vartheta_fixedtheta_his, 'grey', label='His median', alpha=1, linewidth=3 )


ax=plt.plot(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp26.index, diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp26, 'green', label='RCP2.6 median', alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp60.index, diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp60, 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp85.index, diff_median_annual_hypoxia_duration_vartheta_fixedtheta_rcp85, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )



ax=plt.ylabel('Difference of fixed and variable Ktemp assumption in simulating annual hypoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(-4, 3, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22)


####### test with fixed theta in calibration but variable for GOTM simulation 
fig.savefig("GLUE_Timeseries_hypolimnetic_DO_6combinationJaJv_ave_obs_4models_diff_fixed_var_theta.png", dpi=300, bbox_inches='tight')




#%% first 10 years 2020-2029

#rcp26
glue_df_annual_hypoxia_duration_median_1st_10years_rcp26=glue_df_annual_hypoxia_duration_rcp26[(2019<glue_df_annual_hypoxia_duration_rcp26.index) & (glue_df_annual_hypoxia_duration_rcp26.index<2030)]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_1st_10years_rcp26)
#7.470031426050075

glue_df_annual_hypoxia_duration_median_1st_10years_rcp26_vartheta=glue_df_annual_hypoxia_duration_rcp26_vartheta[(2019<glue_df_annual_hypoxia_duration_rcp26_vartheta.index) & (glue_df_annual_hypoxia_duration_rcp26_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_1st_10years_rcp26_vartheta)
#5.655030434919324


#rcp60

glue_df_annual_hypoxia_duration_median_1st_10years_rcp60=glue_df_annual_hypoxia_duration_rcp60[(2019<glue_df_annual_hypoxia_duration_rcp60.index) & (glue_df_annual_hypoxia_duration_rcp60.index<2030)]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_1st_10years_rcp60)
#7.077280785340525



glue_df_annual_hypoxia_duration_median_1st_10years_rcp60_vartheta=glue_df_annual_hypoxia_duration_rcp60_vartheta[(2019<glue_df_annual_hypoxia_duration_rcp60_vartheta.index) & (glue_df_annual_hypoxia_duration_rcp60_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_1st_10years_rcp60_vartheta)
#5.442294872796134

#rcp85

glue_df_annual_hypoxia_duration_median_1st_10years_rcp85=glue_df_annual_hypoxia_duration_rcp85[(2019<glue_df_annual_hypoxia_duration_rcp85.index) & (glue_df_annual_hypoxia_duration_rcp85.index<2030)]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_1st_10years_rcp85)
#6.80621601212993

glue_df_annual_hypoxia_duration_median_1st_10years_rcp85_vartheta=glue_df_annual_hypoxia_duration_rcp85_vartheta[(2019<glue_df_annual_hypoxia_duration_rcp85_vartheta.index) & (glue_df_annual_hypoxia_duration_rcp85_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_1st_10years_rcp85_vartheta)
#5.589130553716512

#%%last 10 years 2090-2099

#rcp26
glue_df_annual_hypoxia_duration_median_last_10years_rcp26=glue_df_annual_hypoxia_duration_rcp26[glue_df_annual_hypoxia_duration_rcp26.index>2089]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_last_10years_rcp26)
#8.613753815447875

glue_df_annual_hypoxia_duration_median_last_10years_rcp26_vartheta=glue_df_annual_hypoxia_duration_rcp26_vartheta[glue_df_annual_hypoxia_duration_rcp26_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_last_10years_rcp26_vartheta)
#5.99974215818178

#rcp60
glue_df_annual_hypoxia_duration_median_last_10years_rcp60=glue_df_annual_hypoxia_duration_rcp60[glue_df_annual_hypoxia_duration_rcp60.index>2089]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_last_10years_rcp60)
#8.840670784774442

glue_df_annual_hypoxia_duration_median_last_10years_rcp60_vartheta=glue_df_annual_hypoxia_duration_rcp60_vartheta[glue_df_annual_hypoxia_duration_rcp60_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_last_10years_rcp60_vartheta)
#7.461205289215991
#rcp85
glue_df_annual_hypoxia_duration_median_last_10years_rcp85=glue_df_annual_hypoxia_duration_rcp85[glue_df_annual_hypoxia_duration_rcp85.index>2089]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_last_10years_rcp85)
#10.848450635366076

glue_df_annual_hypoxia_duration_median_last_10years_rcp85_vartheta=glue_df_annual_hypoxia_duration_rcp85_vartheta[glue_df_annual_hypoxia_duration_rcp85_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypoxia_duration_median_last_10years_rcp85_vartheta)
#9.225106418152142

#%% 100 years for rcps 

#rcp26

#fixed theta
glue_df_annual_hypoxia_duration_4models_100years_rcp26=pd.concat([glue_df_annual_hypoxia_duration_his[glue_df_annual_hypoxia_duration_his.index>1999] , glue_df_annual_hypoxia_duration_rcp26])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypoxia_duration_4models_100years_rcp26 ['50%'])  

(0.03233165257593502,
 'positively autocorrelated',
 'increasing',
 1.235052435877293e-07,
 0.0121937938499866,
 7.255097746966682)





#Var theta
glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta=pd.concat([glue_df_annual_hypoxia_duration_his_vartheta[glue_df_annual_hypoxia_duration_his_vartheta.index>1999] , glue_df_annual_hypoxia_duration_rcp26_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta ['50%'])  

(0.03955505915646442,
 'positively autocorrelated',
 'increasing',
 0.0006010992236442636,
 0.010497984593900105,
 5.030834333984101)



#rcp60

#fixed theta
glue_df_annual_hypoxia_duration_4models_100years_rcp60=pd.concat([glue_df_annual_hypoxia_duration_his[glue_df_annual_hypoxia_duration_his.index>1999] , glue_df_annual_hypoxia_duration_rcp60])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypoxia_duration_4models_100years_rcp60 ['50%'])  
(0.02795672807292709,
 'positively autocorrelated',
 'increasing',
 2.220446049250313e-16,
 0.0332750689583886,
 5.986757230735907)




#Var theta
glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta=pd.concat([glue_df_annual_hypoxia_duration_his_vartheta[glue_df_annual_hypoxia_duration_his_vartheta.index>1999] , glue_df_annual_hypoxia_duration_rcp60_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta ['50%'])  
(0.029177475988549587,
 'positively autocorrelated',
 'increasing',
 2.970956813896919e-13,
 0.03420571640423424,
 4.397863069746866)


#rcp85

#fixed theta
glue_df_annual_hypoxia_duration_4models_100years_rcp85=pd.concat([glue_df_annual_hypoxia_duration_his[glue_df_annual_hypoxia_duration_his.index>1999] , glue_df_annual_hypoxia_duration_rcp85])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypoxia_duration_4models_100years_rcp85 ['50%'])  
(0.031072004914250547,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05455817956023478,
 5.832292270455436)




#Var theta
glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta=pd.concat([glue_df_annual_hypoxia_duration_his_vartheta[glue_df_annual_hypoxia_duration_his_vartheta.index>1999] , glue_df_annual_hypoxia_duration_rcp85_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta ['50%'])  

(0.035580951696717295,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05165045008766002,
 3.9207344560109947)

#%% trendline sen's slope 

autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_his['50%']) 

Out[1243]: 
(0.08861134396877238,
 'positively autocorrelated',
 'no trend',
 0.10192618852194646,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_his_vartheta['50%']) 

(0.1383412609645987,
 'positively autocorrelated',
 'no trend',
 0.31072008139962315,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp26['50%']) 
(0.03379118006876991,
 'positively autocorrelated',
 'increasing',
 6.908279212325397e-05,
 0.010564337601135008,
 7.4785025189153735)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp26_vartheta['50%']) 
(0.039507716688300144,
 'positively autocorrelated',
 'increasing',
 0.022504355893704142,
 0.008218111766768784,
 5.1831384217248875)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp60['50%']) 
(0.028720309370685593,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.03880652178553318,
 5.88161432295651)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp60_vartheta['50%']) 
(0.028883853368500165,
 'positively autocorrelated',
 'increasing',
 7.286293790542686e-10,
 0.033514404467106934,
 4.616452079764355)


autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp85['50%']) 
(0.03167796451466309,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.059792750353943616,
 5.873773932605548)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_rcp85_vartheta['50%']) 
(0.03389759807269532,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05300685412619691,
 4.1760561507416)



#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%Annual hypoxia duration 

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


#ax=plt.fill_between(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['5%'], glue_df_annual_hypoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta['5%'], glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_4models_100years_rcp26_vartheta['50%'])
ax=plt.text(2020, 10, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta['5%'], glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_4models_100years_rcp60_vartheta['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta['5%'], glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_4models_100years_rcp85_vartheta['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Hypoxia duration per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_hypoxic_duration_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


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


#ax=plt.fill_between(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['5%'], glue_df_annual_hypoxia_duration_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_hypoxia_duration_his.index.astype(float), glue_df_annual_hypoxia_duration_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypoxia_duration_4models_100years_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp26['5%'], glue_df_annual_hypoxia_duration_4models_100years_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_4models_100years_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_4models_100years_rcp26['50%'])
ax=plt.text(2020, 15, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypoxia_duration_4models_100years_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp60['5%'], glue_df_annual_hypoxia_duration_4models_100years_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_4models_100years_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_4models_100years_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypoxia_duration_4models_100years_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp85['5%'], glue_df_annual_hypoxia_duration_4models_100years_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_4models_100years_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_4models_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypoxia_duration_4models_100years_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Hypoxia duration per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_hypoxic_duration_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
# original # fixed gcm temp in 2020 and 2021
np.mean(glue_df_annual_hypoxia_duration_his['50%'])#5.118056494914366# 5.371846482897608
np.mean(glue_df_annual_hypoxia_duration_rcp26['50%'])#7.009871810216667# 7.960074150018018
np.mean(glue_df_annual_hypoxia_duration_rcp60['50%'])#7.599031745432739# 7.661889247294462
np.mean(glue_df_annual_hypoxia_duration_rcp85['50%'])#8.15444840073441#8.680607289244922

np.mean(glue_df_annual_hypoxia_duration_his_vartheta['50%'])#3.8503066523454508
np.mean(glue_df_annual_hypoxia_duration_rcp26_vartheta['50%'])#5.659131530439698
np.mean(glue_df_annual_hypoxia_duration_rcp60_vartheta['50%'])#6.302569680884974
np.mean(glue_df_annual_hypoxia_duration_rcp85_vartheta['50%'])#6.840280749721157



#%%hypoxic_duration 30 yerars from each scenarios compare 


#Sorting the glue dataframe according to the index (year)

glue_df_annual_hypoxia_duration_his=glue_df_annual_hypoxia_duration_his.sort_index()

glue_df_annual_hypoxia_duration_rcp26=glue_df_annual_hypoxia_duration_rcp26.sort_index()

glue_df_annual_hypoxia_duration_rcp60=glue_df_annual_hypoxia_duration_rcp60.sort_index()

glue_df_annual_hypoxia_duration_rcp85=glue_df_annual_hypoxia_duration_rcp85.sort_index()





#anomaly 

# baseline [1976-2005]
annual_hypoxia_duration_ref=glue_df_annual_hypoxia_duration_his[1975 < glue_df_annual_hypoxia_duration_his.index]['50%'].mean()

#5.410877320721374
#5.914740063212032


#near future [2030-2059] 

glue_df_annual_hypoxia_duration_rcp26[(2029 < glue_df_annual_hypoxia_duration_rcp26.index) & (glue_df_annual_hypoxia_duration_rcp26.index < 2060)]['50%'].mean()
# 7.072947718287684
# 7.950218353351354
glue_df_annual_hypoxia_duration_rcp60[(2029 < glue_df_annual_hypoxia_duration_rcp60.index) & (glue_df_annual_hypoxia_duration_rcp60.index < 2060)]['50%'].mean()
# 7.156265572954701
# 7.139975067233944

glue_df_annual_hypoxia_duration_rcp85[(2029 < glue_df_annual_hypoxia_duration_rcp85.index) & (glue_df_annual_hypoxia_duration_rcp85.index < 2060)]['50%'].mean()
# 7.630745663516447
# 8.223867040126178
 
#Distant future [2070-2099]

glue_df_annual_hypoxia_duration_rcp26[(2069 < glue_df_annual_hypoxia_duration_rcp26.index) & (glue_df_annual_hypoxia_duration_rcp26.index < 2100)]['50%'].mean()
#7.17035474380281
#8.221226628944514


glue_df_annual_hypoxia_duration_rcp60[(2069 < glue_df_annual_hypoxia_duration_rcp60.index) & (glue_df_annual_hypoxia_duration_rcp60.index < 2100)]['50%'].mean()
#8.781804641713899
#8.984771173520228

glue_df_annual_hypoxia_duration_rcp85[(2069 < glue_df_annual_hypoxia_duration_rcp85.index) & (glue_df_annual_hypoxia_duration_rcp85.index < 2100)]['50%'].mean()
#7.630745663516447
# 10.612461480324987



#%%hypoxic_duration_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypoxia_duration_his[1975 < glue_df_annual_hypoxia_duration_his.index].index.astype(float),
                      glue_df_annual_hypoxia_duration_his[1975 < glue_df_annual_hypoxia_duration_his.index]['5%'].astype(float) - annual_hypoxia_duration_ref,
                      glue_df_annual_hypoxia_duration_his[1975 < glue_df_annual_hypoxia_duration_his.index ]['95%'].astype(float) - annual_hypoxia_duration_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index) ].index.astype(float),
            glue_df_annual_hypoxia_duration_his[(1975 < glue_df_annual_hypoxia_duration_his.index)]['50%'].astype(float) - annual_hypoxia_duration_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['5%'].astype(float)-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp26['95%'].astype(float)-annual_hypoxia_duration_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp26.index.astype(float), glue_df_annual_hypoxia_duration_rcp26['50%'].astype(float)-annual_hypoxia_duration_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['5%'].astype(float)-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp60['95%'].astype(float)-annual_hypoxia_duration_ref, color='b', alpha=0.27 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp60.index.astype(float), glue_df_annual_hypoxia_duration_rcp60['50%'].astype(float)-annual_hypoxia_duration_ref, 'b', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['5%'].astype(float)-annual_hypoxia_duration_ref, glue_df_annual_hypoxia_duration_rcp85['95%'].astype(float)-annual_hypoxia_duration_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypoxia_duration_rcp85.index.astype(float), glue_df_annual_hypoxia_duration_rcp85['50%'].astype(float)-annual_hypoxia_duration_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of hypoxia duration [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_hypoxic_duration_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


