#PART 1
import csv
import re,sys
from datetime import datetime


dictionary_of_states = {}
solution_rows = []

def main():
	dictionary_of_states = generate_dictionary()
	progress_bar = 0

	#data input from test.csv
	with open('../data/CSVFiles/test.csv') as input_csv:
		test_csv = csv.DictReader(input_csv)
		for row in test_csv:
			#get state name from abbreviation
			row['state'] = dictionary_of_states[(row['state'])]
			#preprocess and normalize bio
			row['bio'] = pre_process(row['bio'])	
			#convert valid dates to 		
			row['start_date'], row['start_date_description'] = date_validation(row['start_date'])			
			solution_rows.append(row)
			
    #ordered headers for solution.csv 
	fieldnames = ['name','gender','birthdate','address','city','state','zipcode','email','bio','job','start_date','start_date_description']
	
	#writes each row of solution_rows to output file solution.csv
	with open('../data/results/solution.csv','w') as output_csv:
		writer = csv.DictWriter(output_csv, fieldnames = fieldnames)
		writer.writeheader()
		for row in solution_rows:
			writer.writerow(row)
			progress_bar += 1
			update_progress(progress_bar/5)
		sys.stdout.write('\n')

def update_progress(progress):
    sys.stdout.write('\r[{0}] {1}%'.format('#'*(progress/5), progress))
    sys.stdout.flush()

#regex to erase all extra spaces
def pre_process(row):
	return re.sub('\s+',' ',row)

#generate dictionary of state abbreviations from static file
def generate_dictionary():
	with open('../data/CSVFiles/state_abbreviations.csv') as dict_of_states:
		dict_file = csv.DictReader(dict_of_states)
		for row in dict_file:			
			dictionary_of_states[row['state_abbr']] = row['state_name']
	return  dictionary_of_states

#date format validation
def date_validation(date):
	#valid date formats
	valid_formats = ['%Y-%m-%d','%m/%d/%Y', '%B %d, %Y']
	newly_formatted = '' #saves the valid dates or N/A if invalid
	invalid_format = ''  #saves invalid dates or returns empty string if valid
	split_date = re.findall(r'[\w]+',date)
	#if split date comprises of 3 parts, then it is probably valid , error handler incase of mismatch eg a/b/c
	if len(split_date) == 3:
		for date_format in valid_formats:
			try:
				tuples = datetime.strptime(date, date_format)
				newly_formatted = str(tuples).split(' ')[0]
			except ValueError:
				pass
	if newly_formatted == '':
		newly_formatted = 'N/A'
		invalid_format = date
	else:
		invalid_format = ''
	return newly_formatted, invalid_format

if __name__ == '__main__':
	main()








