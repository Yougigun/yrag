#############################################
# File Name: setup.py
# Author: Gary
# Mail: s14031403@gmail.com
# Created Time:  2020-8-23 13:51:34 AM
#############################################


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="yrag", # Replace with your own username,
    version="0.1.4",
    author="Gary",
    author_email="s14031403@gmail.com",
    description="Yrag aim to deploy machine-learing model quickly and easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yougigun/yrag",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    entry_points = {
    'console_scripts': [
        'yrag=yrag.yrag_cli:main'
    ]
}
)