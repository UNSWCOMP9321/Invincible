import sqlite3
import os

dbpath = os.getcwd()+os.path.sep+"database"+os.path.sep+"COMP9313_Ass3.db"
conn = sqlite3.connect(dbpath,check_same_thread=False)

cu=conn.cursor()

#{location: {'city1':[x,y], 'city2':[x,y],...}, data:[{name: 'city1', value:233}, {name: 'city2', value:500}]}
def get_CITY_AU():
    cu.execute("select * from CITY_AU")
    loc_dic={}
    data=[]
    for c in cu.fetchall():

        loc_dic[c[0]]=(c[1],c[2])

        data.append({"name":c[0],"value":c[3]})

    return {"location":loc_dic,"data":data}

def retrive_CITY_AU(name):
    select_query = "SELECT city FROM CITY_AU"
    city_au = []
    choosen_city = []
    for row in cu.execute(select_query).fetchall():
        city_au.append(row[0])
    x = len(name)
    name = name[0].upper() + name[1:]
    for i in city_au:
        if i[0:x] == name:
            choosen_city.append(i)
        if len(choosen_city)>5:
            break
    return {"City":choosen_city}

retrive_CITY_AU("a")




