"""Determine Bob's response to a given input."""
def response(hey_bob):
    """
    Gives specific responses to specific inputs.
    """
    call = hey_bob.strip()
    if call == "":
        return "Fine. Be that way!"
    elif ("?" in call[-1]) and (call.isupper()):
        return "Calm down, I know what I'm doing!"
    elif "?" in call[-1]:
        return "Sure."
    elif call.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
