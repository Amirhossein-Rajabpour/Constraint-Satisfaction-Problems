# TODO take a dictionary as input
def MRV(domains_dict):
    # TODO return variable with the least domain
    domains_dict = dict(sorted(domains_dict.items(), key=lambda x:len(x[1])))
    return list(domains_dict)[0]
