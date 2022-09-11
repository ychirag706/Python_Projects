def main():
    print(" this program converts US DOLLARS to  Pounds Sterling")
    print()

    dollars =  eval(input("Enter amount in dollars: "))

    pounds = covert_to_pounds(dollars)

    print("That is", pounds, "pounds.")
    