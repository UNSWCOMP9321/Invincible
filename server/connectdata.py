import sqlite3
conn = sqlite3.connect('.\database\COMP9313_Ass3.db',check_same_thread=False)

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
