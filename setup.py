from distutils.cmd import Command
from setuptools import find_packages, setup


class YapfCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import yapf
        yapf.main(['yapf', '--recursive', '--in-place', 'setup.py', 'tests'] +
                  find_packages())


setup(
    name='keith',
    packages=find_packages(),
    cmdclass={'yapf': YapfCommand},
    install_requires=['lark-parser==0.6.5'],
    setup_requires=['pytest-runner==4.2', 'yapf==0.24.0'],
    tests_require=['pytest==3.9.3'])
