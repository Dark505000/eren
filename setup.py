from setuptools import setup, find_packages


setup(
    name='eren',
    version='0.6',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='hhhuuuooo94@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Dark505000/eren/edit/main/setup.py',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
