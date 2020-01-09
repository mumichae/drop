import setuptools
import os
import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'wbuild @ git+https://github.com/gagneurlab/wBuild.git@master#egg=wbuild',
    #'wbuild',
    'snakemake==5.5.2',
    'pandas',
]

files = []
for dir_ in ['drop/modules', 'drop/template']:
    for (path, directories, filenames) in os.walk(dir_):
        directories[:] = [d for d in directories if 
                          not (d.startswith('.') or d == 'Data')]
        filenames[:] = [f for f in filenames if 
                        not (f.startswith('.') or f.endswith('.Rproj'))]
        for filename in filenames:
            files.append(os.path.join('..', path, filename))

setuptools.setup(
    name="drop",
    version="0.9.0",
    author="Michaela Müller, Daniela Andrade Salazar",
    author_email="mumichae@in.tum.de",
    description="Detection of RNA Outlier Pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mumichae/drop",
    packages=setuptools.find_packages(include=["drop"]),
    entry_points={'console_scripts': ['drop=drop.cli:main']},
    package_data={'drop': files},
    include_package_data=True,
    install_requires=requirements
)


