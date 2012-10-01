from distutils.core import setup  
setup(name='finalseg',  
      version='0.12',  
      description='Chinese Words Segementation Utilities',  
      author='Sun, Junyi',  
      author_email='ccnusjy@gmail.com',  
      url='http://github.com/fxsjy',  
      packages=['finalseg'],  
      package_dir={'finalseg':'finalseg'},
      package_data={'finalseg':['*.*']}
)  
