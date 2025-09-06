from setuptools import setup, find_packages

setup(
    name="data-eating-storage-mysql",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python",
    ],
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    description="A MySQL storage solution for data eating operations",
    license="MIT",
    python_requires=">=3.6",
)