# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 13:04:41 2025

@author: P.Hristov
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, pacf

#%% Load data
all_data = pd.read_csv('Y_out_example.csv')

#%% Split into DFs for each time series
sample_data = {}
for col in all_data.columns:
    sample_data[col] = np.array(all_data[col][1:]).T.reshape((100,60))
    
#%% Visualise a couple
#%%
plt.plot(sample_data['y1'].T, color='r', lw=0.5)
plt.xlabel('Time', fontsize=16)
plt.ylabel('QoI', fontsize=16)
plt.title('$y_1$', fontsize=20)

#%%
plt.plot(sample_data['y2'].T, color='r', lw=0.5)
plt.xlabel('Time', fontsize=16)
plt.ylabel('QoI', fontsize=16)
plt.title('$y_2$', fontsize=20)

#%%
plt.plot(sample_data['y4'].T, color='r', lw=0.5)
plt.xlabel('Time', fontsize=16)
plt.ylabel('QoI', fontsize=16)
plt.title('$y_4$', fontsize=20)

#%%
plt.plot(sample_data['y6'].T, color='r', lw=0.5)
plt.xlabel('Time', fontsize=16)
plt.ylabel('QoI', fontsize=16)
plt.title('$y_6$', fontsize=20)

#%% Look at ACF and PACF
lag = 20
f, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 6))
plot_acf(sample_data['y1'][0], lags=lag, ax=ax[0])
plot_pacf(sample_data['y1'][0], lags=lag, ax=ax[1], method='ols')
plt.tight_layout()

#%% Compute ACF and PACF for all samples
out = 'y1'
lag = 20

afval = []
afci = []
pafval = []
pafci = []

for i, rep in enumerate(sample_data['y1']):
    af = acf(rep, nlags=lag, alpha=0.05)
    paf = pacf(rep, nlags=lag, method='ols', alpha=0.05)
    if np.all(~np.isnan(af[0])):
        afval.append(af[0])
        afci.append(af[1])
        pafval.append(paf[0])
        pafci.append(paf[1])
        

afval = np.array(afval)
afci = np.array(afci)
pafval = np.array(pafval)
pafci = np.array(pafci)

dec_thresh_af = np.abs(afci[:,:,0] - afval)
active_lags_af = np.mean(afval > dec_thresh_af, axis=0)

dec_thresh_paf = np.abs(pafci[:,:,0] - pafval)
active_lags_paf = np.mean(pafval > dec_thresh_paf, axis=0)

#%% Plot boxes of correlation
plt.boxplot(afval)
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Correlation', fontsize=12)
plt.title(f'$y_{out[1]}$ autocorrelation', fontsize=14)

#%%
plt.boxplot(pafval)
plt.xlabel('Lag', fontsize=12)
plt.ylabel('Correlation', fontsize=12)
plt.title(f'$y_{out[1]}$ partial autocorrelation', fontsize=14)
plt.ylim([-1,1])