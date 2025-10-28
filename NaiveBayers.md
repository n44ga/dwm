import math
from collections import defaultdict

#
# Step 1: Create Dataset
#
# Features: Outlook, Temperature | Target: Play (Yes/No)
dataset = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rainy', 'Mild', 'Yes'],
    ['Rainy', 'Cool', 'Yes'],
    ['Rainy', 'Cool', 'No'],
    ['Overcast', 'Cool', 'Yes'],
    ['Sunny', 'Mild', 'No'],
    ['Sunny', 'Cool', 'Yes'],
    ['Rainy', 'Mild', 'Yes'],
    ['Sunny', 'Mild', 'Yes'],
    ['Overcast', 'Mild', 'Yes'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rainy', 'Mild', 'No']
]

#
# Step 2: Split Features (X) & Labels (y)
#
X = [row[:-1] for row in dataset] # Features
y = [row[-1] for row in dataset] # Labels
classes = set(y)

#
# Step 3: Calculate Priors P(C)
#
priors = {c: y.count(c)/len(y) for c in classes}

#
# Step 4: Calculate Likelihoods P(X|C)
#
likelihoods = defaultdict(lambda: defaultdict(dict))
for feature_idx in range(len(X[0])):
    values = set(row[feature_idx] for row in X)
    for value in values:
        for c in classes:
            count = sum(1 for i in range(len(X)) if X[i][feature_idx] == value and y[i] == c)
            total = sum(1 for i in range(len(X)) if y[i] == c)
            likelihoods[feature_idx][value][c] = count / total if total > 0 else 0

#
# Step 5: Prediction Function
#
def predict(sample):
    posteriors = {}
    for c in classes:
        # Start with prior P(C)
        prob = math.log(priors[c])
        for feature_idx, value in enumerate(sample):
            # Add log-likelihoods P(X|C)
            if value in likelihoods[feature_idx]:
                prob += math.log(likelihoods[feature_idx][value].get(c, 1e-6)) # Using 1e-6 for smoothing
        posteriors[c] = prob

    # Convert log-probs to probabilities
    max_log = max(posteriors.values())
    exp_probs = {c: math.exp(v - max_log) for c, v in posteriors.items()}
    total_sum_exp_probs = sum(exp_probs.values())
    normalized = {c: v / total_sum_exp_probs for c, v in exp_probs.items()}

    predicted_class = max(normalized, key=normalized.get)
    return predicted_class, normalized

#
# Step 6: Test the Model
#
test_sample = ['Sunny', 'Cool']
pred_class, prob_values = predict(test_sample)

print(f"Test Sample:", test_sample)
print(f"Predicted Class:", pred_class)
print(f"Class Probabilities:", prob_values)