import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

DAY_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']

"""                                           $"   *.
              d$$$$$$$P"                  $    J
                  ^$.                     4r  "
                  d"b                    .db
                 P   $                  e" $
        ..ec.. ."     *.              zP   $.zec..
    .^        3*b.     *.           .P" .@"4F      "4
  ."         d"  ^b.    *c        .$"  d"   $         %
 /          P      $.    "c      d"   @     3r         3
4        .eE........$r===e$$$$eeP    J       *..        b
$       $$$$$       $   4$$$$$$$     F       d$$$.      4
$       $$$$$       $   4$$$$$$$     L       *$$$"      4
4         "      ""3P ===$$$$$$"     3                  P
 *                 $       $$$        b                J
  |             .P                    %.             @
    %.         z*"                      ^%.        .r"
       "*==*""                             ^"*==*"" """

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_city():
    print('Hello! Let\'s explore some US bikeshare data!\nIn this application we have bikeshare data from Jan-Jun of 2017 for Chicago, Washington, and New York City.')
    city = ""
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input("Would you like to see data for 'Chicago', 'New York City', or 'Washington'):")
        if city.lower() == 'chicago':
            print("Great, let's take a look at the Chicago data!")
            print('-'*40)
            return 'chicago'
        elif city.lower() == 'new york city':
            print("Great, let's take a look at the New York City data!")
            print('-'*40)
            return 'new york city'
        elif city.lower() == 'washington':
            print("Great, let's take a look at the Washington data!")
            print('-'*40)
            return 'washington'
        else:
            print("That's not a city we have data for, Please input either Chicago, New York, or Washington.")
    return city

    if city.lower() in ["chicago", "new_york", "washington"]:
        return city.lower()
    else:
        print("That's not a city we have data for, Please input either Chicago, New York, or Washington.")

# TO DO: get user input for month (all, january, february, ... , june)
def get_month():
    print("Ok now let's filter the data for the desired month.")
    month = ""
    while month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input("Which month of data would you like to examine 'January', 'February', 'March', 'April', 'May', 'June' or 'All'?:")
        if month.lower() == 'all':
            print("Great, let's examine data from January through June!")
            print('-'*40)
            return 'all'
        elif month.lower() == 'january':
            print("Great, let's examine data from January!")
            print('-'*40)
            return 'january'
        elif month.lower() == 'feburary':
            print("Great, let's examine data from Feburary!")
            print('-'*40)
            return 'feburary'
        elif month.lower() == 'march':
            print("Great, let's examine data from March!")
            print('-'*40)
            return 'march'
        elif month.lower() == 'april':
            print("Great, let's examine data from April!")
            print('-'*40)
            return 'april'
        elif month.lower() == 'may':
            print("Great, let's examine data from May!")
            print('-'*40)
            return 'may'
        elif month.lower() == 'june':
            print("Great, let's examine data from June!")
            print('-'*40)
            return 'june'
        else:
            print("That\'s not a month we have data for, Please input either 'January', 'February', 'March', 'April', 'May', 'June' or 'All'.")
    return month

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
def get_day():
    print("Ok now let's filter the data for the desired day")
    day = ""
    while day not in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']:
        day = input("Which day of the week:'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' or 'All'")
        if day == 'All':
            print("Great, let's see all the data!")
            print('-'*40)
            return 'all'
        elif day == 'Sunday':
            print("Great, let's examine data from Sunday!")
            print('-'*40)
            return 'sunday'
        elif day == 'Monday':
            print("Great, let's examine data from Monday!")
            print('-'*40)
            return 'monday'
        elif day == 'Tuesday':
            print("Great, let's examine data from Tuesday!")
            print('-'*40)
            return 'tuesday'
        elif day == 'Wednesday':
            print("Great, let's examine data from Wednesday!")
            print('-'*40)
            return 'wednesday'
        elif day == 'Thursday':
            print("Great, let's examine data from Thursday!")
            print('-'*40)
            return 'thursday'
        elif day == 'Friday':
            print("Great, let's examine data from Friday!")
            print('-'*40)
            return 'friday'
        elif day == 'Saturday':
            print("Great, let's examine data from Saturday!")
            print('-'*40)
            return 'saturday'
        else:
            print("")
    return day
    print('-'*40)

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

    # TO DO load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', MONTHS[popular_month-1])

    # TO DO: display the most common day of week
    # extract day of day ofweek from the Start Time column to create an day_of_week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # find the most popular day of week
    popular_day_of_week = df['month'].mode()[0]
    print('Most Popular Start Day of Week:', DAY_WEEK[popular_day_of_week])

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)
    # TO DO: display top 10 most commonly used start stations with associated trip counts
    start_station_counts = df.groupby('Start Station')['Start Station'].count()
    sorted_start_stations = start_station_counts.sort_values(ascending=False)
    print('\nTop 10 Most Popular Start Stations & Number of Trips:\n', sorted_start_stations.nlargest(10))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_end_station)
    # TO DO: display top 10 most commonly used end stations with associated trip counts
    end_station_counts = df.groupby('End Station')['End Station'].count()
    sorted_end_stations = end_station_counts.sort_values(ascending=False)
    print('\nTop 10 Most Popular End Stations & Number of Trips:\n', sorted_end_stations.nlargest(10))


    # TO DO: display most frequent combination of start station and end station trip
    df['Start & End Station Combo'] = df['Start Station']+' '+df['End Station']
    popular_station_combo = df['Start & End Station Combo'].mode()[0]
    print('\nMost Popular Station Combo:', popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])


    df['Trip Time'] = df['End Time']-df['Start Time']
    total_trip_time = df['Trip Time'].sum()
    print('The Total Trip Time:', total_trip_time)

    # TO DO: display mean travel time

    average_trip_time = df['Trip Time'].mean()
    print('\nThe Average Trip Time:', average_trip_time, 'mins')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('User Type Counts:\n', user_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('\nUser Gender Counts:\n', gender_counts)
    except KeyError:
        print('\nGender Types:\nNo user gender data for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Birth Year of User:\n', int(earliest_birth_year))
    except KeyError:
        print('\nBirth Year:\nNo birth year data for this city.')

    try:
        latest_birth_year = df['Birth Year'].max()
        print('Most Recent Birth Year of User:\n', int(latest_birth_year))
    except KeyError:
        print('\nBirth Year:\nNo birth year data for this city.')

    try:
        common_birth_year = df['Birth Year'].mode()
        print('Most Common Birth Year of User:\n', int(common_birth_year))
    except KeyError:
        print('\nBirth Year:\nNo birth year data for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):
    """TO DO Display raw data upon request by the user in this manner:
    Script should prompt the user if they want to see 5 lines of raw data,
    display that data if the answer is 'yes', and continue these prompts and
    displays until the user says 'no'."""

    show_data = input("Would you like to see 5 rows of raw data ('Yes' or 'No')?")

    first_display_row = 0
    last_display_row = 5

    # TO DO if user answers yes, display 5 rows of data until user says no
    if show_data.lower() == 'yes':
        print("Awesome, let's take a look at some raw data!")
        print(df.iloc[first_display_row:last_display_row])
        first_display_row += 5
        last_display_row += 5
        return display_raw(df)
    elif show_data.lower() == 'no':
        print("Thank you for exploring this program!")
    else:
        print("Sorry, I don't understand your response, please answer 'Yes' or 'No'.")
        return display_raw(df)


def main():

    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
