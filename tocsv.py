import csv

college_info = [['AERONAUTICAL ENGINEERING',
[['ACE16AN007', [['BE103', 'C']]],
['ACE16AN012', [['EC100', 'Nochange'], ['BE100', 'Nochange']]],
['ACE16AN014', [['BE100', 'Nochange']]], ['ACE16AN016', [['BE100', 'Nochange']]],
['ACE16AN022', [['BE100', 'Nochange']]], ['ACE16AN029', [['BE100', 'Nochange']]]]],
['CIVIL ENGINEERING',
[['ACE16CE001', [['BE10101', 'Nochange']]],
['ACE16CE002', [['BE10101', 'A']]],
['ACE16CE005', [['BE110', 'Nochange'],['PH100', 'Nochange'], ['BE10101', 'Nochange']]],
['ACE16CE006', [['BE10101', 'Nochange']]], ['ACE16CE007', [['BE10101', 'Nochange']]],
['ACE16CE011', [['BE10101', 'Nochange'], ['BE110', 'C'], ['MA101', 'Nochange']]],
['ACE16CE012', [['BE10101', 'C']]], ['ACE16CE013', [['BE10101', 'Nochange']]],
['ACE16CE014', [['BE10101', 'Nochange']]],
['ACE16CE021', [['BE10101', 'Nochange'], ['BE110', 'Nochange']]], ['ACE16CE023', [['MA101', 'C'], ['BE10101', 'Nochange']]],
['ACE16CE025', [['BE10101', 'Nochange']]], ['ACE16CE026', [['BE10101', 'Nochange']]],
['ACE16CE027', [['BE10101', 'Nochange'], ['PH100', 'B+']]],
['ACE16CE029',[['BE10101', 'Nochange']]], ['ACE16CE030', [['BE10101', 'Nochange']]],
['ACE16CE031', [['PH100', 'Nochange']]], ['ACE16CE032', [['BE10101', 'Nochange']]],
['ACE16CE034', [['BE10101', 'Nochange'], ['BE110', 'Nochange']]],
['ACE16CE037', [['BE110', 'Nochange']]],
['ACE16CE040', [['BE110', 'Nochange'], ['BE10101', 'Nochange']]],
['ACE16CE041', [['EE100', 'Nochange']]]]],
['ELECTRICAL AND ELECTRONICS ENGINEERING',
[['ACE16EE011', [['CE100', 'Nochange']]]]],
['ELECTRONICS & COMMUNICATION ENGG',
[['ACE16EC003', [['MA101', 'C']]]]],
['MECHANICAL ENGINEERING',
[['ACE15ME047', [['CY100', 'C']]],
['ACE16ME005', [['BE100', 'Nochange']]],
['ACE16ME009', [['BE103', 'Nochange']]],
['ACE16ME014', [['BE103', 'Nochange'], ['MA101', 'Nochange'], ['EE100', 'Nochange']]],
['ACE16ME015', [['BE103', 'Nochange'], ['MA101', 'Nochange']]],
['ACE16ME016', [['BE100', 'Nochange']]],
['ACE16ME019', [['EE100', 'Nochange'], ['BE10102', 'Nochange']]],
['ACE16ME027', [['BE100', 'Nochange'], ['CY100', 'P']]],
['ACE16ME029', [['BE100', 'Nochange']]], ['ACE16ME030', [['BE10102', 'Nochange']]],
['ACE16ME031', [['EE100', 'C']]], ['ACE16ME033', [['BE10102', 'Nochange']]],
['ACE16ME035', [['EE100', 'Nochange'], ['BE10102', 'Nochange']]],
['ACE16ME036', [['BE100', 'Nochange']]]]]]

def to_csv(l,cname):
	with open('persons.csv', 'w+') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in l:
			for j in i[1]:
				for k,l in j[1]:				
					filewriter.writerow([j[0], i[0], k, l, cname])

if __name__ == '__main__':
	to_csv(college_info,"GOV SKP")
   

