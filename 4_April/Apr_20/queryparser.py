def parse_query(query):
    """
    Parse the query string into a list of tokens.
    """
    return query.split()


def execute_query(data, tokens):
    """
    Execute the query on the given data.
    """
    result = data
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "filter":
            i += 1
            key = tokens[i]
            i += 1
            value = tokens[i]
            result = filter_data(result, key, value)
        elif token == "project":
            i += 1
            keys = tokens[i:]
            result = project_data(result, keys)
            break
        elif token == "count":
            result = len(result)
            break
        else:
            raise ValueError("Invalid token: {}".format(token))
        i += 1
    return result


def filter_data(data, key, value):
    """
    Filter the data based on the given key-value pair.
    """
    return [item for item in data if item.get(key) == value]


def project_data(data, keys):
    """
    Project the data to include only the specified keys.
    """
    return [{key: item[key] for key in keys if key in item} for item in data]


# Example usage
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
]

query = "filter city New York project name age"
tokens = parse_query(query)
result = execute_query(data, tokens)
print(result)

query = "count"
tokens = parse_query(query)
result = execute_query(data, tokens)
print(result)
