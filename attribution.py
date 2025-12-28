from regression_model import run_factor_regression
from factor_data import merge_data

def calculate_factor_attribution(ticker="SPY"):
    print(f"\nRunning factor attribution for {ticker}...")
    
    model = run_factor_regression(ticker)
    df = merge_data(ticker)

    factor_means = df[["MKT", "SMB", "HML"]].mean()
    betas = model.params.drop("const")

    contributions = betas * factor_means

    print("\nFactor Contribution Estimate:")
    print(contributions)
    return contributions

# This ensures the file runs correctly by itself
if __name__ == "__main__":
    calculate_factor_attribution("SPY")

