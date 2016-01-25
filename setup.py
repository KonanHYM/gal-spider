from setuptools import setup, find_packages

requires=[
          'requests',
          'PyMySQL',
          'SQLAlchemy',
          'anyjson',
          'ujson==1.33',
          'zope.interface==4.0.5',
          'zope.sqlalchemy==0.7.3',
          'mongoengine',
          'pymongo',
          ]

setup(
      name='weibo',
      version='1.0',
      description='web spider',
      packages = find_packages(),
      zip_safe=False,
      install_packages_data=True,
      install_requires=requires,
      )
