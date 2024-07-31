# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:28:45 2024

@author: mahta
"""

import matplotlib.pyplot as plt

# Create a 2x2 subplot grid
fig, axs = plt.subplots(2, 2, figsize=(23, 16))

# Adjust subplot layout with padding
plt.subplots_adjust(hspace=0.2, wspace=0.32)


# Plot 1

#rcp26
axs[0, 0].fill_between(glue_df_deox_dur_80years_rcp26.index, glue_df_deox_dur_80years_rcp26['5%'], glue_df_deox_dur_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
axs[0, 0].plot(glue_df_deox_dur_80years_rcp26.index, glue_df_deox_dur_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3)  
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp26['50%'])
axs[0, 0].plot(glue_df_deox_dur_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--', label= 'RCP2.6 trendline')
axs[0, 0].text(2030, 67, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )

#rcp60
axs[0, 0].fill_between(glue_df_deox_dur_80years_rcp60.index, glue_df_deox_dur_80years_rcp60['5%'], glue_df_deox_dur_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
axs[0, 0].plot(glue_df_deox_dur_80years_rcp60.index, glue_df_deox_dur_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp60['50%'])
axs[0, 0].plot(glue_df_deox_dur_80years_rcp60.index,trendline_rcp60[-2]*(np.arange(1,81))+trendline_rcp60[-1] ,color='orange',  linestyle='--',  label= 'RCP6.0 trendline')
axs[0, 0].text(2030, 60, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.0001', color='orange', fontsize= 20 )

#rcp85
axs[0, 0].fill_between(glue_df_deox_dur_80years_rcp85.index, glue_df_deox_dur_80years_rcp85['5%'], glue_df_deox_dur_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
axs[0, 0].plot(glue_df_deox_dur_80years_rcp85.index, glue_df_deox_dur_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_df_deox_dur_80years_rcp85['50%'])
axs[0, 0].plot(glue_df_deox_dur_80years_rcp85.index,trendline_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--',  label= 'RCP8.5 trendline')
axs[0, 0].text(2030, 53, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.0001', color='r', fontsize=20)
axs[0, 0].text(0.98, 0.98, '(a)', fontsize=20, transform=axs[0, 0].transAxes, verticalalignment='top', horizontalalignment='right')
axs[0, 0].text(0.02, 0.98, 'n=4', fontsize=26, transform=axs[0, 0].transAxes, verticalalignment='top', horizontalalignment='left')

axs[0, 0].set_ylabel('Startification duration [d]', fontsize=26)
#axs[0, 0].set_xlabel('Year', fontsize=26)
axs[0, 0].tick_params(axis='both', which='major', labelsize=22)  # setting major tick parameters

# Setting specific yticks
axs[0, 0].set_yticks(np.arange(50, 180, 30))

# Setting xtick rotation
axs[0, 0].tick_params(axis='x', rotation=45)


axs[0, 0].legend(bbox_to_anchor=(1.9, -1.5), fontsize=22, ncol=3)


# Legend
#axs[0, 0].legend(loc='upper right', fontsize=22)

# Plot 2
axs[1, 1].set_yscale('log')
# Specify the y-axis tick values
#y_ticks = [0.5*10**-5, 10**-5, 2*10**-5, 3*10**-5, 4*10**-5 , 5*10**-5, 6*10**-5]  # Replace with your actual values
axs[1, 1].set_ylim([3*10**-6, 0.3*10**-4])

# Your existing plotting code remains unchanged
axs[1, 1].fill_between(glue_df_kz_mean_surf_80years_rcp26.index, glue_df_kz_mean_surf_80years_rcp26['5%'], glue_df_kz_mean_surf_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6  90% CI')
axs[1, 1].plot(glue_df_kz_mean_surf_80years_rcp26.index, glue_df_kz_mean_surf_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
axs[1, 1].fill_between(glue_df_kz_mean_surf_80years_rcp60.index, glue_df_kz_mean_surf_80years_rcp60['5%'], glue_df_kz_mean_surf_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
axs[1, 1].plot(glue_df_kz_mean_surf_80years_rcp60.index, glue_df_kz_mean_surf_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )

axs[1, 1].fill_between(glue_df_kz_mean_surf_80years_rcp85.index, glue_df_kz_mean_surf_80years_rcp85['5%'], glue_df_kz_mean_surf_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
axs[1, 1].plot(glue_df_kz_mean_surf_80years_rcp85.index, glue_df_kz_mean_surf_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )

axs[1, 1].set_ylabel('K$_z$ at top of deep-water [m$^{2}$ s$^{-1}$]' , fontsize=26)
#axs[0, 1].set_xlabel('Year', fontsize=26)
axs[1, 1].tick_params(axis='both', which='major', labelsize=22)  # setting major tick parameters
# Adding text at the right top corner (d)
axs[1, 1].text(0.98, 0.98, '(d)', fontsize=20, transform=axs[1, 1].transAxes, verticalalignment='top', horizontalalignment='right')
axs[1, 1].text(0.02, 0.98, 'n=4', fontsize=26, transform=axs[1, 1].transAxes, verticalalignment='top', horizontalalignment='left')

axs[1, 1].set_xlabel('Year', fontsize=26)
# Setting xtick rotation
axs[1, 1].tick_params(axis='x', rotation=45)

# Plot 3
##########inital condition C:

axs[0, 1].fill_between(glue_df_C_ave_inital_cond_80years_rcp26.index, glue_df_C_ave_inital_cond_80years_rcp26['5%'], glue_df_C_ave_inital_cond_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
axs[0, 1].plot(glue_df_C_ave_inital_cond_80years_rcp26.index, glue_df_C_ave_inital_cond_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26= autocorr_MK_org_modif_sens_slope_test(glue_df_C_ave_inital_cond_80years_rcp26['50%'])
axs[0, 1].plot(glue_df_C_ave_inital_cond_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--' , label= 'RCP2.6 trendline')

axs[0, 1].text(2030, 10.2, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f},  p-value = {trendline_rcp26[-3]:.3f}', color='g' , fontsize= 20 )


axs[0, 1].fill_between(glue_df_C_ave_inital_cond_80years_rcp60.index, glue_df_C_ave_inital_cond_80years_rcp60['5%'], glue_df_C_ave_inital_cond_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
axs[0, 1].plot(glue_df_C_ave_inital_cond_80years_rcp60.index, glue_df_C_ave_inital_cond_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )


axs[0, 1].fill_between(glue_df_C_ave_inital_cond_80years_rcp85.index, glue_df_C_ave_inital_cond_80years_rcp85['5%'], glue_df_C_ave_inital_cond_80years_rcp85['95%'], color='r', alpha=0.3,  label= 'RCP8.5 90% CI')
axs[0, 1].plot(glue_df_C_ave_inital_cond_80years_rcp85.index, glue_df_C_ave_inital_cond_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )


axs[0, 1].set_ylabel('Deep-water DO onset [mg L$^{-1}$]' , fontsize=26)
axs[0, 1].tick_params(axis='both', which='major', labelsize=22)  # setting major tick parameters
# Adding text at the right top corner (a)
axs[0, 1].text(0.98, 0.98, '(b)', fontsize=20, transform=axs[0, 1].transAxes, verticalalignment='top', horizontalalignment='right')
axs[0, 1].text(0.02, 0.98, 'n=4', fontsize=26, transform=axs[0, 1].transAxes, verticalalignment='top', horizontalalignment='left')

# Setting xtick rotation
axs[0, 1].tick_params(axis='x', rotation=45)

axs[0, 1].set_yticks(np.arange(10, 14, 1))
axs[0, 1].tick_params(axis='both', which='major', labelsize=22)  # setting major tick parameters



#############Ktemp
axs[1, 0].fill_between(glue_ktemp_80years_rcp26.index, glue_ktemp_80years_rcp26['5%'], glue_ktemp_80years_rcp26['95%'], color='green', alpha=0.4,  label= 'RCP2.6 90% CI')
axs[1, 0].plot(glue_ktemp_80years_rcp26.index, glue_ktemp_80years_rcp26['50%'], 'green', label='RCP2.6 median', alpha=1, linewidth=3 )
trendline_rcp26=autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp26['50%'])
#ax=plt.plot(glue_ktemp_80years_rcp26.index,trendline_rcp26[-2]*(np.arange(1,81))+trendline_rcp26[-1] ,color='green',  linestyle='--')
#ax=plt.text(2065, 9, f'y = {trendline_rcp26[-2]:.3f}x + {trendline_rcp26[-1]:.3f}, p-value < 0.05', color='green', fontsize= 20 )


axs[1, 0].fill_between(glue_ktemp_80years_rcp60.index, glue_ktemp_80years_rcp60['5%'], glue_ktemp_80years_rcp60['95%'], color='yellow', alpha=0.4 ,  label= 'RCP6.0 90% CI')
axs[1, 0].plot(glue_ktemp_80years_rcp26.index, glue_ktemp_80years_rcp60['50%'], 'yellow', label='RCP6.0 median',alpha=1, linewidth=3 )
trendline_rcp60=autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp60['50%'])
#ax=plt.plot(glue_ktemp_80years_rcp60.index,trendline_rcp60[-2]*(np.arange(1,81))+trendline_rcp60[-1] ,color='gold',  linestyle='--')
#ax=plt.text(2065, 9, f'y = {trendline_rcp60[-2]:.3f}x + {trendline_rcp60[-1]:.3f}, p-value < 0.05', color='gold', fontsize= 20 )



axs[1, 0].fill_between(glue_ktemp_80years_rcp85.index, glue_ktemp_80years_rcp85['5%'], glue_ktemp_80years_rcp85['95%'], color='r', alpha=0.3 ,  label= 'RCP8.5 90% CI')
axs[1, 0].plot(glue_ktemp_80years_rcp85.index, glue_ktemp_80years_rcp85['50%'], 'r', label='RCP8.5 median', alpha=0.9, linewidth=3 )
trendline_rcp85=autocorr_MK_org_modif_sens_slope_test(glue_ktemp_80years_rcp85['50%'])
#axs[1, 1].plot(glue_ktemp_80years_rcp85.index,glue_ktemp_80years_rcp85[-2]*(np.arange(1,81))+trendline_rcp85[-1] ,color='r',  linestyle='--')
#axs[1, 1].text(2065, 9.5, f'y = {trendline_rcp85[-2]:.3f}x + {trendline_rcp85[-1]:.3f}, p-value < 0.05', color='r', fontsize= 20 )

axs[1, 0].set_ylabel('Temperature coefficient of \n DO depletion rate[]', fontsize=26)
axs[1, 0].set_xlabel('Year', fontsize=26)
axs[1, 0].set_yticks(np.arange(0.3, 0.7, 0.1))
axs[1, 0].tick_params(axis='x', rotation=45, labelsize=22)
axs[1, 0].tick_params(axis='both', which='major', labelsize=22)  # setting major tick parameters


# Adding text at the right top corner (c)
axs[1, 0].text(0.98, 0.98, '(c)', fontsize=20, transform=axs[1, 0].transAxes, verticalalignment='top', horizontalalignment='right')


axs[1, 0].text(0.02, 0.98, 'n=64', fontsize=26, transform=axs[1, 0].transAxes, verticalalignment='top', horizontalalignment='left')



plt.savefig("combined_attribution_plots.png", dpi=300, bbox_inches='tight')
plt.show()
#%%
#2020s
glue_df_deox_dur_80years_rcp26[glue_df_deox_dur_80years_rcp26.index<2030 ]['50%'].mean()
#122.0
glue_df_deox_dur_80years_rcp60[glue_df_deox_dur_80years_rcp60.index<2030 ]['50%'].mean()
#123.25
glue_df_deox_dur_80years_rcp85[glue_df_deox_dur_80years_rcp85.index<2030 ]['50%'].mean()
#120.2

#2090s
glue_df_deox_dur_80years_rcp26[glue_df_deox_dur_80years_rcp26.index>2089 ]['50%'].mean()
#129.2
glue_df_deox_dur_80years_rcp60[glue_df_deox_dur_80years_rcp60.index>2089 ]['50%'].mean()
#137.85
glue_df_deox_dur_80years_rcp85[glue_df_deox_dur_80years_rcp85.index>2089 ]['50%'].mean()
#151.85