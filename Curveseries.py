# First download  CSDataAPI on curveseries website. 
#GLUCK running... I had it running once, and now it crashes my terminal...


#Start of code
import CSDataAPI
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


equation= "Swap_Nap_FP_2019F.Close"
start_date= "01-Jan-2018"
end_date= "31-Jan-2018"

#getting historical timeseries
result = CSDataAPI.getCSData(equation, start_date, end_date)
result = np.array(result)


data = np.array(result)

# Extract dates and values
dates = [datetime.strptime(date, '%d-%b-%Y %H:%M:%S.%f') for date in data[:, 0]]
values = data[:, 1].astype(float)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(dates, values, marker='o', linestyle='-')
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()