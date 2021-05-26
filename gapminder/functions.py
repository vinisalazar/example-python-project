"""
File containing package code.
"""

from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

data_dir = "./"
gapminder_all = "gapminder_all.csv"


def load_gapminder_all(custom_file=None):
    if custom_file:
        assert Path(custom_file).exists(), f"File {custom_file} wasn't found."
        file = custom_file
    else:
        file = Path(data_dir).joinpath(gapminder_all)
    return pd.read_csv(file, index_col="country")


def create_df_views(df):
    """
    Splits the 'gapminder_all.csv' DataFrame into separate DFs for gdp, life_exp, and pop.

    Also produces a fourth DF with melted data.
    """

    output = dict()

    for var in "gdpPercap", "lifeExp", "pop":
        var_df = df[[i for i in df.columns if i.startswith(var) or i == "continent"]]
        melt = var_df.melt(
            value_vars=[i for i in var_df.columns if i != "continent"],
            var_name="year",
            value_name=var,
            ignore_index=False,
        )
        melt["year"] = melt["year"].str[-4:]
        output[var] = var_df
        output[var + "_melt"] = melt

    # produce melted dataframe
    cat = pd.concat([v for k, v in output.items() if "melt" in k], axis=1)
    cat = cat.merge(df["continent"], left_index=True, right_index=True)
    cat = cat.loc[:, ~cat.columns.duplicated()]  # remove duplicate year columns
    output["cat"] = cat

    return output["gdpPercap"], output["lifeExp"], output["pop"], output["cat"]


def plot_gdp_growth_by_continent(gdp_df, outdir=".", save=False):
    fig, ax = plt.subplots()
    gb = gdp_df.groupby("continent").mean().T.copy()
    gb.index = [i[-4:] for i in gb.index]
    gb.plot(ax=ax)
    _ = plt.xticks(rotation="vertical")
    _ = plt.ylabel("Mean GDP per capita in USD")
    _ = plt.legend(title="Continent")
    if save:
        plt.savefig(Path(outdir).joinpath("Mean_GDP_by_continent.png"))
    else:
        plt.show()


def plot_gdp_50_years_diff_by_continent(gdp_df, outdir=".", save=False):
    fig, ax = plt.subplots()
    gb = gdp_df[["continent", "gdpPercap_1957", "gdpPercap_2007"]].reset_index().copy()
    gb = gb.melt(
        value_vars=["gdpPercap_1957", "gdpPercap_2007"],
        id_vars=["country", "continent"],
    )
    gb.set_index("country", inplace=True)
    gb.columns = "continent", "Year", "Mean GDP"
    gb["Year"] = gb["Year"].apply(lambda s: s[-4:])
    sns.boxplot(x="continent", y="Mean GDP", hue="Year", data=gb, ax=ax)
    _ = plt.xticks(rotation="vertical")
    _ = plt.xlabel("")
    _ = plt.ylabel("GDP per capita")
    _ = plt.legend(title="Continent")
    if save:
        plt.savefig(
            Path(outdir).joinpath("GDP_growth_by_continent.png"), bbox_inches="tight"
        )
    else:
        plt.show()


def plot_world_development_by_year(cat_df, year="2007", outdir=".", save=False):

    """
    Creates scatter plot of world development for a particular year.

    Uses the `cat` DataFrame outputted from create_df_views.

    From https://www.kaggle.com/tklimonova/gapminder-graph-using-python
    """

    # Input validation
    years = list(cat_df['year'].unique())
    assert year in years, f"No data available for that year. Choose from:\n{years}"

    cat = cat_df.query(f'year == "{year}"')
    np_pop = np.array(cat["pop"])
    np_pop2 = np_pop * 2
    # Use seaborn scatterplot for better customization
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.scatterplot(
        x=cat["gdpPercap"],
        y=cat["lifeExp"],
        hue=cat["continent"],
        size=np_pop2,
        sizes=(20, 400),
        ax=ax,
    )
    _ = plt.grid(True)
    _ = plt.xscale("log")
    _ = plt.xlabel("GDP per Capita [in USD]")
    _ = plt.ylabel("Life Expectancy [in years]")
    _ = plt.title(f"World Development in {year}")
    _ = plt.xticks([1000, 10000, 100000], ["1k", "10k", "100k"])
    if save:
        plt.savefig(Path(outdir).joinpath(f"World_development_in_{year}.png"))
    else:
        plt.show()
