# Simple File handing module to reduce writing efforts

```python
from fileop import file
data="saurabh londhe"
file.create("data.txt") #creates a file
file.write("data.txt",data) #write content to the file
file.append("data.txt","\n Python lover") #appends data to the same file
s=file.read("data.txt")
print (s)
``` 
output:
``` 
saurabh londhe
 Python lover
 ``` 

