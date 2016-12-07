import os
import sys

from distutils.sysconfig import get_python_lib
from setuptools import find_packages, setup


setup(
    name='pdf-image-to-text',
    version='0.0.1',
    url='https://github.com/MEEM-MLHD/pdf-image-to-text',
    author='Samuel Goldszmidt',
    author_email='samuel.goldszmidt@gmail.com',
    description='Convert a PDF made of images to text',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    scripts=['pdf-image-to-text.py'],
    install_requires=['pdfminer.six==20160615', 'Pillow==3.4.2', 'pyocr==0.4.3'],
    dependency_links = ['https://github.com/MEEM-MLHD/pdfminer/tarball/6537e0853c8e616e60ba2af227624ed469d80d1e#egg=pdfminer.six-20160615', ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)


