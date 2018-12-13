import requests
import json

class gitHubProfileAnalyzer:
    ''' The GitHub Profile Analyzer '''

    URL = "https://api.github.com/users/"   
    repoURL = "https://api.github.com/repos/"
    
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_url = self.URL + user_name
        self.languages = {}
        self.commits = 0
    
    def get_status(self):
        r = requests.get(self.user_url)
        return r.status_code, r.reason

    def get_info(self, url):
        r = requests.get(url)
        st = r.content.decode("utf-8")  
        d = json.loads(st)              
        return d

    def user_info(self):
        info = self.get_info(self.user_url)
        print("User Info:")
        print("Username\t: " + str(info['login']))
        print("ID\t\t: " + str(info['id']))
        print(("Name\t\t: " + str(info['name'])))
        print("GitHub URL\t: " + str(info['html_url']))
        print("Comapny\t\t: " + str(info['company']))
        print("Public Repos\t: "+ str(info['public_repos']))
        print("Followers\t: "+ str(info['followers']))
        print("Followings\t: "+ str(info['following']))
        print(str(info['name']) + " is contributing since " + info['created_at'])

    def user_followers(self):
        followers_url = self.user_url + "/followers"
        info = self.get_info(followers_url)
        print("\n\nFollowers:\nName\t\tGitHub URL")
        for follower in info:
            print(follower['login'] + "\t" + follower['html_url'])

    def user_folllowing(self):
        following_url = self.user_url + "/following"
        info = self.get_info(following_url)
        print("\n\nFolLowings:\nName\t\tGitHub URL")
        for following in info:
            print(following['login'] + "\t" + following['html_url'])

    def user_starred(self):
        starred_url = self.user_url + "/starred"
        info = self.get_info(starred_url)
        print("\n\nStarred Repositories:")
        for starred in info:
            print(starred['name'])
            print("\t" + "Owner\t: " + starred['owner']['login'])
            print("\t " + "URL\t:" + starred['html_url'] + "\n")
    
    def user_repos(self):
        repos_url = self.user_url + "/repos"
        info = self.get_info(repos_url)
        print("\n\nRepositories:")
        for repo in info:
            print(repo['name'])
            print("\tURL : " + repo['html_url'])
            lang = repo['language']
            print("\tLanguage : " + str(lang))
            if lang is not None:
                if lang in self.languages.keys():
                    self.languages[lang] += 1
                else:
                    self.languages[lang] = 1
            pr = self.get_info(self.repoURL + self.user_name + "/" + repo['name'] + "/pulls")
            print("\tPull Requests : " + str(len(pr)))
            issues = self.get_info(self.repoURL + self.user_name + "/" + repo['name'] + "/issues")
            print("\tIssues : " + str(len(issues)))
            print("\tStargazers : " + str(repo['stargazers_count']))
            print("\tForks : " + str(repo['forks']) + "\n")
            comm = self.get_info(self.repoURL + self.user_name + "/" + repo['name'] + "/commits")
            self.commits += len(comm)
    
    def user_languages(self):
        print("Languages Used:")
        for lang in self.languages:
            print(lang + " : " + str(self.languages[lang]))
        print("\nTotal Commits: " + str(self.commits))

def analyze():
    username = input("Enter the GitHub username > ")
    myObj = gitHubProfileAnalyzer(username)
    status, req_reason = myObj.get_status()
    if status == requests.codes.ok:
        myObj.user_info()
        myObj.user_followers()
        myObj.user_folllowing()
        myObj.user_starred()
        myObj.user_repos()
        myObj.user_languages()
    else:
        print("Error " + str(status) + ": " + str(req_reason))
