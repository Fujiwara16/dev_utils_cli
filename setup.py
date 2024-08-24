from setuptools import setup, find_packages

setup(
    name="dev_utils_cli",
    version="0.1",
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'xyz=utils.cli:main',  # This creates the `xyz` command
        ],
    },
    author="Fujiwara",
    author_email="nijmehar16@gmail.com",
    description="A CLI app for developer utils",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Fujiwara16/dev_utils_cli",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
