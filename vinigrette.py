import random
import datetime
begin = datetime.date(1912, 6, 23)
end = datetime.date(1954, 6, 7)
random_days = random.randrange((end - begin).days)
random_date = begin + datetime.timedelta(days=random_days)
print(random_date)
if random_date.weekday() == 0:
    print("אין לי ויניגרט")
