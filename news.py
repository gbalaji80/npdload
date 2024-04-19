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

configFile="config.csv"
path="/home/balaji/Documents/googleDrive/news/"

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
        URL = "https://freemagazines.top/financial-times-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        #URL = "https://freemagazines.top/financial-times-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        #URL = "https://freemagazinespdf.com/financial-times-uk-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL 
    elif dailyPaper == "tt":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazinespdf.com/the-times-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        URL =  "https://freemagazines.top/the-times-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        #URL =  "https://freemagazines.top/the-times-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"

        return URL
    elif dailyPaper == "ftwk":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazinespdf.com/financial-times-weekend-uk-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        URL = "https://freemagazines.top/financial-times-weekend-uk-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "wsj":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazinespdf.com/the-wall-street-journal-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        #URL = "https://freemagazines.top/the-wall-street-journal-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        URL = "https://freemagazines.top/the-wall-street-journal-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "wp":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazinespdf.com/the-washington-post-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        URL = "https://freemagazines.top/the-washington-post-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "gm":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = "https://freemagazinespdf.com/The_Globe_and_Mail-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "eco":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazinespdf.com/the-economist-usa-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        URL = "https://freemagazines.top/the-economist-usa-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "tg":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazines.top/the-guardian-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"-free-pdf-download/"
        URL = "https://freemagazines.top/the-guardian-" + dailyDate + "-" + dailyMonth + "-" + dailyYear+"/"
        return URL
    elif dailyPaper == "br":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazinespdf.com/barrons-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        URL = "https://freemagazines.top/barrons-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "brm":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        URL = "https://freemagazines.top/barrons-magazine-"+dailyMonth+"-"+dailyDate+"-"+dailyYear+"/"
        return URL
    elif dailyPaper == "mw":
        dailyMonth = getMonth(dailyMonth)
        dailyDate = getDate(dailyPaper,dailyDate)
        #URL = "https://freemagazinespdf.com/moneyweek-issue-"+mwIssueNumber+"-"+dailyDate+"-"+dailyMonth+"-"+dailyYear+"/"
        URL = "https://freemagazines.top/moneyweek-issue-"+mwIssueNumber+"-"+dailyDate+"-" + dailyMonth  + "-" + dailyYear +"/"
        return URL 
    
with open(configFile, newline='') as csvfile:
    valuesExtracted = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for line in valuesExtracted:
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
        urls = re.findall('https?://(vk.com/doc[\\d]+_\\d+)', pageText)
        #urls = re.findall('(vk.com/doc[0-9].*_\d+)', pageText)
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
        chunk_size=2000
        fileName=dailyYear+dailyMonth+dailyDate+".pdf"
        month=getMonthCode(dailyMonth)
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




sys.exit(1)

