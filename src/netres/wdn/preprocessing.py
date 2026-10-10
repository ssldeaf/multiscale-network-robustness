"""Граф водопроводной сети из EPANET .inp. Фаза II.

Строго по протоколу 09_nir/nir2/wdn_preprocessing.md (зафиксирован 10.10.2026 до расчётов).
Объект — физическая топология сети. Манифест: data/wdn/manifest.csv.

G_raw:
 1. wn = wntr.network.WaterNetworkModel(path); M = wn.to_graph()  (MultiDiGraph, ключ ребра = имя связи);
 2. без ориентации: M.to_undirected();
 3. все вершины (Junction, Tank, Reservoir) и все связи (Pipe, Pump, Valve) — независимо от
    начального статуса; статус — атрибут ребра; число закрытых связей записать
    (link.initial_status.name == 'Closed');
 4. простой граф: параллельные связи схлопнуть, атрибуты ребра multiplicity и список имён/типов;
    петли удалить и посчитать;
 5. вершины степени 1 и 2 сохраняются;
 6. если сеть не связна — признаки по наибольшей компоненте, её доля записывается.

G_contracted (только проверка чувствительности, основной вариант всегда G_raw):
 одним проходом каждая максимальная цепочка узлов степени 2 (не баки и не резервуары) между
 вершинами степени != 2 заменяется одним ребром; петли удаляются; кратные рёбра сливаются;
 компонента-чистый цикл остаётся как есть; повторных проходов нет.
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx


def sha256_file(path: str | Path) -> str:
    raise NotImplementedError


def load_physical_topology(path: str | Path) -> tuple[nx.Graph, dict]:
    """(G_raw, статистика для manifest.csv)."""
    raise NotImplementedError


def contract_degree2(G_raw: nx.Graph) -> tuple[nx.Graph, dict]:
    """(G_contracted, статистика: стянутые вершины, удалённые петли, слитые рёбра)."""
    raise NotImplementedError
