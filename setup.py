import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='data_augmentation_GASPLN',
    packages=['data_augmentation_GASPLn'],
    version='0.0.1',
    license='GPL-3.0',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Artur Melchiori Cerri',
    author_email='arturmelchiori@gmail.com',
    url='https://github.com/amcerri/data-augmentation-GASPLN', 
    project_urls = {                                
        'Bug Tracker': 'https://github.com/amcerri/data-augmentation-GASPLN/issues'
    },
    install_requires=['nltk', 'pandas', 'pyarrow', 'numpy', 'translators'],                        
    keywords=["pypi", "data_augmentation", "nlp"],
    classifiers=[ # https://pypi.org/classifiers
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    include_package_data=True,
    package_data={'': ['data/*.parquet']},
    
    download_url="https://github.com/amcerri/data-augmentation-GASPLN/archive/refs/tags/0.0.1.tar.gz",
)