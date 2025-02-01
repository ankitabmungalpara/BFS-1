"""

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
Space Complexity: O(V + E), due to adjacency list storage and in-degree dictionary.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# used Kahn's Algorithm (Topological Sorting) with an adjacency list and in-degree tracking.  
# enqueued courses with zero in-degree and iteratively process them, reducing the in-degree of dependent courses.  
# If processed all courses, it means we can finish them; otherwise, a cycle exists.

from queue import Queue


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_lst = {i: [] for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}

        for course, pre in prerequisites:
            adj_lst[pre].append(course)
            in_degree[course] += 1

        q = Queue()
        for k, v in in_degree.items():
            if v == 0:
                q.put(k)

        count = 0
        while not q.empty():
            ele = q.get()
            count += 1
            for v in adj_lst[ele]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.put(v)

        return count == numCourses

