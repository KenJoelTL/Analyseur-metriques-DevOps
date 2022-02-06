from re import match
import requests
from datetime import datetime
import config

'''--------------------------------------------------------------------------------------main service calls begin'''
def getSingleTaskLeadtime(task_number):
    r =requests.get(url=config.repo_base_url+"issues/"+str(task_number),headers=config.headers)
    if r.status_code == 200:
        task = r.json();
       # print(task["title"], task["id"],)
        opendate=datetime.strptime(task["created_at"],'%Y-%m-%dT%H:%M:%SZ')
        if task["closed_at"] == None:
            leadTime= (datetime.now()-opendate).days          
        else:
            closedDate = datetime.strptime(task["closed_at"],'%Y-%m-%dT%H:%M:%SZ')
            leadTime = (closedDate-opendate).days
        return str(leadTime)+" days"
    elif r.status_code == 404:
        print(r)
        return "task not found"
    else:
        print(r)
        return "an error occured"


        

def getMultiTaskleadtime(startDate,endDate):
    startDate=datetime.strptime(startDate,'%Y-%m-%d')
    endDate = datetime.strptime(endDate,'%Y-%m-%d')
    response=[]
    params = {"state":"closed"}
    r =requests.get(url=config.repo_base_url+"issues",params=params,headers=config.headers)
    
    if r.status_code == 200:
        issues = r.json()
        for issue in issues:
            
            if issue["closed_at"] != None:
                closedDate = datetime.strptime(issue["closed_at"],'%Y-%m-%dT%H:%M:%SZ')
                if((closedDate>=startDate) and (closedDate<=endDate)):
                    opendate=datetime.strptime(issue["created_at"],'%Y-%m-%dT%H:%M:%SZ')
                    leadtime = (closedDate-opendate).days
                    response.append("taskNumber: "+str(issue["number"])+" "+"taskTitle: "+issue["title"]+" "+"taskLeadTime: "+str(leadtime)+" days")      
                    
    elif r.status_code == 404:
        print( "no tasks found on this project")
    else:
        print( "an error has occured")
    
    return response

def getActiveTasks(column_id):
    card_list=[]
    r =requests.get(url=config.baseUrl+"projects/columns/"+str(column_id)+"/cards",headers=config.headers)
    if r.status_code == 200:
        data = r.json();
        for cards in data:
            r =requests.get(url=cards["content_url"],headers=config.headers)
            if r.status_code == 200:
                card = r.json()
                card_list.append(card)
            
        return card_list
    else:
        return None
    

def getCompletedTasks(startDate,endDate):
    startDate=datetime.strptime(startDate,'%Y-%m-%d')
    endDate = datetime.strptime(endDate,'%Y-%m-%d')
    response=[]
    params = {"state":"closed"}
    r =requests.get(url=config.repo_base_url+"issues",params=params,headers=config.headers)
    if r.status_code == 200:
        issues = r.json()
        for issue in issues:
            if issue["closed_at"] != None:
                closedDate = datetime.strptime(issue["closed_at"],'%Y-%m-%dT%H:%M:%SZ')
                if((closedDate>=startDate) and (closedDate<=endDate)):
                    response.append(issue["title"])      
        
    elif r.status_code == 404:
        print( "no tasks found on this project")
    else:
        print( "an error has occured")
    return response
'''--------------------------------------------------------------------------------------main service calls end'''


def getKanBanTaskList():
    r =requests.get(url=config.baseUrl+"projects/"+str(config.kanban_id)+"/columns",headers=config.headers)
    if r.status_code == 200:
        data = r.json()
        tasks=[]
        #print("cards")
        for columns in data:
            r=requests.get(url=columns["url"]+"/cards",headers=config.headers)
            if r.status_code == 200:
                res = r.json()
                for cards in res:
                    r=requests.get(url=cards["content_url"],headers=config.headers)
                    if r.status_code == 200:
                        card=r.json()
                        tasks.append(card)
                        #print(card["title"],card["id"])
    return tasks

def getKanBanColumnList():
    r =requests.get(url=config.baseUrl+"projects/"+str(config.project_id)+"/columns",headers=config.headers)
    columns=[]
    if r.status_code == 200:
        columns = r.json()
    return columns   
