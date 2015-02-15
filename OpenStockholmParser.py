# coding: latin-1
__author__ = 'Fabian'
import requests, json, os


def parse_befolkningsforandring(data):
    dictionary = {}
    for i in data["data"]["befforandr"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
            dictionary[i["AREA_CODE"]][i["YEAR"]] = {u"födelsenetto": 0, "flyttnetto": 0}

        #svenska tecken 'kräver' unicode
        if i["MFORANDK_TEXT"] == u"födelsenetto" or i["MFORANDK_TEXT"] == "flyttnetto":
            dictionary[i["AREA_CODE"]][i["YEAR"]][i["MFORANDK_TEXT"]] += int(i["BEFOR6_ANTAL"])

    return dictionary


def parse_arbetslosa(data):
    dictionary = {}
    for i in data["data"]["arbetslosa"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
                #arbetslosa2013, totalbefolkning2013, arbetslösa2009, totalbefolkning2009
                dictionary[i["AREA_CODE"]][i["YEAR"]] = {"ALOKT_ANTAL":0, "OCT_ANTAL": 0}


        dictionary[i["AREA_CODE"]][i["YEAR"]]["ALOKT_ANTAL"] += int(i["ALOKT_ANTAL"])
        dictionary[i["AREA_CODE"]][i["YEAR"]]["OCT_ANTAL"] += int(i["OCT_ANTAL"])


    return dictionary


def parse_arbetstillfallen(data):
    dictionary = {}

    for i in data["data"]["arbetstillfallen"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
                #FSNI5_ANTAL = nattbefolkning, FDSNI5_ANTAL = dagsbefolkning
                dictionary[i["AREA_CODE"]][i["YEAR"]] = {"FSNI5_ANTAL":0, "FDSNI5_ANTAL": 0}

        dictionary[i["AREA_CODE"]][i["YEAR"]]["FSNI5_ANTAL"] += int(i["FSNI5_ANTAL"])
        dictionary[i["AREA_CODE"]][i["YEAR"]]["FDSNI5_ANTAL"] += int(i["FDSNI5_ANTAL"])

    return dictionary


def parse_antal_bostader(data):
    dictionary = {}
    for i in data["data"]["bostader_flerbostadshus"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
            dictionary[i["AREA_CODE"]][i["YEAR"]] = {u'\xf6vr. hyresr\xe4tter': 0, u'bostadsr\xe4ttsf\xf6r.': 0, u'allm\xe4nnyttan': 0}
                #AGKAT_CODE 3 = 'bostadsrättsför
                #AGKAT_CODE 2 = övr. hyresrätter
                #AGKAT_CODE 1 = allmännyttan

        dictionary[i["AREA_CODE"]][i["YEAR"]][i["AGKAT_TEXT"]] += int(i["LAGK_ANTAL"])

    return dictionary


def parse_flytt(data):
    dictionary = {}
    for i in data["data"]["flyttningar"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
                #AGKAT_CODE 3 = 'bostadsrättsför
                #AGKAT_CODE 2 = övr. hyresrätter
                #AGKAT_CODE 1 = allmännyttan
                dictionary[i["AREA_CODE"]][i["YEAR"]] = {'ut till utlandet': 0, u'ut till \xf6vr Sverige': 0, u'ut till \xf6vr l\xe4net': 0, u'ut till \xf6vr Sthlm': 0,
                                              'in fr utlandet': 0, u'in fr \xf6vr Sverige': 0, u'in fr \xf6vr l\xe4net': 0, "inomflyttning": 0, u'in fr \xf6vr Sthlm':0}

        dictionary[i["AREA_CODE"]][i["YEAR"]][i["FLYTT3K_TEXT"]] += int(i["FLYTT6_ANTAL"])


    return dictionary


def parse_folkmangd(data):
    dictionary = {}
    for i in data["data"]["befolkning"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
            dictionary[i["AREA_CODE"]][i["YEAR"]] = {"befolkningsmangd": 0}

        dictionary[i["AREA_CODE"]][i["YEAR"]]["befolkningsmangd"] += int(i["BEF_ANTAL"])

    return dictionary


def parse_inkomst(data):
    dictionary = {}
    for i in data["data"]["medelinkomst"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
            dictionary[i["AREA_CODE"]][i["YEAR"]] = {"INKOMST": 0, "INKOM_ANTAL": 0, "INKOM2_ANTAL": 0}

        dictionary[i["AREA_CODE"]][i["YEAR"]]["INKOMST"] += int(i["INKOMST"])
        dictionary[i["AREA_CODE"]][i["YEAR"]]["INKOM_ANTAL"] += int(i["INKOM_ANTAL"])
        dictionary[i["AREA_CODE"]][i["YEAR"]]["INKOM2_ANTAL"] += int(i["INKOM2_ANTAL"])

    return dictionary

def parse_byggnadsregister(data):
    dictionary = {}

    for i in data['data']['byggnadsregister']:
        print i
        break

    return dictionary


def save_opendata(uploadfolder):
    dictionary = {}
    url = ["http://data.stockholm.se/set/Befolkning/Arbetstillfallen?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Befforandr?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Bostader_flerbostadshus?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Kultur/Byggnadsregister?apikey=A3PC00KE72SCA68A1F2918L40F830AL3",
           "http://data.stockholm.se/set/Befolkning/flyttningar?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Befolkning?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Medelinkomst?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC",
           "http://data.stockholm.se/set/Befolkning/Arbetslosa?apikey=6CR9U95D68Q8J258E830XCE874Z0J6IC"]
    filenames = ["arbetstillfallen", "befolkningsforandring", "antalbostader", "byggnadsregister", "flytt", "folkmangd", "inkomst", "arbetslöshet"]
    for i in range(len(filenames)):
        print str(i+1) + "/" + str(len(filenames))
        tempdict = {}

        r = requests.get(url[i])
        r = xmltodict.parse(r.content)

        if i == 0:
            tempdict = parse_arbetstillfallen(r)
        elif i == 1:
            tempdict = parse_befolkningsforandring(r)
        elif i == 2:
             tempdict = parse_antal_bostader(r)
        elif i == 4:
            tempdict = parse_flytt(r)
        elif i == 5:
            tempdict = parse_folkmangd(r)
        elif i == 6:
            tempdict = parse_inkomst(r)
        elif i == 7:
            tempdict = parse_arbetslosa(r)

        #example ["outerkey"]["innerkey"]["even_inner_key"] = "value"
        #merge the data from the tempdict with the dictionary
        for outerkey in tempdict.keys():
            for innerkey in tempdict[outerkey].keys():
                if not outerkey in dictionary.keys():
                    dictionary[outerkey] = {}
                if not innerkey in dictionary[outerkey].keys():
                    dictionary[outerkey][innerkey] = tempdict[outerkey][innerkey]
                else:
                    for even_inner_key in tempdict[outerkey][innerkey].keys():
                        dictionary[outerkey][innerkey][even_inner_key] = tempdict[outerkey][innerkey][even_inner_key]

    save_to_file(uploadfolder, dictionary)
    print "Done getting openData"


def save_to_file(uploadfolder, data):
    filename = "openstockholmdata.txt"
    f = open(os.path.join(uploadfolder, filename), 'w')
    f.write(json.dumps(data))
    f.close()


def read_from_file(filename):
    f = open(filename, 'r+')
    return json.loads(f.read())


def get_opendata(uploadfolder):
    filename = "openstockholmdata.txt"
    f = open(os.path.join(uploadfolder, filename), 'r+')
    return json.loads(f.read())