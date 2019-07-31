import hashlib

str = 'this is a md5 test.'
str2 = 'I am xin ,hello wprld.'

# 创建md5对象
hl = hashlib.md5()

# Tips
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))
print(str+'MD5加密后为 ：' + hl.hexdigest())

hl.update(str2.encode(encoding='utf-8'))
print(str2+'MD5加密后为 ：' + hl.hexdigest())

