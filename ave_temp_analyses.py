# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:51:59 2024

@author: mahta
"""


#%% annual hypolimnetic_ave_his

all_annual_temp_his=pd.DataFrame([])

#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):

        # Read from CSV
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_his = pd.concat([all_annual_temp_his , result], axis=1)
        
        
        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_his.csv'
        

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):

        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        
        
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_his = pd.concat([all_annual_temp_his , result], axis=1)

        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_his = pd.concat([all_annual_temp_his , result], axis=1)

        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_his = pd.concat([all_annual_temp_his , result], axis=1)

        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        


#%% GLUE method on all_annual_temp_his 
          

        
#all_annual_temp_his= all_annual_temp_his.set_index(all_annual_temp_his['Datetime'])


# annual anoxic duration  
timeseries_year_his= all_annual_temp_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_temp_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_temperature_his.csv')
        




#%% Apr_Oct hypolimnetic_ave_his

all_Apr_Oct_temp_his=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_gfdl_his"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_his = pd.concat([all_Apr_Oct_temp_his , result], axis=1)
        

        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_hadgem_his"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_his = pd.concat([all_Apr_Oct_temp_his , result], axis=1)
        

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_ipsl_his"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_his = pd.concat([all_Apr_Oct_temp_his , result], axis=1)
        

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_his.csv'
        
        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_miroc_his"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_his = pd.concat([all_Apr_Oct_temp_his , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        



#%% GLUE method on all_Apr_Oct_temp_his 
          

        
#all_Apr_Oct_temp_his= all_Apr_Oct_temp_his.set_index(all_Apr_Oct_temp_his['Datetime'])


# Apr_Oct anoxic duration  
timeseries_year_his= all_Apr_Oct_temp_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_temp_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_his=glue_df_Apr_Oct_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_temperature_his.csv')
        


#%% annual hypolimnetic_ave_rcp26

all_annual_temp_rcp26=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp26 = pd.concat([all_annual_temp_rcp26 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp26.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp26 = pd.concat([all_annual_temp_rcp26 , result], axis=1)
        

        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp26.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV

        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp26 = pd.concat([all_annual_temp_rcp26 , result], axis=1)
        

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp26.csv'
        


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp26 = pd.concat([all_annual_temp_rcp26 , result], axis=1)
        
        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp26.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
      

#%% GLUE method on all_annual_temp_rcp26 
          

        
#all_annual_temp_rcp26= all_annual_temp_rcp26.set_index(all_annual_temp_rcp26['Datetime'])


# annual anoxic duration  
timeseries_year_rcp26= all_annual_temp_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_temp_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_temperature_rcp26.csv')
        

#%% Apr_Oct hypolimnetic_ave_rcp26

all_Apr_Oct_temp_rcp26=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_gfdl_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp26 = pd.concat([all_Apr_Oct_temp_rcp26 , result], axis=1)
        

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_rcp26.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_hadgem_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp26 = pd.concat([all_Apr_Oct_temp_rcp26 , result], axis=1)

        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_rcp26.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_ipsl_rcp26"):
        
        # Read from CSV

        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp26 = pd.concat([all_Apr_Oct_temp_rcp26 , result], axis=1)
        
        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_rcp26.csv'
        
        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_miroc_rcp26"):
        
        # Read from CSV

        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp26 = pd.concat([all_Apr_Oct_temp_rcp26 , result], axis=1)

        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_rcp26.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        


#%% GLUE method on all_Apr_Oct_temp_rcp26 
          

        
#all_Apr_Oct_temp_rcp26= all_Apr_Oct_temp_rcp26.set_index(all_Apr_Oct_temp_rcp26['Datetime'])


# Apr_Oct anoxic duration  
timeseries_year_rcp26= all_Apr_Oct_temp_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_temp_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_temperature_rcp26.csv')
        

#%%%RCP6.0

#%% annual hypolimnetic_ave_rcp60

all_annual_temp_rcp60=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp60 = pd.concat([all_annual_temp_rcp60 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp60 = pd.concat([all_annual_temp_rcp60 , result], axis=1)

        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp60 = pd.concat([all_annual_temp_rcp60 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV

        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp60 = pd.concat([all_annual_temp_rcp60 , result], axis=1)
        

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        

#%% GLUE method on all_annual_temp_rcp60 
          

        
#all_annual_temp_rcp60= all_annual_temp_rcp60.set_index(all_annual_temp_rcp60['Datetime'])


# annual anoxic duration  
timeseries_year_rcp60= all_annual_temp_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_temp_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_temperature_rcp60.csv')
        

#%% Apr_Oct hypolimnetic_ave_rcp60

all_Apr_Oct_temp_rcp60=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_gfdl_rcp60"):
        
        # Read from CSV

        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp60 = pd.concat([all_Apr_Oct_temp_rcp60 , result], axis=1)
        

        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_rcp60.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_hadgem_rcp60"):
        
        # Read from CSV

        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp60 = pd.concat([all_Apr_Oct_temp_rcp60 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_rcp60.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_ipsl_rcp60"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp60 = pd.concat([all_Apr_Oct_temp_rcp60 , result], axis=1)
        

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_miroc_rcp60"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp60 = pd.concat([all_Apr_Oct_temp_rcp60 , result], axis=1)
        
        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        

#%% GLUE method on all_Apr_Oct_temp_rcp60 
          

        
#all_Apr_Oct_temp_rcp60= all_Apr_Oct_temp_rcp60.set_index(all_Apr_Oct_temp_rcp60['Datetime'])


# Apr_Oct anoxic duration  
timeseries_year_rcp60= all_Apr_Oct_temp_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_temp_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_temperature_rcp60.csv')
        

#%%RCP8.5


#%% annual hypolimnetic_ave_rcp85

all_annual_temp_rcp85=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp85 = pd.concat([all_annual_temp_rcp85 , result], axis=1)
        

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp85 = pd.concat([all_annual_temp_rcp85 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp85 = pd.concat([all_annual_temp_rcp85 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        all_annual_temp_rcp85 = pd.concat([all_annual_temp_rcp85 , result], axis=1)

        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        




#%% GLUE method on all_annual_temp_rcp85 
          

        
#all_annual_temp_rcp85= all_annual_temp_rcp85.set_index(all_annual_temp_rcp85['Datetime'])


# annual anoxic duration  
timeseries_year_rcp85= all_annual_temp_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_temp_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_temperature_rcp85.csv')
        

#%% Apr_Oct hypolimnetic_ave_rcp85

all_Apr_Oct_temp_rcp85=pd.DataFrame([])
all_weights= np.array([])


#gfdl

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_gfdl_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp85 = pd.concat([all_Apr_Oct_temp_rcp85 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
#hadgem               
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_hadgem_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp85 = pd.concat([all_Apr_Oct_temp_rcp85 , result], axis=1)

        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#ipsl       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_ipsl_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp85 = pd.concat([all_Apr_Oct_temp_rcp85 , result], axis=1)
        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
#miroc       
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("mixingincl_temp_prof_miroc_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the Apr_Oct_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series )

        all_Apr_Oct_temp_rcp85 = pd.concat([all_Apr_Oct_temp_rcp85 , result], axis=1)


        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_rcp85.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        


#%% GLUE method on all_Apr_Oct_temp_rcp85 
          

        
#all_Apr_Oct_temp_rcp85= all_Apr_Oct_temp_rcp85.set_index(all_Apr_Oct_temp_rcp85['Datetime'])


# Apr_Oct anoxic duration  
timeseries_year_rcp85= all_Apr_Oct_temp_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_temp_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_temperature_rcp85.csv')
        

#%%monthly_hypolimnetic_ave

#%%monthly_temp_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )


        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])


#%%monthly_hypolimnetic_ave_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 

#%%monthly_hypolimnetic_ave_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_hypolimnetic_ave_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%%monthly_hypolimnetic_ave_hadgem_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
 
#%%monthly_hypolimnetic_ave_hadgem_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_hadgem_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
   
#%%monthly_hypolimnetic_ave_hadgem_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl

#%%monthly_hypolimnetic_ave_ipsl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )


        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        

#%%monthly_hypolimnetic_ave_ipsl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_ipsl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%%monthly_hypolimnetic_ave_ipsl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85.csv'


        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
  
#%%monthly_hypolimnetic_ave_miroc_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV

        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
 
#%%monthly_hypolimnetic_ave_miroc_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%%monthly_hypolimnetic_ave_miroc_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])

#%%monthly_hypolimnetic_ave_miroc_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV

        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85.csv'

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        


#%%sorting the indexs_annual_hypolimnetic_ave 

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his.sort_index()
glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26.sort_index()
glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60.sort_index()
glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85.sort_index()


#%%sorting the indexs_Apr_Oct_hypolimnetic_ave 

glue_df_Apr_Oct_hypolimnetic_ave_his= glue_df_Apr_Oct_hypolimnetic_ave_his.sort_index()
glue_df_Apr_Oct_hypolimnetic_ave_rcp26= glue_df_Apr_Oct_hypolimnetic_ave_rcp26.sort_index()
glue_df_Apr_Oct_hypolimnetic_ave_rcp60= glue_df_Apr_Oct_hypolimnetic_ave_rcp60.sort_index()
glue_df_Apr_Oct_hypolimnetic_ave_rcp85= glue_df_Apr_Oct_hypolimnetic_ave_rcp85.sort_index()











#%%Plotting and analyses 



#%%########annual temp

#%%ploting annual temp

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'], glue_df_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'], glue_df_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'], glue_df_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Hypolimnetic temperature \nin each deoxygenation period [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22 , ncol=4)#)   
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_temp_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_annual_hypolimnetic_ave_his['50%'])#10.170975698325146
np.mean(glue_df_annual_hypolimnetic_ave_rcp26['50%'])#10.224875614759105
np.mean(glue_df_annual_hypolimnetic_ave_rcp60['50%'])#10.397738242266778
np.mean(glue_df_annual_hypolimnetic_ave_rcp85['50%'])#10.624017826059932

#%%temperature 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his[1975 < glue_df_annual_hypolimnetic_ave_his.index]['50%']
annual_hypolimnetic_ave_ref=np.mean(glue_base_annual_hypolimnetic_ave_his)
#9.94578914056355


#near future [2030-2059]

glue_near_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2029 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp26)
# 10.252336518132559
glue_near_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2029 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp60)
#10.380050110791306
glue_near_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2029 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_annual_hypolimnetic_ave_rcp85)
# 10.5276361166333

 
#Distant future [2070-2099]

glue_distant_future_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[(2069 < glue_df_annual_hypolimnetic_ave_rcp26.index) & (glue_df_annual_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp26)
#10.174414736788405
glue_distant_future_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[(2069 < glue_df_annual_hypolimnetic_ave_rcp60.index) & (glue_df_annual_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp60)
#10.554283108952978
glue_distant_future_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[(2069 < glue_df_annual_hypolimnetic_ave_rcp85.index) & (glue_df_annual_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_annual_hypolimnetic_ave_rcp85)
#10.86752815285299
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_annual_hypolimnetic_ave_his)
(0.010146870719503575,
 'positively autocorrelated',
 'no trend',
 0.5206932698330875,
 0,
 0)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp26)
(0.00394672461253693,
 'positively autocorrelated',
 'no trend',
 0.2535263593015791,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp60)
(0.004294986492726307,
 'positively autocorrelated',
 'no trend',
 0.5206932698330875,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_annual_hypolimnetic_ave_rcp85)
(0.007221761983087712,
 'positively autocorrelated',
 'no trend',
 0.2844114676220473,
 0,
 0)


#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp26)
(0.005689260677840264,
 'positively autocorrelated',
 'no trend',
 0.7481053914270006,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp60)
(0.002656796426119481,
 'positively autocorrelated',
 'no trend',
 0.3353389634847317,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_annual_hypolimnetic_ave_rcp85)
(0.00687106317152284,
 'positively autocorrelated',
 'no trend',
 0.5206932698330875,
 0,
 0)





#%% 80 years from 2020 for annual_hypolimnetic_ave


glue_80years_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26[2019 < glue_df_annual_hypolimnetic_ave_rcp26.index]

glue_80years_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60[2019 < glue_df_annual_hypolimnetic_ave_rcp60.index]

glue_80years_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85[2019 < glue_df_annual_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index<2030]['50%'])
10.447882416112016

#2020, 2021:
    

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index<2030]['50%'])
10.042853480093452

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index<2030]['50%'])
10.554501751187365

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_annual_hypolimnetic_ave_rcp26[glue_80years_annual_hypolimnetic_ave_rcp26.index>2089]['50%'])
10.255518954463678

#rcp6.0
np.mean(glue_80years_annual_hypolimnetic_ave_rcp60[glue_80years_annual_hypolimnetic_ave_rcp60.index>2089]['50%'])
10.444091404723286

#rcp8.5
np.mean(glue_80years_annual_hypolimnetic_ave_rcp85[glue_80years_annual_hypolimnetic_ave_rcp85.index>2089]['50%'])
11.10752051110289

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp26['50%'])
(0.006976032159904319,
 'positively autocorrelated',
 'no trend',
 0.5088744343515299,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp60['50%'])
(0.004609894081441866,
 'positively autocorrelated',
 'no trend',
 0.08698224793375631,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp85['50%'])
0.006549647882369905,
 'positively autocorrelated',
 'increasing',
 0.029788714455492027,
 0.00745940389570332,
 10.356474294251887)


#%%plotting annual temperature over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp26['5%'], glue_80years_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp26['50%'])
#ax=plt.text(2020, 7, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value ={trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot([2021, 2020],[14,14], color= 'white',label=' ')



ax=plt.fill_between(glue_80years_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp60['5%'], glue_80years_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp60['50%'])
#ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value <0.0001', color='gold', fontsize= 20 )

ax=plt.plot([2021, 2020],[14,14],
        linestyle='--', color='white', alpha=0.9, linewidth=3, label=' ')


ax=plt.fill_between(glue_80years_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp85['5%'], glue_80years_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_annual_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 14.5, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value ={trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_annual_hypolimnetic_ave_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3, label='RCP8.5 trendline')



ax=plt.ylabel('Hypolimnetic temperature in deoxygenation period [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1, -0.2), fontsize=22, ncol= 3)#)   
fig.savefig("GLUE_Timeseries_80years_annual_hypolimnetic_temp_ave.png",  dpi=300, bbox_inches='tight')


#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_his['50%'])
(0.006652178308854033,
 'positively autocorrelated',
 'decreasing',
 0.008016385542677362,
 -0.0032817906986939635,
 10.416458099617214)

#in intire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp26['50%'])
(0.006463213058262786,
 'positively autocorrelated',
 'no trend',
 0.43693905240401065,
 0,
 0)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp60['50%'])
(0.004630666976598362,
 'positively autocorrelated',
 'no trend',
 0.06430763469290146,
 0,
 0)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_rcp85['50%'])
(0.006544293572025691,
 'positively autocorrelated',
 'increasing',
 0.0003980520263278109,
 0.0070089164258447505,
 10.259756484713082)

#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%temperature_anomaly 
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
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%']-annual_hypolimnetic_ave_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%']-annual_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%']-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%']-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of hypolimnetic temperature [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_temp_ave_anomaly.png",  dpi=300, bbox_inches='tight')












#%%ploting Apr_Oct temperature 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_his.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_his['5%'], glue_df_Apr_Oct_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_his.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['5%'], glue_df_Apr_Oct_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['5%'], glue_df_Apr_Oct_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['5%'], glue_df_Apr_Oct_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Deep temperature in Apr-Oct [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)#)   
fig.savefig("GLUE_Timeseries_Apr_Oct_hypolimnetic_temp_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_his['50%'])# 9.311637252008202
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%'])#9.770223035713588
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%'])#9.993953342950217
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%'])#10.260605505028932

#%%temperature 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_Apr_Oct_hypolimnetic_ave_his=glue_df_Apr_Oct_hypolimnetic_ave_his[1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index]['50%']
Apr_Oct_hypolimnetic_ave_ref=np.mean(glue_base_Apr_Oct_hypolimnetic_ave_his)
#9.150192403369203


#near future [2030-2059]

glue_near_future_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26[(2029 < glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp26)
#9.792386491881938
glue_near_future_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60[(2029 < glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp60)
# 9.93742829824252
glue_near_future_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85[(2029 < glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp85)
# 10.157851222991786

 
#Distant future [2070-2099]

glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26[(2069 < glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp26)
#9.760966209026064
glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60[(2069 < glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp60)
#10.308558789203087
glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85[(2069 < glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp85)
#10.632349047277517
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_Apr_Oct_hypolimnetic_ave_his)
(0.004378302669327523,
 'positively autocorrelated',
 'no trend',
 0.8304750241244809,
 0,
 0)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp26)
(0.0030727768350840693,
 'positively autocorrelated',
 'no trend',
 0.5924901808547871,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp60)
(0.0024720713266663486,
 'positively autocorrelated',
 'no trend',
 0.2686642304239091,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp85)

(0.0025681583254929213,
 'positively autocorrelated',
 'no trend',
 0.30909117948885356,
 0,
 0)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp26)
(0.00360638157300963,
 'positively autocorrelated',
 'no trend',
 0.4977975765265772,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp60)
(0.00256626374809534,
 'positively autocorrelated',
 'no trend',
 0.6685166224807093,
 0,
 0)
autocorr_MK_org_modif_sens_slope_test(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp85)
(0.006142397048613383,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)




#%% 80 years from 2020 for Apr_Oct_hypolimnetic_ave


glue_80years_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26[2019 < glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index]

glue_80years_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60[2019 < glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index]

glue_80years_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85[2019 < glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26[glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index<2030]['50%'])
9.858636724466312

#rcp6.0
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60[glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index<2030]['50%'])
9.66360456951937

#rcp8.5
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85[glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index<2030]['50%'])
10.183440255199654

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26[glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index>2089]['50%'])
9.94448375288383

#rcp6.0
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60[glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index>2089]['50%'])
10.250584698300083

#rcp8.5
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85[glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index>2089]['50%'])
10.920014921832085

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['50%'])
(0.003977885379262978,
 'positively autocorrelated',
 'no trend',
 0.9040987949483423,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['50%'])
(0.003474657659919147,
 'positively autocorrelated',
 'increasing',
 3.974429574515881e-05,
 0.009415787926752734,
 9.71205588235245)

autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['50%'])
(0.004435276630191254,
 'positively autocorrelated',
 'increasing',
 0.0022702618421353016,
 0.008987615840257222,
 9.944025030771572)

#%%plotting Apr_Oct temperature over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['5%'], glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['50%'])
#ax=plt.text(2020, 7, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value ={trendline_rcp26[-3]:.3f}', color='green', fontsize= 20 )

ax=plt.plot([2021, 2020],[14,14], color= 'white',label=' ')



ax=plt.fill_between(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['5%'], glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value <0.0001', color='gold', fontsize= 20 )

ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float),
        trendline_rcp60[-2] * np.arange(80) + trendline_rcp60[-1],
        linestyle='--', color='yellow', alpha=0.9, linewidth=3, label='RCP6.0 trendline')


ax=plt.fill_between(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['5%'], glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 13.5, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value ={trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )


ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float),
        trendline_rcp85[-2] * np.arange(80) + trendline_rcp85[-1],
        linestyle='--', color='r', alpha=0.9, linewidth=3, label='RCP8.5 trendline')



ax=plt.ylabel('Deep temperature in Apr-Oct [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1, -0.2), fontsize=22, ncol= 3)#)   
fig.savefig("GLUE_Timeseries_80years_Apr_Oct_hypolimnetic_temp_ave.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_his['50%'])
(0.003589403899680557,
 'positively autocorrelated',
 'decreasing',
 0.005178976764409038,
 -0.002280134534835113,
 9.47534663805256)
#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%'])
(0.004035435876423928,
 'positively autocorrelated',
 'no trend',
 0.4330958512983918,
 0,
 0)

#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%'])
(0.003589031968967494,
 'positively autocorrelated',
 'increasing',
 8.698572684373573e-07,
 0.009113215174071414,
 9.635994925208937)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%'])
(0.004433120260985229,
 'positively autocorrelated',
 'increasing',
 1.7972246553199511e-06,
 0.011226324396100548,
 9.705604576461376)
#slope in entire RCP8.5> RCP6.0> his (decreasinggg temperature ????) , rcp2.6 no trend 



 
#%%temperature_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index)]['5%'] - Apr_Oct_hypolimnetic_ave_ref,
                      glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index) ]['95%'] - Apr_Oct_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index)]['50%'] - Apr_Oct_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['5%']-Apr_Oct_hypolimnetic_ave_ref, glue_df_Apr_Oct_hypolimnetic_ave_rcp26['95%']-Apr_Oct_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%']-Apr_Oct_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['5%']-Apr_Oct_hypolimnetic_ave_ref, glue_df_Apr_Oct_hypolimnetic_ave_rcp60['95%']-Apr_Oct_hypolimnetic_ave_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%']-Apr_Oct_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['5%']-Apr_Oct_hypolimnetic_ave_ref, glue_df_Apr_Oct_hypolimnetic_ave_rcp85['95%']-Apr_Oct_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%']-Apr_Oct_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('Anomaly of deep temperature in Apr-Oct [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(1.1, -0.2), fontsize=22, ncol=4)  
fig.savefig("GLUE_Timeseries_Apr_Oct_hypolimnetic_temp_ave_anomaly.png",  dpi=300, bbox_inches='tight')












#%%%%%%%%======================
#============OLD
#############
#%% Annual temperature_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% Apr_Oct temperature_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_gfdl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_gfdl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_gfdl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% Apr_Oct temperature_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_gfdl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_gfdl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_gfdl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_gfdl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_gfdl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_gfdl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_gfdl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_gfdl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_gfdl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_gfdl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%%hadgem

#%% Annual temperature_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% Apr_Oct temperature_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_hadgem_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_hadgem_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_hadgem_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% Apr_Oct temperature_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_hadgem_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_hadgem_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_hadgem_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_hadgem_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_hadgem_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_hadgem_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_hadgem_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_hadgem_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_hadgem_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_hadgem_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%ipsl
#%% Annual temperature_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% Apr_Oct temperature_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_ipsl_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_ipsl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_ipsl_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% Apr_Oct temperature_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_ipsl_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_ipsl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_ipsl_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_ipsl_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_ipsl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_ipsl_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_ipsl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_ipsl_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_ipsl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_ipsl_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
#%%miroc 
#%% Annual temperature_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                

#%% Apr_Oct temperature_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_miroc_his
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_miroc_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_miroc_his

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
#%% Apr_Oct temperature_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_miroc_rcp26
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_miroc_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                


                


#%%monthly_hypolimnetic_ave_miroc_rcp26

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_miroc_rcp60
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_miroc_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                










#%%monthly_hypolimnetic_ave_miroc_rcp60

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                
#%% Apr_Oct temperature_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = Apr_Oct_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'Apr_Oct_hypolimnetic_temp_ave_miroc_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['Apr_Oct_hypolimnetic_ave'])
        
                
#%% summer temperature_miroc_rcp85
# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = summer_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'summer_hypolimnetic_temp_ave_miroc_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['summer_hypolimnetic_ave'])
        
                




#%%monthly_hypolimnetic_ave_miroc_rcp85

# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series A0=23.67*10**6 , threshold=2)

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
            
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_his = pd.concat([all_annual_hypolimnetic_ave_his , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_temperature_his.csv')


#%%rcp26_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_annual_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp26 = pd.concat([all_annual_hypolimnetic_ave_rcp26 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_temperature_rcp26.csv')


#%%rcp60_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_annual_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp60 = pd.concat([all_annual_hypolimnetic_ave_rcp60 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_temperature_rcp60.csv')

#%%rcp85_annual_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_annual_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave.index)
        
        all_annual_hypolimnetic_ave_rcp85 = pd.concat([all_annual_hypolimnetic_ave_rcp85 , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("annual_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_temperature_rcp85.csv')




#%%sorting the indexs_annual_hypolimnetic_ave 

glue_df_annual_hypolimnetic_ave_his= glue_df_annual_hypolimnetic_ave_his.sort_index()
glue_df_annual_hypolimnetic_ave_rcp26= glue_df_annual_hypolimnetic_ave_rcp26.sort_index()
glue_df_annual_hypolimnetic_ave_rcp60= glue_df_annual_hypolimnetic_ave_rcp60.sort_index()
glue_df_annual_hypolimnetic_ave_rcp85= glue_df_annual_hypolimnetic_ave_rcp85.sort_index()


#%% Apr_Oct temperature
#%%his_Apr_Oct_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_Apr_Oct_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_his = pd.concat([all_Apr_Oct_hypolimnetic_ave_his , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_his = pd.concat([all_Apr_Oct_hypolimnetic_ave_his , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_his = pd.concat([all_Apr_Oct_hypolimnetic_ave_his , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_his = pd.concat([all_Apr_Oct_hypolimnetic_ave_his , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        
        
all_Apr_Oct_hypolimnetic_ave_his= all_Apr_Oct_hypolimnetic_ave_his.set_index(Apr_Oct_hypolimnetic_ave['year'])


# Apr_Oct anoxic duration  
timeseries_year_his= all_Apr_Oct_hypolimnetic_ave_his.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_hypolimnetic_ave_his.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_his=glue_df_Apr_Oct_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_temperature_his.csv')


#%%rcp26_Apr_Oct_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_Apr_Oct_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp26 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp26 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp26 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp26 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp26 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp26 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp26 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp26 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        
        

all_Apr_Oct_hypolimnetic_ave_rcp26= all_Apr_Oct_hypolimnetic_ave_rcp26.set_index(Apr_Oct_hypolimnetic_ave['year'])

# Apr_Oct anoxic duration  
timeseries_year_rcp26= all_Apr_Oct_hypolimnetic_ave_rcp26.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_hypolimnetic_ave_rcp26.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_temperature_rcp26.csv')


#%%rcp60_Apr_Oct_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_Apr_Oct_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp60 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp60 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp60 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp60 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp60 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp60 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp60 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp60 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        
        

all_Apr_Oct_hypolimnetic_ave_rcp60= all_Apr_Oct_hypolimnetic_ave_rcp60.set_index(Apr_Oct_hypolimnetic_ave['year'])

# Apr_Oct anoxic duration  
timeseries_year_rcp60= all_Apr_Oct_hypolimnetic_ave_rcp60.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_hypolimnetic_ave_rcp60.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_temperature_rcp60.csv')

#%%rcp85_Apr_Oct_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_Apr_Oct_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp85 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp85 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp85 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp85 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp85 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp85 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("Apr_Oct_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        Apr_Oct_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        Apr_Oct_hypolimnetic_ave=Apr_Oct_hypolimnetic_ave.set_index(Apr_Oct_hypolimnetic_ave.index)
        
        all_Apr_Oct_hypolimnetic_ave_rcp85 = pd.concat([all_Apr_Oct_hypolimnetic_ave_rcp85 , Apr_Oct_hypolimnetic_ave['Apr_Oct_hypolimnetic_ave']], axis=1)
        
        
        
        
all_Apr_Oct_hypolimnetic_ave_rcp85= all_Apr_Oct_hypolimnetic_ave_rcp85.set_index(Apr_Oct_hypolimnetic_ave['year'])


# Apr_Oct anoxic duration  
timeseries_year_rcp85= all_Apr_Oct_hypolimnetic_ave_rcp85.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_Apr_Oct_hypolimnetic_ave_rcp85.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_Apr_Oct_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_Apr_Oct_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_temperature_rcp85.csv')



#%%sorting the indexs_Apr_Oct_hypolimnetic_ave 

glue_df_Apr_Oct_hypolimnetic_ave_his= glue_df_Apr_Oct_hypolimnetic_ave_his.sort_index()
glue_df_Apr_Oct_hypolimnetic_ave_rcp26= glue_df_Apr_Oct_hypolimnetic_ave_rcp26.sort_index()
glue_df_Apr_Oct_hypolimnetic_ave_rcp60= glue_df_Apr_Oct_hypolimnetic_ave_rcp60.sort_index()
glue_df_Apr_Oct_hypolimnetic_ave_rcp85= glue_df_Apr_Oct_hypolimnetic_ave_rcp85.sort_index()



#%%===== summer temperature Glue dataframe 

#%%his_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'
all_summer_hypolimnetic_ave_his= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_his = pd.concat([all_summer_hypolimnetic_ave_his , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_summer_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_his=glue_df_summer_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_temperature_his.csv')


#%%rcp26_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp26'
all_summer_hypolimnetic_ave_rcp26= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp26 = pd.concat([all_summer_hypolimnetic_ave_rcp26 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp26'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp26=glue_df_summer_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/glue_df_temperature_rcp26.csv')


#%%rcp60_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp60'
all_summer_hypolimnetic_ave_rcp60= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp60 = pd.concat([all_summer_hypolimnetic_ave_rcp60 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp60'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp60=glue_df_summer_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/glue_df_temperature_rcp60.csv')

#%%rcp85_summer_hypolimnetic_ave


# Specify the directory where the CSV files are located
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/rcp85'
all_summer_hypolimnetic_ave_rcp85= pd.DataFrame([])
all_weights= np.array([])


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        summer_hypolimnetic_ave=summer_hypolimnetic_ave.set_index(summer_hypolimnetic_ave.index)
        
        all_summer_hypolimnetic_ave_rcp85 = pd.concat([all_summer_hypolimnetic_ave_rcp85 , summer_hypolimnetic_ave['summer_hypolimnetic_ave']], axis=1)
        
        
        

directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/rcp85'
        

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("summer_hypolimnetic_ave_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
         
        
        
        
        summer_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_summer_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_summer_hypolimnetic_ave_rcp85=glue_df_summer_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory
glue_df_summer_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/glue_df_temperature_rcp85.csv')


#%%sorting the indexs_summer_hypolimnetic_ave 

glue_df_summer_hypolimnetic_ave_his= glue_df_summer_hypolimnetic_ave_his.sort_index()
glue_df_summer_hypolimnetic_ave_rcp26= glue_df_summer_hypolimnetic_ave_rcp26.sort_index()
glue_df_summer_hypolimnetic_ave_rcp60= glue_df_summer_hypolimnetic_ave_rcp60.sort_index()
glue_df_summer_hypolimnetic_ave_rcp85= glue_df_summer_hypolimnetic_ave_rcp85.sort_index()













#%%Plotting and analyses 



#%%########annual temperature 

#%%ploting annual temperature 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['5%'], glue_df_annual_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_his.index.astype(float), glue_df_annual_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['5%'], glue_df_annual_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp26.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%'], glue_df_annual_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%'], glue_df_annual_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('temperature per each deoxygenation period [d/year]' , fontsize=26)
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

#%%temperature 30 yerars from each scenarios compare 



#anomaly 
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



 
#%%temperature_anomaly 
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
                      
                     
ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp60['95%']-annual_hypolimnetic_ave_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp60['50%']-annual_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['5%']-annual_hypolimnetic_ave_ref, glue_df_annual_hypolimnetic_ave_rcp85['95%']-annual_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_rcp85['50%']-annual_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of annual temperature [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_annual_hypolimnetic_ave_anomaly.png",  dpi=300, bbox_inches='tight')











#%%===========May-Sep average of temp


#%%ploting Apr_Oct temp

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_his.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_his['5%'], glue_df_Apr_Oct_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_his.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['5%'], glue_df_Apr_Oct_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['5%'], glue_df_Apr_Oct_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['5%'], glue_df_Apr_Oct_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('temperature May-Sep [d]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_Apr_Oct_hypolimnetic_ave.png",  dpi=300, bbox_inches='tight')




#%%
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_his['50%'])#6.077082662821386
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%'])#7.992767795524755
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%'])#8.585258963812871
np.mean(glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%'])#9.149586881905822

#%%temperature 30 yerars from each scenarios compare 



#anomaly 
# baseline [1976-2005]
glue_base_Apr_Oct_hypolimnetic_ave_his=glue_df_Apr_Oct_hypolimnetic_ave_his[1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index]['50%']
Apr_Oct_hypolimnetic_ave_ref=np.mean(glue_base_Apr_Oct_hypolimnetic_ave_his)
#6.389027950812897


#near future [2030-2059]

glue_near_future_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26[(2029 < glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index < 2060)]['50%']
np.mean(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp26)
# 8.070525139552648
glue_near_future_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60[(2029 < glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index < 2060)]['50%']
np.mean(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp60)
# 8.107889314159742
glue_near_future_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85[(2029 < glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index < 2060)]['50%']
np.mean(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp85)
# 8.63044924136971

 
#Distant future [2070-2099]

glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26[(2069 < glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index < 2100)]['50%']
np.mean(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp26)
#8.153608896799094
glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60[(2069 < glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index< 2100)]['50%']
np.mean(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp60)
#9.787975473676404
glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85[(2069 < glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index) & (glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index < 2100)]['50%']
np.mean(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp85)
#10.963418155408705
   


###====over 30 years in his and each RCPs 

# baseline [1976-2005]
autocorr_MK_org_modif_sens_slope_test(glue_base_Apr_Oct_hypolimnetic_ave_his)
(0.03791672471698212,
 'positively autocorrelated',
 'increasing',
 0.004067701513906119,
 0.04887120166082099,
 5.685266536515649)

#near future [2030-2059]


autocorr_MK_org_modif_sens_slope_test(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp26)
(0.018345477426765625,
 'positively autocorrelated',
 'no trend',
 0.09353135296636017,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp60)
(0.011313156566510486,
 'positively autocorrelated',
 'increasing',
 0.0007961960227531595,
 0.0470080311379157,
 7.4730648265627355)

autocorr_MK_org_modif_sens_slope_test(glue_near_future_Apr_Oct_hypolimnetic_ave_rcp85)

(0.01548644557384171,
 'positively autocorrelated',
 'increasing',
 0.0048191095611576085,
 0.05773266804253006,
 7.722484654253696)



#Distant future [2070-2099]


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp26)
(0.015039983618369416,
 'positively autocorrelated',
 'no trend',
 0.1989481007752456,
 0,
 0)

autocorr_MK_org_modif_sens_slope_test(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp60)
(0.012394095955031883,
 'positively autocorrelated',
 'no trend',
 0.41182433473249125,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_distant_future_Apr_Oct_hypolimnetic_ave_rcp85)
(0.014377923696788013,
 'positively autocorrelated',
 'increasing',
 0.0322801899241516,
 0.04781875151369361,
 10.409571253394757)






#%% 80 years from 2020 for Apr_Oct_hypolimnetic_ave


glue_80years_Apr_Oct_hypolimnetic_ave_rcp26=glue_df_Apr_Oct_hypolimnetic_ave_rcp26[2019 < glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index]

glue_80years_Apr_Oct_hypolimnetic_ave_rcp60=glue_df_Apr_Oct_hypolimnetic_ave_rcp60[2019 < glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index]

glue_80years_Apr_Oct_hypolimnetic_ave_rcp85=glue_df_Apr_Oct_hypolimnetic_ave_rcp85[2019 < glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index]


#============= mean of first 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26[glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index<2030]['50%'])
7.781968220542252

#rcp6.0
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60[glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index<2030]['50%'])
7.835574478598173

#rcp8.5
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85[glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index<2030]['50%'])
7.7236229767454985

#============== mean of last 10 yaers over 80 years 

#rcp2.6
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26[glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index>2079]['50%'])
8.243966830565041

#rcp6.0
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60[glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index>2079]['50%'])
9.864621453257977

#rcp8.5
np.mean(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85[glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index>2079]['50%'])
11.12826268210691

#=========== trendline # Over the 80 years


autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['50%'])
(0.02031492443906448,
 'positively autocorrelated',
 'no trend',
 0.11371844918011509,
 0,
 0)


autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['50%'])
(0.012504340139489645,
 'positively autocorrelated',
 'increasing',
 1.4566126083082054e-13,
 0.036058805989694846,
 7.282950340706922)


autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['50%'])
(0.015654880429522035,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05661191309631117,
 7.160412951529136)

#%%plotting Apr_Oct temp over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['5%'], glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['5%'], glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value ={trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['5%'], glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_Apr_Oct_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value ={trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('Deep temperature factor in Apr_Oct [°C]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_Timeseries_80years_Apr_Oct_deep_temp.png",  dpi=300, bbox_inches='tight')





#%%If there is a trend in entire 

# in whole his
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_his['50%'])
(0.054103668580385816,
 'positively autocorrelated',
 'no trend',
 0.07068845447209426,
 0,
 0)

#in entire rcp2.6
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%'])
(0.02002132148516097,
 'positively autocorrelated',
 'increasing',
 0.0012506240636172006,
 0.009277291512717471,
 7.539997545595559)


#in entire rcp6.0
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%'])
(0.01438079345143515,
 'positively autocorrelated',
 'increasing',
 2.6645352591003757e-13,
 0.03278504999647535,
 6.993374854517668)

#in entire rcp8.5
autocorr_MK_org_modif_sens_slope_test(glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%'])
(0.016659625265317696,
 'positively autocorrelated',
 'increasing',
 0.0,
 0.05578367086692144,
 6.403552589696595)
#slope in entire RCP8.5> RCP6.0>RCP2.6 # his no trend 



 
#%%temperature_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index)]['5%'] - Apr_Oct_hypolimnetic_ave_ref,
                      glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index) ]['95%'] - Apr_Oct_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_Apr_Oct_hypolimnetic_ave_his[(1975 < glue_df_Apr_Oct_hypolimnetic_ave_his.index)]['50%'] - Apr_Oct_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['5%']-Apr_Oct_hypolimnetic_ave_ref, glue_df_Apr_Oct_hypolimnetic_ave_rcp26['95%']-Apr_Oct_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp26.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp26['50%']-Apr_Oct_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['5%']-Apr_Oct_hypolimnetic_ave_ref, glue_df_Apr_Oct_hypolimnetic_ave_rcp60['95%']-Apr_Oct_hypolimnetic_ave_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp60.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp60['50%']-Apr_Oct_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['5%']-Apr_Oct_hypolimnetic_ave_ref, glue_df_Apr_Oct_hypolimnetic_ave_rcp85['95%']-Apr_Oct_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_Apr_Oct_hypolimnetic_ave_rcp85.index.astype(float), glue_df_Apr_Oct_hypolimnetic_ave_rcp85['50%']-Apr_Oct_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of deep temperature in May-Sep [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_Apr_Oct_temp_hypolimnetic_ave_anomaly.png",  dpi=300, bbox_inches='tight')













#%%===========summer average of anoxic afctor 


#%%########summer temperature 

#%%ploting summer temperature 

os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['5%'], glue_df_summer_hypolimnetic_ave_his['95%'], color='grey', alpha=0.2 ,  label= 'His 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_his.index.astype(float), glue_df_summer_hypolimnetic_ave_his['50%'].astype(float), 'k', label='His median', alpha=0.9, linewidth=3  )



ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%'], glue_df_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%'], glue_df_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%'], glue_df_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('temperature in summer [d/year]' , fontsize=26)
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

#%%temperature 30 yerars from each scenarios compare 



#anomaly 
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



#%%plotting summer temperature over 80 years 





os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['5%'], glue_80years_summer_hypolimnetic_ave_rcp26['95%'], color='darkgreen', alpha=0.3 ,  label= 'RCP2.6 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp26['50%'], 'darkgreen', label='RCP2.6 median', alpha=0.9, linewidth=3  )


ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['5%'], glue_80years_summer_hypolimnetic_ave_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp60['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value ={trendline_rcp60[-3]:.3f}', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['5%'], glue_80years_summer_hypolimnetic_ave_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_80years_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_80years_summer_hypolimnetic_ave_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_80years_summer_hypolimnetic_ave_rcp85['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f},  p-value ={trendline_rcp85[-3]:.3f}', color='r', fontsize= 20 )




ax=plt.ylabel('temperature in summer [d/year]' , fontsize=26)
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



 
#%%temperature_anomaly 
os.chdir('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/')

import matplotlib.pyplot as plt

fig =plt.figure(figsize=(15, 10))
ax= plt.subplot(111)


ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_his[(1975 < glue_df_summer_hypolimnetic_ave_his.index)].index.astype(float),
                      glue_df_summer_hypolimnetic_ave_his[(1975 < glue_df_summer_hypolimnetic_ave_his.index)]['5%'] - summer_hypolimnetic_ave_ref,
                      glue_df_summer_hypolimnetic_ave_his[(1975 < glue_df_summer_hypolimnetic_ave_his.index) ]['95%'] - summer_hypolimnetic_ave_ref,
                      color='grey', alpha=0.2, label='His 90% CI')


ax=plt.plot(glue_df_summer_hypolimnetic_ave_his[(1975 < glue_df_summer_hypolimnetic_ave_his.index) ].index.astype(float),
            glue_df_summer_hypolimnetic_ave_his[(1975 < glue_df_summer_hypolimnetic_ave_his.index)]['50%'] - summer_hypolimnetic_ave_ref,
            'k', label='His median', alpha=0.9, linewidth=3   )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp26['95%']-summer_hypolimnetic_ave_ref, color='darkgreen', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp26.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp26['50%']-summer_hypolimnetic_ave_ref, 'darkgreen', label='RCP6.0 median', alpha=0.9, linewidth=3  )
                      
                     
ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp60['95%']-summer_hypolimnetic_ave_ref, color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp60.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp60['50%']-summer_hypolimnetic_ave_ref, 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )

ax=plt.fill_between(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['5%']-summer_hypolimnetic_ave_ref, glue_df_summer_hypolimnetic_ave_rcp85['95%']-summer_hypolimnetic_ave_ref, color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_summer_hypolimnetic_ave_rcp85.index.astype(float), glue_df_summer_hypolimnetic_ave_rcp85['50%']-summer_hypolimnetic_ave_ref, 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )

ax=plt.ylabel('anomaly of temperature in summer [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_summer_hypolimnetic_ave_anomaly.png",  dpi=300, bbox_inches='tight')










#%%
####################################old one
############################################
############################################

#%% Annual temperature_gfdl_his
# Specify the directory where the CSV files are located


#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/gfdl_senarios/his_calibinfixedtheta_simuvartheta'




# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_gfdl_rcp26
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_gfdl_rcp60
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_gfdl_rcp85
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_gfdl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_gfdl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_gfdl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual temperature_hadgem_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/hadgem_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_hadgem_rcp26
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_hadgem_rcp60
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_hadgem_rcp85
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_hadgem_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_hadgem_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_hadgem_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                


#%% Annual temperature_ipsl_his
# Specify the directory where the CSV files are located
#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/ipsl_senarios/his_calibinfixedtheta_simuvartheta'


# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_ipsl_rcp26
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_ipsl_rcp60
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_ipsl_rcp85
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_ipsl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_ipsl_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_ipsl_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_miroc_his
# Specify the directory where the CSV files are located

#########original test with variable theta:
#########directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his'


######## fixed theta both in calib and simulation 
#######directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_fixedtheta'




####### test with fixed theta in calibration but variable for GOTM simulation 
directory = 'C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/miroc_senarios/his_calibinfixedtheta_simuvartheta'

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_his"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_his.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                
#%% Annual temperature_miroc_rcp26
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp26"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp26.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

#%% Annual temperature_miroc_rcp60
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp60"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp60.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                



#%% Annual temperature_miroc_rcp85
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
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = annual_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'annual_hypolimnetic_temp_ave_miroc_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN', header=['annual_hypolimnetic_ave'])
        
                


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
    if filename.endswith(".csv") and filename.startswith("temp_prof_miroc_rcp85"):
        
        # Read from CSV
        
        
        
        
        
        
        read_data_df = pd.read_csv(os.path.join(directory, filename))
        # Extract relevant columns (adjust column names accordingly)
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        Vr= hypo_morpho_vriables_gotm_grid[0]  # Replace with your actual Vr values
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        # Apply the annual_hypolimnetic_ave function
        result = monthly_hypolimnetic_ave(C, Vr, time_series )

        
        
        
        
        
        
        


        
        # Save the result to a new CSV file
        result_filename = f'monthly_hypolimnetic_ave_miroc_rcp85.csv'
        
        
        
       

        result.to_csv(os.path.join(directory, result_filename) , index_label='year', na_rep='NaN')#, columns=[f'month:{i}' for i in range (1:13)])
        
                

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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_his= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.set_index(timeseries_year_his)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/glue_df_temperature_his.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_fixedtheta/glue_df_temperature_his.csv')



####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_his.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his_calibinfixedtheta_simuvartheta/glue_df_temperature_his.csv')

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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp26= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.set_index(timeseries_year_rcp26)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_temperature_rcp26.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_temperature_rcp26.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp26 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_temperature_rcp26.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp26.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_temperature_rcp26.csv')



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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp60= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.set_index(timeseries_year_rcp60)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_temperature_rcp60.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_temperature_rcp60.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp60 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_temperature_rcp60.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp60.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_temperature_rcp60.csv')



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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
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
        
        
        
        
        
         
        
        
        
        annual_hypolimnetic_ave = pd.read_csv(os.path.join(directory, filename))
        annual_hypolimnetic_ave=annual_hypolimnetic_ave.set_index(annual_hypolimnetic_ave['year'])
        
        all_annual_hypolimnetic_ave = pd.concat([all_annual_hypolimnetic_ave , annual_hypolimnetic_ave['annual_hypolimnetic_ave']], axis=1)
        
        
        
        


# annual anoxic duration  
timeseries_year_rcp85= all_annual_hypolimnetic_ave.index

quants = [0.05 ,0.5 , 0.95 ]#[0,1]#[0.025, 0.5, 0.975]    
out=[]    
for index, row in all_annual_hypolimnetic_ave.iterrows():# for each timesteps
    #values = row    
    values = pd.to_numeric(row, errors='coerce') 
    out.append(weighted_quantiles(values, quants))

# Build glue df
glue_df_annual_hypolimnetic_ave_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    
glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.set_index(timeseries_year_rcp85)    


# Use to_csv to save the DataFrame to a CSV file in the specified directory

#########original test with variable theta:
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther/glue_df_temperature_rcp85.csv')


######## fixed theta both in calib and simulation 
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta/glue_df_temperature_rcp85.csv')


###### test with fixed theta in calibration a temp ave hypo in ipcl rcp85 for years 2020 and 2021
#########glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_fixedtheta_temp_gcms_2020_2021/glue_df_temperature_rcp85.csv')


####### test with fixed theta in calibration but variable for GOTM simulation 
glue_df_annual_hypolimnetic_ave_rcp85.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/alltogther_calibinfixedtheta_simuvartheta/glue_df_temperature_rcp85.csv')


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



ax=plt.ylabel('Difference of fixed and variable Ktemp assumption in simulating annual temperature [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(np.arange(-4, 3, 1) , fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.15), fontsize=22)


####### test with fixed theta in calibration but variable for GOTM simulation 
fig.savefig("GLUE_Timeseries_hypolimnetic_temp_6combinationJaJv_ave_obs_4models_diff_fixed_var_theta.png", dpi=300, bbox_inches='tight')




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
#%%Annual temperature 

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
ax=plt.text(2020, 10, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value < 0.0001', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60_vartheta['50%'])
ax=plt.text(2020, 11, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.0001', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85_vartheta['50%'])
ax=plt.text(2020, 12, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize= 20 )



ax=plt.ylabel('temperature per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_temperature_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


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
ax=plt.text(2020, 15, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value < 0.0001', color='green', fontsize= 20 )


ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['95%'], color='yellow', alpha=0.3 ,  label= 'RCP6.0 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['50%'], 'yellow', label='RCP6.0 median', alpha=0.9, linewidth=3  )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp60['50%'])
ax=plt.text(2020, 14, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.0001', color='gold', fontsize= 20 )



ax=plt.fill_between(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['5%'], glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['95%'], color='r', alpha=0.2 ,  label= 'RCP8.5 90% CI')
ax=plt.plot(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85.index.astype(float), glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3  )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_annual_hypolimnetic_ave_4models_100years_rcp85['50%'])
ax=plt.text(2020, 13, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize= 20 )



ax=plt.ylabel('temperature per each deoxygenation period [d/year]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(fontsize=22)#rotation=45 , 
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)#)   
fig.savefig("GLUE_100years_Timeseries_temperature_7combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')




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



#%%temperature 30 yerars from each scenarios compare 


#Sorting the glue dataframe according to the index (year)

glue_df_annual_hypolimnetic_ave_his=glue_df_annual_hypolimnetic_ave_his.sort_index()

glue_df_annual_hypolimnetic_ave_rcp26=glue_df_annual_hypolimnetic_ave_rcp26.sort_index()

glue_df_annual_hypolimnetic_ave_rcp60=glue_df_annual_hypolimnetic_ave_rcp60.sort_index()

glue_df_annual_hypolimnetic_ave_rcp85=glue_df_annual_hypolimnetic_ave_rcp85.sort_index()





#anomaly 

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



#%%temperature_anomaly 
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

ax=plt.ylabel('anomaly of temperature [d year$^{-1}$]' , fontsize=26)
ax=plt.xlabel('Year' , fontsize=26)
ax=plt.yticks(fontsize= 22)
ax=plt.xticks(rotation=45 , fontsize=22)
ax=plt.legend(bbox_to_anchor=(0.7, -0.2), fontsize=22)  
fig.savefig("GLUE_Timeseries_temperature_anomaly_16combinationJaJv_ave_obs_4models_4scenarios.png",  dpi=300, bbox_inches='tight')


