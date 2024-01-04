# pyEDFlib is a python library to read/write EDF+/BDF+ files based on EDFlib.
from pyedflib import highlevel
import numpy as np

# write an edf file
def write_edf(filename, signals, signal_headers=None, header=None):
    if signals is None:
        signals = np.random.rand(5, 256 * 300) * 200  # 5 minutes of random signal

    if signal_headers is None:
        channel_names = ["ch1", "ch2", "ch3", "ch4", "ch5"]
        signal_headers = highlevel.make_signal_headers(
            channel_names,
            sample_rate=200,
            physical_min=-300,
            physical_max=300,
            digital_min=0,
            digital_max=4095,
        )

    if header is None:
        header = highlevel.make_header(patientname="patient_x", sex="Female")

    highlevel.write_edf(
        "./edf_file.edf" if filename is None else filename + ".edf",
        signals,
        signal_headers,
        header,
    )
    # save in csv file
    np.savetxt(
        "./signals.csv" if filename is None else filename + ".csv",
        signals,
        delimiter=",",
    )

    # return file location
    return filename + ".edf"


# # read an edf file
# signals, signal_headers, header = highlevel.read_edf('edf_file.edf', ch_names=['ch1', 'ch2'])
# print(signal_headers[0]['sample_frequency']) # prints 256

# # drop a channel from the file or anonymize edf
# highlevel.drop_channels('edf_file.edf', to_drop=['ch2', 'ch4'])
# highlevel.anonymize_edf('edf_file.edf', new_file='anonymized.edf'
#                          to_remove=['patientname', 'birthdate'],
#                          new_values=['anonymized', ''])
# # check if the two files have the same contentsample_rate
# highlevel.change_polarity('file.edf', channels=[1,3])
# # rename channels within a file
# highlevel.rename_channels('file.edf', mapping={'C3-M1':'C3'})
