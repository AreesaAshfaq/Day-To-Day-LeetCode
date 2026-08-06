# Time Complexity: O(n log n)
# - Building the heap takes O(n log n) using n heappush operations.
# - Each smash operation performs heap pop/push operations, each taking O(log n).
# - In the worst case, we perform these operations for n stones.

# Space Complexity: O(n)
# - The heap stores all stones, requiring O(n) extra space.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Create Max Heap using negative values
        heap = []
                
        # Smash stones until at most one remains
        for stone in stones: 
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:

            # Get two largest stones            
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            # If they are different, put the difference back
            if x != y:
                heapq.heappush(heap, -(y - x))

        # Return remaining stone        
        if heap:
            return -heap[0]

        return 0

