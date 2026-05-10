from src.math_utilis import add, multiply
from src.file_utilis import save_text

# Use functions from modules
sum_result = add(10, 5)
product_result = multiply(4, 6)


# Display results
print("Sum:", sum_result)
print("Product:", product_result)


# Save results to a file
report = f"""
Sum: {sum_result}
Product: {product_result}

"""

save_text("documents.txt", report)

print("Results saved to documents.txt")