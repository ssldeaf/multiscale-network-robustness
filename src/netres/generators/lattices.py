"""Решётки и самоподобные графы с известной структурой. Фазы II и IV.

Базы траекторий перестройки (протокол НИР-2, §2.1), периодические границы, n ~ 4096:
    квадратная 64 x 64 (k = 4), кубическая 16 x 16 x 16 (k = 6), сотовая (k = 3),
    (u,v)-цветок (2,2), поколение 6 (n = 2732, d_B = 2 — сверить с Rozenfeld и др., 2007).
Графы для E-rep (§2.3): решётки 2D (L = 32…128) и 3D (L = 8…20),
    треугольник Серпинского (поколения 5–8, d = ln 3 / ln 2), цветы (2,2) и (2,3).
"""

from __future__ import annotations

import networkx as nx


def square_lattice(L: int, periodic: bool = True) -> nx.Graph:
    raise NotImplementedError


def cubic_lattice(L: int, periodic: bool = True) -> nx.Graph:
    raise NotImplementedError


def honeycomb_lattice(rows: int, cols: int, periodic: bool = True) -> nx.Graph:
    """Можно через nx.hexagonal_lattice_graph — проверить условия на rows, cols при periodic=True."""
    raise NotImplementedError


def uv_flower(u: int, v: int, generation: int) -> nx.Graph:
    """(u,v)-цветок: на каждом шаге каждое ребро заменяется двумя путями длины u и v."""
    raise NotImplementedError


def sierpinski_gasket(generation: int) -> nx.Graph:
    raise NotImplementedError
