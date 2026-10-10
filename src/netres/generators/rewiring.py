"""Перестройка с сохранением степеней и связности (протокол НИР-2, §2.1). Фаза III.

Только nx.connected_double_edge_swap; его параметр nswap считает ПОПЫТКИ, а не успешные перестановки.
    q_E    = 1 - |E(G_q) ∩ E(G0)| / m — доля реально изменённых рёбер (ось эксперимента);
    q_swap = число успешных перестановок / m — записывается отдельно. q_E != q_swap.
Сетка q_E: 0; 0.01; 0.02; 0.05; 0.1; 0.2; 0.4; 0.6; ~0.85; по 10 реализаций на точку.
Перестановки делаются порциями, пока q_E не достигнет целевого.
Нулевая модель для ВРС (wdn_preprocessing.md, §5): фиксированный бюджет 10 * m попыток.
"""

from __future__ import annotations

from collections.abc import Sequence

import networkx as nx


def edge_change_fraction(G0: nx.Graph, G: nx.Graph) -> float:
    """q_E (рёбра сравниваются как неупорядоченные пары)."""
    raise NotImplementedError


def rewire_to_targets(
    G0: nx.Graph, targets: Sequence[float], seed: int, batch_fraction: float = 0.01
) -> list[tuple[float, nx.Graph, float]]:
    """Одна траектория: для каждого целевого q_E -> (достигнутое q_E, граф-копия, q_swap)."""
    raise NotImplementedError


def rewire_fixed_budget(G: nx.Graph, attempts: int, seed: int) -> tuple[nx.Graph, int, float]:
    """Копия G после attempts попыток -> (граф, число успешных перестановок, q_E)."""
    raise NotImplementedError
