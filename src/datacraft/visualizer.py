def simple_bar_chart(data):
    """Generate a simple bar chart from a dict."""
    for key, value in data.items():
        print(f"{key}: " + "#" * value)