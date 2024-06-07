def apply_filter(data, criteria):
    filtered_data = []
    for item in data:
        # Evaluate each item against the criteria
        if evaluate_criteria(item, criteria):
            filtered_data.append(item)
    return filtered_data

def evaluate_criteria(item, criteria):
    if 'and' in criteria:
        # If criteria has 'and', all conditions must be true
        return all(evaluate_criteria(item, sub_criteria) for sub_criteria in criteria['and'])
    elif 'or' in criteria:
        # If criteria has 'or', any condition must be true
        return any(evaluate_criteria(item, sub_criteria) for sub_criteria in criteria['or'])
    else:
        # Evaluate individual condition
        field, operator, value = criteria['field'], criteria['operator'], criteria['value']
        item_value = item.get(field)
        if operator == '==':
            return item_value == value
        elif operator == '!=':
            return item_value != value
        elif operator == '>':
            return item_value > value
        elif operator == '<':
            return item_value < value
        elif operator == '>=':
            return item_value >= value
        elif operator == '<=':
            return item_value <= value
        else:
            raise ValueError("Invalid operator")

# Example usage:
data = [
    {'name': 'Alice', 'age': 30, 'gender': 'female'},
    {'name': 'Bob', 'age': 25, 'gender': 'male'},
    {'name': 'Charlie', 'age': 35, 'gender': 'male'},
    {'name': 'Diana', 'age': 40, 'gender': 'female'}
]

criteria = {
    'and': [
        {'field': 'age', 'operator': '>=', 'value': 30},
        {'or': [
            {'field': 'gender', 'operator': '==', 'value': 'female'},
            {'field': 'name', 'operator': '==', 'value': 'Bob'}
        ]}
    ]
}

filtered_data = apply_filter(data, criteria)
print(filtered_data)
