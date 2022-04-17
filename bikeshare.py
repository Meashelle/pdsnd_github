import time
import pandas as pd
import numpy as np
import collections

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city_option = ["chicago", "new york", "washington"]
    city = input("What city would you like to see data from? choose between Chicago, New York, and Washington \n").lower()
    
    while city not in city_option:
        
        print('The input you provided is invalid, Kindly look out for your spelling or any other source')
        city = input("What city would you like to see data from? choose between Chicago, New York, and Washington \n").lower()
         
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_option = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "all"]
    month = input("Enter month between January and December or all to select all the available months \n").lower()
    while month not in month_option:
        
        print('The input you provided is invalid, Kindly look out for your spelling or any other source')
        month = input("Enter month between January and December or all to select all the available months \n").lower()      
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    weekday_option = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    day = input("Enter month between sunday and saturday \n").lower()
    while day not in weekday_option:
        
        print('The input you provided is invalid, Kindly look out for your spelling or any other source')
        day = input("Enter month between sunday and saturday \n").lower()
        
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
    df_data = pd.read_csv(CITY_DATA[city])
    df_data['Start Time'] = pd.to_datetime(df_data['Start Time'])

    weekday_ = df_data['Start Time'].dt.day_name().str.lower()
    month_ = df_data['Start Time'].dt.month_name().str.lower()
    hour_ = df_data['Start Time'].dt.hour
    df_data['Weekday'], df_data['Month'], df_data['Hour'] = weekday_, month_, hour_
    
    if month == 'all':
        df = df_data[df_data['Weekday'] == day]
    else:
        df = df_data[(df_data['Month'] == month) & (df_data['Weekday'] == day)]
    
    #df = print(data)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is", df['Month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of the week is", df['Weekday'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour is", df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most common end station is", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    answer = df.groupby('Start Station')['End Station'].value_counts().idxmax()
    print("The most frequent combination of start and end stations are %s and %s" %(answer[0], answer[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Duration:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Average Duration", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, month):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    countedUser = collections.Counter(df['User Type'])
    for key in countedUser:
        print(f"%s: %s counts\n" %(key, countedUser[key]))

    # TO DO: Display counts of gender
    gend_ = 'Gender'
    
    if gend_ in df:
        counted_ = collections.Counter(df["Gender"])
        for key in counted_:    
            print(f"%s: %s counts\n" %(key, counted_[key]))  
    else:
        print ("Gender stats cannot be calculated because Gender does not appear in the data frame") 
           
    # TO DO: Display earliest, most recent, and most common year of birth
    birthYear = 'Birth Year'
    
    if birthYear in df:
        x = df['Birth Year'].min()
        y = df['Birth Year'].max()
        z = df['Birth Year'].mode()
        print('Earliest year of birth:', x, "\n Most recent year of birth:", y, "\n Most common year of birth:", z)
    else:
        print ("Birth year stats cannot be calculated because Birth year does not appear in the data frame")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of of individual trip data? Enter yes or no  ").lower()
    start_loc = 0
    while(view_data == 'yes'):
        if (start_loc <= df.size):
            print(df[start_loc:start_loc + 5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else:
            print("We have exhausted the available data")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, month)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
