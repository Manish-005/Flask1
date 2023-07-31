'''
class Marksheet():
	def __init__(self, name, fatherName, schoolName, rollNo, dob, physics, mathematics, chemistry, hindi, english):
		self._name = name
		self._fathername = fatherName
		self._schoolName = schoolName
		self._rollNo = rollNo
		self._dob = dob
		self._physics = physics
		self._mathematics = mathematics
		self._chemistry = chemistry
		self._hindi = hindi
		self._english = english
'''


student = input("Enter Your Name : ")
fatherName = input("Enter Your Father's Name : ")
schoolName = input("Enter Your School Name : ")
rollNo = int(input("Enter Your Roll Number : "))
dob = input("What is your B'day? (in DD/MM/YYYY) : ")
physics = int(input("Enter Your Physics Marks : "))
maths = int(input("Enter Your Mathematics Marks : "))
chem = int(input("Enter Your Chemistry Marks : "))
hindi = int(input("Enter Your Hindi Marks : "))
eng = int(input("Enter Your English Marks : "))

subjectMarksList = [physics, maths, chem, hindi, eng]

print("-"*142)
print("|\t\t\t\t\t\t\tHigher Secondary Education Board\t\t\t\t\t\t\t|")
print("|\t\t\t\t\t\t\t\t    (Bhopal)\t\t\t\t\t\t\t\t\t|")
print("-"*142)
print("|\t\t\t\t\t\t\t\t  (Mark-Sheet)\t\t\t\t\t\t\t\t\t|")
print("-"*142)
print("|Student Name	:- "+student.title()+"\t\t\t\t\t\t| Father Name :- "+fatherName.title()+"\t\t\t\t\t\t\t|")
print("|Date of Birth	:- "+dob+"\t\t\t\t\t\t| Roll Number :- ",rollNo,"\t\t\t\t\t\t\t|")
print("|School Name	:- "+schoolName.upper()+"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|")
print("-"*142)
print("|\t\tSubject\t\t\t|\t\tMarks\t\t|\t\tTotal\t\t|\t\tGrade\t\t\t\t|")
print("-"*142)
class Subject:
	def __init__(self, grade_):
		self.grade_ = grade_
		for i in range(0, len(subjectMarksList)):
			subjects = ["Physics", "Mathematics", "Chemistry", "Hindi	", "English"]
			if subjectMarksList[i] >= 75:
				self.grade_ = "A"
				print("|\t\t",subjects[i],"\t\t|\t\t  ",subjectMarksList[i],"\t\t|\t\t  100\t\t|\t\t"+self.grade_+"\t\t\t|")
			elif subjectMarksList[i] >= 60 and subjectMarksList[i] <=74:
				self.grade_ = "B"
				print("|\t\t",subjects[i],"\t\t|\t\t  ",subjectMarksList[i],"\t\t|\t\t  100\t\t|\t\t"+self.grade_+"\t\t\t|")
			elif subjectMarksList[i] >= 45 and subjectMarksList[i] <=59:
				self.grade_ = "C"
				print("|\t\t",subjects[i],"\t\t|\t\t  ",subjectMarksList[i],"\t\t|\t\t  100\t\t|\t\t"+self.grade_+"\t\t\t|")
			elif subjectMarksList[i] >= 33 and subjectMarksList[i] <=44:
				self.grade_ = "D"
				print("|\t\t",subjects[i],"\t\t|\t\t  ",subjectMarksList[i],"\t\t|\t\t  100\t\t|\t\t"+self.grade_+"\t\t\t|")
			else:
				self.grade_ = "E"
				print("|\t\t",subjects[i],"\t\t|\t\t  ",subjectMarksList[i],"\t\t|\t\t  100\t\t|\t\t"+self.grade_+"\t\t\t|")
			
obj = Subject("grade_")

print("-"*142)
print("|\t\t\t\tTotal Marks\t\t\t\t|\t\t\t\t",sum(subjectMarksList),"\t\t\t\t\t|")
print("-"*142)
print("|\t\t\t\tPercentage\t\t\t\t|\t\t\t\t",round(sum(subjectMarksList)/5,2),"%\t\t\t\t\t|")
print("-"*142)