from collections import deque

print("=== Airtel Queue Example ===")
airtel_queue = deque(["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"])
print("Initial queue:", list(airtel_queue))

for _ in range(4):
    airtel_queue.popleft()

print("Queue after 4 served:", list(airtel_queue))
print("Now in front:", airtel_queue[0])  # who is at front

print("\n=== RSSB Queue Example ===")
rssb_queue = deque(["P1", "P2", "P3", "P4", "P5"])
print("Initial queue:", list(rssb_queue))

print("Last served:", rssb_queue[-1])

print("\n=== Challenge ===")
print("Polling stations must use a Queue (FIFO) so people are served in the order they arrive, not Stack.")



print("\n=== Reflection ===")
print("FIFO builds trust in elections because it ensures fairness: the first person to arrive votes first, "
      "and no one can skip the line.")
