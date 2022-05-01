# Telecom-Churn-Analysis-EDA-project

The capstone project is based on Exploratory data analysis on a Telecom churn
analysis dataset. The problem statement for the project is;

“Are Customers with higher charges more prone to churn?”

The dataset had 20 variables in the beginning. A few variables were created that
were subservient for the analysis. The dataset has 3333 records with no null
observations.

The following steps are involved in the project:

1. A brief introduction to the variables that have the information on the
charges (4 different charges) being levied on the customers. Largely, the
variables could be surmised in the 5 number summary proposed by Tukey
that include mean, median, 1st, 3rd quartile, and mode. KDE plots are used
for portraying a comparative analysis between the customers that are
churning and the ones that are not.

2. Added the corresponding records of the 4 variables into 1 variable. Used
the same techniques to depict the result as are discussed in the earlier
point. Concluded that for the given sample apparently, the customers that
are being charged more than 70 units are more likely to churn than not.

3. The statistical significance of the apparent effects are demonstrated using
3 methods;

  a. Effect size - Using Cohen’s d; An effect size of 0.67 suggested a
medium effect.

  b. Hypothesis testing - Using Permutation test; A p-value of 14%
suggested that the null hypothesis “The customers that are charged
more, churn less” could not be rejected. Perhaps we need more data
to establish the claim.

  c. Relative risk - Suggested that the customers that are being charged
more than 70 units are about less likely to stay (not churn).

4. The effect of other variables on the ‘Total charge’ variable is studied. Only the
striking conclusions are noted.

5. Finally, 3 suggestions are given based on the analysis.
