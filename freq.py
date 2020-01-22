 # ==============================================
# Name: Gurbani Baweja
# ID: 1590254
# CMPUT 274, 2019
# 
# Weekly Exercise 3: Word Frequency
# ==============================================

import sys

# Function check_file to check whether the user has input the correct command line.
def check_commandLine():

	
	length_list = len(sys.argv)
	# Checking the number of command line arguments entered by the user using the length of the list.
	if length_list ==1:
		print("Too few command-line arguments.\nThe correct format is: python3 freq.py <name of the file>, where <name of the file> should be exactly one word long.")
		exit()
	
	elif length_list>3 or length_list ==3:
		print("Too many command-line arguments.\nThe correct format is: python3 freq.py <name of the file>, where <name of the file> should be exactly one word long.")
		exit()
	
	else:
		# Storing the entered filename in a variable called file_Name.
		file_Name = sys.argv[1]
		return file_Name
		

# Function ReadandCount to read from the given file and count the number of times each word appears in the file.
def ReadandCount(read_file):
	
	# List to store all the words prsent in the file.
	Word_List = [] 
	
	# Dictionary to store the words and their count.
	word_dict = {}
	
	
	with open(read_file) as rfile:
		words = rfile.read()
		Word_List= words.split()
		
		for word in Word_List:
			
			if word in word_dict:
				word_dict[word] =Word_List.count(word)
				
			else:
				word_dict[word] =1

    # Calling the function out_table to calculate the frequencies and write the output table to a file.
	out_table(word_dict,read_file)		
		
def out_table(w_dict,f_name):

	# A list for storing all the output to be written to the file.
	write_list = []
	
	output_file = f_name + ".out"	
	with open(output_file,"w+") as newFile:

        # Putting the dictionary in the lexicographic order.
		for i in sorted(w_dict.keys()):
			
			# Count for calculating the sum of all the word counts.
			count = sum(w_dict.values())
			freq = w_dict[i]/count
			rounded_freq = round(freq,3)
			write_list =[i," ",str(w_dict[i])," ",str(rounded_freq)]
			Words = ''.join(write_list)
			newFile.write(Words)
			newFile.write("\n")
			

			
if __name__=="__main__":
	File = check_commandLine()
	ReadandCount(File)
	

