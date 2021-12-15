import numpy as np

class W14:
    def __init__(self):
        pass

    def W14(
            u10,
            c=0.251
    ):
        """
        Computes the 

        Inputs
        anb - a non-dimensional coefficient between the transfer velocity and friction velocity
        ust - friction velocity, in units of m/s for output kw_660 in units of m/s

        Returns
        kw_660_nb - the transfer velocity in units of ust (usually m/s)
        """
        return  (c * u10**2)
