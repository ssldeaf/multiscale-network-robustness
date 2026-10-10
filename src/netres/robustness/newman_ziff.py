"""Алгоритм Ньюмана–Зиффа: вся кривая S за почти линейное время. Фаза II (19–25.10).

Источник: Newman, Ziff (2001), Phys. Rev. E 64, 016706; Newman, «Networks», 16.5.

Удалять вершины в порядке order — то же самое, что ДОБАВЛЯТЬ их в обратном порядке
в пустой граф. Компоненты поддерживаются системой непересекающихся множеств
(union-find) со сжатием путей и объединением по размеру; после каждого добавления
известен размер наибольшей компоненты.

Требование: для одного и того же order результат ТОЧНО совпадает с
simulation.simulate_failures (добавить тест test_newman_ziff_matches_naive).
Замер: решётка 64 x 64 — наивно ~4 с на порядок, Ньюман–Зифф на чистом Python ~9 мс.
"""

from __future__ import annotations

from collections.abc import Hashable, Sequence

import networkx as nx
import numpy as np


def newman_ziff_curve(G: nx.Graph, order: Sequence[Hashable]) -> np.ndarray:
    """Кривая S длины n + 1 — тот же контракт, что у simulation.simulate_failures."""
    raise NotImplementedError
