"""Структурные профили ВРС и сравнение с ансамблями (wdn_preprocessing.md, §5–6). Фаза V.

Только признаки X (M1 ∪ M2), без R (протокол НИР-2, §2.4).
- Нулевая модель: связные перестановки с сохранением степеней, 50 реализаций, бюджет 10 * m
  попыток на реализацию; записать успешные перестановки и q_E; q_E < 0.85 -> «слабый нуль».
  z, перцентиль и x / mean — только для признаков, НЕ заданных степенями
  (<k>, kappa, доля вершин степени 1 в нуле фиксированы, sigma = 0).
- Сопоставимый пространственный ансамбль: разрежённая квадратная решётка с ОТКРЫТЫМИ
  границами; подгоняется наибольшая компонента по n и <k>; остаточное расхождение по kappa,
  доле степени 1 и максимальной степени записывается. При <k> < ~2.33 сопоставимая
  решётка околокритическая — это ограничение, а не повод вводить новое семейство.
- Контрастный ансамбль: ER G(n, m), признаки по наибольшей компоненте; сопоставимым не считается.
- RGG для ВРС не используется.
- Покрытие отдельного признака: перцентиль ВРС среди графов широкого набора в [1, 99].
"""

from __future__ import annotations

import networkx as nx


def null_ensemble(G: nx.Graph, n_samples: int = 50, attempts_factor: int = 10, seed: int = 0) -> list[dict]:
    raise NotImplementedError


def diluted_lattice_reference(n_target: int, k_target: float, n_samples: int = 50, seed: int = 0) -> list[dict]:
    raise NotImplementedError


def er_contrast(n: int, m: int, n_samples: int = 50, seed: int = 0) -> list[dict]:
    raise NotImplementedError


def compare_to_ensemble(x_real: dict, ensemble: list[dict], skip: set[str] = frozenset()) -> dict:
    """{признак: (z, перцентиль, x / mean)}; признаки из skip не сравниваются."""
    raise NotImplementedError


def univariate_coverage(x_real: dict, synthetic: list[dict]) -> dict:
    """{признак: (перцентиль, покрыт ли: перцентиль в [1, 99])}."""
    raise NotImplementedError
