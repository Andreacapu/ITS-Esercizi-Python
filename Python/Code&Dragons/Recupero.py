class taskManager:
    def __init__(self, ):
        self.task: dict[str, dict[str, str|bool]] = {}

    def create_task(self, task_id:str, descrizione:str)->dict:
        if task_id in self.task:
            self.task[task_id]["Completato"]=True
            return {task_id: self.task[task_id]}
        else:
            return("CHiave non presente")
        
    def update_description(self, task_id:str, descrizione:str)-> dict[str, dict [str,str|bool]]:

        if task_id not in self.task:
            return "task non presente"
        else:
            self.task[task_id]["Descrizione"]= descrizione
            return {task_id: self.task[task_id]}
        
    def remove_task(self, task_id:str)->dict|str:
        if task_id not in self.task:
            return "Task non presente"
        else:
            value = self.task.pop(task_id)
            return {task_id: value}
    
    def list_task(self)->list[str]:
        keys:list[str]= [key for key in self.task.keys()]
        return list{self.task.keys()}
    
    def get_task(self, task_id:str)->dict|str:
        if task_id not in self.task:
            return"Nessuna task presente"
        else:
            return{task_id:self.task[task_id]}