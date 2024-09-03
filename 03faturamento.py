import json

with open('faturamento.json', 'r') as f:
    inv = json.load(f)

valid_values = [d['valor'] for d in inv if d['valor'] > 0]

min_inv = min(valid_values)
max_inv = max(valid_values)

monthly_avg = sum(valid_values) / len(valid_values)

d_above_avg = len([value for value in valid_values if value > monthly_avg])