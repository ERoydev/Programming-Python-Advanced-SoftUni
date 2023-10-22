from collections import deque


eggs = deque([int(x) for x in input().split(", ")])
papers = [int(x) for x in input().split(", ")]

while eggs and papers:
    curr_egg = eggs.popleft()
    curr_paper = papers.pop()

