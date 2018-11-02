from lark import Lark

grammar = Lark('''
start: IDENTIFIER "(" arguments ")"

arguments: expr ("," expr)*

?expr: STRING

%import common.CNAME -> IDENTIFIER
%import common.ESCAPED_STRING -> STRING
''')


def parse(inp):
    return grammar.parse(inp)
