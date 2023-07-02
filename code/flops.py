import numpy as np

def f_Cholesky(D, P):
    '''
    parameters
    ----------
    D : int
        Total number of potential-field data.
    P : int
        Total number of equivalent sources.

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(D, int) and (D > 0), 'D must be a positive integer'
    assert isinstance(P, int) and (P > 0), 'P must be a positive integer'

    flops = (1/3)*D**3 + 2*D**2 + 2*(P**2 + P)*D

    return flops


def f_CGLS(D, P, ITMAX):
    '''
    parameters
    ----------
    D : int
        Total number of potential-field data.
    P : int
        Total number of equivalent sources.
    ITMAX : int
        Maximum number of iterations in Algorithm (1).

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(D, int) and (D > 0), 'D must be a positive integer'
    assert isinstance(P, int) and (P > 0), 'P must be a positive integer'
    assert isinstance(ITMAX, int) and (ITMAX > 0), 'ITMAX must be a positive integer'

    flops = 2*P*(D+1) + ITMAX*(2*P*(2*D + 3) + 4*D)

    return flops


def f_LS89(M, Dw, Pw):
    '''
    parameters
    ----------
    M : int
        Total number of windows.
    Dw : int
        Total number of potential-field data in a window.
    Pw : int
        Total number of equivalent sources in a window.

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(M, int) and (M > 0), 'M must be a positive integer'
    assert isinstance(Dw, int) and (Dw > 0), 'Dw must be a positive integer'
    assert isinstance(Pw, int) and (Pw > 0), 'Pw must be a positive integer'

    flops = (7/6)*Dw**3 + 4*Pw*Dw**2 + M*2*Pw

    return flops


def f_SU21(M, Dw, Pw):
    '''
    parameters
    ----------
    M : int
        Total number of windows.
    Dw : int
        Total number of potential-field data in a window.
    Pw : int
        Total number of equivalent sources in a window.

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(M, int) and (M > 0), 'M must be a positive integer'
    assert isinstance(Dw, int) and (Dw > 0), 'Dw must be a positive integer'
    assert isinstance(Pw, int) and (Pw > 0), 'Pw must be a positive integer'

    flops = M*((1/3)*Pw**3 + 2*(Dw+1)*Pw**2 + (4*Dw+1)*Pw)

    return flops


def f_C92(D, ITMAX):
    '''
    parameters
    ----------
    D : int
        Total number of potential-field data.
    ITMAX : int
        Maximum number of iterations in Algorithm (1).

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(D, int) and (D > 0), 'D must be a positive integer'
    assert isinstance(ITMAX, int) and (ITMAX > 0), 'ITMAX must be a positive integer'

    flops = D*np.log(D) + ITMAX*(2*D + D*np.log(D))

    return flops


def f_reparam(D, P, Q, ITMAX):
    '''
    parameters
    ----------
    D : int
        Total number of potential-field data.
    P : int
        Total number of equivalent sources.
    Q : int
        Total number of parameters in the reparameterizarized space.
    ITMAX : int
        Maximum number of iterations in Algorithm (1).

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(D, int) and (D > 0), 'D must be a positive integer'
    assert isinstance(P, int) and (P > 0), 'P must be a positive integer'
    assert isinstance(Q, int) and (Q > 0), 'Q must be a positive integer'
    assert isinstance(ITMAX, int) and (ITMAX > 0), 'ITMAX must be a positive integer'

    flops = 2*Q*(D*P+D+1) + 2*P*Q + ITMAX*(2*Q*(2*D + 3) + 4*D)

    return flops


def f_SOB17(D, ITMAX):
    '''
    parameters
    ----------
    D : int
        Total number of potential-field data.
    ITMAX : int
        Maximum number of iterations in Algorithm (1).

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(D, int) and (D > 0), 'D must be a positive integer'
    assert isinstance(ITMAX, int) and (ITMAX > 0), 'ITMAX must be a positive integer'

    flops = 2*D**2 + 2*D + ITMAX*(2*D**2 + 3*D)

    return flops


def f_TOB20(D, ITMAX, lambda_FFT=5):
    '''
    parameters
    ----------
    D : int
        Total number of potential-field data.
    ITMAX : int
        Maximum number of iterations in Algorithm (1).
    lambda_FFT : int
        Scale factor related to the FFT algorithm. We consider lambda_FFT=5, which is
        compatible with radix2-FFT algorithm.

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(D, int) and (D > 0), 'D must be a positive integer'
    assert isinstance(ITMAX, int) and (ITMAX > 0), 'ITMAX must be a positive integer'
    assert isinstance(lambda_FFT, int) and (lambda_FFT > 0), 'lambda_FFT must be a positive integer'

    flops = lambda_FFT*(16*D)*np.log(4*D) + 26*D + ITMAX*(lambda_FFT*(16*D)*np.log(4*D) + 58*D)

    return flops


def f_deconv(D, lambda_FFT=5):
    '''
    parameters
    ----------
    D : int
        Total number of potential-field data.
    lambda_FFT : int
        Scale factor related to the FFT algorithm. We consider lambda_FFT=5, which is
        compatible with radix2-FFT algorithm.

    returns
    -------
    flops : int
        Total number of flops.
    '''
    assert isinstance(D, int) and (D > 0), 'D must be a positive integer'
    assert isinstance(lambda_FFT, int) and (lambda_FFT > 0), 'lambda_FFT must be a positive integer'

    flops = lambda_FFT*(12*D)*np.log(4*D) + 72*D

    return flops


