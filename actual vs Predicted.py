import matplotlib.pyplot as plt

def plot_actual_vs_predicted(y_actual, y_predicted, title="Actual vs Predicted"):
    plt.figure(figsize=(10, 6))
    plt.plot(y_actual, label='Actual', marker='o')
    plt.plot(y_predicted, label='Predicted', marker='x')
    plt.title(title)
    plt.xlabel('Samples')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
