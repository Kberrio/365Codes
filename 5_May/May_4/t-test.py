import numpy as np
from scipy import stats

def perform_t_test(sample1, sample2, alpha=0.05):
    """
    Performs a t-test to determine if the differences between two samples are significant.
    
    Arguments:
    sample1 : array-like
        The first sample data.
    sample2 : array-like
        The second sample data.
    alpha : float, optional
        The significance level, default is 0.05.
        
    Returns:
    t_statistic : float
        The t-statistic value.
    p_value : float
        The p-value.
    """
    # Convert samples to numpy arrays
    sample1 = np.array(sample1)
    sample2 = np.array(sample2)
    
    # Calculate means and standard deviations
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    std1 = np.std(sample1, ddof=1)
    std2 = np.std(sample2, ddof=1)
    
    # Calculate t-statistic
    n1 = len(sample1)
    n2 = len(sample2)
    dof = n1 + n2 - 2
    pooled_std = np.sqrt(((n1 - 1) * std1 ** 2 + (n2 - 1) * std2 ** 2) / dof)
    t_statistic = (mean1 - mean2) / (pooled_std * np.sqrt(1 / n1 + 1 / n2))
    
    # Calculate p-value
    p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), dof))
    
    # Determine significance
    if p_value < alpha:
        print("The difference between the two samples is statistically significant (p < {:.3f})".format(alpha))
    else:
        print("The difference between the two samples is not statistically significant (p >= {:.3f})".format(alpha))
    
    return t_statistic, p_value

# Example usage
sample1 = [15, 20, 25, 30, 35]
sample2 = [10, 22, 28, 32, 38]
t_statistic, p_value = perform_t_test(sample1, sample2)
print("t-statistic:", t_statistic)
print("p-value:", p_value)
