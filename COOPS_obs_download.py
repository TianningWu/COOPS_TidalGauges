# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 10:37:31 2020

Download observed hourly sea level data from NOAA CO-OPS
https://tidesandcurrents.noaa.gov/map/index.html
API: https://www.tidesandcurrents.noaa.gov/api-helper/url-generator.html
Datum is mean sea level (MSL); time zone is GMT; units are metric

Input: A list of desired Station IDs in a file ('station_num.txt')
Output: Avalible hourly sea level data from year_str to year_end. 
Each station is put in a file separately. Time with no valid data will not output.

The metadata are requested through another code COOPS_metadata.py
@author: Tianning Wu
"""

import requests

api_head = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?"

year_str = 1900
year_end = 2020

for st in open('station_num.txt','r'):
    st_id = st.rstrip()
    outfile = open('obshourly\COOPS_SLobs_hr_'+st_id+'.dat','w')
    for yyyy in range(year_str,year_end+1):
        begindate = str(yyyy)+'0101'
        enddate = str(yyyy)+'1231'
        api_url = api_head+'begin_date='+begindate+'&end_date='+enddate+'&station='+st_id+'&product=hourly_height&datum=MSL&time_zone=gmt&units=metric&format=xml'
        print "Processing "+api_url
        response = requests.get(api_url)
        for lines in response.text.split('\n'):
            if 'No data was found' in lines:
                print "No data"
                continue
            elif '<hr' in lines:
                sl_time = lines.split('=')[1][1:-4]
                sl_value = lines.split('=')[2][1:-3]
                if len(sl_value)==0:
                    continue          
                outfile.writelines(sl_time+'    '+sl_value+'\n')
    outfile.close()