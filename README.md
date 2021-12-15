# airsea_fluxes  

This package includes varoius methods for computing the air-sea gas transfer velocity using the methods from Deike and Melville, 2018 and from Wanninkhof 2014.  

## Installation (existing environment)  

To install from source:  
```  
pip install -e .  
```  

### Creating a clean conda install with minimal external packages  

This package utilizes numpy libraries for functionality of the fluxes software.  Notebooks and other tests may require additional packages, such as xarray and matplotlib.  To create a clean conda environment with the minimum required packages follow:  
```  
conda create -n airsea_fluxes numpy  
conda activate airsea_fluxes  
```  

You can then activate the airsea_fluxes environment and follow the installation instructions into an existing environment as above.  


### Optional additional packages to use all scripts and notebooks:  

```  
conda install matplotlib jupyter netcdf4 xarray ipykernel  
```  

A reminder, Jupyter environments can be added with:  
```  
python -m ipykernel install --user --name airsea_fluxes --display-name "airsea_fluxes"  
```  

## Instructions for using the installed package  

More examples coming, a brief tests is given in notebook form in the Sample folder.  
