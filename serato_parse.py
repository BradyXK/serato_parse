import csv, os, sys
from datetime import date, datetime


fields = []
fields_to_use = []
output_rows = []
beginning_time_s = '0:00:00'
beginning_time_dt = datetime.strptime(beginning_time_s, '%H:%M:%S')
next_time_s = ''
next_time_dt = beginning_time_dt
time_delta_s = ''
time_delta_dt = beginning_time_dt
output_list = []
current_time_s = ''
current_time_dt = beginning_time_dt

output_txt = open('parsed_tl.txt', 'w')

with open('input_tl.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)

    selected_fields = ['artist', 'name']

    for row in csvreader:
        output_rows.append(row)

    print("Total rows %d" % (csvreader.line_num))

    count = 0

    while count < len(output_rows):
        if count is 0:
            count += 1
        elif count is 1:

            output_string = output_rows[count][0] + ' - '+ output_rows[count][1] + ' ' + beginning_time_s
            output_list.append(output_string)
            next_time_s = output_rows[count + 1][3].strip('PM PDT')
            next_time_dt = datetime.strptime(next_time_s, '%H:%M:%S')
            time_delta_dt = next_time_dt - datetime.strptime(output_rows[count][3].strip('PM PDT'), "%H:%M:%S")
            current_time_dt = time_delta_dt
            current_time_s = str(current_time_dt)
            time_delta_s = str(time_delta_dt)
            
            count += 1
        else:
            
            output_string = output_rows[count][0] + ' - '+ output_rows[count][1] + ' ' + current_time_s
            output_list.append(output_string)
            if (count + 1) < len(output_rows):
                next_time_s = output_rows[count + 1][3].strip('PM PDT')
            else:
                break
            next_time_dt = datetime.strptime(next_time_s, '%H:%M:%S')
            time_delta_dt = next_time_dt - datetime.strptime(output_rows[count][3].strip('PM PDT'), "%H:%M:%S")
            current_time_dt = current_time_dt + time_delta_dt
            current_time_s = str(current_time_dt)
            count += 1
           
    for item in output_list:
        print(item)
        string = item + '\r\n'
        output_txt.write(string)
    
    output_txt.close()

