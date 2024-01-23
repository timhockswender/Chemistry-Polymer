# Aspects of Polymer Chemistry 
This is (hopefully) a series of scripts that encompass many aspects of Polymer Chemistry.
There is a strong overlap with math and engineering in this area and I will ilustrate what I expect are some useful concepts and techniques.

The first script will serve as the template for the kinetic modeling of the polymerization of monomers in solution.
The processes involved are quite straightforward.The model was based on the work [AKS] that ispublically available.
The script integrates the equations for reaction of initiator, monomer and polymer formation along with molecular weight calculations.
The results fit the original paper and are comfirmed by a modern, reaction modeling commercial code[PREDICI].

The second model was developed to support the hypothesis that the set of differential equations developed for AKS would work for all solution polymerizations. These results fuly support the hypothesis. The generated files and plots match the original paper: Molecular Weight Control of a Batch Polymerization Reactor: Experimental Study Ind.Eng.Chem.Res. 1999, 38, 38, 144-153.
The authors are Jhy-Shyong Chang and Po-Hsun Liao, hence the file name "Chang_Liao14" though the number underestimates the numbr of veersions!

BONUS: I have uploaded various plotting routines that have been useful. I will update as new onesare added.
The simplest usage is to include them in the directory in which one is working, use via 'import'. They do assume a specific order for the solution developed by solve_ivp. Some hints in the files but the order of the solution array exactly matches the returned values from the function which is being integrated.

A new notebook has been added to continue exploring the utility of the standard moment mode calculatios provided with the  [AKS] ntebook.
This model was developed to support the hypothesis that the set of differential equations developed for [AKS] would work for all solution polymerizations.
These results fuly support the hypothesis with one major caveat or note:
The moment names in this paper (aka Dhooge) are reversed from those in [AKS]
No effort was made to check the authors use/non-use of a factor of two in some equatins related to the termination constant, kt.
The generated files and plots match the original paper.
  "Modeling of Bulk and Solution Radical Polymerization..."
  Macromol. Theory Simul. 2020, 29, 2000065


