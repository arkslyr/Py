l=int(input("Enter the limit for the list "))
words=[]
for i in range(l):
	inp=input("Enter the value for list ")
	words.append(inp)
longest_word = ""
for word in words:
 if len(word) > len(longest_word):
  longest_word = word
print("The longest word is:", longest_word)

