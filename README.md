These 3 python codes download tide gauges data and station metadata from NOAA CO-OPS through their API 
NOAA CO-OPS: https://tidesandcurrents.noaa.gov/map/index.html
NOAA CO-OPS API: https://www.tidesandcurrents.noaa.gov/api-helper/url-generator.html

COOPS_metadata.py:
It downloads the metadata of the selected stations whose IDS are provided as a list in a separate file 'station_num.txt'.
Input: A list of desired station IDs in a file ('station_num.txt')
Output: A list of metadata of the desired stations

COOPS_obs_download.py:
It downloads the observed hourly tidal gauge data of the selected stations.
Input: A list of desired station IDs in a file ('station_num.txt')
Output: Available hourly observed tidal gauge data from year_str to year_end 
Each station is saved in a file separately. Time with no valid data will not output.
Datum is mean sea level (MSL); time zone is GMT; units are metric.

COOPS_pre_download.py:
It downloads the predicted hourly tidal gauge data of the selected stations.
Input: A list of desired station IDs in a file ('station_num.txt')
Output: Available hourly predicted tidal gauge data from year_str to year_end 
Each station is saved in a file separately. Time with no valid data will not output.
Datum is mean sea level (MSL); time zone is GMT; units are metric.
The original predicted data are 6-min data. Here we only save the values at **:00 to save time and space  

@author: Tianning Wu (twu27@ncsu.edu)
