import yfinance as yf

data= yf.download("AAPL", start="2020-01-01", end="2026-3-30")
print(data.head())

def save_text(filename, text):
    with open(filename, 'w') as file:
        file.write(text)



# Save results to a file
report = f"""
result:{data}

"""

save_text("documents.txt", report)

print("Results saved to documents.txt")