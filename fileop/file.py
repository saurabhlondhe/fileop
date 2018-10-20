class file:
	name=None
	def __error(error):
		if ("invalid file" in str(error)):
			return ("\033["+str(31)+"m"+str(error)+"""
please set file.name='filename' or use help(fileop.file)"""+"\033[0m")
		return ("\033["+str(31)+"m"+str(error)+"\033[0m")

	#-------------------append to file------------------------------
	def append(name=None,data=None):
		"""
		appends existing file's data	
			>>> import fileop.file as file
			>>> file.append("file_name.txt","data")
						or
			>>> file.name="file_name"
			>>> file.append("data")"""
		if name==None:
			name=file.name
		try:
			with open(name,'a') as f:
				f.write(data)
		except Exception as e1:
			print (file.__error(e1))


	def copy(name1,name2):
		"""copy content of one file to other file
		such as copy file1 -> file2
			>>> file.copy("file_name1.txt","file_name2.txt")
			returns True"""
		try:
			with open(name1,'r') as f1,open(name2,'w') as f2:
				f2.write(str(f1.read()))
				return True
		except Exception as e1:
			print (file.__error(e1))

	def count(name=None,word=None,char=None,line=None):
		"""
		Used to count words,characters,lines
		syntax as follows
			file.name="file_name"
			file.count(word=True)
			>>> 24

			# count no of word occurances
			file.count(word="text")
			>>> 54

			#count no. of lines
			file.count(line=True)
			>>> 5

			returns int
		"""
		if name==None:
			name=file.name
		try:
			if(word==True):
				return (len(file.read(name).split()))
			elif(char==True):
				return (len(file.read(name)))
			elif(line==True):
				return (len(file.read(name).split("\n"))-1)
			elif (word is not None):
				return (len(file.read(name).split(word))-1)
			elif (char is not None):
				return (len(file.read(name).split(char))-1)
			elif (line is not None):
				return (len(file.read(name).split(line))-1)
		except Exception as e:
			raise e


	def create(name=None):
		"""Used to create a files with out maintaining file poiners
		usage
			>>> import fileop.file as file
			>>> file.name="file_name"
			>>> file.create()

			returns True"""
		if name==None:
			name=file.name
		try:
			import os
			if os.path.exists(name):
				return True
			else:
				with open(name,'w') as f:
					f.write("")
					return True
		except Exception as e1:
			print (file.__error(e1))
	
	def delete(name=None):
		"""
		delete the file
			>>> file.delete()
					or
			>>> file.delete("file_name.txt")

			returns True"""
		if name==None:
			name=file.name
		try:
			import os
			os.remove(name)
			return True
		except Exception as e1:
			print (file.__error(e1))
	
	
	#-------------read content of file-------------------------------
	def read(name=None):
		"""Read content of file and return as string 
			>>> file.read()
					or
			>>> file.read("file_name.txt")"""
		if name==None:
			name=file.name
		try:
			with open(name) as f:
				return f.read()
		except Exception as e1:
			print (file.__error(e1))
	#-----------------write to file----------------------------------
	def write(data=None):
		"""file.write("file_name.txt","data")"""
		name=file.name
		try:
			with open(name,'w') as f:
				f.write(data)
		except Exception as e1:
			print (file.__error(e1))