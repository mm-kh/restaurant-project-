import mysql.connector
mydb = mysql.connector.connect(user='root', password='1234',host='127.0.0.1',database='restaurant')

import os
from prettytable import PrettyTable

def add_db_food(ID,name,price,materials):
    cursor=mydb.cursor()
    cursor.execute('insert into food values(\'%i\' , \'%s\' , \'%i\' , \'%s\')' %(ID,name,price,materials))
    mydb.commit()

def add_db_salad(ID,name,price,materials):
    cursor=mydb.cursor()
    cursor.execute('insert into salad values(\'%i\' , \'%s\' , \'%i\' , \'%s\')' %(ID,name,price,materials))
    mydb.commit()

def add_db_drink(ID,name,price):
    cursor=mydb.cursor()
    cursor.execute('insert into drink values(\'%i\' , \'%s\' , \'%i\' )' %(ID,name,price))
    mydb.commit()

def del_db_food(ID):
    cursor=mydb.cursor()
    cursor.execute('delete from food where id =\'%i\'' %(ID))
    mydb.commit()

def del_db_salad(ID):
    cursor=mydb.cursor()
    cursor.execute('delete from salad where id =\'%i\'' %(ID))
    mydb.commit()    

def del_db_drink(ID):
    cursor=mydb.cursor()
    cursor.execute('delete from drink where id =\'%i\'' %(ID))
    mydb.commit()
    
def edit_db_food(ID,newName,newPrice,newMaterials):
    cursor=mydb.cursor()
    cursor.execute('update food set name=\'%s\' where id=\'%i\''  %(newName,ID))
    mydb.commit()

    cursor=mydb.cursor()
    cursor.execute('update food set price=\'%i\' where id=\'%i\''  %(newPrice,ID))
    mydb.commit()

    cursor=mydb.cursor()
    cursor.execute('update food set material=\'%s\' where id=\'%i\''  %(newMaterials,ID))
    mydb.commit()

def edit_db_salad(ID,newName,newPrice,newMaterials):
    cursor=mydb.cursor()
    cursor.execute('update salad set name=\'%s\' where id=\'%i\''  %(newName,ID))
    mydb.commit()

    cursor=mydb.cursor()
    cursor.execute('update salad set price=\'%i\' where id=\'%i\''  %(newPrice,ID))
    mydb.commit()

    cursor=mydb.cursor()
    cursor.execute('update salad set material=\'%s\' where id=\'%i\''  %(newMaterials,ID))
    mydb.commit()    

def edit_db_drink(ID,newName,newPrice):
    cursor=mydb.cursor()
    cursor.execute('update drink set name=\'%s\' where id=\'%i\''  %(newName,ID))
    mydb.commit()

    cursor=mydb.cursor()
    cursor.execute('update drink set price=\'%i\' where id=\'%i\''  %(newPrice,ID))
    mydb.commit()


class Food:

    def __init__(self,ID,name,price,materials):
        self.ID=ID
        self.name=name
        self.price=price 
        self.materials=materials
        self.next=None

class Salad:

    def __init__(self,ID,name,price,materials):
        self.ID=ID
        self.name=name 
        self.price=price 
        self.materials=materials
        self.next=None

class Drink:

    def __init__(self,ID,name,price):
        self.ID=ID
        self.name=name
        self.price=price
        self.next=None

class Order:

    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.next=None
                
#-----------------------------------------------------------------------------
                
