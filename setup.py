from distutils.core import setup

import sprint_cli

setup(
    name='sprint_cli',
    version=sprint_cli.__version__,
    packages=['sprint_cli'],
    description='Command line interface to sprint.ly',
    scripts=['bin/sprint-cli'],
    long_description='buuu, have to do',
    author='Radu Voicilas',
    author_email='radu.voicilas@gmail.com')
