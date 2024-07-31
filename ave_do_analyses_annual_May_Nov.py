# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:51:59 2024

@author: mahta
"""


#%% annual hypolimnetic_ave_his

all_annual_do_his=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_his = pd.concat([all_annual_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_his = pd.concat([all_annual_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_his = pd.concat([all_annual_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_his = pd.concat([all_annual_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_annual_do_his

anova_annual_do_his=annova_uncertainity(all_annual_do_his)

anova_annual_do_his.describe().loc['mean', :]
"""
GCMs             72.459544
param            26.953894
interaction       0.586562
GCMs/param        8.260193
year           1933.000000
Name: mean, dtype: float64
"""


anova_annual_do_his.describe().loc['std', :]
"""
GCMs           23.133600
param          23.094532
interaction     0.367664
GCMs/param     15.564964
year           42.001984
Name: std, dtype: float64
"""





#%% GLUE method on all_annual_do_his 
          

        
#all_annual_do_his= all_annual_do_his.set_index(all_annual_do_his['Datetime'])


# annual anoxic duration  
timeseries_year_his= all_annual_do_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_do_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_annual_hypolimnetic_ave_his.csv')
        




#%%


#%% May_Nov hypolimnetic_ave_his

all_May_Nov_do_his=pd.DataFrame([])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_his = pd.concat([all_May_Nov_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_his = pd.concat([all_May_Nov_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_his = pd.concat([all_May_Nov_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_his = pd.concat([all_May_Nov_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_May_Nov_do_his

anova_May_Nov_do_his=annova_uncertainity(all_May_Nov_do_his)

anova_May_Nov_do_his.describe().loc['mean', :]
"""
GCMs             83.096621
param            15.981735
interaction       0.921644
GCMs/param       14.028110
year           1933.000000
Name: mean, dtype: float6
"""


anova_May_Nov_do_his.describe().loc['std', :]
"""
GCMs           16.223553
param          15.102593
interaction     1.546537
GCMs/param     20.177495
year           42.001984
Name: std, dtype: float64
"""




#%% GLUE method on all_May_Nov_do_his 
          

        
#all_May_Nov_do_his= all_May_Nov_do_his.set_index(all_May_Nov_do_his['Datetime'])


# May_Nov anoxic duration  
timeseries_year_his= all_May_Nov_do_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_do_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_his=glue_df_May_Nov_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_May_Nov_hypolimnetic_ave_his.csv')
        


#%% summer hypolimnetic_ave_his
"""
all_summer_do_his=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_his = pd.concat([all_summer_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_his = pd.concat([all_summer_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_his = pd.concat([all_summer_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_his = pd.concat([all_summer_do_his , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_summer_do_his

anova_summer_do_his=annova_uncertainity(all_summer_do_his)

anova_summer_do_his.describe().loc['mean', :]
"""
GCMs             69.078802
param            29.748975
interaction       1.172223
GCMs/param        7.618359
year           1933.000000
Name: mean, dtype: float64
"""


anova_summer_do_his.describe().loc['std', :]
"""
GCMs           22.984311
param          22.439665
interaction     1.093608
GCMs/param     16.724656
year           42.001984
Name: std, dtype: float64
"""



#%% GLUE method on all_summer_do_his 
          

        
#all_summer_do_his= all_summer_do_his.set_index(all_summer_do_his['Datetime'])


# summer anoxic duration  
timeseries_year_his= all_summer_do_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_do_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_summer_hypolimnetic_ave_his.csv')
        
"""

#%% annual hypolimnetic_ave_rcp26

all_annual_do_rcp26=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp26 = pd.concat([all_annual_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp26 = pd.concat([all_annual_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp26 = pd.concat([all_annual_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp26 = pd.concat([all_annual_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_annual_do_rcp26

anova_annual_do_rcp26=annova_uncertainity(all_annual_do_rcp26)

anova_annual_do_rcp26.describe().loc['mean', :]
"""
GCMs             72.654117
param            26.716640
interaction       0.629243
GCMs/param        5.024947
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_do_rcp26.describe().loc['std', :]
"""
GCMs           17.236089
param          17.229883
interaction     0.387267
GCMs/param      5.218334
year           27.279418
Name: std, dtype: float64
"""
#80 years:
anova_annual_80years_AF_rcp26=annova_uncertainity(all_annual_do_rcp26[all_annual_do_rcp26.index>2019])


anova_annual_80years_AF_rcp26.describe().loc['mean', :]
"""
GCMs             74.187974
param            25.168550
interaction       0.643476
GCMs/param        5.418013
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_AF_rcp26.describe().loc['std', :]

"""
GCMs           16.443271
param          16.399948
interaction     0.404390
GCMs/param      5.492773
year           23.237900
Name: std, dtype: float64

"""


#%% GLUE method on all_annual_do_rcp26 
          

        
#all_annual_do_rcp26= all_annual_do_rcp26.set_index(all_annual_do_rcp26['Datetime'])


# annual anoxic duration  
timeseries_year_rcp26= all_annual_do_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_annual_hypolimnetic_ave_rcp26.csv')
        

#%% May_Nov hypolimnetic_ave_rcp26

all_May_Nov_do_rcp26=pd.DataFrame([])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp26 = pd.concat([all_May_Nov_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp26 = pd.concat([all_May_Nov_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp26 = pd.concat([all_May_Nov_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp26 = pd.concat([all_May_Nov_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_May_Nov_do_rcp26

anova_May_Nov_do_rcp26=annova_uncertainity(all_May_Nov_do_rcp26)

anova_May_Nov_do_rcp26.describe().loc['mean', :]
"""
GCMs             80.833547
param            18.370069
interaction       0.796384
GCMs/param        8.580787
year           2052.500000
Name: mean, dtype: float64
"""


anova_May_Nov_do_rcp26.describe().loc['std', :]
"""
GCMs           14.976681
param          14.375212
interaction     0.906969
GCMs/param      9.014452
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_May_Nov_80years_AF_rcp26=annova_uncertainity(all_May_Nov_do_rcp26[all_May_Nov_do_rcp26.index>2019])


anova_May_Nov_80years_AF_rcp26.describe().loc['mean', :]
"""
GCMs             82.165576
param            17.099085
interaction       0.735339
GCMs/param        9.154025
year           2059.500000
Name: mean, dtype: float64
"""


anova_May_Nov_80years_AF_rcp26.describe().loc['std', :]

"""
GCMs           13.703266
param          13.290064
interaction     0.726849
GCMs/param      9.473476
year           23.237900
Name: std, dtype: float64

"""




#%% GLUE method on all_May_Nov_do_rcp26 
          

        
#all_May_Nov_do_rcp26= all_May_Nov_do_rcp26.set_index(all_May_Nov_do_rcp26['Datetime'])


# May_Nov anoxic duration  
timeseries_year_rcp26= all_May_Nov_do_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_May_Nov_hypolimnetic_ave_rcp26.csv')
        

#%% summer hypolimnetic_ave_rcp26
"""
all_summer_do_rcp26=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp26 = pd.concat([all_summer_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp26 = pd.concat([all_summer_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp26 = pd.concat([all_summer_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp26 = pd.concat([all_summer_do_rcp26 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_summer_do_rcp26

anova_summer_do_rcp26=annova_uncertainity(all_summer_do_rcp26)

anova_summer_do_rcp26.describe().loc['mean', :]
"""
GCMs             68.440303
param            30.398388
interaction       1.161309
GCMs/param        4.272011
year           2052.500000
Name: mean, dtype: float64
"""


anova_summer_do_rcp26.describe().loc['std', :]
"""
GCMs           19.498603
param          19.260813
interaction     0.875944
GCMs/param      4.594866
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_summer_80years_AF_rcp26=annova_uncertainity(all_summer_do_rcp26[all_summer_do_rcp26.index>2019])


anova_summer_80years_AF_rcp26.describe().loc['mean', :]
"""
GCMs             70.058206
param            28.764500
interaction       1.177294
GCMs/param        4.528975
year           2059.500000
Name: mean, dtype: float64
"""


anova_summer_80years_AF_rcp26.describe().loc['std', :]

"""
GCMs           18.656181
param          18.394197
interaction     0.895962
GCMs/param      4.718334
year           23.237900
Name: std, dtype: float64
"""





#%% GLUE method on all_summer_do_rcp26 
          

        
#all_summer_do_rcp26= all_summer_do_rcp26.set_index(all_summer_do_rcp26['Datetime'])


# summer anoxic duration  
timeseries_year_rcp26= all_summer_do_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_summer_hypolimnetic_ave_rcp26.csv')
"""        


#%%%RCP6.0

#%% annual hypolimnetic_ave_rcp60

all_annual_do_rcp60=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp60 = pd.concat([all_annual_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp60 = pd.concat([all_annual_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp60 = pd.concat([all_annual_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp60 = pd.concat([all_annual_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_annual_do_rcp60

anova_annual_do_rcp60=annova_uncertainity(all_annual_do_rcp60)

anova_annual_do_rcp60.describe().loc['mean', :]
"""
GCMs             73.895453
param            25.492631
interaction       0.611915
GCMs/param        5.996926
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_do_rcp60.describe().loc['std', :]
"""
GCMs           17.337576
param          17.304980
interaction     0.363240
GCMs/param      8.210553
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_AF_rcp60=annova_uncertainity(all_annual_do_rcp60[all_annual_do_rcp60.index>2019])


anova_annual_80years_AF_rcp60.describe().loc['mean', :]
"""
GCMs             73.745831
param            25.645952
interaction       0.608217
GCMs/param        5.337325
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_AF_rcp60.describe().loc['std', :]

"""
GCMs           17.067370
param          17.043662
interaction     0.351924
GCMs/param      5.358185
year           23.237900
Name: std, dtype: float64

"""



#%% GLUE method on all_annual_do_rcp60 
          

        
#all_annual_do_rcp60= all_annual_do_rcp60.set_index(all_annual_do_rcp60['Datetime'])


# annual anoxic duration  
timeseries_year_rcp60= all_annual_do_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_do_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_annual_hypolimnetic_ave_rcp60.csv')
        

#%% May_Nov hypolimnetic_ave_rcp60

all_May_Nov_do_rcp60=pd.DataFrame([])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp60 = pd.concat([all_May_Nov_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp60 = pd.concat([all_May_Nov_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp60 = pd.concat([all_May_Nov_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp60 = pd.concat([all_May_Nov_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_May_Nov_do_rcp60

anova_May_Nov_do_rcp60=annova_uncertainity(all_May_Nov_do_rcp60)

anova_May_Nov_do_rcp60.describe().loc['mean', :]
"""
GCMs             83.127075
param            16.057413
interaction       0.815511
GCMs/param       12.843245
year           2052.500000
Name: mean, dtype: float64
"""


anova_May_Nov_do_rcp60.describe().loc['std', :]
"""
GCMs           16.098909
param          15.268639
interaction     1.073050
GCMs/param     16.078582
year           27.279418
Name: std, dtype: float64
"""
#80 years:
anova_May_Nov_80years_AF_rcp60=annova_uncertainity(all_May_Nov_do_rcp60[all_May_Nov_do_rcp60.index>2019])


anova_May_Nov_80years_AF_rcp60.describe().loc['mean', :]
"""
GCMs             83.365378
param            15.822790
interaction       0.811832
GCMs/param       12.357125
year           2059.500000
Name: mean, dtype: float64
"""


anova_May_Nov_80years_AF_rcp60.describe().loc['std', :]

"""
GCMs           16.215414
param          15.393627
interaction     1.089197
GCMs/param     15.021182
year           23.237900
Name: std, dtype: float64

"""


#%% GLUE method on all_May_Nov_do_rcp60 
          

        
#all_May_Nov_do_rcp60= all_May_Nov_do_rcp60.set_index(all_May_Nov_do_rcp60['Datetime'])


# May_Nov anoxic duration  
timeseries_year_rcp60= all_May_Nov_do_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_do_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_May_Nov_hypolimnetic_ave_rcp60.csv')
        

#%% summer hypolimnetic_ave_rcp60
"""
all_summer_do_rcp60=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp60 = pd.concat([all_summer_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp60 = pd.concat([all_summer_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp60 = pd.concat([all_summer_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp60 = pd.concat([all_summer_do_rcp60 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_summer_do_rcp60
 
anova_summer_do_rcp60=annova_uncertainity(all_summer_do_rcp60)

anova_summer_do_rcp60.describe().loc['mean', :]
"""
GCMs             67.228499
param            31.437619
interaction       1.333882
GCMs/param        4.997149
year           2052.500000
Name: mean, dtype: float64
"""


anova_summer_do_rcp60.describe().loc['std', :]
"""
GCMs           21.123080
param          20.671360
interaction     1.036433
GCMs/param      7.285514
year           27.279418
Name: std, dtype: float64
"""

#%% GLUE method on all_summer_do_rcp60 
          

        
#all_summer_do_rcp60= all_summer_do_rcp60.set_index(all_summer_do_rcp60['Datetime'])


# summer anoxic duration  
timeseries_year_rcp60= all_summer_do_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_do_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_summer_hypolimnetic_ave_rcp60.csv')
"""        


#%%RCP8.5


#%% annual hypolimnetic_ave_rcp85

all_annual_do_rcp85=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp85 = pd.concat([all_annual_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp85 = pd.concat([all_annual_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp85 = pd.concat([all_annual_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_do_rcp85 = pd.concat([all_annual_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_annual_do_rcp85

anova_annual_do_rcp85=annova_uncertainity(all_annual_do_rcp85)

anova_annual_do_rcp85.describe().loc['mean', :]
"""
GCMs             74.334391
param            25.078907
interaction       0.586703
GCMs/param        6.095223
year           2052.500000
Name: mean, dtype: float64
"""


anova_annual_do_rcp85.describe().loc['std', :]
"""
GCMs           19.948941
param          19.929369
interaction     0.302550
GCMs/param      7.461302
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_annual_80years_AF_rcp85=annova_uncertainity(all_annual_do_rcp85[all_annual_do_rcp85.index>2019])


anova_annual_80years_AF_rcp85.describe().loc['mean', :]
"""
GCMs             73.716848
param            25.685570
interaction       0.597582
GCMs/param        6.041900
year           2059.500000
Name: mean, dtype: float64
"""


anova_annual_80years_AF_rcp85.describe().loc['std', :]

"""
GCMs           20.640350
param          20.603474
interaction     0.309331
GCMs/param      7.674285
year           23.237900
Name: std, dtype: float64
"""





#%% GLUE method on all_annual_do_rcp85 
          

        
#all_annual_do_rcp85= all_annual_do_rcp85.set_index(all_annual_do_rcp85['Datetime'])


# annual anoxic duration  
timeseries_year_rcp85= all_annual_do_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_do_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_annual_hypolimnetic_ave_rcp85.csv')
        

#%% May_Nov hypolimnetic_ave_rcp85

all_May_Nov_do_rcp85=pd.DataFrame([])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp85 = pd.concat([all_May_Nov_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp85 = pd.concat([all_May_Nov_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp85 = pd.concat([all_May_Nov_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
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
        
        # Apply the May_Nov_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series )

        all_May_Nov_do_rcp85 = pd.concat([all_May_Nov_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_May_Nov_do_rcp85

anova_May_Nov_do_rcp85=annova_uncertainity(all_May_Nov_do_rcp85)

anova_May_Nov_do_rcp85.describe().loc['mean', :]
"""
GCMs             90.027357
param             9.408128
interaction       0.564516
GCMs/param       19.203202
year           2052.500000
Name: mean, dtype: float64
"""


anova_May_Nov_do_rcp85.describe().loc['std', :]
"""
GCMs            9.967089
param           9.391762
interaction     0.783800
GCMs/param     16.940240
year           27.279418
Name: std, dtype: float64
"""

#80 years:
anova_May_Nov_80years_AF_rcp85=annova_uncertainity(all_May_Nov_do_rcp85[all_May_Nov_do_rcp85.index>2019])


anova_May_Nov_80years_AF_rcp85.describe().loc['mean', :]
"""
GCMs             90.419270
param             9.018240
interaction       0.562490
GCMs/param       20.461463
year           2059.500000
Name: mean, dtype: float64
"""


anova_May_Nov_80years_AF_rcp85.describe().loc['std', :]

"""
GCMs            9.307721
param           8.673204
interaction     0.784823
GCMs/param     17.879410
year           23.237900
Name: std, dtype: float64

"""





#%% GLUE method on all_May_Nov_do_rcp85 
          

        
#all_May_Nov_do_rcp85= all_May_Nov_do_rcp85.set_index(all_May_Nov_do_rcp85['Datetime'])


# May_Nov anoxic duration  
timeseries_year_rcp85= all_May_Nov_do_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_do_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_May_Nov_hypolimnetic_ave_rcp85.csv')
        

#%% summer hypolimnetic_ave_rcp85
"""
all_summer_do_rcp85=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp85 = pd.concat([all_summer_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp85 = pd.concat([all_summer_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp85 = pd.concat([all_summer_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the summer_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series )

        all_summer_do_rcp85 = pd.concat([all_summer_do_rcp85 , result], axis=1)
        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        

#%%Uncertainity partitioning on all_summer_do_rcp85

anova_summer_do_rcp85=annova_uncertainity(all_summer_do_rcp85)

anova_summer_do_rcp85.describe().loc['mean', :]
"""
GCMs             66.021081
param            32.367026
interaction       1.611892
GCMs/param        4.403968
year           2052.500000
Name: mean, dtype: float64
"""


anova_summer_do_rcp85.describe().loc['std', :]
"""
GCMs           21.769336
param          21.227654
interaction     1.361793
GCMs/param      5.731570
year           27.279418
Name: std, dtype: float64
"""


#80 years:
anova_summer_80years_AF_rcp85=annova_uncertainity(all_summer_do_rcp85[all_summer_do_rcp85.index>2019])


anova_summer_80years_AF_rcp85.describe().loc['mean', :]
"""
GCMs             64.777746
param            33.513591
interaction       1.708663
GCMs/param        4.434388
year           2059.500000
Name: mean, dtype: float64
"""


anova_summer_80years_AF_rcp85.describe().loc['std', :]

"""
GCMs           22.782127
param          22.221454
interaction     1.411983
GCMs/param      6.070039
year           23.237900
Name: std, dtype: float64

"""

#%% GLUE method on all_summer_do_rcp85 
          

        
#all_summer_do_rcp85= all_summer_do_rcp85.set_index(all_summer_do_rcp85['Datetime'])


# summer anoxic duration  
timeseries_year_rcp85= all_summer_do_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_do_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_summer_hypolimnetic_ave_rcp85.csv')
"""        
#%% Plotting of annual DO, May_Nov DO summer DO of his 


# the whole years


######his_annual_DO

#years
contributions_annual_do_his_years=anova_annual_do_his['year']
#GCMs
gcm_contributions_annual_do_his= anova_annual_do_his['GCMs']
#Param
param_contributions_annual_do_his=anova_annual_do_his['param']
#interaction
interact_contributions_annual_do_his =anova_annual_do_his['interaction']

######his_May_Nov_DO

#years
contributions_May_Nov_do_his_years=anova_May_Nov_do_his['year']
#GCMs
gcm_contributions_May_Nov_do_his = anova_May_Nov_do_his['GCMs']
#Param
param_contributions_May_Nov_do_his =anova_May_Nov_do_his['param']
#interaction
interact_contributions_May_Nov_do_his =anova_May_Nov_do_his['interaction']



"""
######his_summer_DO

#years
contributions_summer_do_his_years=anova_summer_do_his['year']
#GCMs
gcm_contributions_summer_do_his = anova_summer_do_his['GCMs']
#Param
param_contributions_summer_do_his =anova_summer_do_his['param']
#interaction
interact_contributions_summer_do_his =anova_summer_do_his['interaction']
"""


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
fig, axs = plt.subplots(1, 2, figsize=(24, 5), sharey=True)

# Define data for each subplot (assuming you have defined your data earlier)

# Subplot for rcp26
axs[0].fill_between(contributions_annual_do_his_years, 0, gcm_contributions_annual_do_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_annual_do_his_years, gcm_contributions_annual_do_his , gcm_contributions_annual_do_his + param_contributions_annual_do_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_annual_do_his_years, gcm_contributions_annual_do_his  + param_contributions_annual_do_his, gcm_contributions_annual_do_his + param_contributions_annual_do_his + interact_contributions_annual_do_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) DO in deoxygenation period', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(1861, 2005)
axs[0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_May_Nov_do_his_years, 0, gcm_contributions_May_Nov_do_his, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_May_Nov_do_his_years, gcm_contributions_May_Nov_do_his, gcm_contributions_May_Nov_do_his + param_contributions_May_Nov_do_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_May_Nov_do_his_years, gcm_contributions_May_Nov_do_his + param_contributions_May_Nov_do_his, gcm_contributions_May_Nov_do_his + param_contributions_May_Nov_do_his + interact_contributions_May_Nov_do_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) May-Nov DO', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(1861, 2005)
axs[1].tick_params(axis='both', which='major', labelsize=20)
"""
# Subplot for rcp85
axs[2].fill_between(contributions_summer_do_his_years, 0, gcm_contributions_summer_do_his, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_summer_do_his_years, gcm_contributions_summer_do_his, gcm_contributions_summer_do_his + param_contributions_summer_do_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_summer_do_his_years, gcm_contributions_summer_do_his + param_contributions_summer_do_his, gcm_contributions_summer_do_his + param_contributions_summer_do_his + interact_contributions_summer_do_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('Summer DO', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(1861, 2005)
axs[2].tick_params(axis='both', which='major', labelsize=20)
"""
# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in hypolimnetic DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_hypolimnetic_annual_May_Nov_DO_allyears_his.png', dpi=300, bbox_inches='tight')

plt.show()






#%%Plot of Anova test on all_annual_do_rcps




# the whole RCPs years


######rcp26

#years
contributions_annual_do_rcp26_years=anova_annual_do_rcp26['year']
#GCMs
gcm_contributions_annual_do_rcp26 = anova_annual_do_rcp26['GCMs']
#Param
param_contributions_annual_do_rcp26 =anova_annual_do_rcp26['param']
#interaction
interact_contributions_annual_do_rcp26 =anova_annual_do_rcp26['interaction']

######rcp60

#years
contributions_annual_do_rcp60_years=anova_annual_do_rcp60['year']
#GCMs
gcm_contributions_annual_do_rcp60 = anova_annual_do_rcp60['GCMs']
#Param
param_contributions_annual_do_rcp60 =anova_annual_do_rcp60['param']
#interaction
interact_contributions_annual_do_rcp60 =anova_annual_do_rcp60['interaction']




######rcp85

#years
contributions_annual_do_rcp85_years=anova_annual_do_rcp85['year']
#GCMs
gcm_contributions_annual_do_rcp85 = anova_annual_do_rcp85['GCMs']
#Param
param_contributions_annual_do_rcp85 =anova_annual_do_rcp85['param']
#interaction
interact_contributions_annual_do_rcp85 =anova_annual_do_rcp85['interaction']




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
axs[0].fill_between(contributions_annual_do_rcp26_years, 0, gcm_contributions_annual_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_annual_do_rcp26_years, gcm_contributions_annual_do_rcp26, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_annual_do_rcp26_years, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26 + interact_contributions_annual_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2006, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_annual_do_rcp60_years, 0, gcm_contributions_annual_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_annual_do_rcp60_years, gcm_contributions_annual_do_rcp60, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_annual_do_rcp60_years, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60 + interact_contributions_annual_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2006, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[2].fill_between(contributions_annual_do_rcp85_years, 0, gcm_contributions_annual_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_annual_do_rcp85_years, gcm_contributions_annual_do_rcp85, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_annual_do_rcp85_years, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85 + interact_contributions_annual_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2006, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in hypolimnetic DO\n over deoxygenation period [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_annualDO_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()

#%%

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models\uncertainty'

# Change the current working directory
os.chdir(directory_path) 

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Define colors explicitly as RGB tuples
colors = [(0.96, 0.80, 0.69), (0.6, 0.4, 0.8), (0, 0, 1)]  # Flesh, Dark Orchid, Blue

# Create a figure with three subplots
fig, axs = plt.subplots(2, 2, figsize=(24, 15), sharey=True)


# Subplot for rcp26
axs[0, 0].fill_between(contributions_annual_do_his_years, 0, gcm_contributions_annual_do_his , label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_do_his_years, gcm_contributions_annual_do_his , gcm_contributions_annual_do_his + param_contributions_annual_do_his, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 0].fill_between(contributions_annual_do_his_years, gcm_contributions_annual_do_his  + param_contributions_annual_do_his, gcm_contributions_annual_do_his + param_contributions_annual_do_his + interact_contributions_annual_do_his, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 0].set_title('(a) His', fontsize=20)
axs[0, 0].set_ylim(0,100)
axs[0, 0].set_xlim(1861, 2005)
axs[0, 0].tick_params(axis='both', which='major', labelsize=20)



# Define data for each subplot (assuming you have defined your data earlier)

# Subplot for rcp26
axs[0, 1].fill_between(contributions_annual_do_rcp26_years, 0, gcm_contributions_annual_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_do_rcp26_years, gcm_contributions_annual_do_rcp26, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0, 1].fill_between(contributions_annual_do_rcp26_years, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26, gcm_contributions_annual_do_rcp26 + param_contributions_annual_do_rcp26 + interact_contributions_annual_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0, 1].set_title('(b) RCP2.6', fontsize=20)
axs[0, 1].set_ylim(0,100)
axs[0, 1].set_xlim(2006, 2099)
axs[0, 1].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp60
axs[1, 0].fill_between(contributions_annual_do_rcp60_years, 0, gcm_contributions_annual_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_do_rcp60_years, gcm_contributions_annual_do_rcp60, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1, 0].fill_between(contributions_annual_do_rcp60_years, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60, gcm_contributions_annual_do_rcp60 + param_contributions_annual_do_rcp60 + interact_contributions_annual_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1,0].set_title('(c) RCP6.0', fontsize=20)
axs[1,0].set_ylim(0,100)
axs[1,0].set_xlim(2006, 2099)
axs[1,0].tick_params(axis='both', which='major', labelsize=20)

# Subplot for rcp85
axs[1,1].fill_between(contributions_annual_do_rcp85_years, 0, gcm_contributions_annual_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1,1].fill_between(contributions_annual_do_rcp85_years, gcm_contributions_annual_do_rcp85, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1,1].fill_between(contributions_annual_do_rcp85_years, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85, gcm_contributions_annual_do_rcp85 + param_contributions_annual_do_rcp85 + interact_contributions_annual_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1,1].set_title('(d) RCP8.5', fontsize=20)
axs[1,1].set_ylim(0,100)
axs[1,1].set_xlim(2006, 2099)
axs[1,1].tick_params(axis='both', which='major', labelsize=20)

# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in hypolimnetic DO over deoxygenation period [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.7, 0.06), fontsize=22, ncol= 3)


# Save the plot
#plt.savefig('uncertainty_annualDO_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()









#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_annual_do_rcp26_years=anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019].year
#gcms
gcm_contributions_80years_annual_do_rcp26 = anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_annual_do_rcp26 =anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_annual_do_rcp26 =anova_annual_do_rcp26[anova_annual_do_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_annual_do_rcp60_years=anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019].year
#gcms
gcm_contributions_80years_annual_do_rcp60 = anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_annual_do_rcp60 =anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_annual_do_rcp60 =anova_annual_do_rcp60[anova_annual_do_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_annual_do_rcp85_years=anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019].year
#gcms
gcm_contributions_80years_annual_do_rcp85 = anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_annual_do_rcp85 =anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_annual_do_rcp85 =anova_annual_do_rcp85[anova_annual_do_rcp85.year>2019]['interaction']


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
axs[0].fill_between(contributions_80years_annual_do_rcp26_years, 0, gcm_contributions_80years_annual_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_do_rcp26_years, gcm_contributions_80years_annual_do_rcp26, gcm_contributions_80years_annual_do_rcp26 + param_contributions_80years_annual_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_annual_do_rcp26_years, gcm_contributions_80years_annual_do_rcp26 + param_contributions_80years_annual_do_rcp26, gcm_contributions_80years_annual_do_rcp26 + param_contributions_80years_annual_do_rcp26 + interact_contributions_80years_annual_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_annual_do_rcp60_years, 0, gcm_contributions_80years_annual_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_do_rcp60_years, gcm_contributions_80years_annual_do_rcp60, gcm_contributions_80years_annual_do_rcp60 + param_contributions_80years_annual_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_annual_do_rcp60_years, gcm_contributions_80years_annual_do_rcp60 + param_contributions_80years_annual_do_rcp60, gcm_contributions_80years_annual_do_rcp60 + param_contributions_80years_annual_do_rcp60 + interact_contributions_80years_annual_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_annual_do_rcp85_years, 0, gcm_contributions_80years_annual_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_do_rcp85_years, gcm_contributions_80years_annual_do_rcp85, gcm_contributions_80years_annual_do_rcp85 + param_contributions_80years_annual_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_annual_do_rcp85_years, gcm_contributions_80years_annual_do_rcp85 + param_contributions_80years_annual_do_rcp85, gcm_contributions_80years_annual_do_rcp85 + param_contributions_80years_annual_do_rcp85 + interact_contributions_80years_annual_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
fig.text(0.08, 0.5, 'Uncertainty sources in hypolimnetic DO\n over deoxygenation period [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)



# Save the plot
plt.savefig('uncertainty_annual_do_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()






#%%Plotting of May_Nov do


#%%Plot of Anova test on all_May_Nov_do_rcps




# the whole RCPs years


######rcp26

#years
contributions_May_Nov_do_rcp26_years=anova_May_Nov_do_rcp26['year']
#GCMs
gcm_contributions_May_Nov_do_rcp26 = anova_May_Nov_do_rcp26['GCMs']
#Param
param_contributions_May_Nov_do_rcp26 =anova_May_Nov_do_rcp26['param']
#interaction
interact_contributions_May_Nov_do_rcp26 =anova_May_Nov_do_rcp26['interaction']

######rcp60

#years
contributions_May_Nov_do_rcp60_years=anova_May_Nov_do_rcp60['year']
#GCMs
gcm_contributions_May_Nov_do_rcp60 = anova_May_Nov_do_rcp60['GCMs']
#Param
param_contributions_May_Nov_do_rcp60 =anova_May_Nov_do_rcp60['param']
#interaction
interact_contributions_May_Nov_do_rcp60 =anova_May_Nov_do_rcp60['interaction']




######rcp85

#years
contributions_May_Nov_do_rcp85_years=anova_May_Nov_do_rcp85['year']
#GCMs
gcm_contributions_May_Nov_do_rcp85 = anova_May_Nov_do_rcp85['GCMs']
#Param
param_contributions_May_Nov_do_rcp85 =anova_May_Nov_do_rcp85['param']
#interaction
interact_contributions_May_Nov_do_rcp85 =anova_May_Nov_do_rcp85['interaction']




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
axs[0].fill_between(contributions_May_Nov_do_rcp26_years, 0, gcm_contributions_May_Nov_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_May_Nov_do_rcp26_years, gcm_contributions_May_Nov_do_rcp26, gcm_contributions_May_Nov_do_rcp26 + param_contributions_May_Nov_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_May_Nov_do_rcp26_years, gcm_contributions_May_Nov_do_rcp26 + param_contributions_May_Nov_do_rcp26, gcm_contributions_May_Nov_do_rcp26 + param_contributions_May_Nov_do_rcp26 + interact_contributions_May_Nov_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2006, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2006, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_May_Nov_do_rcp60_years, 0, gcm_contributions_May_Nov_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_May_Nov_do_rcp60_years, gcm_contributions_May_Nov_do_rcp60, gcm_contributions_May_Nov_do_rcp60 + param_contributions_May_Nov_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_May_Nov_do_rcp60_years, gcm_contributions_May_Nov_do_rcp60 + param_contributions_May_Nov_do_rcp60, gcm_contributions_May_Nov_do_rcp60 + param_contributions_May_Nov_do_rcp60 + interact_contributions_May_Nov_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2006, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_May_Nov_do_rcp85_years, 0, gcm_contributions_May_Nov_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_May_Nov_do_rcp85_years, gcm_contributions_May_Nov_do_rcp85, gcm_contributions_May_Nov_do_rcp85 + param_contributions_May_Nov_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_May_Nov_do_rcp85_years, gcm_contributions_May_Nov_do_rcp85 + param_contributions_May_Nov_do_rcp85, gcm_contributions_May_Nov_do_rcp85 + param_contributions_May_Nov_do_rcp85 + interact_contributions_May_Nov_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2006, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.07, 0.5, 'Uncertainty sources in \n May-Nov deep DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_May_Nov_do_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()




#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_May_Nov_do_rcp26_years=anova_May_Nov_do_rcp26[anova_May_Nov_do_rcp26.year>2019].year
#gcms
gcm_contributions_80years_May_Nov_do_rcp26 = anova_May_Nov_do_rcp26[anova_May_Nov_do_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_May_Nov_do_rcp26 =anova_May_Nov_do_rcp26[anova_May_Nov_do_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_May_Nov_do_rcp26 =anova_May_Nov_do_rcp26[anova_May_Nov_do_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_May_Nov_do_rcp60_years=anova_May_Nov_do_rcp60[anova_May_Nov_do_rcp60.year>2019].year
#gcms
gcm_contributions_80years_May_Nov_do_rcp60 = anova_May_Nov_do_rcp60[anova_May_Nov_do_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_May_Nov_do_rcp60 =anova_May_Nov_do_rcp60[anova_May_Nov_do_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_May_Nov_do_rcp60 =anova_May_Nov_do_rcp60[anova_May_Nov_do_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_May_Nov_do_rcp85_years=anova_May_Nov_do_rcp85[anova_May_Nov_do_rcp85.year>2019].year
#gcms
gcm_contributions_80years_May_Nov_do_rcp85 = anova_May_Nov_do_rcp85[anova_May_Nov_do_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_May_Nov_do_rcp85 =anova_May_Nov_do_rcp85[anova_May_Nov_do_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_May_Nov_do_rcp85 =anova_May_Nov_do_rcp85[anova_May_Nov_do_rcp85.year>2019]['interaction']


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
axs[0].fill_between(contributions_80years_May_Nov_do_rcp26_years, 0, gcm_contributions_80years_May_Nov_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_May_Nov_do_rcp26_years, gcm_contributions_80years_May_Nov_do_rcp26, gcm_contributions_80years_May_Nov_do_rcp26 + param_contributions_80years_May_Nov_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_May_Nov_do_rcp26_years, gcm_contributions_80years_May_Nov_do_rcp26 + param_contributions_80years_May_Nov_do_rcp26, gcm_contributions_80years_May_Nov_do_rcp26 + param_contributions_80years_May_Nov_do_rcp26 + interact_contributions_80years_May_Nov_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('(a) RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_May_Nov_do_rcp60_years, 0, gcm_contributions_80years_May_Nov_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_May_Nov_do_rcp60_years, gcm_contributions_80years_May_Nov_do_rcp60, gcm_contributions_80years_May_Nov_do_rcp60 + param_contributions_80years_May_Nov_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_May_Nov_do_rcp60_years, gcm_contributions_80years_May_Nov_do_rcp60 + param_contributions_80years_May_Nov_do_rcp60, gcm_contributions_80years_May_Nov_do_rcp60 + param_contributions_80years_May_Nov_do_rcp60 + interact_contributions_80years_May_Nov_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('(b) RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_May_Nov_do_rcp85_years, 0, gcm_contributions_80years_May_Nov_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_May_Nov_do_rcp85_years, gcm_contributions_80years_May_Nov_do_rcp85, gcm_contributions_80years_May_Nov_do_rcp85 + param_contributions_80years_May_Nov_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_May_Nov_do_rcp85_years, gcm_contributions_80years_May_Nov_do_rcp85 + param_contributions_80years_May_Nov_do_rcp85, gcm_contributions_80years_May_Nov_do_rcp85 + param_contributions_80years_May_Nov_do_rcp85 + interact_contributions_80years_May_Nov_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('(c) RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in\n May-Nov deep DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)



# Save the plot
plt.savefig('uncertainty_May_Nov_do_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()










#%%Plotting of summer DO rcp26, rcp60, and rcp85

#%%Plot of Anova test on all_summer_do_rcps
"""



# the whole RCPs years


######rcp26

#years
contributions_summer_do_rcp26_years=anova_summer_do_rcp26['year']
#GCMs
gcm_contributions_summer_do_rcp26 = anova_summer_do_rcp26['GCMs']
#Param
param_contributions_summer_do_rcp26 =anova_summer_do_rcp26['param']
#interaction
interact_contributions_summer_do_rcp26 =anova_summer_do_rcp26['interaction']

######rcp60

#years
contributions_summer_do_rcp60_years=anova_summer_do_rcp60['year']
#GCMs
gcm_contributions_summer_do_rcp60 = anova_summer_do_rcp60['GCMs']
#Param
param_contributions_summer_do_rcp60 =anova_summer_do_rcp60['param']
#interaction
interact_contributions_summer_do_rcp60 =anova_summer_do_rcp60['interaction']




######rcp85

#years
contributions_summer_do_rcp85_years=anova_summer_do_rcp85['year']
#GCMs
gcm_contributions_summer_do_rcp85 = anova_summer_do_rcp85['GCMs']
#Param
param_contributions_summer_do_rcp85 =anova_summer_do_rcp85['param']
#interaction
interact_contributions_summer_do_rcp85 =anova_summer_do_rcp85['interaction']




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
axs[0].fill_between(contributions_summer_do_rcp26_years, 0, gcm_contributions_summer_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_summer_do_rcp26_years, gcm_contributions_summer_do_rcp26, gcm_contributions_summer_do_rcp26 + param_contributions_summer_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_summer_do_rcp26_years, gcm_contributions_summer_do_rcp26 + param_contributions_summer_do_rcp26, gcm_contributions_summer_do_rcp26 + param_contributions_summer_do_rcp26 + interact_contributions_summer_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2006, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2006, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_summer_do_rcp60_years, 0, gcm_contributions_summer_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_summer_do_rcp60_years, gcm_contributions_summer_do_rcp60, gcm_contributions_summer_do_rcp60 + param_contributions_summer_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_summer_do_rcp60_years, gcm_contributions_summer_do_rcp60 + param_contributions_summer_do_rcp60, gcm_contributions_summer_do_rcp60 + param_contributions_summer_do_rcp60 + interact_contributions_summer_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2006, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_summer_do_rcp85_years, 0, gcm_contributions_summer_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_summer_do_rcp85_years, gcm_contributions_summer_do_rcp85, gcm_contributions_summer_do_rcp85 + param_contributions_summer_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_summer_do_rcp85_years, gcm_contributions_summer_do_rcp85 + param_contributions_summer_do_rcp85, gcm_contributions_summer_do_rcp85 + param_contributions_summer_do_rcp85 + interact_contributions_summer_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2006, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2006, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in summer hypolimnetic DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)


# Save the plot
plt.savefig('uncertainty_summerdo_allyears_rcps.png', dpi=300, bbox_inches='tight')

plt.show()





#%% analyses onley for 80 years


########rcp26

#year
contributions_80years_summer_do_rcp26_years=anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019].year
#gcms
gcm_contributions_80years_summer_do_rcp26 = anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019]['GCMs']
#param
param_contributions_80years_summer_do_rcp26 =anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019]['param']
#interaction
interact_contributions_80years_summer_do_rcp26 =anova_summer_do_rcp26[anova_summer_do_rcp26.year>2019]['interaction']



#########rcp60

#year
contributions_80years_summer_do_rcp60_years=anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019].year
#gcms
gcm_contributions_80years_summer_do_rcp60 = anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019]['GCMs']
#param
param_contributions_80years_summer_do_rcp60 =anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019]['param']
#interaction
interact_contributions_80years_summer_do_rcp60 =anova_summer_do_rcp60[anova_summer_do_rcp60.year>2019]['interaction']


##########rcp85
#year
contributions_80years_summer_do_rcp85_years=anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019].year
#gcms
gcm_contributions_80years_summer_do_rcp85 = anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019]['GCMs']
#param
param_contributions_80years_summer_do_rcp85 =anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019]['param']
#interaction
interact_contributions_80years_summer_do_rcp85 =anova_summer_do_rcp85[anova_summer_do_rcp85.year>2019]['interaction']


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
axs[0].fill_between(contributions_80years_summer_do_rcp26_years, 0, gcm_contributions_80years_summer_do_rcp26, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[0].fill_between(contributions_80years_summer_do_rcp26_years, gcm_contributions_80years_summer_do_rcp26, gcm_contributions_80years_summer_do_rcp26 + param_contributions_80years_summer_do_rcp26, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[0].fill_between(contributions_80years_summer_do_rcp26_years, gcm_contributions_80years_summer_do_rcp26 + param_contributions_80years_summer_do_rcp26, gcm_contributions_80years_summer_do_rcp26 + param_contributions_80years_summer_do_rcp26 + interact_contributions_80years_summer_do_rcp26, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[0].set_title('RCP2.6', fontsize=20)
axs[0].set_ylim(0,100)
axs[0].set_xlim(2020, 2099)
axs[0].tick_params(axis='both', which='major', labelsize=20)
#axs[0].set_xticks(np.arange(2020, 2100, 10),fontsize=20)

# Subplot for rcp60
axs[1].fill_between(contributions_80years_summer_do_rcp60_years, 0, gcm_contributions_80years_summer_do_rcp60, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[1].fill_between(contributions_80years_summer_do_rcp60_years, gcm_contributions_80years_summer_do_rcp60, gcm_contributions_80years_summer_do_rcp60 + param_contributions_80years_summer_do_rcp60, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[1].fill_between(contributions_80years_summer_do_rcp60_years, gcm_contributions_80years_summer_do_rcp60 + param_contributions_80years_summer_do_rcp60, gcm_contributions_80years_summer_do_rcp60 + param_contributions_80years_summer_do_rcp60 + interact_contributions_80years_summer_do_rcp60, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[1].set_title('RCP6.0', fontsize=20)
axs[1].set_ylim(0,100)
axs[1].set_xlim(2020, 2099)
axs[1].tick_params(axis='both', which='major', labelsize=20)
#axs[1].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Subplot for rcp85
axs[2].fill_between(contributions_80years_summer_do_rcp85_years, 0, gcm_contributions_80years_summer_do_rcp85, label='GCMs', alpha=0.7, color=colors[0], edgecolor='black')
axs[2].fill_between(contributions_80years_summer_do_rcp85_years, gcm_contributions_80years_summer_do_rcp85, gcm_contributions_80years_summer_do_rcp85 + param_contributions_80years_summer_do_rcp85, label='Parameters', alpha=0.7, color=colors[1], edgecolor='black')
axs[2].fill_between(contributions_80years_summer_do_rcp85_years, gcm_contributions_80years_summer_do_rcp85 + param_contributions_80years_summer_do_rcp85, gcm_contributions_80years_summer_do_rcp85 + param_contributions_80years_summer_do_rcp85 + interact_contributions_80years_summer_do_rcp85, label='Interactions', alpha=0.7, color=colors[2], edgecolor='black')
axs[2].set_title('RCP8.5', fontsize=20)
axs[2].set_ylim(0,100)
axs[2].set_xlim(2020, 2099)
axs[2].tick_params(axis='both', which='major', labelsize=20)
#axs[2].set_xticks(np.arange(2020, 2100, 20),fontsize=20)


# Adding labels and title with increased font size
# fig.text(0.5, 0.08, 'Year', ha='center', fontsize=20)
fig.text(0.08, 0.5, 'Uncertainty sources in summer hypolimnetic DO [%]', va='center', rotation='vertical', fontsize=22)

# Create legend handles and labels
legend_handles = [Patch(facecolor=colors[0], edgecolor='black'), 
                  Patch(facecolor=colors[1], edgecolor='black'), 
                  Patch(facecolor=colors[2], edgecolor='black')]
legend_labels = ['GCMs', 'Parameters', 'Interactions']

# Add a single legend outside the subplots
fig.legend(legend_handles, legend_labels,bbox_to_anchor=(0.57, 0.06), fontsize=22)



# Save the plot
plt.savefig('uncertainty_summer_do_80years_rcps.png', dpi=300, bbox_inches='tight')

plt.show()

"""
















#%%monthly_hypolimnetic_ave

#%%monthly_do_gfdl_his

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%monthly_hypolimnetic_ave_gfdl_rcp26

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 

#%%monthly_hypolimnetic_ave_gfdl_rcp60

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_hypolimnetic_ave_gfdl_rcp85

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%%monthly_hypolimnetic_ave_hadgem_his

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 
#%%monthly_hypolimnetic_ave_hadgem_rcp26

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_hadgem_rcp60

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
   
#%%monthly_hypolimnetic_ave_hadgem_rcp85

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl

#%%monthly_hypolimnetic_ave_ipsl_his

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_hypolimnetic_ave_ipsl_rcp26

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_ipsl_rcp60

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp85

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
#%%monthly_hypolimnetic_ave_miroc_his

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
 
#%%monthly_hypolimnetic_ave_miroc_rcp26

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_miroc_rcp60

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%%monthly_hypolimnetic_ave_miroc_rcp85

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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%sorting the indexs_annual_hypolimnetic_ave 

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his.sort_index()
glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26.sort_index()
glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60.sort_index()
glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85.sort_index()


#%%sorting the indexs_May_Nov_hypolimnetic_ave 

glue_df_May_Nov_hypolimnetic_ave_his= glue_df_May_Nov_hypolimnetic_ave_his.sort_index()
glue_df_May_Nov_hypolimnetic_ave_rcp26= glue_df_May_Nov_hypolimnetic_ave_rcp26.sort_index()
glue_df_May_Nov_hypolimnetic_ave_rcp60= glue_df_May_Nov_hypolimnetic_ave_rcp60.sort_index()
glue_df_May_Nov_hypolimnetic_ave_rcp85= glue_df_May_Nov_hypolimnetic_ave_rcp85.sort_index()





#%%Plotting and analyses 



#%%########annual do

#%%ploting annual do

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'], glue_df_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'], glue_df_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'], glue_df_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypolimnetic DO per each deoxygenation period [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)   
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_hypolimnetic_ave_his['50%'])#4.609596756177265
np.mean(glue_df_annual_hypolimnetic_ave_rcp26['50%'])#4.184518602288504
np.mean(glue_df_annual_hypolimnetic_ave_rcp60['50%'])#3.971564759760348
np.mean(glue_df_annual_hypolimnetic_ave_rcp85['50%'])#3.8434305500383124

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['50%']
annual_hypolimnetic_ave_ref=np.mean(glue_base_annual_hypolimnetic_ave_his)
#4.613891885145245


#near future [2030-2059]

glue_near_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2029 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp26)
#4.174146060868154
glue_near_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2029 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp60)
#4.058613738110313
glue_near_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2029 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp85)
#3.9832593182266893

 
#Distant future [2070-2099]

glue_distant_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2069 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp26)
#4.217150264508205
glue_distant_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2069 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp60)
#3.690863672475098
glue_distant_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2069 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp85)
# 3.4556821721461737
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_hypolimnetic_ave_his)
(0.024889050164759213,
 'positively autocorrelated',
 'no trend',
 0.6737680588269763,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp26)
(0.01564847901234311,
 'positively autocorrelated',
 'no trend',
 0.45968986302260806,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp60)
(0.013811164267201246,
 'positively autocorrelated',
 'no trend',
 0.05860441886618495,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp85)
(0.024200079051438957,
 'positively autocorrelated',
 'no trend',
 0.1434770815195705,
 0,
 0)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp26)
(0.014006453046156905,
 'positively autocorrelated',
 'no trend',
 0.4324504235358999,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp60)
(0.019728764803858295,
 'positively autocorrelated',
 'no trend',
 0.9147523390847367,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp85)

(0.024277783906209317,
 'positively autocorrelated',
 'no trend',
 0.617392769071009,
 0,
 0)





#%% 80 years from 2020 for annual_hypolimnetic_ave


glue_80years_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[2019 < glue_df_annual_hypolimnetic_ave_rcp26.index]

glue_80years_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[2019 < glue_df_annual_hypolimnetic_ave_rcp60.index]

glue_80years_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[2019 < glue_df_annual_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index<2030]['50%'])
4.075227960784212

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index<2030]['50%'])
4.267678912848086

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index<2030]['50%'])
 4.101546754158499

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index>2079]['50%'])
4.2130729481914235

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index>2079]['50%'])
3.7141909010679006

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index>2079]['50%'])
3.4778668896763256

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp26['50%'])
(0.020437372056957975,
 'positively autocorrelated',
 'no trend',
 0.6465146170427558,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp60['50%'])

(0.017656470550551733,
 'positively autocorrelated',
 'decreasing',
 4.269529974010311e-08,
 -0.00955520515995046,
 4.294398532888216)

autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp85['50%'])
(0.022833788524830017,
 'positively autocorrelated',
 'decreasing',
 1.7660877249525697e-07,
 -0.010995355387484442,
 4.2255920752661025)

#%% plot of trendlines in 80 years annual hypo DO 


os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp26['5%'], glue_80years_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp26['50%'])
#ax=plt.text(2020, 4, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p={trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

#ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp26.index.astype(float),
#        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
#        linestyle='--', color='green', alpha=0.9, linewidth=3)


ax=plt.fill_between(glue_80years_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp60['5%'], glue_80years_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p <0.0001', color='gold', fontsize= 20 )

ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)


ax=plt.fill_between(glue_80years_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp85['5%'], glue_80years_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 1.5, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p<0.0001', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3)



ax=plt.ylabel('Hypolimnetic DO during \ndeoxygenation period [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.2), fontsize=22 , ncol= 3)   
fig.savefig("GLUE_Timeseries_80years_annual_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')








#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his['50%'])
(0.03620882677974085,
 'positively autocorrelated',
 'no trend',
 0.5531533662908403,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26['50%'])
(0.01875570448782784,
 'positively autocorrelated',
 'no trend',
 0.4505722805611243,
 0,
 0)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60['50%'])
(0.017258975018624268,
 'positively autocorrelated',
 'decreasing',
 3.820487819217178e-06,
 -0.007687167867926738,
 4.290304701873718)


#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85['50%'])
(0.023626023381098597,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.010971782425621801,
 4.347534599132159)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%do_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)]['5%'] - annual_hypolimnetic_ave_ref,
                      glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index) ]['95%'] - annual_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)]['50%'] - annual_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp26['95%']-annual_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%']-annual_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%']-annual_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%']-annual_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%']-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%']-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of DO in deoxygenation period [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')











#%%===========May-Nov average of anoxic afctor 


#%%ploting May_Nov anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_his.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_his['5%'], glue_df_May_Nov_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_his.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['5%'], glue_df_May_Nov_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['5%'], glue_df_May_Nov_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['5%'], glue_df_May_Nov_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypolimnetic DO in May-Nov [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)
fig.savefig("GLUE_Timeseries_May_Nov_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_May_Nov_hypolimnetic_ave_his['50%'])# 7.66120828881849
np.mean(glue_df_May_Nov_hypolimnetic_ave_rcp26['50%'])#6.618663963770041
np.mean(glue_df_May_Nov_hypolimnetic_ave_rcp60['50%'])#6.320917663879071
np.mean(glue_df_May_Nov_hypolimnetic_ave_rcp85['50%'])# 6.046266677458798

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_May_Nov_hypolimnetic_ave_his=glue_df_May_Nov_hypolimnetic_ave_his[1975 < glue_df_May_Nov_hypolimnetic_ave_his.index]['50%']
May_Nov_hypolimnetic_ave_ref=np.mean(glue_base_May_Nov_hypolimnetic_ave_his)
#7.138866446048089


#near future [2030-2059]

glue_near_future_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26[(2029 < glue_df_May_Nov_hypolimnetic_ave_rcp26.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_May_Nov_hypolimnetic_ave_rcp26)
#6.259790200562322
glue_near_future_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60[(2029 < glue_df_May_Nov_hypolimnetic_ave_rcp60.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_May_Nov_hypolimnetic_ave_rcp60)
#6.245612088377149
glue_near_future_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85[(2029 < glue_df_May_Nov_hypolimnetic_ave_rcp85.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_May_Nov_hypolimnetic_ave_rcp85)
#5.983519297014239

 
#Distant future [2070-2099]

glue_distant_future_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26[(2069 < glue_df_May_Nov_hypolimnetic_ave_rcp26.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_May_Nov_hypolimnetic_ave_rcp26)
# 6.225348018214687
glue_distant_future_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60[(2069 < glue_df_May_Nov_hypolimnetic_ave_rcp60.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_May_Nov_hypolimnetic_ave_rcp60)
#5.427896874035917
glue_distant_future_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85[(2069 < glue_df_May_Nov_hypolimnetic_ave_rcp85.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_May_Nov_hypolimnetic_ave_rcp85)
#4.84063010155642
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_May_Nov_hypolimnetic_ave_his)

(0.005187150879213314,
 'positively autocorrelated',
 'decreasing',
 0.00020664750829468836,
 -0.024866956958808435,
 7.516873625240289)
#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Nov_hypolimnetic_ave_rcp26)
(0.005979574184823156,
 'positively autocorrelated',
 'no trend',
 0.08039114754218035,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Nov_hypolimnetic_ave_rcp60)
(0.003945845571485635,
 'positively autocorrelated',
 'decreasing',
 0.00015538682123561465,
 -0.032597615481306304,
 6.677100458739104)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Nov_hypolimnetic_ave_rcp85)

(0.007585887596381148,
 'positively autocorrelated',
 'decreasing',
 0.0048191095611576085,
 -0.023876963936711033,
 6.38019685190543)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Nov_hypolimnetic_ave_rcp26)
(0.005507530383489476,
 'positively autocorrelated',
 'no trend',
 0.11641261541028025,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Nov_hypolimnetic_ave_rcp60)
(0.007474438883454963,
 'positively autocorrelated',
 'no trend',
 0.17512514633807807,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Nov_hypolimnetic_ave_rcp85)
(0.015306708297526618,
 'positively autocorrelated',
 'no trend',
 0.13396533563924473,
 0,
 0)





#%% 80 years from 2020 for May_Nov_hypolimnetic_ave


glue_80years_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26[2019 < glue_df_May_Nov_hypolimnetic_ave_rcp26.index]

glue_80years_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60[2019 < glue_df_May_Nov_hypolimnetic_ave_rcp60.index]

glue_80years_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85[2019 < glue_df_May_Nov_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp26[glue_80years_May_Nov_hypolimnetic_ave_rcp26.index<2030]['50%'])
6.451878498847852

#rcp6.0
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp60[glue_80years_May_Nov_hypolimnetic_ave_rcp60.index<2030]['50%'])
6.34886612277881

#rcp8.5
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp85[glue_80years_May_Nov_hypolimnetic_ave_rcp85.index<2030]['50%'])
6.486532995492065

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp26[glue_80years_May_Nov_hypolimnetic_ave_rcp26.index>2079]['50%'])
6.150918098404295

#rcp6.0
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp60[glue_80years_May_Nov_hypolimnetic_ave_rcp60.index>2079]['50%'])
5.369105591071739

#rcp8.5
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp85[glue_80years_May_Nov_hypolimnetic_ave_rcp85.index>2079]['50%'])
 4.7672851608810225

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp26['50%'])
(0.00811196915341652,
 'positively autocorrelated',
 'decreasing',
 0.03256525306652791,
 -0.0038845562809241433,
 6.38506546575602)


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp60['50%'])
(0.005556890007357073,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.017627507714108592,
 6.526890392574551)

autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp85['50%'])
(0.010394322448773006,
 'positively autocorrelated',
 'decreasing',
 2.049471703458039e-13,
 -0.027757859300480348,
 6.647814540246592)

#%%plotting May_Nov do over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp26['5%'], glue_80years_May_Nov_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp26['50%'])
ax=plt.text(2020, 4, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p={trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp26.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)


ax=plt.fill_between(glue_80years_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp60['5%'], glue_80years_May_Nov_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 3.5, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p <0.0001', color='gold', fontsize= 20 )

ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)


ax=plt.fill_between(glue_80years_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp85['5%'], glue_80years_May_Nov_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 3, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p<0.0001', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3)



ax=plt.ylabel('Deep DO in May-Nov [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.95, -0.2), fontsize=22 , ncol= 3)   
fig.savefig("GLUE_Timeseries_80years_May_Nov_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_his['50%'])
(0.007829074534044191,
 'positively autocorrelated',
 'no trend',
 0.08051361529571932,
 0,
 0)
#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_rcp26['50%'])
(0.007474826766924049,
 'positively autocorrelated',
 'decreasing',
 0.00038613537861231784,
 -0.004581738416384463,
 6.523344359524091)
#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_rcp60['50%'])
(0.00639768298570022,
 'positively autocorrelated',
 'decreasing',
 1.4499512701604544e-13,
 -0.016355787245149606,
 6.781138397165717)
#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_rcp85['50%'])
(0.009643205085654959,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.027334191791791838,
 7.011761445956935)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%DO_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_his[(1975 < glue_df_May_Nov_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_May_Nov_hypolimnetic_ave_his[(1975< glue_df_May_Nov_hypolimnetic_ave_his.index)]['5%'] - May_Nov_hypolimnetic_ave_ref,
                      glue_df_May_Nov_hypolimnetic_ave_his[(1975 < glue_df_May_Nov_hypolimnetic_ave_his.index) ]['95%'] - May_Nov_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_his[(1975 < glue_df_May_Nov_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_May_Nov_hypolimnetic_ave_his[(1975 < glue_df_May_Nov_hypolimnetic_ave_his.index)]['50%'] - May_Nov_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['5%']-May_Nov_hypolimnetic_ave_ref, glue_df_May_Nov_hypolimnetic_ave_rcp26['95%']-May_Nov_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['50%']-May_Nov_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['5%']-May_Nov_hypolimnetic_ave_ref, glue_df_May_Nov_hypolimnetic_ave_rcp60['95%']-May_Nov_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['50%']-May_Nov_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['5%']-May_Nov_hypolimnetic_ave_ref, glue_df_May_Nov_hypolimnetic_ave_rcp85['95%']-May_Nov_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['50%']-May_Nov_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of deep DO in May-Nov [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_May_Nov_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')












#%%===========summer average of DO


#%%########summer DO

#
"""%%ploting summer DO

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['5%'], glue_df_summer_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%'], glue_df_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%'], glue_df_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%'], glue_df_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypolimnetic DO in summer [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_summer_hypolimnetic_ave_his['50%'])#3.3877648031141754
np.mean(glue_df_summer_hypolimnetic_ave_rcp26['50%'])#2.4731856742174827
np.mean(glue_df_summer_hypolimnetic_ave_rcp60['50%'])#2.1550693101618354
np.mean(glue_df_summer_hypolimnetic_ave_rcp85['50%'])#2.0216371732488216

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his[1975 < glue_df_summer_hypolimnetic_ave_his.index]['50%']
summer_hypolimnetic_ave_ref=np.mean(glue_base_summer_hypolimnetic_ave_his)
#3.405313623842368


#near future [2030-2059]

glue_near_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2029 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp26)
# 2.442836677609118
glue_near_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2029 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp60)
# 2.284296650730716
glue_near_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2029 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp85)
#  2.12983053408194

 
#Distant future [2070-2099]

glue_distant_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2069 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp26)
#2.4802458923822894
glue_distant_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2069 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp60)
#1.689415770106308
glue_distant_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2069 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp85)
#1.4371589966037255
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_summer_hypolimnetic_ave_his)
(0.031019579516014202,
 'positively autocorrelated',
 'no trend',
 0.31774734769908775,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp26)
(0.05682632419306522,
 'positively autocorrelated',
 'no trend',
 0.4754490495282657,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp60)
(0.05219898587244871,
 'positively autocorrelated',
 'decreasing',
 0.0021502307218466132,
 -0.016953890759819783,
 2.40141707693214)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp85)

(0.03832191743597291,
 'positively autocorrelated',
 'decreasing',
 0.0021502307218466132,
 -0.020959827900911027,
 2.4141430334696334)


#Distant future [2070-2099]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp26)
(0.04482308242625801,
 'positively autocorrelated',
 'decreasing',
 0.026946782463489027,
 -0.023917748930890097,
 2.790762223592984)

#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp60)
(0.0456967488175919,
 'positively autocorrelated',
 'no trend',
 0.7752944295177846,
 0,
 0)

#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp85)
(0.11218537402374852,
 'positively autocorrelated',
 'no trend',
 0.18675613776082578,
 0,
 0)




#%% 80 years from 2020 for summer_hypolimnetic_ave


glue_80years_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[2019 < glue_df_summer_hypolimnetic_ave_rcp26.index]

glue_80years_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[2019 < glue_df_summer_hypolimnetic_ave_rcp60.index]

glue_80years_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[2019 < glue_df_summer_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index<2030]['50%'])
2.4180066251627204

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index<2030]['50%'])
2.5254198256447875

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index<2030]['50%'])
2.5022468009157883

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index>2079]['50%'])
2.3967191677896356

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index>2079]['50%'])
1.695719305767162

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index>2079]['50%'])
1.4096391938251762

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp26['50%'])
(0.05183371297244382,
 'positively autocorrelated',
 'no trend',
 0.7871194357602034,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
(0.0515504405602805,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.013130707423988409,
 2.543645550696846)


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
(0.07002175830344304,
 'positively autocorrelated',
 'decreasing',
 1.7563728249569976e-13,
 -0.01737490807443354,
 2.5716138716171484)



#%%plotting summer anoxic factor over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['5%'], glue_80years_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['5%'], glue_80years_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 7.5, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )

ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3)


ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['5%'], glue_80years_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 7, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )

ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3)


ax=plt.ylabel('Hypolimnetic DO in summer [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire scenario

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_his['50%'])
(0.06159841953286706,
 'positively autocorrelated',
 'no trend',
 0.9414027070186699,
 0,
 0)
#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp26['50%'])
(0.04644270972932335,
 'positively autocorrelated',
 'no trend',
 0.14546212346892773,
 0,
 0)
#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp60['50%'])
(0.051817592017632405,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.013175385343608388,
 2.7227019069401925)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp85['50%'])
(0.07264701310648392,
 'positively autocorrelated',
 'decreasing',
 0.0,
 -0.017930312930872327,
 2.859156895471733)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['5%'] - summer_hypolimnetic_ave_ref,
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ]['95%'] - summer_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['50%'] - summer_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp26['95%']-summer_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%']-summer_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp60['95%']-summer_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%']-summer_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp85['95%']-summer_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%']-summer_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of hypolimnetic DO in summer [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')

"""


#%%Anlyses on the RCP2.6 with constant inital condition as 12.298 mg/L

#annual/May_Nov/summer AF
#gfdl


all_annual_do_rcp26_test= pd.DataFrame([])
all_May_Nov_do_rcp26_test= pd.DataFrame([])
#all_summer_do_rcp26_test= pd.DataFrame([])
all_weights= np.array([])

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26"):
        
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
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_May_Nov_do_rcp26_test= pd.concat([all_May_Nov_do_rcp26_test , result_May_Nov], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result May_Nov to a new CSV file
        result_May_Nov_filename = f'May_Nov_do_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Nov_filename))#, index=False)
       

        result_May_Nov.to_csv(os.path.join(directory, result_May_Nov_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
        
#hadgem

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26"):
        
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
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_May_Nov_do_rcp26_test= pd.concat([all_May_Nov_do_rcp26_test , result_May_Nov], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result May_Nov to a new CSV file
        result_May_Nov_filename = f'May_Nov_do_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Nov_filename))#, index=False)
       

        result_May_Nov.to_csv(os.path.join(directory, result_May_Nov_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
        
        
#ipsl

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26"):
        
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
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_May_Nov_do_rcp26_test= pd.concat([all_May_Nov_do_rcp26_test , result_May_Nov], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result May_Nov to a new CSV file
        result_May_Nov_filename = f'May_Nov_do_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Nov_filename))#, index=False)
       

        result_May_Nov.to_csv(os.path.join(directory, result_May_Nov_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
            
        
#miroc

directory = "C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26_initialcond_attribution"


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26"):
        
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
        result_annual =annual_hypolimnetic_ave (C, Vr, time_series )
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_annual_do_rcp26_test = pd.concat([all_annual_do_rcp26_test , result_annual], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result annual to a new CSV file
        result_annual_filename = f'annual_do_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_annual_filename))#, index=False)
       

        result_annual.to_csv(os.path.join(directory, result_annual_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_AF'])
        
        
        
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
        result_May_Nov =May_Nov_hypolimnetic_ave (C, Vr, time_series )
        #result_summer =summer_hypolimnetic_ave (C, Vr, time_series )
        
        
        all_May_Nov_do_rcp26_test= pd.concat([all_May_Nov_do_rcp26_test , result_May_Nov], axis=1)
        #all_summer_do_rcp26_test= pd.concat([all_summer_do_rcp26_test , result_summer], axis=1)


        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }

        
        # Save the result May_Nov to a new CSV file
        result_May_Nov_filename = f'May_Nov_do_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_May_Nov_filename))#, index=False)
       

        result_May_Nov.to_csv(os.path.join(directory, result_May_Nov_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_AF'])
    
"""        
        # Save the result summer to a new CSV file
        result_summer_filename = f'summer_do_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_summer_filename))#, index=False)
       

        result_summer.to_csv(os.path.join(directory, result_summer_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_AF'])
"""    
        


    
    
    
    
    
    
    
        
#%% GLUE of diff of test rcp26 scenarios for annual/May_Nov/summer do


all_annual_do_rcp26_test
all_May_Nov_do_rcp26_test
#all_summer_do_rcp26_test

all_annual_do_rcp26
all_May_Nov_do_rcp26
#all_summer_do_rcp26


diff_base_test_annual_do_rcp26= pd.DataFrame(np.array(all_annual_do_rcp26)-np.array(all_annual_do_rcp26_test))

diff_base_test_May_Nov_do_rcp26= pd.DataFrame(np.array(all_May_Nov_do_rcp26)-np.array(all_May_Nov_do_rcp26_test))

#diff_base_test_summer_do_rcp26= pd.DataFrame(np.array(all_summer_do_rcp26)-np.array(all_summer_do_rcp26_test))



all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_annual_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_annual_do_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_annual_do_rcp26=glue_diff_base_test_annual_do_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_annual_do_rcp26=glue_diff_base_test_annual_do_rcp26.sort_index()
glue_diff_base_test_annual_do_rcp26_80years=glue_diff_base_test_annual_do_rcp26[glue_diff_base_test_annual_do_rcp26.index>2019]


# May_Nov DO hypolimnion 
timeseries_year_rcp26= all_May_Nov_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_May_Nov_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_May_Nov_do_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_May_Nov_do_rcp26=glue_diff_base_test_May_Nov_do_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_May_Nov_do_rcp26=glue_diff_base_test_May_Nov_do_rcp26.sort_index()
glue_diff_base_test_May_Nov_do_rcp26_80years=glue_diff_base_test_May_Nov_do_rcp26[glue_diff_base_test_May_Nov_do_rcp26.index>2019]
"""
# summer DO hypolimnion 
timeseries_year_rcp26= all_summer_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in diff_base_test_summer_do_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_diff_base_test_summer_do_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_diff_base_test_summer_do_rcp26=glue_diff_base_test_summer_do_rcp26.set_index(timeseries_year_rcp26)    
glue_diff_base_test_summer_do_rcp26=glue_diff_base_test_summer_do_rcp26.sort_index()
glue_diff_base_test_summer_do_rcp26_80years=glue_diff_base_test_summer_do_rcp26[glue_diff_base_test_summer_do_rcp26.index>2019]
"""




#%%GLUE for rcp26 test 
all_weights


# annual DO hypolimnion 
timeseries_year_rcp26= all_annual_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_do_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_annual_do_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_annual_do_rcp26_test=glue_annual_do_rcp26_test.set_index(timeseries_year_rcp26)    
glue_annual_do_rcp26_test=glue_annual_do_rcp26_test.sort_index()
glue_annual_do_rcp26_test_80years=glue_annual_do_rcp26_test[glue_annual_do_rcp26_test.index>2019]


# May_Nov DO hypolimnion 
timeseries_year_rcp26= all_May_Nov_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_do_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_May_Nov_do_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_May_Nov_do_rcp26_test=glue_May_Nov_do_rcp26_test.set_index(timeseries_year_rcp26)    
glue_May_Nov_do_rcp26_test=glue_May_Nov_do_rcp26_test.sort_index()
glue_May_Nov_do_rcp26_test_80years=glue_May_Nov_do_rcp26_test[glue_May_Nov_do_rcp26_test.index>2019]

"""
# summer DO hypolimnion 
timeseries_year_rcp26= all_summer_do_rcp26_test.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_do_rcp26_test.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_summer_do_rcp26_test = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_summer_do_rcp26_test=glue_summer_do_rcp26_test.set_index(timeseries_year_rcp26)    
glue_summer_do_rcp26_test=glue_summer_do_rcp26_test.sort_index()
glue_summer_do_rcp26_test_80years=glue_summer_do_rcp26_test[glue_summer_do_rcp26_test.index>2019]
"""





#%% Diff of test and baseline->only for onset
### test->only for stratification duration 

#%% analysing the difference of baseline scenarios and test with fixed inital condition 

#%%annual do over 80 years

glue_diff_base_test_annual_do_rcp26_80years=glue_diff_base_test_annual_do_rcp26[glue_diff_base_test_annual_do_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_annual_do_rcp26_80years['50%'])

(2.0, 'non autocorrelated', 'no trend', 0.21949168333305025, 0, 0)







#%%May_Nov do

glue_diff_base_test_May_Nov_do_rcp26_80years=glue_diff_base_test_May_Nov_do_rcp26[glue_diff_base_test_May_Nov_do_rcp26.index>2019]
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_May_Nov_do_rcp26_80years['50%'])

(1.9930754757343887,
 'positively autocorrelated',
 'increasing',
 0.009950165094664731,
 0.0011949898705893892,
 -0.015490856889306855)













#%%summer do

"""
autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_summer_do_rcp26[glue_diff_base_test_summer_do_rcp26.index>2019]['50%'])
(1.9999999999999996,
 'positively autocorrelated',
 'no trend',
 0.635340267384636,
 0,
 0)
"""




#%% trendline in test scenario of rcp26 over 80 years 


#%% annual do
autocorr_MK_org_modif_sens_slope_test(glue_annual_do_rcp26_test_80years['50%'])
(0.014500132581905217,
 'positively autocorrelated',
 'no trend',
 0.693069521433799,
 0,
 0)

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_annual_do_rcp26_test_80years.index.astype(float), glue_annual_do_rcp26_test_80years['5%'], glue_annual_do_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_annual_do_rcp26_test_80years.index.astype(float), glue_annual_do_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




#trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_annual_do_rcp26_test_80years['50%'])
#ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

#ax=plt.plot(glue_annual_do_rcp26_test_80years.index.astype(float),
#        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
#        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('DO in deoxygenation period of RCP2.6 with\n fixed inital condition [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("test_initalcondition_fixed_annual_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')




#%%

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_diff_base_test_annual_do_rcp26_80years.index.astype(float), glue_diff_base_test_annual_do_rcp26_80years['5%'], glue_diff_base_test_annual_do_rcp26_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_diff_base_test_annual_do_rcp26_80years.index.astype(float), glue_diff_base_test_annual_do_rcp26_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




#trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_annual_do_rcp26_test_80years['50%'])
#ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

#ax=plt.plot(glue_diff_base_test_annual_do_rcp26_80years.index.astype(float),
#        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
#        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('DO diff between test and baseline of\n DO deoxygenation period of RCP2.6 with\n fixed inital condition [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("test_diff_initalcondition_fixed_annual_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')








#%% May_Nov do:


autocorr_MK_org_modif_sens_slope_test(glue_May_Nov_do_rcp26_test_80years['50%'])
(0.010085099408398666,
 'positively autocorrelated',
 'decreasing',
 0.015428208140098487,
 -0.004868384737487827,
 6.455874166439429)





#%% No trend for during deoxygenation for neither test nor the difference 

#%%for paper both plot of diff and test of May_Nov rcp26 in one plot 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Create figure and axes for subplots
fig, axs = plt.subplots(1, 2, figsize=(25, 10))

# Plot for the first subplot
ax = axs[1]
ax.fill_between(glue_diff_base_test_May_Nov_do_rcp26_80years.index,
                glue_diff_base_test_May_Nov_do_rcp26_80years['5%'],
                glue_diff_base_test_May_Nov_do_rcp26_80years['95%'],
                color='green', alpha=0.2, label='90% CI')
ax.plot(glue_diff_base_test_May_Nov_do_rcp26_80years.index,
        glue_diff_base_test_May_Nov_do_rcp26_80years['50%'],
        'green', label='Median', alpha=0.9, linewidth=3)

# Add trendline
trendline_rcp26_1 = autocorr_MK_org_modif_sens_slope_test(glue_diff_base_test_May_Nov_do_rcp26_80years['50%'])
ax.text(0.95, 0.95, '(b)', transform=ax.transAxes, fontsize=22,
        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 0.5, f'y = {trendline_rcp26_1[-2]:.3f}x + {trendline_rcp26_1[-1]:.3f}, p = {trendline_rcp26_1[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_diff_base_test_May_Nov_do_rcp26_80years.index.astype(float),
        trendline_rcp26_1[-2] * np.arange(80) + trendline_rcp26_1[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)

# Set labels for the first subplot
ax.set_ylabel('Deep DO in May-Nov of RCP2.6 \n difference between fixed initial condition \n and original scenario  [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_diff_base_test_May_Nov_do_rcp26_80years.index)
ax.set_xticklabels(glue_diff_base_test_May_Nov_do_rcp26_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Plot for the second subplot
ax = axs[0]
ax.fill_between(glue_May_Nov_do_rcp26_test_80years.index,
                glue_May_Nov_do_rcp26_test_80years['5%'],
                glue_May_Nov_do_rcp26_test_80years['95%'],
                color='green', alpha=0.2)#, label='90% CI')
ax.plot(glue_May_Nov_do_rcp26_test_80years.index,
        glue_May_Nov_do_rcp26_test_80years['50%'].astype(float),
        'green', alpha=0.9, linewidth=3)# label='Median',

# Add trendline
trendline_rcp26_0 = autocorr_MK_org_modif_sens_slope_test(glue_May_Nov_do_rcp26_test_80years['50%'])
ax.text(0.95, 0.95, '(a)', transform=ax.transAxes, fontsize=22,
        verticalalignment='top', horizontalalignment='right')
ax.text(2020, 9.8, f'y = {trendline_rcp26_0[-2]:.3f}x + {trendline_rcp26_0[-1]:.3f}, p = {trendline_rcp26_0[-3]:.3f}',
        color='green', fontsize=20)
ax.plot(glue_May_Nov_do_rcp26_test_80years.index,
        trendline_rcp26_0[-2] * np.arange(80) + trendline_rcp26_0[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)

# Set labels for the second subplot
ax.set_ylabel('Deep DO in May-Nov of RCP2.6 with\n fixed initial condition [mg L$^{-1}$]', fontsize=26)
ax.set_xlabel('Year', fontsize=26)
ax.tick_params(axis='y', labelsize=22)
ax.set_xticks(glue_May_Nov_do_rcp26_test_80years.index)
ax.set_xticklabels(glue_May_Nov_do_rcp26_test_80years.index, rotation=45, fontsize=22)
ax.xaxis.set_major_locator(MaxNLocator(prune='both'))

# Add a single legend for both subplots in the center bottom
fig.legend(loc='lower center', fontsize=22, ncol=1)

plt.tight_layout()

plt.savefig("atttest_difference_test_initalcondition_fixed_May_Nov_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')




#%%
glue_diff_base_test_May_Nov_do_rcp26_80years
glue_May_Nov_do_rcp26_test_80years


os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_May_Nov_do_rcp26_test_80years.index.astype(float), glue_May_Nov_do_rcp26_test_80years['5%'], glue_May_Nov_do_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_May_Nov_do_rcp26_test_80years.index.astype(float), glue_May_Nov_do_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_May_Nov_do_rcp26_test_80years['50%'])
ax=plt.text(2020, 9, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_May_Nov_do_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Hypolimnetic DO in May-Nov o\nf RCP2.6 with fixed inital condition [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22, ncol=2)  
fig.savefig("test_initalcondition_fixed_May_Nov_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')

#%% summer do
"""
autocorr_MK_org_modif_sens_slope_test(glue_summer_do_rcp26_test_80years['50%'])

(0.0443638104024983,
 'positively autocorrelated',
 'no trend',
 0.08159993472744387,
 0,



#%%summer do

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')


import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_summer_do_rcp26_test_80years.index.astype(float), glue_summer_do_rcp26_test_80years['5%'], glue_summer_do_rcp26_test_80years['95%'], color='green', alpha=0.2 ,  label= '90% CI')
ax=plt.plot(glue_summer_do_rcp26_test_80years.index.astype(float), glue_summer_do_rcp26_test_80years['50%'].astype(float), 'green', label='Median', alpha=0.9, linewidth=3  )




trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_summer_do_rcp26_test_80years['50%'])
ax=plt.text(2020, 2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p = {trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot(glue_summer_do_rcp26_test_80years.index.astype(float),
        trendline_rcp26[-2] * np.arange(80) + trendline_rcp26[-1],
        linestyle='--', color='green', alpha=0.9, linewidth=3)




ax=plt.ylabel('Hypolimnetic DO in summer of RCP2.6 with fixed inital condition [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("test_initalcondition_fixed_summer_do_80years_rcp26.png",  dpi=300, bbox_inches='tight')

"""




#%%%%%%%%======================
#============OLD
#############
#%% Annual anoxic factor_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% May_Nov anoxic factor_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% May_Nov anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%% Annual anoxic factor_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% May_Nov anoxic factor_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_hadgem_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% May_Nov anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_hadgem_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_hadgem_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_hadgem_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl
#%% Annual anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% May_Nov anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_ipsl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% May_Nov anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_ipsl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_ipsl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_ipsl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%miroc 
#%% Annual anoxic factor_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% May_Nov anoxic factor_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_miroc_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% May_Nov anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_miroc_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_miroc_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% May_Nov anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = May_Nov_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'May_Nov_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['May_Nov_hypolimnetic_ave'])
        
                
#%% summer anoxic factor_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_miroc_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%GLUE method raeding again these files %%%%%%%%%%%%%%%%%%%

#%%his_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_annual_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        
all_annual_hypolimnetic_ave_his= all_annual_hypolimnetic_ave_his.set_index(annual_hypolimnetic_ave['year'])


# annual anoxic duration  
timeseries_year_his= all_annual_hypolimnetic_ave_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


#%%rcp26_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_annual_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        

all_annual_hypolimnetic_ave_rcp26= all_annual_hypolimnetic_ave_rcp26.set_index(annual_hypolimnetic_ave['year'])

# annual anoxic duration  
timeseries_year_rcp26= all_annual_hypolimnetic_ave_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')


#%%rcp60_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_annual_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        

all_annual_hypolimnetic_ave_rcp60= all_annual_hypolimnetic_ave_rcp60.set_index(annual_hypolimnetic_ave['year'])

# annual anoxic duration  
timeseries_year_rcp60= all_annual_hypolimnetic_ave_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')

#%%rcp85_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_annual_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        
all_annual_hypolimnetic_ave_rcp85= all_annual_hypolimnetic_ave_rcp85.set_index(annual_hypolimnetic_ave['year'])


# annual anoxic duration  
timeseries_year_rcp85= all_annual_hypolimnetic_ave_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')




#%%sorting the indexs_annual_hypolimnetic_ave 

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his.sort_index()
glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26.sort_index()
glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60.sort_index()
glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85.sort_index()


#%% May_Nov anoxic factor
#%%his_May_Nov_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_May_Nov_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_his = pd.concat([all_May_Nov_hypolimnetic_ave_his , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_his = pd.concat([all_May_Nov_hypolimnetic_ave_his , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_his = pd.concat([all_May_Nov_hypolimnetic_ave_his , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_his = pd.concat([all_May_Nov_hypolimnetic_ave_his , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        
        
all_May_Nov_hypolimnetic_ave_his= all_May_Nov_hypolimnetic_ave_his.set_index(May_Nov_hypolimnetic_ave['year'])


# May_Nov anoxic duration  
timeseries_year_his= all_May_Nov_hypolimnetic_ave_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_hypolimnetic_ave_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_his=glue_df_May_Nov_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


#%%rcp26_May_Nov_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_May_Nov_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp26 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp26 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp26 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp26 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp26 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp26 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp26 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp26 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        
        

all_May_Nov_hypolimnetic_ave_rcp26= all_May_Nov_hypolimnetic_ave_rcp26.set_index(May_Nov_hypolimnetic_ave['year'])

# May_Nov anoxic duration  
timeseries_year_rcp26= all_May_Nov_hypolimnetic_ave_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_hypolimnetic_ave_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')


#%%rcp60_May_Nov_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_May_Nov_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp60 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp60 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp60 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp60 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp60 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp60 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp60 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp60 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        
        

all_May_Nov_hypolimnetic_ave_rcp60= all_May_Nov_hypolimnetic_ave_rcp60.set_index(May_Nov_hypolimnetic_ave['year'])

# May_Nov anoxic duration  
timeseries_year_rcp60= all_May_Nov_hypolimnetic_ave_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_hypolimnetic_ave_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')

#%%rcp85_May_Nov_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_May_Nov_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp85 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp85 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp85 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp85 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp85 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp85 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("May_Nov_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        May_Nov_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        May_Nov_hypolimnetic_ave=May_Nov_hypolimnetic_ave.set_index(May_Nov_hypolimnetic_ave.index)
        
        all_May_Nov_hypolimnetic_ave_rcp85 = pd.concat([all_May_Nov_hypolimnetic_ave_rcp85 , May_Nov_hypolimnetic_ave['May_Nov_hypolimnetic_ave']], axis=1)
        
        
        
        
all_May_Nov_hypolimnetic_ave_rcp85= all_May_Nov_hypolimnetic_ave_rcp85.set_index(May_Nov_hypolimnetic_ave['year'])


# May_Nov anoxic duration  
timeseries_year_rcp85= all_May_Nov_hypolimnetic_ave_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_May_Nov_hypolimnetic_ave_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_May_Nov_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_May_Nov_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')



#%%sorting the indexs_May_Nov_hypolimnetic_ave 

glue_df_May_Nov_hypolimnetic_ave_his= glue_df_May_Nov_hypolimnetic_ave_his.sort_index()
glue_df_May_Nov_hypolimnetic_ave_rcp26= glue_df_May_Nov_hypolimnetic_ave_rcp26.sort_index()
glue_df_May_Nov_hypolimnetic_ave_rcp60= glue_df_May_Nov_hypolimnetic_ave_rcp60.sort_index()
glue_df_May_Nov_hypolimnetic_ave_rcp85= glue_df_May_Nov_hypolimnetic_ave_rcp85.sort_index()



#%%===== summer anoxic factor Glue dataframe 

#%%his_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_summer_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        
all_summer_hypolimnetic_ave_his= all_summer_hypolimnetic_ave_his.set_index(summer_hypolimnetic_ave['year'])


# summer anoxic duration  
timeseries_year_his= all_summer_hypolimnetic_ave_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


#%%rcp26_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_summer_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        

all_summer_hypolimnetic_ave_rcp26= all_summer_hypolimnetic_ave_rcp26.set_index(summer_hypolimnetic_ave['year'])

# summer anoxic duration  
timeseries_year_rcp26= all_summer_hypolimnetic_ave_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_anoxic_factor_rcp26.csv')


#%%rcp60_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_summer_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        

all_summer_hypolimnetic_ave_rcp60= all_summer_hypolimnetic_ave_rcp60.set_index(summer_hypolimnetic_ave['year'])

# summer anoxic duration  
timeseries_year_rcp60= all_summer_hypolimnetic_ave_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_anoxic_factor_rcp60.csv')

#%%rcp85_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_summer_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        
        
all_summer_hypolimnetic_ave_rcp85= all_summer_hypolimnetic_ave_rcp85.set_index(summer_hypolimnetic_ave['year'])


# summer anoxic duration  
timeseries_year_rcp85= all_summer_hypolimnetic_ave_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_summer_hypolimnetic_ave_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_anoxic_factor_rcp85.csv')


#%%sorting the indexs_summer_hypolimnetic_ave 

glue_df_summer_hypolimnetic_ave_his= glue_df_summer_hypolimnetic_ave_his.sort_index()
glue_df_summer_hypolimnetic_ave_rcp26= glue_df_summer_hypolimnetic_ave_rcp26.sort_index()
glue_df_summer_hypolimnetic_ave_rcp60= glue_df_summer_hypolimnetic_ave_rcp60.sort_index()
glue_df_summer_hypolimnetic_ave_rcp85= glue_df_summer_hypolimnetic_ave_rcp85.sort_index()













#%%Plotting and analyses 



#%%########annual anoxic factor 

#%%ploting annual anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'], glue_df_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'], glue_df_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'], glue_df_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_hypolimnetic_ave_his['50%'])#6.077082662821386
np.mean(glue_df_annual_hypolimnetic_ave_rcp26['50%'])#7.992767795524755
np.mean(glue_df_annual_hypolimnetic_ave_rcp60['50%'])#8.585258963812871
np.mean(glue_df_annual_hypolimnetic_ave_rcp85['50%'])#9.156680524881311

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['50%']
annual_hypolimnetic_ave_ref=np.mean(glue_base_annual_hypolimnetic_ave_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2029 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp26)
# 8.070525139552648
glue_near_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2029 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp60)
# 8.107889314159742
glue_near_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2029 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2069 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp26)
#8.153608896799094
glue_distant_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2069 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp60)
#9.787975473676404
glue_distant_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2069 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp85)
#10.985644903398574
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_hypolimnetic_ave_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp85)
(0.014499198182054042,
 'positively autocorrelated',
 'increasing',
 0.026946782463489027,
 0.05377923636923881,
 10.323144222989352)






#%% 80 years from 2020 for annual_hypolimnetic_ave


glue_80years_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[2019 < glue_df_annual_hypolimnetic_ave_rcp26.index]

glue_80years_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[2019 < glue_df_annual_hypolimnetic_ave_rcp60.index]

glue_80years_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[2019 < glue_df_annual_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index>2079]['50%'])
11.160292464667199

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)



autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp85['50%'])
(0.015711631920486826,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05742827331247126,
 7.128166722990812)





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85['50%'])
(0.01670964657273115,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05615663487366421,
 6.386209763383056)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index)]['5%'] - annual_hypolimnetic_ave_ref,
                      glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index) ]['95%'] - annual_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_annual_hypolimnetic_ave_his[(1960 < glue_df_annual_hypolimnetic_ave_his.index)]['50%'] - annual_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp26['95%']-annual_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%']-annual_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%']-annual_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%']-annual_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%']-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%']-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of annual hypolimnetic DO [mg L$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')











#%%===========May-Nov average of anoxic afctor 


#%%ploting May_Nov anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_his.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_his['5%'], glue_df_May_Nov_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_his.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['5%'], glue_df_May_Nov_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['5%'], glue_df_May_Nov_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['5%'], glue_df_May_Nov_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anoxic factor May-Nov [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_May_Nov_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_May_Nov_hypolimnetic_ave_his['50%'])#6.077082662821386
np.mean(glue_df_May_Nov_hypolimnetic_ave_rcp26['50%'])#7.992767795524755
np.mean(glue_df_May_Nov_hypolimnetic_ave_rcp60['50%'])#8.585258963812871
np.mean(glue_df_May_Nov_hypolimnetic_ave_rcp85['50%'])#9.149586881905822

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_May_Nov_hypolimnetic_ave_his=glue_df_May_Nov_hypolimnetic_ave_his[1975 < glue_df_May_Nov_hypolimnetic_ave_his.index]['50%']
May_Nov_hypolimnetic_ave_ref=np.mean(glue_base_May_Nov_hypolimnetic_ave_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26[(2029 < glue_df_May_Nov_hypolimnetic_ave_rcp26.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_May_Nov_hypolimnetic_ave_rcp26)
# 8.070525139552648
glue_near_future_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60[(2029 < glue_df_May_Nov_hypolimnetic_ave_rcp60.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_May_Nov_hypolimnetic_ave_rcp60)
# 8.107889314159742
glue_near_future_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85[(2029 < glue_df_May_Nov_hypolimnetic_ave_rcp85.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_May_Nov_hypolimnetic_ave_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26[(2069 < glue_df_May_Nov_hypolimnetic_ave_rcp26.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_May_Nov_hypolimnetic_ave_rcp26)
#8.153608896799094
glue_distant_future_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60[(2069 < glue_df_May_Nov_hypolimnetic_ave_rcp60.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_May_Nov_hypolimnetic_ave_rcp60)
#9.787975473676404
glue_distant_future_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85[(2069 < glue_df_May_Nov_hypolimnetic_ave_rcp85.index) & (glue_df_May_Nov_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_May_Nov_hypolimnetic_ave_rcp85)
#10.963418155408705
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_May_Nov_hypolimnetic_ave_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Nov_hypolimnetic_ave_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Nov_hypolimnetic_ave_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_May_Nov_hypolimnetic_ave_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Nov_hypolimnetic_ave_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Nov_hypolimnetic_ave_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_May_Nov_hypolimnetic_ave_rcp85)
(0.014377923696788013,
 'positively autocorrelated',
 'increasing',
 0.0322801899241516,
 0.04781875151369361,
 10.409571253394757)






#%% 80 years from 2020 for May_Nov_hypolimnetic_ave


glue_80years_May_Nov_hypolimnetic_ave_rcp26=glue_df_May_Nov_hypolimnetic_ave_rcp26[2019 < glue_df_May_Nov_hypolimnetic_ave_rcp26.index]

glue_80years_May_Nov_hypolimnetic_ave_rcp60=glue_df_May_Nov_hypolimnetic_ave_rcp60[2019 < glue_df_May_Nov_hypolimnetic_ave_rcp60.index]

glue_80years_May_Nov_hypolimnetic_ave_rcp85=glue_df_May_Nov_hypolimnetic_ave_rcp85[2019 < glue_df_May_Nov_hypolimnetic_ave_rcp85.index]



#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp26[glue_80years_May_Nov_hypolimnetic_ave_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp60[glue_80years_May_Nov_hypolimnetic_ave_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp85[glue_80years_May_Nov_hypolimnetic_ave_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp26[glue_80years_May_Nov_hypolimnetic_ave_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp60[glue_80years_May_Nov_hypolimnetic_ave_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_May_Nov_hypolimnetic_ave_rcp85[glue_80years_May_Nov_hypolimnetic_ave_rcp85.index>2079]['50%'])
11.12826268210691

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)


autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp85['50%'])
(0.015654880429522035,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05661191309631117,
 7.160412951529136)

#%%plotting May_Nov anoxic factor over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp26['5%'], glue_80years_May_Nov_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp60['5%'], glue_80years_May_Nov_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp85['5%'], glue_80years_May_Nov_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_May_Nov_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_May_Nov_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('anoxic factor in May_Nov [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_May_Nov_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)


#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_May_Nov_hypolimnetic_ave_rcp85['50%'])
(0.016659625265317696,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05578367086692144,
 6.403552589696595)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_his[(1960 < glue_df_May_Nov_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_May_Nov_hypolimnetic_ave_his[(1960 < glue_df_May_Nov_hypolimnetic_ave_his.index)]['5%'] - May_Nov_hypolimnetic_ave_ref,
                      glue_df_May_Nov_hypolimnetic_ave_his[(1960 < glue_df_May_Nov_hypolimnetic_ave_his.index) ]['95%'] - May_Nov_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_his[(1960 < glue_df_May_Nov_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_May_Nov_hypolimnetic_ave_his[(1960 < glue_df_May_Nov_hypolimnetic_ave_his.index)]['50%'] - May_Nov_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['5%']-May_Nov_hypolimnetic_ave_ref, glue_df_May_Nov_hypolimnetic_ave_rcp26['95%']-May_Nov_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp26.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp26['50%']-May_Nov_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['5%']-May_Nov_hypolimnetic_ave_ref, glue_df_May_Nov_hypolimnetic_ave_rcp60['95%']-May_Nov_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp60.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp60['50%']-May_Nov_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['5%']-May_Nov_hypolimnetic_ave_ref, glue_df_May_Nov_hypolimnetic_ave_rcp85['95%']-May_Nov_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_May_Nov_hypolimnetic_ave_rcp85.index.astype(float), glue_df_May_Nov_hypolimnetic_ave_rcp85['50%']-May_Nov_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of anoxic factor in May-Nov [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_May_Nov_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')













#%%===========summer average of anoxic afctor 


#%%########summer anoxic factor 

#%%ploting summer anoxic factor 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['5%'], glue_df_summer_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%'], glue_df_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%'], glue_df_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%'], glue_df_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anoxic factor in summer [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_summer_hypolimnetic_ave_his['50%'])#5.7419538116211175
np.mean(glue_df_summer_hypolimnetic_ave_rcp26['50%'])#7.164633836912792
np.mean(glue_df_summer_hypolimnetic_ave_rcp60['50%'])#7.660016638342764
np.mean(glue_df_summer_hypolimnetic_ave_rcp85['50%'])#7.798265277646058

#%%anoxic_factor 30 yerars from each scenarios compare 



#anormaly 
# baseline [1976-2005]
glue_base_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his[1975 < glue_df_summer_hypolimnetic_ave_his.index]['50%']
summer_hypolimnetic_ave_ref=np.mean(glue_base_summer_hypolimnetic_ave_his)
#5.830216997377137


#near future [2030-2059]

glue_near_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2029 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp26)
# 7.189791199644448
glue_near_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2029 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp60)
# 7.408290028941934
glue_near_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2029 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_summer_hypolimnetic_ave_rcp85)
# 7.577321792421727

 
#Distant future [2070-2099]

glue_distant_future_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[(2069 < glue_df_summer_hypolimnetic_ave_rcp26.index) & (glue_df_summer_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp26)
#7.182315856408658
glue_distant_future_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[(2069 < glue_df_summer_hypolimnetic_ave_rcp60.index) & (glue_df_summer_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp60)
#8.404224632950019
glue_distant_future_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[(2069 < glue_df_summer_hypolimnetic_ave_rcp85.index) & (glue_df_summer_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_summer_hypolimnetic_ave_rcp85)
#8.844476856722357
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_summer_hypolimnetic_ave_his)
(0.03384344872449237,
 'positively autocorrelated',
 'no trend',
 0.2389927879015219,
 0,
 0)


#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp26)
(0.017426799559486894,
 'positively autocorrelated',
 'no trend',
 0.2686642304239091,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp60)
(0.011027838419972513,
 'positively autocorrelated',
 'no trend',
 0.08039114754218035,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_summer_hypolimnetic_ave_rcp85)

(0.010531400508757774,
 'positively autocorrelated',
 'increasing',
 0.0053825476031263975,
 0.0337942438328447,
 7.0319428173255965)


#Distant future [2070-2099]

#rcp26
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp26)
(0.007455597611559313,
 'positively autocorrelated',
 'increasing',
 0.011479484705922305,
 0.03254964585051723,
 6.704083850293537)
#rcp60
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp60)
(0.005218209926031563,
 'positively autocorrelated',
 'no trend',
 0.7752944295177846,
 0,
 0)
#rcp85
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_summer_hypolimnetic_ave_rcp85)
(0.011260089055346817,
 'positively autocorrelated',
 'no trend',
 0.2844114676220473,
 0,
 0)





#%% 80 years from 2020 for summer_hypolimnetic_ave


glue_80years_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26[2019 < glue_df_summer_hypolimnetic_ave_rcp26.index]

glue_80years_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60[2019 < glue_df_summer_hypolimnetic_ave_rcp60.index]

glue_80years_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85[2019 < glue_df_summer_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index<2030]['50%'])
7.236131611808827

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index<2030]['50%'])
7.0480838080216754

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index<2030]['50%'])
6.92973720099211

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_summer_hypolimnetic_ave_rcp26[glue_80years_summer_hypolimnetic_ave_rcp26.index>2079]['50%'])
7.284732847455828

#rcp6.0
np.mean(glue_80years_summer_hypolimnetic_ave_rcp60[glue_80years_summer_hypolimnetic_ave_rcp60.index>2079]['50%'])
8.376808940760498

#rcp8.5
np.mean(glue_80years_summer_hypolimnetic_ave_rcp85[glue_80years_summer_hypolimnetic_ave_rcp85.index>2079]['50%'])
8.902897713112784

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp26['50%'])
(0.012431261551918694,
 'positively autocorrelated',
 'no trend',
 0.4722909038902814,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
(0.009054412557226742,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.021466406502838986,
 6.936654760438897)


autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
(0.012767144112602902,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031086674796400225,
 6.7697952941890875)



#%%plotting summer anoxic factor over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['5%'], glue_80years_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['5%'], glue_80years_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p = {trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['5%'], glue_80years_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p = {trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('Anoxic factor in summer [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_summer_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire scenario

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_his['50%'])
(0.050102399473259764,
 'positively autocorrelated',
 'no trend',
 0.15346389188435516,
 0,
 0)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp26['50%'])
(0.011480536925277993,
 'positively autocorrelated',
 'increasing',
 0.030392451085676786,
 0.0039129273367328335,
 6.963469344761228)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp60['50%'])
(0.010198727721089741,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.02131982928372496,
 6.689481345978918)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_summer_hypolimnetic_ave_rcp85['50%'])
(0.014688565156364046,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.031748328950495945,
 6.343632396381782)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['5%'] - summer_hypolimnetic_ave_ref,
                      glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ]['95%'] - summer_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_summer_hypolimnetic_ave_his[(1960 < glue_df_summer_hypolimnetic_ave_his.index)]['50%'] - summer_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp26['95%']-summer_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%']-summer_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp60['95%']-summer_hypolimnetic_ave_ref, color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%']-summer_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp85['95%']-summer_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%']-summer_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of anoxic factor in summer [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave_anormaly.png",  dpi=300, bbox_inches='tight')










#%%
####################################old one
############################################
############################################

#%% Annual anoxic factor_gfdl_his
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_gfdl_rcp26
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_rcp26

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_gfdl_rcp60
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_rcp60

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_gfdl_rcp85
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_gfdl_rcp85

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_gfdl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxic factor_hadgem_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_hadgem_rcp26
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_rcp26

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_hadgem_rcp60
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_rcp60

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_hadgem_rcp85
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_hadgem_rcp85

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_hadgem_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual anoxic factor_ipsl_his
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_his

# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_ipsl_rcp26
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp26

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_ipsl_rcp60
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp60

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_ipsl_rcp85
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp85

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_ipsl_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_his

# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'



####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_his_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual anoxic factor_miroc_rcp26
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_rcp26

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp26_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual anoxic factor_miroc_rcp60
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_rcp60

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp60_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual anoxic factor_miroc_rcp85
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
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


#%%monthly_hypolimnetic_ave_miroc_rcp85

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
    if filename.endswith(".csv") and filename.startswith("DO_prof_miroc_rcp85_Jv_"):
        
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
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
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



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'


####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'     

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_his= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_anoxic_factor_his.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_fixedtheta/glue_df_anoxic_factor_his.csv')



####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_his.csv')

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



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp26= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp26.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp26.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp26.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp26.csv')



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



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp60= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp60.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp60.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp60.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp60.csv')



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



all_annual_hypolimnetic_ave= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

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
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        read_header_df = pd.read_csv(os.path.join(directory, filename), nrows=1)
        jv_value = read_header_df['Jv'].iloc[0]
        ja_value = read_header_df['Ja'].iloc[0]
        weights = read_header_df['weights'].iloc[0]
        
        all_weights= np.append(all_weights , weights) 
        
        
        # Read the DataFrame below the header
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename), skiprows=2)
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp85= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_anoxic_factor_rcp85.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_anoxic_factor_rcp85.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_anoxic_factor_rcp85.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_anoxic_factor_rcp85.csv')


#%%#######fixed theta:
    
#######glue_df_annual_hypolimnetic_ave_his_fixedtheta=  glue_df_annual_hypolimnetic_ave_his.copy()

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his_fixedtheta.copy()

#######glue_df_annual_hypolimnetic_ave_rcp26_fixedtheta=  glue_df_annual_hypolimnetic_ave_rcp26.copy()

glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26_fixedtheta.copy()

#######glue_df_annual_hypolimnetic_ave_rcp60_fixedtheta=  glue_df_annual_hypolimnetic_ave_rcp60.copy()

glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60_fixedtheta.copy()

#######glue_df_annual_hypolimnetic_ave_rcp85_fixedtheta=  glue_df_annual_hypolimnetic_ave_rcp85.copy()

glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85_fixedtheta.copy()



#%%_vartheta

glue_df_annual_hypolimnetic_ave_his_vartheta= glue_df_annual_hypolimnetic_ave_his.copy()



glue_df_annual_hypolimnetic_ave_rcp26_vartheta= glue_df_annual_hypolimnetic_ave_rcp26.copy()


glue_df_annual_hypolimnetic_ave_rcp60_vartheta= glue_df_annual_hypolimnetic_ave_rcp60.copy()


glue_df_annual_hypolimnetic_ave_rcp85_vartheta= glue_df_annual_hypolimnetic_ave_rcp85.copy()


#%%difference of Vartheta model and fixed theta 


diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his=glue_df_annual_hypolimnetic_ave_his_vartheta['50%']-glue_df_annual_hypolimnetic_ave_his['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his)
-1.521539830552154

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his)
(0.4102745697759908,
 'positively autocorrelated',
 'no trend',
 0.08641995700155558,
 0,
 0)




diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26=glue_df_annual_hypolimnetic_ave_rcp26_vartheta['50%']-glue_df_annual_hypolimnetic_ave_rcp26['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26)
-2.3009426195783225
autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26)

(0.2471291056619972,
 'positively autocorrelated',
 'no trend',
 0.5406757306713583,
 0,
 0)



diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60=glue_df_annual_hypolimnetic_ave_rcp60_vartheta['50%']-glue_df_annual_hypolimnetic_ave_rcp60['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60)
-1.3593195664094877

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60)
(0.45142216245912026,
 'positively autocorrelated',
 'no trend',
 0.24575216426645285,
 0,
 0)



diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85=glue_df_annual_hypolimnetic_ave_rcp85_vartheta['50%']-glue_df_annual_hypolimnetic_ave_rcp85['50%']
np.mean(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85)
-1.8403265395237618

autocorr_MK_org_modif_sens_slope_test(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85)
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


ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_his, 'grey', label='His median', alpha=1, linewidth=3 )


ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp26, 'green', label='RCP2.6 median', alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp60, 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )

ax=plt.plot(diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85.index, diff_median_annual_hypolimnetic_ave_vartheta_fixedtheta_rcp85, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )



ax=plt.ylabel('Difference of fixed and variable Ktemp assumption in simulating annual anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(-4, 3, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22)


####### test with fixed theta in calibration but variable for GOTM simulation 
fig.savefig("GLUE_Timeseries_hypolimnetic_DO_6combinationJaJv_ave_obs_4models_diff_fixed_var_theta.png", dpi=300, bbox_inches='tight')




#%% first 10 years 2020-2029

#rcp26
glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2019<glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26)
#7.470031426050075

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26_vartheta=glue_df_annual_hypolimnetic_ave_rcp26_vartheta[(2019<glue_df_annual_hypolimnetic_ave_rcp26_vartheta.index) & (glue_df_annual_hypolimnetic_ave_rcp26_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp26_vartheta)
#5.655030434919324


#rcp60

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2019<glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60)
#7.077280785340525



glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60_vartheta=glue_df_annual_hypolimnetic_ave_rcp60_vartheta[(2019<glue_df_annual_hypolimnetic_ave_rcp60_vartheta.index) & (glue_df_annual_hypolimnetic_ave_rcp60_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp60_vartheta)
#5.442294872796134

#rcp85

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2019<glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85)
#6.80621601212993

glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85_vartheta=glue_df_annual_hypolimnetic_ave_rcp85_vartheta[(2019<glue_df_annual_hypolimnetic_ave_rcp85_vartheta.index) & (glue_df_annual_hypolimnetic_ave_rcp85_vartheta.index<2030)]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_1st_10years_rcp85_vartheta)
#5.589130553716512

#%%last 10 years 2090-2099

#rcp26
glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[glue_df_annual_hypolimnetic_ave_rcp26.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26)
#8.613753815447875

glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26_vartheta=glue_df_annual_hypolimnetic_ave_rcp26_vartheta[glue_df_annual_hypolimnetic_ave_rcp26_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp26_vartheta)
#5.99974215818178

#rcp60
glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[glue_df_annual_hypolimnetic_ave_rcp60.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60)
#8.840670784774442

glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60_vartheta=glue_df_annual_hypolimnetic_ave_rcp60_vartheta[glue_df_annual_hypolimnetic_ave_rcp60_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp60_vartheta)
#7.461205289215991
#rcp85
glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[glue_df_annual_hypolimnetic_ave_rcp85.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85)
#10.848450635366076

glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85_vartheta=glue_df_annual_hypolimnetic_ave_rcp85_vartheta[glue_df_annual_hypolimnetic_ave_rcp85_vartheta.index>2089]['50%']
np.mean(glue_df_annual_hypolimnetic_ave_median_last_10years_rcp85_vartheta)
#9.225106418152142

#%% 100 years for rcps 

#rcp26

#fixed theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp26=pd.concat([glue_df_annual_hypolimnetic_ave_his[glue_df_annual_hypolimnetic_ave_his.index>1999] , glue_df_annual_hypolimnetic_ave_rcp26])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp26 ['50%'])  

(0.03233165257593502,
 'positively autocorrelated',
 'increasing',
 1.235052435877293e-07,
 0.0121937938499866,
 7.255097746966682)





#Var theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta=pd.concat([glue_df_annual_hypolimnetic_ave_his_vartheta[glue_df_annual_hypolimnetic_ave_his_vartheta.index>1999] , glue_df_annual_hypolimnetic_ave_rcp26_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta ['50%'])  

(0.03955505915646442,
 'positively autocorrelated',
 'increasing',
 0.0006010992236442636,
 0.010497984593900105,
 5.030834333984101)



#rcp60

#fixed theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp60=pd.concat([glue_df_annual_hypolimnetic_ave_his[glue_df_annual_hypolimnetic_ave_his.index>1999] , glue_df_annual_hypolimnetic_ave_rcp60])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp60 ['50%'])  
(0.02795672807292709,
 'positively autocorrelated',
 'increasing',
 2.220446049250313e-16,
 0.0332750689583886,
 5.986757230735907)




#Var theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta=pd.concat([glue_df_annual_hypolimnetic_ave_his_vartheta[glue_df_annual_hypolimnetic_ave_his_vartheta.index>1999] , glue_df_annual_hypolimnetic_ave_rcp60_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta ['50%'])  
(0.029177475988549587,
 'positively autocorrelated',
 'increasing',
 2.970956813896919e-13,
 0.03420571640423424,
 4.397863069746866)


#rcp85

#fixed theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp85=pd.concat([glue_df_annual_hypolimnetic_ave_his[glue_df_annual_hypolimnetic_ave_his.index>1999] , glue_df_annual_hypolimnetic_ave_rcp85])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp85 ['50%'])  
(0.031072004914250547,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05455817956023478,
 5.832292270455436)




#Var theta
glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta=pd.concat([glue_df_annual_hypolimnetic_ave_his_vartheta[glue_df_annual_hypolimnetic_ave_his_vartheta.index>1999] , glue_df_annual_hypolimnetic_ave_rcp85_vartheta])
autocorr_MK_org_modif_sens_slope_test( glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta ['50%'])  

(0.035580951696717295,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05165045008766002,
 3.9207344560109947)

#%% trendline sen's slope 

autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his['50%']) 

Out[1243]: 
(0.08861134396877238,
 'positively autocorrelated',
 'no trend',
 0.10192618852194646,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his_vartheta['50%']) 

(0.1383412609645987,
 'positively autocorrelated',
 'no trend',
 0.31072008139962315,
 0,
 0)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26['50%']) 
(0.03379118006876991,
 'positively autocorrelated',
 'increasing',
 6.908279212325397e-05,
 0.010564337601135008,
 7.4785025189153735)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26_vartheta['50%']) 
(0.039507716688300144,
 'positively autocorrelated',
 'increasing',
 0.022504355893704142,
 0.008218111766768784,
 5.1831384217248875)



autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60['50%']) 
(0.028720309370685593,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.03880652178553318,
 5.88161432295651)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60_vartheta['50%']) 
(0.028883853368500165,
 'positively autocorrelated',
 'increasing',
 7.286293790542686e-10,
 0.033514404467106934,
 4.616452079764355)


autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85['50%']) 
(0.03167796451466309,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.059792750353943616,
 5.873773932605548)
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85_vartheta['50%']) 
(0.03389759807269532,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05300685412619691,
 4.1760561507416)



#%%Plotiing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%Annual anoxic factor 

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


#ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26_vartheta['50%'])
ax=plt.text(2020, 10, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxic_factor_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


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


#ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
#ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp26['50%'])
ax=plt.text(2020, 15, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p < 0.05', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['95%'], color='yellow', alpha=0.2 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p < 0.05', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p < 0.05', color='r', fontsize= 20 )



ax=plt.ylabel('Anoxic factor per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_anoxic_factor_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




#%%
# original # fixed gcm temp in 2020 and 2021
np.mean(glue_df_annual_hypolimnetic_ave_his['50%'])#5.118056494914366# 5.371846482897608
np.mean(glue_df_annual_hypolimnetic_ave_rcp26['50%'])#7.009871810216667# 7.960074150018018
np.mean(glue_df_annual_hypolimnetic_ave_rcp60['50%'])#7.599031745432739# 7.661889247294462
np.mean(glue_df_annual_hypolimnetic_ave_rcp85['50%'])#8.15444840073441#8.680607289244922

np.mean(glue_df_annual_hypolimnetic_ave_his_vartheta['50%'])#3.8503066523454508
np.mean(glue_df_annual_hypolimnetic_ave_rcp26_vartheta['50%'])#5.659131530439698
np.mean(glue_df_annual_hypolimnetic_ave_rcp60_vartheta['50%'])#6.302569680884974
np.mean(glue_df_annual_hypolimnetic_ave_rcp85_vartheta['50%'])#6.840280749721157



#%%anoxic_factor 30 yerars from each scenarios compare 


#Sorting the glue dataframe according to the index (year)

glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.sort_index()

glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.sort_index()

glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.sort_index()

glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.sort_index()





#anormaly 

# baseline [1976-2005]
annual_hypolimnetic_ave_ref=glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['50%'].mean()

#5.410877320721374
#5.914740063212032


#near future [2030-2059] 

glue_df_annual_hypolimnetic_ave_rcp26[(2029 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2060)]['50%'].mean()
# 7.072947718287684
# 7.950218353351354
glue_df_annual_hypolimnetic_ave_rcp60[(2029 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2060)]['50%'].mean()
# 7.156265572954701
# 7.139975067233944

glue_df_annual_hypolimnetic_ave_rcp85[(2029 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2060)]['50%'].mean()
# 7.630745663516447
# 8.223867040126178
 
#Distant future [2070-2099]

glue_df_annual_hypolimnetic_ave_rcp26[(2069 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2100)]['50%'].mean()
#7.17035474380281
#8.221226628944514


glue_df_annual_hypolimnetic_ave_rcp60[(2069 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2100)]['50%'].mean()
#8.781804641713899
#8.984771173520228

glue_df_annual_hypolimnetic_ave_rcp85[(2069 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2100)]['50%'].mean()
#7.630745663516447
# 10.612461480324987



#%%anoxic_factor_anormaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index].index.astype(float),
                      glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['5%'].astype(float) - annual_hypolimnetic_ave_ref,
                      glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index ]['95%'].astype(float) - annual_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_annual_hypolimnetic_ave_his[(1975 < glue_df_annual_hypolimnetic_ave_his.index)]['50%'].astype(float) - annual_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'].astype(float)-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp26['95%'].astype(float)-annual_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'].astype(float)-annual_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'].astype(float)-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%'].astype(float)-annual_hypolimnetic_ave_ref, color='b', alpha=0.27 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'].astype(float)-annual_hypolimnetic_ave_ref, 'b', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'].astype(float)-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%'].astype(float)-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'].astype(float)-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anormaly of anoxic factor [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_anoxic_factor_anormaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


