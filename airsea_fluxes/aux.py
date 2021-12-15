import numpy as np

class aux:
    def __init__(self):
        pass

    def SchmidtNumber(SST,
                      c1=2116.8,
                      c2=-136.25,
                      c3=4.7353,
                      c4=-0.092307,
                      c5=0.000755
                  ):
        """
        Compute the Schmidt number from the SST in Celcius

        Input
        SST: Sea surface temperature, Celcius

        Returns:
        Non-dimensional Schmidt number
        """
        return c1+c2*SST+c3*SST**2+c4*SST**3+c5*SST**4

    def Alpha_Solubility(K0, SST, Atm2Pa = 101325., R = 8.314):
        """
        Computes the non-dimensional solubility from solubility and SST
        R=8.314 #kg m2/s2/mol/K                                                                                                        
        """
        return K0*R*SST/Atm2Pa

    def Solubility(
            SST, SSS,
            a1=-58.0931,a2=90.5069,a3=22.2940,b1=0.027766,b2=-0.025888,b3=0.0050578
    ):
        """
        Computes the solubility from the SST and SSS
        """
        return (np.exp(a1+a2*(100./SST)+a3*np.log(SST/100.)+SSS*(b1+b2*SST/100.+b3*(SST/100.)**2.))*1000.)
