
def index(smolkovia, n):
    """ Basic solution """
    result = -1
    for cislo_smolka, smolko in enumerate(smolkovia):
        if cislo_smolka == n:
            result = smolko ** n

    return result


def index(smolkovia, n):
    """ Second solution """
    return smolkovia[n] ** n if len(smolkovia) >= n else -1
