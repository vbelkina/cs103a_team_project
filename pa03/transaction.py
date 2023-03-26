import sqlite3
#import os

def toDict(t):
    print('t='+str(t))
    tracker = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker

class trackerList():
    def __init__(self, db_path):
        self.db_path=db_path
        self.runQuery('''CREATE TABLE IF NOT EXISTS tracker
                    (amount text, category text, date text, description text)''',())
    
    def selectAll(self):
        return self.runQuery("SELECT rowid,* from tracker",())

    def add(self,item):
        return self.runQuery("INSERT INTO tracker VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        return self.runQuery("DELETE FROM tracker WHERE rowid=(?)",(rowid,))

    def selectByCategory(self,category):
        return self.runQuery("SELECT rowid,* FROM tracker WHERE category=(?)",(category,))
    
    def selectByYear(self,year):
        return self.runQuery("SELECT rowid,* FROM tracker WHERE date LIKE (?)",(year+'%',))
    
    def selectByMonth(self,month):
        return self.runQuery("SELECT rowid,* FROM tracker WHERE date LIKE (?)",(month+'%',))
    
    def selectByDate(self,date):
        return self.runQuery("SELECT rowid,* FROM tracker WHERE date=(?)",(date+'%',))

    def runQuery(self,query,ntuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(self.db_path)
        cur = con.cursor() 
        cur.execute(query,ntuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

    
        
