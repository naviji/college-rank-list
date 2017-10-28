import re

engineering_dept = ["APPLIED ELECTRONICS & INSTRUMENTATION ENGINEERING", #
			"COMPUTER SCIENCE & ENGINEERING", #
			"ELECTRICAL AND ELECTRONICS ENGINEERING", #
			"ELECTRONICS & COMMUNICATION ENGG",#
			"INFORMATION TECHNOLOGY",#
			"MECHANICAL ENGINEERING", #
			"MATHEMATICS",
			"INSTRUMENTATION & CONTROL ENGG",
 			"BIOMEDICAL ENGG",
			"AUTOMOBILE ENGG",
			"BIOTECHNOLOGY & BIOCHEMICAL ENGG",
			"BIOTECHNOLOGY", #
			"CHEMICAL ENGINEERING",
			"INDUSTRIAL ENGG",
			"NAVAL ARCHITECTURE & SHIP BUILDING",
			"PRODUCTION ENGG",
			"SAFETY & FIRE ENGG",
			"FOOD TECHNOLOGY",
			"HUMANITIES",
			"METALLURGY",
			"MECHATRONICS",
			"AERONAUTICAL ENGINEERING",
			"CIVIL ENGINEERING"]

def is_reg_num(string):
	p = re.compile('[A-Z]?[A-Z][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]')
	if (p.match(string)):
		return True
	else:
		return False

def is_course_code(string):
	p = re.compile('[A-Z][A-Z][0-9][0-9][0-9][0-9]?[0-9]?$')
	if (p.match(string)):
		return True
	else:
		return False

def is_grade_line(string):
	p = re.compile('([A-Z][A-Z][0-9][0-9][0-9](.+?),?)+')
	if (p.match(string)):
		return True
	else:
		return False

def is_subject(string):
	p = re.compile('([A-Z]*,? ?)*')
	if (p.match(string) and (string not in engineering_dept)):
		return True
	else:
		return False

def is_dept(string):
	if string in engineering_dept:
		return True
	else:
		return False
	# for dept in engineering_dept:
	# 	if dept in string:
	# 		return True
	# 	else:
	# 		return False


def text_between_para(s):
	return s[s.find("(")+1:s.find(")")]


def text_before_para(s):
	s = s.strip()
	return s[:s.find("(")]

if __name__ == '__main__':
	print(is_grade_line("ME206(Absent)"))
