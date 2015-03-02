from bs4 import BeautifulSoup
import re
import MySQLdb
import datetime
import urllib2

def FuckStick(title,arrayz):
    print title
    print "============================"
    for item in arrayz:
        print item.contents[1].renderContents(),
        print "  ",
        print item.contents[3].renderContents().translate(None,'(,)')      
    print ""

def CuntStick(title,arrayz):
    print title
    print "============================"
    for item in arrayz:
        print item.contents[1].renderContents(),
        print "  ",
        print item.contents[1].renderContents(),
        print "  ",
        print item.contents[3].renderContents().translate(None,'(,)')      
    print ""

    
def CuntUp(dbCur,table,data,timey):
    for item in data:
        sql = "INSERT INTO `" + table + "` (`data`, `count`, `date`) VALUES ('" + item.contents[1].renderContents()  + "', " + item.contents[3].renderContents().translate(None,'(,)') + ", '" + timey + "');"
        cur.execute(sql)
		
		
def FuckUp(dbCur,table,data,timey):
	for item in data:
		sql = "INSERT INTO `data-table` (`dimension`,`data`, `count`, `date`) VALUES (`" + table + "`, " + item.contents[1].renderContents() + "', " + item.contents[3].renderContents().translate(None,'(,)') + ", '" + timey + "');"
		cur.execute(sql)

        
timex = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        
print "Get Page",
url = 'http://www.carsales.com.au/cars/results?silo=stock&q=(Service%3d%5bCarsales%5d)&vertical=car&WT.z_srchsrcx=makemodel&sortby=TopDeal&cpw=1'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
data = opener.open(url)
print "\tOK"

## Uncomment to open a local file        
# f = open('carz.html',"r")
# data = f.read()

print "Parsing",
soup = BeautifulSoup(data)

titleTag = soup.html.head.title

make = soup.find('div', { "data-name" : "Make" })
makeAll = make.findAll('li',{"class":" more"})

state = soup.find('div', { "data-name" : "State" })
stateAll = state.findAll('li')

manufprog = soup.find('div', { "data-name" : "Manufacturer Program" })
manufprogAll = manufprog.findAll('li')

body = soup.find('div', { "data-name" : "Body Style" })
bodyAll = body.findAll('li', {"class":" less"})

gear = soup.find('div', { "data-name" : "Gear Type" })
gearAll = gear.findAll('li', {"class":"last-item less"})
gearAll = [gearAll[0],gear.findAll('li', {"class":" less"})[0]]

colour = soup.find('div', { "data-name" : "Colour" })
colourAll = colour.findAll('li',{"class" : " more"})

fuel = soup.find('div', { "data-name" : "Fuel Type" })
fuelAll = fuel.findAll('li')

fuelEco = soup.find('div', { "data-name" : "Fuel Economy" })
fuelEcoAll = fuelEco.findAll('li')

drive = soup.find('div', { "data-name" : "Drive" })
driveAll = drive.findAll('li')

lifestyles = soup.find('div', { "data-name" : "Lifestyles" })
lifestylesAll = lifestyles.findAll('li')

doors = soup.find('div', { "data-name" : "Doors" })
doorsAll = doors.findAll('li')

cylinders = soup.find('div', { "data-name" : "Cylinders" })
cylindersAll = cylinders.findAll('li')

engine = soup.find('div', { "data-name" : "Engine Type" })
engineAll = engine.findAll('li')

induction = soup.find('div', { "data-name" : "Induction" })
inductionAll = induction.findAll('li')

ancap = soup.find('div', { "data-name" : "ANCAP Rating" })
ancapAll = ancap.findAll('li')

greenStar = soup.find('div', { "data-name" : "GreenStar Rating"})
greenStarAll = greenStar.findAll('li')

pPlate = soup.find('div', { "data-name" : "P-Plate Approved State"})
pPlateAll =  pPlate.findAll('li')

adsWith = soup.find('div', { "data-name" : "AdsWith"})
adsWithAll =  adsWith.findAll('li')
print "\tOK"


print "SQL Write",

# Open database connection
server      = "localhost"
user        = "root"
password    = "password"
database    = "cactus"

db = MySQLdb.connect(server,user,password,database )
cur = db.cursor()

# FuckUp(cur,'data-table',makeAll,timex)


# CuntUp(cur,'make',makeAll,timex)
# CuntUp(cur,'state',stateAll,timex)
# CuntUp(cur,'manufprog',manufprogAll,timex)
# CuntUp(cur,'body',bodyAll,timex)
# CuntUp(cur,'gear',gearAll,timex)
# CuntUp(cur,'colour',colourAll,timex)
# CuntUp(cur,'fuel',fuelAll,timex)
# CuntUp(cur,'fuelEco',fuelEcoAll,timex)
# CuntUp(cur,'drive',driveAll,timex)
# CuntUp(cur,'lifestyle',lifestylesAll,timex)
# CuntUp(cur,'doors',doorsAll,timex)
# CuntUp(cur,'cylinders',cylindersAll,timex)
# CuntUp(cur,'engine',engineAll,timex)
# CuntUp(cur,'induction',inductionAll,timex)
# CuntUp(cur,'ancap',ancapAll,timex)
# CuntUp(cur,'greenStar',greenStarAll,timex)
# CuntUp(cur,'pplate',pPlateAll,timex)
# CuntUp(cur,'adswith',adsWithAll,timex)
# Sax's version



sql = "INSERT INTO `executions` (`date`) VALUES ('" + timex + "');"
cur.execute(sql)

print "\tOK"

# commit & disconnect from server
db.commit()
db.close()


# FuckStick('Make',makeAll)
FuckStick('State',stateAll)
# FuckStick("Manufacturer Program", manufprogAll)  
# FuckStick("Body Style",bodyAll)    
# FuckStick("Gear Type",gearAll)
# FuckStick("Colour",colourAll)
# FuckStick("Fuel",fuelAll)
# FuckStick("Fuel Economy",fuelEcoAll)
# FuckStick("Drive",driveAll)
# FuckStick("Lifestyle",lifestylesAll)
# FuckStick("Doors",doorsAll)
# FuckStick("Cylinders",cylindersAll)
# FuckStick("Engine Type",engineAll)
# FuckStick("Induction",inductionAll)
# FuckStick("ANCAP",ancapAll)
# FuckStick("Green Star",greenStarAll)
# FuckStick("P Plate State",pPlateAll)
# FuckStick("Ads With",adsWithAll)

# print stateAll

CuntStick('State',stateAll)

FuckUp (cur,'state',stateAll,timex)


print ""
print "That's All Yolks !"
