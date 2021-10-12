import matplotlib.pyplot as plt

try:
    print("A Simple Data Analysis Program")
    print()

    emission_dict = {}

    with open('Emissions.csv', 'r') as file:
        for data in file.read().split('\n'):
            emission_dict.update({data.split(',')[0]: data.split(',')[1:]})

    print("All data from Emissions.csv has been read into a dictionary.", end='\n\n')
    '''TODO: input_year = input('Enter the year for which you'd like to see the data: ')'''
    input_year = '2001'

    index_of = None
    lines = []
    # Loop through First VALUE of Dictionary and if year present in list then set index of VALUE as index_of
    for item in emission_dict.values():
        if input_year in item:
            index_of = (item.index(input_year))

    total = 0
    i = 0
    emissions_in_year = []
    # Loop through VALUES of Dictionary
    for value in emission_dict.values():
        # For the first loop skip the code because in our case it contains Column Names and Years
        if i != 0:
            # Add VALUE of Emission to total
            total += float(value[index_of])
            # Append the value to emissions_in_year
            emissions_in_year.append(list(emission_dict.values())[i][index_of])
        i += 1
    # Let's try to understand this from inner Single Line loop. We converted String to float and created list, from this
    # list we found the maximum and minimum float value, converted that into string and got the index of maximum and
    # minimum emission country.
    max_country_index = int(emissions_in_year.index(
        str(max(float(str_value) for str_value in emissions_in_year))))
    min_country_index = int(emissions_in_year.index(
        str(min(float(str_value) for str_value in emissions_in_year))))
    average_emissions = total / len(emission_dict.values())

    # Using index value we got the Name of maximum and minimum country name
    max_emission = list(emission_dict.keys())[max_country_index + 1]
    min_emission = list(emission_dict.keys())[min_country_index + 1]
    print(f'In {input_year}, countries with minimum and maximum CO2 emission levels were: [{min_emission}] '
          f'and [{max_emission}] respectively.')
    print(
        f'Average CO2 emissions in {input_year} were {"%.6f" % round(average_emissions, 6)}')
    print()
    ''' TODO: visualize_country = input('Enter the country for which you'd like to visualize the data)
        TODO: Exception Handling
    '''
    visualize_country = 'Qatar'
    # From user entered value we extracted the Index value of country
    number = list(emission_dict.keys()).index(visualize_country)
    # Passed that index value to matplotlib plot function. As x value we passed years and as y value we passed emission value
    plt.plot(list(map(float, list(emission_dict.values())[0])),
             list(map(float, list(emission_dict.values())[number])))
    # Given the Title and Lable to Plot
    plt.title("Year vs Emissions in Capita")
    plt.xlabel("Year")
    plt.ylabel("Emissions in " + visualize_country.title())
    plt.show()
    print()
    '''TODO:country1, country2 = input("Write two comma-separated countries for which you want to visualize data: ").split(", ")'''
    country1, country2 = 'India', 'Qatar'
     index_num_1 = list(emission_dict.keys()).index(country1)
    index_num_2 = list(emission_dict.keys()).index(country2)
    # In this task we combined two plots in one and given the label to identify.
    plt.plot(list(map(float, list(emission_dict.values())[0])),
             list(map(float, list(emission_dict.values())[index_num_1])), label=country1)
    plt.plot(list(map(float, list(emission_dict.values())[0])),
             list(map(float, list(emission_dict.values())[index_num_2])), label=country2)
    plt.title("Year vs Emissions in Capita")
    plt.xlabel("Year")
    plt.ylabel("Emissions")
    plt.legend()
    plt.show()
    print()
    def extract_data(country):
        list_len = len(country)
        for length in range(0, list_len):
            # Validating input up to three countries - If there are more then three countries then return false
            if list_len > 3:
                print("ERR: Sorry, at most 3 countries can be entered.", end="\n\n")
                return False
        else:
            # Creating string to write in CSV File
            write_line_csv = list(emission_dict.keys())[0].title(
            ) + "," + ",".join(list(emission_dict.values())[0]) + "\n"
            for num in range(0, len(country)):
                write_line_csv += country[num].title() + "," + ",".join(
                    emission_dict[country[num]]) + "\n"
            # Open CSV in write mode and writing lines to CSV
            with open('Emissions_subset.csv', 'w') as new_file:
                new_file.writelines(write_line_csv)
            # Printing the value in required format
            print(f"Data successfully extracted for countries " + ", ".join(
                country).title() + " saved into file Emissions_subset.csv", end="\n\n")
        return True

    print("A Simple Data Analysis Program")
    print()


    while True:
        '''TODO: input_string = input("Write up to three comma-separated countries for which you want to extract data: ")'''
        input_string = 'India, Oman, Qatar'
        input_country = input_string.split(", ")
        # Calling the Function to validate input
        if not extract_data(input_country):
            continue
        else:
            break

except FileNotFoundError:
    print("File not found....")
except IOError:
    print("Output file can�t be saved")