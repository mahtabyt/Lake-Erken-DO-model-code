#for managemnt on Hdur under future scenarios 
# The function of having DO prof with VHOD is in DO_model_my file 
# this function was used to calculate the results 
# of different Jz sets less than calibrated value in each GCMs and scenarios 

#NOW we will use Hdur-annual-summer-May-jun functions
#For mangement senarios 

#%% testing the DO model using VHOD ranges lower than the calibarted ones 
"""
16 behavioural VHOD:
'Minimum': 0.49552461937155823,
 'Maximum': 0.6014850988014254,
"""

jz_min, jz_max = 0, 0.6

num_points =len(np.arange(jz_min, jz_max+0.01 , 0.01))

param_values = np.arange(jz_min, jz_max+0.01 , 0.01)



jz_management_test=[]
for i, p in enumerate(param_values):
    
    
    jz_management_test.append([p, 1])


#minimum is mnnually set to 0.001
jz_management_test[0]=[0.001, 1]


#%%
#make annual-summer- May_sep Hdur
#for different VHODs for RCPs and GCMs
# for each year

#%%rcp26

#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_gfdl_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

#hadgem

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_hadgem_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

#ipsl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_ipsl_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

 
#miroc

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      


        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_miroc_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

 
#%%rcp60

#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      


        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_gfdl_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        


#hadgem

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_hadgem_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

#ipsl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      


        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_ipsl_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

 
#miroc

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_miroc_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        
     
 
#%%rcp85

#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_gfdl_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

 

#hadgem

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_hadgem_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

 
#ipsl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_ipsl_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        
 
#miroc

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_C_daily_VHOD_mangement_test'



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jz_"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])

        # Apply the annual_hypoxia_duration function
        result_annual = annual_hypoxia_duration(C, time_series,Vr , threshold=2)
      

        
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the annual_Hdur to a new CSV file
        result_filename_annual = f'annual_Hdur_miroc_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename_annual))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_filename_annual) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
        

 
#%% extracting last 10 years and current 10 years 

#%%==================gfdl====================

#%% gfdl_rcp26

#%% Hdur_annual_gfdl_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_gfdl_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_gfdl_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_gfdl_rcp26 = pd.concat([df_Hdur_annual_inlast10years_gfdl_rcp26, temp_df_gfdl_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_gfdl_rcp26 = pd.concat([df_Hdur_annual_incurr10years_gfdl_rcp26, temp_df_gfdl_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_gfdl_rcp26 = (df_Hdur_annual_incurr10years_gfdl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_gfdl_rcp26['mean'] = mean_Hdur_annual_incurr10years_gfdl_rcp26
          



# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_gfdl_rcp26 = (df_Hdur_annual_inlast10years_gfdl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_gfdl_rcp26['mean'] = mean_Hdur_annual_inlast10years_gfdl_rcp26



#%% gfdl_rcp60

