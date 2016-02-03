import badger
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

build_requires = []

tests_require = []

packages=find_packages()


metadata = dict(name='badger',
                maintainer='Nick Kypreos',
                maintainer_email='',
                description='',
                license='',
                url='',
                version=badger.__version__,
                download_url='',
                long_description='',
                packages=packages,
                entry_points={
                          'console_scripts': [
                              'badger=badger.badger:badger'
                          ]
                },
                install_requires=build_requires,
                build_requires=build_requires,
                tests_require=tests_require)

setup(**metadata)

