import matplotlib.pyplot as plt

def plot_column(df, column_name):
    """
    Diya gaya column ka histogram plot karta hai.
    """
    try:
        df[column_name].hist()
        plt.title(f"Distribution of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.show()
    except Exception as e:
        print(f"❌ Error in plotting: {e}")
