import libxml2
import sys

'''
purpose
	store the information from an answer element
'''
class Answer:
	def __init__(self, index, path, result, answer, time):
		self.index = index
		self.path = path
		self.result = result
		self.answer = answer
		self.time = time

'''
purpose
	Store the information from a display element.
'''
class Display:
	def __init__(self, index, path, time):
		self.index = index
		self.path = path
		self.time = time

'''
purpose
	Extract the information from log_file and return it as a list
	of answer and display objects.
preconditions
	log_file is the name of a legal, readable quiz log XML file
'''
def load_quiz_log(log_file):
	#a list to contain all information from the file
	log_list = []
	
	#parse the xml file so its content can be traversed
	parse_tree = libxml2.parseFile(log_file)
	context = parse_tree.xpathNewContext()
	root = parse_tree.getRootElement()
	quiz = root.children
	
	#look at each child of the root
	while quiz is not None:
		if quiz.name == 'answer':
			a = quiz.children
			index, path, result, answer, time = 0, 0, 0, 0, 0
			
			#traverse each child of the answer element and extract its contents
			while a is not None:
				if a.name == 'index':
					index = int(a.content)
				if a.name == 'path':
					path = a.content
				if a.name == 'result':
					if a.content == '':
						result = None
					else:
						result = int(a.content)					
				if a.name == 'answer':
					answer = a.content
					if answer == '':
						answer = None
				if a.name == 'time':
					if a.content == '':
						time = None
					else:
						time = int(a.content)
				a = a.next
			
			#create an object of class Answer with this information
			object = Answer(index, path, result, answer, time)
			
			#append this new object to the log_list
			log_list.append(object)
			
		elif quiz.name == 'display':
			q = quiz.children
			index, path, time = 0, 0, 0
			
			#traverse each child of the display element and extract its contents
			while q is not None:
				if q.name == 'index':
					index = int(q.content)					
				if q.name == 'path':
					path = q.content
				if q.name == 'time':
					time = int(q.content)
				q = q.next
				
			#create an object of class Display with this information
			object = Display(index, path, time)
			
			#append this new object to the log_list
			log_list.append(object)
			
		quiz = quiz.next
		
	return log_list

'''
purpose
	Return the number of distinct questions in log_list.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_question_count(log_list):
	#counter to keep track of where we are in the log_list
	i = 0
	
	#tracks the number of Answer objects encountered
	count = 0
	
	#traverse the first n dummy answers in the log_list until the first Display object is found 
	while isinstance(log_list[i], Answer):
		count += 1
		i += 1

	return count

'''
purpose
	Extract the list of marks.
	For each index value, use the result from the last non-empty answer,
	or 0 if there are no non-empty results.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_mark_list(log_list):
	#index of current question whose mark we are looking for
	index = 0
	
	#the last found result value for the question
	mark = 0
	
	num_questions = compute_question_count(log_list)
	marks = [0]*num_questions
	
	#while there are still questions whose marks we need to find
	while index < num_questions:
		for x in log_list:
			if isinstance(x, Answer) and int(x.index) == index and x.result != None:
				
				#save the result of this entry until a later one is found
				mark = int(x.result)
		
		#save the last found mark for the question
		marks[index] = mark
		
		#move onto next question
		index += 1
	
	return marks
