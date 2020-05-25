import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

VALID_CITIES = ['chicago','new york city','washington']

VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

VALID_DAYS = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

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
        try:
            city = str(input('For which city would you like to see data Chicago, New York City or Washington?\n'))
            city = city.lower()          
            if city in VALID_CITIES:
                break
            else:
                print('Invalid city name! Try again')
        except KeyboardInterrupt:
            print('No input taken')
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('For which month would you like to see data ? January,February,March,April,May,June. Type \'all\' to see data for all mentioned months\n')
            month = month.lower()
            if month == 'all' or month in VALID_MONTHS:
                break
            else:
                print('Invalid month! Try again')
        except KeyboardInterrupt:
            print('No input taken')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('For which day would you like to see data ? Sunday,Monday.....etc. Type \'all\' to see data for all days\n')
            day = day.lower()  
            if day == 'all' or day in VALID_DAYS:
                break
            else:
                print('Invalid day! Try again')
        except KeyboardInterrupt:
            print('No input taken')

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = VALID_MONTHS.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nMost common month of travel: ', VALID_MONTHS[common_month-1].title())

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nMost common day of week of travel: ', common_day)
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('\nMost common start hour for travel: ', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts()
    print('\nMost commonly used start station: {} Count: {}'.format(common_start_station.idxmax(), common_start_station.max()))
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts()
    print('\nMost commonly used end station: {} Count: {}'.format(common_end_station.idxmax(), common_end_station.max()))
    # TO DO: display most frequent combination of start station and end station trip
    freq = df.groupby('Start Station')['End Station'].value_counts().idxmax()
    freq_count = df.groupby('Start Station')['End Station'].value_counts().max()
    print('\nMost frequent trips starts from {} station and ends at {} station. Count: {}'.format(freq[0],freq[1],freq_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time: {} seconds'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: {} seconds'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('\nThere are {} Subscribers and {} Customers'.format(user_type_count['Subscriber'],user_type_count['Customer']))
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('\nThere are {} Males and {} Females'.format(gender_count['Male'],gender_count['Female']))
    else:
        print('\nThere is no gender info available')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarliest birth year: ',int(earliest_birth_year))
        print('\nMost recent birth year: ',int(most_recent_birth_year))
        print('\nMost common birth year: ',int(most_common_birth_year))
    else:
        print('\nThere is no Birth Year info available')
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
        lines = []
        with open('chicago.csv') as f:
            for line in f:
                lines.append(line.strip())
        start = 1
        end = 6
        while True:
            raw_data = input('\nWould you like to see individual trip data \'yes\' or \'no\'?\n')
            if raw_data.lower() == 'yes':
                temp = lines[start:end]
                for i in range(5):
                    print('{',temp[i],'}')
                start = end
                end = end + 5
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
