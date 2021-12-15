from .aux import aux as aux
from .DM18 import DM18 as DM18
from .W14 import W14 as W14
class airsea_fluxes:
    """
    Main class for air-sea flux calculations.
    """

    def __init__(self):
        pass

    def DM18(ustar,hs,alpha,sc_no,anb=1.66e-4,abt=1.1e-5,gamma=5./3.,zeta=4./3., grav=9.81):
        """
        Interface to the DM18 method to compute the air-sea gas transfer velocity
        """
        kwNB_660      = DM18.DM18_KW660_nb(ustar,anb=anb)
        kwB_660       = DM18.DM18_KW660_b( ustar, hs, alpha, sc_no, abt=abt, gamma=gamma, zeta=zeta, grav=grav)
        return kwNB_660+kwB_660

    def W14(u10,c=0.251):
        """
        Interface to Waninkhof 2014 method to compute the air-sea gas transfer velocity
        """
        return W14.W14(u10,c)

    def SchmidtNumber(SST):
        """
        Interface to Schmidt number from SST fit (in degree C)
        """
        return aux.SchmidtNumber(SST)

    def Solubility(SST,SSS):
        """
        Interface to solubility fit from SST and SSS
        """
        return aux.Solubility(SST,SSS)

    def Alpha(K0,SST):
        """
        Interface to non-dimensional solubility alpha from K0 and SST
        """
        return aux.Alpha_Solubility(K0,SST)
