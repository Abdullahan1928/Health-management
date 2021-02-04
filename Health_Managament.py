def name():
    while 1:

        if n == 1:
            print("You chose 1.Your name is Abdullah.")
            break
        elif n == 2:
            print("You chose 2.Your name is Ali.")
            break
        elif n == 3:
            print("You chose 3.Your name is Ahmad.")
            break
        else:
            print("You chose wrong number.Choose one of the given choices.")
            continue


def choice():

    while 1:

        if c == 1:
            print("You chose to write about excercise.")
            break
        elif c == 2:
            print("You chose to write about diet.")
            break
        else:
            print("Choose from the given options.")
            continue


def getdate():
    import datetime
    return datetime.datetime.now()


def files():

    if n == 1 and c == 1:
        if x == 1:
            print("You chose to read the file.\n")
            print("Now start reading about your excersice.\n")

            f1 = open("Harryexcercise.txt", "r+")

            content = f1.read()
            print(content)

            f1.close()

        if x == 2:
            print("You chose to write the file.\n")
            print("Now start writing about your excersice.")

            f1 = open("Harryexcercise.txt", "a+")

            date = str(getdate())
            write1 = input()
            f1.write("["+date+"]:\t"+write1+"\n")

            f1.close()

    if n == 1 and c == 2:

        if x == 1:
            print("You chose to read the file.\n")
            print("Now start reading about your excersice.\n")

            f2 = open("Harrydiet.txt", "r+")

            content = f2.read()
            print(content)

            f2.close()

        if x == 2:
            print("You chose to write the file.\n")
            print("Now start writing about your excersice.")

            f2 = open("Harrydiet.txt", "a+")

            date = str(getdate())
            write1 = input()
            f2.write("["+date+"]:\t"+write1+"\n")

            f2.close()

    if n == 2 and c == 1:

        if x == 1:
            print("You chose to read the file.\n")
            print("Now start reading about your excersice.\n")

            f3 = open("Rohanexcercise.txt", "r+")

            content = f3.read()
            print(content)

            f3.close()

        if x == 2:
            print("You chose to write the file.\n")
            print("Now start writing about your excersice.")

            f3 = open("Rohanexcercise.txt", "a+")

            date = str(getdate())
            write1 = input()
            f3.write("["+date+"]:\t"+write1+"\n")

            f3.close()

    if n == 2 and c == 2:

        if x == 1:
            print("You chose to read the file.\n")
            print("Now start reading about your excersice.\n")

            f4 = open("Rohandiet.txt", "r+")

            content = f4.read()
            print(content)

            f4.close()

        if x == 2:
            print("You chose to write the file.\n")
            print("Now start writing about your excersice.")

            f4 = open("Rohandiet.txt", "a+")

            date = str(getdate())
            write1 = input()
            f4.write("["+date+"]:\t"+write1+"\n")

            f4.close()

    if n == 3 and c == 1:

        if x == 1:
            print("You chose to read the file.\n")
            print("Now start reading about your excersice.\n")

            f5 = open("Hammadexcercise.txt", "r+")

            content = f5.read()
            print(content)

            f5.close()

        if x == 2:
            print("You chose to write the file.\n")
            print("Now start writing about your excersice.")

            f5 = open("Hammadexcercise.txt", "a+")

            date = str(getdate())
            write1 = input()
            f5.write("["+date+"]:\t"+write1+"\n")

            f5.close()

    if n == 3 and c == 2:

        if x == 1:
            print("You chose to read the file.\n")
            print("Now start reading about your excersice.\n")

            f6 = open("Hammaddiet.txt", "r+")

            content = f6.read()
            print(content)

            f6.close()

        if x == 2:
            print("You chose to write the file.\n")
            print("Now start writing about your excersice.")

            f6 = open("Hammaddiet.txt", "a+")

            date = str(getdate())
            write1 = input()
            f6.write("["+date+"]:\t"+write1+"\n")

            f6.close()

print("\t\t\t\t******************************")
print("\t\t\t\t WELCOME TO HEALTH MANAGEMENT")
print("\t\t\t\t******************************")

while(1):
    n = int(
        input("Enter the number to for your name:\n1)Abdullah\n2)Ali\n3)Ahmad\n"))
    name()

    c = int(
        input("Enter what you want to write about:\n1)Excercise\n2)Diet\n"))
    choice()

    x = int(input(
        "Choose one of the following options:\n1)Reading the file\n2)Writing the file\n"))
    files()

    close = input(
        print("Press e to exit program.Press any other key to continue."))
    if(close == "e"):
        exit()
