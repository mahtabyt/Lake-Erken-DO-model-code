# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:43:54 2024

@author: mahta
"""
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
#%%rcp26

# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp26_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_gfdl_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
               
# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp26_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_hadgem_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                

# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp26_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_ipsl_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                
        
# Specify the directory where the CSV files are located


directory= 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp26_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_miroc_rcp26_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                        
        
#%%rcp60

# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp60_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_gfdl_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                
# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp60_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_hadgem_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                

# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp60_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_ipsl_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                
        
# Specify the directory where the CSV files are located


directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp60_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_miroc_rcp60_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                                    
#%%rcp85

# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_gfdl_rcp85_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_gfdl_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                
# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_hadgem_rcp85_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_hadgem_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                

# Specify the directory where the CSV files are located

directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_ipsl_rcp85_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_ipsl_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                
        
# Specify the directory where the CSV files are located


directory='C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_C_daily_VHOD_mangement_test'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_DO_prof_miroc_rcp85_Jz_"):
        
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        
        # Read the DataFrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])

        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        result_sum=result.sum(axis=1)
        # Round Ja and Jv to 3 decimal places
        Jz_name = round(jz_value, 3)
        
        
        header_values = {'Jz': jz_value }

        
        # Save the dep_rate to a new CSV file
        result_filename = f'sum_annual_anaerobic_duration_miroc_rcp85_Jz_{Jz_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result_sum.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
                    
      
#%% extracting last 10 years and current 10 years 

#%%==================gfdl====================

#%% gfdl_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_gfdl_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_gfdl_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_gfdl_rcp26 = pd.concat([df_sum_anaerobic_dur_inlast10years_gfdl_rcp26, temp_df_gfdl_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_gfdl_rcp26 = pd.concat([df_sum_anaerobic_dur_incurr10years_gfdl_rcp26, temp_df_gfdl_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_gfdl_rcp26 = (df_sum_anaerobic_dur_incurr10years_gfdl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_gfdl_rcp26['mean'] = mean_sum_anaerobic_dur_incurr10years_gfdl_rcp26
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_gfdl_rcp26 = (df_sum_anaerobic_dur_inlast10years_gfdl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_gfdl_rcp26['mean'] = mean_sum_anaerobic_dur_inlast10years_gfdl_rcp26


#%% gfdl_rcp60

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_gfdl_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_gfdl_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_gfdl_rcp60 = pd.concat([df_sum_anaerobic_dur_inlast10years_gfdl_rcp60, temp_df_gfdl_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_gfdl_rcp60 = pd.concat([df_sum_anaerobic_dur_incurr10years_gfdl_rcp60, temp_df_gfdl_rcp60_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_gfdl_rcp60 = (df_sum_anaerobic_dur_incurr10years_gfdl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_gfdl_rcp60['mean'] = mean_sum_anaerobic_dur_incurr10years_gfdl_rcp60
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_gfdl_rcp60 = (df_sum_anaerobic_dur_inlast10years_gfdl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_gfdl_rcp60['mean'] = mean_sum_anaerobic_dur_inlast10years_gfdl_rcp60

#%% gfdl_rcp85

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_gfdl_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_gfdl_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_gfdl_rcp85 = pd.concat([df_sum_anaerobic_dur_inlast10years_gfdl_rcp85, temp_df_gfdl_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_gfdl_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_gfdl_rcp85 = pd.concat([df_sum_anaerobic_dur_incurr10years_gfdl_rcp85, temp_df_gfdl_rcp85_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_gfdl_rcp85 = (df_sum_anaerobic_dur_incurr10years_gfdl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_gfdl_rcp85['mean'] = mean_sum_anaerobic_dur_incurr10years_gfdl_rcp85
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_gfdl_rcp85 = (df_sum_anaerobic_dur_inlast10years_gfdl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_gfdl_rcp85['mean'] = mean_sum_anaerobic_dur_inlast10years_gfdl_rcp85



#%%==================hadgem====================

#%% hadgem_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_hadgem_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_hadgem_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_hadgem_rcp26 = pd.concat([df_sum_anaerobic_dur_inlast10years_hadgem_rcp26, temp_df_hadgem_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_hadgem_rcp26 = pd.concat([df_sum_anaerobic_dur_incurr10years_hadgem_rcp26, temp_df_hadgem_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_hadgem_rcp26 = (df_sum_anaerobic_dur_incurr10years_hadgem_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_hadgem_rcp26['mean'] = mean_sum_anaerobic_dur_incurr10years_hadgem_rcp26
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_hadgem_rcp26 = (df_sum_anaerobic_dur_inlast10years_hadgem_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_hadgem_rcp26['mean'] = mean_sum_anaerobic_dur_inlast10years_hadgem_rcp26


#%% hadgem_rcp60

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_hadgem_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_hadgem_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_hadgem_rcp60 = pd.concat([df_sum_anaerobic_dur_inlast10years_hadgem_rcp60, temp_df_hadgem_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_hadgem_rcp60 = pd.concat([df_sum_anaerobic_dur_incurr10years_hadgem_rcp60, temp_df_hadgem_rcp60_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_hadgem_rcp60 = (df_sum_anaerobic_dur_incurr10years_hadgem_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_hadgem_rcp60['mean'] = mean_sum_anaerobic_dur_incurr10years_hadgem_rcp60
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_hadgem_rcp60 = (df_sum_anaerobic_dur_inlast10years_hadgem_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_hadgem_rcp60['mean'] = mean_sum_anaerobic_dur_inlast10years_hadgem_rcp60

#%% hadgem_rcp85

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_hadgem_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_hadgem_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_hadgem_rcp85 = pd.concat([df_sum_anaerobic_dur_inlast10years_hadgem_rcp85, temp_df_hadgem_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_hadgem_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_hadgem_rcp85 = pd.concat([df_sum_anaerobic_dur_incurr10years_hadgem_rcp85, temp_df_hadgem_rcp85_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_hadgem_rcp85 = (df_sum_anaerobic_dur_incurr10years_hadgem_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_hadgem_rcp85['mean'] = mean_sum_anaerobic_dur_incurr10years_hadgem_rcp85
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_hadgem_rcp85 = (df_sum_anaerobic_dur_inlast10years_hadgem_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_hadgem_rcp85['mean'] = mean_sum_anaerobic_dur_inlast10years_hadgem_rcp85


#%%==================ipsl====================

#%% ipsl_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_ipsl_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_ipsl_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_ipsl_rcp26 = pd.concat([df_sum_anaerobic_dur_inlast10years_ipsl_rcp26, temp_df_ipsl_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_ipsl_rcp26 = pd.concat([df_sum_anaerobic_dur_incurr10years_ipsl_rcp26, temp_df_ipsl_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_ipsl_rcp26 = (df_sum_anaerobic_dur_incurr10years_ipsl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_ipsl_rcp26['mean'] = mean_sum_anaerobic_dur_incurr10years_ipsl_rcp26
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_ipsl_rcp26 = (df_sum_anaerobic_dur_inlast10years_ipsl_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_ipsl_rcp26['mean'] = mean_sum_anaerobic_dur_inlast10years_ipsl_rcp26


#%% ipsl_rcp60

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_ipsl_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_ipsl_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_ipsl_rcp60 = pd.concat([df_sum_anaerobic_dur_inlast10years_ipsl_rcp60, temp_df_ipsl_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_ipsl_rcp60 = pd.concat([df_sum_anaerobic_dur_incurr10years_ipsl_rcp60, temp_df_ipsl_rcp60_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_ipsl_rcp60 = (df_sum_anaerobic_dur_incurr10years_ipsl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_ipsl_rcp60['mean'] = mean_sum_anaerobic_dur_incurr10years_ipsl_rcp60
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_ipsl_rcp60 = (df_sum_anaerobic_dur_inlast10years_ipsl_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_ipsl_rcp60['mean'] = mean_sum_anaerobic_dur_inlast10years_ipsl_rcp60

#%% ipsl_rcp85

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_ipsl_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_ipsl_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_ipsl_rcp85 = pd.concat([df_sum_anaerobic_dur_inlast10years_ipsl_rcp85, temp_df_ipsl_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_ipsl_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_ipsl_rcp85 = pd.concat([df_sum_anaerobic_dur_incurr10years_ipsl_rcp85, temp_df_ipsl_rcp85_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_ipsl_rcp85 = (df_sum_anaerobic_dur_incurr10years_ipsl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_ipsl_rcp85['mean'] = mean_sum_anaerobic_dur_incurr10years_ipsl_rcp85
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_ipsl_rcp85 = (df_sum_anaerobic_dur_inlast10years_ipsl_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_ipsl_rcp85['mean'] = mean_sum_anaerobic_dur_inlast10years_ipsl_rcp85


#%%==================miroc====================

#%% miroc_rcp26

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_miroc_rcp26 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_miroc_rcp26 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp26_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_miroc_rcp26 = pd.concat([df_sum_anaerobic_dur_inlast10years_miroc_rcp26, temp_df_miroc_rcp26_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp26_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_miroc_rcp26 = pd.concat([df_sum_anaerobic_dur_incurr10years_miroc_rcp26, temp_df_miroc_rcp26_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_miroc_rcp26 = (df_sum_anaerobic_dur_incurr10years_miroc_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_miroc_rcp26['mean'] = mean_sum_anaerobic_dur_incurr10years_miroc_rcp26
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_miroc_rcp26 = (df_sum_anaerobic_dur_inlast10years_miroc_rcp26.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_miroc_rcp26['mean'] = mean_sum_anaerobic_dur_inlast10years_miroc_rcp26


#%% miroc_rcp60

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_miroc_rcp60 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_miroc_rcp60 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp60_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_miroc_rcp60 = pd.concat([df_sum_anaerobic_dur_inlast10years_miroc_rcp60, temp_df_miroc_rcp60_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp60_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_miroc_rcp60 = pd.concat([df_sum_anaerobic_dur_incurr10years_miroc_rcp60, temp_df_miroc_rcp60_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_miroc_rcp60 = (df_sum_anaerobic_dur_incurr10years_miroc_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_miroc_rcp60['mean'] = mean_sum_anaerobic_dur_incurr10years_miroc_rcp60
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_miroc_rcp60 = (df_sum_anaerobic_dur_inlast10years_miroc_rcp60.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_miroc_rcp60['mean'] = mean_sum_anaerobic_dur_inlast10years_miroc_rcp60


#%% miroc_rcp85

import os
import pandas as pd

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85_C_daily_VHOD_mangement_test'
os.chdir(directory)

# last 10 years (2009-2099)

column_names = ['jz'] + [f'sum_anaerobic_dur_last_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_inlast10years_miroc_rcp85 = pd.DataFrame(columns=column_names)


# current 10 years 
column_names = ['jz'] + [f'sum_anaerobic_dur_curr_10years_{i}' for i in range(0, 10)]  # Adjust column names for each year
df_sum_anaerobic_dur_incurr10years_miroc_rcp85 = pd.DataFrame(columns=column_names)



# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("sum_annual_anaerobic_duration"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jz_value = read_header_df['Jz'].iloc[0]
        

        # Read the Datdo_annualrame below the header
        read_data_df = pd.read_csv(os.path.join(directory, filename), skiprows=2)

        # Extract relevant columns (adjust column names accordingly)
        do_annual = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        year = read_data_df['year']
        anaerobic_dur_index = pd.DataFrame(do_annual).set_index(year)




        
        # last 10 years
        anaerobic_dur_last_10years = anaerobic_dur_index[anaerobic_dur_index.index > 2089].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp85_last_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_last_10years_{i}': [anaerobic_dur_last_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_inlast10years_miroc_rcp85 = pd.concat([df_sum_anaerobic_dur_inlast10years_miroc_rcp85, temp_df_miroc_rcp85_last_10years], ignore_index=True)
        


        #current 10 years # Extract current 10 years'(2020-2029) data
        anaerobic_dur_curr_10years = anaerobic_dur_index[(anaerobic_dur_index.index > 2019) & (anaerobic_dur_index.index< 2030)].iloc[:, :10].values.flatten()  # Take only 10 years and flatten to a 1D array
        # Append results for each iteration
        temp_df_miroc_rcp85_curr_10years = pd.DataFrame({
            'jz': [jz_value],
            **{f'sum_anaerobic_dur_curr_10years_{i}': [anaerobic_dur_curr_10years[i]] for i in range(0, 10)}
        })
        
        df_sum_anaerobic_dur_incurr10years_miroc_rcp85 = pd.concat([df_sum_anaerobic_dur_incurr10years_miroc_rcp85, temp_df_miroc_rcp85_curr_10years], ignore_index=True)



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_incurr10years_miroc_rcp85 = (df_sum_anaerobic_dur_incurr10years_miroc_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_incurr10years_miroc_rcp85['mean'] = mean_sum_anaerobic_dur_incurr10years_miroc_rcp85
          



# Calculate the mean value for each row, excluding the first two columns
mean_sum_anaerobic_dur_inlast10years_miroc_rcp85 = (df_sum_anaerobic_dur_inlast10years_miroc_rcp85.iloc[:, 2:]).mean(axis=1)

# Create a new column named 'Mean' in the dataframe and assign the calculated max values
df_sum_anaerobic_dur_inlast10years_miroc_rcp85['mean'] = mean_sum_anaerobic_dur_inlast10years_miroc_rcp85


#%% GlUE method without weighting 

#%%======================sum_anaerobic_dur

#%%=======rcp26


#sum_anaerobic_dur_incurr10years_rcp26

data = {
    'gfdl': mean_sum_anaerobic_dur_incurr10years_gfdl_rcp26,
    'hadgem': mean_sum_anaerobic_dur_incurr10years_hadgem_rcp26,
    'ipsl': mean_sum_anaerobic_dur_incurr10years_ipsl_rcp26,
    'miroc': mean_sum_anaerobic_dur_incurr10years_miroc_rcp26
}

# Assuming you have an index for the DataFrame
index_jz = df_sum_anaerobic_dur_inlast10years_miroc_rcp85['jz']

# Creating the DataFrame
mean_sum_anaerobic_dur_incurr10years_rcp26 = pd.DataFrame(data)

mean_sum_anaerobic_dur_incurr10years_rcp26= mean_sum_anaerobic_dur_incurr10years_rcp26.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_sum_anaerobic_dur_incurr10years_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26= glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26.set_index(index_jz)




data = {
    'gfdl': mean_sum_anaerobic_dur_inlast10years_gfdl_rcp26,
    'hadgem': mean_sum_anaerobic_dur_inlast10years_hadgem_rcp26,
    'ipsl': mean_sum_anaerobic_dur_inlast10years_ipsl_rcp26,
    'miroc': mean_sum_anaerobic_dur_inlast10years_miroc_rcp26
}

# Assuming you have an index for the DataFrame
index_jz = df_sum_anaerobic_dur_inlast10years_miroc_rcp85['jz']

# Creating the DataFrame
mean_sum_anaerobic_dur_inlast10years_rcp26 = pd.DataFrame(data)

mean_sum_anaerobic_dur_inlast10years_rcp26= mean_sum_anaerobic_dur_inlast10years_rcp26.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_sum_anaerobic_dur_inlast10years_rcp26.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26= glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26.set_index(index_jz)

#%%=======rcp60

#sum_anaerobic_dur_incurr10years_rcp60

data = {
    'gfdl': mean_sum_anaerobic_dur_incurr10years_gfdl_rcp60,
    'hadgem': mean_sum_anaerobic_dur_incurr10years_hadgem_rcp60,
    'ipsl': mean_sum_anaerobic_dur_incurr10years_ipsl_rcp60,
    'miroc': mean_sum_anaerobic_dur_incurr10years_miroc_rcp60
}

# Assuming you have an index for the DataFrame
index_jz = df_sum_anaerobic_dur_inlast10years_miroc_rcp85['jz']

# Creating the DataFrame
mean_sum_anaerobic_dur_incurr10years_rcp60 = pd.DataFrame(data)

mean_sum_anaerobic_dur_incurr10years_rcp60= mean_sum_anaerobic_dur_incurr10years_rcp60.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_sum_anaerobic_dur_incurr10years_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60= glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60.set_index(index_jz)




data = {
    'gfdl': mean_sum_anaerobic_dur_inlast10years_gfdl_rcp60,
    'hadgem': mean_sum_anaerobic_dur_inlast10years_hadgem_rcp60,
    'ipsl': mean_sum_anaerobic_dur_inlast10years_ipsl_rcp60,
    'miroc': mean_sum_anaerobic_dur_inlast10years_miroc_rcp60
}

# Assuming you have an index for the DataFrame
index_jz = df_sum_anaerobic_dur_inlast10years_miroc_rcp85['jz']

# Creating the DataFrame
mean_sum_anaerobic_dur_inlast10years_rcp60 = pd.DataFrame(data)

mean_sum_anaerobic_dur_inlast10years_rcp60= mean_sum_anaerobic_dur_inlast10years_rcp60.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_sum_anaerobic_dur_inlast10years_rcp60.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60= glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60.set_index(index_jz)

#%%=================rcp85
#sum_anaerobic_dur_incurr10years_rcp85

data = {
    'gfdl': mean_sum_anaerobic_dur_incurr10years_gfdl_rcp85,
    'hadgem': mean_sum_anaerobic_dur_incurr10years_hadgem_rcp85,
    'ipsl': mean_sum_anaerobic_dur_incurr10years_ipsl_rcp85,
    'miroc': mean_sum_anaerobic_dur_incurr10years_miroc_rcp85
}

# Assuming you have an index for the DataFrame
index_jz = df_sum_anaerobic_dur_inlast10years_miroc_rcp85['jz']

# Creating the DataFrame
mean_sum_anaerobic_dur_incurr10years_rcp85 = pd.DataFrame(data)

mean_sum_anaerobic_dur_incurr10years_rcp85= mean_sum_anaerobic_dur_incurr10years_rcp85.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_sum_anaerobic_dur_incurr10years_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85= glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85.set_index(index_jz)




data = {
    'gfdl': mean_sum_anaerobic_dur_inlast10years_gfdl_rcp85,
    'hadgem': mean_sum_anaerobic_dur_inlast10years_hadgem_rcp85,
    'ipsl': mean_sum_anaerobic_dur_inlast10years_ipsl_rcp85,
    'miroc': mean_sum_anaerobic_dur_inlast10years_miroc_rcp85
}

# Assuming you have an index for the DataFrame
index_jz = df_sum_anaerobic_dur_inlast10years_miroc_rcp85['jz']

# Creating the DataFrame
mean_sum_anaerobic_dur_inlast10years_rcp85 = pd.DataFrame(data)

mean_sum_anaerobic_dur_inlast10years_rcp85= mean_sum_anaerobic_dur_inlast10years_rcp85.set_index(index_jz)


#GLUE

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in mean_sum_anaerobic_dur_inlast10years_rcp85.iterrows():# for each timesteps
    values = row    
    out.append(weighted_quantiles(values, quants))

    # Build df
    glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85= glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85.set_index(index_jz)



#%%Plotting mangement on 

#management VHOD
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models'
os.chdir(directory)

#dep_rate

import matplotlib.pyplot as plt

# Create a figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))#, sharey=True)


# Set x-axis label for each subplot
for ax in axs:
    ax.set_xlabel('VHOD [g m$^{-3}$ d$^{-1}$]', fontsize=20)
    ax.set_ylim(0, 1400)  # Set y-axis limits
    #ax.set_yticks(np.arange(0, 15, 2))  # Set y-axis ticks with an interval of 2



# Plot data for RCP26
axs[0].plot(glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26.index, glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26['50%'], 'b', label='Median (2020-2029)')
axs[0].fill_between(glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26.index, glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26['5%'], glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26['95%'], color='blue', alpha=0.2 ,label= '90% CI (2019-2029)')
axs[0].plot(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26.index, glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26['50%'], 'r', label='Median (2090-2099)')
axs[0].fill_between(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26.index, glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26['5%'], glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26['95%'], color='red', alpha=0.2 ,  label= '90% CI (2090-2099)')
axs[0].set_title('RCP2.6', fontsize=18 )
axs[0].set_ylabel('Profile sum of annual anaerobic duration [d]', fontsize=20)
# Plot data for RCP60
axs[1].plot(glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60.index, glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60['50%'], 'b')#, label='50% 2020-2029')
axs[1].fill_between(glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60.index, glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60['5%'], glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60['95%'], color='blue', alpha=0.2)# ,label= '5-95% model bound in 2019-2029')
axs[1].plot(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60.index, glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60['50%'], 'r')#, label='2090-2099')
axs[1].fill_between(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60.index, glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60['5%'], glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60['95%'], color='red', alpha=0.2 )#,  label= '5-95% model bound in 2090-2099')
axs[1].set_title('RCP6.0', fontsize=18 )



# Plot data for RCP85
axs[2].plot(glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85.index, glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85['50%'], 'b')#, label='50% 2020-2029')
axs[2].fill_between(glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85.index, glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85['5%'], glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85['95%'], color='blue', alpha=0.2)# ,label= '5-95% model bound in 2019-2029')
axs[2].plot(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85.index, glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85['50%'], 'r')#, label='2090-2099')
axs[2].fill_between(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85.index, glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85['5%'], glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85['95%'], color='red', alpha=0.2 )#,  label= '5-95% model bound in 2090-2099')
axs[2].set_title('RCP8.5', fontsize=18 )


for ax in axs:
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_ylim(0, 1400)
# Adjust layout to prevent overlap
plt.tight_layout()

# Create a common legend outside the subplots
legend = fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2, fontsize= 20)

# Save the figure with DPI of 300, considering the extra space for the legend
plt.savefig('mangemnet_sum_anaerobic_dur_VHOD_RCPs.png', dpi=300, bbox_extra_artists=(legend,), bbox_inches='tight')


#%% Calculate the mangemnet for VHOD reduction 

#%%dep_rate

#mean_sum_anaerobic_dur_current_10_years_with_VHOD_0.55

incurr10years_sum_anaerobic_dur_rcp26=glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26[glue_df_mean_sum_anaerobic_dur_incurr10years_rcp26.index==0.55]['50%']
#663.944444
incurr10years_sum_anaerobic_dur_rcp60=glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60[glue_df_mean_sum_anaerobic_dur_incurr10years_rcp60.index==0.55]['50%']
#693.277778
incurr10years_sum_anaerobic_dur_rcp85=glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85[glue_df_mean_sum_anaerobic_dur_incurr10years_rcp85.index==0.55]['50%']
#752.5

#mean_sum_anaerobic_dur_last_10_years_with_VHOD_0.55

inlast10years_sum_anaerobic_dur_rcp26=glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26[glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26.index==0.55]['50%']
#807.833333
inlast10years_sum_anaerobic_dur_rcp60=glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60[glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60.index==0.55]['50%']
#919.833333
inlast10years_sum_anaerobic_dur_rcp85=glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85[glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85.index==0.55]['50%']
#1135.666667


# required VHOD to mean_sum_anaerobic_dur_last_10_years_with_VHOD== mean_sum_anaerobic_dur_current_10_years_with_VHOD_0.55


VHOD_manage_sum_anaerobic_dur_rcp26=max(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26[glue_df_mean_sum_anaerobic_dur_inlast10years_rcp26['50%']<= float(incurr10years_sum_anaerobic_dur_rcp26) ].index)
#0.48
VHOD_manage_sum_anaerobic_dur_rcp60=max(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60[glue_df_mean_sum_anaerobic_dur_inlast10years_rcp60['50%']<= float(incurr10years_sum_anaerobic_dur_rcp60) ].index)
#0.45
VHOD_manage_sum_anaerobic_dur_rcp85=max(glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85[glue_df_mean_sum_anaerobic_dur_inlast10years_rcp85['50%']<= float(incurr10years_sum_anaerobic_dur_rcp85) ].index)
#0.4

# required reduction in VHOD for managemnet 

VHOD_manage_sum_anaerobic_dur_rcp26-0.55
#-0.07
VHOD_manage_sum_anaerobic_dur_rcp60-0.55
#-0.1
VHOD_manage_sum_anaerobic_dur_rcp85-0.55
#-0.15





