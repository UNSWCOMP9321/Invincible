import sqlite3
import os
import operator


dbpath = os.getcwd()+os.path.sep+"database"+os.path.sep+"COMP9313_Ass3.db"
conn = sqlite3.connect(dbpath,check_same_thread=False)

cu=conn.cursor()

#{location: {'city1':[x,y], 'city2':[x,y],...}, data:[{name: 'city1', value:233}, {name: 'city2', value:500}]}
def get_CITY_AU(city_name="all",limit=15):
    if city_name=="all":
        cu.execute("select * from CITY_AU ORDER BY job_amount DESC limit "+str(limit))
    else:
        cu.execute(f'select * from CITY_AU where LOWER(city) = \'{city_name.lower()}\'')
    loc_dic={}
    data=[]
    for c in cu.fetchall():
        loc_dic[c[0]]=(c[2],c[1])
        data.append({"name":c[0],"value":c[3]})
    return {"location":loc_dic,"data":data}


def get_CITY_UK(city_name="all",limit=15):
    if city_name=="all":
        cu.execute("select * from CITY_UK ORDER BY job_amount DESC limit "+str(limit))
    else:
        cu.execute(f'select * from CITY_UK where LOWER(city) = \'{city_name.lower()}\'')
    loc_dic={}
    data=[]
    for c in cu.fetchall():
        loc_dic[c[0]]=(c[2],c[1])
        data.append({"name":c[0],"value":c[3]})
    return {"location":loc_dic,"data":data}

def get_CATE_AU():
    cu.execute("select category,job_amount from CATE_AU")
    data = []
    for c in cu.fetchall():
        data.append([c[0], c[1]])
    data.sort(key=takeSecond)
    data.reverse()
    return {"Data": data}

def get_CATE_UK():
    cu.execute("select category,job_amount from CATE_UK")
    data=[]
    for c in cu.fetchall():
        data.append([c[0],c[1]])
    data.sort(key=takeSecond)
    data.reverse()
    return {"Data":data}

#{"category":[],"male_au":[],"female_au":[],"male_uk":[],"female_uk":[]}

def get_WORK_HOURS():
    cu.execute("select * from WORK_HOURS where sex != 'Total'")
    data=[]
    for c in cu.fetchall():
        data.append(c)
    data = sorted(data, key = lambda item:item[2])
    category=[]
    male_au=[]
    female_au=[]
    male_uk=[]
    female_uk=[]
    for t in data:
        if t[2] not in category:
            category.append(t[2])
        if t[0] == "AU":
            if t[1] == "Female":
                female_au.append(-t[3])
            else:
                male_au.append(-t[3])
        else:
            if t[1] == "Female":
                female_uk.append(t[3])
            else:
                male_uk.append(t[3])
    return {"category":category,"male_au":male_au,"female_au":female_au,"male_uk":male_uk,"female_uk":female_uk}

def retrive_CITY_AU(name):
    select_query = "SELECT city FROM CITY_AU"
    city_au = []
    choosen_city = []
    for row in cu.execute(select_query).fetchall():
        city_au.append(row[0])
    x = len(name)
    name = name[0].upper() + name[1:].lower()
    for i in city_au:
        if i[0:x] == name:
            choosen_city.append(i)
        if len(choosen_city)>5:
            break
    return {"City":choosen_city}

def retrive_CITY_UK(name):
    select_query = "SELECT city FROM CITY_UK"
    city_uk = []
    choosen_city = []
    for row in cu.execute(select_query).fetchall():
        city_uk.append(row[0])
    x = len(name)
    name = name[0].upper() + name[1:].lower()
    for i in city_uk:
        if i[0:x] == name:
            choosen_city.append(i)
        if len(choosen_city)>5:
            break
    return {"City":choosen_city}

def takeSecond(elem):
    return elem[1]

def information_au(name):

    select_query = "SELECT city,category FROM job_au"
    city_au = []

    for row in cu.execute(select_query).fetchall():
        if row[0].lower() == name.lower():
            city_au.append(row[1])
    myset = set(city_au)
    au_city = []
    for item in myset:
        au_city.append([item,city_au.count(item)])
    au_city.sort(key=takeSecond)
    au_city.reverse()
    return {"Data":au_city}

def information_uk(name):
    select_query = "SELECT city,category FROM job_uk"
    city_uk = []
    for row in cu.execute(select_query).fetchall():
        if row[0].lower() == name.lower():
            city_uk.append(row[1])
    myset = set(city_uk)
    uk_city = []
    for item in myset:
        uk_city.append([item,city_uk.count(item)])
    uk_city.sort(key=takeSecond)
    uk_city.reverse()
    return {"Data":uk_city}


