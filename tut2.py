from collections import deque

def lru_page_faults(reference_string, frame_count):
    frames = []
    page_faults = 0
    for page in reference_string:
        if page not in frames:
            if len(frames) >= frame_count:
                frames.pop(0)
            frames.append(page)
            page_faults += 1
        else:
            frames.remove(page)
            frames.append(page)
    return page_faults

def fifo_page_faults(reference_string, frame_count):
    frames = deque(maxlen=frame_count)
    page_faults = 0
    for page in reference_string:
        if page not in frames:
            if len(frames) == frame_count:
                frames.popleft()
            frames.append(page)
            page_faults += 1
    return page_faults

def optimal_page_faults(reference_string, frame_count):
    frames = []
    page_faults = 0
    for i in range(len(reference_string)):
        page = reference_string[i]
        if page not in frames:
            if len(frames) >= frame_count:
                future_use = []
                for f in frames:
                    if f in reference_string[i+1:]:
                        future_use.append(reference_string[i+1:].index(f))
                    else:
                        future_use.append(float('inf'))
                frames.pop(future_use.index(max(future_use)))
            frames.append(page)
            page_faults += 1
    return page_faults

# Reference string
reference_string = [1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6]

# Number of frames
frames_3 = 3
frames_5 = 5

# Calculate page faults
lru_faults_3 = lru_page_faults(reference_string, frames_3)
fifo_faults_3 = fifo_page_faults(reference_string, frames_3)
optimal_faults_3 = optimal_page_faults(reference_string, frames_3)

lru_faults_5 = lru_page_faults(reference_string, frames_5)
fifo_faults_5 = fifo_page_faults(reference_string, frames_5)
optimal_faults_5 = optimal_page_faults(reference_string, frames_5)

# Print results
print(f"LRU with 3 frames: {lru_faults_3} page faults")
print(f"FIFO with 3 frames: {fifo_faults_3} page faults")
print(f"Optimal with 3 frames: {optimal_faults_3} page faults")

print(f"LRU with 5 frames: {lru_faults_5} page faults")
print(f"FIFO with 5 frames: {fifo_faults_5} page faults")
print(f"Optimal with 5 frames: {optimal_faults_5} page faults")
