import csv 

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def format_output_as_desired(output_in_original_form):
    if is_number(output_in_original_form):
        if float(output_in_original_form) >= 0.5:
            return "1"
        else:
            return "0"
    elif "prediction" in output_in_original_form.lower():
        next
    elif "true" in output_in_original_form.lower():
        return "1"
    elif "false" in output_in_original_form.lower():
        return "0"
    else:
        raise Exception("Could not convert value to 0 or 1, check the script, value was:{}".format(output_in_original_form))


fields = ""
both = []
for i in range(1,11):
    long_file = 'hadoop_test_' + str(i) + '.csv'
    prediction = 'hadoop_prediction_' + str(i) + '.csv'

    with open(long_file, 'r') as book1:
        with open(prediction, 'r') as book2:
            reader1 = csv.reader(book1, delimiter=',')
            reader2 = csv.reader(book2, delimiter=',')

            fields = next(reader1)  # read header row
            fields.append('x')
            fields.append('False rf')
            fields.append('True rf')

            next(reader2) # read and ignore header row
            for row2, row1 in zip(reader1, reader2):
                row2.append(format_output_as_desired(row1[-3]))
                row2.append(row1[-2])
                row2.append(row1[-1])

                both.append(row2)

final_file = 'hadoop_final_results.csv'
with open(final_file, 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    writer.writerow(fields)  # write a header row
    writer.writerows(both)

# import csv 

# def is_number(string):
#     try:
#         float(string)
#         return True
#     except ValueError:
#         return False


# def format_output_as_desired(output_in_original_form):
#     if is_number(output_in_original_form):
#         if float(output_in_original_form) >= 0.5:
#             return "1"
#         else:
#             return "0"
#     elif "true" in output_in_original_form.lower():
#         return "1"
#     elif "false" in output_in_original_form.lower():
#         return "0"
#     else:
#         raise Exception("Could not convert value to 0 or 1, check the script, value was:{}".format(output_in_original_form))


# fields = ""
# both = []
# for i in range(1,11):
#     long_file = 'hadoop_test_' + str(i) + '.csv'
#     prediction = 'hadoop_prediction_' + str(i) + '.csv'

#     with open(long_file, 'r') as book1:
#         with open(prediction, 'r') as book2:
#             reader1 = csv.reader(book1, delimiter=',')
#             reader2 = csv.reader(book2, delimiter=',')

#             fields = next(reader1)  # read header row
#             fields.append('x')
#             next(reader2) # read and ignore header row
#             for row2, row1 in zip(reader1, reader2):
#                 row2.append(format_output_as_desired(row1[-1]))
#                 both.append(row2)

# final_file = 'hadoop_final_results.csv'
# with open(final_file, 'w', newline='') as output:
#     writer = csv.writer(output, delimiter=',')
#     writer.writerow(fields)  # write a header row
#     writer.writerows(both)
