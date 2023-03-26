import sqlite3
import os

def toDict(t):
    print('t='+str(t))
    categories = {'rowid':t[0], 'categories_name':t[1]}
    return categories

class categoriesList():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS categories (categories_name text)''',())
    
    def selectAll(self):
        return self.runQuery("SELECT rowid,* from categories",())

    def add(self,item):
        return self.runQuery("INSERT INTO categories VALUES(?)",(item['categories_name'],))

    # added by Veronika
    def modify(self,item):
        return self.runQuery("UPDATE categories SET categories_name=(?) WHERE rowid=(?)",(item['categories_name'],item['rowid']))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv("HOME")+'/categories.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

    
        
