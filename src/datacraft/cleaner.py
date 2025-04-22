def remove_nulls(data):
    """Remove keys with None values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}