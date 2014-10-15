# coding: latin-1
from __future__ import division
from flask import Flask, render_template, jsonify
import OpenStockholmParser, os

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/stockholmAPI')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    coordinates = [59.33258778133236, 18.08694126883216]

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


@app.route('/storeseniro/')
def ddeadView():
    coordinates = [59.33258778133236, 18.08694126883216]
    return render_template("test/placesNearbyStoresENIROJS.html", coordinates=coordinates)


@app.route('/data/')
def opendata():
    #bara temporär funktion, datan bör sparas på ett bättre sätt
    #senaste datan är från 2011 ---- arbetstillfallen
    #senaste datan är från 2012 ---- antalbostader
    #senaste datan är från 2012 ---- flytt
    data = OpenStockholmParser.get_opendata(app.config['UPLOAD_FOLDER'])
    flyttnetto = data['SDO15']['2012']['flyttnetto']


    snittinkomst = data['SDO15']['2011']['INKOMST'] / data['SDO15']['2011']['INKOM_ANTAL']  # INKOMST/INKOM_ANTAL
    snittinkomst_change = (snittinkomst / (data['SDO15']['2010']['INKOMST']/ data['SDO15']['2010']['INKOM_ANTAL']))*100

    befolkningsmangd = data['SDO04']['2012']['befolkningsmangd']
    befolkningsmangd_change = (befolkningsmangd / data['SDO04']['2011']['befolkningsmangd'])*100

    lista = [
        u"Flyttnetto: "+str(flyttnetto),
        u"Snittinkomst per år: "+str(snittinkomst)+ u" Procentuell förändring: " + str(snittinkomst_change-100),
        u"Befolkning: "+str(befolkningsmangd)+ u" Procentuell förändring: " + str(befolkningsmangd_change-100)
    ]

    return render_template("test/openstockholm.html", lista=lista)

@app.route('/getopendata/')
def getopendata():
    #this will take quite a while
    OpenStockholmParser.save_opendata(app.config['UPLOAD_FOLDER'])
    return jsonify({"loading": "done"})

if __name__ == '__main__':
    #har inte tagit med parkering och fastighetskartan
    #print OpenStockholmParser.parseByggnadsregister(OpenStockholmParser.readFromFile(filenames[3]))
    app.run(debug=True)




