# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:34:42 2023

@author: mahta
"""

#%%startistical analysing for finding trendline 
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

#%%some inital disription 

#https://pypi.org/project/pymannkendall/

import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm

#1.his 
# seasonality correlation were ignore because it is annual average 

#1.a autocorrelation test (with acf plot)
fig, ax = plt.subplots(figsize=(12, 8))
sm.graphics.tsa.plot_acf(deox_dur_mean4models_his[deox_dur_mean4models_his.index>1911], lags=20, ax=ax)
plt.show()

#1.b autocorrelation test (with durbin_watson test)
from statsmodels.stats.stattools import durbin_watson
durbin_watson(deox_dur_mean4models_his[deox_dur_mean4models_his.index>1911])
# 0.008834675509237328 # Keep in you mind
# Close to 2: Little to no autocorrelation.
# smaller than 2 (0-2): positively correlated 
# garater tahn 2 (2-4): negetively correlated


#2.a original mk test if it is not autocorrelated 
print(mk.original_test(deox_dur_mean4models_his[deox_dur_mean4models_his.index>1911], alpha=0.05))


#2.b modified mk test if it is autocorrelated 
print (mk.hamed_rao_modification_test(deox_dur_mean4models_his[deox_dur_mean4models_his.index>1975]))
#print(mk.yue_wang_modification_test(onset_jday_4models_rcp85))
#print(mk.trend_free_pre_whitening_modification_test(onset_jday_4models_rcp85))
#print(mk.pre_whitening_modification_test(onset_jday_4models_rcp85))































