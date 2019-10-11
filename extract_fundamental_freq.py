import numpy as np
from fractions import Fraction
from scipy.fftpack import fft
import matplotlib.pyplot as plt

def extract_fundamental_freq(sample, fs):
    transform = fft(sample)             #fast fourier transform
    freq_len = fs / len(transform)      #how many hertz in between each index
    spectrum_halved = transform[:len(sample)//2]
    amplitude = np.array(abs(spectrum_halved))
    peak_vec = np.array([])
    print(amplitude[0])
    for i in range(1, len(amplitude) - 1, 1):     #leaving only highest peaks of spectrum
        if amplitude[i - 1] < amplitude[i] and amplitude[i + 1] < (amplitude[i]):
            peak_vec = np.append(peak_vec, amplitude[i])
        else:
            peak_vec = np.append(peak_vec, 0.0)
    peak_1_idx = np.argmax(peak_vec).astype(np.int32)   #searching for two 'loudest harmonics'
    peak_vec[peak_1_idx] = 0.0
    peak_2_idx = np.argmax(peak_vec)
    if peak_1_idx > peak_2_idx:
        peak_1_idx, peak_2_idx = peak_2_idx, peak_1_idx     
    freq_ratio = Fraction(peak_1_idx, peak_2_idx).limit_denominator(40)
    fundamental_idx = peak_1_idx / freq_ratio.numerator
    return fundamental_idx * freq_len   #idx * how many hertz between idxs

