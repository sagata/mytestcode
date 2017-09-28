#coding=utf8
import re

#re.match 尝试从字符串的开始匹配一个模式，如：下面的例子匹配第一个单词。 
def match_test():
	text = "JGood is a handsome boy, he is cool, clever, and so on..."
	m = re.match(r"(\w+)\s", text)
	if m:
		print m.group(0), '\n', m.group(1)
	else:
		print 'not match'  
	m.group(1)


match_test()