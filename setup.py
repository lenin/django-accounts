from setuptools import setup, find_packages

version = '0.5.1'

LONG_DESCRIPTION = """
User accounts
--------------------------
"""

setup(
    name='django-accounts',
    version=version,
    description="django-accounts",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='accounts,django',
    author='Lenin Yee',
    author_email='lenin.ayr@gmail.com',
    url='http://github.com/lenin/django-accounts',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
