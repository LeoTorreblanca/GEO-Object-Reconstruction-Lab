import math


def observable(theta_deg):
    theta = math.radians(theta_deg)
    return math.cos(theta) ** 2


def complement(theta_deg):
    theta = math.radians(theta_deg)
    return math.sin(theta) ** 2


def coupling_gap(theta_deg):
    a = observable(theta_deg)
    b = complement(theta_deg)
    return a * b


def coherence(theta_deg):
    return coupling_gap(theta_deg) / 0.25


def imbalance(theta_deg):
    a = observable(theta_deg)
    b = complement(theta_deg)
    return abs(a - b)
