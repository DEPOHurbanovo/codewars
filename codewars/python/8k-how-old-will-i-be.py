# https://www.codewars.com/kata/how-old-will-i-be-in-2099
def calculate_age(year_of_birth, current_year):
    difference = abs(current_year - year_of_birth)
    if difference > 1:
        year_format = 'years'
    else:
        year_format = 'year'

    if current_year > year_of_birth:
        difference = current_year - year_of_birth
        text = 'You are {} {} old.'.format(str(difference), year_format)
    elif current_year < year_of_birth:
        difference = year_of_birth - current_year
        text = 'You will be born in {} {}.'.format(str(difference), year_format)
    elif current_year == year_of_birth:
        text = 'You were born this very year!'
    else:
        text = 'No match'

    return text
