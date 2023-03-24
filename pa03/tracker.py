from transaction import trackerList
from category import categoriesList
import sys

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            type quit (description: to end the program)
            type showall_categories (description: show all categories)
            type add_category (description: to add a new category)
            type showall_transactions(description: for all transactions)
            type add_transaction amount category date description (description: to add a new transaction)
            '''
            )

def print_transactions(todos):
    if len(todos)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-30s %-30s %-30s %-30s %-30s"%('item #', 'amount', 'category', 'date', 'description'))
    print('-'*150)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-30s %-30s %-30s %-30s %-30s"%values)

def print_categories(todos):
    if len(todos)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-30s %-30s"%('item #', 'category',))
    print('-'*50)
    for item in todos:
        values = tuple(item.values()) #(rowid,category)
        print("%-30s %-30s "%values)

def process_args(arglist):
    track_list = trackerList()
    category_list = categoriesList()
    if arglist==[]:
        print_usage()
        
    elif arglist[0]=="showall_transactions":
        print_transactions(todos = track_list.selectAll())

    elif arglist[0]=="showall_categories":
        print_categories(todos = category_list.selectAll())

    elif arglist[0]=='add_transaction':
        # Here I want to check if the inputed category is inside category db. if yes then we continue else we put it into the db.
        category_inputed = arglist[2]
        exists = False
        for item in category_list.selectAll():
            values = tuple(item.values()) #(rowid,category)
            if values[1] == category_inputed:
                exists = True
                break
        
        if exists == False:
            temp_args = ['add_category', category_inputed]
            category_list.add({'categories_name':temp_args[1]})

        # Check is over

        todo = {'amount':arglist[1],'category':arglist[2], 'date':arglist[3], 'description':arglist[4]}
        track_list.add(todo)

    elif arglist[0]=='add_category':
        category_list.add({'categories_name':arglist[1]})

    else:
        print(arglist,"is not implemented")
        print_usage()


def toplevel():
    if len(sys.argv)==1:
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='quit':
                break

            elif args[0]=='add_transaction':
                args = ['add_transaction', args[1], args[2], args[3], args[4]]

            elif args[0]=='add_category':
                args = ['add_category', args[1]]

            process_args(args)
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()