class FoodList:

    def __init__(self):
        self.head=None



    def checkID(self,ID):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.ID!=ID:
                temp=temp.next
                if temp.next==None:
                    if temp.ID==ID:
                        return 1
                    else:
                        return None
            return 1


    def checkName(self,name): 
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.name!=name:
                temp=temp.next
                if temp.next==None:
                    if temp.name==name:
                        return 1
                    else:
                        return None
            return 1             


    def checkPrice(self,price): 
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.price!=price:
                temp=temp.next
                if temp.next==None:
                    if temp.price==price:
                        return 1
                    else:
                        return None
            return 1               


    def Add(self,ID,name,price,materials):
        temp=Food(ID,name,price,materials)
        if self.head==None:
            self.head=temp
        else:
            s=self.head
            while s.next!=None:
                s=s.next
            s.next=temp



    def Search_By_ID(self,ID):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.ID!=ID:
                temp=temp.next
                if temp.next==None:
                    if temp.ID==ID:
                        return temp
                    else:
                        return None
            return temp


    def Search_By_Name(self,name):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.name!=name:
                temp=temp.next
                if temp.next==None:
                    if temp.name==name:
                        return temp
                    else:
                        return None
            return temp


    def Search_By_Price(self,price):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.price!=price:
                temp=temp.next
                if temp.next==None:
                    if temp.price==price:
                        return temp
                    else:
                        return None
            return temp        


    def Delete_By_ID(self,ID):
        temp=List_1.Search_By_ID(ID)
        del_db_food(ID)
        if temp!=None:

            if temp==self.head:
                self.head=temp.next
            else:
                temp1=self.head
                s=temp1
                while temp1!=temp:
                    s=temp1
                    temp1=temp1.next
                s.next=temp1.next
            print("food deleted successfully.")    
        else:
            print("not found!")

    def Delete_By_Name(self,name):
        temp=List_1.Search_By_Name(name)
        ID=temp.ID
        del_db_food(ID)
        if temp!=None:

            if temp==self.head:
                self.head=temp.next
            else:
                temp1=self.head
                s=temp1
                while temp1!=temp:
                    s=temp1
                    temp1=temp1.next
                s.next=temp1.next 
            print("food deleted successfully.")    
        else:
            print("not found!")                


    def Print(self):
        temp=self.head
        table_food=PrettyTable(['ID' , 'Name' , 'Price' , 'Materials'])
        while temp!=None:
            #print(temp.ID,"  ",temp.name,"  ",temp.price,"  ",temp.materials)
            table_food.add_row([temp.ID,temp.name,temp.price,temp.materials])
            temp=temp.next
        print(table_food)    
        b=input("press enter to continue...")
        print()
        return 0   



class SaladList:


    def __init__(self):
        self.head=None                        


    def checkID(self,ID):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.ID!=ID:
                temp=temp.next
                if temp.next==None:
                    if temp.ID==ID:
                        return 1
                    else:
                        return None
            return 1


    def checkName(self,name): 
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.name!=name:
                temp=temp.next
                if temp.next==None:
                    if temp.name==name:
                        return 1
                    else:
                        return None
            return 1            


    def checkPrice(self,price): 
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.price!=price:
                temp=temp.next
                if temp.next==None:
                    if temp.price==price:
                        return 1
                    else:
                        return None
            return 1            


    def Add(self,ID,name,price,materials):
        temp=Salad(ID,name,price,materials)
        if self.head==None:
            self.head=temp
        else:
            s=self.head
            while s.next!=None:
                s=s.next
            s.next=temp
            



    def Search_By_ID(self,ID):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.ID!=ID:
                temp=temp.next
                if temp.next==None:
                    if temp.ID==ID:
                        return temp
                    else:
                        return None
            return temp


    def Search_By_Name(self,name):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.name!=name:
                temp=temp.next
                if temp.next==None:
                    if temp.name==name:
                        return temp
                    else:
                        return None
            return temp


    def Search_By_Price(self,price):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.price!=price:
                temp=temp.next
                if temp.next==None:
                    if temp.price==price:
                        return temp
                    else:
                        return None
            return temp        


    def Delete_By_ID(self,ID):
        temp=List_2.Search_By_ID(ID)
        del_db_salad(ID)
        if temp!=None:

            if temp==self.head:
                self.head=temp.next
            else:
                temp1=self.head
                s=temp1
                while temp1!=temp:
                    s=temp1
                    temp1=temp1.next
                s.next=temp1.next
            print("salad deleted successfully.")    
        else:
            print("not found!")


    def Delete_By_Name(self,name):
        temp=List_2.Search_By_Name(name)
        ID=temp.ID
        del_db_salad(ID)
        if temp!=None:

            if temp==self.head:
                self.head=temp.next
            else:
                temp1=self.head
                s=temp1
                while temp1!=temp:
                    s=temp1
                    temp1=temp1.next
                s.next=temp1.next
            print("salad deleted successfully.")    
        else:
            print("not found!")


    def Print(self):
        temp=self.head
        table_salad=PrettyTable(['ID','Name','Price','Materials'])
        while temp!=None:
            #print(temp.ID,"  ",temp.name,"  ",temp.price,"  ",temp.materials)
            table_salad.add_row([temp.ID,temp.name,temp.price,temp.materials])
            temp=temp.next
        print(table_salad)    
        b=input("press enter to continue...")
        print()
        return 0   


