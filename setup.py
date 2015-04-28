from setuptools import setup

setup(
    name='smibbler',
    version='0.1',
    py_modules=['smibbler'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        smibbler=smibbler:smibbler
    ''',
)
