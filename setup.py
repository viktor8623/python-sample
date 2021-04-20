from io import open

from setuptools import find_packages, setup

with open('python_sample/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = [
    'atomicwrites==1.3.0',
    'attrs==19.1.0',
    'colorama==0.4.1',
    'future==0.17.1',
    'importlib-metadata==0.20',
    'more-itertools==7.2.0',
    'numpy==1.17.2',
    'packaging==19.1',
    'pandas==0.25.1',
    'pluggy==0.12.0',
    'py==1.10.0',
    'pyparsing==2.4.2',
    'pytest==5.1.2',
    'python-dateutil==2.8.0',
    'python-sample==0.0.1',
    'pytz==2019.2',
    'selenium==3.141.0',
    'six==1.12.0',
    'urllib3==1.25.3',
    'waiting==1.4.1',
    'wcwidth==0.1.7',
    'webium==1.2.1',
    'xlrd==1.2.0',
    'zipp==0.6.0']

setup(
    name='python-sample',
    version=version,
    description='',
    long_description=readme,
    author='Viktor Yenjchak',
    author_email='viktor8623@mail.ru',
    maintainer='Viktor Yenjchak',
    maintainer_email='viktor8623@mail.ru',
    url='https://github.com/_/python-sample',
    license='MIT/Apache-2.0',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
