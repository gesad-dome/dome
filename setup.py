import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text2system",                     # This is the name of the package
    version="0.0.5",                        # The initial release version
    author="Anderson Martins Gomes",                     # Full name of the author
    author_email='andersonmg@gmail.com',
    url='https://github.com/andersonmgomes/text2system',
    description="A self-adaptative architecture implementation.",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),   # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=['aiengine'
                ,'analyticsengine'
                ,'autonomouscontroller'
                ,'businessprocessengine'
                ,'domainengine'
                ,'externalservice'
                ,'integrationengine'
                ,'interfacecontroller'
                ,'multchannelapp'
                ,'user'
                , 'securityengine'],             # Name of the python package
    
    package_dir={'':'src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)