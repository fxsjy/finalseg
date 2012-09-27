finalseg
========
Chinese Words Segment Library in Python based on HMM Model

Usage
========
* 自动：easy_install finalseg
* 手动: 将finalseg目录放置于当前目录或者site-packages目录



代码示例


	import finalseg

	sentence_list = [
	"姚晨和老凌离婚了",
	"他说的确实在理",
	"长春市长春节讲话"
	]

	print u"=默认效果"

	for sentence in sentence_list:
		seg_list = finalseg.cut(sentence)
		print "/ ".join(seg_list)

	print u"\n=打开新词发现功能后的效果\n"


	for sentence in sentence_list:
		seg_list = finalseg.cut(sentence,find_new_word=True)
		print "/ ".join(seg_list)


Algorithm
=========
* 算法是基于HMM模型,采用了Viterbi算法
* 可以选择是否打开新词发现功能
* 算法简单，只有89行纯Python代码 https://github.com/fxsjy/finalseg/blob/master/finalseg/__init__.py

Performance
=========
* 200 KB/Second
* Test Env: Intel(R) Core(TM) i7-2600 CPU @ 3.4GHz；《围城》.txt

Example
=========
* 在线分词效果展示  https://finalseg.appspot.com/   (需要翻墙)
