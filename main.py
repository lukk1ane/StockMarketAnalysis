import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# Debug information
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())
print("Files in Data folder:", os.listdir('Data'))

data_files = os.listdir('Data')
csv_files = [f for f in data_files if f.endswith('.csv')]
print("\nCSV files found:", csv_files)

if csv_files:
    file_path = os.path.join('Data', csv_files[0])
    print(f"\nReading file: {file_path}")
    df = pd.read_csv(file_path)
else:
    raise FileNotFoundError("No CSV files found in Data directory")

# Data preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print("\nMissing Values:")
print(df.isnull().sum())

# Technical indicators
df['Volume_MA50'] = df['Volume'].rolling(window=50).mean()
df['Daily_Return'] = df['Closing Volume'].pct_change()


def perform_eda():
    print("\nBasic Statistics:")
    print(df.describe())

    correlation_matrix = df.corr()

    # Price trends
    plt.figure(figsize=(15, 7))
    plt.plot(df.index, df['Closing Volume'], label='Closing Price', alpha=0.7)
    plt.plot(df.index, df['50-Day Moving Average'], label='50-day MA', alpha=0.7)
    plt.plot(df.index, df['200-Day Moving Average'], label='200-day MA', alpha=0.7)
    plt.title('Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Volume trends
    plt.figure(figsize=(15, 7))
    plt.bar(df.index, df['Volume'], alpha=0.5, label='Daily Volume')
    plt.plot(df.index, df['Volume_MA50'], color='red', label='50-day Volume MA')
    plt.title('Trading Volume Analysis')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Returns distribution
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Daily_Return'].dropna(), bins=50, kde=True)
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Returns')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

    # Correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()

    # Monthly patterns
    df['Month'] = df.index.month
    plt.figure(figsize=(15, 7))
    sns.boxplot(x='Month', y='Volume', data=df)
    plt.title('Monthly Volume Distribution')
    plt.xlabel('Month')
    plt.ylabel('Volume')
    plt.tight_layout()
    plt.show()


def perform_statistical_analysis():
    # Normality test
    statistic, p_value = stats.normaltest(df['Daily_Return'].dropna())
    print("\nNormality Test for Daily Returns:")
    print(f"Statistic: {statistic:.2f}")
    print(f"P-value: {p_value:.4f}")

    # Risk metrics
    var_95 = np.percentile(df['Daily_Return'].dropna(), 5)
    print(f"\n95% Value at Risk: {var_95:.4f}")

    volatility = df['Daily_Return'].std() * np.sqrt(252)
    print(f"\nAnnualized Volatility: {volatility:.4f}")

    # Moving average crossovers
    df['MA_Crossover'] = np.where(df['50-Day Moving Average'] > df['200-Day Moving Average'], 1, 0)
    crossover_changes = df['MA_Crossover'].diff()
    golden_cross = (crossover_changes == 1).sum()
    death_cross = (crossover_changes == -1).sum()

    print("\nMoving Average Crossover Analysis:")
    print(f"Number of Golden Crosses: {golden_cross}")
    print(f"Number of Death Crosses: {death_cross}")

    # Volume stats
    avg_volume = df['Volume'].mean()
    std_volume = df['Volume'].std()
    volume_coefficient_variation = std_volume / avg_volume

    print("\nVolume Analysis:")
    print(f"Average Daily Volume: {avg_volume:,.0f}")
    print(f"Volume Coefficient of Variation: {volume_coefficient_variation:.4f}")


if __name__ == "__main__":
    try:
        print("Starting Stock Data Analysis...")
        perform_eda()
        perform_statistical_analysis()
        print("\nAnalysis Complete!")
    except FileNotFoundError as e:
        print("\nError: CSV file not found!")
        print(f"Error details: {str(e)}")
        print("\nDebug info:")
        print(f"Working directory: {os.getcwd()}")
        print(f"Data folder contents: {os.listdir('Data')}")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
