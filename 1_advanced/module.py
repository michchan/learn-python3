# --------------- Standard Modules ---------------
# "time" is written in C language
import time
# "os" is a "os.py" python file
import os
# --------------- Third-party Modules ---------------
# Rename a module with "as"
import pandas as pd

file_path = 'assets/temps_today.csv'
# Suppose you want to read the file on every second
while True:
    # Check if the file exists
    if os.path.exists(file_path):
        # A data frame is created
        data = pd.read_csv(file_path)
        print(data.mean())
        print(data.mean()['st1'])
    else:
        print('File does not exist.')
    # Wait a number of second
    time.sleep(1)

