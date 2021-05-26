import argparse
from pathlib import Path

from .functions import (
    load_gapminder_all,
    create_df_views,
    plot_gdp_growth_by_continent,
    plot_gdp_50_years_diff_by_continent,
    plot_world_development_by_year,
)


def main(custom_file, plots, outdir="."):

    print("Loading data.")
    df = load_gapminder_all(custom_file=custom_file)

    # create views
    print("Creating views.")
    gdp, life_exp, pop, cat = create_df_views(df)

    if plots:
        abs_path = Path(outdir).absolute()
        print(f"Creating plots in '{abs_path}'.")
        print("Plotting mean GDP by continent.")
        plot_gdp_growth_by_continent(gdp, outdir, save=True)
        print("Plotting GDP growth by continent.")
        plot_gdp_50_years_diff_by_continent(gdp, outdir, save=True)
        print("Plotting World Development scatter plot.")
        plot_world_development_by_year(cat, outdir, save=True)
        print("Done.")

    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Print statistics of the Gapminder dataset."
    )
    parser.add_argument(
        "-f", "--file", help="Path to Gapminder file.", default=None, required=False
    )
    parser.add_argument(
        "-p",
        "--plots",
        help="Whether to generate plots (default is False).",
        action="store_true",
    )
    parser.add_argument(
        "-o", "--outdir", help="Output directory for plots", default=".", required=False
    )
    args = parser.parse_args()
    main(args.file, args.plots, args.outdir)
