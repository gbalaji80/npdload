import requests
import csv
import sys
import re
import os

dailyPaper=""
dailyYear=""
dailyMonth=""
dailyDate=""

mwIssueNumber=""

ftURL="https://freemagazines.top/financial-times-"
ttURL="https://freemagazines.top/the-times-"
ftwkURL="https://freemagazines.top/financial-times-weekend-uk-"
wsjURL="https://freemagazines.top/the-wall-street-journal-"
wpURL="https://freemagazinespdf.com/the-washington-post-"
ecoURL="https://freemagazines.top/the-economist-usa-"
tgURL="https://freemagazines.top/the-guardian-"
brURL="https://freemagazines.top/barrons-"
brmURL="https://freemagazines.top/barrons-magazine-"
mwURL="https://freemagazines.top/moneyweek-issue-"




configFile="config.csv"
#path="/home/balaji/Documents/googleDrive/news/"
path="/mnt/sda/docs/news/"

def getMonth(dailyMonth):
    if dailyMonth == "01":
        return "january"
    elif dailyMonth == "02":
        return "february"
    elif dailyMonth == "03":
        return "march"
    elif dailyMonth == "04":
        return "april"
    elif dailyMonth == "05":
        return "may"
    elif dailyMonth == "06":
        return "june"
    elif dailyMonth == "07":
        return "july"
    elif dailyMonth == "08":
        return "august"
    elif dailyMonth == "09":
        return "september"
    elif dailyMonth == "10":
        return "october"
    elif dailyMonth == "11":
        return "november"
    elif dailyMonth == "12":
        return "december"

def getMonthCode(dailyMonth):
    if dailyMonth == "01":
        return "JAN"
    elif dailyMonth == "02":
        return "FEB"
    elif dailyMonth == "03":
        return "MAR"
    elif dailyMonth == "04":
        return "APR"
    elif dailyMonth == "05":
        return "MAY"
    elif dailyMonth == "06":
        return "JUN"
    elif dailyMonth == "07":
        return "JUL"
    elif dailyMonth == "08":
        return "AUG"
    elif dailyMonth == "09":
        return "SEP"
    elif dailyMonth == "10":
        return "OCT"
    elif dailyMonth == "11":
        return "NOV"
    elif dailyMonth == "12":
        return "DEC"

        
def getDate(dailyPaper,dailyDate):
    return dailyDate
    if dailyPaper == "ft":
        
        if dailyDate.startswith('0'):
            return dailyDate[1:]
        else:
            return dailyDate
        
    else:
        return dailyDate

def extractUrl(dailyPaper,dailyYear,dailyMonth,dailyDate):
    if dailyPaper == "ft":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = ftURL+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        #URL = ftURL+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL 
    elif dailyPaper == "tt":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL=ttURL+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        #URL = ftURL+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "ftwk":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = ftwkURL+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "wsj":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = wsjURL+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "wp":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = wpURL+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "gm":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = "https://freemagazinespdf.com/The_Globe_and_Mail-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "eco":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = ecoURL+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "tg":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = tgURL + dailyDate + "-" + dailyMonth + "-" + dailyYear+"/"
        return URL
    elif dailyPaper == "br":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = brURL+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "brm":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = brmURL+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "mw":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = mwURL+mwIssueNumber+"-"+dailyDate+"-" + dailyMonth  + "-" + dailyYear +"/"
        return URL 
    
with open(configFile, newline='') as csvfile:
    valuesExtracted = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for line in valuesExtracted:
        if line[0].startswith("#"):
            continue

        currentline = line[0].split(",")
        dailyPaper=currentline[0]
        dailyYear=currentline[1]
        dailyMonth=currentline[2]
        dailyDate=currentline[3]
        
        if dailyPaper=="mw":
            mwIssueNumber=currentline[4]
        URL=extractUrl(dailyPaper,dailyYear,dailyMonth,dailyDate)
        headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
        print("URL:\t" + URL)
        page= requests.get(URL.strip(), headers=headers, timeout=10)
        pageText = page.text
        #print(pageText)
        #urls = re.findall('https?://(vk.com/doc[\\d].*_\\d+)', pageText)
        #urls = re.findall('https?://(vk.com/doc[\\d]+_\\d+)', pageText)
        #urls = re.findall('https?:\/\/(vk.com\/s\/v1\/doc\/[\d\w\-]+\-\w+)', pageText)
        
        urls = re.findall('(vk.com/s/v1/doc/[\-\_a-zA-Z0-9]+)',pageText)
        #urls = re.findall('(vk.com/s/v1/doc/\w+)',pageText)

        print(urls)
        #https://vk.com/s/v1/doc/fLSqkf3747eWwfDMFGCi4uTQcEU_qOm617l2tm7vWfrm_UO2TGM
        if urls == []:
            print("the list is empty")
            sys.exit(1)
        print("VK urls \t" + str(urls))
        URL = "https://"+urls[0]
        page = requests.get(URL)
        pageText = page.text
        #urls = re.findall('(psv\\d.userapi.com.*.pdf)', pageText)
        urls = re.findall('([a-z]{3}\\d+.*.userapi.com.*.pdf)', pageText)
        
        if urls == []:
            #print("psv4.userapi.com url is not present")
            #print("trying sun6-21.userapi.com")
            #urls = re.findall('(sun\\d\\-\\d{2}.userapi.com.*.pdf)', pageText)
            print("No url to download. exiting ....")
        URL= "https://"+urls[0].replace("\\","")
        r = requests.get(URL, stream=True)
        chunk_size=256000
        if int(dailyDate) < 10:
            dailyDate="0"+dailyDate
        fileName=dailyYear+dailyMonth+dailyDate+".pdf"
        month=getMonthCode(dailyMonth)
        if int(dailyDate) < 10:
            dailyDate="0"+dailyDate
        with open(fileName, 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)
        if dailyPaper=="ft":
            command='mv ' + fileName +' '+ path+ 'FinancialTimes/' + dailyYear + "/" + month + "/"
            os.system(command)
            print("Moved file to " + path+ 'FinancialTimes/' + dailyYear + "/"+ month +"/")
        if dailyPaper=="ftwk":
            command='mv ' + fileName +' '+ path+ 'FinancialTimes/' + dailyYear + "/" +month+ "/"
            os.system(command)
            print("Moved file to " + path+ 'FinancialTimes/' + dailyYear + "/"+ month+"/")
        if dailyPaper=="tt":
            command='mv ' + fileName +' '+ path+ 'Times/' + dailyYear + "/" + month+"/"
            os.system(command)
            print("Moved file to " + path+ 'Times/' + dailyYear + "/"+ month +"/")
        if dailyPaper=="wsj":
            command='mv ' + fileName +' '+ path+ 'WallStreetJournal/' + dailyYear + "/" + month+"/"
            os.system(command)
            print("Moved file to " + path+ 'WallStreetJournal/' + dailyYear + "/"+ month +"/")
        if dailyPaper=="mw":
            command='mv ' + fileName +' '+ path+ 'MoneyWeek/' + dailyYear + "/" + month+"/"
            os.system(command)
            print("Moved file to " + path+ 'WallStreetJournal/' + dailyYear + "/"+ month +"/")





sys.exit(1)

