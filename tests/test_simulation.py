"""Тесты симуляции отказов. Ответы посчитаны руками (план дня 09.10).

Сначала посчитай каждую строку CASES на бумаге сам, потом сверяйся.
"""

import networkx as nx
import numpy as np
import pytest

from netres.robustness.simulation import (
    largest_component_fraction,
    robustness_score,
    simulate_failures,
    simulate_random_failures,
)

GRID_ORDER = [(1, 1), (0, 1), (2, 1), (1, 0), (1, 2), (0, 0), (0, 2), (2, 0), (2, 2)]

# (имя, граф, порядок удаления, ожидаемая кривая S, ожидаемое R)
CASES = [
    ("K10", nx.complete_graph(10), [3, 7, 0, 9, 1, 5, 2, 8, 4, 6],
     [(10 - t) / 10 for t in range(11)], 0.45),
    ("P5", nx.path_graph(5), [2, 0, 1, 3, 4],
     [1, 0.4, 0.4, 0.4, 0.2, 0], 0.28),
    ("C6", nx.cycle_graph(6), [0, 3, 1, 2, 4, 5],
     [1, 5 / 6, 1 / 3, 1 / 3, 1 / 3, 1 / 6, 0], 1 / 3),
    ("star_center_first", nx.star_graph(4), [0, 1, 2, 3, 4],
     [1, 0.2, 0.2, 0.2, 0.2, 0], 0.16),
    ("star_center_last", nx.star_graph(4), [1, 2, 3, 4, 0],
     [1, 0.8, 0.6, 0.4, 0.2, 0], 0.4),
    ("five_isolated", nx.empty_graph(5), [0, 1, 2, 3, 4],
     [0.2, 0.2, 0.2, 0.2, 0.2, 0], 0.16),
    ("grid3x3", nx.grid_2d_graph(3, 3), GRID_ORDER,
     [1, 8 / 9, 7 / 9, 3 / 9, 3 / 9, 1 / 9, 1 / 9, 1 / 9, 1 / 9, 0], 25 / 81),
]


@pytest.mark.parametrize("name, G, order, S_exp, R_exp", CASES, ids=[c[0] for c in CASES])
def test_curve_exact(name, G, order, S_exp, R_exp):
    S = simulate_failures(G, order)
    assert len(S) == G.number_of_nodes() + 1
    np.testing.assert_allclose(S, S_exp, atol=1e-12)


@pytest.mark.parametrize("name, G, order, S_exp, R_exp", CASES, ids=[c[0] for c in CASES])
def test_R_exact(name, G, order, S_exp, R_exp):
    assert robustness_score(simulate_failures(G, order)) == pytest.approx(R_exp, abs=1e-12)


def test_largest_component_fraction_basic():
    assert largest_component_fraction(nx.Graph(), 10) == 0.0
    G = nx.Graph([(0, 1), (1, 2), (3, 4)])  # компоненты размеров 3 и 2
    assert largest_component_fraction(G, 10) == pytest.approx(0.3)


@pytest.mark.parametrize("seed", range(20))
def test_lcc_matches_networkx(seed):
    G = nx.gnp_random_graph(60, 0.03, seed=seed)
    expected = max(len(c) for c in nx.connected_components(G)) / 60
    assert largest_component_fraction(G, 60) == pytest.approx(expected)


def _property_graphs():
    return [
        ("er", nx.gnp_random_graph(60, 0.06, seed=1)),
        ("grid6x6", nx.grid_2d_graph(6, 6)),  # вершины-кортежи
        ("star", nx.star_graph(9)),
        ("two_triangles", nx.disjoint_union(nx.cycle_graph(3), nx.cycle_graph(3))),
    ]


@pytest.mark.parametrize("name, G", _property_graphs(), ids=[g[0] for g in _property_graphs()])
@pytest.mark.parametrize("seed", [0, 1, 2])
def test_curve_properties(name, G, seed):
    n = G.number_of_nodes()
    nodes_before, edges_before = set(G.nodes), {frozenset(e) for e in G.edges}
    S = simulate_random_failures(G, seed)
    assert len(S) == n + 1
    assert S[-1] == 0
    assert np.all(np.diff(S) <= 1e-12), "S не должна расти"
    t = np.arange(n + 1)
    assert np.all(S <= (n - t) / n + 1e-12), "S_t <= (n - t) / n"
    assert robustness_score(S) <= (n - 1) / (2 * n) + 1e-12
    assert set(G.nodes) == nodes_before and {frozenset(e) for e in G.edges} == edges_before, "G изменился"


def test_same_seed_same_curve():
    G = nx.gnp_random_graph(80, 0.05, seed=3)
    np.testing.assert_array_equal(simulate_random_failures(G, 7), simulate_random_failures(G, 7))
