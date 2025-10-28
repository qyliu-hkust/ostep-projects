# Project: Implementing a Lottery Scheduler

**Objective.** Implement and evaluate a [lottery scheduler](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-lottery.pdf) — a probabilistic CPU scheduler that allocates CPU time in proportion to the number of tickets each process holds. 

---

## Learning Outcomes
By the end of this project you will be able to:
- Explain proportional fairness and how randomness yields fair sharing over time.
- Implement a schedulable process abstraction and a lottery-based `schedule()` function.
- Handle dynamic changes: blocking/unblocking and ticket updates.
- Validate a stochastic system with statistical tests.

---

## What We Provide
- `scheduler.py`: a starter file with API definitions and docstrings.
- `tests/`: pytest test suite verifying core behavior.
- This instruction file.

> **Important:** Do not change function names or their semantics. You may add helper methods.

---

## Core Requirements

1. **Process API**
   - `add(pid, tickets)`: add a READY process with `tickets >= 0`.
   - `remove(pid)`: mark process DONE (no longer scheduled).
   - `set_tickets(pid, tickets)`: change ticket count; affects the next lottery.
   - `block(pid)` / `unblock(pid)`: change process state (BLOCKED vs READY).

2. **Scheduling API**
   - `schedule() -> pid`:
     - Consider **only** processes that are `READY` and have `tickets > 0`.
     - Draw one integer uniformly at random from `[1, total_tickets]`.
     - Walk the READY list cumulatively to select a winner.
     - If no READY process has tickets, raise `EmptyReadyQueue`.
   - `run(n_ticks, quantum=1) -> List[str]`:
     - Call `schedule()` `n_ticks` times.
     - Update `cpu_time[pid] += quantum` for the selected process each tick.

3. **Determinism for Testing**
   - The scheduler is initialized with an optional `seed` (`LotteryScheduler(seed=...)`).
   - Use this RNG for all drawings to keep unit tests reproducible.


---

## Getting Started

Finish TODO in `scheduler.py` and then run
```bash
pytest -q
```