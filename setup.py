import setuptools

with open("README.md") as f:
    readme = f.read()

setuptools.setup(
    name="gapminder_example",
    version="0.0.1",
    author="Vini Salazar",
    author_email="17276653+vinisalazar@users.noreply.github.com",
    description="Example Python project with Gapminder data, to be used in Carpentries lessons.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com:vinisalazar/example-python-project",
    packages=setuptools.find_packages(),
    include_package_data=True,
    keywords="example project data-science carpentries",
    python_requires=">=3.6",
    install_requires=["numpy", "matplotlib", "pandas", "seaborn", "pandoc"],
)
