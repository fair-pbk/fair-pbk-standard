---
hide:
  - navigation
---

# Example

To illustrate the practical application of the FAIR PBK standard, the EuroMix generic PBK model from [Tebby et al. (2020)](https://doi.org/10.1016/j.fct.2020.111440) was re-implemented in compliance with the standard. A brief description of this re-implementation is provided below. The full model code is available on [GitHub](https://github.com/rivm-syso/euromix-to-sbml).

## Re-implementation in Antimony

The EuroMix generic PBK model was originally coded in the MCSim language and shared as supplementary material alongside the scientific paper presenting the model. The model was re-implemented in Antimony. Antimony was selected because it offers robust tools for converting models to and from SBML.

To translate to Antimony, differential equations were manually converted to transfer equations, used in Antimony. In order to comply with criterion G01, all hardcoded dosing parameters of the original implementation were excluded from the model.

## Model annotation

Annotations of the model and its element are specified in a separate CSV file. This annotations file links the different model elements (e.g., compartments and parameters) to ontological terms and specifies the units of measure Although the Antimony language also allows specification of units and annotations in the model code itself, maintaining these in a separate CSV file makes the code better readible.

## SBML conversion

Conversion to an annotated SBML file is done automatically using the SBML PBK workflow. This workflow follows several steps. It first converts the Antimony model implementation to SBML. Then, it annotates this SBML file using the annotations specified in the euromix.annotations.csv file. After this, it runs validation scripts on the generated SBML file to check for consistency and completeness (e.g, of the units). Finally, it publishes the generated SBML file (and log files) as build artifacts and adds/updates the generated/updated SBML file.

## Publication on Zenodo

TODO
