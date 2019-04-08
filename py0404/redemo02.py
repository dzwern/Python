# 单个字符串的匹配

import re

# result=re.findall(".","hello \n world",flags=re.M)
# print(result)

result = re.findall("[012].ello", "0hello 1ello 2 ello")
print(result)


result1=re.findall("\dhello","hello 1hello 0hello")
print(result1)

result2=re.findall("\Dhello","xhello 1hello 5hello")
print(result2)

result3=re.findall("\shello", " hello    hello")
print(result3)


result4=re.findall("\wello","hello we_ello ^ello")
print(result4)


