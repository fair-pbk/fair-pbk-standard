---
hide:
  - navigation
---

# FAIR PBK Standard

Physiologically Based Kinetic (PBK) models are models for simulating the absorption, distribution, metabolism, and excretion of chemicals in living systems. To maximize their impact, PBK models should not only be scientifically sound but also FAIR — Findable, Accessible, Interoperable, and Reusable. The **FAIR PBK standard** provides **a structured set of rules for publishing PBK models** in a way that ensures long-term (re)usability. These rules cover technical aspects (e.g., file formats, metadata, annotations) and contextual aspects (e.g., provenance, licensing, documentation). By following this standard standard, PBK model developers ensure their work is transparent, reproducible, and reusable for future applications.

## Guiding principle

A guiding principle of the FAIR PBK standard is the acknowledgment that developers are, and always will be, using different modelling software and coding standards when creating PBK models. The standard is not intended to replace how PBK models are developed and implemented, but rather to provide a harmonized framework for publishing them, making models easier for other developers to reuse. For this, the FAIR PBK standard adopts the [Systems Biology Markup Language (SBML)](https://sbml.org/) as a common/harmonized exchange format, complemented with rules for annotating model units and model elements.

The figure below illustrates the workflow for PBK model developers and model users. PBK model developers, on the left of the figure, develop models using the modelling software/language of their own preference. When publishing (versions of) developed PBK models, the modellers can convert their model to an annotated FAIR PBK model to make it interoperable and reusable, and publish it on a repository to make it findable and accessible. Model (re)users can, on the right side of the figure, can find and access models via the repositories, and import and use the interoperable and reusable format within their own environment.

![alt text](FAIR_PBK_workflow.png "FAIR PBK workflow")

## Scope

The FAIR standard applies to PBK model definitions — the structural representations of the models. It does not cover specific parametrisations (i.e., specific values for parameters like physiological parameters and partition coefficients) and dosing scenarios. Because of this, PBK models following the standard are flexible and reusable across diverse dosing and parametrisation scenarios.

## At a glance

To achieve a high level of interoperability and reusability, the central elements of the FAIR PBK standard are the use of the [Systems Biology Markup Language (SBML)](https://sbml.org/) as harmonized, technical exchange format, complemented with specific rules for annotation of units and model elements. For specification of the model units, SBML's built-in framework is used and the RDF-based framework of SBML is employed to annotate model elements. For the latter, however, specific rules are provided on what to annotate and what ontologies to use. That is, all model elements should be annotated (or labelled with) specific terms from the PBPKO ontology, the chemical applicability domain and the chemical identifiers of chemical-specific model elements shoud be annotated using the ChEBI ontology, and the modelled (animal) species should be specified using the NCBI Taxonomy.

To assure findability and accessibility of PBK model implementations, the FAIR PBK follows common standard FAIR practices. Essentially, to assure findability and accessibility, published PBK models should be identifiable with a persistent identifier (DOI), and be available via publicly accessible, recognized repositories (e.g., Zenodo, BioModels). Metadata such as title, authors, and description should be included in the SBML file, and all model and model-element annotations are also considered part of the metadata. The latter enables highly specific searches, e.g., to find models including specific compartments and/or models designed for specific chemicals/animal species.

The table below summarizes the key elements of the FAIR PBK standard for each FAIR principle. For the complete guidelines, see the [full specification](specification.md).

| FAIR principle | Guideline | How to achieve |
| -------------- | --------- | -------------- |
| **Findability** | Each (version of a) PBK model should be identifiable with a persistent identifier and deposited in searchable repositories. | Assign a DOI or persistent identifier, deposit in recognized repositories (e.g., BioModels, Zenodo), and include metadata with title, authors, keywords, and version. |
| **Accessibility** | Models must be retrievable via open protocols and have clear licensing and access conditions. | Make the model downloadable via a web link (e.g., by publishing on Zenodo), provide clear access instructions, include a standard license (e.g., CC-BY, MIT), and ensure metadata (title, authors, keywords, version) remains accessible even if the model file moves or changes. |
| **Interoperability** | Models should be compatible with software and other datasets. | Publish in SBML with defined units, avoid hard-coded dosing, annotate using PBPKO ontology, ChEBI chemical IDs, and NCBI Taxonomy IDs to ensure machine-readable annotations. |
| **Reusability** | Models need clear licenses, provenance, versioning, and documentation of intended use. | Provide an open license, version control, detailed documentation of model purpose, assumptions, parameter sources, simulation protocols, and compliance with community standards; include metadata tracing model derivation. |
