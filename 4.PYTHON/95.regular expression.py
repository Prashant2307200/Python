import re

pattern = r"[A-Z]+yclone"
patLen = len(pattern)
text = '''My name is Harry Cyclone ,Harry cyclone is a good Dyclone boy'''

matches = re.finditer(pattern, text)
for match in matches:
    subMatch = match.span() #tuple
    for idx,i in enumerate(subMatch):
        if(idx%2 != 0):
            continue
        print(text[i:i+6])

'''
[] : char class
^  : begning
$  : end
.  : ch except new line
?  : occ = {0,1}
|  : any one
*  : occ = [0,infinity]
+  : occ = [1,infinity]
{} : no of occ
() : enclose grm of res
'''