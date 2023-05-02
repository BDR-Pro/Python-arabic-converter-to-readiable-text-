from setuptools import setup

setup(
    name="arabic",
    version="1.0.0",
    description="arabic python text converter to readiable format",
    author="BDR-PRO",
    author_email="baderalotaibi3@gmail.com",
    install_requires=[
        "arabic_reshaper>=3.0.0",
        "python-bidi>=0.4.2",
    ],
)
