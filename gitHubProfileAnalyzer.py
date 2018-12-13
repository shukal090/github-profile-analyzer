import requests
import json
import gitHubProfileAnalyzerGui as gui

class gitHubProfileAnalyzer:
    ''' The GitHub Profile Analyzer '''

    URL = "https://api.github.com/users/"   # GitHub API
    repoURL = "https://api.github.com/repos/"
    
    def __init__(self):
        self.user_name = ""
        self.user_url = ""
        self.languages = {}
    
    def get_status(self):
        self.user_url = self.URL + self.user_name
        r = requests.get(self.user_url)
        return r.status_code, r.reason

    def get_info(self, url):
        r = requests.get(url)
        st = r.content.decode("utf-8")  # convert byte to str
        d = json.loads(st)              # convert str to dict
        return d

    def user_info(self, Obj):
        Obj.destroy_children(Obj.tab_basic)
        info = self.get_info(self.user_url)
        login = str(info['login'])
        iid = str(info['id'])
        name = str(info['name'])
        url = str(info['html_url'])
        company = str(info['company'])
        repos = str(info['public_repos'])
        followers = str(info['followers'])
        following = str(info['following'])
        date = str(info['created_at'])[:10]
        avt = requests.get(str(info['avatar_url']))
        with open("avatar.jpg", "wb") as handler:
            handler.write(avt.content)
        Obj.user_info(login=login, iid=iid, name=name, url=url, company=company, repos=repos, followers=followers, following=following, date=date, languages=self.languages)

    def user_followers(self, Obj):
        Obj.destroy_children(Obj.tab_followers)
        followers_url = self.user_url + "/followers"
        info = self.get_info(followers_url)
        count = 0
        for follower in info:
            name = str(follower['login'])
            url = str(follower['html_url'])
            Obj.user_followers(name=name, url=url, align=count)
            count += 1

    def user_following(self, Obj):
        Obj.destroy_children(Obj.tab_following)
        following_url = self.user_url + "/following"
        info = self.get_info(following_url)
        count = 0
        for following in info:
            name =str(following['login'])
            url = str(following['html_url'])
            Obj.user_following(name=name, url=url, align=count)
            count += 1

    def user_starred(self, Obj):
        Obj.destroy_children(Obj.tab_starred)
        starred_url = self.user_url + "/starred"
        info = self.get_info(starred_url)
        count = 0
        for starred in info:
            name = str(starred['name'])
            owner = (starred['owner']['login'])
            url = (starred['html_url'])
            Obj.user_starred(name=name, owner=owner,url=url, align=count)
            count += 1
    
    def user_repos(self, Obj):
        Obj.destroy_children(Obj.tab_repos)
        repos_url = self.user_url + "/repos"
        info = self.get_info(repos_url)
        count = 0
        for repo in info:
            name = str(repo['name'])
            url = str(repo['html_url'])
            lang = str(repo['language'])
            if lang is not None:
                if lang in self.languages.keys():
                    self.languages[lang] += 1
                else:
                    self.languages[lang] = 1
            stargazers = str(repo['stargazers_count'])
            forks = str(repo['forks'])
            Obj.user_repos(name=name, url=url, lang=lang, stargazers=stargazers, forks=forks, align=count)
            count += 1
    

    def main(self, Obj):
        try:
            status, req_reason = self.get_status()
            if status == requests.codes.ok:
                self.user_info(Obj=Obj)
                self.user_followers(Obj=Obj)
                self.user_following(Obj=Obj)
                self.user_starred(Obj=Obj)
                self.user_repos(Obj=Obj)
            else:
                err = "Error " + str(status) + ": " + str(req_reason)
                Obj.error_msg(msg=err)
        except:
            err = "Error 403: Forbidden"
            Obj.error_msg(msg=err)

def analyze():
    myObj = gitHubProfileAnalyzer()
    myGui = gui.gitHubProfileAnalyzerGui(Obj=myObj)

analyze()