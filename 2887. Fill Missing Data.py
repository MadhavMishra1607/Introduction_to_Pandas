import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    df = products.fillna(0)
    return df