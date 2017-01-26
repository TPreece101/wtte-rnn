# Python functions
def weibull_cdf(t, a, b):
    t = np.double(t)+1e-35
    return 1-np.exp(-np.power(t/a,b))

def weibull_hazard(t, a, b):
    t = np.double(t)+1e-35
    return (b/a)*np.power(t/a,b-1)

def weibull_pdf(t, a, b):
    t = np.double(t)+1e-35
    return (b/a)*np.power(t/a,b-1)*np.exp(-np.power(t/a,b))

def weibull_cmf(t, a, b):
    t = np.double(t)+1e-35
    return weibull_cdf(t+1, a, b)

def weibull_pmf(t, a, b):
    t = np.double(t)+1e-35
    return weibull_cdf(t+1.0, a, b)-weibull_cdf(t, a, b)

def weibull_mode(a, b):
    mode = a*np.power((b-1)/b,1/b)
    mode[b<=1]=0
    return mode

def weibull_mean(a, b):
    from scipy.special import gamma
    return a*gamma(1.0+1.0/b)

def weibull_quantiles(a, b, p):
    return a*np.power(-np.log(1-p),1/b)


def weibull_continuous_logLik(t, a, b, u=1):
    # With equality instead of proportionality. 
    return u*np.log(weibull_pdf(t, a, b))+(1-u)*np.log(1-weibull_cdf(t, a, b))

def weibull_discrete_logLik(t, a, b, u=1):
    # With equality instead of proportionality. 
    return u*np.log(weibull_pmf(t, a, b))+(1-u)*np.log(1-weibull_cdf(t+1, a, b))
