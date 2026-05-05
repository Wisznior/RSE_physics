from pint import UnitRegistry

reg = UnitRegistry()

def calc_speed(distance: str, time: str) -> str:
    """
    Oblicza prędkość i zwraca wynik w km/h w postaci stringa
    (100m, 10s) -> 36km/h
    """
    d = reg(distance)
    t = reg(time)
    v = d/t

    return str(v.to('km/h'))