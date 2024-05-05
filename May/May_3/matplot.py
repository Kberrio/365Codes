import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets

# Generate some random data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the initial plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

line1, = ax1.plot(x, y1, 'r-')
line2, = ax2.plot(x, y2, 'b-')

ax1.set_title('Sine Wave')
ax2.set_title('Cosine Wave')

# Function to update the plots based on user input
def update_plot(amplitude=1.0, frequency=1.0):
    new_y1 = amplitude * np.sin(frequency * x)
    new_y2 = amplitude * np.cos(frequency * x)
    
    line1.set_ydata(new_y1)
    line2.set_ydata(new_y2)
    
    fig.canvas.draw()

# Create sliders for user interaction
amplitude_slider = widgets.FloatSlider(value=1.0, min=0.1, max=2.0, step=0.1, description='Amplitude:')
frequency_slider = widgets.FloatSlider(value=1.0, min=0.5, max=2.0, step=0.1, description='Frequency:')

# Arrange the widgets
widgets.interactive(update_plot, amplitude=amplitude_slider, frequency=frequency_slider)