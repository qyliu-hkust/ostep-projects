# tests/test_dynamic_updates.py
from scheduler import LotteryScheduler

def test_dynamic_ticket_updates_affect_next_draw():
    sch = LotteryScheduler(seed=3)
    sch.add("P", tickets=1)
    sch.add("Q", tickets=1)

    # First few picks split ~50/50
    sch.run(10000)
    p1 = sch.cpu_time["P"]
    q1 = sch.cpu_time["Q"]
    assert 0.40 <= p1 / (p1 + q1) <= 0.60

    # Now boost Q's tickets; should dominate subsequently
    sch.set_tickets("Q", 9)
    sch.run(10000)
    p2 = sch.cpu_time["P"] - p1
    q2 = sch.cpu_time["Q"] - q1
    # Q should now win ~90% of subsequent draws
    assert 0.84 <= q2 / (p2 + q2) <= 0.96
