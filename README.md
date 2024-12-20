# Stock Market Analysis Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data Description](#data-description)
3. [Installation & Setup](#installation--setup)
4. [Technical Analysis](#technical-analysis)
5. [Visualizations](#visualizations)
6. [Statistical Analysis Results](#statistical-analysis-results)
7. [Trading Implications](#trading-implications)
8. [Future Development](#future-development)

## Project Overview
This project implements a comprehensive stock market analysis tool using Python. It combines technical analysis, statistical methods, and data visualization to provide insights into stock price movements, volume patterns, and market trends. The analysis focuses on identifying trading opportunities while assessing market risks through various metrics and indicators.

## Data Description
The analysis utilizes historical stock market data with the following components:
- **Date**: Trading day timestamps
- **Closing Volume**: Daily closing prices
- **Volume**: Daily trading volume
- **50-Day Moving Average**: Average closing price over 50 trading days
- **200-Day Moving Average**: Average closing price over 200 trading days

### Data Preprocessing Steps:
1. Date conversion to datetime format
2. Index setting to date
3. Missing value handling
4. Additional metric calculations:
   - Daily returns
   - Volume moving averages
   - Technical indicators

## Installation & Setup
```bash
# Clone the repository
git clone https://github.com/lukk1ane/StockMarketAnalysis.git
cd StockMarketAnalysis

# Install required packages
pip install pandas numpy matplotlib seaborn scipy
```

## Technical Analysis
### Moving Average Analysis
- Implementation of 50-day and 200-day moving averages
- Golden Cross and Death Cross signal detection
- Trend strength measurement
- Support/resistance level identification

### Volume Analysis Implementation
- 50-day volume moving average calculation
- Volume trend pattern recognition
- Price-volume relationship analysis
- Liquidity assessment metrics

### Returns Analysis Methods
- Daily return calculations
- Distribution analysis
- Volatility measurements
- Risk metric computations

## Visualizations

### 1. Price and Moving Averages Chart
```python
plt.figure(figsize=(15, 7))
plt.plot(df.index, df['Closing Volume'], label='Closing Price', alpha=0.7)
plt.plot(df.index, df['50-Day Moving Average'], label='50-day MA', alpha=0.7)
plt.plot(df.index, df['200-Day Moving Average'], label='200-day MA', alpha=0.7)
```
**Purpose:** Visualization of price trends and moving average interactions

### 2. Volume Analysis Chart
```python
plt.figure(figsize=(15, 7))
plt.bar(df.index, df['Volume'], alpha=0.5)
plt.plot(df.index, df['Volume_MA50'], color='red')
```
**Purpose:** Analysis of trading activity and volume patterns

### 3. Returns Distribution
```python
sns.histplot(df['Daily_Return'].dropna(), bins=50, kde=True)
```
**Purpose:** Visualization of return distribution and volatility patterns

### 4. Correlation Matrix
```python
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
```
**Purpose:** Analysis of relationships between different metrics

### 5. Monthly Volume Patterns
```python
sns.boxplot(x='Month', y='Volume', data=df)
```
**Purpose:** Identification of seasonal trading patterns

## Statistical Analysis Results

### Basic Statistics Summary
```
Statistical Measures for Closing Volume:
- Count: 2500.000000
- Mean: 49.980192
- Std: 29.214364
- Min: 0.055142
- 25%: 24.353805
- 50%: 49.935725
- 75%: 75.810897
- Max: 99.991633
```

### Normality Test Results
```
Daily Returns Analysis:
- Statistic: 5980.39
- P-value: 0.0000
```
**Interpretation:** Strong evidence of non-normal distribution in returns

### Risk Metrics
- **95% Value at Risk:** -0.9035
- **Annualized Volatility:** 380.2750%

### Moving Average Crossover Statistics
- **Golden Crosses:** 111 occurrences
- **Death Crosses:** 112 occurrences

### Volume Analysis Metrics
- **Average Daily Volume:** 492,857 shares
- **Volume Coefficient of Variation:** 0.5886

## Trading Implications

### Risk Management Strategies
1. Position Sizing:
   - Use VaR-based position limits
   - Implement volatility-adjusted sizing

2. Market Condition Adaptation:
   - Range-bound market indicators
   - Trend-following opportunities
   - Volume-based confirmation signals

### Trading Strategy Development
1. Mean Reversion Opportunities:
   - Equal number of bullish/bearish signals
   - Cyclical pattern exploitation

2. Volume-Based Signals:
   - Moderate volume volatility
   - Consistent trading activity
   - Liquidity assessment

3. Risk-Adjusted Approaches:
   - Non-normal distribution consideration
   - Volatility-based adjustments
   - Statistical arbitrage potential

## Future Development

### Technical Enhancements
1. Additional Indicators:
   - RSI (Relative Strength Index)
   - MACD (Moving Average Convergence Divergence)
   - Bollinger Bands

2. Advanced Analytics:
   - Machine Learning integration
   - Pattern recognition algorithms
   - Automated signal generation

3. System Improvements:
   - Real-time data processing
   - Backtesting capabilities
   - Performance optimization

### Analytical Expansions
1. Additional Data Sources:
   - Fundamental data integration
   - Market sentiment analysis
   - Economic indicators

2. Enhanced Risk Metrics:
   - Conditional VaR
   - Drawdown analysis
   - Risk-adjusted returns

3. Trading Strategies:
   - Multi-timeframe analysis
   - Portfolio optimization
   - Automated execution signals

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.
