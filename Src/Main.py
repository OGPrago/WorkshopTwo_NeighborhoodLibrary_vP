import sys
import os

from Model.Book import Book

def main():
    bookInventory = [
        Book(1, "1435158695", "The Art of War", True, "Tony"),
        Book(2, "1590309847", "The Book of Five Rings", True, "Jeremy"),
        Book(3, "00553418033", "Fast Food Maniac", True, "Jeremy"),
        Book(4, "1975314212", "Three Days of Happiness", True, "Jeremy"),
        Book(5, "9781975303129", "86—EIGHTY-SIX, Vol. 1", False, ""),
        Book(6, "9781250866448", "Friends, Lovers, and the Big Terrible Thing", False, ""),
        Book(7, "9781974734641", "Look Back", True, "Jeremy"),
        Book(8, "9781646512492", "A Silent Voice Complete Collector's Edition 1", True, "Jeremy"),
        Book(9, "9781646514069", "A Silent Voice Complete Collector's Edition 2", True, "Jeremy"),
        Book(10, "9781632366436", "A Silent Voice Complete Series Box Set", True, ""),
        Book(11, "9781637742617", "Tremendous", True, "Jeremy"),
        Book(12, "9780399592096", "The Ride of a Lifetime: Lessons Learned from 15 Years as CEO of the Walt Disney Company", True, "Jeremy"),
        Book(13, "9780525478812", "The Fault in Our Stars", True, "Jeremy"),
        Book(14, "9780765367297", "Halo: The Fall of Reach", True, "Jeremy"),
        Book(15, "9781789092615", "Gears of War: Ascendance", True, "Jeremy"),
        Book(16, "9781421561325", "Uzumaki", True, "Jeremy"),
        Book(17, "9781645059998", "My Alcoholic Escape from Reality", True, "Jeremy"),
        Book(18, "9780316254205", "Kingdom Hearts: Final Mix, Vol. 1 - manga", True, "Jeremy"),
        Book(19, "9780316254212", "Kingdom Hearts: Final Mix Vol. 2", True, "Jeremy"),
        Book(20, "9781501194290", "Howard Stern Comes Again", False, ""),
        Book(21, "9780316512442", "The Saga of Tanya the Evil, Vol. 1: Deus lo Vult", True, "Jeremy"),
        Book(22, "9780316512466", "The Saga of Tanya the Evil, Vol. 2: Plus Ultra", True, "Jeremy"),
        Book(23, "9780316512480", "The Saga of Tanya the Evil, Vol. 3: The Finest Hour", True, "Jeremy"),
        Book(24, "9780316560627", "The Saga of Tanya the Evil, Vol. 4: Dabit Deus his Quoque Finem", False, ""),
        Book(25, "9781250183866", "Extreme Ownership: How U.S. Navy SEALs Lead and Win", True, "Jeremy"),
        Book(26, "1451627289", "11/22/63: A Novel", False, ""),
        Book(27, "1982173610", "Billy Summers", False, ""),
        Book(28, "150114426X", "The Long Walk", False, "")
    ]

    book_inventory = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10,
                      book11, book12, book13, book14, book15, book16, book17, book18, book19,
                      book20, book21, book22, book23, book24, book25, book26, book27, book28]

    while True:
        print("Welcome to the Library")
        print("Please select an option: ")
        print("\t1) Show available books")
        print("\t2) Show checked out books")
        print("\t3) Exit")

        command = input().strip()

        if command == "1":
            print("Here are all the available books: ")
            for book in bookInventory:
                if book.available:
                    print(book)

            print("Would you like to check out a book?")
            print("\t1) Yes")
            print("\t2) No, go back to home screen")
            checkoutOption = input().strip()

            if checkoutOption == "1":
                while True:
                    print("Please enter the ID of the book you want to check out (or 0 to go back):")
                    bookIdToCheckout = int(input().strip())

                    if bookIdToCheckout == 0:
                        break 

                    for book in bookInventory:
                        if book.id == bookIdToCheckout and book.available:
                            print("Please enter your name to check out the book:")
                            borrowerName = input().strip()

                            if book.check_out(borrowerName):
                                print(f"Successfully checked out to {borrowerName}")
                            else:
                                print("Book is already checked out.")
                            break
                    else:
                        print("Invalid book ID or book is not available.")
            elif checkoutOption == "2":
                continue
            else:
                print("Command not found.")

        elif command == "2":
            print("Here are all books currently checked out: ")
            hasCheckedOutBooks = False
            for book in bookInventory:
                if not book.available:
                    print(book)
                    hasCheckedOutBooks = True

            if not hasCheckedOutBooks:
                print("No books are currently checked out.")
                continue

            print("Please select an option:")
            print("\tC) Check In a book")
            print("\tX) Go back to home screen")
            checkInOption = input().strip().upper()

            if checkInOption == "C":
                print("Please enter the ID of the book you want to check in:")
                bookIdToCheckIn = int(input().strip())

                for book in bookInventory:
                    if book.id == bookIdToCheckIn and not book.available:
                        book.check_in()
                        print(f"Book ID {bookIdToCheckIn} has been returned and checked in.")
                        break
                else:
                    print("Invalid book ID or book is not checked out.")
            elif checkInOption == "X":
                continue
            else:
                print("Command not found.")

        elif command == "3":
            print("Thank you for visiting the library!")
            break

        else:
            print("Command not found.")

if __name__ == "__main__":
    main()