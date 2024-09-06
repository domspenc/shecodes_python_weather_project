import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C" # sets a 'not-to-be-changed' variable called <DEGREE_SYMBOL> to the code version of the degree symbol, to use later

def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}" # passes a temp argument into the <format_temperature> function, then adds the degree symbol from above, and stores it in the <format_temperature> function

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
    store_iso_date = datetime.fromisoformat(iso_string) # pass argument <iso_string> into .fromisoformat function from within <datetime> python library and store it in <store_iso_date> variable
    human_readable_date = store_iso_date.strftime('%A %d %B %Y') # take <store_iso_date> variable and pass it into .strftime function, using correct format codes
    return human_readable_date # store the result in the <convert_date> function

# CODE TO TEST
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
    return round((float(temp_in_fahrenheit) - 32) * 5/9, 1) # convert argument <temp_in_fahrenheit> to a float, perform the equation on that number then store the rounded number in the <convert_f_to_c> function (notice the brackets to identify what happens when!)

# CODE TO TEST
# test = convert_f_to_c(-10.0)
# print(test)

"""Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

pass


def calculate_mean(weather_data):
    try:
        return float((sum(weather_data) / len(weather_data))) # try to calculate the mean with the assumption that all data is numeric
    except TypeError:
        weather_data_converted = [float(data) for data in weather_data] # if a TypeError occurs (aka data is not numeric), convert each element to a float (using list comprehensions)...
        return sum(weather_data_converted) / len(weather_data_converted) # ...then calculate the mean and store the result in the <calculate_mean> function

# CODE TO TEST  
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
        csv_file_data = csv.reader(csv_file) # use <csv.reader> to read data in csv file
        next(csv_file_data) # skips the header row
  
        final_list = [] # create an empty list to store our eventual newly formatted list in
        for data in csv_file_data: # for loop to read through each row in the csv file
                if data != []: # if statement to catch only lines that ARE NOT (!=) empty
                    date = data[0] # accessing the date string using 0 index and storing in <date> variable
                    temp_one = int(data[1]) # accessing the min_temp string using 1 index, converting it to an integer (because the for loop will return everything as a string!) and storing in <temp_one> variable
                    temp_two = int(data[2]) # doing the same ^ for max_temp, but finding the data as the third value (index 2)
                    final_list.append([date, temp_one, temp_two]) # adding to our empty list <final_list> using the data within the variables, and labeling each column
        return final_list # store the result in the <load_data_from_csv> function

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
    
    # start a for loop using range(len(weather_data)), to iterate over the indexes of the list (0, 1, 2, etc.). this means I can access and modify elements directly in the list using weather_data[i].
    # if I use a for loop directly on the list like <for num in weather_data>, I can get each element (<num>), but I can't modify the original list directly because <num> is just a copy of the value, not a reference to the actual list element.
    for i in range(len(weather_data)):
        if not isinstance(weather_data[i], int): # <isinstance> looks for instances that are NOT a specific data type, in this case not 'int'
            weather_data[i] = float(weather_data[i]) # find any other data types, convert them to floats then store that value in the current iteration of <weather_data> using the <weather_data[i]> variable
    
    min_value = weather_data[0]  # set the minimum value and store it in the <min_value> variable
    min_index = 0  # set the index of the minimum value and store it in the <min_index> variable
    
    # loop through the list to find the minimum value and its last occurrence
    for index, num in enumerate(weather_data): # start a for loop to iterate through the data in <weather_data>, and use enumerate to find the min value AND its index
        if num <= min_value:  # find the last occurrence of the min value
            min_value = num # store the final min value in a variable called <min_value>
            min_index = index # store the associated index in a variable called <min_index>
    
    return min_value, min_index # store these values in the <find_min> function!

# CODE TO TEST
# test = find_min([10.4, 14.5, 12.9, 8.9, 10.5, 11.7])
# print(test)

"""Calculates the minimum value in a list of numbers.

Args:
    weather_data: A list of numbers.
Returns:
    The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