#%% Hdur_annual_gfdl_rcp60

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_gfdl_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_gfdl_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_gfdl_rcp60 = pd.concat([df_Hdur_annual_inlast10years_gfdl_rcp60, temp_df_gfdl_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_gfdl_rcp60 = pd.concat([df_Hdur_annual_incurr10years_gfdl_rcp60, temp_df_gfdl_rcp60_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_gfdl_rcp60 = (df_Hdur_annual_incurr10years_gfdl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_gfdl_rcp60['mean'] = mean_Hdur_annual_incurr10years_gfdl_rcp60
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_gfdl_rcp60 = (df_Hdur_annual_inlast10years_gfdl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_gfdl_rcp60['mean'] = mean_Hdur_annual_inlast10years_gfdl_rcp60



#%% gfdl_rcp85

#%% Hdur_annual_gfdl_rcp85

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_gfdl_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_gfdl_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_gfdl_rcp85 = pd.concat([df_Hdur_annual_inlast10years_gfdl_rcp85, temp_df_gfdl_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_gfdl_rcp85 = pd.concat([df_Hdur_annual_incurr10years_gfdl_rcp85, temp_df_gfdl_rcp85_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_gfdl_rcp85 = (df_Hdur_annual_incurr10years_gfdl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_gfdl_rcp85['mean'] = mean_Hdur_annual_incurr10years_gfdl_rcp85
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_gfdl_rcp85 = (df_Hdur_annual_inlast10years_gfdl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_gfdl_rcp85['mean'] = mean_Hdur_annual_inlast10years_gfdl_rcp85



#%%===================hadgem
#%% hadgem_rcp26

#%% Hdur_annual_hadgem_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_hadgem_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_hadgem_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_hadgem_rcp26 = pd.concat([df_Hdur_annual_inlast10years_hadgem_rcp26, temp_df_hadgem_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_hadgem_rcp26 = pd.concat([df_Hdur_annual_incurr10years_hadgem_rcp26, temp_df_hadgem_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_hadgem_rcp26 = (df_Hdur_annual_incurr10years_hadgem_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_hadgem_rcp26['mean'] = mean_Hdur_annual_incurr10years_hadgem_rcp26
          



# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_hadgem_rcp26 = (df_Hdur_annual_inlast10years_hadgem_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_hadgem_rcp26['mean'] = mean_Hdur_annual_inlast10years_hadgem_rcp26


#%% hadgem_rcp60

#%% Hdur_annual_hadgem_rcp60

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_hadgem_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_hadgem_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_hadgem_rcp60 = pd.concat([df_Hdur_annual_inlast10years_hadgem_rcp60, temp_df_hadgem_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_hadgem_rcp60 = pd.concat([df_Hdur_annual_incurr10years_hadgem_rcp60, temp_df_hadgem_rcp60_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_hadgem_rcp60 = (df_Hdur_annual_incurr10years_hadgem_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_hadgem_rcp60['mean'] = mean_Hdur_annual_incurr10years_hadgem_rcp60
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_hadgem_rcp60 = (df_Hdur_annual_inlast10years_hadgem_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_hadgem_rcp60['mean'] = mean_Hdur_annual_inlast10years_hadgem_rcp60


#%% hadgem_rcp85

#%% Hdur_annual_hadgem_rcp85

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_hadgem_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_hadgem_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_hadgem_rcp85 = pd.concat([df_Hdur_annual_inlast10years_hadgem_rcp85, temp_df_hadgem_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_hadgem_rcp85 = pd.concat([df_Hdur_annual_incurr10years_hadgem_rcp85, temp_df_hadgem_rcp85_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_hadgem_rcp85 = (df_Hdur_annual_incurr10years_hadgem_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_hadgem_rcp85['mean'] = mean_Hdur_annual_incurr10years_hadgem_rcp85
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_hadgem_rcp85 = (df_Hdur_annual_inlast10years_hadgem_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_hadgem_rcp85['mean'] = mean_Hdur_annual_inlast10years_hadgem_rcp85


  
#%%==================ipsl=================


#%% ipsl_rcp26

#%% Hdur_annual_ipsl_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_ipsl_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_ipsl_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_ipsl_rcp26 = pd.concat([df_Hdur_annual_inlast10years_ipsl_rcp26, temp_df_ipsl_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_ipsl_rcp26 = pd.concat([df_Hdur_annual_incurr10years_ipsl_rcp26, temp_df_ipsl_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_ipsl_rcp26 = (df_Hdur_annual_incurr10years_ipsl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_ipsl_rcp26['mean'] = mean_Hdur_annual_incurr10years_ipsl_rcp26
          



# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_ipsl_rcp26 = (df_Hdur_annual_inlast10years_ipsl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_ipsl_rcp26['mean'] = mean_Hdur_annual_inlast10years_ipsl_rcp26


#%% ipsl_rcp60

#%% Hdur_annual_ipsl_rcp60

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_ipsl_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_ipsl_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_ipsl_rcp60 = pd.concat([df_Hdur_annual_inlast10years_ipsl_rcp60, temp_df_ipsl_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_ipsl_rcp60 = pd.concat([df_Hdur_annual_incurr10years_ipsl_rcp60, temp_df_ipsl_rcp60_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_ipsl_rcp60 = (df_Hdur_annual_incurr10years_ipsl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_ipsl_rcp60['mean'] = mean_Hdur_annual_incurr10years_ipsl_rcp60
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_ipsl_rcp60 = (df_Hdur_annual_inlast10years_ipsl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_ipsl_rcp60['mean'] = mean_Hdur_annual_inlast10years_ipsl_rcp60


#%% ipsl_rcp85

#%% Hdur_annual_ipsl_rcp85

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_ipsl_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_ipsl_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_ipsl_rcp85 = pd.concat([df_Hdur_annual_inlast10years_ipsl_rcp85, temp_df_ipsl_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_ipsl_rcp85 = pd.concat([df_Hdur_annual_incurr10years_ipsl_rcp85, temp_df_ipsl_rcp85_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_ipsl_rcp85 = (df_Hdur_annual_incurr10years_ipsl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_ipsl_rcp85['mean'] = mean_Hdur_annual_incurr10years_ipsl_rcp85
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_ipsl_rcp85 = (df_Hdur_annual_inlast10years_ipsl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_ipsl_rcp85['mean'] = mean_Hdur_annual_inlast10years_ipsl_rcp85


#%%==================miroc==========

#%% miroc_rcp26

#%% Hdur_annual_miroc_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_miroc_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_miroc_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_miroc_rcp26 = pd.concat([df_Hdur_annual_inlast10years_miroc_rcp26, temp_df_miroc_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_miroc_rcp26 = pd.concat([df_Hdur_annual_incurr10years_miroc_rcp26, temp_df_miroc_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_miroc_rcp26 = (df_Hdur_annual_incurr10years_miroc_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_miroc_rcp26['mean'] = mean_Hdur_annual_incurr10years_miroc_rcp26
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_miroc_rcp26 = (df_Hdur_annual_inlast10years_miroc_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_miroc_rcp26['mean'] = mean_Hdur_annual_inlast10years_miroc_rcp26


#%% miroc_rcp60

#%% Hdur_annual_miroc_rcp60

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_miroc_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_miroc_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_miroc_rcp60 = pd.concat([df_Hdur_annual_inlast10years_miroc_rcp60, temp_df_miroc_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_miroc_rcp60 = pd.concat([df_Hdur_annual_incurr10years_miroc_rcp60, temp_df_miroc_rcp60_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_miroc_rcp60 = (df_Hdur_annual_incurr10years_miroc_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_miroc_rcp60['mean'] = mean_Hdur_annual_incurr10years_miroc_rcp60
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_miroc_rcp60 = (df_Hdur_annual_inlast10years_miroc_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_miroc_rcp60['mean'] = mean_Hdur_annual_inlast10years_miroc_rcp60



#%% miroc_rcp85

#%% Hdur_annual_miroc_rcp85

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_C_daily_VHOD_mangement_test'



# last 10 years (2009-2099)
column_names = ['jz'] + [f'Hdur_annual_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_inlast10years_miroc_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'Hdur_annual_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_annual_incurr10years_miroc_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_Hdur"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DatHdur_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        Hdur_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        Hdur_annual_index = pd.DataFrame(Hdur_annual).set_index(year)




        
        # last 10 years
        Hdur_annual_last_10years = Hdur_annual_index[Hdur_annual_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_last_10years_{i}': [Hdur_annual_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_inlast10years_miroc_rcp85 = pd.concat([df_Hdur_annual_inlast10years_miroc_rcp85, temp_df_miroc_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        Hdur_annual_curr_10years = Hdur_annual_index[(Hdur_annual_index.index > 2019) & (Hdur_annual_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'Hdur_annual_curr_10years_{i}': [Hdur_annual_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_annual_incurr10years_miroc_rcp85 = pd.concat([df_Hdur_annual_incurr10years_miroc_rcp85, temp_df_miroc_rcp85_curr_10years], ignore_index=True)




# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_incurr10years_miroc_rcp85 = (df_Hdur_annual_incurr10years_miroc_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_incurr10years_miroc_rcp85['mean'] = mean_Hdur_annual_incurr10years_miroc_rcp85
          


# Calculate the mean value for each row, excluding the first two columns
mean_Hdur_annual_inlast10years_miroc_rcp85 = (df_Hdur_annual_inlast10years_miroc_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_annual_inlast10years_miroc_rcp85['mean'] = mean_Hdur_annual_inlast10years_miroc_rcp85



#%% GlUE method without weighting 

#%%======================annual_Hdur

#%%=======rcp26


#Hdur_annual_incurr10years_rcp26

data = {
    'gfdl': mean_Hdur_annual_incurr10years_gfdl_rcp26,
    'hadgem': mean_Hdur_annual_incurr10years_hadgem_rcp26,
    'ipsl': mean_Hdur_annual_incurr10years_ipsl_rcp26,
    'miroc': mean_Hdur_annual_incurr10years_miroc_rcp26
}

# Assuming you have an index for the DataFrame
index_jz = df_Hdur_annual_incurr10years_gfdl_rcp26['jz']

# Creating the DataFrame
mean_Hdur_annual_incurr10years_rcp26 = pd.DataFrame(data)

mean_Hdur_annual_incurr10years_rcp26= mean_Hdur_annual_incurr10years_rcp26.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_Hdur_annual_incurr10years_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_Hdur_annual_incurr10years_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_Hdur_annual_incurr10years_rcp26= glue_df_mean_Hdur_annual_incurr10years_rcp26.set_index(index_jz)




#Hdur_annual_inlast10years_rcp26

data = {
    'gfdl': mean_Hdur_annual_inlast10years_gfdl_rcp26,
    'hadgem': mean_Hdur_annual_inlast10years_hadgem_rcp26,
    'ipsl': mean_Hdur_annual_inlast10years_ipsl_rcp26,
    'miroc': mean_Hdur_annual_inlast10years_miroc_rcp26
}

# Assuming you have an index for the DataFrame
index_jz = df_Hdur_annual_incurr10years_gfdl_rcp26['jz']

# Creating the DataFrame
mean_Hdur_annual_inlast10years_rcp26 = pd.DataFrame(data)

mean_Hdur_annual_inlast10years_rcp26= mean_Hdur_annual_inlast10years_rcp26.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_Hdur_annual_inlast10years_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_Hdur_annual_inlast10years_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_Hdur_annual_inlast10years_rcp26= glue_df_mean_Hdur_annual_inlast10years_rcp26.set_index(index_jz)


#%%=======rcp60

#Hdur_annual_incurr10years_rcp60

data = {
    'gfdl': mean_Hdur_annual_incurr10years_gfdl_rcp60,
    'hadgem': mean_Hdur_annual_incurr10years_hadgem_rcp60,
    'ipsl': mean_Hdur_annual_incurr10years_ipsl_rcp60,
    'miroc': mean_Hdur_annual_incurr10years_miroc_rcp60
}

# Assuming you have an index for the DataFrame
index_jz = df_Hdur_annual_incurr10years_gfdl_rcp60['jz']

# Creating the DataFrame
mean_Hdur_annual_incurr10years_rcp60 = pd.DataFrame(data)

mean_Hdur_annual_incurr10years_rcp60= mean_Hdur_annual_incurr10years_rcp60.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_Hdur_annual_incurr10years_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_Hdur_annual_incurr10years_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_Hdur_annual_incurr10years_rcp60= glue_df_mean_Hdur_annual_incurr10years_rcp60.set_index(index_jz)




#Hdur_annual_inlast10years_rcp60

data = {
    'gfdl': mean_Hdur_annual_inlast10years_gfdl_rcp60,
    'hadgem': mean_Hdur_annual_inlast10years_hadgem_rcp60,
    'ipsl': mean_Hdur_annual_inlast10years_ipsl_rcp60,
    'miroc': mean_Hdur_annual_inlast10years_miroc_rcp60
}

# Assuming you have an index for the DataFrame
index_jz = df_Hdur_annual_incurr10years_gfdl_rcp60['jz']

# Creating the DataFrame
mean_Hdur_annual_inlast10years_rcp60 = pd.DataFrame(data)

mean_Hdur_annual_inlast10years_rcp60= mean_Hdur_annual_inlast10years_rcp60.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_Hdur_annual_inlast10years_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_Hdur_annual_inlast10years_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_Hdur_annual_inlast10years_rcp60= glue_df_mean_Hdur_annual_inlast10years_rcp60.set_index(index_jz)







#%%=======rcp85

#Hdur_annual_incurr10years_rcp85

data = {
    'gfdl': mean_Hdur_annual_incurr10years_gfdl_rcp85,
    'hadgem': mean_Hdur_annual_incurr10years_hadgem_rcp85,
    'ipsl': mean_Hdur_annual_incurr10years_ipsl_rcp85,
    'miroc': mean_Hdur_annual_incurr10years_miroc_rcp85
}

# Assuming you have an index for the DataFrame
index_jz = df_Hdur_annual_incurr10years_gfdl_rcp85['jz']

# Creating the DataFrame
mean_Hdur_annual_incurr10years_rcp85 = pd.DataFrame(data)

mean_Hdur_annual_incurr10years_rcp85= mean_Hdur_annual_incurr10years_rcp85.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_Hdur_annual_incurr10years_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_Hdur_annual_incurr10years_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_Hdur_annual_incurr10years_rcp85= glue_df_mean_Hdur_annual_incurr10years_rcp85.set_index(index_jz)




#Hdur_annual_inlast10years_rcp85

data = {
    'gfdl': mean_Hdur_annual_inlast10years_gfdl_rcp85,
    'hadgem': mean_Hdur_annual_inlast10years_hadgem_rcp85,
    'ipsl': mean_Hdur_annual_inlast10years_ipsl_rcp85,
    'miroc': mean_Hdur_annual_inlast10years_miroc_rcp85
}

# Assuming you have an index for the DataFrame
index_jz = df_Hdur_annual_inlast10years_gfdl_rcp85['jz']

# Creating the DataFrame
mean_Hdur_annual_inlast10years_rcp85 = pd.DataFrame(data)

mean_Hdur_annual_inlast10years_rcp85= mean_Hdur_annual_inlast10years_rcp85.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_Hdur_annual_inlast10years_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_Hdur_annual_inlast10years_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_Hdur_annual_inlast10years_rcp85= glue_df_mean_Hdur_annual_inlast10years_rcp85.set_index(index_jz)



#%%Plotting mangement on 

#Hdur_annual

import matplotlib.pyplot as plt

# Create a figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))


# Set x-axis label for each subplot
for ax in axs:
    ax.set_xlabel('VHOD [g m$^{-3}$ d$^{-1}$]', fontsize=20)
    ax.set_ylim(0, 12)  # Set y-axis limits
    ax.set_yticks(np.arange(0, 120, 10))  # Set y-axis ticks with an interval of 2



# Plot data for RCP26
axs[0].plot(glue_df_mean_Hdur_annual_incurr10years_rcp26.index, glue_df_mean_Hdur_annual_incurr10years_rcp26['50%'], 'b', label='Median (2020-2029)')
axs[0].fill_between(glue_df_mean_Hdur_annual_incurr10years_rcp26.index, glue_df_mean_Hdur_annual_incurr10years_rcp26['5%'], glue_df_mean_Hdur_annual_incurr10years_rcp26['95%'], color='blue', alpha=0.2 ,label= '90% CI (2019-2029)')
axs[0].plot(glue_df_mean_Hdur_annual_inlast10years_rcp26.index, glue_df_mean_Hdur_annual_inlast10years_rcp26['50%'], 'r', label='Median (2090-2099)')
axs[0].fill_between(glue_df_mean_Hdur_annual_inlast10years_rcp26.index, glue_df_mean_Hdur_annual_inlast10years_rcp26['5%'], glue_df_mean_Hdur_annual_inlast10years_rcp26['95%'], color='red', alpha=0.2 ,  label= '90% CI (2090-2099)')
axs[0].set_title('RCP2.6', fontsize=18 )
axs[0].set_ylabel('Annual hypoxia duration [d year$^{-1}$]', fontsize=20)
# Plot data for RCP60
axs[1].plot(glue_df_mean_Hdur_annual_incurr10years_rcp60.index, glue_df_mean_Hdur_annual_incurr10years_rcp60['50%'], 'b')#, label='50% 2020-2029')
axs[1].fill_between(glue_df_mean_Hdur_annual_incurr10years_rcp60.index, glue_df_mean_Hdur_annual_incurr10years_rcp60['5%'], glue_df_mean_Hdur_annual_incurr10years_rcp60['95%'], color='blue', alpha=0.2)# ,label= '5-95% model bound in 2019-2029')
axs[1].plot(glue_df_mean_Hdur_annual_inlast10years_rcp60.index, glue_df_mean_Hdur_annual_inlast10years_rcp60['50%'], 'r')#, label='2090-2099')
axs[1].fill_between(glue_df_mean_Hdur_annual_inlast10years_rcp60.index, glue_df_mean_Hdur_annual_inlast10years_rcp60['5%'], glue_df_mean_Hdur_annual_inlast10years_rcp60['95%'], color='red', alpha=0.2 )#,  label= '5-95% model bound in 2090-2099')
axs[1].set_title('RCP6.0', fontsize=18 )



# Plot data for RCP85
axs[2].plot(glue_df_mean_Hdur_annual_incurr10years_rcp85.index, glue_df_mean_Hdur_annual_incurr10years_rcp85['50%'], 'b')#, label='50% 2020-2029')
axs[2].fill_between(glue_df_mean_Hdur_annual_incurr10years_rcp85.index, glue_df_mean_Hdur_annual_incurr10years_rcp85['5%'], glue_df_mean_Hdur_annual_incurr10years_rcp85['95%'], color='blue', alpha=0.2)# ,label= '5-95% model bound in 2019-2029')
axs[2].plot(glue_df_mean_Hdur_annual_inlast10years_rcp85.index, glue_df_mean_Hdur_annual_inlast10years_rcp85['50%'], 'r')#, label='2090-2099')
axs[2].fill_between(glue_df_mean_Hdur_annual_inlast10years_rcp85.index, glue_df_mean_Hdur_annual_inlast10years_rcp85['5%'], glue_df_mean_Hdur_annual_inlast10years_rcp85['95%'], color='red', alpha=0.2 )#,  label= '5-95% model bound in 2090-2099')
axs[2].set_title('RCP8.5', fontsize=18 )


for ax in axs:
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    #ax.set_ylim(0, 12)

# Adjust layout to prevent overlap
plt.tight_layout()

# Create a common legend outside the subplots
legend = fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fontsize= 20)

# Save the figure with DPI of 300, considering the extra space for the legend
plt.savefig('mangemnet_annual_Hdur_VHOD_RCPs.png', dpi=300, bbox_extra_artists=(legend,), bbox_inches='tight')




#%% Calculate the mangemnet for VHOD reduction 

   
#%%Hdur_annual

#mean_Hdur_annual_current_10_years_with_VHOD_0.55

incurr10years_Hdur_annual_rcp26=glue_df_mean_Hdur_annual_incurr10years_rcp26[glue_df_mean_Hdur_annual_incurr10years_rcp26.index==0.55]['50%']
#54.777778
incurr10years_Hdur_annual_rcp60=glue_df_mean_Hdur_annual_incurr10years_rcp60[glue_df_mean_Hdur_annual_incurr10years_rcp60.index==0.55]['50%']
#57.055556
incurr10years_Hdur_annual_rcp85=glue_df_mean_Hdur_annual_incurr10years_rcp85[glue_df_mean_Hdur_annual_incurr10years_rcp85.index==0.55]['50%']
#61.166667

#mean_Hdur_annual_last_10_years_with_VHOD_0.55

inlast10years_Hdur_annual_rcp26=glue_df_mean_Hdur_annual_inlast10years_rcp26[glue_df_mean_Hdur_annual_inlast10years_rcp26.index==0.55]['50%']
#65.222222
inlast10years_Hdur_annual_rcp60=glue_df_mean_Hdur_annual_inlast10years_rcp60[glue_df_mean_Hdur_annual_inlast10years_rcp60.index==0.55]['50%']
#73.055556
inlast10years_Hdur_annual_rcp85=glue_df_mean_Hdur_annual_inlast10years_rcp85[glue_df_mean_Hdur_annual_inlast10years_rcp85.index==0.55]['50%']
#89.166667


# required VHOD to mean_Hdur_annual_last_10_years_with_VHOD== mean_Hdur_annual_current_10_years_with_VHOD_0.55


VHOD_manage_Hdur_annual_rcp26=max(glue_df_mean_Hdur_annual_inlast10years_rcp26[glue_df_mean_Hdur_annual_inlast10years_rcp26['50%']<= float(incurr10years_Hdur_annual_rcp26) ].index)
#0.47
VHOD_manage_Hdur_annual_rcp60=max(glue_df_mean_Hdur_annual_inlast10years_rcp60[glue_df_mean_Hdur_annual_inlast10years_rcp60['50%']<= float(incurr10years_Hdur_annual_rcp60) ].index)
#0.45
VHOD_manage_Hdur_annual_rcp85=max(glue_df_mean_Hdur_annual_inlast10years_rcp85[glue_df_mean_Hdur_annual_inlast10years_rcp85['50%']<= float(incurr10years_Hdur_annual_rcp85) ].index)
#0.39

# required reduction in VHOD for managemnet 

VHOD_manage_Hdur_annual_rcp26-0.55
#-0.08
VHOD_manage_Hdur_annual_rcp60-0.55
#-0.10
VHOD_manage_Hdur_annual_rcp85-0.55
#-0.16


#%%OLD 
                           
#%%max and mean of each Ja and Jv combinations 

##################last 30 years 
#management 

df_Hdur_inlast30years_4models_manage_rcp26=(df_Hdur_inlast30years_gfdl_rcp26+df_Hdur_inlast30years_hadgem_rcp26+df_Hdur_inlast30years_ipsl_rcp26+df_Hdur_inlast30years_miroc_rcp26)/4


# Calculate the maximum value for each row, excluding the first two columns
df_max_Hdur_inlast30years_4models_manage_rcp26 = (df_Hdur_inlast30years_4models_manage_rcp26.iloc[:, 2:]).max(axis=1)

# Create a new column named 'Max' in the dataframe and assign the calculated max values
df_Hdur_inlast30years_4models_manage_rcp26['max'] = df_max_Hdur_inlast30years_4models_manage_rcp26
"""


#actual

df_Hdur_inlast30years_4models_actual_rcp26=(df_Hdur_inlast30years_gfdl_rcp26+df_Hdur_inlast30years_hadgem_rcp26+df_Hdur_inlast30years_ipsl_rcp26+df_Hdur_inlast30years_miroc_rcp26)/4


# Calculate the maximum value for each row, excluding the first two columns
df_max_Hdur_inlast30years_4models_actual_rcp26 = (df_Hdur_inlast30years_4models_actual_rcp26.iloc[:, 2:]).max(axis=1)

# Create a new column named 'Max' in the dataframe and assign the calculated max values
df_Hdur_inlast30years_4models_actual_rcp26['max'] = df_max_Hdur_inlast30years_4models_actual_rcp26
"""


##############last 10 yeras 


#management 

df_Hdur_inlast10years_4models_manage_rcp26=(df_Hdur_inlast10years_gfdl_rcp26+df_Hdur_inlast10years_hadgem_rcp26+df_Hdur_inlast10years_ipsl_rcp26+df_Hdur_inlast10years_miroc_rcp26)/4


# Calculate the mean value for each row, excluding the first two columns
df_mean_Hdur_inlast10years_4models_manage_rcp26 = (df_Hdur_inlast10years_4models_manage_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_inlast10years_4models_manage_rcp26['mean'] = df_mean_Hdur_inlast10years_4models_manage_rcp26


############current 10 years 



#management 

df_Hdur_incurr10years_4models_manage_rcp26=(df_Hdur_incurr10years_gfdl_rcp26+df_Hdur_incurr10years_hadgem_rcp26+df_Hdur_incurr10years_ipsl_rcp26+df_Hdur_incurr10years_miroc_rcp26)/4


# Calculate the maximum value for each row, excluding the first two columns
df_mean_Hdur_incurr10years_4models_manage_rcp26 = (df_Hdur_incurr10years_4models_manage_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_incurr10years_4models_manage_rcp26['mean'] = df_mean_Hdur_incurr10years_4models_manage_rcp26





#%%%%%%%%%%%%rcp60
#%% Annual Hypoxia duration :gfdl

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_gfdl_rcp60 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_gfdl_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_gfdl_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp60_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_gfdl_rcp60 = pd.concat([df_Hdur_inlast30years_gfdl_rcp60, temp_df_gfdl_rcp60_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_gfdl_rcp60 = pd.concat([df_Hdur_inlast10years_gfdl_rcp60, temp_df_gfdl_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_gfdl_rcp60 = pd.concat([df_Hdur_incurr10years_gfdl_rcp60, temp_df_gfdl_rcp60_curr_10years], ignore_index=True)




#%%%%%%%%%%%%rcp60
#%% Annual Hypoxia duration :hadgem

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_hadgem_rcp60 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_hadgem_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_hadgem_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp60_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_hadgem_rcp60 = pd.concat([df_Hdur_inlast30years_hadgem_rcp60, temp_df_hadgem_rcp60_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_hadgem_rcp60 = pd.concat([df_Hdur_inlast10years_hadgem_rcp60, temp_df_hadgem_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_hadgem_rcp60 = pd.concat([df_Hdur_incurr10years_hadgem_rcp60, temp_df_hadgem_rcp60_curr_10years], ignore_index=True)





 
#%%%%%%%%%%%%rcp60
#%% Annual Hypoxia duration :ipsl

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_ipsl_rcp60 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_ipsl_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_ipsl_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp60_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_ipsl_rcp60 = pd.concat([df_Hdur_inlast30years_ipsl_rcp60, temp_df_ipsl_rcp60_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_ipsl_rcp60 = pd.concat([df_Hdur_inlast10years_ipsl_rcp60, temp_df_ipsl_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_ipsl_rcp60 = pd.concat([df_Hdur_incurr10years_ipsl_rcp60, temp_df_ipsl_rcp60_curr_10years], ignore_index=True)



#%%%%%%%%%%%%rcp60
#%% Annual Hypoxia duration :miroc

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_miroc_rcp60 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_miroc_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_miroc_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp60_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_miroc_rcp60 = pd.concat([df_Hdur_inlast30years_miroc_rcp60, temp_df_miroc_rcp60_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_miroc_rcp60 = pd.concat([df_Hdur_inlast10years_miroc_rcp60, temp_df_miroc_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_miroc_rcp60 = pd.concat([df_Hdur_incurr10years_miroc_rcp60, temp_df_miroc_rcp60_curr_10years], ignore_index=True)



                              
#%%max and mean of each Ja and Jv combinations 

##################last 30 years 
#management 

df_Hdur_inlast30years_4models_manage_rcp60=(df_Hdur_inlast30years_gfdl_rcp60+df_Hdur_inlast30years_hadgem_rcp60+df_Hdur_inlast30years_ipsl_rcp60+df_Hdur_inlast30years_miroc_rcp60)/4


# Calculate the maximum value for each row, excluding the first two columns
df_max_Hdur_inlast30years_4models_manage_rcp60 = (df_Hdur_inlast30years_4models_manage_rcp60.iloc[:, 2:]).max(axis=1)

# Create a new column named 'Max' in the dataframe and assign the calculated max values
df_Hdur_inlast30years_4models_manage_rcp60['max'] = df_max_Hdur_inlast30years_4models_manage_rcp60
"""


#actual

df_Hdur_inlast30years_4models_actual_rcp60=(df_Hdur_inlast30years_gfdl_rcp60+df_Hdur_inlast30years_hadgem_rcp60+df_Hdur_inlast30years_ipsl_rcp60+df_Hdur_inlast30years_miroc_rcp60)/4


# Calculate the maximum value for each row, excluding the first two columns
df_max_Hdur_inlast30years_4models_actual_rcp60 = (df_Hdur_inlast30years_4models_actual_rcp60.iloc[:, 2:]).max(axis=1)

# Create a new column named 'Max' in the dataframe and assign the calculated max values
df_Hdur_inlast30years_4models_actual_rcp60['max'] = df_max_Hdur_inlast30years_4models_actual_rcp60
"""


##############last 10 yeras 


#management 

df_Hdur_inlast10years_4models_manage_rcp60=(df_Hdur_inlast10years_gfdl_rcp60+df_Hdur_inlast10years_hadgem_rcp60+df_Hdur_inlast10years_ipsl_rcp60+df_Hdur_inlast10years_miroc_rcp60)/4


# Calculate the maximum value for each row, excluding the first two columns
df_mean_Hdur_inlast10years_4models_manage_rcp60 = (df_Hdur_inlast10years_4models_manage_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_inlast10years_4models_manage_rcp60['mean'] = df_mean_Hdur_inlast10years_4models_manage_rcp60


############current 10 years 



#management 

df_Hdur_incurr10years_4models_manage_rcp60=(df_Hdur_incurr10years_gfdl_rcp60+df_Hdur_incurr10years_hadgem_rcp60+df_Hdur_incurr10years_ipsl_rcp60+df_Hdur_incurr10years_miroc_rcp60)/4


# Calculate the maximum value for each row, excluding the first two columns
df_mean_Hdur_incurr10years_4models_manage_rcp60 = (df_Hdur_incurr10years_4models_manage_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_incurr10years_4models_manage_rcp60['mean'] = df_mean_Hdur_incurr10years_4models_manage_rcp60








#%%%%%%%%%%%%rcp85
#%% Annual Hypoxia duration :gfdl

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_gfdl_rcp85 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_gfdl_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_gfdl_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp85_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_gfdl_rcp85 = pd.concat([df_Hdur_inlast30years_gfdl_rcp85, temp_df_gfdl_rcp85_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_gfdl_rcp85 = pd.concat([df_Hdur_inlast10years_gfdl_rcp85, temp_df_gfdl_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_gfdl_rcp85 = pd.concat([df_Hdur_incurr10years_gfdl_rcp85, temp_df_gfdl_rcp85_curr_10years], ignore_index=True)




#%%%%%%%%%%%%rcp85
#%% Annual Hypoxia duration :hadgem

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_hadgem_rcp85 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_hadgem_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_hadgem_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp85_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_hadgem_rcp85 = pd.concat([df_Hdur_inlast30years_hadgem_rcp85, temp_df_hadgem_rcp85_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_hadgem_rcp85 = pd.concat([df_Hdur_inlast10years_hadgem_rcp85, temp_df_hadgem_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_hadgem_rcp85 = pd.concat([df_Hdur_incurr10years_hadgem_rcp85, temp_df_hadgem_rcp85_curr_10years], ignore_index=True)





 
#%%%%%%%%%%%%rcp85
#%% Annual Hypoxia duration :ipsl

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_ipsl_rcp85 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_ipsl_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_ipsl_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp85_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_ipsl_rcp85 = pd.concat([df_Hdur_inlast30years_ipsl_rcp85, temp_df_ipsl_rcp85_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_ipsl_rcp85 = pd.concat([df_Hdur_inlast10years_ipsl_rcp85, temp_df_ipsl_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_ipsl_rcp85 = pd.concat([df_Hdur_incurr10years_ipsl_rcp85, temp_df_ipsl_rcp85_curr_10years], ignore_index=True)



#%%%%%%%%%%%%rcp85
#%% Annual Hypoxia duration :miroc

# Specify the directory where the CSV files are located


#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_C_daily_VHOD_mangement_test'

#management 
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_C_daily_mangement_test'

#actual scenario
#directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'


import os
import pandas as pd

column_names = ['jz'] + [f'AF_last_30years_{i}' for i in range(0, 30)]  # Adjust column names for each year
df_Hdur_inlast30years_miroc_rcp85 = pd.DataFrame(columns=column_names)


# last 10 years (2009-2099)
column_names = ['jz'] + [f'AF_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_inlast10years_miroc_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'AF_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_Hdur_incurr10years_miroc_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Sep_hypoxia_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        AF = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        AF_index = pd.DataFrame(AF).set_index(year)




        AF_last_30years = AF_index[AF_index.index > 2069].iloc[:, :30].values.flatten()  # Take only 30 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp85_last_30years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_30years_{i}': [AF_last_30years[i]] for i in range(0, 30)}
        })
        
        df_Hdur_inlast30years_miroc_rcp85 = pd.concat([df_Hdur_inlast30years_miroc_rcp85, temp_df_miroc_rcp85_last_30years], ignore_index=True)

        
        
        # last 10 years
        AF_last_10years = AF_index[AF_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_last_10years_{i}': [AF_last_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_inlast10years_miroc_rcp85 = pd.concat([df_Hdur_inlast10years_miroc_rcp85, temp_df_miroc_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        AF_curr_10years = AF_index[(AF_index.index > 2019) & (AF_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'AF_curr_10years_{i}': [AF_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_Hdur_incurr10years_miroc_rcp85 = pd.concat([df_Hdur_incurr10years_miroc_rcp85, temp_df_miroc_rcp85_curr_10years], ignore_index=True)



                              
#%%max and mean of each Ja and Jv combinations 

##################last 30 years 
#management 

df_Hdur_inlast30years_4models_manage_rcp85=(df_Hdur_inlast30years_gfdl_rcp85+df_Hdur_inlast30years_hadgem_rcp85+df_Hdur_inlast30years_ipsl_rcp85+df_Hdur_inlast30years_miroc_rcp85)/4


# Calculate the maximum value for each row, excluding the first two columns
df_max_Hdur_inlast30years_4models_manage_rcp85 = (df_Hdur_inlast30years_4models_manage_rcp85.iloc[:, 2:]).max(axis=1)

# Create a new column named 'Max' in the dataframe and assign the calculated max values
df_Hdur_inlast30years_4models_manage_rcp85['max'] = df_max_Hdur_inlast30years_4models_manage_rcp85
"""


#actual

df_Hdur_inlast30years_4models_actual_rcp85=(df_Hdur_inlast30years_gfdl_rcp85+df_Hdur_inlast30years_hadgem_rcp85+df_Hdur_inlast30years_ipsl_rcp85+df_Hdur_inlast30years_miroc_rcp85)/4


# Calculate the maximum value for each row, excluding the first two columns
df_max_Hdur_inlast30years_4models_actual_rcp85 = (df_Hdur_inlast30years_4models_actual_rcp85.iloc[:, 2:]).max(axis=1)

# Create a new column named 'Max' in the dataframe and assign the calculated max values
df_Hdur_inlast30years_4models_actual_rcp85['max'] = df_max_Hdur_inlast30years_4models_actual_rcp85
"""


##############last 10 yeras 


#management 

df_Hdur_inlast10years_4models_manage_rcp85=(df_Hdur_inlast10years_gfdl_rcp85+df_Hdur_inlast10years_hadgem_rcp85+df_Hdur_inlast10years_ipsl_rcp85+df_Hdur_inlast10years_miroc_rcp85)/4


# Calculate the maximum value for each row, excluding the first two columns
df_mean_Hdur_inlast10years_4models_manage_rcp85 = (df_Hdur_inlast10years_4models_manage_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_inlast10years_4models_manage_rcp85['mean'] = df_mean_Hdur_inlast10years_4models_manage_rcp85


############current 10 years 



#management 

df_Hdur_incurr10years_4models_manage_rcp85=(df_Hdur_incurr10years_gfdl_rcp85+df_Hdur_incurr10years_hadgem_rcp85+df_Hdur_incurr10years_ipsl_rcp85+df_Hdur_incurr10years_miroc_rcp85)/4


# Calculate the maximum value for each row, excluding the first two columns
df_mean_Hdur_incurr10years_4models_manage_rcp85 = (df_Hdur_incurr10years_4models_manage_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_Hdur_incurr10years_4models_manage_rcp85['mean'] = df_mean_Hdur_incurr10years_4models_manage_rcp85




















#%%Plotting

# last 30 years Max 

#RCP2.6

#RCP85
df_Hdur_inlast30years_4models_manage_rcp85['jv']

df_Hdur_inlast30years_4models_manage_rcp85['ja']

df_Hdur_inlast30years_4models_manage_rcp85['max']



#RCP60
df_Hdur_inlast30years_4models_manage_rcp60['jv']

df_Hdur_inlast30years_4models_manage_rcp60['ja']

df_Hdur_inlast30years_4models_manage_rcp60['max']




#RCP26

df_Hdur_inlast30years_4models_manage_rcp26['jv']

df_Hdur_inlast30years_4models_manage_rcp26['ja']

df_Hdur_inlast30years_4models_manage_rcp26['max']






#####last 10 yaers Mean for mangemnet prespective 


#RCP85
df_Hdur_inlast10years_4models_manage_rcp85['jz']

df_Hdur_inlast10years_4models_manage_rcp85['mean']



#RCP60
df_Hdur_inlast10years_4models_manage_rcp60['jz']

df_Hdur_inlast10years_4models_manage_rcp60['mean']




#RCP26

df_Hdur_inlast10years_4models_manage_rcp26['jz']

df_Hdur_inlast10years_4models_manage_rcp26['mean']











######current 30 years Mean from the cuurent situation according 16 behavioural sets 


#RCP85
plt.plot(df_Hdur_incurr10years_4models_manage_rcp85['jz'], df_Hdur_incurr10years_4models_manage_rcp85['mean'], 'b')

plt.plot(df_Hdur_inlast10years_4models_manage_rcp85['jz'],df_Hdur_inlast10years_4models_manage_rcp85['mean'], 'r')





#RCP60
plt.plot(df_Hdur_incurr10years_4models_manage_rcp60['jz'], df_Hdur_incurr10years_4models_manage_rcp60['mean'], 'b')

plt.plot(df_Hdur_inlast10years_4models_manage_rcp60['jz'],df_Hdur_inlast10years_4models_manage_rcp60['mean'], 'r')



#RCP26

plt.plot(df_Hdur_incurr10years_4models_manage_rcp26['jz'], df_Hdur_incurr10years_4models_manage_rcp26['mean'], 'b')

plt.plot(df_Hdur_inlast10years_4models_manage_rcp26['jz'],df_Hdur_inlast10years_4models_manage_rcp26['mean'], 'r')




#%% VHOD=0.56 the calibareted value 


df_Hdur_incurr10years_4models_manage_rcp85[df_Hdur_inlast10years_4models_manage_rcp85['jz']==0.56]['mean']# 6.59129
df_Hdur_incurr10years_4models_manage_rcp60[df_Hdur_inlast10years_4models_manage_rcp60['jz']==0.56]['mean']# 6.89892
df_Hdur_incurr10years_4models_manage_rcp26[df_Hdur_inlast10years_4models_manage_rcp26['jz']==0.56]['mean']# 6.83091




df_Hdur_inlast10years_4models_manage_rcp85[df_Hdur_inlast10years_4models_manage_rcp85['mean']<=6.59129]['jz'].max()#0.4
df_Hdur_inlast10years_4models_manage_rcp60[df_Hdur_inlast10years_4models_manage_rcp60['mean']<=6.89892]['jz'].max()#0.46
df_Hdur_inlast10years_4models_manage_rcp26[df_Hdur_inlast10years_4models_manage_rcp26['mean']<=6.83091]['jz'].max()#0.51




#%%


import matplotlib.pyplot as plt

# Create a figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Set the common y-axis label
fig.text(0.0005, 0.5, 'Hypoxia duration in May to Sep [d]', va='center', rotation='vertical')

# Set x-axis label for each subplot
for ax in axs:
    ax.set_xlabel('VHOD [g m$^{-3}$ d$^{-1}$]')
    ax.set_ylim(0, 12)  # Set y-axis limits
    ax.set_yticks(np.arange(0, 13, 2))  # Set y-axis ticks with an interval of 2



# Plot data for RCP26
axs[0].plot(df_Hdur_incurr10years_4models_manage_rcp26['jz'], df_Hdur_incurr10years_4models_manage_rcp26['mean'], 'b', label='2020-2029')
axs[0].plot(df_Hdur_inlast10years_4models_manage_rcp26['jz'], df_Hdur_inlast10years_4models_manage_rcp26['mean'], 'r', label='2090-2099')
axs[0].set_title('RCP2.6')
# Plot data for RCP60
axs[1].plot(df_Hdur_incurr10years_4models_manage_rcp60['jz'], df_Hdur_incurr10years_4models_manage_rcp60['mean'], 'b')
axs[1].plot(df_Hdur_inlast10years_4models_manage_rcp60['jz'], df_Hdur_inlast10years_4models_manage_rcp60['mean'], 'r')
axs[1].set_title('RCP6.0')
# Plot data for RCP85
axs[2].plot(df_Hdur_incurr10years_4models_manage_rcp85['jz'], df_Hdur_incurr10years_4models_manage_rcp85['mean'], 'b')
axs[2].plot(df_Hdur_inlast10years_4models_manage_rcp85['jz'], df_Hdur_inlast10years_4models_manage_rcp85['mean'], 'r')
axs[2].set_title('RCP8.5')


# Adjust layout to prevent overlap
plt.tight_layout()

# Create a common legend outside the subplots
legend = fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2)

# Save the figure with DPI of 300, considering the extra space for the legend
plt.savefig('mangemnet_VHOD_RCPs.png', dpi=300, bbox_extra_artists=(legend,), bbox_inches='tight')

# Show the plot
plt.show()





#%%
#Plotting 

#%%

#==============For max 30 years============

#%%rcp26

import matplotlib.pyplot as plt
import numpy as np

# Assuming df_Hdur_inlast30years_4models_rcp26 is your DataFrame
df = df_Hdur_inlast30years_4models_manage_rcp26

# Extracting data from DataFrame
jv_values = df['jv'].values
ja_values = df['ja'].values
max_values = df['max'].values

# Creating a contour plot with filled contours
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(jv_values, ja_values, max_values, cmap='RdYlGn_r', levels=20)

# Adding colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Maximum Hypoxia duration (2070-2100) [d]', rotation=270, labelpad=15, fontsize=14)

# Adding contour lines with values
contour_lines = plt.tricontour(jv_values, ja_values, max_values, colors='k', linewidths=0.5)

# Adding contour labels with inline text
plt.clabel(contour_lines, fmt='%1.1f', inline=True, fontsize=10)


#df_Hdur_inlast30years_4models_actual_rcp26
"""
for  index, point in df_Hdur_inlast30years_4models_actual_rcp26.iterrows():
   
    plt.scatter(point.jv, point.ja, c='k', marker='o', s=50)

# Adding a single legend entry for all specific points
plt.scatter([], [], c='k', marker='o', s=50, label='Actual scenario results')

# Adding legend for specific points outside the contour plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1) ,fontsize=14)
"""


# Adding labels and title with increased font size
plt.xlabel('Jv [g m$^{-3}$ d$^{-1}$]', fontsize=14)
plt.ylabel('Ja [g m$^{-2}$ d$^{-1}$]', fontsize=14)
plt.title('RCP2.6', fontsize=16)

# Increase the font size of x and y axis tick labels
plt.tick_params(axis='both', which='major', labelsize=12)

# Save the plot with 300 dpi resolution
#plt.savefig('max_Hdur_management_rcp26.png', dpi=300, bbox_inches='tight')
plt.savefig('max_Hdur_management_rcp26_with_actual_scenario_dots.png', dpi=300)

# Display the plot
plt.show()





#####How much reduction needed in ja nd jv 
alpha_hypo_bulk_gotm = sum(hypo_morpho_vriables_gotm_grid[2])/sum(hypo_morpho_vriables_gotm_grid[0])#

df['jz']=df ['jv']+(df ['ja'])* alpha_hypo_bulk_gotm




df [df ['max']<=6]['jv']
df [df ['max']<=6]['ja']

df[df['max']<=6]['jz']

df[df['max']<=6]['jz'].max()#0.40463380281690137

df [df ['max']<=6]['max']

df_F_L_6_rcp26= df[df['max']<=6]
#%%rcp60

import matplotlib.pyplot as plt
import numpy as np

# Assuming df_Hdur_inlast30years_4models_rcp60 is your DataFrame
df = df_Hdur_inlast30years_4models_manage_rcp60

# Extracting data from DataFrame
jv_values = df['jv'].values
ja_values = df['ja'].values
max_values = df['max'].values

# Creating a contour plot with filled contours
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(jv_values, ja_values, max_values, cmap='RdYlGn_r', levels=20)

# Adding colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Maximum Hypoxia duration (2070-2100) [d]', rotation=270, labelpad=15, fontsize=14)

# Adding contour lines with values
contour_lines = plt.tricontour(jv_values, ja_values, max_values, colors='k', linewidths=0.5)

# Adding contour labels with inline text
plt.clabel(contour_lines, fmt='%1.1f', inline=True, fontsize=10)


#df_Hdur_inlast30years_4models_actual_rcp60

for  index, point in df_Hdur_inlast30years_4models_actual_rcp60.iterrows():
   
    plt.scatter(point.jv, point.ja, c='k', marker='o', s=50)

# Adding a single legend entry for all specific points
plt.scatter([], [], c='k', marker='o', s=50, label='Actual scenario results')

# Adding legend for specific points outside the contour plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1) ,fontsize=14)



# Adding labels and title with increased font size
plt.xlabel('Jv [g m$^{-3}$ d$^{-1}$]', fontsize=14)
plt.ylabel('Ja [g m$^{-2}$ d$^{-1}$]', fontsize=14)
plt.title('RCP6.0', fontsize=16)

# Increase the font size of x and y axis tick labels
plt.tick_params(axis='both', which='major', labelsize=12)

# Save the plot with 300 dpi resolution
#plt.savefig('max_Hdur_management_rcp60.png', dpi=300, bbox_inches='tight')
plt.savefig('max_Hdur_management_rcp60_with_actual_scenario_dots.png', dpi=300)

# Display the plot
plt.show()



#####How much reduction needed in ja nd jv 
alpha_hypo_bulk_gotm = sum(hypo_morpho_vriables_gotm_grid[2])/sum(hypo_morpho_vriables_gotm_grid[0])#

df['jz']=df ['jv']+(df ['ja'])* alpha_hypo_bulk_gotm




df [df ['max']<=6]['jv']
df [df ['max']<=6]['ja']

df[df['max']<=6]['jz']

df[df['max']<=6]['jz'].max()#0.35424256651017216

df [df ['max']<=6]['max']


df_F_L_6_rcp60= df[df['max']<=6]
#%%rcp85

import matplotlib.pyplot as plt
import numpy as np

# Assuming df_Hdur_inlast30years_4models_rcp85 is your DataFrame
df = df_Hdur_inlast30years_4models_manage_rcp85

# Extracting data from DataFrame
jv_values = df['jv'].values
ja_values = df['ja'].values
max_values = df['max'].values

# Creating a contour plot with filled contours
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(jv_values, ja_values, max_values, cmap='RdYlGn_r', levels=20)

# Adding colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Maximum Hypoxia duration (2070-2100) [d]', rotation=270, labelpad=15, fontsize=14)

# Adding contour lines with values
contour_lines = plt.tricontour(jv_values, ja_values, max_values, colors='k', linewidths=0.5)

# Adding contour labels with inline text
plt.clabel(contour_lines, fmt='%1.1f', inline=True, fontsize=10)


#df_Hdur_inlast30years_4models_actual_rcp85

for  index, point in df_Hdur_inlast30years_4models_actual_rcp85.iterrows():
   
    plt.scatter(point.jv, point.ja, c='k', marker='o', s=50)

# Adding a single legend entry for all specific points
plt.scatter([], [], c='k', marker='o', s=50, label='Actual scenario results')

# Adding legend for specific points outside the contour plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1) ,fontsize=14)



# Adding labels and title with increased font size
plt.xlabel('Jv [g m$^{-3}$ d$^{-1}$]', fontsize=14)
plt.ylabel('Ja [g m$^{-2}$ d$^{-1}$]', fontsize=14)
plt.title('RCP8.5', fontsize=16)

# Increase the font size of x and y axis tick labels
plt.tick_params(axis='both', which='major', labelsize=12)

# Save the plot with 300 dpi resolution
#plt.savefig('max_Hdur_management_rcp85.png', dpi=300, bbox_inches='tight')
plt.savefig('max_Hdur_management_rcp85_with_actual_scenario_dots.png', dpi=300)

# Display the plot
plt.show()


#####How much reduction needed in ja nd jv 
alpha_hypo_bulk_gotm = sum(hypo_morpho_vriables_gotm_grid[2])/sum(hypo_morpho_vriables_gotm_grid[0])#

df['jz']=df ['jv']+(df ['ja'])* alpha_hypo_bulk_gotm




df [df ['max']<=6]['jv']
df [df ['max']<=6]['ja']

df[df['max']<=6]['jz']

df[df['max']<=6]['jz'].max()#0.35189514866979654

df [df ['max']<=6]['max']



df_F_L_6_rcp85= df[df['max']<=6]




#%%Plottting 

#%%

#================For last 10 years  and compartion with dots from current 10 years of actual simulation 

#%%rcp26


import matplotlib.pyplot as plt
import numpy as np

# Assuming df_Hdur_inlast30years_4models_rcp26 is your DataFrame
df = df_Hdur_inlast10years_4models_manage_rcp26

# Extracting data from DataFrame
jv_values = df['jv'].values
ja_values = df['ja'].values
mean_values = df['mean'].values

# Creating a contour plot with filled contours
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(jv_values, ja_values, mean_values, cmap='RdYlGn_r', levels=20)

# Adding colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Mean Hypoxia duration in 2090-2099 [d]', rotation=270, labelpad=15, fontsize=14)

# Adding contour lines with values
contour_lines = plt.tricontour(jv_values, ja_values, mean_values, colors='k', linewidths=0.5)

# Adding contour labels with inline text
plt.clabel(contour_lines, fmt='%1.1f', inline=True, fontsize=10)

# from actual values 
#df_Hdur_incurr10years_4models_manage_rcp26

for  index, point in df_Hdur_incurr10years_4models_manage_rcp26.iterrows():
   
    plt.scatter(point.jv, point.ja, c='k', marker='o', s=50)

# Adding a single legend entry for all specific points
plt.scatter([], [], c='k', marker='o', s=50, label='Actual scenario results')

# Adding legend for specific points outside the contour plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1) ,fontsize=14)



# Adding labels and title with increased font size
plt.xlabel('Jv [g m$^{-3}$ d$^{-1}$]', fontsize=14)
plt.ylabel('Ja [g m$^{-2}$ d$^{-1}$]', fontsize=14)
plt.title('RCP2.6', fontsize=16)

# Increase the font size of x and y axis tick labels
plt.tick_params(axis='both', which='major', labelsize=12)

# Save the plot with 300 dpi resolution
#plt.savefig('max_Hdur_management_rcp26.png', dpi=300, bbox_inches='tight')
plt.savefig('mean_last_10years_Hdur_management_rcp26_with_actual_scenario_dots.png', dpi=300)

# Display the plot
plt.show()





#####How much reduction needed in ja nd jv 
alpha_hypo_bulk_gotm = sum(hypo_morpho_vriables_gotm_grid[2])/sum(hypo_morpho_vriables_gotm_grid[0])#


#alpha_hypo_bulk_gotm= 0.5039123630672926

df['jz']=df ['jv']+(df ['ja'])* alpha_hypo_bulk_gotm




df [df ['mean']<=6.7]['jv']
df [df ['mean']<=6.7]['ja']

df[df['mean']<=6.7]['jz']

df[df['mean']<=6.7]['jz'].mean()

#Mean last 10 years Jz in RCP2.6 when
#is suppose to have a lower or equal value 
#of current 10 years (2020-2029):VHOD 0.3292512606503216 
# AHOD 0.16591378079718866


df [df ['mean']<=6.7]['mean']

df_F_L_6_rcp26= df[df['mean']<=6.7]


#%%rcp60


import matplotlib.pyplot as plt
import numpy as np

# Assuming df_Hdur_inlast30years_4models_rcp60 is your DataFrame
df = df_Hdur_inlast10years_4models_manage_rcp60

# Extracting data from DataFrame
jv_values = df['jv'].values
ja_values = df['ja'].values
mean_values = df['mean'].values

# Creating a contour plot with filled contours
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(jv_values, ja_values, mean_values, cmap='RdYlGn_r', levels=20)

# Adding colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Mean Hypoxia duration in 2090-2099 [d]', rotation=270, labelpad=15, fontsize=14)

# Adding contour lines with values
contour_lines = plt.tricontour(jv_values, ja_values, mean_values, colors='k', linewidths=0.5)

# Adding contour labels with inline text
plt.clabel(contour_lines, fmt='%1.1f', inline=True, fontsize=10)

# from actual values 
#df_Hdur_incurr10years_4models_manage_rcp60

for  index, point in df_Hdur_incurr10years_4models_manage_rcp60.iterrows():
   
    plt.scatter(point.jv, point.ja, c='k', marker='o', s=50)

# Adding a single legend entry for all specific points
plt.scatter([], [], c='k', marker='o', s=50, label='Actual scenario results')

# Adding legend for specific points outside the contour plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1) ,fontsize=14)



# Adding labels and title with increased font size
plt.xlabel('Jv [g m$^{-3}$ d$^{-1}$]', fontsize=14)
plt.ylabel('Ja [g m$^{-2}$ d$^{-1}$]', fontsize=14)
plt.title('RCP6.0', fontsize=16)

# Increase the font size of x and y axis tick labels
plt.tick_params(axis='both', which='major', labelsize=12)

# Save the plot with 300 dpi resolution
#plt.savefig('max_Hdur_management_rcp60.png', dpi=300, bbox_inches='tight')
plt.savefig('mean_last_10years_Hdur_management_rcp60_with_actual_scenario_dots.png', dpi=300)

# Display the plot
plt.show()





#####How much reduction needed in ja nd jv 
alpha_hypo_bulk_gotm = sum(hypo_morpho_vriables_gotm_grid[2])/sum(hypo_morpho_vriables_gotm_grid[0])#


#alpha_hypo_bulk_gotm= 0.5039123630672926

df['jz']=df ['jv']+(df ['ja'])* alpha_hypo_bulk_gotm




df [df ['mean']<=6.6]['jv']
df [df ['mean']<=6.6]['ja']

df[df['mean']<=6.6]['jz']

df[df['mean']<=6.6]['jz'].mean()


#Mean last 10 years Jz in RCP2.6 when
#is suppose to have a lower or equal value 
#of current 10 years (2020-2029):VHOD 0.29440949400104327
#AHOD 0.14835658383151162


df [df ['mean']<=6.6]['mean']

df_F_L_6_rcp60= df[df['mean']<=6.6]

#%%rcp85


import matplotlib.pyplot as plt
import numpy as np

# Assuming df_Hdur_inlast30years_4models_rcp85 is your DataFrame
df = df_Hdur_inlast10years_4models_manage_rcp85

# Extracting data from DataFrame
jv_values = df['jv'].values
ja_values = df['ja'].values
mean_values = df['mean'].values

# Creating a contour plot with filled contours
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(jv_values, ja_values, mean_values, cmap='RdYlGn_r', levels=20)

# Adding colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Mean Hypoxia duration in 2090-2099 [d]', rotation=270, labelpad=15, fontsize=14)

# Adding contour lines with values
contour_lines = plt.tricontour(jv_values, ja_values, mean_values, colors='k', linewidths=0.5)

# Adding contour labels with inline text
plt.clabel(contour_lines, fmt='%1.1f', inline=True, fontsize=10)

# from actual values 
#df_Hdur_incurr10years_4models_manage_rcp85

for  index, point in df_Hdur_incurr10years_4models_manage_rcp85.iterrows():
   
    plt.scatter(point.jv, point.ja, c='k', marker='o', s=50)

# Adding a single legend entry for all specific points
plt.scatter([], [], c='k', marker='o', s=50, label='Actual scenario results')

# Adding legend for specific points outside the contour plot
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1) ,fontsize=14)



# Adding labels and title with increased font size
plt.xlabel('Jv [g m$^{-3}$ d$^{-1}$]', fontsize=14)
plt.ylabel('Ja [g m$^{-2}$ d$^{-1}$]', fontsize=14)
plt.title('RCP8.5', fontsize=16)

# Increase the font size of x and y axis tick labels
plt.tick_params(axis='both', which='major', labelsize=12)

# Save the plot with 300 dpi resolution
#plt.savefig('max_Hdur_management_rcp85.png', dpi=300, bbox_inches='tight')
plt.savefig('mean_last_10years_Hdur_management_rcp85_with_actual_scenario_dots.png', dpi=300)

# Display the plot
plt.show()





#####How much reduction needed in ja nd jv 
alpha_hypo_bulk_gotm = sum(hypo_morpho_vriables_gotm_grid[2])/sum(hypo_morpho_vriables_gotm_grid[0])#


#alpha_hypo_bulk_gotm= 0.5039123630672926

df['jz']=df ['jv']+(df ['ja'])* alpha_hypo_bulk_gotm




df [df ['mean']<=6.4]['jv']
df [df ['mean']<=6.4]['ja']

df[df['mean']<=6.4]['jz']

df[df['mean']<=6.4]['jz'].mean()


#Mean last 10 years Jz in RCP2.6 when
#is suppose to have a lower or equal value 
#of current 10 years (2020-2029):
    
#Jz or VHOD 0.22748200312989045


# AHOD 0.11463099375246434

df [df ['mean']<=6.4]['mean']

df_F_L_6_rcp85= df[df['mean']<=6.4]



