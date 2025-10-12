import os
import libsbml as ls
from jinja2 import Environment, FileSystemLoader
from sbmlpbkutils import PbkModelInfosExtractor

sbml_file = os.path.join('scripts/euromix.sbml')
document = ls.readSBML(sbml_file)
infos_extractor = PbkModelInfosExtractor(document)

# Load Jinja2 template from file
env = Environment(loader=FileSystemLoader("."))

# Model infos table
model_info = infos_extractor.get_model_info()
model_records = []
template = env.get_template("templates/model_infos_table.md.j2")
chebi_terms = [f"[{term.name.replace("_", ":")}]({term.iri}) ({term.label[0]})" for term in model_info.chebi_bqb_has_property_terms]
ncbitaxon_terms = [f"[{term.name.replace("_", ":")}]({term.iri}) ({term.label[0]})" for term in model_info.ncbi_bqb_has_taxon_terms]
output_md = template.render(
    model_info=model_info,
    chebi_terms=chebi_terms,
    ncbitaxon_terms=ncbitaxon_terms
)
output_file = "include/model_infos_table.md"
with open(output_file, mode="w", encoding="utf-8") as f:
    f.write(output_md)

print(f"✅ Model infos table generated: {output_file}")

# Compartment infos table
compartment_infos = infos_extractor.get_compartment_infos()
compartment_records = []
for c in compartment_infos:
    compartment_records.append({
        "id": c.id,
        "name": c.name,
        "unit": c.unit,
        "bqm_is_id": c.pbpko_bqm_is_class.name.replace("_", ":") if c.pbpko_bqm_is_class else "",
        "bqm_is_label": c.pbpko_bqm_is_class.label[0] if c.pbpko_bqm_is_class else "",
        "bqm_is_iri": c.pbpko_bqm_is_class.iri if c.pbpko_bqm_is_class else ""
    })
template = env.get_template("templates/compartment_infos_table.md.j2")
output_md = template.render(
    records=compartment_records
)
output_file = "include/compartment_infos_table.md"
with open(output_file, mode="w", encoding="utf-8") as f:
    f.write(output_md)

print(f"✅ Compartments table generated: {output_file}")

# Species infos table
species_infos = infos_extractor.get_species_infos()
species_records = []
for c in species_infos:
    species_records.append({
        "id": c.id,
        "name": c.name,
        "unit": c.unit,
        "bqm_is_id": c.pbpko_bqm_is_class.name.replace("_", ":") if c.pbpko_bqm_is_class else "",
        "bqm_is_label": c.pbpko_bqm_is_class.label[0] if c.pbpko_bqm_is_class else "",
        "bqm_is_iri": c.pbpko_bqm_is_class.iri if c.pbpko_bqm_is_class else "",
        "bqb_is_id": c.chebi_bqb_is_class.name.replace("_", ":") if c.chebi_bqb_is_class else "",
        "bqb_is_label": c.chebi_bqb_is_class.label[0] if c.chebi_bqb_is_class else "",
        "bqb_is_iri": c.chebi_bqb_is_class.iri if c.chebi_bqb_is_class else ""
    })
template = env.get_template("templates/species_infos_table.md.j2")
output_md = template.render(
    records=species_records
)
output_file = "include/species_infos_table.md"
with open(output_file, mode="w", encoding="utf-8") as f:
    f.write(output_md)

print(f"✅ Species table generated: {output_file}")

# Parameter infos table
parameter_infos = infos_extractor.get_parameter_infos()
parameter_records = []
for c in parameter_infos:
    parameter_records.append({
        "id": c.id,
        "name": c.name,
        "unit": c.unit,
        "bqm_is_id": c.pbpko_bqm_is_class.name.replace("_", ":") if c.pbpko_bqm_is_class else "",
        "bqm_is_label": c.pbpko_bqm_is_class.label[0] if c.pbpko_bqm_is_class else "",
        "bqm_is_iri": c.pbpko_bqm_is_class.iri if c.pbpko_bqm_is_class else "",
        "bqb_is_id": c.chebi_bqb_is_class.name.replace("_", ":") if c.chebi_bqb_is_class else "",
        "bqb_is_label": c.chebi_bqb_is_class.label[0] if c.chebi_bqb_is_class else "",
        "bqb_is_iri": c.chebi_bqb_is_class.iri if c.chebi_bqb_is_class else ""
    })
template = env.get_template("templates/parameter_infos_table.md.j2")
output_md = template.render(
    records=parameter_records
)
output_file = "include/parameter_infos_table.md"
with open(output_file, mode="w", encoding="utf-8") as f:
    f.write(output_md)

print(f"✅ Parameters table generated: {output_file}")
