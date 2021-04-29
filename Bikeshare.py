import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
 
       # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
 
    city_selection = input('To view the available bikeshare data, kindly type:\n The letter (c) for\
        Chicago\n The letter (n) for New York City\n The letter (w) for Washington\n ').lower()
    
    while True:
        try:
            city_selection = input('To view the available bikeshare data, kindly type:\n The letter (c) for\n Chicago\n The letter (n) for New York City\n The letter (w) for Washington\n ').lower()
            city_ch_list = ["c", "n", "w"]
            if city_selection in city_ch_list:
                break
        except KeyboardInterrupt:
            print('\nNo input given')
        else:
            print('Invalid month choice!')
    
    city_selections = {"c": "chicago", "n": "newyork city", "w": "washington"}
    if city_selection in city_selections.keys():
        city = city_selections[city_selection]
    
        # get user input for month (all, january, february, ... , june)
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december', 'all']
    month = input('\n\nTo filter by {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:').format(city.title()).lower()
    while month not in months:
        print('That is an invalid choice, please type a valid month name or all')
        month = input('\n\nTo filter by {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:').format(city.title()).lower()
    
        # get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input('\n\nTo filter by a particular day, please type the day name or all for not filtering by day: \n-saturday \n-sunday\n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-all')
    while day not in days:
        print('That is an invalid choise, please type a valid day name or all')
        day = input('\n\nTo filter by a particular day, please type the day name or all for not filtering by day: \n-saturday \n-sunday\n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-all')
        
        print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']
       month = months.index(month) +1
       df = df[df['month'] == month]
    
    if day != 'all':
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        df = df[df['day_of_week'] == day.title()]

    return df

#required statstics 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df['month'].mode()[0])
    print(df['day_of_week'].mode()[0])
    print(df['hour'].mode()[0])

    # display the most common month


    # display the most common day of week


    # display the most common start hour

# %s for string 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print(df['Start Station'].mode()[0])
    print(df['End Station'].mode()[0])
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combination = df['Start To End'].mode()[0]
    print(combination)

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_duration = df['Trip Duration'].sum()
    print(total_duration)
    average_duration = df['Trip Duration'].mean()
    print(average_duration)

    # display total travel time


    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(df['User Type'].value_counts())
    try:
        print(df['Gender'].value_counts())
    except:
        print('\n There is no gender column in this file')
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f'\n The earliest year of birth: {earliest} \n\n The most recent year of birth: {recent} \n\n The most common year of birth: {common_year}')
    except:
        print('\n There is no birth year details in this file')
    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

#Function to display the data frame itself as per user request
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*80)



#final step
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


