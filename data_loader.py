import pandas as pd

def load_csv(file_path):
    """
    CSV file load karta hai aur pandas DataFrame return karta hai.
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully.")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
