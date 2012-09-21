import re
import os

def load_model(f_name):
	_curpath=os.path.normpath( os.path.join( os.getcwd(), os.path.dirname(__file__) )  )
	prob_p_path = os.path.join(_curpath,f_name)
	if f_name.endswith(".py"):
		return eval(open(prob_p_path,"rb").read())
	else:
		result = set()
		for line in open(prob_p_path,"rb"):
			result.add(line.strip().decode('utf-8'))
		return result

print "Init..."
prob_start = load_model("prob_start.py")
prob_trans = load_model("prob_trans.py")
prob_emit = load_model("prob_emit.py")
near_char_tab = load_model("near_char_tab.txt")
print "OK."

def __raw_seg(sentence):
	result = []
	i,j =0,0
	while j<len(sentence)-1:
		if not ( sentence[j:j+2] in near_char_tab):
			result.append(sentence[i:j+1])
			i=j+1
		j+=1
	result.append(sentence[i:j+1])
	return result


def viterbi(obs, states, start_p, trans_p, emit_p):
	V = [{}] #tabular
	path = {}
	for y in states: #init
		V[0][y] = start_p[y] * emit_p[y].get(obs[0],0)
		path[y] = [y]
	for t in range(1,len(obs)):
		V.append({})
		newpath = {}
		for y in states:
			(prob,state ) = max([(V[t-1][y0] * trans_p[y0].get(y,0) * emit_p[y].get(obs[t],0) ,y0) for y0 in states])
			V[t][y] =prob
			newpath[y] = path[state] + [y]
		path = newpath
	(prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
	return (prob, path[state])


def __cut(sentence):
	prob, pos_list =  viterbi(sentence,('B','M','E','S'), prob_start, prob_trans, prob_emit)
	tmp=u""
	result =[]
	for i,char in enumerate(sentence):
		pos = pos_list[i]
		if pos=='B':
			tmp+=char
		elif pos=='M':
			tmp+=char
		elif pos=='E':
			tmp+=char
			result.append(tmp)
			tmp=u""
		elif pos=='S':
			result.append(char)
		if i==len(sentence)-1 and tmp!='' : 
			result.append(tmp)
	return result

def cut(sentence,find_new_word=False):
	if not ( type(sentence) is unicode):
		try:
			sentence = sentence.decode('utf-8')
		except:
			sentence = sentence.decode('gbk','ignore')
	re_han, re_skip = re.compile(ur"([\u4E00-\u9FA5]+)"), re.compile(ur"[^a-zA-Z0-9+#]")
	blocks = re_han.split(sentence)
	result = []
	for blk in blocks:
		if re_han.match(blk):
			lbs = [blk] if find_new_word else __raw_seg(blk) 
			for lb in lbs:
				result.extend(__cut(lb))
		else:
			tmp = re_skip.split(blk)
			result.extend([x for x in tmp if x.strip()!=""])
	return result
