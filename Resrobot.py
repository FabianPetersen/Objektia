# coding: latin-1
__author__ = 'Fabian'
import requests, os
import json
url = "http://api.sl.se/api2/FileService?key=801b9c420711419481bc0507e98d7bad&filename="
filenames = ["JourneyPatternPointOnLine.csv", "Lines.csv", "Sites.csv", "StopPoints.csv", "Transportmode.csv"]

def save_resrobot(uploadfolder):
    alldata = {}
    #get data from resrobot
    for i in range(len(filenames)):
        r = requests.get(url + filenames[i])
        alldata[filenames[i]] = r.content
        print filenames[i]
    interpret_resrobot(alldata, uploadfolder)

def interpret_resrobot(input, uploadfolder):
    print "Start processing resrobot linjer"
    output = {}
    #loop over keys
    for filename in input.iterkeys():
        lines = input[filename].split("\r\n") # "\r\n" if needed
        #col names
        titles = lines[0].split(";")
        output[filename] = []
        for line in lines[1:]:
            if line != "":#to avoid empty rows
                object_to_append = {}
                cols = line.split(";")
                for d in range(len(titles)):
                    object_to_append[titles[d]] = cols[d]
                output[filename].append(object_to_append)

    f = open(os.path.join(uploadfolder, "ResrobotLinjer.json"), 'w')
    f.write(json.dumps(output))
    f.close()
    print "Done processing"