import re

s1 = "hello world"

# 开头的匹配
# result=re.match("h",s1)
# 搜索匹配
# result=re.search("l",s1)
# 全局匹配
# result = re.fullmatch("hello world", s1)
# 返回的是列表
# result=re.findall("l",s1)
# 得到的是一个列表
# result=re.split("ll",s1,3)
# 替换字符串
# result=re.sub("l","pp",s1)
# 返回的形式迭代器
result = re.finditer("l", s1)

print(result)
for r in result:
    # print(result)
    # print(result.group())
    print(r)

# if isinstance(result,re.Match):
# g1=result.group()
s2 = "helloworld\nhi\nhellowold"
print(s2)
pat = re.match("h", re.M | re.I)
print(pat)
