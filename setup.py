from setuptools import setup, find_packages

setup(
    name='bullet_cli',
    version='0.0.1',
    author="monkeyliu",
    description='watch stock in Terminal',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bullet = bullet_cli.main:cli',
        ],
    },
)
