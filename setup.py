from setuptools import setup, find_packages

setup(
    name='serializer',
    version='1.0',
    author="Yan Mikhniuk",
    author_email="yan.mihnuk@gmail.com",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'serializer = console_app:main',
        ],
    }
)