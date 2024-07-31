# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:49:42 2024

@author: mahta
"""

all_anaerobic_dur_his=pd.DataFrame([])
all_weights= np.array([])

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_his = pd.concat([all_anaerobic_dur_his , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_gfdl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_his = pd.concat([all_anaerobic_dur_his , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_hadgem_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_his = pd.concat([all_anaerobic_dur_his , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_ipsl_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_his = pd.concat([all_anaerobic_dur_his , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_miroc_his_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
#%%Uncertainity partitioning on:
    
all_anaerobic_dur_his= all_anaerobic_dur_his.reset_index()   
# Exclude the 'Datetime' column
df_data = all_anaerobic_dur_his.drop('Datetime', axis=1)    
    
# Calculate the sum of every 14 columns for each row
sums = []
for index, row in df_data.iterrows():
    row_sums = [sum(row[i:i+14]) for i in range(0, len(row), 14)]
    sums.append(row_sums)

# Convert the list of sums to a DataFrame
sums_anaerobic_dur_his = pd.DataFrame(sums)

# Insert the 'Datetime' column back
sums_anaerobic_dur_his.insert(0, 'Datetime', all_anaerobic_dur_his['Datetime'])    
    
sums_anaerobic_dur_his=sums_anaerobic_dur_his.set_index('Datetime')    

#
all_anaerobic_dur_his= all_anaerobic_dur_his.set_index('Datetime')

anova_sum_anaerobic_dur_his=annova_uncertainity(sums_anaerobic_dur_his)

anova_sum_anaerobic_dur_his.describe().loc['mean', :]

"""

