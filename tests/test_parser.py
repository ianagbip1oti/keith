from keith.parser import parse

from lark.lexer import Token
from lark.tree import Tree

hello_world_print = Tree('function_call', [
    Token('IDENTIFIER', 'print'),
    Tree('arguments', [Tree('literal', [Token('STRING', '"hello world"')])])
])


def test_parse_hello_world():
    p = 'print("hello world")'

    assert parse(p) == Tree('compound_expr', [hello_world_print])


def test_parse_hello_world_multi():
    p = """
print("hello world")
print("hello world")
"""

    assert parse(p) == Tree('compound_expr',
                            [hello_world_print, hello_world_print])


def test_parse_hello_world_comment():
    p = """
print("hello world") # This is a comment
"""

    assert parse(p) == Tree('compound_expr', [hello_world_print])
