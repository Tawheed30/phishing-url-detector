def decide_response(score, ml_label, ml_confidence, vt_malicious):
    """
    Returns automated SOC-style response decision
    """

    if vt_malicious > 0:
        return "BLOCK"

    elif ml_label == 1 and ml_confidence >= 0.7:
        return "BLOCK"

    elif score >= 3:
        return "MONITOR"

    else:
        return "ALLOW"

