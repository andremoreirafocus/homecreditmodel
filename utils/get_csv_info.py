import dask.dataframe as dd
from pathlib import Path
from IPython.display import display

from utils.get_file_info import get_file_sizes


def get_df_with_csv_info(filename: Path) -> dd.DataFrame:
    get_file_sizes(filename)
    df = dd.read_csv(str(filename))
    pdf = df.compute()
    display(pdf.head())
    pdf.info()
    display(pdf.describe())
    null_counts = pdf.isnull().sum()
    null_pct = (null_counts / len(pdf) * 100).round(2)
    display(
        null_counts.to_frame("null_count")
        .assign(null_pct=null_pct)
        .query("null_count > 0")
        .sort_values("null_count", ascending=False)
    )
    return df
