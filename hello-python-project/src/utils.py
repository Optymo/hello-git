def greet(name: str) -> str:
    """
    Zwraca pozdrowienie dla podanej osoby.

    Args:
        name (str): Imię lub identyfikator osoby, której ma dotyczyć powitanie.

    Returns:
        str: Sformatowany łańcuch w postaci "hello, <name>!".

    Examples:
        >>> greet("Ala")
        'hello, Ala!'
    """
    return f"hello, {name}!"