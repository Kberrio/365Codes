def merge_datasets(datasets, key):
    """
    Merge multiple datasets based on a common key.

    Args:
        datasets (list of dict): List of datasets to be merged.
        key (str): Key to merge datasets on.

    Returns:
        list of dict: Merged dataset.
    """

    # Create a dictionary to store merged data
    merged_data = {}

    # Loop through each dataset
    for dataset in datasets:
        # Loop through each record in the dataset
        for record in dataset:
            # Extract the value of the key
            key_value = record[key]
            # If the key value is not in the merged data dictionary, add it
            if key_value not in merged_data:
                merged_data[key_value] = {}
            # Merge the record into the merged data dictionary
            merged_data[key_value].update(record)

    # Convert the merged data dictionary to a list of records
    merged_list = [record for _, record in merged_data.items()]

    return merged_list

# Example usage:
dataset1 = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 35}
]

dataset2 = [
    {"id": 1, "city": "New York"},
    {"id": 2, "city": "Los Angeles"}
]

merged_dataset = merge_datasets([dataset1, dataset2], "id")
print(merged_dataset)
