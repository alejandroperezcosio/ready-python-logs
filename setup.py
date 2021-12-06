import setuptools

setuptools.setup(
    name='ready-python-logs',
    version='0.3',
    author="Alejandro Perez Cosio",
    author_email="alejandroperezcosio@gmail.com",
    url="https://github.com/alejandroperezcosio/ready-python-logs",
    license='MIT',
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires= [
        'rpyconfig @ git+https://github.com/alejandroperezcosio/ready-python-config.git#egg=rpyconfig'
    ],
    dependency_links=[
        'http://github.com/user/repo/tarball/master#egg=rpyconfig'
    ]
)