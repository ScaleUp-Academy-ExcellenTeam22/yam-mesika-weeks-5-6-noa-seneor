import random
from datetime import datetime
from datetime import timedelta


def date_between():
    """
    asks the user to enter two dates 
    print a random date between the two dates if the day printed is monday then 
    prints "אין לי ויניגרט"
    """
    start = input("enter your start date:")
    end = input("enter your end date:")
    # converts the input to dates
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    # choose a random day number between the two dates
    random_days = random.randrange((end_date - start_date).days)
    # add the random day number to the start date
    random_date = start_date + timedelta(days=random_days)
    print(random_date.strftime('%Y-%m-%d'))
    
    if random_date.weekday() == 0:
        print("אין לי ויניגרט")


date_between()
