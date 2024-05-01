import matplotlib.pyplot as plt
import numpy as np

def detect_outliers(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return outliers

def create_box_plot(data):
    outliers = detect_outliers(data)
    fig, ax = plt.subplots()
    ax.boxplot(data)

    if outliers:
        ax.plot(np.ones_like(outliers), outliers, 'ro', label='Outliers')

    ax.legend()
    plt.show()

# Example usage:
data = np.random.normal(loc=0, scale=1, size=100)
data[5] = 10  # Adding an outlier

create_box_plot(data)
