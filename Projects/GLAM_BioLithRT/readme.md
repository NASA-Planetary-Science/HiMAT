## Authors
- Dr. Roberto Furfaro - Professor, Systems and Industrial Engineering, University of Arizona, Tucson, AZ
- Mr. Enrico Schiassi - PhD Student, Systems and Industrial Engineering, University of Arizona, Tucson, AZ
- Dr. Jeffrey S. Kargel, Senior Scientist, Planetary Science Institute, Tucson, AZ

## Installation and run of GLAM_BioLithRT

- Download and install a recent version of Matlab (from R2015a on)
- all the files needed to run the code (data base - w/ input spectra  -, Matlab functions, and Matlab script) must be in the same folder (in any location)
- The Input Spectra are taken from the data base in the folder DATA available in WASI4 package (http://www.ioccg.org/data/software.html)

## Major files
- main.m : script to enter the input and run the code
- AOP_Rs.m: function to simulate the Remote sensing reflectance (Rrs) given the required input
- InvModeBioLithRT.m: function to compute the objective function for the constrained optimization for water components concentration retrieval

## Notes

- the code is in source format (i.e. no GUI is provided). The user has access and can modify all the scripts and the functions provided according to his/her tasks (where GLAM BioLithRT can accomplish those)
- if any modifications are done in AOP_Rs.m, the same modifications must be done in InvModeBioLithRT.m, and viceversa 
- more details and instructions are provided in the presentation/user manual available w/ the code
- please contact the authors if: need any more details explanation or have any questions, discovered a  bug, have suggestions of comment to improve the code, to be informed about updates and status

e-mail: eschiassi@email.arizona.edu ( or enrico.schiassi90@gmail.com)

