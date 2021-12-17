import csv
file_path = "titanic.csv"
records = []

print("Loading data...", end="")

# Opening the file
try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

    print("Done!")
    print(f"Successfully loaded {len(records)} records.")

# Creating a menu
    selected_option = 0
    index = 0
    while selected_option < 1 or selected_option > 5:
        if index > 0:
            print("You must select an option from the menu provided.")
            index = 1

        selected_option = int(input("\nPlease select one of the following:\n"
                                    "[1] Display the names of all passengers\n"
                                    "[2] Display the number of passengers that survived\n"
                                    "[3] Display the number of passengers per gender\n"
                                    "[4] Display the number of passengers per age group\n"
                                    "[5] Display the number of survivors per age group \n"))
        index += 1

    print(f"\nYou have selected Option {selected_option}.\n")

# Processing Option 1 from the Menu
    if selected_option == int(1):
        print("The names of the passengers are:")
        for record in records:
            passenger_name = record[3]
            print(f"{passenger_name}")

# Processing Option 2 - number of passengers that survived
    elif selected_option == int(2):
        num_survived = 0
        for record in records:
            survival_status = int(record[1])
            if survival_status == int(1):
                num_survived += 1
        print(f"{num_survived} passengers survived the sinking of the Titanic.")

# Processing Option 3 - number of passengers per gender
    elif selected_option == int(3):
        females = 0
        males = 0
        for record in records:
            gender = str(record[4])
            if gender == "female":
                females += 1
            else:
                males += 1
        print(f"There were {females} female passengers and {males} male passengers aboard the RMS Titanic.")

# Processing Option 4 - number of passengers per age group
    elif selected_option == int(4):
        children = 0
        adults = 0
        elderly = 0
        for record in records:
            if record[5] != "":
                age = float(record[5])
                if age < 18:
                    children += 1
                elif age < 65:
                    adults += 1
                else:
                    elderly += 1
        print(f"There were {children} children, {adults} adults, and {elderly} elderly aboard the RMS Titanic.")

# Processing Option 5 - displaying survivors per age group
    elif selected_option == int(5):
        children = adults = elderly = 0
        children_survivors = adult_survivors = elderly_survivors = 0
        for record in records:
            survival_status = int(record[1])
            if record[5] != "":
                age = float(record[5])
                if age < 18:
                    children += 1
                    if survival_status == int(1):
                        children_survivors += 1
                elif age < 65:
                    adults += 1
                    if survival_status == int(1):
                        adult_survivors += 1
                else:
                    elderly += 1
                    if survival_status == int(1):
                        elderly_survivors += 1

        print(f"After the sinking of the RMS Titanic, the following were survivors based on age group: \n"
              f"Children: {children_survivors}/{children}\n"
              f"Adults: {adult_survivors}/{adults}\n"
              f"Elderly: {elderly_survivors}/{elderly}")

except IOError:
    print("Cannot read file.")