class DrinkList:


    def __init__(self):
        self.head=None


    def checkID(self,ID):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.ID!=ID:
                temp=temp.next
                if temp.next==None:
                    if temp.ID==ID:

                        return 1
                    else:
                        return None
            return 1


    def checkName(self,name): 
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.name!=name:
                temp=temp.next
                if temp.next==None:
                    if temp.name==name:
                        return 1
                    else:
                        return None
            return 1            


    def checkPrice(self,price): 
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.price!=price:
                temp=temp.next
                if temp.next==None:
                    if temp.price==price:
                        return 1
                    else:
                        return None
            return 1            


    def Add(self,ID,name,price):
        temp=Drink(ID,name,price)
        if self.head==None:
            self.head=temp
        else:
            s=self.head
            while s.next!=None:
                s=s.next
            s.next=temp



    def Search_By_ID(self,ID):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.ID!=ID:
                temp=temp.next
                if temp.next==None:
                    if temp.ID==ID:
                        return temp
                    else:
                        return None
            return temp


    def Search_By_Name(self,name):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.name!=name:
                temp=temp.next
                if temp.next==None:
                    if temp.name==name:
                        return temp
                    else:
                        return None
            return temp


    def Search_By_Price(self,price):
        temp=self.head
        if self.head==None:
            return None
        else:
            while temp.price!=price:
                temp=temp.next
                if temp.next==None:
                    if temp.price==price:
                        return temp
                    else:
                        return None
            return temp        


    def Delete_By_ID(self,ID):
        temp=List_3.Search_By_ID(ID)
        del_db_drink(ID)
        if temp!=None:

            if temp==self.head:
                self.head=temp.next
            else:
                temp1=self.head
                s=temp1
                while temp1!=temp:
                    s=temp1
                    temp1=temp1.next
                s.next=temp1.next
            print("drink deleted successfully.")    
        else:
            print("not found!")


    def Delete_By_Name(self,name):
        temp=List_3.Search_By_Name(name)
        ID=temp.ID
        del_db_drink(ID)
        if temp!=None:

            if temp==self.head:
                self.head=temp.next
            else:
                temp1=self.head
                s=temp1
                while temp1!=temp:
                    s=temp1
                    temp1=temp1.next
                s.next=temp1.next 
            print("drink deleted successfully.")    
        else:
            print("not found!")


    def Print(self):
        temp=self.head
        table_drink=PrettyTable(['ID','Name','Price'])
        while temp!=None:
            #print(temp.ID,"  ",temp.name,"  ",temp.price)
            table_drink.add_row([temp.ID,temp.name,temp.price])
            temp=temp.next
        print(table_drink)    
        b=input("press enter to back :")
        print()
        return 0         


class OrderList:


    def __init__(self):
        self.head=None


    def Add(self,name,price):
        temp=Order(name,price)
        if self.head==None:
            self.head=temp
        else:
            s=self.head
            while s.next!=None:
                s=s.next
            s.next=temp

    def Print(self):
        temp=self.head
        if temp==None:
            print("order not found!")
            print()
            b=input("press enter to back :")
            print()
            Show()            
            
        else:
            table_order=PrettyTable(['Name','Price'])
            while temp!=None:
                table_order.add_row([temp.name,temp.price])
                temp=temp.next

            print(table_order)   
            print("the final price is : ",List_4.price())
            print()
            b=input("press enter to back :")
            print()
            Show()


    def price(self):
        temp=self.head
        m=0
        while temp!=None:
            m+=temp.price
            temp=temp.next
        return m                  

#-----------------------------------------------------------------------------


