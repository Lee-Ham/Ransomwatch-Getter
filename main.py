import requests
import jmespath
import json
import datetime
import os

def main():
    try:
        f = open(os.path.dirname(__file__)+"\\lastrun.date","r")
        lastRun = f.readline()
        f.close()

    except:
        f = open(os.path.dirname(__file__)+"\\lastrun.date","w")
        lastRun = "1970-01-01 00:00:00.000000"
        f.close()

    date = datetime.datetime.now()
    print(date)
    r = requests.get("https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json").text

    path = jmespath.search("[?discovered > '"+lastRun+"']",json.loads(r))
    try:
        f = open(os.path.dirname(__file__)+"\\ransomwatch.txt","a",encoding="utf-8")
        for item in path:
            print(item)
            f.write(str(item)+"\n")

        f = open(os.path.dirname(__file__)+"\lastrun.date","w")
        f.write(str(date))
        f.close()

    except Exception as error:
        print(error)    


if __name__ == "__main__":
    main()