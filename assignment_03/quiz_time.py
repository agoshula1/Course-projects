import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	For each log file, compute the total time taken for each question. 

	Write to standard output, the average time spent for each question.
preconditions
	Each command-line argument is the name of a readable and
	legal quiz log file.

	All the log_files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

#make log_list of the first log file
log_list = quiz_library.load_quiz_log(sys.argv[1])

#calculate number of questions in the file(s)
num_questions = quiz_library.compute_question_count(log_list)

#set total to size num_questions and set each element to 0
total = [0 for x in range(num_questions)]

#current question number
q = None

#total time spent on the current question
q_time = 0

#for each file passed in through the command line
for x in range(1, len(sys.argv)):

	#for each question in the quiz
	for y in range(0, num_questions):
	
		#for each element of log_list (excluding the last element)
		for z in range(0, len(log_list)-1):
			if q is None and log_list[z].index == y:			
				#this is the next question to look at
				if isinstance(log_list[z], quiz_library.Display):
				
					#not one of the dummy answer elements
					q_time = log_list[z+1].time - log_list[z].time
					q = log_list[z].index
					
			elif log_list[z].index == q:
				#add time spent during this event
				q_time += log_list[z+1].time - log_list[z].time
				
		#if we found a non-dummy element of the question
		if q is not None:
			#add time spent on the question in this quiz to total
			total[y] += q_time
			
		q = None
	
	#if we haven't run out of files
	if x < (len(sys.argv) - 1):
		# make log_list of the next log file
		log_list = quiz_library.load_quiz_log(sys.argv[x+1])

#for each corresponding question in the log_files (excluding the last)		
for x in range(0, num_questions-1):
	#calculate the average time
	avg = total[x]/float(len(sys.argv)-1)
	
	#print the average time
	sys.stdout.write(str(avg) + ',')

#index of last question
last = num_questions-1

#calculate the average time for the last question
avg = total[last]/float(len(sys.argv)-1)

#print the calculated average time for the last question without the comma
print str(avg)