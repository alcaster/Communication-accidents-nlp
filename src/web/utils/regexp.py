import csv
import re
from geo_decoder import GeoEncoder
from sklearn.cluster import KMeans
import itertools
def remove_duplicates(values):
    output = list()
    seen = list()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.append(value)
    return output
with open('ret.csv', 'a+', newline='') as csvfilewrite:
    spamwriter = csv.writer(csvfilewrite, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(["start date", "end date", "startHour", "endHour", "x", "y"])
    with open('../../../data/ztm_newsfeed/ztmmessages.csv', newline='') as csvfileread:
        spamreader = csv.DictReader(csvfileread, delimiter='|', quotechar='"')
        'ĄĘŁŃÓŚŹŻ'

        ge = GeoEncoder()
        i = 5000
        for row in spamreader:
            if i > 4200:
                i = i - 1
                continue
            i = i -1
            endOfString = str(row['content']).find('Inne zmiany')
            if endOfString > 0:
                message = str(row['content'])[:endOfString]
            else:
                message = str(row['content'])

            date = re.findall(r'(dn.|dniu|dnia|od|do) (\d{1}|\d{2})(.\d{2})(.\D|.\d{4})', message)
            hour = re.findall(r'(\d{2}:\d{2}| \d{1}:\d{2})', message)
            busStops = remove_duplicates(re.findall(r'([A-ZĄĘŁŃÓŚŹŻ][A-ZĄĘŁŃÓŚŹŻ.]+[A-ZĄĘŁŃÓŚŹŻ ]+)', message))
            pkpStops = remove_duplicates(re.findall(r'(PKP [a-zA-ZĄĘŁŃÓŚŹŻąęłńóśżź]+)', message))
            wkdStops = remove_duplicates(re.findall(r'(WKD [a-zA-ZĄĘŁŃÓŚŹŻąęłńóśżź]+)', message))
            metroStops = remove_duplicates(re.findall(r'(M. [a-zA-ZĄĘŁŃÓŚŹŻąęłńóśżź]+)', message))
            chStops = remove_duplicates(re.findall(r'(CH [a-zA-ZĄĘŁŃÓŚŹŻąęłńóśżź]+)', message))
            streets = remove_duplicates(re.findall(r'(-|–)([^–,;:.]+)', message))
            streets2 = remove_duplicates(re.findall(r'(ul|ulica|ulic|ulicy) ([^–,;:. ]+) ', message))

            print (date, hour, busStops, pkpStops, wkdStops, metroStops, chStops, streets, streets2)
            startDate = ''
            endDate = ''
            if len(date) > 0:
                startDate = ''
                for s in date[0]:
                    result = re.findall(r'\d+', s)
                    startDate = startDate + '.' + ''.join(result)

                startDate = re.search(r'\d.+', startDate).group(0)
            if len(date) > 1:
                for s in date[1]:
                    result = re.findall(r'\d+', s)
                    endDate = endDate + '.' + ''.join(result)
                endDate = re.search(r'\d.+', endDate).group(0)

            if len(date) == 1:
                endDate = startDate

            startHour = ''
            endHour = ''
            if len(hour) == 0:
                startHour = '0000'
                endHour = '2359'
            if len(hour) > 0:
                s = hour[0]
                result = re.findall(r'\d+', s)
                startHour = startHour + ''.join(result)
            if len(hour) > 1:
                s = hour[1]
                result = re.findall(r'\d', s)
                endHour = endHour +  ''.join(result)
            if len(hour) == 1:
                endHour = '2359'

            properBusStops = list()

            if len(busStops) > 0:
                for s in busStops:
                    if s.find(". ") != -1:
                        s = s.replace(". ", ".")
                    # print(s)
                    if (s.find('PKP') and s.find('II ') and s.find('UWAGA') and s.find('M.') and s.find("META") and
                    s.find('WKD') and s.find("M.") and s.find("ETAP") and s.find("TRAMWAJE") and s.find("LOTTO") and
                    s.find("SKM") and s.find("ZP ") and s.find("CH ") and s.find("ZW ") and s.find("EC ") and
                    s.find("ZTM") and s.find("PKT") and s.find("OBOWIĄZUJĄ TRASY") and s.find("AUTOBUSY") and s.find("KOMUNIKACJA") and
                    s.find("PŁATNE") and s.find("ML ")) == -1:
                        properBusStops.append(s)
            if 10 > len(properBusStops):
                busStops = properBusStops
            else: busStops = ""

            properStreets = list()
            if 15 > len(streets) > 0:
                for s in streets:
                    properStreets.append(s[1])

            pointsForCluster = list()
            for s in properStreets:
                try:
                    tmp = ge.get_geo_coordinates(s, "street")
                    pointsForCluster.append([tmp[0], tmp[1]])
                except TypeError and IndexError:
                    print("wrong ret type")
            for s in busStops:
                try:
                    tmp = ge.get_geo_coordinates(s, "bus_stop")
                    pointsForCluster.append([tmp[0], tmp[1]])
                except TypeError:
                    print("wrong ret type")

            for s in pkpStops:
                try:
                    tmp = ge.get_geo_coordinates(s, "street")
                    pointsForCluster.append([tmp[0], tmp[1]])
                except TypeError:
                    print("wrong ret type")
            for s in chStops:
                try:
                    tmp = ge.get_geo_coordinates(s, "street")
                    pointsForCluster.append([tmp[0], tmp[1]])
                except TypeError:
                    print("wrong ret type")
            for s in metroStops:
                try:
                    tmp = ge.get_geo_coordinates(s, "street")
                    pointsForCluster.append([tmp[0], tmp[1]])
                except TypeError:
                    print("wrong ret type")
            for s in wkdStops:
                try:
                    tmp = ge.get_geo_coordinates(s, "street")
                    pointsForCluster.append([tmp[0], tmp[1]])
                except TypeError:
                    print("wrong ret type")


            pointsForCluster = remove_duplicates(pointsForCluster)
            if len(pointsForCluster) > 2:
                est = KMeans(n_clusters=2)
                est.fit(pointsForCluster)
                pointsForCluster = est.cluster_centers_
            print(pointsForCluster)
            for p in pointsForCluster:
                    spamwriter.writerow([startDate, endDate, startHour, endHour, p[0], p[1]])
            if i < 1:
               break