from keith.parser import parse

from lark.lexer import Token
from lark.tree import Tree


def identifier(i):
    return Token('IDENTIFIER', i)


def parameters(*args):
    return Tree('parameters', [identifier(a) for a in args])


hello_world_print = Tree('function_call', [
    identifier('print'),
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


def test_parse_hello_world_function():
    p = """
def hello_world():
   print("hello world")
"""

    assert parse(p) == Tree('compound_expr', [
        Tree('function_def', [
            identifier('hello_world'),
            parameters(),
            Tree('compound_expr', [hello_world_print])
        ])
    ])


def test_parse_hello_world_function_with_parameters():
    p = """
def hello_world(a, b):
   print("hello world")
"""

    assert parse(p) == Tree('compound_expr', [
        Tree('function_def', [
            Token('IDENTIFIER', 'hello_world'),
            parameters('a', 'b'),
            Tree('compound_expr', [hello_world_print])
        ])
    ])
