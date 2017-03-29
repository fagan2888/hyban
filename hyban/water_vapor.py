#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
from utils import read_hyper

def get_patch_spectra(fname,oname=None):
    """
    Get the patch spectra and write to a csv file.

    :param fname:
        The name of the data cube (e.g., data.raw).

    :param oname: (optional)
        The output name of the csv file.  The default is to replace .raw 
        from the data file with .csv.
    """

    # -- set the output file name
    oname = oname if oname else fname.replace(".raw",".csv")

    # -- read the data cube
    cube = hu.read_hyper(fname)

    # -- set the patch coordinates (the first is sky)
    rr = ((0,160), (1276, 1428), (1009, 1081), (872, 896), (925,948), 
          (901,921))
    cr = ((0,cube.ncol), (474, 521), (826, 846), (747, 760), (733,736), 
          (771,775))

    # -- loop through patches and get spectra
    print("getting patch spectra...")
    specs = np.array([cube.data[:,rr[i][0]:rr[i][1],cr[i][0]:cr[i][1]] \
                          .mean(-1).mean(-1) for i in range(len(rr))])

    # -- save to csv
    print("writing to {0}...".format(oname))
    np.savetxt(oname,np.vstack([cube.waves,specs]).T,delimiter=",")

    return


if __name__=="__main__":

    # # -- June 4, 6, 8, 10 at 15:01
    # dpath = os.path.join(os.path.expanduser("~"),"vegetation","data")
    # flist = ["veg_01125.raw", "veg_01207.raw", "veg_01289.raw", 
    #          "veg_01370.raw"]
    # dates = ["060416_1500", "060616_1500", "060816_1500", "061016_1500"]

    # -- May 31, June 2,4,6  11:00
    dpath = os.path.join("..", "data")
    flist = ["veg_00945.raw", "veg_01027.raw", "veg_01109.raw", 
             "veg_01191.raw", ]
    dates = ["053116_1100", "060216_1100", "060416_1100", "060616_1100"]

    # -- get patch spectra
    for ii,tfile in enumerate(flist):
        oname = tfile.replace(".raw","_{0}.csv".format(dates[ii]))
        get_patch_spectra(os.path.join(dpath,tfile),oname)