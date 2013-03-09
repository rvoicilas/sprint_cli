from distutils.core import setup

from sprint_cli import __version__

setup(
    name='sprint_cli',
    version=__version__,
    author='Radu Voicilas',
    author_email='radu.voicilas@gmail.com',
    license='MIT',
    description='Command line interface to sprint.ly',
    long_description=open('README.md').read(),
    packages=['sprint_cli'],
    scripts=['bin/sprint-cli'],
    classifiers=[
        'Development Status :: 0.1dev',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License'
    ],
)
