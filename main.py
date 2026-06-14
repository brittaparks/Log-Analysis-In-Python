#Using Pandas to analzye the vulnerabilities file I previously created.  

import pandas as pd

# Load the CSV file
data_frame = pd.read_csv("vulnerabilities.csv")

# Filter logs to identify patterns in a select few hostsl
critical_data_frame = data_frame[data_frame['Hostname'].isin(["Server01", "Server96","Server97"])]

# Group logs by the CVE column and count their activities
servers_in_use = critical_data_frame.groupby("CVE").size()
print(servers_in_use)
