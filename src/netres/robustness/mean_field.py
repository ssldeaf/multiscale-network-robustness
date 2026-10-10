"""Перколяционный прогноз по распределению степеней. Фаза III (26.10–01.11).

Протокол НИР-2, §1. Источники: Newman, «Networks», гл. 13 и 16.2;
Callaway и др. (2000); Newman, Strogatz, Watts (2001).

    G0(x) = sum_k p_k x^k,      G1(x) = G0'(x) / G0'(1) = sum_k (k + 1) p_{k+1} x^k / <k>.
Перколяция по вершинам, phi — доля оставшихся вершин:
    u = 1 - phi + phi * G1(u)      (наименьший корень на [0, 1]: итерации от u = 0),
    S_MF(phi) = phi * (1 - G0(u)).
    R_MF = (1/n) * sum_{t=1..n} S_MF(1 - t/n) — на той же сетке, что R.
Порог: phi_c = <k> / (<k^2> - <k>) = 1 / (kappa - 1),  kappa = <k^2> / <k>.

Контрольные значения для тестов (предел n -> бесконечности; на сетке n отличие порядка 1/n):
    ER, c = 4:                R_MF = s1 - s1^2/2 - Li2(s1)/c^2 = 0.4031, s1 — корень s = 1 - exp(-c s);
    случайный 3-регулярный:   R_MF = 3 ln 2 - 7/4 = 0.3294, phi_c = 1/2.

R_MF — асимптотический прогноз для локально древовидных графов, а не точная теория.
Для отказов рёбер (НИР-3): S = 1 - G0(u), без множителя phi.
"""

from __future__ import annotations

import networkx as nx
import numpy as np


def degree_distribution(G: nx.Graph) -> np.ndarray:
    """p_k, k = 0..k_max (сумма = 1)."""
    raise NotImplementedError


def critical_occupation(pk: np.ndarray) -> float:
    """phi_c = <k> / (<k^2> - <k>)."""
    raise NotImplementedError


def solve_u(phi: float, pk: np.ndarray, tol: float = 1e-13, max_iter: int = 100_000) -> float:
    """Наименьший корень u = 1 - phi + phi * G1(u) на [0, 1] — итерации от u = 0."""
    raise NotImplementedError


def s_mean_field(phi: float, pk: np.ndarray) -> float:
    """S_MF(phi) = phi * (1 - G0(u))."""
    raise NotImplementedError


def r_mean_field(pk: np.ndarray, n: int) -> float:
    """R_MF на сетке t = 1..n: (1/n) * sum S_MF(1 - t/n)."""
    raise NotImplementedError
