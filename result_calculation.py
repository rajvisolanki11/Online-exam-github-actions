def result(score):
    if score == 0:
        raise ValueError("Invalid score")
    elif score >= 35:
        return "Pass"
    else:
        return "Fail"