GCMs             70.017204
param            29.053574
interaction       0.929221
GCMs/param        4.995717
year           1933.000000
Name: mean, dtype: float64
"""
anova_sum_anaerobic_dur_his.describe().loc['std', :]
"""
GCMs           18.780377
param          18.537385
interaction     0.827264
GCMs/param      6.036257
year           42.001984
Name: std, dtype: float64
"""

#%%GLUE
#%%GLUE of each depth gathered in a dictionary 


import pandas as pd

# Create an empty dictionary to store the DataFrames
glue_subset_dataframes_his = {}

# Iterate over unique column names
for column_name in all_anaerobic_dur_his.columns:

    # Subset the DataFrame for the current column name
    subset_anaerobic_dur_his = all_anaerobic_dur_his[column_name]
    
    # Extract the index
    timeseries_year_his = subset_anaerobic_dur_his.index

    # Define quantiles
    quants = [0.05, 0.5, 0.95]

    # Initialize an empty list to store the quantile results
    out = []

    # Iterate over rows for each timestep
    for index, row in subset_anaerobic_dur_his.iterrows():
        # Convert the row values to numeric
        values = pd.to_numeric(row, errors='coerce') 
        # Calculate quantiles and append to the list
        out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

    # Create a DataFrame with quantiles
    glue_subset_df_his = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    # Set index to timeseries
    glue_subset_df_his = glue_subset_df_his.set_index(timeseries_year_his)
    
    # Assign the DataFrame to the dictionary with the column name as key
    glue_subset_dataframes_his[column_name] = glue_subset_df_his

# Now we have a dictionary containing DataFrames for each column name

#%% GLUE three different dataset of 5, 50, 95% for each depth 

import pandas as pd

# Initialize empty DataFrames for 5%, 50%, and 95% values
df_anaerobic_dur_his_5_percent = pd.DataFrame()
df_anaerobic_dur_his_50_percent = pd.DataFrame()
df_anaerobic_dur_his_95_percent = pd.DataFrame()

# Iterate over the dictionary containing DataFrames for each column
for column_name, df in glue_subset_dataframes_his.items():
    # Concatenate the quantile values for each column to the corresponding DataFrame
    df_anaerobic_dur_his_5_percent[column_name] = df['5%']
    df_anaerobic_dur_his_50_percent[column_name] = df['50%']
    df_anaerobic_dur_his_95_percent[column_name] = df['95%']


# Now we have three DataFrames containing the quantile values for 5%, 50%, and 95% across all columns
# df_5_percent contains the 5% quantile values for each column
# df_50_percent contains the 50% quantile values for each column
# df_95_percent contains the 95% quantile values for each column
filename = f"glue_subset_anaerobic_dur_his_5.csv"
df_anaerobic_dur_his_5_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_his_50.csv"
df_anaerobic_dur_his_50_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_his_95.csv"
df_anaerobic_dur_his_95_percent.to_csv(filename)

# saving GLUEs 

# Use to_csv to save the DataFrame to a CSV file in the specified directory
df_anaerobic_dur_his_5_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/df_anaerobic_dur_his_5_percent.csv')
df_anaerobic_dur_his_50_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/df_anaerobic_dur_his_50_percent.csv')
df_anaerobic_dur_his_95_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/his/df_anaerobic_dur_his_95_percent.csv')
                        


#%% Plotting each percentage differently:

# Define the directory path
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models'

# Change the current working directory
os.chdir(directory_path)    
    


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

depth =  (np.array([14.25, 14.75, 15.25, 15.75, 16.25, 16.75, 17.25, 17.75,
                  18.25, 18.75, 19.25, 19.75, 20.25, 20.75]))
percentages = [5,  50,  95]
dataframes = [df_anaerobic_dur_his_5_percent,  
              df_anaerobic_dur_his_50_percent,  
              df_anaerobic_dur_his_95_percent]

# Find the global min and max values
global_min = min(df.min().min() for df in dataframes)
global_max = max(df.max().max() for df in dataframes)

# Normalize the colorbar based on the global min and max
norm = colors.Normalize(vmin=global_min, vmax=global_max)

# Create the figure and subplots
fig, axs = plt.subplots(1,  3, figsize=(18,  6))

# Plot the contour plots without adding a colorbar
for i, ax in enumerate(axs):
    contour = ax.contourf(dataframes[i].index, depth, dataframes[i].values.T, cmap='rainbow', norm=norm)
    ax.set_title(f'{percentages[i]}% model bound', fontsize=16)  # Adjust title font size
    ax.set_ylim(depth.min(), depth.max())
    ax.tick_params(axis='both', which='major', labelsize=12)  # Adjust tick font size
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis tick labels by 45 degrees
    ax.set_ylim(depth.max(), depth.min())
    if i == 0:
        ax.set_ylabel('Depth [m]', fontsize=14)  # Set y-axis label only for the first subplot

# Add a shared colorbar to the right of the subplots
cbar_ax = fig.add_axes([0.93,  0.15,  0.02,  0.7])  # Adjust positioning as needed
cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='rainbow'), cax=cbar_ax)
cbar.set_label('Anaerobic duration [d]', fontsize=14)  # Adjust color bar label font size
#plt.invert_yaxis()



# Save the plot with dpi 300
plt.savefig('contour_plot_anearobic_dur_his.png', dpi=300, bbox_inches='tight')


#%% RCP2.6

#%%rcp26

all_anaerobic_dur_rcp26=pd.DataFrame([])
all_weights= np.array([])

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp26 = pd.concat([all_anaerobic_dur_rcp26 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_gfdl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp26 = pd.concat([all_anaerobic_dur_rcp26 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_hadgem_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp26 = pd.concat([all_anaerobic_dur_rcp26 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_ipsl_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp26 = pd.concat([all_anaerobic_dur_rcp26 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_miroc_rcp26_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
#%%Uncertainity partitioning on sum of anearobic prof:
    
all_anaerobic_dur_rcp26= all_anaerobic_dur_rcp26.reset_index()   
# Exclude the 'Datetime' column
df_data = all_anaerobic_dur_rcp26.drop('Datetime', axis=1)    
    
# Calculate the sum of every 14 columns for each row
sums = []
for index, row in df_data.iterrows():
    row_sums = [sum(row[i:i+14]) for i in range(0, len(row), 14)]
    sums.append(row_sums)

# Convert the list of sums to a DataFrame
sums_anaerobic_dur_rcp26 = pd.DataFrame(sums)

# Insert the 'Datetime' column back
sums_anaerobic_dur_rcp26.insert(0, 'Datetime', all_anaerobic_dur_rcp26['Datetime'])    
    
sums_anaerobic_dur_rcp26=sums_anaerobic_dur_rcp26.set_index('Datetime')    


all_anaerobic_dur_rcp26= all_anaerobic_dur_rcp26.set_index('Datetime')

anova_sum_anaerobic_dur_rcp26=annova_uncertainity(sums_anaerobic_dur_rcp26)

anova_sum_anaerobic_dur_rcp26.describe().loc['mean', :]

"""
GCMs             67.106389
param            32.165351
interaction       0.728260
GCMs/param        3.423447
year           2052.500000
Name: mean, dtype: float64
"""
anova_sum_anaerobic_dur_rcp26.describe().loc['std', :]
"""
GCMs           19.581439
param          19.244969
interaction     0.672351
GCMs/param      3.351635
year           27.279418
Name: std, dtype: float64
"""


anova_sum_anaerobic_dur_rcp26_80years=annova_uncertainity(sums_anaerobic_dur_rcp26[sums_anaerobic_dur_rcp26.index>2019])

anova_sum_anaerobic_dur_rcp26_80years.describe().loc['mean', :]
"""
GCMs             68.703660
param            30.596946
interaction       0.699395
GCMs/param        3.638525
year           2059.500000
Name: mean, dtype: float64
"""

anova_sum_anaerobic_dur_rcp26_80years.describe().loc['std', :]
"""
GCMs           18.579312
param          18.327543
interaction     0.605877
GCMs/param      3.519522
year           23.237900
Name: std, dtype: float64
"""

#%%GLUE
#%%GLUE of each depth gathered in a dictionary 


import pandas as pd

# Create an empty dictionary to store the DataFrames
glue_subset_dataframes_rcp26 = {}

# Iterate over unique column names
for column_name in all_anaerobic_dur_rcp26.columns:

    # Subset the DataFrame for the current column name
    subset_anaerobic_dur_rcp26 = all_anaerobic_dur_rcp26[column_name]
    
    # Extract the index
    timeseries_year_rcp26 = subset_anaerobic_dur_rcp26.index

    # Define quantiles
    quants = [0.05, 0.5, 0.95]

    # Initialize an empty list to store the quantile results
    out = []

    # Iterate over rows for each timestep
    for index, row in subset_anaerobic_dur_rcp26.iterrows():
        # Convert the row values to numeric
        values = pd.to_numeric(row, errors='coerce') 
        # Calculate quantiles and append to the list
        out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

    # Create a DataFrame with quantiles
    glue_subset_df_rcp26 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    # Set index to timeseries
    glue_subset_df_rcp26 = glue_subset_df_rcp26.set_index(timeseries_year_rcp26)
    
    # Assign the DataFrame to the dictionary with the column name as key
    glue_subset_dataframes_rcp26[column_name] = glue_subset_df_rcp26

# Now we have a dictionary containing DataFrames for each column name

#%% GLUE three different dataset of 5, 50, 95% for each depth 

import pandas as pd

# Initialize empty DataFrames for 5%, 50%, and 95% values
df_anaerobic_dur_rcp26_5_percent = pd.DataFrame()
df_anaerobic_dur_rcp26_50_percent = pd.DataFrame()
df_anaerobic_dur_rcp26_95_percent = pd.DataFrame()

# Iterate over the dictionary containing DataFrames for each column
for column_name, df in glue_subset_dataframes_rcp26.items():
    # Concatenate the quantile values for each column to the corresponding DataFrame
    df_anaerobic_dur_rcp26_5_percent[column_name] = df['5%']
    df_anaerobic_dur_rcp26_50_percent[column_name] = df['50%']
    df_anaerobic_dur_rcp26_95_percent[column_name] = df['95%']


# Now we have three DataFrames containing the quantile values for 5%, 50%, and 95% across all columns
# df_5_percent contains the 5% quantile values for each column
# df_50_percent contains the 50% quantile values for each column
# df_95_percent contains the 95% quantile values for each column
filename = f"glue_subset_anaerobic_dur_rcp26_5.csv"
df_anaerobic_dur_rcp26_5_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_rcp26_50.csv"
df_anaerobic_dur_rcp26_50_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_rcp26_95.csv"
df_anaerobic_dur_rcp26_95_percent.to_csv(filename)

# saving GLUEs 

# Use to_csv to save the DataFrame to a CSV file in the specified directory
df_anaerobic_dur_rcp26_5_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/df_anaerobic_dur_rcp26_5_percent.csv')
df_anaerobic_dur_rcp26_50_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/df_anaerobic_dur_rcp26_50_percent.csv')
df_anaerobic_dur_rcp26_95_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp26/df_anaerobic_dur_rcp26_95_percent.csv')
                        
#%%RCP6.0

#%%rcp60

all_anaerobic_dur_rcp60=pd.DataFrame([])
all_weights= np.array([])

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp60 = pd.concat([all_anaerobic_dur_rcp60 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_gfdl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp60 = pd.concat([all_anaerobic_dur_rcp60 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_hadgem_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp60 = pd.concat([all_anaerobic_dur_rcp60 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_ipsl_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp60 = pd.concat([all_anaerobic_dur_rcp60 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_miroc_rcp60_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
#%%Uncertainity partitioning on sum of anearobic prof:
    
all_anaerobic_dur_rcp60= all_anaerobic_dur_rcp60.reset_index()   
# Exclude the 'Datetime' column
df_data = all_anaerobic_dur_rcp60.drop('Datetime', axis=1)    
    
# Calculate the sum of every 14 columns for each row
sums = []
for index, row in df_data.iterrows():
    row_sums = [sum(row[i:i+14]) for i in range(0, len(row), 14)]
    sums.append(row_sums)

# Convert the list of sums to a DataFrame
sums_anaerobic_dur_rcp60 = pd.DataFrame(sums)

# Insert the 'Datetime' column back
sums_anaerobic_dur_rcp60.insert(0, 'Datetime', all_anaerobic_dur_rcp60['Datetime'])    
    
sums_anaerobic_dur_rcp60=sums_anaerobic_dur_rcp60.set_index('Datetime')    


all_anaerobic_dur_rcp60= all_anaerobic_dur_rcp60.set_index('Datetime')

anova_sum_anaerobic_dur_rcp60=annova_uncertainity(sums_anaerobic_dur_rcp60)

anova_sum_anaerobic_dur_rcp60.describe().loc['mean', :]

"""
GCMs             71.586553
param            27.620606
interaction       0.792841
GCMs/param        4.796543
year           2052.500000
Name: mean, dtype: float64
"""
anova_sum_anaerobic_dur_rcp60.describe().loc['std', :]
"""
GCMs           19.057704
param          18.528456
interaction     0.823420
GCMs/param      4.895604
year           27.279418
Name: std, dtype: float64
"""

anova_sum_anaerobic_dur_rcp60_80years=annova_uncertainity(sums_anaerobic_dur_rcp60[sums_anaerobic_dur_rcp60.index>2019])

anova_sum_anaerobic_dur_rcp60_80years.describe().loc['mean', :]
"""
GCMs             71.590829
param            27.606880
interaction       0.802291
GCMs/param        4.587013
year           2059.500000
Name: mean, dtype: float64
"""

anova_sum_anaerobic_dur_rcp60_80years.describe().loc['std', :]
"""
GCMs           19.361256
param          18.804588
interaction     0.848581
GCMs/param      4.296137
year           23.237900
Name: std, dtype: float64
"""

#%%GLUE
#%%GLUE of each depth gathered in a dictionary 


import pandas as pd

# Create an empty dictionary to store the DataFrames
glue_subset_dataframes_rcp60 = {}

# Iterate over unique column names
for column_name in all_anaerobic_dur_rcp60.columns:

    # Subset the DataFrame for the current column name
    subset_anaerobic_dur_rcp60 = all_anaerobic_dur_rcp60[column_name]
    
    # Extract the index
    timeseries_year_rcp60 = subset_anaerobic_dur_rcp60.index

    # Define quantiles
    quants = [0.05, 0.5, 0.95]

    # Initialize an empty list to store the quantile results
    out = []

    # Iterate over rows for each timestep
    for index, row in subset_anaerobic_dur_rcp60.iterrows():
        # Convert the row values to numeric
        values = pd.to_numeric(row, errors='coerce') 
        # Calculate quantiles and append to the list
        out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

    # Create a DataFrame with quantiles
    glue_subset_df_rcp60 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    # Set index to timeseries
    glue_subset_df_rcp60 = glue_subset_df_rcp60.set_index(timeseries_year_rcp60)
    
    # Assign the DataFrame to the dictionary with the column name as key
    glue_subset_dataframes_rcp60[column_name] = glue_subset_df_rcp60

# Now we have a dictionary containing DataFrames for each column name

#%% GLUE three different dataset of 5, 50, 95% for each depth 

import pandas as pd

# Initialize empty DataFrames for 5%, 50%, and 95% values
df_anaerobic_dur_rcp60_5_percent = pd.DataFrame()
df_anaerobic_dur_rcp60_50_percent = pd.DataFrame()
df_anaerobic_dur_rcp60_95_percent = pd.DataFrame()

# Iterate over the dictionary containing DataFrames for each column
for column_name, df in glue_subset_dataframes_rcp60.items():
    # Concatenate the quantile values for each column to the corresponding DataFrame
    df_anaerobic_dur_rcp60_5_percent[column_name] = df['5%']
    df_anaerobic_dur_rcp60_50_percent[column_name] = df['50%']
    df_anaerobic_dur_rcp60_95_percent[column_name] = df['95%']


# Now we have three DataFrames containing the quantile values for 5%, 50%, and 95% across all columns
# df_5_percent contains the 5% quantile values for each column
# df_50_percent contains the 50% quantile values for each column
# df_95_percent contains the 95% quantile values for each column
filename = f"glue_subset_anaerobic_dur_rcp60_5.csv"
df_anaerobic_dur_rcp60_5_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_rcp60_50.csv"
df_anaerobic_dur_rcp60_50_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_rcp60_95.csv"
df_anaerobic_dur_rcp60_95_percent.to_csv(filename)

# saving GLUEs 

# Use to_csv to save the DataFrame to a CSV file in the specified directory
df_anaerobic_dur_rcp60_5_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/df_anaerobic_dur_rcp60_5_percent.csv')
df_anaerobic_dur_rcp60_50_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/df_anaerobic_dur_rcp60_50_percent.csv')
df_anaerobic_dur_rcp60_95_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp60/df_anaerobic_dur_rcp60_95_percent.csv')
                        
#%%RCP8.5

#%%rcp85

all_anaerobic_dur_rcp85=pd.DataFrame([])
all_weights= np.array([])

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp85 = pd.concat([all_anaerobic_dur_rcp85 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_gfdl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp85 = pd.concat([all_anaerobic_dur_rcp85 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_hadgem_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
        
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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp85 = pd.concat([all_anaerobic_dur_rcp85 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_ipsl_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')

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
        C = read_data_df.iloc[:, 1:].values  # Assuming your concentrations are in columns 1 and onwards
        time_series = pd.to_datetime(read_data_df['Datetime'])
        
        result = anearobic_duration_annually(C , time_series, threshold= 0.5)
        
        all_anaerobic_dur_rcp85 = pd.concat([all_anaerobic_dur_rcp85 , result], axis=1)
        
        # Round Ja and Jv to 3 decimal places
        Jv_name = round(jv_value, 3)
        Ja_name = round(ja_value, 3)
        
        header_values = {'Jv': jv_value, 'Ja': ja_value , 'weights': weights }


        
        # Save the result to a new CSV file
        result_filename = f'anaerobic_duration_miroc_rcp85_Jv_{Jv_name}_Ja_{Ja_name}.csv'
        
        header_df = pd.DataFrame([header_values])
        header_df.to_csv(os.path.join(directory, result_filename))#, index=False)
       

        result.to_csv(os.path.join(directory, result_filename) , mode='a' , index_label='year', na_rep='NaN')
        
#%%Uncertainity partitioning on sum of anearobic prof:
    
all_anaerobic_dur_rcp85= all_anaerobic_dur_rcp85.reset_index()   
# Exclude the 'Datetime' column
df_data = all_anaerobic_dur_rcp85.drop('Datetime', axis=1)    
    
# Calculate the sum of every 14 columns for each row
sums = []
for index, row in df_data.iterrows():
    row_sums = [sum(row[i:i+14]) for i in range(0, len(row), 14)]
    sums.append(row_sums)

# Convert the list of sums to a DataFrame
sums_anaerobic_dur_rcp85 = pd.DataFrame(sums)

# Insert the 'Datetime' column back
sums_anaerobic_dur_rcp85.insert(0, 'Datetime', all_anaerobic_dur_rcp85['Datetime'])    
    
sums_anaerobic_dur_rcp85=sums_anaerobic_dur_rcp85.set_index('Datetime')    


all_anaerobic_dur_rcp85= all_anaerobic_dur_rcp85.set_index('Datetime')

anova_sum_anaerobic_dur_rcp85=annova_uncertainity(sums_anaerobic_dur_rcp85)

anova_sum_anaerobic_dur_rcp85.describe().loc['mean', :]

"""
GCMs             80.540186
param            18.797799
interaction       0.662015
GCMs/param        7.420500
year           2052.500000
Name: mean, dtype: float64
"""
anova_sum_anaerobic_dur_rcp85.describe().loc['std', :]
"""
GCMs           14.717990
param          14.191526
interaction     0.719976
GCMs/param      6.149882
year           27.279418
Name: std, dtype: float64

