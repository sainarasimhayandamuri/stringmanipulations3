friends = "we are friends and we all will be always together"
e = friends.split(" ",1) # when we pass a index to split function it will give index+1 elements
print(list(e))
g = friends.rsplit(" ",1)
print(list(g))
#split() function splits from left and rsplit function splits from right
h = friends.rpartition('we are friends and we all will be always together')
print(h)
i = friends.partition('we are friends')
print(i)

#Search Substring
#syntax: str.startswith(prefix,start,end)
friends = "we are friends and we all will be always together"
print(friends.startswith("friends"))
print(friends.startswith("we"))
#startswith() function returns true if the string passed to the function and starting element of the defined string is same or else it will give false.
#syntax: str.startswith(suffix,start,end)
print(friends.startswith("are",3,6))
print(friends.startswith("friends",7,14))
print(friends.endswith("together"))
print(friends.endswith("are",2,6))