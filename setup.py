import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
os.chdir(os.path.normapth(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-fluxbb',
    version='0.1',
    packages=['fluxbb'],
    include_package_data=True,
    liscense='GPLv2',
    description='Django app to interface with fluxbb',
    long_description=README,
    url='http://github.com/kalhartt/django-fluxbb',
    author='kalhartt',
    author_email='kalhartt@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet : :WWW/HTTP'
    ]
)
