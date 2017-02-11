# Calculating the Mechanical properties of Giant Schwarzites

* For reference on this work see [Mechanical properties of hypothetical graphene foams: Giant Schwarzites](http://www.sciencedirect.com/science/article/pii/S000862231530350X)
* [Tuning the Poisson Ratio of Porous Graphene by Defects](https://github.com/alejandrox1/poisson_lammps/blob/master/nsfposter.pdf)
* For a brief introduction to how to use `Stampede` see [HPC-howto](https://github.com/alejandrox1/HPC-howto)

# Production

This repo is strutured as follows:
* [writeparam.sh](https://github.com/alejandrox1/poisson_lammps/blob/master/writeparam.sh)
 With [parameters.md](https://github.com/alejandrox1/poisson_lammps/blob/master/parameters.md) as a template, `writeparam.sh` will create an input file to run a series of MD calculations.
 The assumed directory structure is that each directory will hold a different Scwarzite alculation and the corresponding `parameters.md` file will be moved to the corresponding subdir.

* [submit_single_stampede.sh](https://github.com/alejandrox1/poisson_lammps/blob/master/submit_single_stampede.sh)
 This sript was set up to submit a [LAMMPS](http://lammps.sandia.gov/) MD calculation to [TACC's Stampede cluster](https://portal.tacc.utexas.edu/user-guides/stampede).
 The input file is based off [parameters.md](https://github.com/alejandrox1/poisson_lammps/blob/master/parameters.md).
 The actual calculation is performed by `stampede_single.sh`
 * [stampede_single.sh](https://github.com/alejandrox1/poisson_lammps/blob/master/stampede_single.sh)
   This will perform the actual MD run on Stampede.
   In order for the script to function, you will need to enter the appropiate `PATHS` for the dependenies and for the struture (`runfiles` and `structures`).
  * Dependenies:
    * [in.elastic](https://github.com/alejandrox1/poisson_lammps/blob/master/in.elastic)
    * [init.mod](https://github.com/alejandrox1/poisson_lammps/blob/master/init.mod)
    * [potential.mod](https://github.com/alejandrox1/poisson_lammps/blob/master/potential.mod)
    * [displace.mod](https://github.com/alejandrox1/poisson_lammps/blob/master/displace.mod)
    * [CH.airebo](https://github.com/alejandrox1/poisson_lammps/blob/master/CH.airebo)


# Analysis
Analysis is very straight forward with using the previously described set up.
You can see sample outputs in [P8 defects](https://github.com/alejandrox1/poisson_lammps/tree/master/p8defects).
For visualization (and instrutions on how to format the results) check out [plot.py](https://github.com/alejandrox1/poisson_lammps/blob/master/p8defects/RESULTS_txt/plot.py)

# Structures
The structures were formated to `atomi` using [VMD's](http://www.ks.uiuc.edu/Research/vmd/) plugin [TopoTools](http://www.ks.uiuc.edu/Research/vmd/plugins/topotools/).
See [schwarzite](https://github.com/alejandrox1/poisson_lammps/tree/master/schwarzite/atomic).
