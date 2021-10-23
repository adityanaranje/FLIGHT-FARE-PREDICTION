import numpy as np
import pickle

airlines = ['IndiGo', 'Air India', 'Jet Airways', 'SpiceJet',
       'Multiple carriers', 'GoAir', 'Vistara', 'Air Asia',
       'Vistara Premium economy', 'Jet Airways Business',
       'Multiple carriers Premium economy', 'Trujet']
sources = ['Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai']
dests = ['Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Hyderabad']
stops = [0,1,2,3,4]
addinfos = ['No Info', 'In-flight meal not included','No check-in baggage included',
    '1 Short layover','1 Long layover', 'Change airports', 'Business class',
    'Red-eye flight', '2 Long layover']
durhrs = np.arange(0,21)
durmins = np.arange(0,60)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dates = np.arange(1,32)
dephrs = np.arange(0,24)
depmins = np.arange(0,60)
arrhrs = np.arange(0,24)
arrmins = np.arange(0,60)

model = pickle.load(open('model/pipe.pkl','rb'))