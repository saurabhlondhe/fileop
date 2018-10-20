def __error(error):
		return ("\033["+str(31)+"m"+str(error)+"\033[0m")
def owner(file):
	""" get file owner
		>>> import fileop.fstat as fstat
		>>> fstat.owner(file_path)

		returns str(owner_name)"""
	try:
		import os
		from pwd import getpwuid
		return (getpwuid(os.stat(file).st_uid).pw_name)
	except Exception as e:
		print(__error(str(e)))

def group(file):
	""" get file group
		>>> import fileop.fstat as fstat
		>>> fstat.group(file_path)

		returns str(group_name)"""
	try:
		import os
		from pwd import getpwuid
		return (getgrgid(os.stat(file).st_gid).gr_name)
	except Exception as e:
		print(__error(str(e)))

def size(file):
	""" get file size
		>>> import fileop.fstat as fstat
		>>> fstat.size(file_path)

		returns list	->		[size,"bytes"]"""
	try:
		import os
		return [os.path.getsize(file),"bytes"]
	except Exception as e:
		print(__error(str(e)))

def perm(file,ch=None):
	"""
	get file permissions
		>>> perm(file_path)
		#returns 0644

		>>> perm(file_path,"text")
		#retrun list	->		['rwx','r--','r--']"""
	try:
		if (ch=="text"):
			import os
			count=str(oct(os.stat(file).st_mode))[-3:]
			perm_set=[]
			for i in count:
				if (i=="7"):
					perm_set.append("rwx")
				elif (i=="6"):
					perm_set.append("rw-")
				elif (i=="5"):
					perm_set.append("r-x")
				elif (i=="4"):
					perm_set.append("r--")
				elif (i=="3"):
					perm_set.append("-wx")
				elif (i=="2"):
					perm_set.append("-w-")
				elif (i=="1"):
					perm_set.append("--x")
			return perm_set
		else:
			import os
			return (str(oct(os.stat(file).st_mode))[-4:])
	except Exception as e:
		print(__error(str(e)))

