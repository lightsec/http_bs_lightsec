"""
Created on Nov 10, 2014

@author: Aitor Gómez Goiri <aitor.gomez@deusto.es>

To install/reinstall/uninstall the project and its dependencies using pip:
     pip install ./
     pip install ./ --upgrade
     pip uninstall httpbsliblightsec
"""
from setuptools import setup  # , find_packages

setup(name="httpbsliblightsec",
      version="0.1",
      description="Sample HTTP server for a base station following the lightsec protocol.",
      # long_description = "",
      author="Aitor Gomez-Goiri",
      author_email="aitor.gomez@deusto.es",
      maintainer="Aitor Gomez-Goiri",
      maintainer_email="aitor.gomez@deusto.es",
      url="https://github.com/lightsec/http_bs_lightsec",
      # license = "http://www.apache.org/licenses/LICENSE-2.0",
      platforms=["any"],
      package_dir={
          '': 'src',
      },
      packages=["httplightsec"],
      install_requires=["liblightsec", "Flask-SQLAlchemy", "Flask-Login", "Flask-Admin"],
      entry_points={
          'console_scripts': [
              'run-basestation = httplightsec.run:main',
          ],
      },
)