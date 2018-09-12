import re

print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>"))
#result:['h1']
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>").group())
#result:<h1>hello</h1>
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>").groupdict())
#result:{'tag_name': 'h1'}
print(re.search(r"<(\w+)>\w+</(\w+)>","<h1>hello</h1>").group())
#result:<h1>hello</h1>
print(re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>").group())
#result:<h1>hello</h1>




