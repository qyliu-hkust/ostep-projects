# tests/test_basic.py
import math
import pytest
from scheduler import LotteryScheduler, EmptyReadyQueue


def test_proportional_fairness_long_run():
    sch = LotteryScheduler(seed=7)
    sch.add("A", tickets=1)
    sch.add("B", tickets=2)
    sch.add("C", tickets=3)
    total = 120_000
    sch.run(total, quantum=1)

    # Expected shares: 1:2:3 (≈ 16.7%, 33.3%, 50%)
    a = sch.cpu_time["A"] / total
    b = sch.cpu_time["B"] / total
    c = sch.cpu_time["C"] / total

    # Allow small sampling error (±1.5 percentage points)
    assert abs(a - (1/6)) < 0.015
    assert abs(b - (2/6)) < 0.015
    assert abs(c - (3/6)) < 0.015
    assert math.isclose(a + b + c, 1.0, rel_tol=1e-6)

def test_block_unblock_and_zero_tickets():
    sch = LotteryScheduler(seed=99)
    sch.add("X", tickets=10)
    sch.add("Y", tickets=0)   # zero tickets => never scheduled
    sch.add("Z", tickets=5)

    # Block Z; only X participates
    sch.block("Z")
    picks = sch.run(50)
    assert set(picks) == {"X"}
    assert sch.cpu_time["X"] == 50

    # Unblock Z; both X and Z participate according to tickets
    sch.unblock("Z")
    sch.run(1000)
    # Z should get ~ 1/3 of CPU time compared to X's 2/3 (10:5)
    ratio = sch.cpu_time["Z"] / (sch.cpu_time["X"] - 50)  # exclude earlier 50
    assert 0.40 <= ratio <= 0.60  # loose bounds due to randomness

def test_empty_ready_queue():
    sch = LotteryScheduler(seed=0)
    sch.add("A", tickets=0)
    sch.block("A")
    with pytest.raises(EmptyReadyQueue):
        sch.schedule()
