#coding:utf-8
import hmac,hashlib
import base64

result = hmac.new('test', 'test', hashlib.sha384).hexdigest()
print result
result = hmac.new('1234', '1234', hashlib.sha384).hexdigest()
print result
result = hmac.new('test123', 'test123', hashlib.sha384).hexdigest()
print result
result = hmac.new('', 'test', hashlib.sha384).hexdigest()
print result
result = hmac.new('test', '', hashlib.sha384).hexdigest()
print result

print "分隔符1"
result = hmac.new('_/[]@$%^&~(', '_/[]@$%^&~(', hashlib.sha384).hexdigest()
print result


test = '我擦的'.decode("UTF-8").encode('gbk')


result = hmac.new(test, test, hashlib.sha384).hexdigest()
print result

print "分隔符2"
test = '⊙●○①⊕◎Θ⊙¤㊣△√ ∩¤々♀♂∞①ㄨ≡↘↙┗┛╰☆╮ ℡'.decode("UTF-8").encode('gbk')
result = hmac.new(test, test, hashlib.sha384).hexdigest()
print result

result = hmac.new("12345678901234567890123456789012345678901234567890", "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890", hashlib.sha384).hexdigest()
print result

#   $at call_txe lpc_hmac_encrypt("12345678901234567890123456789012345678901234567890", "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890","sha384")

md5 = hashlib.sha512()
md5.update('test')
print md5.hexdigest()