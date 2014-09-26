# coding: latin-1
from flask import Flask, render_template

app = Flask(__name__)

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
         u"name":u"Allma��������ng man skulle kunna skriva mycket i",
         u"imageURL": u"/static/carbon.jpg",
         u"size": u"7000 m2",
         u"land": u"400ha skog",
         u"cost": u"510 151 156kr",
         u"description": u"lrlrlrg rgllrg llrg  l rgll rgl  lr glr glrg lrg rl rg lrg rlg rlg rlg rlg rlg rlg rlg rlg gr "
        },
        {
         u"name":u"Allm�ng text som man skulle kunna skriva mycket i",
         u"imageURL": u"/static/carbon.jpg",
         u"size": u"7000 m2",
         u"land": u"400ha skog",
         u"cost": u"510 151 156kr",
         u"description": u"lrlrlrg rgllrg llrg  l rgll rgl  lr glr glrg lrg rl rg lrg rlg rlg rlg rlg rlg rlg rlg rlg gr "
        }
    ]
    places = [[-33.8665433, 151.1956316], [-33.8685433, 151.1156316], [-33.8625433, 151.1156316], [-33.8664433, 151.1756316], [-33.8666433, 151.1955316], [-33.8665433, 151.1957316]]
    placesnames = [u'Den d�r gatan, G�vle', u'Den d�r andra gatan, G�vle', u'Den d�r tredje gatan, G�vle',  u'Den d�r fj�rde gatan, G�vle',  u'Den d�r femte gatan, G�vle',
                   u'Den d�r sj�tte gatan, G�vle',  u'Den d�r sjunde gatan, G�vle']
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
        [u"fun���ny header"],
        [u"row header", u"row content"],
        [u"another funny header"]
    ]
    return render_template("adView.html", origins=origins, destinations=destinations, coordinates=coordinates, types=type_of_stores, radius=radius, images=images, rows=rows)



if __name__ == '__main__':
    app.run(debug=True)
