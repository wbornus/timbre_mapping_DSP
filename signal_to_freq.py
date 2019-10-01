import numpy as np
import extract_fundamental_freq as fq
def signal_to_freq(signal, fs, number_of_samples = 8096):
    """
    signal: given signal to convert into list of fundamental frequencies
    fs: sampling frequency
    number of samples: how many samples are processed at once
    returns list of fundamental frequencies in each processed chunk of signal
    """
    freq_list = []
    signal_end_sample_len = signal%number_of_samples
    if signal_end_sample_len != 0:
        len_to_append = number_of_samples - signal_end_sample_len
        signal.append(np.zeros(len_to_append))
    for i in range((len(signal) / number_of_samples) - 1): #iterating over chunks of signal
        chunk = signal[i : i + number_of_samples]
        freq_list.append(fq.extract_fundamental_freq(chunk, fs))
    return freq_list, number_of_samples