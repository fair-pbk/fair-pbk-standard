---
hide:
  - navigation
---

## FAIR enabling resources

The following resources provide the building blocks of the FAIR PBK standard.

## Ontologies and standards

The FAIR PBK standard builds upon existing standards and ontologies.

| Resource | Description |
|---|---|
| [SBML](https://sbml.org/) | The Systems Biology Markup Language (SBML) is the selected harmonized exchange format for PBK models. |
| [PBPKO](https://github.com/InSilicoVida-Research-Lab/pbpko) | Ontology for annotation of PBK model elements (compartments, species, parameters). |
| [ChEBI](https://www.ebi.ac.uk/chebi/) | Chemical Entities of Biological Interest: ontology for chemical identifiers. |
| [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy) | Database for controlled terminology of animal species. |

## FAIR PBK tools

The tools in the table below support development of PBK models compliant with the FAIR PBK standard.

| Resource | Description |
|---|---|
| [SBML PBK Utils](https://github.com/jwkruisselbrink/sbml-pbk-utils) | Small Python package with utilities for annotating, validating, and running SBML PBK models. |
| [SBML PBK Workflow](https://github.com/jwkruisselbrink/sbml-pbk-workflow) | GitHub Actions workflow to generate annotated SBML files from Antimony PBK implementations using CSV annotations. |

## FAIR PBK models

The table below lists open source PBK models that are developed to comply with the FAIR PBK standard.

| Model | Description |
|---|---|
| [EuroMix PBK re-implementation](https://github.com/rivm-syso/euromix-to-sbml/) | FAIR PBK re‑implementation of the EuroMix PBK model in Antimony. |  |
| [PFAS PBK model](https://github.com/rivm-syso/pfasPBK) | Antimony implementation of PFAS PBK kinetics based on Loccisano et al. (2011) with subsequent modifications by Westerhout et al. (2024). |
| [FAIR PBK Demonstration models](https://github.com/rivm-syso/pbk-demo-models) | Collection of small Antimony PBK example models illustrating different modelling choices and translations to PBK implementations. |


## Generic tools and resources

The resources below are not specific to the FAIR PBK standard, but are more generic tools for the development of FAIR PBK models.

| Resource | Description |
|---|---|
| [SBMLutils (Python)](https://github.com/matthiaskoenig/sbmlutils) | Python utilities for manipulation and annotation of SBML models; a major source of inspiration for the SBML PBK Utils package. |
| [libSBML (Python)](https://github.com/sbmlteam/python-libsbml) | Official Python bindings for libSBML providing core functionality to create, manipulate, annotate, validate, and read/write SBML models. |
