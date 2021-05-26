## Example Python package

This package was created to be used in the
[Python Packaging Publishing](https://carpentries-incubator.github.io/python-packaging-publishing/)
lesson of the [Carpentries Incubator](https://github.com/carpentries-incubator/). It is supposed to represent a typical
Python project that is a bit messy and needs to be organised.

The project is a data analysis project on the Gapminder dataset, that is also used in the
[Python Novice Gapminder](http://swcarpentry.github.io/python-novice-gapminder/) lesson. There are
a few different types of files:
* raw data files;
* analysis notebooks;
* Python files with pre-made functions;
* auxiliary files such as this README.

The goal here is to try and make the project a little more organised. Feel free to create directories, move files
around, and rename them.

Checklist:
- [ ] create `paper.md` file simulating a project doc.
- [x] create `gapminder.py` file with functions to load and plot the data.
- [ ] create `knit.py` script to generate the paper.
- [ ] create `setup.py` install script to install the two Python files.
- [x] create `demonstration.ipynb` notebook to demonstrate imports from `functions.py`
- [x] create `.png` figure files that go in the paper.
