import pandas as pd
def temperature_trend(df):
    import matplotlib.pyplot as plt

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # 🔥 FIX: create year column
    df['year'] = df['date'].dt.year

    # Group by year
    yearly = df.groupby('year')['temperature'].mean()

    print(yearly)

    # Plot
    plt.figure()
    yearly.plot(marker='o')
    plt.title("Yearly Temperature Trend")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.grid()
    plt.show()