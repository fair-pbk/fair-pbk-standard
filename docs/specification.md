---
hide:
  - navigation
---

# Specification

## File format

- **F01:** PBK model implementations should be published in *xml* file format using the [Systems Biology Markup Language (SBML)](https://sbml.org/) level 3 version 2 or higher.
- **F02:** The SBML file should be properly annotated using the therefore available [annotation scheme](https://sbml.org/documents/elaborations/miriam_annotation_syntax/).

## General

- **G01:** The PBK model implementation should NOT contain parameters specifying the dosing. These should be added via events in model simulations.

## Model-level annotation requirements

- **M01** The time resolution of the model should be specified via the model-level **timeUnits**.
- **M02** The amounts unit of the model should be specified via the model-level **substanceUnits**.
- **M03** The volume unit of the model should be specified via the model-level **substanceUnits**.
- **M04** The extent unit of the model should be specified via the model-level **extentUnits**.
- **M05** The model should have at least one model-level [BQM_HAS_TAXON](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM annotation, specifying the animal species of the model using a [NCBI Taxonomy](https://registry.identifiers.org/registry/taxonomy) identifier.
- **M06** [TODO: link model to substance chemical applicability domain]

## Compartment-level annotation requirements

- **C01:** All compartments should be assigned a unit representing a volume.
- **C02:** All compartments should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a [compartment](http://purl.obolibrary.org/obo/PBPKO_00446) of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko).
- **C03:** Each compartment should be linked to a different PBPKO [compartment](http://purl.obolibrary.org/obo/PBPKO_00446) class.

## Species-level annotation requirements

- **S01:** All species should be assigned a unit representing an amount.
- **S02:** All species should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a output parameter of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko).
- **S03:** All species should have a [BQB_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a [TODO: link to chemical of a model].

## Parameter-level annotation requirements

- **P01:** All parameters should be assigned a unit.
- **P02:** All parameters should have a [BQM_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a parameter of the [PBPK ontology](https://github.com/InSilicoVida-Research-Lab/pbpko).
- **P03:** Each parameter should be linked to a different PBPKO [parameter](http://purl.obolibrary.org/obo/PBPKO_00002) class.
- **P04:** All parameter linked to a PBPKO [biochemical parameter](http://purl.obolibrary.org/obo/PBPKO_00139) or [physicochemical parameter](http://purl.obolibrary.org/obo/PBPKO_00126) class should have a [BQB_IS](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) MIRIAM element annotation linking them to a [TODO: link to chemical of a model].
- **P05:**  Units should be in compliance with the parameter type annotation.