'''A module for the CategoriesList class.'''

import sqlite3
import os

# added by Daniel
def to_dict(item):
    '''Converts a tuple to a dictionary.'''
    categories = {'rowid': item[0], 'categories_name': item[1]}
    return categories

# added by Daniel
class CategoriesList:
    # added by Daniel
    '''A class representing a list of categories.'''
    def __init__(self):
        '''Initializes the CategoriesList object.'''
        self.run_query('''CREATE TABLE IF NOT EXISTS categories (categories_name text)''',())

    # added by Daniel
    def select_all(self):
        '''Returns all rows from the categories table as a list of dictionaries.'''
        return self.run_query("SELECT rowid,* from categories",())

    # added by Daniel
    def add(self, item):
        '''Inserts a new row into the categories table.'''
        return self.run_query("INSERT INTO categories VALUES(?)", (item['categories_name'],))

    # added by Veronika
    def modify(self, item_name, category_name):
        '''Modifies a row in the categories table.'''
        return self.run_query("UPDATE categories SET categories_name=(?) WHERE categories_name=(?)",
                             (category_name, item_name))

    # added by Daniel
    def run_query(self, query, ntuple):
        '''Executes a SQL query and returns the result as a list of dictionaries.'''
        con = sqlite3.connect(os.getenv("HOME")+'/categories.db')
        cur = con.cursor()
        cur.execute(query, ntuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
