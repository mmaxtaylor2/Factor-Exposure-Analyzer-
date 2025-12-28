## Factor Exposure Analyzer

This project measures asset factor exposures using the Fama–French 3-factor model.
It pulls historical returns, merges factor data, runs regressions, and generates beta charts and attribution estimates for any ticker.

## Project Overview

This tool replicates core workflows used in equity research, portfolio analysis, and factor-risk evaluation.

It performs:

Return & factor data ingestion (Yahoo Finance + Kenneth French dataset)
Excess return calculation vs. risk-free rate
Fama–French 3-factor regression (MKT, SMB, HML)
Factor attribution estimate for recent performance
Automated beta chart output to /charts/outputs

## Features

Feature	Description
Data Pull	Yahoo Finance pricing + Kenneth French factors
Modeling	OLS regression, t-stats, confidence intervals
Attribution	Estimates factor contribution to recent return
Charts	Visual factor exposure chart saved automatically

## File Structure

Factor-Exposure-Analyzer/
│
├── run.py
├── factor_data.py
├── regression_model.py
├── attribution.py
├── requirements.txt
│
├── charts/
│   ├── factor_charts.py
│   ├── outputs/
│       └── [saved beta charts]

## Usage

Run a ticker analysis from Terminal:
python3 run.py SPY
python3 run.py AAPL
python3 run.py TSLA