"""
pass


# code below is exactly the same as <min_value>, read above for comments
def find_max(weather_data):
    if weather_data == []:
        return ()
    
    for i in range(len(weather_data)):
        if isinstance(weather_data[i], str):
            weather_data[i] = float(weather_data[i])
    
    max_value = weather_data[0]  
    max_index = 0  
    
    for index, num in enumerate(weather_data):
        if num >= max_value:
            max_value = num
            max_index = index
    
    return max_value, max_index

# CODE TO TEST
# test = find_max([10.4, 14.5, 12.9, 8.9, 10.5, 11.7])
# print(test)

"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
pass


def generate_summary(weather_data):
        min_temps = [] # create an empty list called <min_temps>, to use later when calculating mean
        max_temps = [] # same as above ^
        for i in range(len(weather_data)): # for loop to iterate over indices in the <weather_data> list of lists
            min_temps.append(weather_data[i][1]) # find the min temps in <weather_data[i][1]>; this takes the data from each iteration that is found as the second value (index 1)
            max_temps.append(weather_data[i][2]) # find the min temps in <weather_data[i][2]>; this takes the data from each iteration that is found as the third value (index 2)
        
        temp_list = min_temps + max_temps # concatenate the <min_temps> and <max_temps> lists so I can find the true min value (I do this because if the temps are swapped between columns, I need to find the minimum value regardless of which column it's in [see example two!]) then store the final value in the <temps_list> variable
        min_temp = find_min(temp_list)[0] # find the min value of <temp_list> then store it in the <min_temp> variable. I need to specify the location using [0] as <temp_list> is a list!
        max_temp = find_max(temp_list)[0] # find the max value of <temp_list> then store it in the <max_temp> variable

        for data in weather_data: # create for loop to iterate over the lists in <weather_data>
            print(data) 
            if min_temp == data[1] or min_temp == data[2]: # compare the value stored in <min_temp> with the second and third values (indexes 1 and 2) in <weather_data>  
                min_date = convert_date(data[0]) # if it's a match, store the associated date value (index 0) in <weather_data> in a variable called <min_date>
            elif max_temp == data[1] or max_temp == data[2]: # do the same as the above for the max temp and max date
                max_date = convert_date(data[0])

        av_low = format_temperature(convert_f_to_c(calculate_mean(min_temps))) # calculate the mean of all the values in the <min_temps> list, then use the functions from above to convert the number to celcius, then format it to include the degree symbol! I then store it in the <av_low> variable
        av_high = format_temperature(convert_f_to_c(calculate_mean(max_temps))) # same as above ^ for <av_high> variable
        min_temp = format_temperature(convert_f_to_c(min_temp)) # convert the value in <min_temp> to celcius, then format it to include the degree symbol and store it in the <min_temp> variable
        max_temp = format_temperature(convert_f_to_c(max_temp)) # same as above ^ for <max_temp> variable
        
        return (f"{len(weather_data)} Day Overview\n" # this is the final section, using the variables to create a summary!
                f"  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n"
                f"  The highest temperature will be {max_temp}, and will occur on {max_date}.\n"
                f"  The average low this week is {av_low}.\n"
                f"  The average high this week is {av_high}.\n"
                )

# CODE TO TEST
# example_one = [
#             ["2020-06-19T07:00:00+08:00", 47, 46],
#             ["2020-06-20T07:00:00+08:00", 51, 67],
#             ["2020-06-21T07:00:00+08:00", 58, 72],
#             ["2020-06-22T07:00:00+08:00", 59, 71],
#             ["2020-06-23T07:00:00+08:00", 52, 71],
#             ["2020-06-24T07:00:00+08:00", 52, 67],
#             ["2020-06-25T07:00:00+08:00", 48, 66],
#             ["2020-06-26T07:00:00+08:00", 53, 66]
#         ]
# test = generate_summary(example_one)
# print(test)

"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
pass


def generate_daily_summary(weather_data):
        daily_summaries = [] # create an empty list called <daily_summaries>, to store each iteration of our summary below into a list

        for i in range(len(weather_data)): # for loop to iterate over indices in the <weather_data> list of lists
            date = convert_date(weather_data[i][0]) # find the dates in <weather_data[i][0]>; this takes the data from each iteration that is found as the first value (index 0)
            min_temp = format_temperature(convert_f_to_c(weather_data[i][1])) # find the temperatures in <weather_data[i][1]>; this takes the data from each iteration that is found as the second value (index 1), converts it to celcius and formats it to include the degree symbol, then stores it in the <min_temp> variable
            max_temp = format_temperature(convert_f_to_c(weather_data[i][2])) # same as above but takes the data from each iteration that is found as the third value (index 2) and stores it in the <max_temp> variable

            daily_summary = ( # create the daily summary for each iteration within the loop, using the data stored in the above variables
                f"---- {date} ----\n"
                f"  Minimum Temperature: {min_temp}\n"
                f"  Maximum Temperature: {max_temp}\n"
            )

            daily_summaries.append(daily_summary) # adds each daily summary to the <daily_summaries> list

        return "\n".join(daily_summaries) + "\n" # joins each of these summaries together with an <\n> space between them, and stores this in the <generate_daily_summary> function


# CODE TO TEST
# example_one = [
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]
# test = generate_daily_summary(example_one)
# print(test)

"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
pass
