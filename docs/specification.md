---
hide:
  - navigation
---

# Specification


## Findability

| Rule | Rule | Description | Motivation |
|------|------|-------------|------------|
| FND01 | Machine-readable metadata | Each PBK model must be accompanied by metadata in a machine-readable format (e.g., JSON-LD or RDF). | Enables automated indexing and discovery across repositories. |
| FND02 | Persistent identifiers | Each PBK model and metadata record must have a globally unique and persistent identifier (e.g., DOI, Handle, identifiers.org URI). | Guarantees stable references for citation and retrieval. |
| FND03 | Rich metadata | Metadata must include authorship, version, creation date, domain keywords, and references to publications or datasets. | Supports precise search and contextual understanding of the model. |
| FND04 | Indexed in searchable repository | Models must be deposited in repositories that are indexed by major repositories/registries (e.g., BioModels, Zenodo). | Ensures models are findable by both humans and machines. |



## Accessibility

| Rule | Rule | Description | Motivation |
|------|------|-------------|------------|
| ACC01 | Open protocols | Models must be retrievable via open, free, and universally implementable protocols (e.g., HTTPS). | Guarantees broad access without proprietary software barriers. |
| ACC02 | Metadata longevity | Metadata should remain accessible even if the model is withdrawn, deprecated, or embargoed. | Preserves discoverability even when data access is restricted. |
| ACC03 | Authentication when required | If access restrictions exist, authentication and authorization procedures must be documented and use open standards (e.g., OAuth2). | Balances openness with ethical/legal requirements. |
| ACC04 | License clarity | Access conditions and usage rights must be explicitly stated in the metadata and repository entry. | Users understand upfront what they can or cannot do with the model. |



## Interoperability

| Rule | Rule | Description | Motivation |
|------|------|-------------|------------|
| F01 | Use SBML L3 v2+ XML | PBK model implementations should be published in *xml* file format using the [Systems Biology Markup Language (SBML)](https://sbml.org/) level 3 version 2 or higher. | Widely supported, machine-readable |
| F02 | Annotate model and elements with SBML annotation scheme | The model and model elements described by the SBML file should be annotated using the therefore available annotation scheme (see, [specification](https://identifiers.org/combine.specifications:sbml.level-3.version-2.core.release-2)). | Enables semantic clarity and interoperability |
| F03 | Specify units via SBML unit definitions | The units of the model and model elements described by the SBML file should specified using the therefore available system for unit definitions (see, [specification](https://identifiers.org/combine.specifications:sbml.level-3.version-2.core.release-2)). | Ensures consistency accross tools and prevents scaling/interpretation errors |
| G01 | No hardcoded dosing parameters | The PBK model implementation should **NOT** contain parameters specifying the dosing. These should be added via events in model simulations. | Enables modular interoperability, avoids hardcoded study-specific assumptions |
| M01 | Define time resolution with timeUnits | The time resolution of the model should be specified via the model-level **timeUnits**. | Enables syntactic clarity, ensures correct temporal interpretation |
| M02 | Define amounts via substanceUnits | The amounts unit of the model should be specified via the model-level **substanceUnits**. | Enables semantic consistency, prevents unit ambiguity |
| M03 | Define volumes via volumeUnits | The volume unit of the model should be specified via the model-level **volumeUnits**. | Enables semantic consistency, prevents unit ambiguity |
| M04 | Define extents via extentUnits | The extent unit of the model should be specified via the model-level **extentUnits**. | Enables semantic consistency, prevents unit ambiguity |
| M05 | Add MIRIAM BQM_HAS_TAXON annotation (species, NCBI Taxonomy) | The model should have at least one model-level [BQM_HAS_TAXON](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM annotation, specifying the animal species of the model using a [NCBI Taxonomy](https://registry.identifiers.org/registry/taxonomy) identifier. | Enables semantic interoperability and cross-species integration |
| M06 | Add MIRIAM BQB_HAS_PROPERTY annotation (chemicals, ChEBI) | The chemical applicability domain of the model should be specified using the [BQB_HAS_PROPERTY](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM annotation, specifying the model chemical(s) a [ChEBI](https://www.ebi.ac.uk/chebi) identifier. | Ensures consistency, explicitly ties model to (classes of) chemical entities |
| C01 | Assign volume units to compartments | All compartments should be assigned a unit representing a volume. | Enables syntactic clarity and quantitative scaling |
| C02 | Annotate with PBPK ontology (BQM_IS) | All compartments should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a [compartment](http://purl.obolibrary.org/obo/PBPKO_00446) of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko). | Enables semantic interoperability by mapping model compartments to shared ontology |
| C03 | Unique PBPKO class for each compartment | Each compartment should be associated with a different PBPKO [compartment](http://purl.obolibrary.org/obo/PBPKO_00446) class. | Enables ontological clarity, prevents duplicate/misaligned semantics |
| S01 | Assign amount units to species | All species should be assigned a unit representing an amount. | Enables numerical clarity, avoids ambiguous concentration vs. amount |
| S02 | Annotate with PBPK ontology (BQM_IS) | All species should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a [output parameter](http://purl.obolibrary.org/obo/PBPKO_00252) of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko). | Enables semantic clarity by linking to ontology-defined output parameter |
| S03 | Annotate with ChEBI chemical (BQB_IS) | All species should have a [BQB_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to one of the [ChEBI](https://www.ebi.ac.uk/chebi/) chemical identifiers defined for the model (see **M06**). | Enables semantic interoperability, ensures consistent chemical reference |
| S04 | Link species to a compartment | All species should be linked to a compartment. | Ensures structural clarity |
| P01 | Assign units to parameters | All parameters should be assigned a unit. | Enables numerical consistency and prevents scaling errors |
| P02 | Annotate with PBPK ontology (BQM_IS) | All parameters should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a parameter of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko). | Enables semantic clarity by linking to ontology-defined parameter type |
| P03 | Unique PBPKO class for each parameter | Each parameter should be associated with a different PBPKO [parameter](http://purl.obolibrary.org/obo/PBPKO_00002) class. | Enables ontological clarity, avoids semantic overlap |
| P04 | Params in biochem/physicochem class must also have ChEBI (BQB_IS) | All parameter associated with a [biochemical parameter](http://purl.obolibrary.org/obo/PBPKO_00139) or [physicochemical parameter](http://purl.obolibrary.org/obo/PBPKO_00126) class of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko) (see **P02**) should have a [BQB_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to one of the [ChEBI](https://www.ebi.ac.uk/chebi/) chemical identifiers defined for the model (see **M06**). | Enables semantic interoperability by connecting parameter to chemical identity |



## Reusability

| Rule | Rule | Description | Motivation |
|------|------|-------------|------------|
| REU01 | Clear usage license | Models must be distributed under a clear, accessible, and preferably open license (e.g., CC-BY, CC0, MIT). | Ensures legal clarity for reuse and derivative works. |
| REU02 | Provenance documentation | Metadata must describe the origin of the model, including data sources, assumptions, and modeling methods. | Allows others to trust, validate, and build upon the model. |
| REU03 | Domain standards compliance | By complying to the FAIR PBK standard, models adhere to community standards. | Promotes interoperability and long-term usability. |
| REU04 | Versioning | Each model release must have a version identifier, with changelogs describing differences from prior versions. Each version should have its own unique identifier (see FND02). | Supports reproducibility and long-term research integrity. |
| REU05 | Documentation of intended use | Model metadata must include statements of scope, limitations, and intended application domains. | Helps users assess whether the model fits their research needs. |



