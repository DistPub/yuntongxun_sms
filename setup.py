import sys
from setuptools import find_packages
from setuptools import setup


setup(
    name='yuntongxun_sms',
    description='python sdk to use yuntongxun sms service',
    url='https://github.com/ugoodspeed/yuntongxun_sms',
    version='2.7.0',

    platforms='linux',
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],

    packages=find_packages('.', exclude=('DEMO',)),
)
