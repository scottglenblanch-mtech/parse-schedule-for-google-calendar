from functools import reduce
import argparse
import csv
import io

def get_elements(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_contents = file.read()
    

    # Remove all newline characters
    file_contents = file_contents.replace('\n', ' ')
    
    f = io.StringIO(file_contents)
    reader = csv.reader(f, delimiter=',')
    return next(reader)


def get_indices_with_instructor_name(elements, matching_value):
    indices = [index for index, value in enumerate(elements) if value == matching_value]
    
    return indices

def get_script_input_arguments():
    parser = argparse.ArgumentParser(description="Process some files and instructor name.")
    parser.add_argument('--input-file', type=str, required=True, help='The input file path')
    parser.add_argument('--output-file', type=str, required=True, help='The output file path')
    parser.add_argument('--instructor-name', type=str, required=True, help='The instructor name')    
    args = parser.parse_args()

    return args.input_file, args.output_file, args.instructor_name

def create_import_events_file_contents(elements, indices):

    def create_row(aggregate, index):
        subject = elements[index - 2]
        start_date = elements[index - 4]
        start_time = '7:30 AM'
        end_date = start_date
        end_time = '10:30 AM'
        description = elements[index - 1]
        location = '"2353 North Triumph Blvd, Lehi, UT 84043"'

        new_row = ",".join([subject, start_date, start_time, end_date, end_time, description, location]) + '\n'

        return aggregate + new_row

    msg = 'Subject,Start Date,Start Time,End Date,End Time,Description,Location\n'
    msg = msg + reduce(create_row, indices, "")

    return msg

def create_import_calendar_file(output_file_path, new_file_contents):
    with open(output_file_path, 'w') as file:
        file.write(new_file_contents)


# Example usage
def main():
    input_file_path, output_file_path, instructor_name  = get_script_input_arguments()
    
    elements =  get_elements(input_file_path)
    indices = get_indices_with_instructor_name(elements, instructor_name)
    new_file_contents = create_import_events_file_contents(elements, indices)

    create_import_calendar_file(output_file_path, new_file_contents)

main()
