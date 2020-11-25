import yaml
from pathlib import Path

cwd = Path(__file__).parent.parent
config_path = cwd / "config.yml"


class Value:
    try:
        with open(config_path, "r") as configfile:
            config = yaml.load(configfile, Loader=yaml.FullLoader)
    except OSError:
        print("Configuration file doesn't exist or has the incorrect format")

    elite_number = config['elite_number']
    population_number = config['population_number']
    mutation_inverse = config['mutation_inverse']
    max_epochs = config['max_epochs']

    triangles = [(1, 2, 3), (1, 0, 2), (0, 0, 2), (1, 1, 0), (0, 0, 0),
                 (1, 3, 2), (1, 0, 0), (2, 2, 2), (1, 3, 2), (2, 1, 0),
                 (1, 1, 1), (0, 3, 3), (1, 2, 3), (1, 2, 0), (3, 3, 3),
                 (2, 0, 1), (1, 0, 2), (2, 2, 0), (3, 0, 0), (0, 1, 2)]

    pa = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    pb = [(0, 2), (4, 1), (5, 0), (13, 2), (14, 1)]
    pc = [(0, 1), (1, 2), (5, 1), (6, 1), (7, 0)]
    pd = [(1, 1), (2, 2), (7, 1), (8, 0), (9, 0)]
    pe = [(2, 1), (3, 2), (9, 1), (10, 1), (11, 0)]
    pf = [(3, 1), (4, 2), (11, 1), (12, 0), (13, 1)]
    pg = [(12, 1), (13, 0), (14, 0), (15, 1), (19, 2)]
    ph = [(5, 2), (6, 0), (14, 2), (15, 2), (16, 1)]
    pi = [(6, 2), (7, 2), (8, 2), (16, 2), (17, 1)]
    pj = [(8, 1), (9, 2), (10, 0), (17, 2), (18, 1)]
    pk = [(10, 2), (11, 2), (12, 2), (18, 2), (19, 1)]
    pl = [(15, 0), (16, 0), (17, 0), (18, 0), (19, 0)]

    pos = [pa, pb, pc, pd, pe, pf, pg, ph, pi, pj, pk, pl]

    A = config['A']
    B = config['B']
    C = config['C']
    D = config['D']
    E = config['E']
    F = config['F']
    G = config['G']
    H = config['H']
    I = config['I']
    J = config['J']
    K = config['K']
    L = config['L']

    letters = [A, B, C, D, E, F, G, H, I, J, K, L]
    faces = [(A, C, B), (A, D, C), (A, E, D), (A, F, E), (A, B, F),
             (B, C, H), (H, C, I), (C, D, I), (D, J, I), (D, E, J),
             (J, E, K), (E, F, K), (F, G, K), (G, F, B), (G, B, H),
             (L, G, H), (L, H, I), (L, I, J), (L, J, K), (L, K, G)]
