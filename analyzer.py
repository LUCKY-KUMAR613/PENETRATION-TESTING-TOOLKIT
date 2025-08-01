def get_summary(df):
    """
    DataFrame ka summary (mean, std, min, max) deta hai.
    """
    try:
        summary = df.describe()
        print("📊 Summary generated.")
        return summary
    except Exception as e:
        print(f"❌ Error in analysis: {e}")
        return None
