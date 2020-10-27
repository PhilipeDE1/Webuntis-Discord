import discord
import webuntis
import datetime
import time
import json

def checkUpdates():
    if s.last_import_time() > lastUpdate:


s = webuntis.Session(
    server='borys.webuntis.com',
    username='E1FI1',
    password='fkS2QXzbyL',
    school='BSZ-Bibi',
    useragent='WebUntis Test')

s.login()

klassendict = {}
raeumedict  = {}
subjectdict = {}
teacherdict = {}
data = {"klassen": klassendict, "raeume": raeumedict, "subjects": subjectdict, "teachers": teacherdict}

lastUpdate = s.last_import_time()

#Muss wegen Herbstferien noch geändert werden!!
today = datetime.date.today()
monday = today + datetime.timedelta(days=6)
friday = monday + datetime.timedelta(days=4)

e1fi1 = s.klassen().filter(id=558) [0]
#print(s.timetable(klasse=e1fi1, start=monday, end=friday))
#print("Test")


for k in s.klassen():
    klassendict[str(k)] = int(k.id)

for r in s.rooms():
    raeumedict[str(r)] = int(r.id)

for t in s.teachers():
    teacherdict[str(t)] = int(t.id)

for sub in s.subjects():
    subjectdict[str(sub)] = int(sub.id)

with open("IDs.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

while True:
    if datetime.datetime.now().minute % 2 == 0: 
        print("tick")
        #do algorithm
    time.sleep(60)

s.logout()


