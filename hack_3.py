"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    result = result.upper()
    substitutions = {
        'A': '@',
        'E': '3',
        'I': '¡',
        'O': '0',
        'U': 'v'
    }
    
    return result
