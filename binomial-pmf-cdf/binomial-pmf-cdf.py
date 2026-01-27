import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    def compute(n, p, k, is_cdf=False):
        result = 0.0
        start = 0 if is_cdf else k
        end = k + 1 if is_cdf else k + 1  
        for i in range(start, end):
            result += comb(n, i, exact=False) * np.pow(p , i) * np.pow((1 - p) ,(n - i))
        return result
           #this is pmf                     this is cdf
    return compute(n,p,k, is_cdf = False), compute(n,p,k, is_cdf = True)
    