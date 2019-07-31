import os
import pydicom
from pydicom.data import get_testdata_files

filename = get_testdata_files("rtplan.dcm")[0]  # type: str
ds = pydicom.dcmread(filename)  # plan dataset
print(ds.PatientName)
ds.PatientName ="testHHHH"
ds.dir("setup")
print(ds.PatientSetupSequence[0])
ds.PatientSetupSequence[0].PatientPosition = "HFP"
ds.save_as("rtplan.dcm")
