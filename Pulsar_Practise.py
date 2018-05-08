"""Tbh I have no idea"""
'''Load the dynamic spectra'''
#import astropy.units as u
import numpy as np
dir = '/mnt/scratch-lustre/simard/b0834/data/'
nt = 660
nf = 16384*4
I = np.zeros([2,nf,nt],dtype=complex)
for i in range(4):
    for g in ['0','1','6']:
        I[0,i*nf//4:(i+1)*nf//4,:]+=np.fromfile(dir+'/Ar-Ar/freq0'+str(i)+'/gate'+g+'.bin',
                                        np.float32).reshape(-1,nf//4).T
        I[1,i*nf//4:(i+1)*nf//4,:]+=np.fromfile(dir+'/Gb-Gb/freq0'+str(i)+'/gate'+g+'.bin',
                                        np.float32).reshape(-1,nf//4).T
f = (np.arange(nf)*8.*4./nf+310.5)*u.MHz
t = (np.arange(nt)*6729./nt)*u.s




