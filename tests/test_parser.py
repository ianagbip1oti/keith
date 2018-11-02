from keith.parser import parse

from lark.lexer import Token
from lark.tree import Tree


def test_parse_hello_world():
    p = 'print("hello world")'

    assert parse(p) == Tree('start', [
        Token('IDENTIFIER', 'print'),
        Tree('arguments', [Token('STRING', '"hello world"')])
    ])
