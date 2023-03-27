import sqlite3
import os

def to_dict(t):
    '''Converts a tuple to a dictionary.'''
    categories = {'rowid': t[0], 'categories_name': t[1]}
    return categories

class CategoriesList:
    '''A class representing a list of categories.'''
    def __init__(self):
        '''Initializes the CategoriesList object.'''
        self.run_query('''CREATE TABLE IF NOT EXISTS categories (categories_name text)''',())

    def selectAll(self):
        '''Returns all rows from the categories table as a list of dictionaries.'''
        return self.run_query("SELECT rowid,* from categories",())

    def add(self, item):
        '''Inserts a new row into the categories table.'''
        return self.run_query("INSERT INTO categories VALUES(?)", (item['categories_name'],))

<<<<<<< HEAD
    # added by Veronika
    def modify(self, item_name, category_name):
        return self.runQuery("UPDATE categories SET categories_name=(?) WHERE categories_name=(?)",(category_name, item_name))
=======
    def modify(self, item):
        '''Modifies an existing row in the categories table.'''
        return self.run_query("UPDATE categories SET categories_name=(?) WHERE rowid=(?)", 
                              (item['categories_name'], item['rowid']))
>>>>>>> 340c188cee37956cf84847b9a63181acdf6aeb1e

    def run_query(self, query, ntuple):
        '''Executes a SQL query and returns the result as a list of dictionaries.'''
        con = sqlite3.connect(os.getenv("HOME")+'/categories.db')
        cur = con.cursor()
        cur.execute(query, ntuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
