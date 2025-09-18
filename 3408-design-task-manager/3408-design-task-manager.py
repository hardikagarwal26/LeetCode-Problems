class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.sl = SortedList()
        self.taskinfo = {}

        for u , t , p in tasks:
            self.sl.add((p,t,u))
            self.taskinfo[t] = (p,u)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.sl.add((priority,taskId,userId))
        self.taskinfo[taskId] = (priority,userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        oldp , u = self.taskinfo[taskId]
        self.sl.discard((oldp , taskId , u))
        self.sl.add((newPriority , taskId , u))
        self.taskinfo[taskId] = (newPriority , u)
        

    def rmv(self, taskId: int) -> None:
        oldp , u = self.taskinfo[taskId]
        self.sl.discard((oldp , taskId , u))
        del self.taskinfo[taskId]
        

    def execTop(self) -> int:
        if not self.sl: return -1
        old_p , old_t , u = self.sl[-1]
        self.sl.pop(-1)
        return u
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()