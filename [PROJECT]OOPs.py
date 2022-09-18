class Library:
    def __init__(self, a, b):
        self.name = a
        self.listogbooks = b
        self.dictionary={}

    def displaybook(self):
        print(self.listogbooks)

    def lendbook(self):
        bookname = input("Enter the book name you want to lend: ")
        lender = input("Enter your name: ")
        for i in self.dictionary:
            if i==bookname:
                print(f"Sorry teh book is alreay lent by {self.dictionary[i]}")
            else:
                self.dictionary[bookname] = lender

    def addbook(self):
        boookname=input("Enter book name you want to add: ")
        self.listogbooks.append(boookname)

    def returnbook(self):
        boookname=input("Enter book name you want to return: ")
        del self.dictionary[boookname]

if __name__ == '__main__':
    lis1 = ["a", "b", "c", "d", "e"]
    devlib = Library("Devraj Lirary", lis1)
    # devlib.lendbook()
    while True:
        print(f"Welcome to {devlib.name}")
        print("Press 1: Display list of books")
        print("Press 2: Lend book")
        print("Press 3: Add book")
        print("Press 4: Return book")
        print("Press 5: Exit")
        while True:
            inp=int(input("Press:"))
            if inp==1:
                devlib.displaybook()
            if inp==2:
                devlib.lendbook()
            if inp==3:
                devlib.addbook()
            if inp==4:
                devlib.returnbook()
            if inp==5:
                print("Have a nice day\n\n")
                # time.sleep(2)
                break