from setuptools import setup

setup(
    name='phpipamsdk',
    version='1.3.post2',
    description='A PHPIPAM REST API Client',
    url='https://github.com/efenian/phpipamsdk',
    author='Eric Donohue',
    packages=['phpipamsdk', 'phpipamsdk.controllers'],
    zip_safe=False,
    install_requires=['requests']
)
