#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 08:26:21 2023

@author: sam
"""

#importing the sqlite3 module
import sqlite3 

#creating a variable to manipulate the database
db = sqlite3.connect('book_catalouge')
cursor = db.cursor()

#if the table does not exist, then it is created with this line
cursor.execute('''
                CREATE TABLE IF NOT EXISTS 
                ebookstore(ID INTEGER PRIMARY KEY,Title TEXT,Author TEXT,Qty INTEGER)
''')



#this function will add a book to the table 
def enter_book():
    
    #the function asks the user for the required fields to add to the table
    Id = int(input("Please enter the ID of the new book: \n"))
    title = input("Please enter the title of the book: \n ")
    author = input("Please enter the author of the book: \n")
    qty = int(input("Please enter the quantity of the book in stock: \n"))
    
    
    #the try except block makes sure that the ID entered is unique. otherwise the user is returned to the menu
    try:
        cursor.execute('''INSERT INTO ebookstore (ID,Title,Author,Qty) VALUES(?,?,?,?)''',(Id,title,author,qty))
        db.commit()
        print("Book added to the catalouge")
    
    except Exception as IntegrityError:
        print("This ID is already in use. Please use a unique ID. You will be returned to the menu.")
        db.rollback

#this function shows the user all the books in the store and asks which one they would like to inspect        
def search_book():
    
    #selecting all the books in the table and printing them in a readable way
    cursor.execute('''SELECT ID,Title,Author,Qty FROM ebookstore''')
    books = cursor.fetchall()
    
    print("\n")
    print("ID       Title               Author        Qty")
    
    for book in books:
        print (book)
    print("\n")
    
    #the while loop keeps asking the user to enter an ID until they enter a valid one 
    while True:
        try:
            id1 = int(input("Please enter the ID number of the book you wish to view:   "))
            cursor.execute('''SELECT ID,Title,Author,Qty FROM ebookstore WHERE ID = ?''',(id1,))
           
            book = cursor.fetchone()
            
            #if the book is not in the table then None will be outputted. So this if block triggers the except block to print an error
            if book == None:
                runexceptblock = "yes"
                runexceptblock = int(runexceptblock)
            else:
                print("\n")
                print(book)
                print("\n")
      
            break

        except ValueError:
            print("No enteries found with that ID")

#this function will delete a book from the table                  
def del_book():
    
    #the while loop will keep asking the user to enter an iD until it is a valid one
    while True:
        
        try:
            Id = int(input("Please enter the ID of the book you wish to delete"))
            cursor.execute('''SELECT ID,Title,Author,Qty FROM ebookstore WHERE ID = ?''',(Id,))
            book = cursor.fetchone()
            
            if book == None:
                runexceptblock = "yes"
                runexceptblock = int(runexceptblock)
            else:
                print("\n")
                print(book)
                print("\n")
            
            break
        
        except ValueError:
            print("No enteries found with that ID")
    
    #the user then needs to confirm that they want to delete the corresponding book
    confirm = input("Is this the book you wish to delete from the catalouge (Y/N)").lower()
    
    
    #this block will keep asking the user for a different ID until they choose the book they want to delete
    if confirm != "y": 
        while confirm != 'y':
            Id = int(input("Please enter the ID of the book you wish to delete"))
            cursor.execute('''SELECT ID,Title,Author,Qty FROM ebookstore WHERE ID = ?''',(Id,))
            book = cursor.fetchone()
            print(book)
            confirm = input("Is this the book you wish to delete from the catalouge (Y/N)").lower()
            
            if confirm == "y": 
                break
    else:
        pass 
    
    #the book is deleted and then the database is commited to so that the changes are saved
    cursor.execute('''DELETE FROM ebookstore WHERE ID = ?''',(Id,))
    print(book)
    db.commit()
    print('Succesfully deleted from catalouge')

#this function will update the details of a book in the table
def update_book():
    
    #the user is asked which attribute of the book they want to edit and the ID of the book they wish to edit
    update = input("""(CASE SENSITIVE) Do you want to update the 'ID', 'Title', 'Author', or 'Qty' of the book""").replace(" ", "")
    Id = int(input("Enter the ID of the book you wish to update: "))
    
    #since Qty and ID are both integers I included them in the same if block
    if update == "Qty" or update == "ID":
        change = int(input("Enter the new id or qty here:"))
   #for the same reason I included title and author in the same block 
    elif update =='Title' or update =='Author':
        change = input("Enter the new title or author here:  ")
    
    #the information from the given if block is then inputted into here and using an f string the requested change is made
    cursor.execute(f'''UPDATE ebookstore SET {update}=? WHERE ID = ?''',(change,Id,))
    db.commit()

#this while loop takes care of the menu 
while True: 
    
    #the user is prompted to enter a number and the corresponding menu item and function are called 
    #if the user enters an invalid number or character they are given an error message and the menu is presented to them again
    try:
        menu = int(input("""
1. Enter Book
2. Update Book 
3. Delete Book 
4. Search Books
0. Exit


"""))
    
        if menu == 1:
            enter_book()
        if menu == 2:
            update_book()
        if menu == 3:
            del_book()
        if menu == 4:
            search_book()
        if menu == 0:
            print("Closing menu...")
            db.close()
            break 
        else:
            print("Please enter the number corresponding with the menu item you want to access")
    except ValueError:
        print("Please enter the number corresponding with the menu item you want to access")


           








