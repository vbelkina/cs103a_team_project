'''
simple demo of fixtures for Python program with pytest
use to test the TodoList class 

added by Veronika
'''

import pytest
import sqlite3
from transaction import trackerList

def to_dict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    tracker = {'rowid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return tracker

def tuples_to_dicts(ts):
    return [to_dict(t) for t in ts]

@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [("100", "test1", "2018-01-01", "test1"), 
            ("100", "test2", "2018-01-01", "test2")
           ]

@pytest.fixture
def returned_tuples(tuples):
    " add a rowid to the beginning of each tuple "
    return [(i+1,)+tuples[i] for i in range(len(tuples))]

@pytest.fixture
def returned_dicts(tuples):
    " add a rowid to the beginning of each tuple "
    return tuples_to_dicts([(i+1,)+tuples[i] for i in range(len(tuples))])

@pytest.fixture
def tracker_path(tmp_path):
    yield tmp_path / 'tracker.db'

@pytest.fixture(autouse=True)
def transactions(tracker_path,tuples):
    "create and initialize the todo.db database in /tmp "
    con= sqlite3.connect(tracker_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tracker
                    (amount text, category text, date text, description text)''')
    for i in range(len(tuples)):
        cur.execute('''insert into tracker values(?,?,?,?)''',tuples[i])
    # create the todolist database
    con.commit()
    td = trackerList(tracker_path)
    yield td
    cur.execute('''drop table tracker''')
    con.commit()

def test_selectAll(transactions,returned_dicts):
    ''' test the selectAll method'''
    td = transactions
    results = td.selectAll()
    expected = returned_dicts
    assert results == expected

def test_add(transactions,returned_dicts):
    ''' test the add method'''
    td = transactions
    td.add({'amount':'100','category':'test3','date':'2018-01-01','description':'test3'})
    results = td.selectAll()
    expected = returned_dicts
    expected.append({'rowid':3,'amount':'100','category':'test3','date':'2018-01-01','description':'test3'})
    assert results == expected

def test_delete(transactions,returned_dicts):
    ''' test the delete method'''
    td = transactions
    td.delete(1)
    results = td.selectAll()
    expected = returned_dicts
    expected.pop(0)
    assert results == expected