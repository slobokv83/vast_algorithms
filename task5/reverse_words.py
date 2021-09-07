'''
@Input: 
Agree with you the council does. Your apprentice Skywalker will be.
@Output:
Does council the you with agree. Be will Skywalker apprentice your.
'''
text = "More to be discovered - in this post, you should learn fast. Can Ben "\
				"follow me? What do You think?"
delimiter = [".", "!", "?"]

def reverse_words(text, delimiter):
	word = ""
	sentence_text = ""
	reverse_text = ""
	flag_previous_was_delimiter = False

	for i in text:
		'''3 - when a word is formed take further steps; word delimiter is the
		space char or sentence delimiter'''
		if i == " " or i in delimiter:

			'''6 - if it is the first word of the sentence, then convert the
			first letter to be lowercase; this will be the last word of the
			reversed sentence'''
			if sentence_text == "" and word != "":
				word = word[0].lower() + word[1:]

			if i == " ":

				'''5 - if previously sentence delimiter was present, then	avoid adding
				the space char in front of delimiter to avoid	double space'''
				if flag_previous_was_delimiter:
					sentence_text = word  + sentence_text
					flag_previous_was_delimiter = False
					
				else:
					'''4 - from words form a sentence; put a word in front of 
					previously saved words to keep reverse order; also, put the 
					space char in front of a word'''
					sentence_text = " " + word  + sentence_text

			'''7 - if the sentence delimiter is present then add a sentence to
			reverse text, put sentence to empty string to be prepared for the next
			sentence, make the first letter of the word be uppercase because this is
			the last word of the sentence or the first word of the reversed sentence,
			and put the flag to True to mark delimiter appereance (important to avoid
			double space in front delimiter)'''
			if i in delimiter:
				word = word[0].upper() + word[1:]

				'''8 - add delimiter with the space char to the end of the
				sentence (i + " ")'''
				sentence_text = word + sentence_text + i + " "
				reverse_text += sentence_text
				sentence_text = ""
				flag_previous_was_delimiter = True

			'''2 - put the word to empty string to be prepared for the next word'''
			word = ""
		else:
			'''1 - add charaters to form word''' 
			word += i

	'''9 - if the end of text finishes with one of three delimiters, but it is
	not in the delimiter list, then it is necessary to keep the last sentence but
	delimiter char will be treated as ordinary char, and text won't end with any
	of the delimiters'''
	if len(delimiter) < 3:
		if i not in delimiter:
			word = word[0].upper() + word[1:]
			reverse_text = reverse_text + "" + word + sentence_text
			return reverse_text

	'''10 - the last character is space, because of i + " " adding, so one needs to
	exclude it'''	
	return reverse_text[:-1]

if __name__ == "__main__":
	print(reverse_words(text, delimiter))