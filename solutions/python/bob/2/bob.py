"""Determine Bob's response to a given input."""
def response(hey_bob):
    """
    Gives specific responses to specific inputs.
    """
    call = hey_bob.strip()
    if call == "":
        return "Fine. Be that way!"
    if ("?" in call[-1]) and (call.isupper()):
        return "Calm down, I know what I'm doing!"
    if "?" in call[-1]:
        return "Sure."
    if call.isupper():
        return "Whoa, chill out!"
    return "Whatever."
