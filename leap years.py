def get_leap_years():
    starting_year = 2001
    year_in_line = 0
    is_leap = False

    for i in range (starting_year, 2101):
        is_leap = False
        if i % 4 == 0 and i % 100 != 0:
            print("{}".format(i), end='')
            year_in_line += 1
            is_leap = True
        elif i % 4 == 0 and i % 100 == 0:
            if i % 400:
                print("{}".format(i), end='')
                year_in_line += 1
                is_leap = True
        if year_in_line < 10 and is_leap:
            print(",", end='')
        elif is_leap:
            print()
            year_in_line = 0

get_leap_years()


