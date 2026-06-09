'''
Loan Approval Knowledge base containing  facts and rules definitions
'''

# Define the facts about the loan applicant
facts = {
    "age": 30,
    "employment_status": "employed",
    "employment_years": 4,
    "job_type": "permanent",

    "monthly_income": 80000,
    "annual_income": 960000,
    "savings": 150000,

    "existing_debt": 20000,
    "monthly_debt_payment": 5000,
    "debt_to_income_ratio": 0.25,

    "credit_score": 720,
    "credit_history": "good",
    "past_default": False,

    "loan_amount": 500000,
    "loan_term": 24,
    "loan_type": "business",

    "collateral_available": True,
    "collateral_value": 700000,
    "guarantor_available": False,

    "loan_to_value_ratio": 0.71,
    "down_payment": 200000,

    "application_complete": True  
}

# Define the rules for loan approval
rules = [
    # credit evaluation
    {
        "name": "Excellent Credit",
        "conditions": ["credit_score >= 700"],
        "conclusion": ("credit_rating", "excellent")
    },
    {
        "name": "Good Credit",
        "conditions": ["credit_score >= 650 and credit_score < 700"],
        "conclusion": ("credit_rating", "good")
    },
    {
        "name": "Fair Credit",
        "conditions": ["credit_score >= 600 and credit_score < 650"],
        "conclusion": ("credit_rating", "fair")
    },
    {
        "name": "Poor Credit",
        "conditions": ["credit_score < 600"],
        "conclusion": ("credit_rating", "poor")
    },
    {
        "name": "Trustworthy Applicant",
        "conditions": ["credit_history == 'good'", "past_default == False"],
        "conclusion": ("trusworthy", True)
    },

    #income stability
    {
        "name": "Stable Income",
        "conditions": ["employment_status == 'employed'", "employment_years >= 3"],
        "conclusion": ("stable_income", True)
    },
    {
        "name": "Stable Job",
        "conditions": ["job_type == 'permanent'"],
        "conclusion": ("stable_job", True)
    },
    {
        "name": "Reliable Income",
        "conditions": ["stable_income == True", "stable_job == True"],
        "conclusion": ("income_reliable", True)
    },

    # debt evaluation
    {
        "name": "Low Debt",
        "conditions": ["debt_to_income_ratio < 0.3"],
        "conclusion": ("low_debt", True)
    },
    {
        "name": "Medium Debt",
        "conditions": ["debt_to_income_ratio >= 0.3", "debt_to_income_ratio <= 0.4"],
        "conclusion": ("medium_debt", True)
    },
    {
        "name": "High Debt",
        "conditions": ["debt_to_income_ratio > 0.4"],
        "conclusion": ("high_debt", True)
    },

    # Loan Security
    {
        "name": "Secured Loan",
        "conditions": ["collateral_available == True", "collateral_value >= 500000"],
        "conclusion": ("secured_loan", True)
    },
    {
        "name": "Unsecured Loan",
        "conditions": ["collateral_available == False"],
        "conclusion": ("secured_loan", False)
    },
    {
        "name": "Additional Security",
        "conditions": ["guarantor_available == True"],
        "conclusion": ("additional_security", True)
    },

    # Loan Risk
    {
        "name": "Acceptable LTV",
        "conditions": ["loan_to_value_ratio < 0.8"],
        "conclusion": ("acceptable_ltv", True)
    },
    {
        "name": "Risky LTV",
        "conditions": ["loan_to_value_ratio >= 0.8"],
        "conclusion": ("risky_ltv", True)
    },

    # Applicant Strength
    {
        "name": "Strong Applicant",
        "conditions": ["credit_rating == 'excellent'", "income_reliable == True"],
        "conclusion": ("strong_applicant", True)
    },
    {
        "name": "Low Risk",
        "conditions": ["low_debt == True", "acceptable_ltv == True"],
        "conclusion": ("low_risk", True)
    },
    {
        "name": "High Risk",
        "conditions": ["high_debt == True or risky_ltv == True"],
        "conclusion": ("high_risk", True)
    },

    # Final Approval
    {
        "name": "Loan Approved",
        "conditions": ["strong_applicant == True", "low_risk == True", "application_complete == True"],
        "conclusion": ("loan_status", "Approved")
    },
    {
        "name": "Loan Approved with Conditions",
        "conditions": ["high_risk == True", "secured_loan == True", "application_complete == True"],
        "conclusion": ("loan_status", "Approved with Conditions")
    },
    {
        "name": "Loan Rejected",
        "conditions": ["credit_rating == 'poor' or income_reliable == False", "application_complete == True"],
        "conclusion": ("loan_status", "Rejected")
    }

]