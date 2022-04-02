# importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
from os import path

import pandas
import os

# prepare some data
df = pandas.read_csv("https://pythonizing.github.io/data/bachelors.csv")
x = df["Year"]
y = df["Engineering"]

# prepare the output file
output_file(path.join(path.dirname(__file__), "Line_from_bachelors.html"))

# create a figure object
f = figure()

# create line plot
f.line(x, y)

# write the plot in the figure object
show(f)

# Problem: ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1122)
# Sol: Run `sudo '/Applications/Python 3.9/Install Certificates.command'` (https://stackoverflow.com/a/58525755)
