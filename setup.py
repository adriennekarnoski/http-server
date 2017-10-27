from setuptools import setup

setup(
    name='httpserver',
    package_dir={'': 'src'},
    py_modules=['httpserver'],
    author='Han Bao and Adrienne Karnoski ',
    author_email='hbao2016@hotmail.com',
    description='http-server from ground up',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    package_dir={"": "src"}
)

