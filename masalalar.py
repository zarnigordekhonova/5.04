# 1
def remove_same(list):
    for i in list:
        for j in list:
            if i == j:
                list.remove(i)
                list.remove(j)
    print(list)

# remove_same([1, 2, 3, 4, 3, 2, 1])


# 2
from datetime import datetime, timedelta

def kabisa_yil(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def coders_day(year):
    kun = 256
    date = datetime(year, 1, 1) + timedelta(days=kun - 1)
    return date.strftime('%Y-%m-%d')

boshlangan_yil = 2000
tugagan_yil = 2009

for year in range(boshlangan_yil, tugagan_yil + 1):
    k = coders_day(year)
    # print(f"World Coders' Day in {year} is on {k}.")

def num_desk(class1, class2, class3):
    c1= class1 / 2
    c2 = class2 / 2
    c3 = class3 / 2
    print(round(c1 + c2 + c3))

num_desk(20, 21, 22)
num_desk(16, 18, 20)







