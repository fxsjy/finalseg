#encoding=utf-8
import finalseg

sentence_list = [
"姚晨和老凌离婚了",
"他说的确实在理",
"长春市长春节讲话"
]

print "==default segment"

for sentence in sentence_list:
	seg_list = finalseg.cut(sentence)
	print "/ ".join(seg_list)

print "==toggle on the function of new word finding"

for sentence in sentence_list:
	seg_list = finalseg.cut(sentence,find_new_word=True)
	print "/ ".join(seg_list)

