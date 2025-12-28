# regression_model.py

from factor_data import merge_data
import statsmodels.api as sm

def run_factor_regression(ticker="SPY"):
    print(f"Running regression for {ticker}...")
    
    df = merge_data(ticker)

    # X = Independent variables (factors)
    X = df[["MKT", "SMB", "HML"]]
    X = sm.add_constant(X)

    # y = Dependent variable (excess return)
    y = df["Excess_Return"]

    model = sm.OLS(y, X).fit()
    print(model.summary())  # shows regression results
    return model

# Allow standalone run
if __name__ == "__main__":
    run_factor_regression("SPY")

