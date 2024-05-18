#Module 5: Mini-project | Library Management System with Database Integration
Library = ["The Great Gatsby", "Moby-dick", "Pinkalicious", "The Hunger Games: Catching Fire book" ]
Checked_out = []
User = ['lildeb288@gmail.com , Debbie Greek', 'susu45@yahoo.com , Susan Johnson', 'yoland468@hotmail.com , Yoland Charls'] 

print("""Welcome to the Library Management System with Database Integration!
     Main Menu:
    1. Book Operations
    2. User Operations
    3. Quit""")
while True:
        print("Welcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print("you selected book operations")
            print("""Book Operations:
                1. Add a new book
                2. Borrow a book 
                3. Return a book
                4. Search for a book
                5. Display all books""")
            selection = input("Enter your selection: ") 
            if selection == '1':
                print("you selected Add a new book")
                Library.append(input("input a new book"))
                print(Library)
            elif selection == '2':
                 print("You selected to Borrow a book")
                 a = input("Title of A book in the Library list you would like to Borrow")
                 Library.remove(a)
                 Checked_out.append(a)
                 print("The Library Books")
                 print(Library)
                 print("You Checked out")
                 print(Checked_out)
            elif selection == '3':
                 b = input("Title of A book in the Library list you would like to return")
                 Checked_out.remove(b)
                 Library.append(b)
                 print("The Library Books")
                 print(Library)
                 print("Books still Checked out")
                 print(Checked_out)
            elif selection == '4':
                print("so, you want to search for a book?")
                def findit():
                    print(Library.count(input("Name of a book")))
                break
            else:
                selection == '5'
                print("Library")
                print(Library)
        elif choice == '2':
            print("you selected User Operations")
            print("""User Operations
                    1. Add a new user
                    2. View user details
                    3. Display all users""")
            choose = input("Enter your choice: ") 
            if choose == '1':
                print("you selected Add a new user")
                User.append(input("user email, Name"))
                print(User)
            elif choose == '2':
                 print("You selected to view user details")
                 print(input("User Name"))
            else:
                choose == '3'
                print("You selected to view user details")
                print(User)
        else:
             print("choose a new option")

