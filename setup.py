from distutils.core import setup

setup(
    name='ghtalks',
    version='0.0.1',
    author='Vince Knight',
    author_email=('vincent.knight@gmail.com'),
    packages=['ghtalks', 'ghtalks.tests'],
    scripts=['bin/gh-talks'],
    url='',
    license='The MIT License (MIT)',
    description='Generate a static side with talks',
    install_requires=[
        "pyyaml >= 3.11",
    ],
)
