import json

# retrieve dists at getIndependentProofOfAgent through data cube
push_dist = [0,0,0,0,0,0,0,0,0,0.1,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.0,0.0,0,0,0,0,0]
star_dist = [0,0,0,0,0,0,0,0,0,0.2,0.1,0.1,0.2,0.1,0.1,0.1,0.1,0.0,0.0,0,0,0,0,0]

class AnalysisLib():

    def __init__(self):
        self.attributes = self.loadAttributes('../config/config.json')

    # data structure looks like
    # {obj_id1: {"push": [], "pull": []}, obj_id2: {"push": [0.1, 0.2, 0.7], "pull": [0.2, 0.3, 0.9]}}
    # Note: put assertion because probability should be between 0 and 1
    def getIndendentProbOfAgent(self, agentId):
        # here is where you can access the data cube to return specific probabilities

        # define temp independent probabilities
        # ind_prob = {id: {0: {"push": push_dist, "star": star_dist}, 1: {"push": push_dist, "star": star_dist}} for id in self.agent_id}
        ind_prob = {0: {"push": push_dist, "star": star_dist}, 1: {"push": push_dist, "star": star_dist}}

        # return ind_prob[agentId]
        return ind_prob
        
    
    def getDependentProbOfAgent(self, agentID):
        pass
    
    def getAttributes(self): # return config data
        return self.attributes

    def getIds(self, target_type): # return list of ids of target type from config data
        id_list = []
        for attributes in self.attributes[target_type]["attributes"]:
            id_list.append(attributes["id"])
        return id_list

    def loadAttributes(self, fname):
        with open(fname) as data_file:
            data = json.load(data_file)
        return data