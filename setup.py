from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in research_app/__init__.py
from research_app import __version__ as version

setup(
	name="research_app",
	version=version,
	description="research_app",
	author="harsh",
	author_email="harsh.t@korecent.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
