import pandas as pd 


def infoo(df):
    """Return summary information for each column in the DataFrame."""
    info_df = pd.DataFrame({
        "num_of_nulls": df.isnull().sum(),
        "perc_of_nulls": (df.isnull().sum() / len(df) * 100).round(2),
        "num_of_unique": df.nunique(),
        "data_type": df.dtypes.astype(str),
        "count_of_notnull": df.notnull().sum()
    })
    return info_df

    return info_df

