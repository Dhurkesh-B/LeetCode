
import heapq

def mostBooked(n, meetings):
    # Step 1: Sort the meetings by start time
    meetings.sort()
    
    # Step 2: Initialize
    room_count = [0] * n                  # Track how many meetings each room handled
    free_rooms = list(range(n))          # Initially all rooms are free
    heapq.heapify(free_rooms)            # Min-heap for available room numbers
    occupied_rooms = []                  # Min-heap of (end_time, room_number)
    
    for start, end in meetings:
        # Step 3: Free rooms whose meeting ended before the current meeting start
        while occupied_rooms and occupied_rooms[0][0] <= start:
            freed_end_time, freed_room = heapq.heappop(occupied_rooms)
            heapq.heappush(free_rooms, freed_room)
        
        duration = end - start
        
        if free_rooms:
            # Step 4A: Use the smallest available room number
            room = heapq.heappop(free_rooms)
            heapq.heappush(occupied_rooms, (end, room))
        else:
            # Step 4B: Delay the meeting until the earliest ending room is free
            earliest_end_time, room = heapq.heappop(occupied_rooms)
            new_end_time = earliest_end_time + duration
            heapq.heappush(occupied_rooms, (new_end_time, room))
        
        # Step 5: Track meeting count
        room_count[room] += 1

    # Step 6: Return the room with the most meetings (lowest index on tie)
    max_meetings = max(room_count)
    for i in range(n):
        if room_count[i] == max_meetings:
            return i
