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
    while True:

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input('Which city would you like to look at? Please enter Washington, Chicago, or New York City: ').lower()
        while True:
            if city == 'chicago':
                break
            elif city == 'new york city':
                break
            elif city == 'washington':
                break
            else:
                city = input("Sorry, that doesn't look like one of the possible cities! Please enter your answer again: ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Would you like to look at a specific month from January to June? Enter the first three letters of the month. If not, enter "all": ').lower()
        while True:
            if month == 'jan' or month == 'feb' or month == 'mar' or month == 'apr' or month == 'may' or month == 'jun' or month == 'jul' or month == 'aug' or month == 'sep' or month == 'oct' or month == 'nov' or month == 'dec' or month == 'all':
                break
            else:
                    month = input('Sorry! Please re-enter the first three letters of the month you would like to look at. If none, please enter "all": ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Would you like to look at a specific day of the week? If not, enter 'none': ").lower()
        while True:
            if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'none':
                break
            else:
                day = input('Sorry! Please re-enter the day of the week you would like to look at. If none, please enter "none": ').lower()

    # TO DO: Confirming user input for city, month, and day
        print('It looks like you want to look at:', city, month, day)
        confirm_input = input("Is this correct? Y/N: ")
        if confirm_input.lower() == 'y':
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

    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        month = months.index(month) + 1

        df = df[df['Month'] == month]

    if day != 'none':
        df = df[df['Day of Week'] == day.title()]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    print('Most Popular Month: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print('Most Popular Day of Week: ', popular_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Hour'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station: ', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Commonly Used End Station: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip

    df['Start_End_Combination'] = df['Start Station'] + ' to ' + df['End Station']

    start_end_freq = df['Start_End_Combination'].mode()[0]

    print('Most Frequent Combination of Start and End Station: ', start_end_freq)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    print('Total Travel Time in Minutes: ', total_time / 60)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time in Minutes: ', mean_travel_time / 60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    print('Types of Users: ', user_types)

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:

        df['Gender'] = df['Gender'].dropna(axis = 0)

        user_gender = df['Gender'].value_counts()

        print('User Gender: ', user_gender)

    else:
        print('Gender Data Unavailable.')



    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:

        df['Birth Year'] = df['Birth Year'].dropna(axis = 0)

        earliest_yob = df['Birth Year'].min()

        most_recent_yob = df['Birth Year'].max()

        most_common_yob = df['Birth Year'].mode()[0]

        print('Earliest Year of Birth: ', earliest_yob)
        print('Most Recent Year of Birth: ', most_recent_yob)
        print('Most Common Year of Birth: ', most_common_yob)

    else:
        print('Birth Year Data Unavailable.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_trip(df):

    view_data = input('Would you like to see 5 rows of trip data? Y/N: ').lower()
    start_loc = 0
    while True:
        if view_data == 'n':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('Would you like to see the next 5 rows of trip data? Y/N: ').lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
