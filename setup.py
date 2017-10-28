from setuptools import setup

setup(
    name='httpserver',
    package_dir={'': 'src'},
    py_modules=['httpserver'],
    author='Han Bao and Adrienne Karnoski ',
    author_email='hbao2016@hotmail.com',
    description='http-server from ground up',
    install_requires=['gevent==1.1.0', 'greenlet==0.4.9'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']},
)
