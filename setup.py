from setuptools import setup

setup(
    name="http-server",
    description="Socket Echo Server.",
    authors='Han & Adrienne',
    py_modules=['server, client'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    package_dir={"": "src"}
)