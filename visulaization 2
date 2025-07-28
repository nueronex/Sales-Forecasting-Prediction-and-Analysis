def plot_monthly_avg(df):
    df['Month'] = df['features.csv'].dt.month
    monthly_avg = df.groupby('Month')['Revenue'].mean()

    plt.figure()
    monthly_avg.plot(kind='histogram', color='skyblue')
    plt.title("Average Revenue by Month")
    plt.xlabel("Month Revenue")
    plt.ylabel("Average Revenue")
    plt.tight_layout()
    plt.show()
