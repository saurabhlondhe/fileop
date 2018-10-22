class net():
	def __error(error):
		return ("\033["+str(31)+"m"+str(error)+"\033[0m")
	def load_data(url,filename=None):
		try:
			import requests
			r = requests.get(url)
			if filename==None:
				return (r.content)
			else:
				with open(filename,'wb') as f:
					f.write(r.content)
					return True
		except Exception as e:
			print(net.__error(str(e)))