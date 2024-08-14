"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    
    if 'ziman' in result:
        new_str = result.replace('ziman', '-')
    else:
        new_str = result    
    return result
