import yapf
from setuptools import find_packages


def test_format():
    assert 0 == yapf.main(
        ['yapf', '--diff', '--recursive', 'setup.py', 'tests'] +
        find_packages())
