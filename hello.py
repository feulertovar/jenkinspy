def say_hello(name="Jenkins"):
    """
    Returns a greeting message. If no name is provided, defaults to "Jenkins".
    If an empty string is provided, defaults to "Jenkins".
    Raises TypeError if the input is not a string.
    """
    if not isinstance(name, str):  # Check if the input is not a string
        raise TypeError("Input must be a string.")
    if not name:  # If the name is an empty string or None, default to 'Jenkins'
        name = "Jenkins"
    return f"Hello, {name}!"
