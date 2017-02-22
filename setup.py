import os
import codecs
from setuptools import setup

def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

setup(
    name='ctdata_sots_cli',
    description='CLI tool for preparing and publishing CT Secretary of State data',
    long_description=read('README.rst'),
    url='https://github.com/CT-Data-Collaborative/ctdata-sots-cli',
    author='Sasha Cuerda',
    author_email='scuerda@ctdata.org',
    license='MIT',
    version='0.1',
    py_modules=['ctdata_sots_sli'],
    install_requires=[
        'click>=6.7',
        'PyYaml==3.12',
        'SQLAlchemy==1.1.5',
        'psycopg2==2.6.2',
        'python-dotenv==0.6.3'
        ],
    entry_points={
        'console_scripts': [
            'sots = ctdata_sots_cli.__main__:main',
            ]
        },
    )