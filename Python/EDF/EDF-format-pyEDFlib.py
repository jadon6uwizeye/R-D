# pyEDFlib is a python library to read/write EDF+/BDF+ files based on EDFlib.
from pyedflib import highlevel
import numpy as np

# write an edf file
signals = np.random.rand(5, 256*300)*200 # 5 minutes of random signal
# signals = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [2100,2200,2300,2400,2500]]

channel_names = ['Test1', 'ch2', 'ch3', 'ch4', 'ch5']

signal_headers = highlevel.make_signal_headers(channel_names, sample_frequency=256)
header = highlevel.make_header(patientname='patient_x', sex='Female')
highlevel.write_edf('./edf_file.edf', signals, signal_headers, header)
# save in csv file
np.savetxt("./signals.csv", signals, delimiter=",")




# # read an edf file
# signals, signal_headers, header = highlevel.read_edf('edf_file.edf', ch_names=['ch1', 'ch2'])
# print(signal_headers[0]['sample_frequency']) # prints 256

# # drop a channel from the file or anonymize edf
# highlevel.drop_channels('edf_file.edf', to_drop=['ch2', 'ch4'])
# highlevel.anonymize_edf('edf_file.edf', new_file='anonymized.edf'
#                          to_remove=['patientname', 'birthdate'],
#                          new_values=['anonymized', ''])
# # check if the two files have the same content
# highlevel.compare_edf('edf_file.edf', 'anonymized.edf')
# # change polarity of certain channels
# highlevel.change_polarity('file.edf', channels=[1,3])
# # rename channels within a file
# highlevel.rename_channels('file.edf', mapping={'C3-M1':'C3'})