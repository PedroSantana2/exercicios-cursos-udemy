'''
Considere a lista a seguir, que apresenta dados referentes a série temporal de 1900 a 2020. Faça o que se pede:



lista_anos=[1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 
            1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 
            1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 
            1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 
            1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939,
            1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 
            1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 
            1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 
            1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 
            1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 
            1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 
            1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 
            1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 
            2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
            2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
            2020]
 


a) Crie uma lista que armazene os 20 primeiros anos da série;

b) Crie uma lista que armazene os anos de 1937 a 1969;

c) Crie uma lista que armazene os anos de 2010 a 2020;

d) Crie uma lista que armazene o último ano da série;

e) Apresente a série temporal de 10 em 10 anos.
'''
lista = list(range(1900, 2021))
lista_a = lista[0:20]
lista_b = lista[lista.index(1937):lista.index(1969) + 1]
lista_c = lista[lista.index(2010):lista.index(2020) + 1]
lista_d = lista[-1]
lista_e = lista[::10]
