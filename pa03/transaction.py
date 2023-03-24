import sqlite3
import os

def toDict(t):
    print('t='+str(t))
    tracker = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker

class trackerList():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS tracker
                    (amount text, category text, date text, description text)''',())
    
    def selectAll(self):
        return self.runQuery("SELECT rowid,* from tracker",())

    def add(self,item):
        return self.runQuery("INSERT INTO tracker VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        return self.runQuery("DELETE FROM tracker WHERE rowid=(?)",(rowid,))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

    
        
