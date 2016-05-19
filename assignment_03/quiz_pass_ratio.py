import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	Accumulate across all the log files the pass ratio for each question.

	A question result is considered a pass if it is not 0 or None
	and fail otherwise.

	The pass ratio for a question is the number of passes
	divided by the number of passes + fails.
preconditions
	Each command-line argument is the name of a
	readable and legal quiz log file.

	All the log_files have the same number of questions.
'''

#check number of command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

#make log_list of the first log file
log_list = quiz_library.load_quiz_log(sys.argv[1])

#make a marks_list of the first log file
marks_list = quiz_library.compute_mark_list(log_list)

#calculate number of questions in the file(s)
num_questions = quiz_library.compute_question_count(log_list)

#set passes and fails to size num_questions and set each element to 0
passes = [0 for x in range(num_questions)]
fails = [0 for x in range(num_questions)]

#for each log file passed in through the command line
for x in range(1, len(sys.argv)):
	#current index of both passes and fails
	index = 0
	for m in marks_list:
		if m != 0:
			passes[index] += 1
		else:
			fails[index] += 1
		index += 1
		
	#if this isn't the last file
	if x < (len(sys.argv) - 1):
		# make log_list of the next log file
		log_list = quiz_library.load_quiz_log(sys.argv[x+1])
		
		#make a marks_list of the next file
		marks_list = quiz_library.compute_mark_list(log_list)

#for each corresponding question in the log_files (excluding the last)		
for y in range(0, num_questions-1):
	#calculate the pass ratio
	pass_ratio = passes[y]/(float(passes[y]+fails[y]))
	
	#print the pass ratio
	sys.stdout.write(str(pass_ratio) + ',')

#index of last question
last = num_questions-1

#calculate the pass ratio for the last question
pass_ratio = passes[last]/(float(passes[last]+fails[last]))

#print the calculated pass ratio for the last question without the comma
print str(pass_ratio)