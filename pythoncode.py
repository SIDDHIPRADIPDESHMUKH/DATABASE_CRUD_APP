import pymysql as p #This is to establish connection of python file with SQL database

def getconnect(): #This function will connect our python code with SQL
    return p.connect(host='localhost', user='root',password='',database='CRUD')


def addrec(rec):   #This function is created to insert record in table 
    db=getconnect()  #get connection of database and save it in variable db
    cr=db.cursor()  #here we call cursor function to perform queries on table
    sql='insert into students values (%s,%s,%s,%s)' #this will insert records in table sequencialy in place of %s
    cr.execute(sql,rec) #execute sql query
    db.commit()    #commits inserted records in data base
    db.close()
    print('Record inserted successfully...')

def readAll(): #To display all records 
    db=getconnect()
    cr=db.cursor()
    sql='select * from students'
    cr.execute(sql)
    stud=cr.fetchall()
    a,b,c,d='ID','NAME','ADDRESS','CONTACT'
    print(f'\n{a:^5} {b:^20} {c:^30} {d:^10}\n') #this will print column names in organised manner
    for i,n,a,c in stud:
        print(f'{i:^5} {n:^20} {a:^30} {c:^10}\n')
    db.commit()
    db.close()
    

def deleterow(ID):
    db=getconnect()
    cr=db.cursor()
    sql='delete from students where ID=%s'
    cr.execute(sql,ID)
    db.commit()
    db.close()
    print('Record deleted.')

def updaterec(rec):
    db=getconnect()
    cr=db.cursor()
    sql='update students set NAME=%s,ADDRESS=%s,CONTACT=%s where ID=%s'
    cr.execute(sql,rec)
    db.commit()
    db.close()
    print('Record updated successfully...')

def singlerec(ID):
    db=getconnect()
    cr=db.cursor()
    sql='select * from students where ID=%s'
    cr.execute(sql,ID)
    stud=cr.fetchall()
    a,b,c,d='ID','NAME','ADDRESS','CONTACT'
    print(f'\n{a:^5} {b:^20} {c:^30} {d:^10}\n') 
    for i,n,a,c in stud:
        print(f'{i:^5} {n:^20} {a:^30} {c:^10}\n')
    db.commit()
    db.close()
    


while True:
    print('\n\n', 'Student\'s section'.center(40,'*')) #this center method will align a string to the center by filling padding at right and left of string
    print('\n1.Insert Record \n2.Read all records \n3.Show single record by ID \n4.Update record \n5.Delete record\n')
    n=int(input('Enter a number from above selection: '))
    if n==1:
        i=int(input('Enter ID of student: '))
        n=input('Enter name of student: ')
        a=input('Enter address of student: ')
        c=input('Enter contact of student: ')
        record=[i,n,a,c]
        addrec(record)

    elif n==2:
        readAll()

    elif n==3:
        i=int(input('Enter ID of student: '))
        singlerec(i)

    elif n==4:
        n=input('Enter updated name of student: ')
        a=input('Enter updated address of student: ')
        c=input('Enter updated contact of student: ')
        
        i=int(input('Enter ID of student to update: '))
        reco=[n,a,c,i]
        updaterec(reco)

    elif n==5:
        n=int(input('Enter ID to be Deleted: '))
        
        deleterow(n)
    else:
        print('Invalid selection')
        break
        

    
    

