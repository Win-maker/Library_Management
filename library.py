books = []
conti = True
while conti:

    print('Register')
    print('List')
    print('Search')
    print('Delete')
    print('Quit')

    choose = input('Choose your process ...')

    def list():
        listBook =','.join(books)
        print("Here is list.... ", listBook)


    def register():
        newbook = input('Enter new book....')
        books.append(newbook)
        registerlist = ','.join(books)
        print("Here is new list ....", registerlist)

    def search():
        usersearch = input('What do you want to search... ')
        for i in books:
            if usersearch == i:
                print(f"We have {usersearch}")
            elif len(books) <= 0 or i != usersearch:
                print(f"Sorry, we dont have {usersearch}")

    def quit():
        print("Thanks For Using Our Program")
        conti = False

    def delete():
        userdelete = input('Type here book you want to delete... ')
        for i in books:
            if userdelete == i:
                books.remove(i)
        print(f"You completely delete {userdelete}")

    if choose == 'Register':
        register()
    elif choose == 'List':
        list()
    elif choose == 'Search':
        search()
    else:
        quit()

    quituser = input("Enter 'f' to exit the program or any key to continue")
    if quituser == 'f':
        print("Thanks For Using Our Program")
        conti = False





