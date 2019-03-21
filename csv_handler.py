import csv


def getKeywordsFromCsv(csv):
    # reading the csv file
    with open(csv, 'r') as file:
        keywords = []

        #sring cleaning
        for keyword in file:
            temp = keyword.replace(";", "").replace("\n", "")
            keywords.append(temp)

        return keywords

def saveAdsAsCsv(adslist, filename):

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        #adding header
        writer.writerow(['keyword'] + ['text'] + ['link'])

        for adObject in adslist:
            #iterate through ad dict
            for ad in adObject.ad_list:
                writer.writerow([adObject.title] + [ad['text']] + [ad['ad_link']])
