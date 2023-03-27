'''Allows user to see summaries of transactions, and add, delete, or modify existing transactions'''
import sys
import os
from transaction import TrackerList
from category import CategoriesList

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            type quit (description: to end the program)
            type showall_categories (description: show all categories)
            type add_category (description: to add a new category)
            type modify_category (description: to modify a category)
            type showall_transactions (description: for all transactions)
            type add_transaction amount category date description (description: to add a new transaction)
            type delete_transaction item# (description: to delete a new transaction)
            type sum_transactions_date date (description: summarizes transactions on the given date in the format yyyy-mm-dd)
            type sum_transactions_month month (description: summarizes transactions in the given month in the format yyyy-mm)
            type sum_transactions_year year (description: summarizes transactions in the given year in the format yyyy)
            type sum_transactions_category category (description: summarizes transactions of the given category)
            type print_usage (description: to print this message)
            ''')
    
# added by Daniel
def print_transactions(todos):
    ''' prints a list of all of the transactions '''
    if len(todos) == 0:
        print('no transactions to print')
        return
    print('\n')
    print("%-30s %-30s %-30s %-30s %-30s"%('item #', 'amount', 'category', 'date', 'description'))
    print('-'*150)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-30s %-30s %-30s %-30s %-30s"%values)
        
# added by Daniel
def print_categories(todos):
    ''' prints a list of each category of transaction in the given database'''
    if len(todos) == 0:
        print('no categories to print')
        return
    print('\n')
    print("%-30s %-30s"%('item #', 'category',))
    print('-'*50)
    for item in todos:
        values = tuple(item.values()) #(rowid,category)
        print("%-30s %-30s "%values)
#written by Ian
def delete_transaction(tracker, rowid):
    """Deletes a transaction from the list."""
    tracker.delete(rowid)
#written by Kevin
def sum_transactions(transactions):
    '''summarizes total # and amounts of transactions'''
    if len(transactions) == 0:
        print('no transactions')
        return
    print('\n')
    print('-'*50)
    total = 0
    count = 0
    for item in transactions:
        total += int(item['amount'])
        count += 1
    print("Total amount for all transactions: ", total)
    print('\n')
    print('Total number of transactions: ', count)

# added by Daniel
def process_args(arglist):
    ''' processes the users arguments and runs the proper function '''
    track_list = TrackerList(os.path.join(os.environ['HOME'], 'tracker.db'))
    category_list = CategoriesList()
    if arglist == []:
        print_usage()
    # added by Daniel
    elif arglist[0] == "showall_transactions":
        print_transactions(todos=track_list.select_all())
    # added by Daniel
    elif arglist[0] == "showall_categories":
        print_categories(todos=category_list.select_all())
    
    # added by Daniel
    elif arglist[0] == 'add_transaction':
        # Here I want to check if the inputed category is inside category db.
        # if yes then we continue else we put it into the db.
        category_inputed = arglist[2]
        exists = False
        for item in category_list.select_all():
            values = tuple(item.values()) #(rowid,category)
            if values[1] == category_inputed:
                exists = True
                break

        if not exists:
            temp_args = ['add_category', category_inputed]
            category_list.add({'categories_name':temp_args[1]})

        # Check is over
        todo = {'amount':arglist[1], 'category':arglist[2], 'date':arglist[3], 'description':arglist[4]}
        track_list.add(todo)
    # added by Daniel
    elif arglist[0] == 'add_category':
        category_list.add({'categories_name':arglist[1]})
    # added by Daniel
    elif arglist[0] == 'modify_category':
        print(arglist[1], arglist[2])
        category_list.modify(arglist[1], arglist[2])

    elif arglist[0] == 'delete_transaction':
        delete_transaction(track_list, arglist[1])

    elif arglist[0] == 'sum_transactions_date':
        sum_transactions(transactions=track_list.select_by_date(arglist[1]))

    elif arglist[0] == 'sum_transactions_month':
        sum_transactions(transactions=track_list.select_by_month(arglist[1]))

    elif arglist[0] == 'sum_transactions_year':
        sum_transactions(transactions=track_list.select_by_year(arglist[1]))

    elif arglist[0] == 'sum_transactions_category':
        sum_transactions(transactions=track_list.select_by_category(arglist[1]))

    else:
        print(arglist, " is not implemented")
        print_usage()

def toplevel():
    ''' takes user input, splits into args for other functions'''
    if len(sys.argv) == 1:
        print_usage()
        args = []
        while args != ['']:
            args = input("command> ").split(' ')
            if args[0] == 'quit':
                break

            elif args[0] == 'add_transaction':
                args = ['add_transaction', args[1], args[2], args[3], args[4]]

            elif args[0] == 'add_category':
                args = ['add_category', args[1]]

            elif args[0] == 'delete_transaction':
                args = ['delete_transaction', args[1]]

            elif args[0] == 'sum_transactions_date':
                args = ['sum_transactions_date', args[1]]

            elif args[0] == 'sum_transactions_month':
                args = ['sum_transactions_month', args[1]]

            elif args[0] == 'sum_transactions_year':
                args = ['sum_transactions_year', args[1]]

            elif args[0] == 'sum_transactions_category':
                args = ['sum_transactions_category', args[1]]

            process_args(args)
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

toplevel()
