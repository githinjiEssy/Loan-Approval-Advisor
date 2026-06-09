# Loan Approval Advisor (Expert System)

An automated Rule-Based Expert System (KBS) designed to evaluate loan applicants by analyzing their personal financial metrics and credit backgrounds. The system processes user data dynamically using a Multi-Step Forward Chaining inference engine to determine creditworthiness and issue explicit underwriting risk assessments.


## 1. Problem Being Solved
Manual credit underwriting is often slow, inconsistent, and prone to human oversight. Financial institutions require a reliable method to parse diverse variables (such as income consistency, existing liabilities, collateral margins, and payment records) to produce immediate, predictable decisions. 

This system resolves this challenge by acting as an automated credit committee. It captures baseline applicant data, processes complex financial ratios, runs multi-tier rule checks, and generates an unambiguous final decision coupled with a transparent audit trail explaining *why* the decision was made.


## 2. System Architecture & Directory Structure
The repository is structured dynamically to separate the Knowledge Base, Inference Logic, and Evaluation Framework, matching the required directory tree layout:

```text
kbs-assignment/
│
├── diagrams/
│   └── semantic_network.png    # Visual graph of fact-rule relationships (Part D)
│
├── screenshots/
│   └── execution_run.png       # Captured terminal testing evidence
│
├── knowledge_base.py           # Contains production rules and helper methods
├── main.py                     # Entry point containing the Forward Chaining Engine
├── test_cases.md               # Collection of 5 detailed testing scenarios
└── README.md                   # System operational documentation
```

## 3. Knowledge Representation (Facts & Rules)

### Part A: Fact Directory (16 Structural Attributes Tracked)
The Knowledge-Based System maintains an internal environment dictionary tracking exactly 16 facts over the execution life cycle, satisfying the requirement for at least 15 base metrics:

* **Dynamic Input Facts (Collected from User):**
    1.  `age`: Age of the primary applicant (Integer).
    2.  `employment_status`: Categorical labor status (`employed` / `unemployed`).
    3.  `employment_years`: Tenure length with current employer (Years).
    4.  `job_type`: Contract security specification (`permanent` / `contract`).
    5.  `monthly_income`: Gross incoming monthly cash yield.
    6.  `credit_score`: Numerical industry credit bureau metric (300-850).
    7.  `credit_history`: General historic payment background evaluation (`good` / `bad`).
    8.  `past_default`: Delinquency indicator tracking previous defaults (Boolean).
    9.  `debt_to_income_ratio`: Current monthly financial leverage index (0.0 - 1.0).
    10. `collateral_available`: Verification flag indicating asset pledging state (Boolean).
    11. `collateral_value`: Market valuation of the physical security asset.
    12. `loan_amount`: Total capital request sum by the borrowing entity.
* **System Engine Control & Derived Facts:**
    13. `application_complete`: Execution verification lock validating process input closure.
    14. `loan_to_value_ratio`: Mathematically computed leverage exposure variable (`loan_amount / collateral_value`).
* **Intermediate and Final Structural Inference Facts:**
    15. `credit_rating`: Synthesized evaluation ranking profile (`excellent`, `good`, `fair`, `poor`).
    16. `loan_status`: The finalized state conclusion marker (`Approved`, `Approved with Conditions`, `Rejected`).

### Part B: Inference Rules Defined (16 Production Rules)

The system maps domain rules as evaluation blocks containing a text name, structural boundary conditions, and target conclusions.
* The rule base consists of precisely 16 production rules:
    1. Excellent Credit Evaluation: Evaluates if `credit_score >= 700`.
    2. Good Credit Evaluation: Evaluates if `credit_score >= 650` and `< 700`.
    3. Fair Credit Evaluation: Evaluates if `credit_score >= 600` and `< 650`.
    4. Poor Credit Evaluation: Evaluates if `credit_score < 600`.
    5. Trustworthy Applicant Assessment: Evaluates clean historical repayment boundaries (`credit_history == 'good'` and `past_default == False`).
    6. Stable Income Tenure: Checks for long-term employment security (`employment_status == 'employed'` and `employment_years >= 3`).
    7. Stable Job Verification: Verifies corporate job structural permanence (`job_type == 'permanent'`).
    8. Reliable Income Conclusion: Aggregates stability markers (`stable_income == True` and `stable_job == True`).
    9. Low Debt Ratio Check: Assesses if debt obligations remain highly manageable (`debt_to_income_ratio < 0.3`).
    10. Medium Debt Ratio Check: Isolates mild leveraging profiles (`debt_to_income_ratio >= 0.3` and `<= 0.4`).
    11. High Debt Burden Warning: Flags critical over-leveraging indicators (`debt_to_income_ratio > 0.4`).
    12. Secured Asset Valuation: Validates premium liquid equity backing parameters (`collateral_available == True` and `collateral_value >= 500000`).
    13. Unsecured Loan Status: Isolates high asset default risk parameters (`collateral_available == False` or `collateral_value < 500000`).
    14. Acceptable Loan-To-Value Spread: Checks if request represents a healthy risk buffer under equity guidelines (`loan_to_value_ratio < 0.8`).
    15. Risky Loan-To-Value Spread: Warns if request exposes lender equity to shortfalls (`loan_to_value_ratio >= 0.8`).
    16. Applicant Strength & Risk Matrix Synthesizers: Rules that aggregate multiple dependencies into unified flags such as `strong_applicant`, `standard_applicant`, `low_risk`, and `high_risk`.

### Part C: Target Recommendations (3 Possible Conclusions)
The system routes reasoning chains to satisfy the core structural assignment constraint of outputting at least 3 possible outcomes:
- **APPROVED**: Granted automatically to low-risk applicants displaying premium or steady income credentials and safe leveraging ratios.
- **APPROVED WITH CONDITIONS**: Granted to elevated risk profiles whose metrics trigger warnings, but whose risks are fully mitigated by high-value capital collateral asset backing.
- **REJECTED**: Denied by automated policy enforcement due to subprime credit scores, explicit past repayment defaults, or crippling debt burden thresholds.

## 4. Explanation Facility
Whenever a rule's conditions validate successfully during a forward chaining iteration, the engine records that rule into an execution container (`kb.fired_rules`).

Upon completion, the system outputs an audit trace tracking every single micro-inference applied, the underlying banking logic executed, and the resulting fact added to the profile database.

## 5. How to run 
Running the System
1. Clone this repository onto your machine or locate your work folder.
2. Move to the project directory
3. Run the application script using the Python compiler command:
 ```
    python main.py

 ```
