
from setuptools import setup, find_packages

setup(name='keith',
      packages=find_packages(),
      setup_requires=['pytest-runner==4.2'],
      tests_require=['pytest==3.9.3']
        )


