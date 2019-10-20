import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

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
    while True:
        city = input("Enter the name of the city to analyze (Chicago, New York City or Washington): ")
        city = city.lower()
        if city in cities:
            break
        else:
            print("Invalid input\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the name of the month to filer by (January, February, March, April, May, June). Type 'all' to apply no month filter: ")
        month = month.lower()
        if (month in months) or (month == 'all'):
            break
        else:
            print("Invalid input\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter the name of the day of week to filter by (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday). Type 'all' to apply no day filter: ")
        day = day.lower()
        if (day in days) or (day == 'all'):
            break
        else:
            print("Invalid input\n")

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
    
    #Loading data for the specified city in a Pandas DataFrame
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    #Converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extracting the month and day of the week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    #Filtering by month (if applicable)
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month']==month]
        
    #Filtering by day (if applicable)
    if day != 'all':
        df = df[df['day']==day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most Common Month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print("Most Common Day of Week: ", most_common_day)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    most_common_starthr = df['Start Hour'].mode()[0]
    print("Most Common Start Hour: ", most_common_starthr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combo_station = df.groupby(['Start Station', 'End Station']).count()
    print("Most Frequent Combination of Start Station and End Station: ", frequent_combo_station.idxmax()[0][0], " and ", frequent_combo_station.idxmax()[0][1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/3600
    print("Total Travel Time = ", total_travel_time, "hrs")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/3600
    print("Mean Travel Time = ", mean_travel_time, "hrs")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("\nCounts of user types: ", user_type_count)
    print()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("\nCounts of gender: ", gender_count)
        print()
    else:
        print("\nCounts of gender: No data available for this month\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print("\nEarliest Year of Birth: ", earliest_birth_year)
        print()
    except KeyError:
        print("\nEarliest Year of Birth: No data available for this month\n")
        
    try:
        most_recent_birth_year = df['Birth Year'].max()
        print("\nMost Recent Year of Birth: ", most_recent_birth_year)
        print()
    except KeyError:
        print("\nMost Recent Year of Birth: No data available for this month\n")
        
    try:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("\nMost Common Year of Birth: ", most_common_birth_year)
        print()
    except KeyError:
        print("\nMost Common Year of Birth: No data available for this month\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
