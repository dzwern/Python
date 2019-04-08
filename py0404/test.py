import requests
import re
import matplotlib.pyplot as plt

reponse = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
list1 = reponse.text

# print(list1)


result = re.search(r'<tbody class="tbody_right" id="datalist">(.*?)</tbody>', list1, re.S)
# print(result.group(1))

# result2=re.search(r'<tr>(.*?)</tr>',result)
# print(result2.group(1))

result1 = re.findall(r'<tr>(.*?)</tr>', result.group(1))
# print(result1[0])

with open('test.txt','w',encoding='utf-8')as file_test:
    for r in result1:
        # print(r)
        # print('/n')
        r1 = re.findall(r'<td.*?>(.*?)</td>', r)
        # print(r1[0],r1[1],r1[2])
        # print(r1[1])

        # result3=re.search(r'<td (.*?)>(.*?)</td><td (.*?)>(.*?)</td><td (.*?)>(.*?)</td>', r)
        # print(result3.group())

        result4 = re.search('<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', r1[0])
        id = result4.group(1)

        result5 = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', r1[1], re.S)
        name = result5.group(2)

        result6 = re.search(r'<span class="red">(.*?)</span>', r1[2])
        price = result6.group(1)
        infos=name+' '+price
        # info="id:"+str(id)+ "name:"+str(name)+"price:"+str(price)
        file_test.write(infos)
        file_test.write('\n')

        # print(type(infos))

filename='test.txt'
x,y=[],[]
with open(filename,'r',encoding='utf-8')as f:
    lines=f.readlines()
    for line in lines:
        value=[str(s)for s in line.split()]
        x.append(value[0])
        y.append(value[1])

print(x)
print(y)

# print(z)
plt.bar(range(len(x)),y)

plt.show()

# print(type(price))
# print(price)
# plt.hist(price)
# plt.show()
