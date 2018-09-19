""" Program that takes a text file (mbox.txt) and parses the emails and hosts contained.
It will simply read any lines beginning with 'FROM: ' or 'TO: ' and parse the user and host name. It then counts
 and displays it's count!"""

#Set up variables needed. I think it would be cleaner to have these contained in the functions.
fromUserDict = dict()
hostDict = dict()
toDict = dict()
toHostDict = dict()
toHostList = []
toList = []
nameList = []
hostList = []

# A very simple loop. The function opens the text file, and for each line that begins with "FROM: " it stores it in a
# variable and parses it by stripping the whitespace and the "FROM: " text. It then splits the user from the host
# name using the .split function. We then simply append the user and host name to two seperate lists.
def processFroms():
    count = 0
    openText = open('mbox.txt', 'r')
    for user in openText:
        if user.startswith("From: "):
            user = user.rstrip()
            user = user.lstrip("From: ")
            user = user.split("@")
            currentName = user[0]
            nameList.append(currentName)
            count += 1
# Here, we have the user name which we set a default value for, we then take that list, count them, and format them in
# a human readable way!
    for name in nameList:
        fromUserDict.setdefault(name, 0)
        fromUserDict[name] += 1
    for name, count in fromUserDict.items():
        print("{}, {}".format(name, count))


# Each of these functions does the same exact thing, just changing where it's looking.
def processHosts():
    count = 0
    openText = open('mbox.txt', 'r')
    for host in openText:
        if host.startswith("From: "):
            host = host.rstrip()
            host = host.lstrip("From: ")
            host = host.split("@")
            currentHost = host[1]
            hostList.append(currentHost)
            count += 1

    for host in hostList:
        hostDict.setdefault(host, 0)
        hostDict[host] += 1
    for host, count in hostDict.items():
        print("{}, {}".format(host, count))

def processToUsers():
    count = 0
    openText = open('mbox.txt', 'r')
    for to in openText:
        if to.startswith("To: "):
            to = to.rstrip()
            to = to.lstrip("To: ")
            to = to.split("@")
            currentTo = to[0]
            toList.append(currentTo)
            count += 1

    for to in toList:
        toDict.setdefault(to, 0)
        toDict[to] += 1
    for to, count in toDict.items():
        print("{}, {}".format(to, count))

def processToUserHost():
    count = 0
    openText = open('mbox.txt', 'r')
    for toHost in openText:
        if toHost.startswith("To: "):
            toHost = toHost.rstrip()
            toHost = toHost.lstrip("To: ")
            toHost = toHost.split("@")
            currentToHost = toHost[1]
            toHostList.append(currentToHost)
            count += 1

    for toHost in toHostList:
        toHostDict.setdefault(toHost, 0)
        toHostDict[toHost] += 1
    for toHost, count in toHostDict.items():
        print("{}, {}".format(toHost, count))


# Simply starts each function. I could probably make this a little cleaner and have the print statement within
# the function, but I find that it helps differentiate what does what.
print("--- FROM USERS ---")
processFroms()

print("--- FROM HOST ---")
processHosts()

print("--- TO USER ---")
processToUsers()

print("--- TO HOST ---")
processToUserHost()

