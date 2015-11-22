# import statements

import os

'''
Function for renaming files with os.translate

'''

def rename_files():

	## get filenames from path (r prefix means interpret raw string)

	file_list = os.listdir(r'../prank')
	print(file_list,len(file_list))

	## get current working directory

	saved_path = os.getcwd()

	## change directory

	os.chdir(r'../prank')


	## rename files

	nums = '0123456789'

	for file_name in file_list:
		print("Old Name: {}".format(file_name))
		new_name = file_name.translate(None,nums)
		print("New Name: {}".format(new_name))
		os.rename(file_name, new_name)
		

	## change back to origin directory

	os.chdir(saved_path)

rename_files()