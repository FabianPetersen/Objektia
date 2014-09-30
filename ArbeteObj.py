# coding: latin-1
from __future__ import division
from flask import Flask, render_template
import requests, xmltodict,json
import pprint
import OpenStockholmParser

app = Flask(__name__)
filenames = ["arbetstillfallen", "befolkningsforandring", "antalbostader", "byggnadsregister", "flytt", "folkmangd", "inkomst", "arbetslöshet"]

@app.route('/')
def index():

    ads = [
        {
         u"name":u"Allmang text som man skulle kunna skriva mycket i",
         u"imageURL": u"/static/carbon.jpg",
         u"size": u"7000 m2",
         u"land": u"400ha skog",
         u"cost": u"510 151 156kr",
         u"description": u"lrlrlrg rgllrg llrg  l rgll rgl  lr glr glrg lrg rl rg lrg rlg rlg rlg rlg rlg rlg rlg rlg gr "
        },
        {
         u"name":u"Allmaääääääääng man skulle kunna skriva mycket i",
         u"imageURL": u"/static/carbon.jpg",
         u"size": u"7000 m2",
         u"land": u"400ha skog",
         u"cost": u"510 151 156kr",
         u"description": u"lrlrlrg rgllrg llrg  l rgll rgl  lr glr glrg lrg rl rg lrg rlg rlg rlg rlg rlg rlg rlg rlg gr "
        },
        {
         u"name":u"Allmäng text som man skulle kunna skriva mycket i",
         u"imageURL": u"/static/carbon.jpg",
         u"size": u"7000 m2",
         u"land": u"400ha skog",
         u"cost": u"510 151 156kr",
         u"description": u"lrlrlrg rgllrg llrg  l rgll rgl  lr glr glrg lrg rl rg lrg rlg rlg rlg rlg rlg rlg rlg rlg gr "
        }
    ]
    places = [[-33.8665433, 151.1956316], [-33.8685433, 151.1156316], [-33.8625433, 151.1156316], [-33.8664433, 151.1756316], [-33.8666433, 151.1955316], [-33.8665433, 151.1957316]]
    placesnames = [u'Den där gatan, Gävle', u'Den där andra gatan, Gävle', u'Den där tredje gatan, Gävle',  u'Den där fjärde gatan, Gävle',  u'Den där femte gatan, Gävle',
                   u'Den där sjätte gatan, Gävle',  u'Den där sjunde gatan, Gävle']
    placesid = [u'gatan1', u'gatan2', u'gatan3',  u'gatan4',  u'gatan5',
                   u'gatan6',  u'gatan7']

    return render_template("adList.html", ads=ads, places=places, placesnames=placesnames, placesid=placesid)

@app.route('/ad/<adId>')
def adView(adId):
    origins = [u'Halmstad, Sweden']
    destinations = [u'Stockholm, Sweden', u'Uddevalla, Sweden']
    coordinates = [-33.8665433, 151.1956316]

    type_of_stores = ['store']
    radius = 500

    images = [
        {
            "regular": "/static/images/large/01.jpg",
            "thumb": "/static/images/thumbnail/thumb-01.jpg"
        },
        {
            "regular": "/static/images/large/01.jpg",
            "thumb": "/static/images/thumbnail/thumb-01.jpg"
        },
        {
            "regular": "/static/images/large/01.jpg",
            "thumb": "/static/images/thumbnail/thumb-01.jpg"
        },
        {
            "regular": "/static/images/large/01.jpg",
            "thumb": "/static/images/thumbnail/thumb-01.jpg"
        }
    ]

    rows = [
        [u"funääöny header"],
        [u"row header", u"row content"],
        [u"another funny header"]
    ]
    return render_template("adView.html", origins=origins, destinations=destinations, coordinates=coordinates, types=type_of_stores, radius=radius, images=images, rows=rows)


