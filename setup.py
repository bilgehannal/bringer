from setuptools import setup
import io

# pandoc is not installed, fallback to using raw contents
with io.open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = 'bringer',
    version = '0.1.3',
    packages = ['bringer'],
    license = 'MIT',
    description = 'You can find the basic and usable scripts, code blocks or informations via using your command line with bringer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Bilgehan NAL',
    author_email = 'bilgehannal@gmail.com',
    url = 'https://github.com/bilgehannal/bringer',
    keywords = ['programming', 'helper', 'find'],
    install_requires=[
        'bios'
    ],
    entry_points = {
        'console_scripts': [
            'bringer = bringer.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)