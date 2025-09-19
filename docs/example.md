---
hide:
  - navigation
---

# Example

To illustrate the practical application of the FAIR PBK standard, the EuroMix generic PBK model from [Tebby et al. (2020)](https://doi.org/10.1016/j.fct.2020.111440) was re-implemented in compliance with the standard. A brief description of this re-implementation is provided below. The full model code is available on [GitHub](https://github.com/rivm-syso/euromix-to-sbml).

## Re-implementation in Antimony

The EuroMix generic PBK model was originally coded in the MCSim language and shared as supplementary material alongside the scientific paper presenting the model. The model was re-implemented in Antimony. Antimony was selected because it offers robust tools for converting models to and from SBML.

To translate the model to Antimony, the differential equations were manually converted to transfer equations as used in Antimony. The names of the model elements were kept consistent with the original implementation wherever possible, facilitating comparison between the original MCSim model and the Antimony re-implementation.

The 13 states of the MCSim model were mapped to chemical species in the Antimony, which were arranged into 12 compartments, with the liver compartment containing two species (modelling the amount of the chemical and the amount metabolized in the liver).

Internal model parameters/variables tracking the compartment volumes were mapped to the compartments themselves, which represent physical volumes in Antimony/SBML. Also the parameters and internal assignments were translated, as much as possible, in a one-to-one manner to parameters in the Antimony re-implementation. However, in order to comply with criterion G01, all hardcoded dosing parameters of the original implementation were excluded from the model.

![alt text](EuroMix_Generic_PBK_Reimplementation.svg "EuroMix PBK Re-implementation")

## Model annotation

Annotations of the model and its element are specified in a separate CSV file. This annotations file links the different model elements (e.g., compartments and parameters) to ontological terms and specifies the units of measure Although the Antimony language also allows specification of units and annotations in the model code itself, maintaining these in a separate CSV file makes the code better readible.

## SBML conversion

Conversion to an annotated SBML file is done automatically using the SBML PBK workflow. This workflow follows several steps. It first converts the Antimony model implementation to SBML. Then, it annotates this SBML file using the annotations specified in the euromix.annotations.csv file. After this, it runs validation scripts on the generated SBML file to check for consistency and completeness (e.g, of the units). Finally, it publishes the generated SBML file (and log files) as build artifacts and adds/updates the generated/updated SBML file.

## Publication on Zenodo

TODO
