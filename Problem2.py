#Course Schedule (https://leetcode.com/problems/course-schedule/)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        indegrees = [0] * numCourses #indegrees list

        #dep_course means dependat course [1,0] 1 is dependant on 0 (ind_course)
        #and also it can be called incoming arrow and outgoing arrow from 0
        '''preMap = {i: [] for i in range(numCourses)}

            # map each course to : prereq list
            for crs, pre in prerequisites:
                preMap[crs].append(pre)'''
        for dep_course, ind_course in prerequisites:
            indegrees[dep_course] += 1
            
            if ind_course not in adjList:
                adjList[ind_course] = []
            adjList[ind_course].append(dep_course)

        #bfs
        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)
        
        completedCourse = 0
        while q:
            current = q.popleft()
            completedCourse += 1
            
            if current in adjList:
                for neighbor in adjList[current]:
                    indegrees[neighbor] -= 1

                    if indegrees[neighbor] == 0:
                        q.append(neighbor)

        if completedCourse == numCourses:
            return True

        