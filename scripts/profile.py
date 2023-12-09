import pandas as pd
import os
from ydata_profiling import ProfileReport
wine_dataset = pd.read_csv('data/wine/wine.data')
profile = ProfileReport(wine_dataset, title= "Wine Data Profiling Report")
profile.to_file('profiling/report.html')
