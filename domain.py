def domainType(domains):
    answer = []
    for i,v in enumerate(domains):
        val = list(v.split('.'))[-1]
        print(val)
        if val == 'org':
            answer.append("organization")
        elif val == 'info':
            answer.append("information")
        elif val == 'net':
            answer.append("network")
        else:
            answer.append("commercial")



domains = ["en.wiki.org", "codesignal.com", "happy.net", "code.info"]
domainType(domains)