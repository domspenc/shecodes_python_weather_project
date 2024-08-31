import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}"

    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    
# test = format_temperature('20')
# print(test)

#-------------------------------------------------

def convert_date(iso_string):
    store_iso_date = datetime.fromisoformat(iso_string)
    human_readable_date = store_iso_date.strftime('%A %d %B %Y')
    return human_readable_date

# result = convert_date('2020-02-01T07:00:00+08:00')
# print(result)

"""Converts an ISO formatted date into a human-readable format.

        Args:
            iso_string: An ISO date string.
        Returns:
            A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
        """
pass


def convert_f_to_c(temp_in_fahrenheit):
    return round((float(temp_in_fahrenheit) - 32) * 5/9, 1)

test = convert_f_to_c(-10.0)
print(test)

"""Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

pass


def calculate_mean(weather_data):
    try:
        # Try to calculate the mean with the assumption that all data is numeric
        return float((sum(weather_data) / len(weather_data)))
    except TypeError:
        # If a TypeError occurs, convert each element to a float
        weather_data_converted = [float(data) for data in weather_data]
        return sum(weather_data_converted) / len(weather_data_converted)
    
        
# test = calculate_mean([49, 57, 56, 55, 53])
# print(test)

"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
pass

def load_data_from_csv(csv_file):
    # open the csv file using csv.reader
    # i tried using readlines() but that returns another list which complicated my code!
    with open(csv_file) as csv_file:
        csv_file_data = csv.reader(csv_file)
        # skips the header row
        next(csv_file_data)
  
        # create an empty list to store our eventual newly formatted list in
        final_list = []
        # for loop to read through the csv file
        for data in csv_file_data:
                # if statement to catch only lines that ARE NOT (!=) empty
                if data != []:
                    # accessing the date string using 0 index and storing in variable
                    date = data[0]
                    # accessing the min_temp string using 1 index, converting it to an integer (because the for loop will return everything as a string!) and storing in variable
                    temp_one = int(data[1])
                    # doing the same for max_temp
                    temp_two = int(data[2])
                    # adding to our empty list using the data within the variables, and labeling each column
                    final_list.append([date, temp_one, temp_two])
        return final_list
    
# MY ORIGINAL CODE - which returns the correct result(!!), but still creates an error (?) for this specific test for whatever reason?!
# def load_data_from_csv(csv_file):
#     # open the csv file using readlines() function - this returns a list of strings within another list
#     with open(csv_file) as csv_file:
#         csv_file_data = csv_file.readlines()
#     # create an empty list to store our eventual newly formatted list in
#     final_list = []
#     # for loop to read through the csv file, from every row after the 1st one (hence [1:])
#     for data in csv_file_data[1:]:
#             # split columns by ',' with split() and remove any trailing whitespace with strip()
#             column = data.strip().split(',')
#             # accessing the date string using 0 index and storing in variable
#             date = column[0]
#             # accessing the min_temp string using 1 index, converting it to an integer (because the for loop will return everything as a string!) and storing in variable
#             temp_one = int(column[1])
#             # doing the same for max_temp
#             temp_two = int(column[2])
#             # adding to our empty list using the data within the variables, and labeling each column
#             final_list.append([date, temp_one, temp_two])
#     return final_list

# test = load_data_from_csv('tests/data/example_one.csv') 
# print(test)


"""Reads a csv file and stores the data in a list.

Args:
    csv_file: a string representing the file path to a csv file.
Returns:
    A list of lists, where each sublist is a (non-empty) line in the csv file.
"""
pass


def find_min(weather_data):
    if weather_data == []:
        return ()
    
    # Convert all elements to integers (if needed) using a for loop
    # By using range(len(weather_data)), we're iterating over the indexes of the list (0, 1, 2, etc.). This allows us to access and modify elements directly in the list using weather_data[i].
    # If we use a for loop directly on the list like for num in weather_data, we get each element (num), but we cannot modify the original list directly because num is just a copy of the value, not a reference to the actual list element.
    for i in range(len(weather_data)):
        if not isinstance(weather_data[i], int):
            weather_data[i] = float(weather_data[i])
    
    min_value = weather_data[0]  # Initialize the minimum value
    min_index = 0  # Initialize the index of the minimum value
    
    # Loop through the list to find the minimum value and its last occurrence
    for index, num in enumerate(weather_data):
        if num <= min_value:  # Find the last occurrence of the minimum
            min_value = num
            min_index = index
    
    return min_value, min_index

# test = find_min([10.4, 14.5, 12.9, 8.9, 10.5, 11.7])
# print(test)


    
"""Calculates the minimum value in a list of numbers.

Args:
    weather_data: A list of numbers.
Returns:
    The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
"""
pass


def find_max(weather_data):
    if weather_data == []:
        return ()
    
    # Convert all elements to integers (if needed) using a for loop
    for i in range(len(weather_data)):
        if isinstance(weather_data[i], str):
            weather_data[i] = float(weather_data[i])
    
    max_value = weather_data[0]  # Initialize the minimum value
    max_index = 0  # Initialize the index of the minimum value
    
    # Loop through the list to find the minimum value and its last occurrence
    for index, num in enumerate(weather_data):
        if num >= max_value:  # Find the last occurrence of the minimum
            max_value = num
            max_index = index
    
    return max_value, max_index

test = find_max([10.4, 14.5, 12.9, 8.9, 10.5, 11.7])
print(test)

"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
pass


def generate_summary(weather_data):
        min_temps = []
        max_temps = []
        for i in range(len(weather_data)):
            min_temps.append(weather_data[i][1])
            max_temps.append(weather_data[i][2])
        
        temp_list = min_temps + max_temps
        min_temp = find_min(temp_list)[0]
        max_temp = find_max(temp_list)[0]

        for data in weather_data:
            if min_temp == data[1] or min_temp == data[2]:
                min_date = convert_date(data[0])
                print(min_date)
            elif max_temp == data[1] or max_temp == data[2]:
                max_date = convert_date(data[0])

        av_low = format_temperature(convert_f_to_c(calculate_mean(min_temps)))
        av_high = format_temperature(convert_f_to_c(calculate_mean(max_temps)))
        min_temp = format_temperature(convert_f_to_c(min_temp))
        max_temp = format_temperature(convert_f_to_c(max_temp))
        
        return (f"{len(weather_data)} Day Overview\n"
                f"  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n"
                f"  The highest temperature will be {max_temp}, and will occur on {max_date}.\n"
                f"  The average low this week is {av_low}.\n"
                f"  The average high this week is {av_high}.\n"
                )

example_one = [
            ["2020-06-19T07:00:00+08:00", 47, 46],
            ["2020-06-20T07:00:00+08:00", 51, 67],
            ["2020-06-21T07:00:00+08:00", 58, 72],
            ["2020-06-22T07:00:00+08:00", 59, 71],
            ["2020-06-23T07:00:00+08:00", 52, 71],
            ["2020-06-24T07:00:00+08:00", 52, 67],
            ["2020-06-25T07:00:00+08:00", 48, 66],
            ["2020-06-26T07:00:00+08:00", 53, 66]
        ]

test = generate_summary(example_one)
print(test)


            # if isinstance(weather_data[i][0], str):
            #     print(weather_data[i][0])
            #     date.append(convert_date(weather_data[i][0]))

        # for i in weather_data:
        #     print(i)
            # min_temp.append(min(weather_data[i]))
            # min_temp.append(weather_data[i][1])
            # print(min_temp)


"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
