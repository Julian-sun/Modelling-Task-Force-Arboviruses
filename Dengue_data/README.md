
# Dengue dataset characteristics.

The first step to understand the process data of diseases are collected is searching the definition of a case. We use data from the Brazilian National Notifiable Diseases Information System (SINAN). We further separated the cases into confirmed and discarded, following the final classification information as used by the Brazilian Ministry of Health. Confirmed cases are all suspected cases of the disease, excluding those discarded or inconclusive. This classification can be based on clinical/epidemiological criteria, namely presence of clinical symptoms in the same area and time as other probable cases, or on clinical/laboratory criteria, namely the presence  of clinical symptoms and a positive IgM ELISA result, viral RNA detection via PCR, NS1 viral antigen detection, or positive viral culture. Discarded cases are defined as any suspected case that satisfies at least one of the following criteria: negative laboratory diagnosis (IgM serology); a laboratory confirmation of another disease; clinical and epidemiological compatibility with other diseases. Still, there are inconclusive cases that were assigned as one of the designations before. 

## Dengue final classification

In table 1 we present the values for the variable "class_fin", which changes over time. The values in the variable classify the reported cases on SINAN according to 1-Dengue Clássico, 2 - Dengue com Complicações, 3 - Febre Hemorrágica do Dengue, 4 -Síndrome do choque da Dengue, 5 - Descartado, 10- Dengue, 11- Dengue com Sinais de Alarme, 12- Dengue Grave, 8 - Inconclusivo.  

| Classifiction per year                             | 2000  | 2001   | 2002   | 2003   | 2004  | 2005   | 2006   | 2007   | 2008   | 2009   | 2010   | 2011   | 2012   | 2013    | 2014   | 2015    | 2016    | 2017   | 2018   |
|----------------------------------------------------|-------|--------|--------|--------|-------|--------|--------|--------|--------|--------|--------|--------|--------|---------|--------|---------|---------|--------|--------|
| 1                                                  | 98646 | 285163 | 473912 | 223874    | 62701 | 126985 | 220338 | 340223 | 385924 | 306859 | 851325 | 589753 | 395819 | 1179584 | 46474  | 66051   | 36361   | 0      | 0      |
| 10                                                 | 0     | 0      | 0      | 0      | 0     | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 2376    | 420052 | 1299671 | 1054112 | 164396 | 143184 |
| Total "Dengue classico"                            | 98646 | 285163 | 473912 | 223874    | 62701 | 126985 | 220338 | 340223 | 385924 | 306859 | 851325 | 589753 | 395819 | 1181960 | 466526 | 1365722 | 1090473 | 164396 | 143184 |
| 2                                                  | 530   | 666    | 4789   | 2605   | 646   | 1367   | 2110   | 4103   | 20327  | 7961   | 14114  | 8206   | 3643   | 5989    | 301    | 222     | 54      | 0      | 0      |
| 11                                                 | 0     | 0      | 0      | 0      | 0     | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 14      | 8418   | 21966   | 9658    | 2864   | 2968   |
| Total "Dengue com sinais de alarme (complicações)" | 530   | 666    | 4789   | 2605   | 646   | 1367   | 2110   | 4103   | 20327  | 7961   | 14114  | 8206   | 3643   | 6003    | 8719   | 22188   | 9712    | 2864   | 2968   |
| 3                                                  | 173   | 783    | 2597   | 863    | 154   | 510    | 864    | 1828   | 4369   | 2587   | 3649   | 2943   | 1030   | 1282    | 46     | 39      | 13      | 0      | 0      |
| 4                                                  | 1     | 11     | 42     | 55     | 6     | 15     | 37     | 83     | 133    | 91     | 158    | 115    | 54     | 123     | 6      | 10      | 3       | 0      | 0      |
| 12                                                 | 0     | 0      | 0      | 0      | 0     | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 0      | 2       | 761    | 1825    | 1027    | 344    | 342    |
| Total "Dengue Grave"                               | 174   | 794    | 2639   | 918    | 160   | 525    | 901    | 1911   | 4502   | 2678   | 3807   | 3058   | 1084   | 1407    | 813    | 1874    | 1043    | 344    | 342    |
| Total "Dengue descartado (5)"                      | 36131 | 101584 | 193604 | 137309 | 64493 | 110355 | 144466 | 216477 | 281601 | 188911 | 354145 | 353708 | 352987 | 561799  | 344140 | 697432  | 782305  | 275235 | 154668 |
| Total "Inconclusivo (8)"                           | 455   | 3686   | 4456   | 2904   | 539   | 1687   | 2297   | 139767 | 195160 | 75353  | 130151 | 96431  | 186772 | 271365  | 96874  | 310162  | 412224  | 75169  | 58733  |
| Total null values                                  | 36919 | 96697  | 217693 | 48861  | 8328  | 20582  | 40910  | 14706  | 31932  | 20365  | 27723  | 78587  | 9875   | 108130  | 26444  | 3794    | 238     | 5996   | 14116  |

# Objective 

The files presented in this folder can be used to:

 * extract variables of the original dataset to perform specific studies, filtered according to the classifications of a case;
 * clean and aggregate the data to be used in statistical/ mathematical models.

# References

[1] Oliveira, Juliane F and Rodrigues, Moreno S. and Skalinski, Lacita M. and Santos, Aline ES and Costa, Larissa C. and Cardim, Luciana L. and Paixão, Enny S. and Costa, Maria da Conceição N. and Oliveira, Wanderson K. and Barreto, Maurício L. and Teixeira, Maria Glória and Andrade, Roberto F. S. 
*Interdependence between confirmed and discarded cases of dengue, chikungunya and Zika viruses in Brazil: A multivariate time-series analysis*, doi 10.1101/708743, https://www.biorxiv.org/content/early/2019/07/20/708743, bioRxiv, 2019.