List_1=FoodList()
List_2=SaladList()
List_3=DrinkList()
List_4=OrderList()

cursor=mydb.cursor()
cursor.execute("select * from food;" )
for (ID,name,price,materials) in cursor:
    List_1.Add(ID, name, price, materials)

cursor=mydb.cursor()
cursor.execute("select * from salad;" )
for (ID,name,price,materials) in cursor:
    List_2.Add(ID, name, price, materials)    

cursor=mydb.cursor()
cursor.execute("select * from drink;" )
for (ID,name,price) in cursor:
    List_3.Add(ID, name, price)

def Desktop_1():
    print("1. food list : ")
    print("2. salad list : ")
    print("3. drink list : ")
    print("4. list of orders : ")
    print("5. exit : ")
    print("select your choice (0...5) : ")


def Desktop_2():
    print("1. add to list. ")
    print("2. edit. ")
    print("3. search. ")
    print("4. delete. ")
    print("5. view list. ")
    print("6. order. ")
    print("7. back. ")
    print("select your choice (0...7) : ")


def Show_1():
    while (True) :
        os.system('cls') 
        key=0
        print("related to food : ")
        Desktop_2()
        key=int(input())
        Choice_1(key)
        if key==7:
            break
        #system pause

def Show_2() :
    while (True):
        os.system('cls')
        key=0
        print("related to salad : ")
        Desktop_2()
        key=int(input())
        Choice_2(key)
        if key==7:
            break
        #system pause

def Show_3():
    while (True):
        os.system('cls') 
        key=0
        print("related to drink")
        Desktop_2()
        key=int(input())
        Choice_3(key)
        if key==7:
            break
        #system pause    

def Show_4():
    os.system('cls')
    print("related to orders : ")
    List_4.Print()


def Choice(key):
    if key==1:
        Show_1()
    elif key==2:
        Show_2()
    elif key==3:
        Show_3()
    elif key==4:
        Show_4()    
    else :
        return 0    


