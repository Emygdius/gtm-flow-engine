# GTM-Flow Integrity Evaluation Suite
# Purpose: Testing agent logic for data quality standards

def eval_e164_format(phone):
    """
    Eval: Validates if the system correctly identifies E.164 phone formats.
    Required for seamless CRM ingestion.
    """
    return str(phone).startswith('+') and len(str(phone)) > 10

def eval_enrichment_quality(data_record):
    """
    Eval: Ensures AI enrichment hasn't left 'Critical' fields empty.
    Checks for Hallucination or missing data.
    """
    critical_fields = ['industry', 'company_size']
    for field in critical_fields:
        if field not in data_record or data_record[field] == "Unknown":
            return False
    return True

# --- Test Run ---
sample_agent_output = {
    "name": "Wisdom Adams",
    "phone": "+2349157460005",
    "industry": "AI Automation",
    "company_size": "1-10"
}

print(f"Running Evals...")
print(f"E.164 Compliance: {'PASSED' if eval_e164_format(sample_agent_output['phone']) else 'FAILED'}")
print(f"Enrichment Quality: {'PASSED' if eval_enrichment_quality(sample_agent_output) else 'FAILED'}")
