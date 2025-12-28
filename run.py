import sys
from attribution import calculate_factor_attribution
from charts.factor_charts import plot_factor_betas
from regression_model import run_factor_regression

def main():
    ticker = sys.argv[1] if len(sys.argv) > 1 else "SPY"
    print("\n==============================")
    print(f"FACTOR ANALYSIS FOR: {ticker}")
    print("==============================\n")

    print("Running regression model...")
    model = run_factor_regression(ticker)

    print("\nComputing factor attribution...")
    calculate_factor_attribution(ticker)

    print("\nGenerating beta chart...")
    plot_factor_betas(ticker)

    print("\nAnalysis complete.")
    print(f"Chart saved to: charts/outputs/{ticker}_betas.png")
    print("==============================\n")

if __name__ == "__main__":
    main()

