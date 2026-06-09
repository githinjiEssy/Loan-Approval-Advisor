# main.py - Entry point for the Loan Application Expert System
from knowledge_base import KnowledgeBase

# Initialize the knowledge base and load rules
kb = KnowledgeBase()

# Part A: User Input Collection
def get_user_input():
    """ Collects dynamic profile details from the user to populate kb.facts """
    print("\n--- Please enter details for the Loan Application ---")
    
    # Collecting basic demographic and financial information
    kb.add_fact("age", int(input("Age: ")))

    # Conditional input for employment details
    kb.add_fact("employment_status", input("Employment Status (employed/unemployed): ").strip().lower())
    if kb.get_fact("employment_status") == "employed":
        kb.add_fact("employment_years", int(input("Years of Employment: ")))
        kb.add_fact("job_type", input("Job Type (permanent/contract): ").strip().lower())
    else:
        kb.add_fact("employment_years", 0)
        kb.add_fact("job_type", "none")

    # Collecting financial attributes relevant to credit evaluation and risk assessment
    kb.add_fact("monthly_income", float(input("Monthly Income: ")))
    kb.add_fact("credit_score", int(input("Credit Score (300-850): ")))
    kb.add_fact("credit_history", input("Credit History (good/bad): ").strip().lower())
    kb.add_fact("past_default", input("Past Default (yes/no): ").strip().lower() == "yes")
    kb.add_fact("debt_to_income_ratio", float(input("Debt-to-Income Ratio (e.g., 0.25): ")))

    # Collateral details for secured loan evaluation
    kb.add_fact("collateral_available", input("Is collateral available? (yes/no): ").strip().lower() == "yes")
    if kb.get_fact("collateral_available"):
        kb.add_fact("collateral_value", float(input("Collateral Value: ")))
    else:
        kb.add_fact("collateral_value", 0.0)

    # Loan amount requested for LTV calculations
    kb.add_fact("loan_amount", float(input("Requested Loan Amount: ")))
    kb.add_fact("application_complete", True)

# Part B: Inference Engine Implementation
def derive_facts():
    """ Compute basic derived attributes before engine analysis """
    # Derive Loan-to-Value (LTV) ratio for collateral evaluation
    collateral = kb.get_fact("collateral_value")
    loan = kb.get_fact("loan_amount")
    
    if collateral and collateral > 0:
        kb.add_fact("loan_to_value_ratio", loan / collateral)
    else:
        kb.add_fact("loan_to_value_ratio", 9.9) # Unsecured high risk baseline

def prepare_inference_environment():
    """ Pre-populates intermediate variables inside kb.facts to prevent eval NameErrors """

    # intermediate variables for credit evaluation
    intermediate_keys = [
        "credit_rating", "trustworthy", "stable_income", "stable_job", 
        "income_reliable", "low_debt", "medium_debt", "high_debt", 
        "secured_loan", "additional_security", "acceptable_ltv", 
        "risky_ltv", "strong_applicant", "standard_applicant", "low_risk", "high_risk", "loan_status"
    ]

    for key in intermediate_keys:
        if not kb.has_fact(key):
            kb.add_fact(key, False)

# forward chaining implementation to evaluate rules and derive conclusions
def forward_chaining():
    """ Multi-step reasoning engine evaluating conditional string lists """

    # Load the inference environment with intermediate variables to avoid NameErrors during eval
    prepare_inference_environment()
    kb.fired_rules = [] 

    # iteratively evaluate rules until no new inferences can be made
    while True:
        new_inferences = False
        for rule in kb.rules:
            # Safely evaluate conditions using eval; if any variable is missing, treat conditions as not met
            try:
                conditions_met = all(eval(cond, {}, kb.facts) for cond in rule["conditions"])
            except NameError:
                conditions_met = False
            
            # If all conditions for a rule are met, apply the conclusion and track the inference
            if conditions_met:
                conclusion_key, conclusion_value = rule["conclusion"]
                if kb.get_fact(conclusion_key) != conclusion_value:
                    kb.add_fact(conclusion_key, conclusion_value)
                    kb.fired_rules.append(rule)
                    new_inferences = True
                    
        if not new_inferences:
            break

# Part C: Output Generation
def display_results():
    """ Outputs formatted summaries and step-by-step audit explanations (Part C) """
    print("\n" + "="*45)
    print("         LOAN APPLICATION UNDERWRITING        ")
    print("="*45)
    
    # 1. Summary Block
    print(f" Applicant Age          : {kb.get_fact('age')} Years")
    print(f" Credit Rating Assigned : {str(kb.get_fact('credit_rating')).upper()}")
    print(f" Debt-to-Income (DTI)   : {kb.get_fact('debt_to_income_ratio')}")
    print(f" Loan-to-Value (LTV)    : {round(kb.get_fact('loan_to_value_ratio'), 2)}")
    print("-"*45)
    
    decision = kb.get_fact("loan_status")
    # check if a final decision was reached; if not, indicate manual review is needed
    if not decision or decision == False:
        decision = "Manual Underwriting Review Required"
        
    print(f" FINAL DECISION        : {decision.upper()}")
    print("="*45)
    
    # 2. Explanation Facility Block 
    print("\n DETAILED REASONING PATHWAY (EXPLANATION LOG)")
    print("-" * 45)
    # check if any rules were fired during the inference process and display the reasoning pathway
    if not kb.fired_rules:
        print(" [!] No inference rule transitions occurred. Incomplete data mapping profile.")
    else:
        for idx, rule in enumerate(kb.fired_rules, 1):
            key, val = rule["conclusion"]
            print(f" {idx:02d}. Rule Triggered : [{rule['name']}]")
            print(f"     Logic Applied  : {rule['description']}")
            print(f"     Fact Inferred  : Derived '{key}' is now set to -> [{val}]\n")
    print("="*45)

# Main execution flow
def main():
    get_user_input()
    derive_facts()
    forward_chaining()
    display_results()

if __name__ == "__main__":
    main()