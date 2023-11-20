#10. Importe a biblioteca pandas, leia um arquivo CSV (por exemplo, "dados.csv") eexiba as primeiras linhas do DataFrame.

import pandas as pd

df = pd.read_csv("dados.csv")

print(df.head())