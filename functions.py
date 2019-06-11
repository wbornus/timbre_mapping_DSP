#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from scipy import fft


# In[4]:


def sample_fft(sample, fs):
    '''returns amplitude and phase - Fast Fourier Transform algorithm'''
    transform = fft(sample)
    transform_half = np.array([])
    transform_half = transform[0:int(len(transform)/2)]
    amp = np.abs(transform_half)
    phase = np.angle(transform_half)
    
    size = int(len(transform_half))
    freq_ratio = fs/(2*size)
    freq_base = np.array([])
    for i in range(size):
        freq_base = np.append(freq_base, i*freq_ratio)
    
    return amp_vector, phase_freq_vector, freq_ratio


# In[5]:


def normalize(data):
    abs_data = map(abs,data)
    max_value = max(abs_data)
    data = data/max_value
    return data


# In[6]:


def spectrum_arrays(amp_vector, phase_vector, freq_ratio, fundamental_freq):
    simplified_amplitude_spectrum = np.array([])
    for i in range(len(data)):
        if data[i] > data[i - 1] and data[i] > data[i + 1]:
            simplified_amplitude_spectrum = np.append(simplified_amplitude_spectrum, data[i])
        else:
            simplified_amplitude_spectrum = np.append(simplified_amplitude_spectrum, 0.0)
            
    amp_array()
            
    return 


# In[ ]:





# In[ ]:


def generate_piano(input_freq, amp_vector, phase_vector):
    freq_array = np.array([])
    amp_array = np.array([])
    phase_array = np.array([])
    
    for i in range(len(fft_vector)):
        if fft_vector[i] > 0:
            
                
    

