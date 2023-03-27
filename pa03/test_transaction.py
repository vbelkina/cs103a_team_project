'''
simple demo of fixtures for Python program with pytest
use to test the TrackerList class
added by Veronika
'''

import sqlite3
import pytest
from transaction import TrackerList

def to_dict(item):
    ''' t is a tuple (rowid,title, desc,completed)'''
    tracker = {'rowid':item[0], 'amount':item[1],
               'category':item[2], 'date':item[3], 'description':item[4]}
    return tracker

def tuples_to_dicts(tups):
    ''' ts is a list of tuples'''
    return [to_dict(t) for t in tups]

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
    '''creates the path to the database to be tracked'''
    yield tmp_path / 'tracker.db'

@pytest.fixture(autouse=True)
def transactions(tracker_path, tuples):
    "create and initialize the todo.db database in /tmp "
    con = sqlite3.connect(tracker_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tracker
                    (amount text, category text, date text, description text)''')
    for i in range(len(tuples)):
        cur.execute('''insert into tracker values(?,?,?,?)''', tuples[i])
    # create the todolist database
    con.commit()
    tracker = TrackerList(tracker_path)
    yield tracker
    cur.execute('''drop table tracker''')
    con.commit()

def test_select_all(transactions, returned_dicts):
    ''' test the selectAll method'''
    tracker = transactions
    results = tracker.select_all()
    expected = returned_dicts
    assert results == expected

def test_add(transactions, returned_dicts):
    ''' test the add method'''
    tracker = transactions
    tracker.add({'amount':'100', 'category':'test3', 'date':'2018-01-01', 'description':'test3'})
    results = tracker.select_all()
    expected = returned_dicts
    expected.append({'rowid':3, 'amount':'100', 'category':'test3',
                     'date':'2018-01-01', 'description':'test3'})
    assert results == expected

def test_delete(transactions, returned_dicts):
    ''' test the delete method'''
    tracker = transactions
    tracker.delete(1)
    results = tracker.select_all()
    expected = returned_dicts
    expected.pop(0)
    assert results == expected

#Written by Kevin
def test_select_by_category(transactions, returned_dicts):
    ''' test the selectByCategory method'''
    tracker = transactions
    results = tracker.select_by_category('test1')
    expected = returned_dicts
    expected.pop(1)
    assert results == expected

#Written by Kevin
def test_select_by_year(transactions, returned_dicts):
    ''' test the selectByYear method'''
    tracker = transactions
    results = tracker.select_by_year('2018')
    expected = returned_dicts
    assert results == expected

#Written by Kevin
def test_select_by_month(transactions, returned_dicts):
    ''' test the selectByMonth method'''
    tracker = transactions
    results = tracker.select_by_month('2018-01')
    expected = returned_dicts
    assert results == expected

#Written by Kevin
def test_select_by_date(transactions, returned_dicts):
    ''' test the selectByDay method'''
    tracker = transactions
    results = tracker.select_by_date('2018-01-01')
    expected = returned_dicts
    assert results == expected
