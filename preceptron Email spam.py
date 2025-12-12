import numpy as np

# suspicious words
SUSPICIOUS_WORDS = ["win", "free", "click", "prize", "money", "offer"]


# analyze the email text
def analyze_email(email_text):
    # Count suspicious words in email
    suspicious_count = sum([email_text.lower().count(word) for word in SUSPICIOUS_WORDS])

    # Counts "http" occurrences as link indicators
    link_count = email_text.count("http")

    return np.array([suspicious_count, link_count])


# Define weights for suspicious words and links
def weights():
    w1 = 1.0  # Importance of suspicious words
    w2 = 0.5  # Importance of links
    return np.array([w1, w2])


# Define bias
def bias():
    return -2


# Adjust threshold for spam detection

# Summation function including bias
def summation(x, w, B):
    return np.dot(x, w) + B  # Σ + B


# Activation function (step function)
def activation(s):
    return 1 if s >= 0 else 0


# Perceptron function to classify email as spam or not spam
def perceptron(email_text):
    x = analyze_email(email_text)
    # Analyze email content
    w = weights()
    # Get weights for features
    B = bias()
    # Define bias
    s = summation(x, w, B)
    # Compute Σ + B (stimulation)
    y = activation(s)
    # Apply activation function
    return y


# Test email
email_text = """
Hello! You have a chance to win a FREE prize. Click this link to claim your reward: http://example.com/win
"""

# Run perceptron
output = perceptron(email_text)
if output == 1:
    print("This email is classified as SPAM.")
else:
    print("This email is classified as NOT SPAM.")