import matplotlib.pyplot as plt

class CustomPlot:
    def __init__(self):
        pass

    def line_graph(self, x_data, y_data, title='', x_label='', y_label=''):
        plt.plot(x_data, y_data)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def bar_chart(self, categories, values, title='', x_label='', y_label=''):
        plt.bar(categories, values)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

# Example usage:
if __name__ == "__main__":
    custom_plot = CustomPlot()
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 3, 5, 7, 11]
    custom_plot.line_graph(x_data, y_data, title='Example Line Graph', x_label='X-axis', y_label='Y-axis')

    categories = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 25]
    custom_plot.bar_chart(categories, values, title='Example Bar Chart', x_label='Categories', y_label='Values')
