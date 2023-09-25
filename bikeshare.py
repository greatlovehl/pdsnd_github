import time
import pandas as pd
import numpy as np

CITY_DATA = {   
                'chicago': 'chicago.csv',
                'new york city': 'new_york_city.csv',
                'washington': 'washington.csv' }
                
CITIES = [  
            'chicago', 
            'new york city', 
            'washington']
            
MONTHS = [
            'all', 
            'january', 
            'february', 
            'march', 
            'april', 
            'may', 
            'june', 
            'july', 
            'august', 
            'september', 
            'october', 
            'november', 
            'december']
            
DAYS = [
            'all', 
            'monday', 
            'tuesday', 
            'wednesday', 
            'thursday', 
            'friday', 
            'saturday', 
            'sunday']
            
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city name
    while True:
        input_city = input('Please input city name (chicago, new york city, washington): ').lower()
        if input_city in CITIES:
            break
        else:
            print('Invalid data. Please input valid city name (chicago, new york city, washington).')
    
    # get user input for month
    while True:
        input_month = input('Please input month (all, january, february, ..., december): ').lower()
        if input_month in MONTHS:
            break
        else:
            print('Invalid data. Please input valid month (all, january, february, ..., december).')

    # get user input for day
    while True:
        input_day = input('Please input day (all, monday, tuesday, ..., sunday): ').lower()
        if input_day in DAYS:
            break
        else:
            print('Invalid data. Please input valid day (all, monday, tuesday, ..., sunday).')

    print('-'*40)
    return input_city, input_month, input_day


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

    try:
        df = pd.read_csv(CITY_DATA[city])
    except:
        print(f'Can not load data')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # check data month when input not all
    if month != 'all':
        month_data = MONTHS.index(month) - 1
        df = df[df['Start Time'].dt.month == month_data]

    # check data month when input not all
    if day != 'all':
        day_data = DAYS.index(day) - 1
        df = df[df['Start Time'].dt.dayofweek == day_data]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    month_data = df["Start Time"].dt.month.value_counts()
    most_common_month = month_data.idxmax()
    print("The most common month:", most_common_month)
    
    # display the most common day of week
    day_data = df["Start Time"].dt.dayofweek.value_counts()
    most_common_day = day_data.idxmax()

    for key, value in listDayOfWeek.items():
        if value == most_common_day:
            print("The most common day of week:", key)
            break

    # display the most common start hour
    hour_data = df["Start Time"].dt.hour.value_counts()
    most_common_hour = hour_data.idxmax()
    print("The most common hour: ", most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {most_common_start_station}")

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {most_common_end_station}")

    # display most frequent combination of start station and end station trip   
    group_combination = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
    most_frequent = group_combination.loc[group_combination['count'].idxmax()]
    print("Most frequent combination:")
    print("Start station: ", most_frequent['Start Station'])
    print("End station: ", most_frequent['End Station'])
    print("Count: ", most_frequent['count'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time")
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender  
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"\nGender: {gender_counts}")
    else:
        print("\nNo Gender information.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print(f"\nEarliest year of birth: {int(earliest_year)}")
        
        most_recent = df['Birth Year'].max()
        print(f"Most recent year of birth: {int(most_recent)}")
        
        most_common_year_of_birth = df['Birth Year'].mode()[0]             
        print(f"Most common year of birth: {int(most_common_year_of_birth)}")
    else:
        print("\nNo Birth Year information.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Displays 5 lines of raw data from the DataFrame.

    Args:
        df - Pandas DataFrame containing city data
    """
    print('\nDisplays 5 lines of raw data from the DataFrame.')
    num_lines = 5
    total_lines = df.shape[0]

    start_line = 0
    while True:
        print(df.iloc[start_line : start_line + num_lines])
        start_line += num_lines

        if start_line >= total_lines:
            print("\nEnd.")
            break

        show_more = input("\nInvalid data. Please enter only 'yes' or 'no'")
        if show_more.lower() != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print('\nThere is no data for this filter')
        else:
            display_raw_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

