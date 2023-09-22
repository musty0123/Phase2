

def extract_tasks(task):
    if task == '':
        raise Exception('No task was found')
    elif ' #TODO ' in task: 
        text = task.replace(' #TODO', '')
        
        return 'task: ' + text
    elif '#TODO' in task: 
        if task == '#TODO':
            return 'YOU HAVE TO DO SOMETHING'
        text = task.replace('#TODO', '')
        new_text = text.strip()
        return 'task: ' + new_text
    
    return 'No #TODO found'