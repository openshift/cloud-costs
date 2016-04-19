import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'boto',
    'fa.jquery',
    'mysql-python',
    'paramiko',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_fanstatic',
    'pyramid_formalchemy',
    'pyramid_tm',
    'python-dateutil',
    'pyyaml',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    ]

setup(name='budget',
      version='0.1',
      description='budget',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='budget',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = budget:main
      [console_scripts]
      initialize_budget_db = budget.scripts.initializedb:main
      """,
      )
