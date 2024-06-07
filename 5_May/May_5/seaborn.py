import seaborn as sns
import matplotlib.pyplot as plt

def generate_violin_plots(data, x, y, hue=None):
    """
    Generate violin plots for comparing distributions across multiple categories.
    
    Parameters:
    - data: DataFrame. Input data.
    - x: str. Column name for the x-axis (category).
    - y: str. Column name for the y-axis (numeric values).
    - hue: str, optional. Column name for grouping data.
    
    Returns:
    - None. Displays the violin plots.
    """
    sns.set(style="whitegrid")  # Set style

    # Create violin plot
    if hue:
        sns.violinplot(x=x, y=y, hue=hue, data=data, split=True, inner="quart", linewidth=1.3)
    else:
        sns.violinplot(x=x, y=y, data=data, inner="quart", linewidth=1.3)
    
    # Adjust plot
    plt.title("Violin Plot")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

# Example usage:
# generate_violin_plots(data=my_data, x='Category', y='Value', hue='Group')
