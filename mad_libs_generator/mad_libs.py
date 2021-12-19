# Mad Libs Game based on user input


print("*" * len("Mad Libs Game"))
print("Mad Libs Game")
print("*" * len("Mad Libs Game"))

# Create variables to get user input
plural_noun1 = input("Enter a plural noun: ")
plural_noun2 = input("Enter a plural noun: ")
plural_noun3 = input("Enter a plural noun: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
noun3 = input("Enter a noun: ")
noun4 = input("Enter a noun: ")
noun5 = input("Enter a noun: ")
noun6 = input("Enter a noun: ")
noun7 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
adjective3 = input("Enter an adjective: ")
adjective4 = input("Enter an adjective: ")
adjective5 = input("Enter an adjective: ")

# Give user a menu of stories
story_option = int(input("What Mad Libs Story would you like to read?\n"
                         "[1] The Stock Market\n"
                         "[2] The Weather Report\n"
                         "[3]"))
# Print story based on selected option
if story_option == 1:
    print(f"This is how I made one million {plural_noun1} in the stock market. It's simple.\n"
          f"At the present time, any {adjective1} investor with a little capital should be able to double his {plural_noun1} in a few months.\n"
          f"All the experts agree that we are nearing the end of the {noun1} market.\n"
          f"Just recently, for instance, the American {noun2} and Foundry Company has shown a {adjective2} trend.\n"
          f"Conditions indicate a {adjective3} market for their principal product, automatic {plural_noun2}.\n"
          f"International Telephone and {noun3} Company also looks angry. At the end of the last fiscal {noun4}, they were earning $10 a {noun5}.\n"
          f"Another {adjective4} tip is Consolidated {noun6}. This outfit manufactures and sells electronic {plural_noun3} of a very {adjective5} quality.\n"
          f"But whatever you do, act now. Remember, prosperity is just around the {noun7}.")

elif story_option == 2:
    print("")

elif story_option == 3:
    print("")