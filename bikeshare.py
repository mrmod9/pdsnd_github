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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = []
    city_list.append('chicago')
    city_list.append('new york city')
    city_list.append('washington') 
    while True:
        city    = input("Enter City Name : chicago | new york city | washington\n").lower()
        if city in city_list:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month    = input("Enter Month : all, january, february, march, april, may, june\n").lower()
        if month in month_list:
            break
        
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    month_list = []
    month_list.append('all')
    month_list.append('january')
    month_list.append('february')
    month_list.append('march')
    month_list.append('april')
    month_list.append('may')
    month_list.append('june')
    while True:
        day    = input("Enter Day : all, monday, tuesday, wednesday, thursday, friday, saturday, sunday\n").lower()
        if day in day_list:
            break


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print ("The most common month :  ", most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print ("The most common day of week :  ", most_common_day)

    # TO DO: display the most common start hour
    df['start_hour']  = df['Start Time'].dt.hour
    most_common_start_hour = df['start_hour'].value_counts().idxmax()
    print ("most common start hour ", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
       
    df['start_station']  = df['Start Station']
    most_common_start_station = df['start_station'].value_counts().idxmax()
    print ("most commonly used start station ", most_common_start_station)

    # TO DO: display most commonly used end station
    
    df['end_station']  = df['End Station']
    most_common_end_station = df['end_station'].value_counts().idxmax()
    print ("most commonly used end station ", most_common_end_station)
    


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination_start_end_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print ("most frequent combination of start station and end station : ", most_frequent_combination_start_end_station )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['start_station']  = df['Start Station']
    df['end_station']  = df['End Station']
    df['trip_duration']  = df['Trip Duration']
    total_travel_time = df.groupby(['start_station','end_station'])['trip_duration'].sum()
    jmp = 5
    print (total_travel_time[:jmp])
    while True:
            next    = input ("do you want to display the next Total Travel Time\n").lower()
            if next == "no":
                break
            elif next == "yes" :
                jmp+=5
                print (total_travel_time[:jmp])
        #print ("Total Travel Time :\n", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df.groupby(['start_station','end_station'])['trip_duration'].mean()
    jmp = 5
    print (mean_travel_time[:jmp])
    while True:
            next    = input ("do you want to display the next Mean Travel Time\n").lower()
            if next == "no":
                break
            elif next == "yes" :
                jmp+=5
                print (mean_travel_time[:jmp])
    #print ("Mean Travel Time :\n", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df['ut'] = df['User Type']
    user_types = df['ut'].value_counts().reset_index()
    print ("Count of user types :", user_types)

    # TO DO: Display counts of gender
    df['gender'] = df['Gender']
    gender = df['gender'].value_counts().reset_index()
    print ("Count of gender :", gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    df['birth_year'] = df['Birth Year']
    earliest_year = int(df['birth_year'].min())
    recent_year = int(df['birth_year'].max())
    common_year = int(df['birth_year'].value_counts().idxmax())
    print ("earliest year is %d \nmost recent year is %d \nmost common year is %d" % (earliest_year, recent_year, common_year))

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
