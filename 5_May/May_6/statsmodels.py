import numpy as np

def linear_trend(x):
    """ Fit a linear trend to a time series """
    n = len(x)
    t = np.arange(n)
    p = np.polyfit(t, x, 1)  # Fit a 1st degree polynomial
    return p[0] * t + p[1]  # Return the trend line

def remove_trend(x, trend_line):
    """ Remove the trend from the time series """
    return x - trend_line

def seasonal_adjustment(x, season_length):
    """ Adjust the time series to remove seasonality """
    n = len(x)
    season_averages = np.array([np.mean(x[i::season_length]) for i in range(season_length)])
    adjusted_seasons = np.tile(season_averages, n // season_length + 1)[:n]
    return x - adjusted_seasons

def reconstruct_series(detrended, trend, seasonality):
    """ Reconstruct the original series from detrended data """
    return detrended + trend + seasonality

# Example usage
data = np.array([np.sin(2 * np.pi * t / 365) + 0.5 * t for t in range(1000)])  # Hypothetical data
trend_line = linear_trend(data)
detrended_data = remove_trend(data, trend_line)
seasonally_adjusted_data = seasonal_adjustment(detrended_data, 365)

# Reconstruction (if needed)
reconstructed_data = reconstruct_series(seasonally_adjusted_data, trend_line, seasonally_adjusted_data + trend_line - data)
