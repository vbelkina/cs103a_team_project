from transaction import trackerList
import sys

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            type quit (description: to end the program)
            type showall (description: for all transactions)
            type add amount category date description (description: to add a new transaction)
            '''
            )

def print_todos(todos):
    if len(todos)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-30s %-30s %-30s %-30s %-30s"%('item #', 'amount', 'category', 'date', 'description'))
    print('-'*150)
    for item in todos:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-30s %-30s %-30s %-30s %-30s"%values)

def process_args(arglist):
    todolist = trackerList()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="showall":
        print_todos(todos = todolist.selectAll())
    elif arglist[0]=='add':
            todo = {'amount':arglist[1],'category':arglist[2], 'date':arglist[3], 'description':arglist[4]}
            todolist.add(todo)
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
            if args[0]=='add':
                args = ['add', args[1], args[2], args[3], args[4]]
            process_args(args)
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()
