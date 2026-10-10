"""Первая кривая S(p) и R на ER (n = 1000, <k> = 4, 5 seeds). Фаза I.

Ожидание: S(0) ~ 0.98; S(0.5) ~ 0.40; распад около p ~ 0.75; R ~ 0.40.
Вдали от порога расхождение с теорией не больше ~0.02. Около порога p ~ 0.75 симуляция
отходит от теории (чуть ниже перед порогом, выше после него) — это конечный размер, а не ошибка.

Теория для ER (локально древовидный граф; это частный случай S_MF):
    S(p) = (1 - p) * s,   s = 1 - exp(-c (1 - p) s).

Запуск из корня репозитория:  python experiments/first_robustness_curve.py
Результат: results/first_curve.png и R по seeds в консоль.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from netres.robustness.simulation import robustness_score, simulate_random_failures

N, C = 1000, 4.0
SEEDS = [0, 1, 2, 3, 4]
RESULTS = Path(__file__).resolve().parents[1] / "results"


def er_theory(p: float, c: float) -> float:
    """S(p) для ER: итерации s <- 1 - exp(-c (1 - p) s) от s = 1."""
    phi, s = 1.0 - p, 1.0
    for _ in range(100_000):
        s_new = 1.0 - np.exp(-c * phi * s)
        if abs(s_new - s) < 1e-12:
            break
        s = s_new
    return phi * s


def main() -> None:
    curves = []
    for seed in SEEDS:
        G = nx.fast_gnp_random_graph(N, C / (N - 1), seed=seed)
        S = simulate_random_failures(G, seed=1000 + seed)
        curves.append(S)
        print(f"seed {seed}: R = {robustness_score(S):.4f}")
    curves = np.array(curves)
    print(f"mean R = {curves[:, 1:].mean():.4f}")

    p = np.arange(N + 1) / N
    theory = [er_theory(x, C) for x in p]
    RESULTS.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(p, curves.mean(axis=0), label=f"симуляция, среднее по {len(SEEDS)} seeds")
    ax.plot(p, theory, "--", label="теория ER")
    ax.set_xlabel("доля удалённых вершин p = t / n")
    ax.set_ylabel("S(p)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(RESULTS / "first_curve.png", dpi=150)
    print(f"рисунок: {RESULTS / 'first_curve.png'}")


if __name__ == "__main__":
    main()
