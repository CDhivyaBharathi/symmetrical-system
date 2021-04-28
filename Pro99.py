import os
import shutil
import time

def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")

	else:
		print(f"Unable to delete the "+path)



def remove_file(path):

	# removing the file
	if not os.remove(path):
		print(f"{path} is removed successfully")

	else:
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
	return ctime

# main 
def main():

	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = "/PATH_TO_DELETE"

	days = 30

	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# checking whether the file is present in path or not
	if os.path.exists(path):

		# iterating over each and every folder and file in the path
		for root_folder, folders, files in os.walk(path):

			# comparing
			if seconds >= get_file_or_folder_age(root_folder):

				# deleting the folder
				remove_folder(root_folder)
				deleted_folders_count += 1 

				
				break

			else:

				# checking folder from the root_folder
				for folder in folders:

		
					folder_path = os.path.join(root_folder, folder)

					if seconds >= get_file_or_folder_age(folder_path):

						# deleting
						remove_folder(folder_path)
						deleted_folders_count += 1


				# checking the current directory files
				for file in files:

					file_path = os.path.join(root_folder, file)

					if seconds >= get_file_or_folder_age(file_path):

						# deleting
						remove_file(file_path)
						deleted_files_count += 1 

		else:

			# if the path is not a directory
			if seconds >= get_file_or_folder_age(path):

				# deleting
				remove_file(path)
				deleted_files_count += 1 

	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1 

	print(f"{deleted_folders_count} folders were deleted")
	print(f"{deleted_files_count} files were deleted")




if __name__ == '__main__':
	main()