from re import match
import requests
from datetime import datetime
import config

#repo_base_url = 'https://api.github.com/repos/KenJoelTL/LOG680-tp01-eq08/'
#repo_base_url = 'https://api.github.com/repos/microsoft/PowerToys/'
#headers={"authorization": "token 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"}


def getPullResquestList(state):
    params = {"state":state}
    r =requests.get(url=config.repo_base_url+"pulls",params=params,headers=config.headers)
    pullRequestList=[]
    if r.status_code == 200:
        pullRequestList = r.json()
    return pullRequestList


def averageLeadTimeClosedPR():
    pullRequestList = getPullResquestList("closed")
    avgLeadTime = 0
    if len(pullRequestList)>0:
        leadtime = 0
        for pr in pullRequestList:
            opendate=datetime.strptime(pr["created_at"],'%Y-%m-%dT%H:%M:%SZ')
            closedDate = datetime.strptime(pr["closed_at"],'%Y-%m-%dT%H:%M:%SZ')
            prleadtime = (closedDate-opendate).days
            if prleadtime > 0:
                leadtime =leadtime+prleadtime
        avgLeadTime = leadtime/len(pullRequestList)
    return avgLeadTime

def averageMergeTimeClosedPR():
    pullRequestList = getPullResquestList("closed")
    avgMergetime = 0
    counter =0
    if len(pullRequestList)>0:
        mergerdtime = 0
        for pr in pullRequestList:
            if pr["merged_at"] != None:
                counter += 1
                opendate=datetime.strptime(pr["created_at"],'%Y-%m-%dT%H:%M:%SZ')
                mergeDate = datetime.strptime(pr["merged_at"],'%Y-%m-%dT%H:%M:%SZ')
                prmergetime = (mergeDate-opendate).days
                if prmergetime > 0:
                    mergerdtime =mergerdtime+prmergetime
        avgMergetime = mergerdtime/counter
    return avgMergetime


def getSinglePullRequestLeadtime(pull_number):
    r =requests.get(url=config.repo_base_url+"pulls/"+str(pull_number),headers=config.headers)
    if r.status_code == 200:
        pr = r.json();
        opendate=datetime.strptime(pr["created_at"],'%Y-%m-%dT%H:%M:%SZ')
        if pr["closed_at"] == None:
            leadTime= (datetime.now()-opendate).days          
        else:
            closedDate = datetime.strptime(pr["closed_at"],'%Y-%m-%dT%H:%M:%SZ')
            leadTime = (closedDate-opendate).days
        return str(leadTime)+" days"
    elif r.status_code == 404:
        print(r)
        return "pull request not found"
    else:
        print(r)
        return "an error occured" 



def prMergeRate():
    closedPR = getPullResquestList("closed")
    allPR = getPullResquestList("all")
    rate = 0
    if len(closedPR)>0:
        counter=0
        for pr in closedPR:
            if pr["merged_at"]!= None:
                counter+=1
        rate = (counter/len(allPR)) * 100

    return rate
        

def prRejectionRate():
    closedPR = getPullResquestList("closed")
    allPR = getPullResquestList("all")
    rate = 0
    if len(closedPR)>0:
        counter=0
        for pr in closedPR:
            if pr["merged_at"] == None:
                counter+=1
        rate = (counter/len(allPR)) * 100

    return rate
    
