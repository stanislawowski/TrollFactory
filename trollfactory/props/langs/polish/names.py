import csv, json

def main ():
	names_women = []
	names_men = []

	total_women = 0
	total_men = 0

	with open('women.csv', newline='') as women_csv:
		reader = csv.reader(women_csv)
		for row in reader:
			if (row[2] == 'LICZBA_WYSTĄPIEŃ'):
				continue
			
			names_women.append([row[0].lower().capitalize(), int(row[2])])
			total_women += int(row[2])

	with open('men.csv', newline='') as men_csv:
		reader = csv.reader(men_csv)
		for row in reader:
			if (row[2] == 'LICZBA_WYSTĄPIEŃ'):
				continue
			
			names_men.append([row[0].lower().capitalize(), int(row[2])])
			total_men += int(row[2])

	# calculate weights 
	for key, women in enumerate(names_women):
		names_women[key][1] = 100 * names_women[key][1]/total_women

	for key, men in enumerate(names_men):
		names_men[key][1] = 100 * names_men[key][1]/total_men

	with open('names.json', 'w') as output:
		json.dump({'male': names_men, 'female': names_women}, output, indent=4)

if __name__ == '__main__':
	main()