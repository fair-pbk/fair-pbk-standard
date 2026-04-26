import yaml
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

def create_specifications_page():
    # Load YAML
    with open("specification/specification.yaml", "r") as f:
        data = yaml.safe_load(f)

    # Group rules by FAIR principle
    rules_by_category = defaultdict(list)
    for rule in data["rules"]:
        fair = rule.get("category", "unknown")
        rules_by_category[fair].append(rule)

    # Load Jinja2 template from file
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("templates/specification.md.j2")

    # Render markdown
    output_md = template.render(
        rules_by_category=rules_by_category
    )

    # Save for MkDocs
    output_file = "docs/specification.md"
    with open(output_file, "w") as f:
        f.write(output_md)

    print(f"✅ Markdown file generated: {output_file}")

def create_fip_page():
    import yaml
    from jinja2 import Environment, FileSystemLoader

    # Load YAML
    with open("specification/fip.yaml", "r") as f:
        data = yaml.safe_load(f)

    # Load Jinja2 template from file
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("templates/fip.md.j2")

    # Render markdown
    output_md = template.render(
        principles=data["principles"]
    )

    # Save for MkDocs
    output_file = "docs/fip.md"
    with open(output_file, "w") as f:
        f.write(output_md)

    print(f"✅ Markdown file generated: {output_file}")

if __name__ == '__main__':
    create_specifications_page()
    create_fip_page()
