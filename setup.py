from setuptools import setup
setup(
    name = 'bringer',
    version = '0.0.1',
    packages = ['bringer'],
    entry_points = {
        'console_scripts': [
            'bringer = bringer.__main__:main'
        ]
    })