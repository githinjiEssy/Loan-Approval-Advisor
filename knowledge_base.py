'''
Loan Approval Knowledge base containing facts and rules definitions
'''

class KnowledgeBase:
    def __init__(self):
        self.facts = {}
        self.rules = []
        self.fired_rules = []

        self.load_rules()

    # FACT MANAGEMENT
    def add_fact(self, key, value):
        """ Add a fact to the knowledge base """
        self.facts[key] = value
    def get_fact(self, key):
        """ Retrieve a fact from the knowledge base """
        return self.facts.get(key, None)
    def has_fact(self, key):
        """ Check if a fact exists in the knowledge base """
        return key in self.facts
    
    # RULES DEFINITION
    def load_rules(self):

        # Credit Evaluation Rules
        self.rules.append({
            "name": "Excellent Credit Evaluation",
            "conditions": ["credit_score >= 700"],
            "conclusion": ("credit_rating", "excellent"),
            "description": "Applicant's credit score is 700 or above, qualifying for premium status."
        })
        self.rules.append({
            "name": "Good Credit Evaluation",
            "conditions": ["credit_score >= 650 and credit_score < 700"],
            "conclusion": ("credit_rating", "good"),
            "description": "Applicant's credit score is in the solid 650-699 range."
        })
        self.rules.append({
            "name": "Fair Credit Evaluation",
            "conditions": ["credit_score >= 600 and credit_score < 650"],
            "conclusion": ("credit_rating", "fair"),
            "description": "Applicant's credit score is marginal (600-649), requiring additional scrutiny."
        })
        self.rules.append({
            "name": "Poor Credit Evaluation",
            "conditions": ["credit_score < 600"],
            "conclusion": ("credit_rating", "poor"),
            "description": "Applicant's credit score is below 600, indicating high historical default risk."
        })
        self.rules.append({
            "name": "Trustworthy Applicant Assessment",
            "conditions": ["credit_history == 'good'", "past_default == False"],
            "conclusion": ("trustworthy", True),
            "description": "Clean historical repayment profile with zero records of past defaults."
        })

        # Income Stability Rules
        self.rules.append({
            "name": "Stable Income Tenure",
            "conditions": ["employment_status == 'employed'", "employment_years >= 3"],
            "conclusion": ("stable_income", True),
            "description": "Applicant has maintained steady employment for 3 or more years."
        })
        self.rules.append({
            "name": "Stable Job Verification",
            "conditions": ["job_type == 'permanent'"],
            "conclusion": ("stable_job", True),
            "description": "Employment contract type is permanent, offering high long-term security."
        })
        self.rules.append({
            "name": "Reliable Income Conclusion",
            "conditions": ["stable_income == True", "stable_job == True"],
            "conclusion": ("income_reliable", True),
            "description": "Combined structural indicators verify a reliable incoming cash flow."
        })

        # Debt Evaluation Rules
        self.rules.append({
            "name": "Low Debt Ratio Check",
            "conditions": ["debt_to_income_ratio < 0.3"],
            "conclusion": ("low_debt", True),
            "description": "Debt-to-Income ratio is under 30%, showing low existing debt overhead."
        })
        self.rules.append({
            "name": "Medium Debt Ratio Check",
            "conditions": ["debt_to_income_ratio >= 0.3", "debt_to_income_ratio <= 0.4"],
            "conclusion": ("medium_debt", True),
            "description": "Debt-to-Income ratio is moderate (30%-40%), within standard limits."
        })
        self.rules.append({
            "name": "High Debt Burden Warning",
            "conditions": ["debt_to_income_ratio > 0.4"],
            "conclusion": ("high_debt", True),
            "description": "Debt-to-Income ratio exceeds 40%, signaling heavy financial leverage."
        })

        # Loan Security Rules
        self.rules.append({
            "name": "Secured Asset Valuation",
            "conditions": ["collateral_available == True", "collateral_value >= 500000"],
            "conclusion": ("secured_loan", True),
            "description": "High-value physical collateral backing exists to safely absorb asset recovery actions."
        })
        self.rules.append({
            "name": "Unsecured Loan Status",
            "conditions": ["collateral_available == False or collateral_value < 500000"],
            "conclusion": ("secured_loan", False),
            "description": "Insufficient or missing collateral backing means this loan is unsecured."
        })

        # Loan Risk Rules
        self.rules.append({
            "name": "Acceptable Loan-To-Value Spread",
            "conditions": ["loan_to_value_ratio < 0.8"],
            "conclusion": ("acceptable_ltv", True),
            "description": "Requested loan amount covers less than 80% of asset value, protecting equity."
        })
        self.rules.append({
            "name": "Risky Loan-To-Value Spread",
            "conditions": ["loan_to_value_ratio >= 0.8"],
            "conclusion": ("risky_ltv", True),
            "description": "Loan-to-Value ratio is 80% or greater, exposing the lender to equity shortfalls."
        })
        
        # Applicant Strength Rules
        self.rules.append({
            "name": "Strong Applicant Verification",
            "conditions": ["credit_rating == 'excellent'", "income_reliable == True"],
            "conclusion": ("strong_applicant", True),
            "description": "Premium tier credit standing joined with rock-solid income metrics."
        })
        self.rules.append({
            "name": "Standard Safe Profile Validation",
            "conditions": ["credit_rating == 'good'", "income_reliable == True"],
            "conclusion": ("standard_applicant", True),
            "description": "Solid credit history paired with confirmed steady employment."
        })
        self.rules.append({
            "name": "Low Total Risk Assessment",
            "conditions": ["low_debt == True", "acceptable_ltv == True"],
            "conclusion": ("low_risk", True),
            "description": "Financial obligations are minor and safely offset by solid asset margins."
        })
        self.rules.append({
            "name": "High Total Risk Assessment",
            "conditions": ["high_debt == True or risky_ltv == True"],
            "conclusion": ("high_risk", True),
            "description": "Excessive structural risk due to heavy debt leverage or poor security coverage ratios."
        })

        # Final Approval Rules (3 Clear Final Decisions) [cite: 32]
        self.rules.append({
            "name": "Standard Tier Loan Approval",
            "conditions": ["(strong_applicant == True or standard_applicant == True)", "low_risk == True", "application_complete == True"],
            "conclusion": ("loan_status", "Approved"),
            "description": "Applicant meets core parameters for standard automated credit expansion."
        })
        self.rules.append({
            "name": "Conditional Mitigated Approval",
            "conditions": ["high_risk == True", "secured_loan == True", "application_complete == True"],
            "conclusion": ("loan_status", "Approved with Conditions"),
            "description": "High structural profile risks are balanced by high-value capital collateral."
        })
        self.rules.append({
            "name": "Automated Policy Rejection",
            "conditions": ["(credit_rating == 'poor' or high_debt == True)", "application_complete == True"],
            "conclusion": ("loan_status", "Rejected"),
            "description": "Risk profile violates standard security boundaries due to poor credit history or high debt ratios."
        })