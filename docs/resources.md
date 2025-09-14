---
hide:
  - navigation
---

## FAIR enabling resources

The following resources provide the building blocks of the FAIR PBK standard:

- **[SBML](https://sbml.org/):** Use of the [Systems Biology Markup Language (SBML)](https://sbml.org/) as a harmonized publication and exchange format for PBK models, which should bridge the gap between the various different model implementation languages that are currently used by PBK model developers.
- **[PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko):** Use of the (currently being developed) [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko) for annotation of all model elements (e.g., compartments, species, parameters).
- **[ChEBI](https://www.ebi.ac.uk/chebi/):** Use of the [ChEBI](https://www.ebi.ac.uk/chebi/) ontology for chemical identifiers to relate PBK model substance applicability domain, chemical species, and chemical-specific parameters to chemicals.
- **[NCBI Taxonomy Database](https://www.ncbi.nlm.nih.gov/taxonomy):** Use of the [NCBI Taxonomy Database](https://www.ncbi.nlm.nih.gov/taxonomy) to link the model applicability domain to controlled terminology for animal species.

## FAIR PBK tools

The below list of tools supporting the FAIR PBK standard:

- **[FAIR PBK Inspector](https://mcra.test.wur.nl/fairpbk):** An online tool to help and annotating and validating SBML (or Antimony) PBK model implementations for compliance with the FAIR PBK standard.
- **[SBML PBK Utils](https://github.com/jwkruisselbrink/sbml-pbk-utils):** A small Python package that contains utility functions for FAIR PBK model implementation in SBML. It provides a number of utility functions and classes for annotating, validating and running SBML PBK models.
- **[SBML PBK Workflow](https://github.com/jwkruisselbrink/sbml-pbk-workflow):** GitHub workflow for automated generation of annotated SBML files from Antimony PBK model implementations combined with annotations provided in CSV file annotations.

## FAIR PBK models

The below lists open source PBK models that are developed to comply with the FAIR PBK standard:

- **[EuroMix PBK re-implementation](https://github.com/rivm-syso/euromix-to-sbml/):** FAIR PBK re-implementation of the EuroMix PBK model in Antimony.
- **[PFAS PBK model](https://github.com/rivm-syso/pfasPBK):** PFAS PBK model implementation in Antimony based on the PFOA and PFOS PBK model by Loccisano et al. (2011) and the subsequently modified version thereof by Westerhout et al. (2024).
- **[FAIR PBK Demonstration models](https://github.com/rivm-syso/pbk-demo-models):** A collection simple PBK model implementations in Antimony demonstrating how different modelling choices that are possible can be translated to PBK model implementations in Antimony.



## Generic resources

The resources below are not specific to the FAIR PBK standard, but are more generic tools for the development of FAIR PBK models:

- **[SBMLutils](https://github.com/matthiaskoenig/sbmlutils):** This python package provides convenient utilities for manipulation and annotation of SBML models. It also serves as a major source of inspiration of the [SBML PBK Utils](https://github.com/jwkruisselbrink/sbml-pbk-utils) package, which is tailored to the sub-domain of PBK models.
- **[libSBML](https://github.com/sbmlteam/python-libsbml):** This python package provides the essential functionality for manipulating SBML models in python. For instance, for enriching SBML model implementations with annotations, units and descriptions of the model elements.
