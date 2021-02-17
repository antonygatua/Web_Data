# Web Data
This repository contains data from different web sources such as [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) and [twitter](https://twitter.com) and other sites.
Data obtain is processed and analyzed for learning purposes. Works on this repository are:

## Covid-Africa
The source of this data is a table on the wikipedia site. The table contains the country, amount of positive cases, active cases, recoveries and the deaths as a result of covid infections.
The table looks as follow:
| Country       | Confirmed Cases  | Active confirmed cases | Recoveries | Deaths  | Ref.   |
| ------------: | ---------------: | ---------------------: |----------: |-------: |------: |
| South Africa  | 1,491,807        | 55,587                 | 1,388,321  | 47,899  |	[1] |
| Morocco       |   478,474        | 11,145                 |   458,852  |  8,477  |	[1] |
| Tunisia       |   222,504        | 33,369                 |   181,627  |  7,508  |	[1] |

Extracted the table from Wikipedia using **Beautiful Soup** to obtain the table for analysis.
Analysis and visualizations include:
⋅⋅* Countries with the most positive cases.⋅⋅
⋅⋅* Countries with the least positive cases.⋅⋅
⋅⋅* Countries with the highest recovery rate.⋅⋅
⋅⋅* Countries with the least recovery rate.⋅⋅
⋅⋅* Countries with the highest death rate.⋅⋅
⋅⋅* Countries with the lowest death rate.⋅⋅

