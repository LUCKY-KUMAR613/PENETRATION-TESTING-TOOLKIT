from data_loader import load_csv
from analyzer import get_summary
from plotter import plot_column

# Step 1: Data load karo
df = load_csv("sample.csv")

if df is not None:
    # Step 2: Summary analysis
    print(get_summary(df))

    # Step 3: Plot a column
    plot_column(df, df.columns[0])
