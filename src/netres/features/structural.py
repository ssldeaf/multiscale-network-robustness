"""Признаки M1 и M2 (протокол НИР-2, §4) — они же структурный профиль ВРС. Фаза V.

M1: log n, <k>, kappa = <k^2>/<k>, доля вершин степени 1, транзитивность,
    square clustering (среднее по вершинам), доля вершин 2-ядра,
    ассортативность по степеням (для регулярных графов не определена: 0 + флаг),
    доля мостов = мосты / m, доля точек сочленения = точки / n.
M2: log <l>, log n / log <l> — прокси масштаба, НЕ размерность.
Только для описания (в модели не входит): флаг планарности.
"""

from __future__ import annotations

import networkx as nx


def m1_features(G: nx.Graph) -> dict[str, float]:
    raise NotImplementedError


def m2_features(G: nx.Graph) -> dict[str, float]:
    raise NotImplementedError


def planarity_flag(G: nx.Graph) -> bool:
    raise NotImplementedError
