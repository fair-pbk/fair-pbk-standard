---
hide:
  - navigation
  - toc
---

# About

This FAIR PBK standard is currently being developed in an explorative manner to evaluate how to obtain a truly harmonised and interoperable exchange format for models, and to develop and test a strategy/standard for annotation of terms and units specifically for PBK models. The aim is to adopt and/or align with already existing initiatives as much as possible. 

At present, the following resources are considered essential for building up a standard for FAIR PBK modelling:

## Resources

- **[SBML](https://sbml.org/):** Use of the [Systems Biology Markup Language (SBML)](https://sbml.org/) as a harmonized publication and exchange format for PBK models, which should bridge the gap between the various different model implementation languages that are currently used by PBK model developers.
- **[PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko):** Use of the (currently being developed) [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko) for annotation of all model elements (e.g., compartments, species, parameters).
- **[ChEBI](https://www.ebi.ac.uk/chebi/):** Use of the [ChEBI](https://www.ebi.ac.uk/chebi/) ontology for chemical identifiers to relate PBK model substance applicability domain, chemical species, and chemical-specific parameters to chemicals.
- **[NCBI Taxonomy Database](https://www.ncbi.nlm.nih.gov/taxonomy):** Use of the [NCBI Taxonomy Database](https://www.ncbi.nlm.nih.gov/taxonomy) to link the model applicability domain to controlled terminology for animal species.
- **[UBERON](https://obophenotype.github.io/uberon/about/):** Use of the [UBERON](https://obophenotype.github.io/uberon/about/) ontology for relating PBK model compartments to the biological entities they represent.
- **[UCUM](https://ucum.org/) and [QUDT](https://qudt.org/):** Alignment with the [Unified Code for Units of Measure (UCUM)](https://ucum.org/) and the [QUDT Ontologies](https://qudt.org/) for annotation of units, combined with the facilities for specification of units available in SBML.

## Tools

The below list of tools supporting the FAIR PBK standard:

- **[FAIR PBK Inspector](https://mcra.test.wur.nl/fairpbk):** An online tool to help and annotating and validating Antimony or SBML PBK model implementations for compliance with the FAIR PBK standard.
- **[SBML PBK workflow](https://github.com/jwkruisselbrink/sbml-pbk-workflow):** GitHub workflow for automated generation of annotated SBML files from Antimony PBK model implementations combined with annotations provided in CSV file annotations.
- **[SBML PBK Utils](https://github.com/jwkruisselbrink/sbml-pbk-utils):** A small Python package that contains utility functions for FAIR PBK model implementation in SBML. It provides a number of utility functions and classes for annotating, validating and running SBML PBK models.

## Generic tools

The tools below are not specific to the FAIR PBK standard, but are more generic tools for the development of FAIR PBK models:

- **[SBMLutils](https://github.com/matthiaskoenig/sbmlutils):** This python package provides convenient utilities for manipulation and annotation of SBML models. It also serves as a major source of inspiration of the [SBML PBK Utils](https://github.com/jwkruisselbrink/sbml-pbk-utils) package, which is tailored to the sub-domain of PBK models.
- **[libSBML](https://github.com/sbmlteam/python-libsbml):** This python package provides the essential functionality for manipulating SBML models in python. For instance, for enriching SBML model implementations with annotations, units and descriptions of the model elements.
