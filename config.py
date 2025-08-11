azure_conf = {
        "endpoint": "https://<your-resource-name>.openai.azure.com/",
        "api_key": "<YOUR_AZURE_OPENAI_API_KEY>",
        "api_version": "2024-02-01",
        "deployment_name": "<YOUR_DEPLOYMENT_NAME>"
    }

LANREOTIDE_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "lanreotide_product_profile",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Molecule Name": {"type": "string"},
                "Country ID": {"type": "string", "pattern": "^[A-Z]{2,3}$"},
                "Product Scope": {"type": "string"},
                "Route Of Administation": {"type": ["string", "null"]},
                "Product Type": {"type": ["string", "null"]},
                "Drug Product Source": {"type": ["string", "null"]},
                "Therapeutic Area (ATC1)": {"type": ["string", "null"]},
                "Innovator (RLD) Country": {"type": ["string", "null"]},
                "Innovator Company Name": {"type": ["string", "null"]},
                "Innovator Dosage Form": {"type": ["string", "null"]},
                "Innovator Status": {"type": ["string", "null"]},
                "Innovator Route Of Administration": {"type": ["string", "null"]},
                "Innovator Molecule Type": {"type": ["string", "null"]},
                "Product Selection Rationale": {"type": ["string", "null"]},
                "DRL Molecule type": {"type": ["string", "null"]},
                "DRL Dosage Form": {"type": ["string", "null"]},
                "Release Profile": {"type": ["string", "null"]},
                "Innovator Brand Name": {"type": ["string", "null"]},
                "Innovator Strength/Fill Volume": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "DRL Strength/Fill Volume": {
                    "type": ["array", "null"],
                    "items": {"type": "string"}
                },
                "Innovator Salt": {"type": ["string", "null"]},
                "Dosage Regimen": {"type": ["string", "null"]},
                "REMS Categorization": {"type": ["string", "null"]},
                "DRL Brand Name": {"type": ["string", "null"]},
                "Product classification": {"type": ["string", "null"]},
                "Innovator Approval Date": {"type": ["string", "null"]},
                "Innovator Approval Date-Date picker": {
                    "type": ["string", "null"],
                    "format": "date"
                },
                "DRL Salt": {"type": ["string", "null"]},
                "Product Strategy": {"type": ["string", "null"]},
                "Business Strategy": {"type": ["string", "null"]},
                "Product Priority Category": {"type": ["string", "null"]},
                "Vertical": {"type": ["string", "null"]},
                "Product Priority Category-Comments": {"type": ["string", "null"]}
            },
            "required": [
                "Molecule Name", "Country ID", "Product Scope", "Route Of Administation",
                "Product Type", "Drug Product Source", "Therapeutic Area (ATC1)",
                "Innovator (RLD) Country", "Innovator Company Name", "Innovator Dosage Form",
                "Innovator Status", "Innovator Route Of Administration", "Innovator Molecule Type",
                "Product Selection Rationale", "DRL Molecule type", "DRL Dosage Form",
                "Release Profile", "Innovator Brand Name", "Innovator Strength/Fill Volume",
                "DRL Strength/Fill Volume", "Innovator Salt", "Dosage Regimen",
                "REMS Categorization", "DRL Brand Name", "Product classification",
                "Innovator Approval Date", "Innovator Approval Date-Date picker", "DRL Salt",
                "Product Strategy", "Business Strategy", "Product Priority Category",
                "Vertical", "Product Priority Category-Comments"
            ]
        }
    }
}