def Choice_1(key):
    os.system('cls')
    if key==1:
        ID=int(input("enter id :"))
        check=List_1.checkID(ID)
        if check==1:
            print("This id is already in the list .")
            print("please try again .")
            b=input("press enter to continue...")
        else:   
            name=input("enter name :")
            checkN=List_1.checkName(name)
            if checkN==1:
                print("This name is already in the list .")
                print("please try again .")
                b=input("press enter to continue...")
            else:                    
                price=int(input("enter price :"))
                checkP=List_1.checkPrice(price)
                if checkP==1:
                    print("This price is already in the list .")
                    print("please try again .")
                    b=input("press enter to continue...")
                else:    
                    materials=input("enter materials :")
                    print("food added successfully .")
                    b=input("press enter to continue...")
                    List_1.Add(ID,name,price,materials)
                    add_db_food(ID, name, price, materials)

    elif key==2:
        print("enter id or name :")
        print("1. id")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            temp=List_1.Search_By_ID(ID)
        elif x==2:
            print("enter name :")
            name=input()
            temp=List_1.Search_By_Name(name)


        if temp!=None:
            table_edit=PrettyTable(['Name','Price','Materials'])
            table_edit.add_row([temp.name,temp.price,temp.materials])
            print(table_edit)            
            #print(temp.name,"  ",temp.price,"  ",temp.materials)
            print()
            b=input("press enter to continue...")
            os.system('cls')
            newName=input("enter new name :")
            newPrice=int(input("enter new price :"))
            newMaterials=input("enter new materials :")
            print("food edited successfully.")
            b=input("press enter to continue...")
            edit_db_food(temp.ID,newName,newPrice,newMaterials)
            temp.name=newName
            temp.price=newPrice
            temp.materials=newMaterials
        else :
            print("not found!") 
            b=input("press enter to continue...")   

    elif key==3:
        print("search by ?:")
        print("1. id")
        print("2. name")
        print("3. price")
        y=int(input())
        os.system('cls')
        if y==1:
            print("enter id :")
            ID=int(input())
            s1=List_1.Search_By_ID(ID)
            if s1!=None:
                os.system('cls')
                print("your search :")
                table_search=PrettyTable(['ID','Name','Price','Materials'])
                table_search.add_row([s1.ID,s1.name,s1.price,s1.materials])
                print(table_search)
                #print(s1.ID,"  ",s1.name,"  ",s1.price,"  ",s1.materials)
            else :
                os.system('cls')
                print("not found!")
            print()    
            b=input("press enter to continue...")
            print()
            return 0                            
           

        elif y==2:
            print("name :")
            name=input()
            s1=List_1.Search_By_Name(name)
            if s1!=None:
                os.system('cls')
                print("your search :")
                table_search=PrettyTable(['ID','Name','Price','Materials'])
                table_search.add_row([s1.ID,s1.name,s1.price,s1.materials])
                print(table_search)                
                #print(s1.ID,"  ",s1.name,"  ",s1.price,"  ",s1.materials)
            else :
                os.system('cls')
                print("not found!")
            print()    
            b=input("press enter to continue...")
            print()
            return 0               


        elif y==3:
            print("enter price :")
            price=int(input())
            s1=List_1.Search_By_Price(price)
            if s1!=None:
                os.system('cls')
                print("your search :")   
                table_search=PrettyTable(['ID','Name','Price','Materials'])
                table_search.add_row([s1.ID,s1.name,s1.price,s1.materials])
                print(table_search)             
                #print(s1.ID,"  ",s1.name,"  ",s1.price,"  ",s1.materials)
            else :
                os.system('cls')
                print("not found!")   
            print()    
            b=input("press enter to continue...")
            print()
            return 0                                

    elif key==4:
        print("delete by ?:")
        print("1. id ")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            List_1.Delete_By_ID(ID)
            b=input("press enter to continue...")
        elif x==2:
            print("enter name :")
            name=input()
            List_1.Delete_By_Name(name)   
            b=input("press enter to continue...") 

    elif key==5:
        os.system('cls')
        List_1.Print()

    elif key==6:
        print("order by ?:")
        print("1. id ")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            s1=List_1.Search_By_ID(ID)
            if s1!=None:
                os.system('cls')
                print("food ordered successfully")
                List_4.Add(s1.name,s1.price)
                b=input("press enter to continue...")
            else:
                os.system('cls')
                print("not found! ")
                b=input("press enter to continue...")
        elif x==2:
            print("enter name :")
            name=input()
            s2=List_1.Search_By_Name(name)
            if s2!=None:
                os.system('cls')
                print("food ordered successfully")
                List_4.Add(s2.name, s2.price)
                b=input("press enter to continue...")
            else:
                os.system('cls')
                print("not found!")
                b=input("press enter to continue...")


    elif key==7:
        Show()