"""


anova_sum_anaerobic_dur_rcp85_80years=annova_uncertainity(sums_anaerobic_dur_rcp85[sums_anaerobic_dur_rcp85.index>2019])

anova_sum_anaerobic_dur_rcp85_80years.describe().loc['mean', :]
"""
GCMs             81.086157
param            18.239157
interaction       0.674686
GCMs/param        7.878737
year           2059.500000
Name: mean, dtype: float64
"""

anova_sum_anaerobic_dur_rcp85_80years.describe().loc['std', :]
"""
GCMs           14.818781
param          14.213918
interaction     0.749806
GCMs/param      6.472886
year           23.237900
Name: std, dtype: float64
"""
#%%GLUE
#%%GLUE of each depth gathered in a dictionary 


import pandas as pd

# Create an empty dictionary to store the DataFrames
glue_subset_dataframes_rcp85 = {}

# Iterate over unique column names
for column_name in all_anaerobic_dur_rcp85.columns:

    # Subset the DataFrame for the current column name
    subset_anaerobic_dur_rcp85 = all_anaerobic_dur_rcp85[column_name]
    
    # Extract the index
    timeseries_year_rcp85 = subset_anaerobic_dur_rcp85.index

    # Define quantiles
    quants = [0.05, 0.5, 0.95]

    # Initialize an empty list to store the quantile results
    out = []

    # Iterate over rows for each timestep
    for index, row in subset_anaerobic_dur_rcp85.iterrows():
        # Convert the row values to numeric
        values = pd.to_numeric(row, errors='coerce') 
        # Calculate quantiles and append to the list
        out.append(weighted_quantiles(values, quants, sample_weight=all_weights))

    # Create a DataFrame with quantiles
    glue_subset_df_rcp85 = pd.DataFrame(data=out, columns=['5%', '50%', '95%'])
    # Set index to timeseries
    glue_subset_df_rcp85 = glue_subset_df_rcp85.set_index(timeseries_year_rcp85)
    
    # Assign the DataFrame to the dictionary with the column name as key
    glue_subset_dataframes_rcp85[column_name] = glue_subset_df_rcp85

# Now we have a dictionary containing DataFrames for each column name

#%% GLUE three different dataset of 5, 50, 95% for each depth 

import pandas as pd

# Initialize empty DataFrames for 5%, 50%, and 95% values
df_anaerobic_dur_rcp85_5_percent = pd.DataFrame()
df_anaerobic_dur_rcp85_50_percent = pd.DataFrame()
df_anaerobic_dur_rcp85_95_percent = pd.DataFrame()

# Iterate over the dictionary containing DataFrames for each column
for column_name, df in glue_subset_dataframes_rcp85.items():
    # Concatenate the quantile values for each column to the corresponding DataFrame
    df_anaerobic_dur_rcp85_5_percent[column_name] = df['5%']
    df_anaerobic_dur_rcp85_50_percent[column_name] = df['50%']
    df_anaerobic_dur_rcp85_95_percent[column_name] = df['95%']


# Now we have three DataFrames containing the quantile values for 5%, 50%, and 95% across all columns
# df_5_percent contains the 5% quantile values for each column
# df_50_percent contains the 50% quantile values for each column
# df_95_percent contains the 95% quantile values for each column
filename = f"glue_subset_anaerobic_dur_rcp85_5.csv"
df_anaerobic_dur_rcp85_5_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_rcp85_50.csv"
df_anaerobic_dur_rcp85_50_percent.to_csv(filename)
filename = f"glue_subset_anaerobic_dur_rcp85_95.csv"
df_anaerobic_dur_rcp85_95_percent.to_csv(filename)

# saving GLUEs 

# Use to_csv to save the DataFrame to a CSV file in the specified directory
df_anaerobic_dur_rcp85_5_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/df_anaerobic_dur_rcp85_5_percent.csv')
df_anaerobic_dur_rcp85_50_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/df_anaerobic_dur_rcp85_50_percent.csv')
df_anaerobic_dur_rcp85_95_percent.to_csv('C:/Users/mahta/OneDrive/Documents/PhD_py_code/Future_simulation_results/all_4_models/rcp85/df_anaerobic_dur_rcp85_95_percent.csv')
                        
#%%Full yeras plot for all rcps so subplots of 3*3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os

# Define the directory path and change the current working directory
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models'
os.chdir(directory_path)

# Assuming depth is defined as in your example
depth = -1 * (np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75,
                         -18.25, -18.75, -19.25, -19.75, -20.25, -20.75]))

# Define RCP scenarios and percentages
rcp_scenarios = ['rcp26', 'rcp60', 'rcp85']
percentages = [5,  50,  95]

# Create a list of dataframe names and load them
dataframe_names = [f"df_anaerobic_dur_{rcp}_{perc}_percent" for rcp in rcp_scenarios for perc in percentages]
dataframes = [eval(name) for name in dataframe_names]  # Load the dataframes using eval (ensure they exist in the scope)

# Find the global min and max values
global_min = min(df.min().min() for df in dataframes)
global_max = max(df.max().max() for df in dataframes)

# Normalize the colorbar based on the global min and max
norm = colors.Normalize(vmin=global_min, vmax=global_max)

# Create the figure and a  3x3 grid of subplots
fig, axs = plt.subplots(3,  3, figsize=(18,  18))  # Adjust the figsize as needed

# Plot the contour plots without adding a colorbar
for i, (ax_row, rcp) in enumerate(zip(axs, rcp_scenarios)):
    for j, ax in enumerate(ax_row):
        ax.contourf(dataframes[(i * len(percentages)) + j].index, depth, dataframes[(i * len(percentages)) + j].values.T, cmap='rainbow', norm=norm)
        #ax.set_title(f'{percentages[j]}% model bound ({rcp})', fontsize=16)
        # Format the RCP scenario title to have a decimal point
        formatted_rcp = f"RCP{float(rcp[3:]):.1f}"
        ax.set_title(f'{percentages[j]}% model bound ({formatted_rcp})', fontsize=16)        
        ax.set_ylim(depth.min(), depth.max())
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.tick_params(axis='x', rotation=45)
        ax.set_ylim(depth.max(), depth.min())
        if i ==  0 or 3 or 6:
            ax.set_ylabel('Depth [m]', fontsize=14)

# Add a shared colorbar to the right of the subplots
cbar_ax = fig.add_axes([0.93,  0.15,  0.02,  0.7])  # Adjust positioning as needed
cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='rainbow'), cax=cbar_ax)
cbar.set_label('Anaerobic duration [d]', fontsize=20)

# Save the plot with dpi  300
plt.savefig('contour_plot_anearobic_dur_all_rcp_scenarios.png', dpi=300)


        

#%% 80 years plot for all rcps so subplots of 3*3


df_anaerobic_80years_dur_rcp26_5_percent= df_anaerobic_dur_rcp26_5_percent[df_anaerobic_dur_rcp26_5_percent.index>2019]
df_anaerobic_80years_dur_rcp26_50_percent= df_anaerobic_dur_rcp26_50_percent[df_anaerobic_dur_rcp26_50_percent.index>2019]
df_anaerobic_80years_dur_rcp26_95_percent= df_anaerobic_dur_rcp26_95_percent[df_anaerobic_dur_rcp26_95_percent.index>2019]


df_anaerobic_80years_dur_rcp60_5_percent= df_anaerobic_dur_rcp60_5_percent[df_anaerobic_dur_rcp60_5_percent.index>2019]
df_anaerobic_80years_dur_rcp60_50_percent= df_anaerobic_dur_rcp60_50_percent[df_anaerobic_dur_rcp60_50_percent.index>2019]
df_anaerobic_80years_dur_rcp60_95_percent= df_anaerobic_dur_rcp60_95_percent[df_anaerobic_dur_rcp60_95_percent.index>2019]


df_anaerobic_80years_dur_rcp85_5_percent= df_anaerobic_dur_rcp85_5_percent[df_anaerobic_dur_rcp85_5_percent.index>2019]
df_anaerobic_80years_dur_rcp85_50_percent= df_anaerobic_dur_rcp85_50_percent[df_anaerobic_dur_rcp85_50_percent.index>2019]
df_anaerobic_80years_dur_rcp85_95_percent= df_anaerobic_dur_rcp85_95_percent[df_anaerobic_dur_rcp85_95_percent.index>2019]



# Define the directory path and change the current working directory
directory_path = r'C:\Users\mahta\OneDrive\Documents\PhD_py_code\Future_simulation_results\all_4_models'
os.chdir(directory_path)

# Assuming depth is defined as in your example
depth = -1 * (np.array([-14.25, -14.75, -15.25, -15.75, -16.25, -16.75, -17.25, -17.75,
                         -18.25, -18.75, -19.25, -19.75, -20.25, -20.75]))

# Define RCP scenarios and percentages
rcp_scenarios = ['rcp26', 'rcp60', 'rcp85']
percentages = [5,  50,  95]

# Create a list of dataframe names and load them
dataframe_names = [f"df_anaerobic_80years_dur_{rcp}_{perc}_percent" for rcp in rcp_scenarios for perc in percentages]
dataframes = [eval(name) for name in dataframe_names]  # Load the dataframes using eval (ensure they exist in the scope)

# Find the global min and max values
global_min = min(df.min().min() for df in dataframes)
global_max = max(df.max().max() for df in dataframes)

# Normalize the colorbar based on the global min and max
norm = colors.Normalize(vmin=global_min, vmax=global_max)

# Create the figure and a  3x3 grid of subplots
fig, axs = plt.subplots(3,  3, figsize=(18,  18))  # Adjust the figsize as needed

# Plot the contour plots without adding a colorbar
for i, (ax_row, rcp) in enumerate(zip(axs, rcp_scenarios)):
    for j, ax in enumerate(ax_row):
        ax.contourf(dataframes[(i * len(percentages)) + j].index, depth, dataframes[(i * len(percentages)) + j].values.T, cmap='rainbow', norm=norm)
        #ax.set_title(f'{percentages[j]}% model bound ({rcp})', fontsize=16)
        # Format the RCP scenario title to have a decimal point
        formatted_rcp = f"RCP{float(rcp[3:])/10:.1f}"
        ax.set_title(f'{percentages[j]}% model bound ({formatted_rcp})', fontsize=16)        
        ax.set_ylim(depth.min(), depth.max())
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.tick_params(axis='x', rotation=45)
        ax.set_ylim(depth.max(), depth.min())
        if i ==  0 or 3 or 6:
            ax.set_ylabel('Depth [m]', fontsize=14)

# Add a shared colorbar to the right of the subplots
cbar_ax = fig.add_axes([0.93,  0.15,  0.02,  0.7])  # Adjust positioning as needed
cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap='rainbow'), cax=cbar_ax)
cbar.set_label('Anaerobic duration [d]', fontsize=20)

# Save the plot with dpi  300
plt.savefig('contour_plot_anearobic_80years_dur_all_rcp_scenarios.png', dpi=300)




