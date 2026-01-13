from setuptools import setup

with open("README.md","r",encoding="utf-8")as fh:
    long_discription=fh.read()

AUTHOR_NAME='Shruti'
SRC_REPO='scr'
LIST_OF_REQUIREMENTS=['streamlit']


setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email="shruti.katulkar2@gmail.com",
    description='A simple python movie recommendation',
    long_description=long_discription,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)