def Choice_2(key):
    os.system('cls')
    if key==1:
        ID=int(input("enter id :"))
        check=List_2.checkID(ID)
        if check==1:
            print("This id is already in the list .")
            print("please try again .")
            b=input("press enter to continue...")
        else:   
            name=input("enter name :")
            checkN=List_2.checkName(name)
            if checkN==1:
                print("This name is already in the list .")
                print("please try again .")
                b=input("press enter to continue...")
            else:   
                price=int(input("enter price :"))
                checkP=List_2.checkPrice(price)
                if checkP==1:
                    print("This price is already in the list .")
                    print("please try again .")
                    b=input("press enter to continue...")
                else:    
                    materials=input("enter materials :")
                    print("salad added successfully .")
                    b=input("press enter to continue...")
                    List_2.Add(ID,name,price,materials)
                    add_db_salad(ID, name, price, materials)

    elif key==2:
        print("enter id or name :")
        print("1. id")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            temp=List_2.Search_By_ID(ID)
        elif x==2:
            print("enter name :")
            name=input()
            temp=List_2.Search_By_Name(name)


        if temp!=None:
            table_edit=PrettyTable(['Name','Price','Materials'])
            table_edit.add_row([temp.name,temp.price,temp.materials])
            print(table_edit)            
            #print(temp.name,"  ",temp.price,"  ",temp.materials)
            print()
            b=input("press enter to continue...")
            os.system('cls')
            newName=input("enter new name :")
            newPrice=int(input("enter new price :"))
            newMaterials=input("enter new materials :")
            print("salad edited successfully.")
            b=input("press enter to continue...")
            edit_db_salad(temp.ID,newName,newPrice,newMaterials)
            temp.name=newName
            temp.price=newPrice
            temp.materials=newMaterials
        else :
            print("not found!")  
            b=input("press enter to continue...")     

    elif key==3:
        print("search by ?:")
        print("1. id")
        print("2. name")
        print("3. price")
        y=int(input())
        os.system('cls')
        if y==1:
            print("enter id :")
            ID=int(input())
            s1=List_2.Search_By_ID(ID)
            if s1!=None:
                os.system('cls')
                print("your search :")
                table_search=PrettyTable(['ID','Name','Price','Materials'])
                table_search.add_row([s1.ID,s1.name,s1.price,s1.materials])
                print(table_search)                 
                #print(s1.ID,"  ",s1.name,"  ",s1.price,"  ",s1.materials)
            else :
                os.system('cls')
                print("not found!")   
            print()    
            b=input("press enter to continue...")
            print()
            return 0                         
           

        elif y==2:
            print("name :")
            name=input()
            s1=List_2.Search_By_Name(name)
            if s1!=None:
                os.system('cls')
                print("your search :")
                table_search=PrettyTable(['ID','Name','Price','Materials'])
                table_search.add_row([s1.ID,s1.name,s1.price,s1.materials])
                print(table_search) 
                #print(s1.ID,"  ",s1.name,"  ",s1.price,"  ",s1.materials)
            else :
                os.system('cls')
                print("not found!") 
            print()    
            b=input("press enter to conyinue...")
            print()
            return 0                  


        elif y==3:
            print("enter price :")
            price=int(input())
            s1=List_2.Search_By_Price(price)
            if s1!=None:
                os.system('cls')
                print("your search :") 
                table_search=PrettyTable(['ID','Name','Price','Materials'])
                table_search.add_row([s1.ID,s1.name,s1.price,s1.materials])
                print(table_search)                 
                #print(s1.ID,"  ",s1.name,"  ",s1.price,"  ",s1.materials)
            else :
                os.system('cls')
                print("not found!") 
            print()    
            b=input("press enter to continue...")
            print()
            return 0                              

    elif key==4:
        print("delete by ?:")
        print("1. id ")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            List_2.Delete_By_ID(ID)
            b=input("press enter to continue...")
        elif x==2:
            print("enter name :")
            name=input()
            List_2.Delete_By_Name(name)
            b=input("press enter to continue...")

    elif key==5:
        os.system('cls')
        List_2.Print()

    elif key==6:
        print("order by ?:")
        print("1. id ")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            s1=List_2.Search_By_ID(ID)
            if s1!=None:
                os.system('cls')
                print("salad ordered successfully")
                List_4.Add(s1.name,s1.price)
                b=input("press enter to continue...")
            else:
                os.system('cls')
                print("not found! ")
                b=input("press enter to continue...")
        elif x==2:
            print("enter name :")
            name=input()
            s2=List_2.Search_By_Name(name)
            if s2!=None:
                os.system('cls')
                print("salad ordered successfully")
                List_4.Add(s2.name, s2.price)
                b=input("press enter to continue...")
            else:
                os.system('cls')
                print("not found!")
                b=input("press enter to continue...")

    elif key==7:
        Show()

