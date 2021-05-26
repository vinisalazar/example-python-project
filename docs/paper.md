---
author: "Data Carpentry"
title: "Example document file"
---

## Example document file

### Introduction

It is common that Python packages or data projects have associated documents, regardless if they are
actual documentation for the code or miscellaneous documents that may include analyses, reports, or 
recorded experiments.

### Results

For the Gapminder package, for example, we could have a scientific paper showcasing the data.
We could present the figures we generated with our package, such as the mean GDP growth by continent:

![Line graph showing mean GDP per capita by continent over the years.](./Mean_GDP_by_continent.png)

Or the growth in GDP after 50 years:

![Box plot comparing GDP per capita by continent between the years of 1957 and 2007.](./GDP_growth_by_continent.png)

We could end our paper with a figure about the state of World Development in the year of 2007:

![Scatter plot with GDP per capita in the 'x' axis and life expectancy in the 'y' axis.
 Countries are colored by continent.](./World_development_in_2007.png)

### Discussion

If we have a Markdown with links to our figures, we may want to compile it, as PDF or HTML, for example.
For that we are going to use an additional script, `knit.py`.