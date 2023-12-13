from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

setup(
    name='expectation-helper',
    version='0.0.3',
    description='Helpers for working with Great Expectations',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/expectation-helper',
    download_url='https://github.com/kenjyco/expectation-helper/tarball/v0.0.3',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=requirements,
    include_package_data=True,
    package_dir={'': '.'},
    package_data={
        '': ['*.ini'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    keywords=['data', 'expectation', 'great expectations', 'gx', 'cli', 'command-line', 'helper', 'kenjyco']
)
