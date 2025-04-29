# methods of dictonary
marks={"shiva":99,"Snehardha":98,"amin":89,"thanush":79,"bharath":60}
print(marks)
print(marks.items()) #returns all the key value pairs
print(marks.keys())#returns all the keys
print(marks.values())#returns all the values
marks.update({"shiva":100}) #used to update any value of key and used to add new key value pair to dictonary
marks.update({"keerthi":99})
print(marks)
print(marks.get("shiva1"))# this method returns "none" if the key is not present
print(marks["shiva1"])#this method returns "error" if the given key is not present