def Choice_3(key):
    os.system('cls')
    if key==1:
        ID=int(input("enter id :"))
        check=List_3.checkID(ID)
        if check==1:
            print("This id is already in the list .")
            print("please try again .")
            b=input("press enter to continue...")
        else:   
            name=input("enter name :")
            checkN=List_3.checkName(name)
            if checkN==1:
                print("This name is already in the list .")
                print("please try again .")
                b=input("press enter to continue...")
            else:                    
                price=int(input("enter price :"))
                checkP=List_3.checkPrice(price)
                if checkP==1:
                    print("This price is already in the list .")
                    print("please try again .")
                    b=input("press enter to continue...")
                else:        
                    print("drink added successfully .")
                    b=input("enter enter to continue...")
                    List_3.Add(ID,name,price)
                    add_db_drink(ID, name, price)

    elif key==2:
        print("enter id or name :")
        print("1. id")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            temp=List_3.Search_By_ID(ID)
        elif x==2:
            print("enter name :")
            name=input()
            temp=List_3.Search_By_Name(name)

        if temp!=None:
            table_edit=PrettyTable(['Name','Price'])
            table_edit.add_row([temp.name,temp.price])
            print(table_edit)            
            #print(temp.name,"  ",temp.price)
            print()
            b=input("press enter to continue...")
            os.system('cls')
            newName=input("enter new name :")
            newPrice=int(input("enter new price :"))
            print("drink edited successfully.")
            b=input("press enter to continue...")
            edit_db_drink(temp.ID,newName,newPrice)
            temp.name=newName
            temp.price=newPrice
        else :
            print("not found")  
            b=input("press enter to continue...")       

    elif key==3:
        print("search by ?:")
        print("1. id")
        print("2. name")
        print("3. price")
        y=int(input())
        os.system('cls')
        if y==1:
            print("enter id :")
            ID=int(input())
            s1=List_3.Search_By_ID(ID)
            if s1!=None:
                os.system('cls')
                print("your search :")
                table_search=PrettyTable(['ID','Name','Price'])
                table_search.add_row([s1.ID,s1.name,s1.price])
                print(table_search) 
                #print(s1.ID,"  ",s1.name,"  ",s1.price)
            else :
                os.system('cls')
                print("not found!") 
            print()    
            b=input("press enter to continue...")
            print()
            return 0                           
           

        elif y==2:
            print("name :")
            name=input()
            s1=List_3.Search_By_Name(name)
            if s1!=None:
                os.system('cls')
                print("your search :")
                table_search=PrettyTable(['ID','Name','Price'])
                table_search.add_row([s1.ID,s1.name,s1.price])
                print(table_search) 
                #print(s1.ID,"  ",s1.name,"  ",s1.price)
            else :
                os.system('cls')
                print("not found!") 
            print()
            b=input("press enter to continue...")
            print()
            return 0                    


        elif y==3:
            print("enter price :")
            price=int(input())
            s1=List_3.Search_By_Price(price)
            if s1!=None:
                os.system('cls')
                print("your search :")
                table_search=PrettyTable(['ID','Name','Price'])
                table_search.add_row([s1.ID,s1.name,s1.price])
                print(table_search)                 
                #print(s1.ID,"  ",s1.name,"  ",s1.price)
            else :
                os.system('cls')
                print("not found!")   
            print()
            b=input("press enter to continue")
            print()
            return 0  


    elif key==4:
        print("delete by ?:")
        print("1. id ")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            List_3.Delete_By_ID(ID)
            b=input("press enter to continue...")
        elif x==2:
            print("enter name :")
            name=input()
            List_3.Delete_By_Name(name)  
            b=input("press enter to continue...")
            
    elif key==5:
        os.system('cls')
        List_3.Print()

    elif key==6:
        print("order by ?:")
        print("1. id ")
        print("2. name")
        x=int(input())
        os.system('cls')
        if x==1:
            print("enter id :")
            ID=int(input())
            s1=List_3.Search_By_ID(ID)
            if s1!=None:
                os.system('cls')
                print("drink ordered successfully")
                List_4.Add(s1.name,s1.price)
                b=input("press enter to continue...")
            else:
                os.system('cls')
                print("not found! ")
                b=input("press enter to continue...")
        elif x==2:
            print("enter name :")
            name=input()
            s2=List_3.Search_By_Name(name)
            if s2!=None:
                os.system('cls')
                print("drink ordered successfully")
                List_4.Add(s2.name, s2.price)
                b=input("press enter to continue...")
            else:
                os.system('cls') 
                print("not found")
                b=input("press enter to continue...")

    elif key==7:
        Show()        

def Show():
    os.system('cls')    
    key=0
    Desktop_1()
    while(True):
        try :
            key=int(input())
            break
        except :
            print("You should have entered a valid number...")
    Choice(key)
 

Show()        