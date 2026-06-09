# Test Cases and Evaluation Results

This document contains the test suites used to evaluate the correctness of the Loan Approval Expert System. It validates the forward chaining inference engine across various applicant risk profiles, fulfilling the requirements for **Part E: Testing and Evaluation**.


## Summary of Test Matrix

| Test Case | Profile Type | Core Indicators | Expected Final Decision |
| :--- | :--- | :--- | :--- |
| **TC-01** | Low-Risk / High-Income | Credit: 750, DTI: 0.20, LTV: 0.50 | **APPROVED** |
| **TC-02** | Standard / Solid Income | Credit: 680, DTI: 0.28, LTV: 0.70 | **APPROVED** |
| **TC-03** | Marginal Credit + High Asset | Credit: 620, DTI: 0.35, Collateral: $600k | **APPROVED WITH CONDITIONS** |
| **TC-04** | Subprime Risk Profile | Credit: 520, DTI: 0.55, No Collateral | **REJECTED** |
| **TC-05** | High Debt Overhead | Credit: 710, DTI: 0.52, LTV: 0.90 | **REJECTED** |

## Detailed Test Case Specifications

### Test Case 1: Premium Tier Approval (Low-Risk / High-Income)
* **Objective:** Verify that an applicant with excellent credit, stable income, low debt, and strong asset coverage automatically receives standard approval.

#### Input Data
* **Age:** `35`
* **Employment Status:** `employed`
* **Years of Employment:** `6`
* **Job Type:** `permanent`
* **Monthly Income:** `85000`
* **Credit Score:** `750`
* **Credit History:** `good`
* **Past Default:** `no`
* **Debt-to-Income Ratio:** `0.20`
* **Is collateral available?:** `yes`
* **Collateral Value:** `550000`
* **Requested Loan Amount:** `220000` *(Calculated LTV: 0.40)*

#### Expected Evaluation Trace
1.  `Excellent Credit Evaluation` fires $\rightarrow$ `credit_rating` = `"excellent"`
2.  `Trustworthy Applicant Assessment` fires $\rightarrow`trustworthy` = `True`
3.  `Stable Income Tenure` & `Stable Job Verification` fire $\rightarrow$ `income_reliable` = `True`
4.  `Low Debt Ratio Check` fires $\rightarrow$ `low_debt` = `True`
5.  `Secured Asset Valuation` fires $\rightarrow$ `secured_loan` = `True`
6.  `Acceptable Loan-To-Value Spread` fires $\rightarrow$ `acceptable_ltv` = `True`
7.  `Strong Applicant Verification` & `Low Total Risk Assessment` fire
8.  **Final Trigger:** `Standard Tier Loan Approval` $\rightarrow$ `loan_status` = `"Approved"`

### Test Case 2: Standard Tier Approval (Solid Income & Good Credit)
* **Objective:** Ensure that qualified applicants who fall into the "Good" credit tier (650–699) rather than "Excellent" are still successfully routed to an approval state if their risk metrics are clean.

#### Input Data
* **Age:** `29`
* **Employment Status:** `employed`
* **Years of Employment:** `4`
* **Job Type:** `permanent`
* **Monthly Income:** `55000`
* **Credit Score:** `680`
* **Credit History:** `good`
* **Past Default:** `no`
* **Debt-to-Income Ratio:** `0.28`
* **Is collateral available?:** `yes`
* **Collateral Value:** `200000`
* **Requested Loan Amount:** `130000` *(Calculated LTV: 0.65)*

#### Expected Evaluation Trace
1.  `Good Credit Evaluation` fires $\rightarrow$ `credit_rating` = `"good"`
2.  `Trustworthy Applicant Assessment` fires $\rightarrow$ `trustworthy` = `True`
3.  `Stable Income Tenure` & `Stable Job Verification` fire $\rightarrow$ `income_reliable` = `True`
4.  `Low Debt Ratio Check` fires $\rightarrow$ `low_debt` = `True`
5.  `Acceptable Loan-To-Value Spread` fires $\rightarrow$ `acceptable_ltv` = `True`
6.  `Standard Safe Profile Validation` & `Low Total Risk Assessment` fire
7.  **Final Trigger:** `Standard Tier Loan Approval` $\rightarrow$ `loan_status` = `"Approved"`

### Test Case 3: Mitigated Conditional Approval (Marginal Profile + High Asset)
* **Objective:** Validate the system's ability to issue an **Approved with Conditions** conclusion when an applicant presents risk (e.g., Fair credit and risky LTV) but counterbalances it with high-value security asset backing.

#### Input Data
* **Age:** `42`
* **Employment Status:** `employed`
* **Years of Employment:** `5`
* **Job Type:** `permanent`
* **Monthly Income:** `62000`
* **Credit Score:** `620`
* **Credit History:** `good`
* **Past Default:** `no`
* **Debt-to-Income Ratio:** `0.35`
* **Is collateral available?:** `yes`
* **Collateral Value:** `650000`
* **Requested Loan Amount:** `585000` *(Calculated LTV: 0.90)*

#### Expected Evaluation Trace
1.  `Fair Credit Evaluation` fires $\rightarrow$ `credit_rating` = `"fair"`
2.  `Medium Debt Ratio Check` fires $\rightarrow$ `medium_debt` = `True`
3.  `Secured Asset Valuation` fires $\rightarrow$ `secured_loan` = `True`
4.  `Risky Loan-To-Value Spread` fires $\rightarrow$ `risky_ltv` = `True`
5.  `High Total Risk Assessment` fires $\rightarrow$ `high_risk` = `True`
6.  **Final Trigger:** `Conditional Mitigated Approval` $\rightarrow$ `loan_status` = `"Approved with Conditions"`

### Test Case 4: Policy Rejection (Subprime Credit / Delinquency Risk)
* **Objective:** Confirm that the engine halts risky credit extensions and issues an automatic **Rejected** status for subprime credit and uncollateralized lending.

#### Input Data
* **Age:** `24`
* **Employment Status:** `employed`
* **Years of Employment:** `1`
* **Job Type:** `contract`
* **Monthly Income:** `30000`
* **Credit Score:** `510`
* **Credit History:** `bad`
* **Past Default:** `yes`
* **Debt-to-Income Ratio:** `0.42`
* **Is collateral available?:** `no`
* **Collateral Value:** `0`
* **Requested Loan Amount:** `80000` *(