"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if len(s) == 1:
        return s
    
    result = []

    for txt in range(len(s)):
        if txt % 2 == 0:
            result.append(str(txt + 1))
        else:
            result.append(txt + 1)

    return result