@app.route('/data/')
def opendata():
    #
    #bara temporär funktion, datan bör sparas på ett bättre sätt
    #och självklart inte parsas varje gång
    #
    #

    #över de senaste 5åren
    befolkningsforandring =  OpenStockholmParser.parseBefolkningsforandring(readFromFile(filenames[1]))

    arbetslosa = OpenStockholmParser.parseArbetslosa(readFromFile(filenames[7]))

    #senaste datan är från 2011
    arbetstillfallen =  OpenStockholmParser.parseArbetstillfallen(readFromFile(filenames[0]))

    #senaste datan är från 2012
    antalbostader = OpenStockholmParser.parseAntalBostader(readFromFile(filenames[2]))

    #senaste datan är från 2012
    flytt = OpenStockholmParser.parseFlytt(readFromFile(filenames[4]))

    folkmangd = OpenStockholmParser.parseFolkmangd(readFromFile(filenames[5]))

    inkomst = OpenStockholmParser.parseInkomst(readFromFile(filenames[6]))

    flyttnetto = befolkningsforandring['SDO15']['2012']['flyttnetto']


    snittinkomst = inkomst['SDO15']['2011']['INKOMST'] / inkomst['SDO15']['2011']['INKOM_ANTAL']  # INKOMST/INKOM_ANTAL
    snittinkomst_change = (snittinkomst / (inkomst['SDO15']['2010']['INKOMST']/ inkomst['SDO15']['2010']['INKOM_ANTAL']))*100

    befolkningsmangd = folkmangd['SDO04']['2012']['befolkningsmangd']
    befolkningsmangd_change = (befolkningsmangd / folkmangd['SDO04']['2011']['befolkningsmangd'])*100

    lista = [
        u"Flyttnetto: "+str(flyttnetto),
        u"Snittinkomst per år: "+str(snittinkomst)+ u" Procentuell förändring: " + str(snittinkomst_change),
        u"Befolkning: "+str(befolkningsmangd)+ u" Procentuell förändring: " + str(befolkningsmangd_change)
    ]

    return render_template("test/openstockholm.html", lista=lista)

def getAllOpenData(url, filenames):
    for i in range(len(filenames)):
        filename = "C:\Users\Fabian\PycharmProjects\ArbeteObj\Static\StockholmAPI\\" + filenames[i] + ".txt"
        saveToFile(filename, url[i])


def saveToFile(filename, url):
    r = requests.get(url)
    f = open(filename, 'w')

    r = xmltodict.parse(r.content)
    f.write(json.dumps(r))

def readFromFile(filenames):
    #for i in filenames:
    f = open("C:\Users\Fabian\PycharmProjects\ArbeteObj\Static\StockholmAPI\\" + filenames + ".txt", 'r+')
    return json.loads(f.read())

def getParkingData(parkingurl):
    filename = "C:\Users\Fabian\PycharmProjects\ArbeteObj\Static\StockholmAPI\\" + "parking" + ".txt"
    r = requests.get(parkingurl)
    f = open(filename, 'w')

    f.write(r.content)

if __name__ == '__main__':
    #har inte tagit med parkering och fastighetskartan
    #"http://data.stockholm.se/set/Befolkning/prognos_2020?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
    #not working

    url = ["http://data.stockholm.se/set/Befolkning/Arbetstillfallen?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Befforandr?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Bostader_flerbostadshus?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Kultur/Byggnadsregister?apikey=A3PC00KE72SCA68A1F2918L40F830AL3",
           "http://data.stockholm.se/set/Befolkning/flyttningar?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Befolkning?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Medelinkomst?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Arbetslosa?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC"]

    #getAllOpenData(url, filenames)
    parkingurl = "http://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/within?radius=1000&lat=59.32784&lng=18.05306&outputFormat=json&apiKey=4a8197bc-01b8-47c0-82d8-db93d5037b9d"
    parkingurl = "http://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/weekday?outputFormat=json&apiKey=4a8197bc-01b8-47c0-82d8-db93d5037b9d"
    parkingurl = "http://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/all?outputFormat=json&apiKey=4a8197bc-01b8-47c0-82d8-db93d5037b9d"
    #getParkingData(parkingurl)




    #print OpenStockholmParser.parseParking(readFromFile("parking"))

    app.run(debug=True)



