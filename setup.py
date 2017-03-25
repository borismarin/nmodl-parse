from setuptools import setup

setup(name='nmodl',
      version='0.1',
      description='NMODL parser',
      url='http://github.com/borismarin/nmodl-parse',
      author='Boris Marin',
      author_email='borimsarin@gmail.com',
      license='GLP3',
      packages=['nmodl'],
      zip_safe=False,
      setup_requires=['pytest-runner'],
      install_requires=['pyparsing'],
      tests_require=['pytest', 'pyparsing'],
)