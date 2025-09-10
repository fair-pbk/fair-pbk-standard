import yaml
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

# Load YAML
with open("specification.yaml", "r") as f:
    data = yaml.safe_load(f)

# Group rules by FAIR principle
rules_by_principle = defaultdict(list)
for rule in data["rules"]:
    fair = rule.get("fair_principle", "unknown")
    rules_by_principle[fair].append(rule)

# Load Jinja2 template from file
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("templates/specification.md.j2")

# Render markdown
output_md = template.render(
    rules_by_principle=rules_by_principle
)

# Save for MkDocs
output_file = "docs/specification.md"
with open(output_file, "w") as f:
    f.write(output_md)

print(f"✅ Markdown file generated: {output_file}")
