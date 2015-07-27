from distutils.core import setup

setup(
    name='ghtalks',
    version='0.0.3',
    author='Vince Knight',
    url='https://github.com/drvinceknight/ghtalks',
    author_email=('vincent.knight@gmail.com'),
    packages=['ghtalks', 'ghtalks.tests'],
    scripts=['bin/gh-talks'],
    license='The MIT License (MIT)',
    description='Generate a static site with your slide decks',
    install_requires=[
        "pyyaml >= 3.11",
    ],
)
