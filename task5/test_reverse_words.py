from reverse_words import reverse_words
import traceback

delimiter = [".", "?", "!"]

text1 = "This in London is very beautiful. I think I will stay more. My"\
				" holiday will be the best in years. So, I will enjoy it."
result1 = "Beautiful very is London in this. More stay will I think i. Years "\
					"in best the be will holiday my. It enjoy will I so,."

text2 = "Very good to learn Physics. I cannot disagree about THE best science"\
				" ever. Do you like it?"
result2 = "Physics learn to good very. Ever science best THE about disagree "\
					"cannot i. It like you do?"

text3 = "More to be discovered - in this post, you should learn fast. Can Ben "\
				"follow me? What do You think?"
result3 = "Fast learn should you post, this in - discovered be to more. Me "\
					"follow Ben can? Think You do what?"

text4 = "Agree with you the council does. Your apprentice Skywalker will be."
result4 = "Does council the you with agree. Be will Skywalker apprentice your."

text5 = "Agree with you the council does. Your apprentice Skywalker will be. "\
				"Agree with you the council does. Your apprentice Skywalker will be."
result5 = "Does council the you with agree. Be will Skywalker apprentice your"\
					". Does council the you with agree. Be will Skywalker apprentice "\
					"your."

text6 = "Very good to learn Physics. I cannot disagree about THE best science"\
				" ever. Do you like it?"
result6 = "Physics learn to good very. Ever science best THE about disagree "\
					"cannot i. It? like you do"

text7 = "More to be discovered - in this post you should learn fast. Can Ben "\
				"follow me? What do You think?"
result7 = "Fast learn should you post this in - discovered be to more. Think?"\
					" You do What me? follow Ben can"


def test_reverse_words():
	assert reverse_words(text1, delimiter) == result1
	assert reverse_words(text2, delimiter) == result2
	assert reverse_words(text3, delimiter) == result3
	assert reverse_words(text4, delimiter) == result4
	assert reverse_words(text5, delimiter) == result5
	assert reverse_words(text6, ".") == result6
	assert reverse_words(text7, ".") == result7

if __name__ == '__main__':
  try:
    test_reverse_words()
    print('PASS')
  except:
    print('FAIL')
    traceback.print_exc()	