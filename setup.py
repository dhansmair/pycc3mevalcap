from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    readme = fh.read()


setup(
    name='pycc3mevalcap',
    version='0.0.1',
    maintainer='dhansmair',
    description="Conceptual Captions 3M Caption Evaluation for Python 3",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/dhansmair/pycc3mevalcap",
    packages=find_packages(),
    install_requires=[
        'pycocoevalcap'
        ],
    python_requires='>=3.6'
)
