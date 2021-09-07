lst1 = ["Apple", "is", "very", "good"]

lst2 = ["I", "like", "to", "watch", "movies"]

lst = []

lst.append(lst1)
lst.append(lst2)

print(lst)


'''
@Input: 
Agree with you the council does. Your apprentice Skywalker will be.
@Output:
Does council the you with agree. Be will Skywalker apprentice your.
'''
text = "Agree with you the council does. Your apprentice Skywalker will be."

def reverse_words(text):
	sentence_lst = []
	word_lst = []
	word = ""
	for i in text:
		if i == " " or i == ".":
			if word == "":
				sentence_lst.append(word_lst)
				print('1',sentence_lst)
				print('WORD:',word_lst)
			else:
				word_lst.append(word)
				word = ""
		else:
			word += i

		# print('2',sentence_lst)


	# print(sentence_lst)

if __name__ == "__main__":
	reverse_words(text)