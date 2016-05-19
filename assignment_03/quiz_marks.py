import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.
	For each log file
		write to standard output the course mark for the log file,
		in CSV format
preconditions
	Each command-line argument is the name of a legal, readable quiz log file.

	All of the log files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

#for each log file included
for x in range(1,len(sys.argv)):
	
	#create a log_list for the file
	log_list = quiz_library.load_quiz_log(sys.argv[x])
	
	#create a marks_list for the file
	marks_list = quiz_library.compute_mark_list(log_list)
	
	quiz_mark = 0
	
	#traverse the marks_list
	for m in marks_list:
	
		#add the mark for the question to the total mark for the quiz
		quiz_mark += m
		
	#print the name of the log_file and the mark for the corresponding quiz
	print str(sys.argv[x]) + ',' + str(quiz_mark)
