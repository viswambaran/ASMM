
# Importing packages ------------------------------------------------------

import pandas as pd
import numpy as np 

# Reading in data ------------------------------------------------------

years = np.arange(0,23) 
years_1 = np.arange(1,24)

## Convert to string and add trailing 0 
## required for website url data is stored on 

years = years.astype(str)
years = np.char.zfill(years, 2)

years_1 = years_1.astype(str)
years_1 = np.char.zfill(years_1, 2)

## Combining to give out the final years
url_years = np.core.defchararray.add(years, years_1)

data_url_base = 'https://www.football-data.co.uk/mmz4281/{Year}/E0.csv'

## creating list with all urls required
data_urls_list = []
for year in url_years:
    url_year = data_url_base.replace('{Year}', year)
    data_urls_list.append(url_year)

