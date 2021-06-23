# Race Conditions

When several processes access and control the same resource at the same time, a race condition occurs, and the result of the execution is determined by the order in which the access occurs. By "running the race," changing the resource, and altering the usual execution flow, the attacker may take advantage of a race situation.

## CHESS by Microsoft Research

CHESS is a tool for systematically testing multithreaded code. Given a concurrent test, CHESS systematically drives the test along all possible thread interleavings. It uses model-checking techniques to explore effectively the enormously large state space of interleavings and provides quantified coverage guarantees. Assertions, deadlocks, livelocks, and data races can all be detected using CHESS. When CHESS discovers a mistake, it may recreate the thread interleaving that revealed it. Microsoft Research created CHESS, a research tool. For more details, go to http://research.microsoft.com/projects/CHESS/.

This tool is only available to Windows equal or higher than 7 and can be downloaded from: https://www.microsoft.com/en-us/download/details.aspx?id=52619&from=https%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2Fb23f8dc3-bb73-498f-bd85-1de121672e69%2F