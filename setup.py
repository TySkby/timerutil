from setuptools import setup
import sys


def get_long_description():
    with open('README.md') as fh:
        description = fh.read()
    return description


def get_test_requirements():
    test_requirements = []
    if sys.version_info < (3, 3):
        test_requirements = ['mock']
    return test_requirements


setup(
    name='wp-timerutil',
    version='1.0.0',
    url='https://github.com/tylerhendrickson/timerutil',
    author='Tyler Hendrickson',
    author_email='hendrickson.tsh@gmail.com',
    description='A handy collection of timer-related utilities for Python',
    long_description=get_long_description(),
    packages=['timerutil'],
    zip_safe=True,
    tests_require=get_test_requirements(),
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
