"""A module for the Transaction class."""


import sqlite3
#import os

def to_dict(tup):
    """Converts a tuple to a dictionary."""
    print('t='+str(tup))
    tracker = {'rowid':tup[0], 'amount':tup[1], 'category':tup[2],
               'date':tup[3], 'description':tup[4]}
    return tracker

class TrackerList():
    """A class representing a list of transactions."""

    def __init__(self, db_path):
        self.db_path=db_path
        self.run_query('''CREATE TABLE IF NOT EXISTS tracker
                    (amount text, category text, date text, description text)''',())

    def select_all(self):
        """Return all of the transactions as a list of dicts."""
        return self.run_query("SELECT rowid,* from tracker",())

    def add(self,item):
        """Add a new transaction to the list."""
        return self.run_query("INSERT INTO tracker VALUES(?,?,?,?)",
                             (item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        """Delete a transaction from the list."""
        return self.run_query("DELETE FROM tracker WHERE rowid=(?)",(rowid,))

    def select_by_category(self,category):
        """Selects all transactions of the given category."""
        return self.run_query("SELECT rowid,* FROM tracker WHERE category=(?)",(category,))

    def select_by_year(self,year):
        """Selects all transactions in the given year."""
        return self.run_query("SELECT rowid,* FROM tracker WHERE date LIKE (?)",(year+'%',))

    def select_by_month(self,month):
        """Selects all transactions in the given month."""
        return self.run_query("SELECT rowid,* FROM tracker WHERE date LIKE (?)",(month+'%',))

    def select_by_date(self,date):
        """Selects all transactions on the given date."""
        return self.run_query("SELECT rowid,* FROM tracker WHERE date=(?)",(date,))

    def run_query(self,query,ntuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute(query,ntuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
