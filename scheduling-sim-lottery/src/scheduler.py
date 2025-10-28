# scheduler.py
from dataclasses import dataclass
from typing import Dict, Optional, List, Iterable, Tuple
import random


class EmptyReadyQueue(Exception):
    """Raised when schedule() is called but no ready process has tickets."""
    pass


@dataclass
class Process:
    pid: str
    tickets: int
    state: str = "READY"  # READY | BLOCKED | DONE

    def is_schedulable(self) -> bool:
        return self.state == "READY" and self.tickets > 0


class LotteryScheduler:
    """
    A testable, seedable lottery scheduler.

    Expected semantics (also enforced by the tests):
    - Only READY processes with tickets > 0 participate in the lottery.
    - schedule() performs exactly ONE lottery draw and returns the selected pid.
    - run(n_ticks, quantum) repeatedly calls schedule() n_ticks times and
      tracks cpu_time[pid] += quantum for the selected process each tick.
    - block/unblock remove/add a process from the lottery without deleting it.
    - set_tickets updates ticket count immediately for the next draw.
    - remove(pid) marks the process DONE and removes it from the lottery.
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        self._procs: Dict[str, Process] = {}
        self.cpu_time: Dict[str, int] = {}
        # Students may replace random.Random with a stronger RNG; tests seed this.
        self._rng = random.Random(seed)

    # ----------------------------- Process API -----------------------------

    def add(self, pid: str, tickets: int) -> None:
        """Add a READY process with the given number of tickets."""
        if tickets < 0:
            raise ValueError("tickets must be >= 0")
        if pid in self._procs:
            raise ValueError(f"duplicate pid: {pid}")
        self._procs[pid] = Process(pid=pid, tickets=tickets, state="READY")
        self.cpu_time.setdefault(pid, 0)

    def remove(self, pid: str) -> None:
        """Mark a process as DONE and exclude it from further scheduling."""
        p = self._require(pid)
        p.state = "DONE"
        p.tickets = 0

    def set_tickets(self, pid: str, tickets: int) -> None:
        """Change ticket count; affects the next lottery immediately."""
        if tickets < 0:
            raise ValueError("tickets must be >= 0")
        p = self._require(pid)
        p.tickets = tickets

    def block(self, pid: str) -> None:
        """Temporarily block a process (e.g., waiting for I/O)."""
        p = self._require(pid)
        if p.state == "READY":
            p.state = "BLOCKED"

    def unblock(self, pid: str) -> None:
        """Make a blocked process READY again."""
        p = self._require(pid)
        if p.state == "BLOCKED":
            p.state = "READY"

    # ----------------------------- Core API --------------------------------

    def schedule(self) -> str:
        """
        Perform one lottery and return the selected pid.

        Algorithm sketch (students implement):
        1) Collect READY processes with tickets > 0.
        2) Sum ticket counts; draw an integer in [1, total].
        3) Walk the list, subtracting ticket counts until crossing the draw.
        """
        # TODO: implement the lottery draw (raise EmptyReadyQueue if none)


        # Defensive: should be unreachable
        return ready[-1].pid

    def run(self, n_ticks: int, quantum: int = 1) -> List[str]:
        """Run n_ticks lotteries; return the chosen pid per tick."""
        chosen: List[str] = []
        for _ in range(n_ticks):
            pid = self.schedule()
            self.cpu_time[pid] = self.cpu_time.get(pid, 0) + quantum
            chosen.append(pid)
        return chosen

    # ----------------------------- Helpers ---------------------------------

    def ready_snapshot(self) -> List[Tuple[str, int]]:
        """Convenience for tests/visualization: [(pid, tickets), ...] for READY procs."""
        return [(p.pid, p.tickets) for p in self._procs.values() if p.is_schedulable()]

    def _require(self, pid: str) -> Process:
        if pid not in self._procs:
            raise KeyError(f"unknown pid: {pid}")
        return self._procs[pid]
