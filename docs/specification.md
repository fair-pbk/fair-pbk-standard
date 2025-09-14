---
hide:
  - navigation
---

# Specification

The FAIR PBK standard sets out rules for publishing PBK model code as digital objects to promote interoperability and reusability. These rules are described below.


## File format

| ID | Rule | Description | Motivation |
|------|------|-------------|------------|
| **F01** | Use SBML L3 v2+ XML | PBK model implementations should be published in *xml* file format using the [Systems Biology Markup Language (SBML)](https://sbml.org/) level 3 version 2 or higher. | Widely supported, machine-readable |
| **F02** | Annotate model and elements with SBML annotation scheme | The model and model elements described by the SBML file should be annotated using the therefore available annotation scheme (see [SBML specification](https://identifiers.org/combine.specifications:sbml.level-3.version-2.core.release-2)). | Enables semantic clarity and interoperability |
| **F03** | Specify units via SBML unit definitions | The units of the model and model elements described by the SBML file should specified using the therefore available system for unit definitions (see [SBML specification](https://identifiers.org/combine.specifications:sbml.level-3.version-2.core.release-2)). | Ensures consistency accross tools and prevents scaling/interpretation errors |


## Model rules

| ID | Rule | Description | Motivation |
|------|------|-------------|------------|
| **G01** | No hardcoded dosing parameters | The PBK model implementation should **NOT** contain parameters specifying the dosing. These should be added via events in model simulations. | Enables modular interoperability, avoids hardcoded study-specific assumptions |
| **M01** | Define time resolution with timeUnits | The time resolution of the model should be specified via the model-level **timeUnits**. | Enables syntactic clarity, ensures correct temporal interpretation |
| **M02** | Define amounts via substanceUnits | The amounts unit of the model should be specified via the model-level **substanceUnits**. | Enables semantic consistency, prevents unit ambiguity |
| **M03** | Define volumes via volumeUnits | The volume unit of the model should be specified via the model-level **volumeUnits**. | Enables semantic consistency, prevents unit ambiguity |
| **M04** | Define extents via extentUnits | The extent unit of the model should be specified via the model-level **extentUnits**. | Enables semantic consistency, prevents unit ambiguity |
| **M05** | Add MIRIAM BQM_HAS_TAXON annotation (species, NCBI Taxonomy) | The model should have at least one model-level [BQM_HAS_TAXON](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM annotation, specifying the animal species of the model using a [NCBI Taxonomy](https://registry.identifiers.org/registry/taxonomy) identifier. | Enables semantic interoperability and cross-species integration |
| **M06** | Add MIRIAM BQB_HAS_PROPERTY annotation (chemicals, ChEBI) | The chemical applicability domain of the model should be specified using the [BQB_HAS_PROPERTY](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM annotation, specifying the model chemical(s) a [ChEBI](https://www.ebi.ac.uk/chebi) identifier. | Ensures consistency, explicitly ties model to (classes of) chemical entities |


## Compartments annotation

| ID | Rule | Description | Motivation |
|------|------|-------------|------------|
| **C01** | Assign volume units to compartments | All compartments should be assigned a unit representing a volume. | Enables syntactic clarity and quantitative scaling |
| **C02** | Annotate with PBPK ontology (BQM_IS) | All compartments should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a [compartment](http://purl.obolibrary.org/obo/PBPKO_00446) of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko). | Enables semantic interoperability by mapping model compartments to shared ontology |
| **C03** | Unique PBPKO class for each compartment | Each compartment should be associated with a different PBPKO [compartment](http://purl.obolibrary.org/obo/PBPKO_00446) class. | Enables ontological clarity, prevents duplicate/misaligned semantics |


## Species annotation

| ID | Rule | Description | Motivation |
|------|------|-------------|------------|
| **S01** | Assign amount units to species | All species should be assigned a unit representing an amount. | Enables numerical clarity, avoids ambiguous concentration vs. amount |
| **S02** | Annotate with PBPK ontology (BQM_IS) | All species should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a [output parameter](http://purl.obolibrary.org/obo/PBPKO_00252) of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko). | Enables semantic clarity by linking to ontology-defined output parameter |
| **S03** | Annotate with ChEBI chemical (BQB_IS) | All species should have a [BQB_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to one of the [ChEBI](https://www.ebi.ac.uk/chebi/) chemical identifiers defined for the model (see **M06**). | Enables semantic interoperability, ensures consistent chemical reference |
| **S04** | Link species to a compartment | All species should be linked to a compartment. | Ensures structural clarity |


## Parameter annotation

| ID | Rule | Description | Motivation |
|------|------|-------------|------------|
| **P01** | Assign units to parameters | All parameters should be assigned a unit. | Enables numerical consistency and prevents scaling errors |
| **P02** | Annotate with PBPK ontology (BQM_IS) | All parameters should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a parameter of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko). | Enables semantic clarity by linking to ontology-defined parameter type |
| **P03** | Unique PBPKO class for each parameter | Each parameter should be associated with a different PBPKO [parameter](http://purl.obolibrary.org/obo/PBPKO_00002) class. | Enables ontological clarity, avoids semantic overlap |
| **P04** | Params in biochem/physicochem class must also have ChEBI (BQB_IS) | All parameter associated with a [biochemical parameter](http://purl.obolibrary.org/obo/PBPKO_00139) or [physicochemical parameter](http://purl.obolibrary.org/obo/PBPKO_00126) class of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko) (see **P02**) should have a [BQB_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to one of the [ChEBI](https://www.ebi.ac.uk/chebi/) chemical identifiers defined for the model (see **M06**). | Enables semantic interoperability by connecting parameter to chemical identity |

