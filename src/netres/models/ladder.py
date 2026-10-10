"""Лестница M0 -> M1 -> M2 -> M3 (протокол НИР-2, §4–5). Фаза V и декабрь.

Единица наблюдения — исходный граф. y = R̄ (или ΔR = R̄ - R_MF). Группа — id исходного графа
(для траекторий перестройки — id базы и реализации).
Модели: Ridge (стандартизация внутри Pipeline), RandomForest, HistGradientBoosting;
гиперпараметры — вложенная групповая CV, малая фиксированная сетка, одинаковый бюджет.
Режим I (интерполяция): повторённый GroupKFold, 5 фолдов x 10 повторов.
Режим II (экстраполяция): leave-one-family-out; leave-parameter-region-out
    (крайние 20 % по <k> или n); на траекториях — отложенный диапазон q_E. Выводы не смешивать.
Сравнение ступеней: парные разности |ошибок| на одних тестовых графах;
    кластерный бутстреп по id графов (2000 повторов) -> 95 % интервал ΔMAE; относительная ΔMAE.
Эффект есть, только если интервал не содержит 0 и это верно для всех трёх моделей.
«Среднее R по семейству» — диагностический ориентир, не baseline.
"""

from __future__ import annotations

FEATURE_SETS: dict[str, list[str]] = {
    "M0": ["r_mf"],
    "M1": [],  # M0 + признаки M1 (features/structural.py)
    "M2": [],  # M1 + log_mean_path, scale_proxy
    "M3": [],  # M2 + представление, выбранное в E-rep
}


def evaluate_ladder(*args, **kwargs):
    raise NotImplementedError


def paired_cluster_bootstrap(*args, **kwargs):
    raise NotImplementedError
