import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Month_Lookup = {"january":31,
                "february":28,
                "march":31,
                "april":30,
                "may":31,
                "june":30}


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

    flag= True
    while flag:
        city = str(input('Enter the city you want to see the data for: chicago, washington, new york city?: ')).lower()
        for (key, value) in set(CITY_DATA.items()):
            if key ==city:
                flag = False
                break
        if flag:
            print('Invalid Input')
            
    month = -1 
    day = -1
    filters = str(input("would you like to filter the data by month, day, both or none?: "))
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    if filters == 'month':
        flag= True
        while flag:
            month = str(input("enter the month you want to explore the data for? January, February, March, April, May, June: "))
            month=month.lower()
            for (key, value) in set(Month_Lookup.items()):
                if key ==month:
                    flag = False
                    break
            if flag:
                print('Invalid Month Name, please Input amongst the listed Months')
        
    elif filters == 'day':
        while True:
            day = int(input("which day? Please give response as an Integer: "))
            if day >=1 and day <=31:
                break
            else:
                print('Invalid Day, please Input Day from 1 to 31')
                
    elif filters == 'both':
        flag= True
        while flag:
            month = str(input("enter the month you want to explore the data for? January, February, March, April, May, June: ")).lower()
            for (key, value) in set(Month_Lookup.items()):
                if key ==month:
                    flag = False
                    break
            if flag:
                print('Invalid Month Name, please Input amongst the listed Months')
        
        flag= True
        while flag:
            day = int(input("which day? Please give response as an Integer: "))
            for (key, value) in set(Month_Lookup.items()):
                if key ==month and day<= value and day >=1:
                    flag = False
                    break
            if flag:
                print('Invalid Day Range for the Month Selected')    
    else:
        filters = 'none'
   
    print('-'*40)
    return filters,city, month, day

def get_data(city):
    for (key, value) in set(CITY_DATA.items()):
        #print(key, city)
        if key ==city:
            df = pd.read_csv(value)
            return df
    
def load_data(filters, city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df= get_data(city)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month !=-1:
        df = df.loc[df['month'].str.lower() == month] 
    if day !=-1:
        df = df.loc[df['day'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    x=df['month'].mode()
    print('most commom month: ' +x)

    # TO DO: display the most common day of week
    y=df['day_of_week'].mode()
    print('most commom day_of_week: ' +y)

    # TO DO: display the most common start hour
    z=df['hour'].mode()[0]
    print('most commom hour: ' +str(z))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    a=df['Start Station'].mode()
    print('most commom start_station: '+a )

    # TO DO: display most commonly used end station
    b=df['End Station'].mode()
    print('most commom end_station: '+b )

    # TO DO: display most frequent combination of start station and end station trip
    c=(df['Start Station'] + df['End Station']).mode()
    print('most commom trip: ' +c )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    m=df['Trip Duration'].sum()
    print('total travel time: '+str(m) )

    # TO DO: display mean travel time
    n=df['Trip Duration'].mean()
    print('average travel time: '+str(n) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    u=df['User Type'].value_counts()
    print('count of each user type: '+str(u) )

    # TO DO: Display counts of gender
    if city =='new york city' or city == 'chicago':
            g=df['Gender'].value_counts()
            print('count of each user type: '+str(g) )

    # TO DO: Display earliest, most recent, and most common year of birth
            e=df['Birth Year'].min()
            r=df['Birth Year'].max()
            comm=df['Birth Year'].mode()
            print(comm.dtype)
            print('earliest year of birth: '+str(e) )
            print('most recent year of birth: '+str(r) )
            print('most common year of birth: '+ str(comm))

    else:
        return

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    """
    Asks if the user would like to see some lines of data from the filtered dataset.
    Displays 6 (display_rows) lines, then asks if they would like to see 5 more.
    Continues asking until they say stop.
    """
    display_rows = 6
    row_start = 0
    row_end = display_rows - 1    

    print('\n    Would you like to see some raw data from the current dataset?')
    while True:
        reply = input('(y or n):  ')
        if reply.lower() == 'y':
            
            print('\n    Displaying rows {} to {}:'.format(row_start + 1, row_end + 1))

            print('\n', df.iloc[row_start : row_end + 1])
            row_start += display_rows
            row_end += display_rows

            print('\n    Would you like to see the next {} rows?'.format(display_rows))
            continue
        else:
            break
    
def main():
    while True:
        filters, city, month, day = get_filters()
        df = load_data(filters,city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
