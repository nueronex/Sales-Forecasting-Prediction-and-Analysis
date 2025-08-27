def plot_correlation_heatmap(df):
  df_numeric_dtypes(include=['int64', 'float64'])
  corr = df_numeric.corr()

  plt.figure()
  sns.heatmap(corr, annot = True,cmap='coolwram',fmt=".2f")
  plt.title("Correlation of the heathmap of montly Revenue of Per month")
  plt.show()
