from lark import Lark
from lark.indenter import Indenter

import os


class PythonIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = ['LPAR', 'LSQB', 'LBRACE']
    CLOSE_PAREN_types = ['RPAR', 'RSQB', 'RBRACE']
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 8


parser = Lark.open(
    'grammar.lark', rel_to=__file__, postlex=PythonIndenter(), parser='lalr')


def parse(inp):
    return parser.parse(inp)
