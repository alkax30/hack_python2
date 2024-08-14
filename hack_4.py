"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    result = result.lower()
    
    if result.startswith("f"):
        return result[1:-1]
    elif result.startswith("b"):
        return result[1:-1]
    else:
        return result
