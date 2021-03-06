try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = "Apache PredictionIO"
__email__ = "user@predictionio.apache.org"
__copyright__ = "Copyright 2017 The Apache Software Foundation"
__license__ = "Apache License, Version 2.0"

setup(
    name='PredictionIO',
    version="0.9.10",
    author=__author__,
    author_email=__email__,
    packages=['predictionio'],
    url='http://predictionio.apache.org/',
    license='LICENSE.txt',
    description='PredictionIO Python SDK',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    long_description="""PredictionIO Python SDK

                       PredictionIO is a prediction server for building smart
                       applications. While you search data through a database
                       server, you can make prediction through PredictionIO.

                       With PredictionIO, you can write apps

                       - that predict user behaviors based on solid data
                         science
                       - using your choice of state-of-the-art machine
                         learning algorithms
                       - without worrying about scalability

                       Detailed documentation is available on our
                       `documentation site <http://predictionio.apache.org/>`_.

                       This module provides convenient access of the
                       PredictionIO API to Python programmers so that they
                       can focus on their application logic.
                       """,
    install_requires=["pytz >= 2014.2", ],
)
