import requests

outfile = open('station_metadata.dat','w')
outfile.writelines('Station#    Longitude    Latitude    Name    State\n')
for lines in open('station_num.txt','r'):
    api_url = "https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/"+lines[0:-1]+".xml?units=english"
    print "Processing "+api_url
    response = requests.get(api_url)
    sta_name = response.text.split("name>")[1][0:-2]
    state = response.text.split("state>")[1][0:-2]
    lat = response.text.split("lat>")[1][0:-2]
    lon = response.text.split("lng>")[1][0:-2]
    outfile.writelines(lines[0:-1]+'    '+lon+'    '+lat+'    '+sta_name+'    '+state+'\n')
outfile.close()