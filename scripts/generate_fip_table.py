import yaml
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

# Load YAML
with open("fair_implementation_profile.yaml", "r") as f:
    data = yaml.safe_load(f)

# Load Jinja2 template from file
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("templates/fip_table.md.j2")

# Render markdown
output_md = template.render(
    principles=data["principles"]
)

# Save for MkDocs
output_file = "include/fip_table.md"
with open(output_file, "w") as f:
    f.write(output_md)

print(f"✅ Markdown file generated: {output_file}")
