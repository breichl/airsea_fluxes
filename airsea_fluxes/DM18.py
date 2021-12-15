import numpy as np

class DM18:
    def __init__(self):
        pass

    def DM18_KW660_nb(
            ust,
            anb=1.66e-4
    ):
        """
        Computes the non-bubble component of kw_660.

        Inputs
        anb - a non-dimensional coefficient between the transfer velocity and friction velocity
        ust - friction velocity, in units of m/s for output kw_660 in units of m/s

        Returns
        kw_660_nb - the transfer velocity in units of ust (usually m/s)
        """
        return (anb*ust)

    def DM18_KW660_b(
            ust, hs, alpha, sc,
            abt=1.1e-5, gamma=5./3., zeta=4./3., grav=9.81
    ):
        """
        Computes the bubble component of kw_660/

        Inputs
        ust: Friction velocity, m s^{-1}
        hs: Significant wave height, m
        abt: Coefficient 1.1e-5, # s^2 m^{-2}
        alpha: Non-dimensional diffusivity
        Sc: Non-dimensional Schmidt number
        gamma: scaling parameter (see DM18)
        zeta: scaling parameter (see DM18)

        """
        ab = abt * np.sqrt(sc/660.)
        
        return ( ab * ust**gamma * np.sqrt(grav*hs)**zeta / alpha )
