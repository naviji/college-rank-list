from regularexp import *

def grade_line_splitter(s):
	grade = s.split(',')
	split = []
	for g in grade:
		split.append([text_before_para(g),text_between_para(g)]);
	return split




def extractor(src,des):
	with open(src) as f:
		content = f.readlines()
	content = [x.strip() for x in content]


	# name of the college from content[4]
	college_name = content[4]
	exam_name = content[6]


	grade_lines = []
	deptname = []
	dept_list = []
	student = []
	temp_grade = []
	prev_gradeline = False
	prev_empty = False
	content = [x.replace("[Full Time]","") for x in content]
	for line in content:
		if(line):
			if (is_dept(line)):
				deptname = line

				dept_list.append([deptname])
			elif (is_reg_num(line)):
				student.append([deptname,line])
			elif (is_course_code(line)):
				continue
			elif (is_grade_line(line)):
					
					if(prev_gradeline is True):
						temp_grade[-1] = temp_grade[-1][:-1]
						temp_grade.append(','+line)
						grade_lines.append("".join(temp_grade))
						temp_grade = []
						prev_gradeline = False
					else:
						prev_gradeline = True
						temp_grade.append(line)
			prev_empty = False
		else:
			prev_empty = True
			if(prev_gradeline is True and prev_empty is True):
				grade_lines.append("".join(temp_grade))
				temp_grade = []
				prev_gradeline = False


	grade_lines = [x.replace(" ","") for x in grade_lines]

	count = 0
	for  i in student:
		i.append([grade_line_splitter(grade_lines[count])])
		count = count + 1


	for i in dept_list:
		temp = []
		for j,k,l in student:
			if (i[0] == j):
				temp.append([k]+l)
		i.append(temp)

	#
	#
	# print(dept_list)
	# for i in dept_list:
	# 	print(i[0])
	# 	for j in i[1]:
	# 		print(j[0])
	# 		for k,l in j[1]:
	# 			print("{} grade for {}".format(l,k))
	#



	text_file = open("{}/{}.txt".format(des,college_name),"w+")
	text_file.write("{} for {}\n".format(exam_name,content[4]))
	for i in dept_list:
		text_file.write("\n{}\n".format(i[0]))
		for j in i[1]:
			text_file.write("\n{}".format(j[0]))
			for k,l in j[1]:
				text_file.write("\n{} grade for {}".format(l,k))
			text_file.write("\n")
	text_file.close()

if __name__ == '__main__':
	extractor("./4.txt",".")
