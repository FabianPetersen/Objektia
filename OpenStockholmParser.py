# coding: latin-1
__author__ = 'Fabian'
def parseBefolkningsforandring(data):
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

def parseArbetslosa(data):
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

def parseArbetstillfallen(data):
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

def parseAntalBostader(data):
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


def parseFlytt(data):
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


def parseFolkmangd(data):
    dictionary = {}
    for i in data["data"]["befolkning"]:
        if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
            dictionary[i["AREA_CODE"]][i["YEAR"]] = {"befolkningsmangd": 0}

        dictionary[i["AREA_CODE"]][i["YEAR"]]["befolkningsmangd"] += int(i["BEF_ANTAL"])

    return dictionary


def parseInkomst(data):
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

def parseParking(data):
    dictionary = {}
    t = 0
    u = 0
    for i in data["features"]:
        '''if not i["AREA_CODE"] in dictionary:
            dictionary[i["AREA_CODE"]] = {}
        if not i["YEAR"] in dictionary[i["AREA_CODE"]]:
            dictionary[i["AREA_CODE"]][i["YEAR"]] = {"INKOMST": 0, "INKOM_ANTAL": 0, "INKOM2_ANTAL": 0}

        dictionary[i["AREA_CODE"]][i["YEAR"]]["INKOMST"] += int(i["INKOMST"])
        dictionary[i["AREA_CODE"]][i["YEAR"]]["INKOM_ANTAL"] += int(i["INKOM_ANTAL"])
        dictionary[i["AREA_CODE"]][i["YEAR"]]["INKOM2_ANTAL"] += int(i["INKOM2_ANTAL"])
        '''
        #{u'P-avgift endast bes\xf6k': 0, 'Reserverad p-plats buss': 0, 'Reserverad p-plats motorcykel': 0, 'Reserverad p-plats utryckningsfordon': 0, u'Reserverad p-plats r\xf6relsehindrad': 0, 'Reserverad p-plats beskickningsbil': 0, 'P Avgift, boende': 0}


        if "VF_PLATS_TYP" in i["properties"]:
            if not i["properties"]["VF_PLATS_TYP"] in dictionary:
                dictionary[i["properties"]["VF_PLATS_TYP"]] = 0
            dictionary[i["properties"]["VF_PLATS_TYP"]] += 1
            t += 1
            #print i["properties"]["VF_PLATS_TYP"]
        else:
            u += 1

    print t
    print u
    return dictionary