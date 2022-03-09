# Nam Doan
# 1847037

from datetime import datetime  # setting datetime to be a reference to the class



input_file = open('inputDates.txt', 'r')
output_file = open('parsedDates.txt', 'w')
dates = input_file.read().splitlines()  # splitlines() splits a string into a list

for line in dates:
    date_string = []
    if line.find('January') != -1:
        date_string = ['January']
        line = line.replace('January ', '')
    elif line.find('February') != -1:
        date_string = ['February']
        line = line.replace('February ', '')
    elif line.find('March') != -1:
        date_string = ['March']
        line = line.replace('March ', '')
    elif line.find('April') != -1:
        date_string = ['April']
        line = line.replace('April ', '')
    elif line.find('May') != -1:
        date_string = ['May']
        line = line.replace('May ', '')
    elif line.find('June') != -1:
        date_string = ['June']
        line = line.replace('June ', '')
    elif line.find('July') != -1:
        date_string = ['July']
        line = line.replace('July ', '')
    elif line.find('August') != -1:
        date_string = ['August']
        line = line.replace('August ', '')
    elif line.find('September') != -1:
        date_string = ['September']
        line = line.replace('September ', '')
    elif line.find('October') != -1:
        date_string = ['October']
        line = line.replace('October ', '')
    elif line.find('November') != -1:
        date_string = ['November']
        line = line.replace('November ', '')
    elif line.find('December') != -1:
        date_string = ['December']
        line = line.replace('December ', '')

    if line.find(',') != -1:
        ind = line.index(',') + 1
        if line[ind - 3:ind].strip() == '':
            date_string.append(line[ind - 2:ind].strip())
        else:
            date_string.append(line[ind - 3:ind].strip())
        date_string.append(line[ind + 1:].strip())

    if len(date_string) == 3:
        t = datetime.strptime(' '.join(date_string), '%B %d, %Y')  # strptime() create a datetime object
        if datetime.today() >= t:
            parsed = (t.strftime('%m/%#d/%Y'))  # returns a string represent month/date/year
            print(parsed)
            output_file.write(parsed + '\n')
