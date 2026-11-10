class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # 0 = unvisited, 1 = visiting, 2 = fully processed
        state = [0] * numCourses
        
        # 2. Define the DFS helper function
        def dfs(course):  # Fixed parameter name from 'courses' to 'course'
            if state[course] == 1:   # Found a cycle!
                return False
            if state[course] == 2:   # Already verified safe
                return True
                
            state[course] = 1        # Mark as 'visiting'
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
                    
            state[course] = 2        # Mark as 'fully processed'
            return True
            
        # 3. Check every course
        for course in range(numCourses):
            if not dfs(course):
                return False
                
        return True
