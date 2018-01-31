import os

def walk(dirname):
	list_files = []
	list_dir = []
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)
		if os.path.isfile(path):
			list_files.append(path)
		elif os.path.isdir(path):
			list_dir.append(path)

			
	print(list_files)
	print(list_dir)		
walk(os.getcwd())
