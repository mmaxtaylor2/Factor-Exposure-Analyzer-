import matplotlib
matplotlib.use("TkAgg")

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from regression_model import run_factor_regression

def plot_factor_betas(ticker="SPY"):
    model = run_factor_regression(ticker)
    betas = model.params.drop("const")
    betas.plot(kind="bar", title=f"{ticker} Factor Betas")
    plt.tight_layout()
    plt.savefig(f"charts/outputs/{ticker}_betas.png")
    plt.show()
    print(f"Saved chart → charts/outputs/{ticker}_betas.png")

if __name__ == "__main__":
    ticker = sys.argv[1] if len(sys.argv) > 1 else "SPY"
    plot_factor_betas(ticker)

