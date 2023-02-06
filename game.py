import pandas as pd
import csv

def get_goose_using_pandas(file_name):
    class_df = pd.read_csv(file_name)
    found_student_name = class_df.loc[class_df['animal'] == 'goose', 'name'].iloc[0]
    return found_student_name

def get_goose_using_csv(file_name):
    student_name = ''
    with open(file_name) as csv_file:
        class_records = csv.DictReader(csv_file)
        for student in class_records:
            if student['animal'] == 'goose':
                found_student_name = student['name']
    return found_student_name

CLASS_FILE = 'class.csv'
options = ['csv','pandas']
method = ''
goose_name = ''

while method not in options:
    method = input(f'How would you like to load the data? (Options are {options}')

if method == 'pandas':
    goose_name = get_goose_using_pandas(CLASS_FILE)
elif method == 'csv':
    goose_name = get_goose_using_csv(CLASS_FILE)

print(f'The goose is {goose_name}.')
