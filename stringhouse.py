class HashTable(object):
    def __init__(self):
        self.table = [None]*12322

    def calculate_hash_value(self, string):
        return ord(string[0])*100 + ord(string[1])

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if self.table[hv] is None:
            self.table[hv] = string
        else:
            print("Sorry no room for this string!"
                  "Room for this string code is already full")

    def look_up(self, string):
        hv = self.calculate_hash_value(string)
        if string in self.table[hv]:
            print("Yes, string exists at location : " + str(hv))
        else:
            print("No, String doesn't exist")


x = 1
hashtable = HashTable()
while x == 1:
    print("             -------- Welcome to house allotment game -------")
    print("Here houses are given to name, on the basis of first two letters of name")
    print("   So, home can't be given to two names with same first two letters   ")
    print("choose in menu:")
    print(" 1 (update) / 2 (Display) / 3 (Exit)")
    choose = int(input())
    if choose == 1:
        print("Choose an option:")
        print("1.Store a string")
        print("2.Find possible address of a string")
        print("3.Find whether this string exists")
        choice = input()
        if choice.isdigit():
            Str = input("Enter a string:")
            if len(Str)>1:
                if int(choice) == 1:
                    hashtable.store(Str)
                    print("String successfully stored!")
                elif int(choice) == 2:
                        print(hashtable.calculate_hash_value(Str))
                elif int(choice) == 3:
                    hashtable.look_up(Str)
                elif int(choice) == 4:
                    x = 0
                else:
                    print("Eh!  invalid choice")
            else:
                print("Invalid string!")
        else:
            print("Invalid choice!")
            print("going back to main menu")
    elif choose == 2:
        print("1.Check string at a given address")
        print("2.Back")
        choice = int(input())
        if choice == 1:
            ch = int(input("Enter address : "))
            if hashtable.table[ch] is not None:
                print("String at this location : " + str(hashtable.table[ch]))
            else:
                print("Sorry this address is empty!")
        elif choice == 2:
            print("Going back to previous menu")
    elif choose == 3:
        x = 0
    else:
        print("Invalid choice!")
