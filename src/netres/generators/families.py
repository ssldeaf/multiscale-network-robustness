"""Широкий набор синтетических графов (протокол НИР-2, §2.2). Фаза II (19–25.10).

Правила:
- n выбирается снаружи (логравномерно в [1000; 4000]) и передаётся генератору;
- параметры заранее задаются внутри режима, где наибольшая компонента >= 0.9 n почти всегда;
- возвращается G0 = наибольшая компонента с вершинами 0..n'-1 и доля её размера;
- реализации с наибольшей компонентой < 0.9 n отбрасываются; доля отброшенных отчитывается
  по каждому семейству;
- RGG: средняя степень заметно выше ~4.5 — порога появления гигантской компоненты
  (это НЕ порог связности: тот растёт как log n);
- разрежённая решётка с открытыми границами — она же эталонный ансамбль для ВРС.
"""

from __future__ import annotations

import networkx as nx


def largest_component(G: nx.Graph) -> tuple[nx.Graph, float]:
    """(наибольшая компонента с вершинами 0..n'-1, её доля |LCC| / n)."""
    raise NotImplementedError


def erdos_renyi(n: int, c: float, seed: int) -> nx.Graph:
    """G(n, p), p = c / (n - 1)."""
    raise NotImplementedError


def random_regular(n: int, k: int, seed: int) -> nx.Graph:
    raise NotImplementedError


def barabasi_albert(n: int, m: int, seed: int) -> nx.Graph:
    raise NotImplementedError


def powerlaw_configuration(n: int, gamma: float, k_min: int, seed: int) -> nx.Graph:
    """Конфигурационная модель, p_k ~ k^(-gamma), gamma в [2.5; 3.5]; петли и кратные рёбра убрать."""
    raise NotImplementedError


def random_geometric_2d(n: int, c: float, seed: int) -> nx.Graph:
    """Единичный квадрат, радиус из c = n * pi * r^2."""
    raise NotImplementedError


def diluted_square_lattice(L: int, p: float, seed: int, periodic: bool) -> nx.Graph:
    """Квадратная решётка L x L, каждое ребро сохраняется с вероятностью p."""
    raise NotImplementedError


def watts_strogatz(n: int, k: int, beta: float, seed: int) -> nx.Graph:
    raise NotImplementedError
