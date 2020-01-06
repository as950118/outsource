""" Data Structures and Algorithms for CL III, WS 2019-2020, Assignment 3
   
    WordNet API

    <Please insert your data and the honor code here.>
"""
from collections import defaultdict
class WordNet:
    """API for querying WordNet information"""
    def __init__(self, synsets_file, hypernyms_file):
        self.synsets = defaultdict(lambda:None)
        self.hypernyms = defaultdict(lambda:None)
        self.edge = defaultdict(lambda:list()) # for find path and common path
        # read synsets
        f = open(synsets_file, 'r')
        line = f.readline()
        while line:
            splited = list(map(str, line[:-1].split(',')))
            num = splited[0]
            name = list(map(str, splited[1].split()))
            gloss = splited[2]
            if len(splited) > 3:
                for i in range(3, len(splited)):
                    gloss += splited[i]
            self.synsets[int(num)] = Synset(name, num, gloss)
            line = f.readline()
        f.close()
        # read hypernyms
        f = open(hypernyms_file, 'r')
        line = f.readline()
        while line:
            splited = list(map(str, line.split(',')))
            self.hypernyms[int(splited[0])] = Relation(splited[0], splited[1:])
            for edge in splited[1:]:
                self.edge[int(splited[0])].append(int(edge))
                self.edge[int(edge)].append(int(splited[0]))
            line = f.readline()
        f.close()

    def __iter__(self):
        for syn in self.synsets:
            if self.synsets[syn] != None:
                yield self.synsets[syn]
        return

    def __len__(self):
        return len([synset for synset in self.synsets if self.synsets[synset] != None])

    def get_synsets(self, noun):
        synsets = list(self.synsets[synset] for synset in self.synsets if self.synsets[synset] != None and noun in self.synsets[synset].name)
        return synsets

    def bfs(self, synset):
        visited, queue = set(), [synset]
        paths = defaultdict(lambda:None)
        path = []
        while queue:
            vertex = queue.pop(0)
            if vertex in visited:
                if paths[vertex] != None:
                    if paths[vertex][1] < len(path)-1:
                        paths[vertex] = (self.synsets[vertex], len(path)-1)
            else:
                visited.add(vertex)
                path.append(vertex)
                paths[vertex] = (self.synsets[vertex], len(path)-1)
                if self.hypernyms[int(vertex.pos)] != None:
                    for par in self.hypernyms[int(vertex.pos)].hyper:
                        queue.append(self.synsets[int(par)])
        if paths[vertex] != None:
            if paths[vertex][1] > len(path) - 1:
                paths[vertex] = (self.synsets[vertex], len(path) - 1)
        else:
            paths[vertex] = (self.synsets[vertex], len(path) - 1)
        return paths

    def paths_to_root(self, synset):
        # using dfs
        visited, queue = set(), [synset]
        paths = []
        path = []
        while queue:
            vertex = queue.pop()
            visited.add(vertex)
            path.append(vertex)
            if vertex != None and self.hypernyms[int(vertex.pos)] != None:
                for par in self.hypernyms[int(vertex.pos)].hyper:
                    queue.append(self.synsets[int(par)])
            else:
                paths.append(path[1:])
                path = []
        return paths

    def lowest_common_hypernyms(self, synset1, synset2):
        # find each synset paths to root
        # and set lowest depth length
        # and find common path in paths
        paths1 = self.paths_to_root(synset1)
        paths2 = self.paths_to_root(synset2)
        set_paths1 = set()
        set_paths2 = set()
        for path1 in paths1:
            for syn in path1:
                set_paths1.add(int(syn.pos))
        for path2 in paths2:
            for syn in path2:
                set_paths2.add(int(syn.pos))
        common_paths = list(set_paths1 & set_paths2) # find common path
        lowest_depth = 0
        for common_path in common_paths:
            common_path = self.synsets[common_path]
            for path1 in paths1:
                try:
                    path1_index = path1.index(common_path)
                    for path2 in paths2:
                        try:
                            path2_index = path2.index(common_path)
                            lowest_depth = max(lowest_depth, min(len(path1) - path1_index, len(path2) - path2_index))
                        except: # if not commonpath in path2
                            pass
                except: # if not commonpath in path1
                    pass
        ret_set = set()
        for common_path in common_paths:
            common_path = self.synsets[common_path]
            for path1 in paths1:
                try:
                    path1_index = path1.index(common_path)
                    for path2 in paths2:
                        try:
                            path2_index = path2.index(common_path)
                            # if, sum of path1 and path2 index == lowest,
                            # it is lowest hypernym
                            if min(len(path1) - path1_index, len(path2) - path2_index) == lowest_depth:
                                ret_set.add(common_path)
                        except: # if not commonpath in path2
                            pass
                except: # if not commonpath in path1
                    pass
        return ret_set

    def distance(self, synset1, synset2):
        # using bfs
        bfs1 = self.bfs(synset1)
        bfs2 = self.bfs(synset2)
        for b2 in bfs2:
            if b2 in bfs1:
                return bfs1[b2][1] + bfs2[b2][1] -1
        '''
        queue = [(int(synset1.pos), [int(synset1.pos)])]
        ret = []
        while queue:
            n, path = queue.pop(0)
            if n == int(synset2.pos):
                ret.append(path)
                break
            else:
                for i in self.edge[n]:
                    queue.append((i, path+[i]))
        return len(ret[0])
        '''

    def lch_similarity(self, synset1, synset2):
        # find distance synset1 to synset2
        # and find maximum depth in synset1 and synset2
        # and return -log((distance) / (2*depth))
        from math import log
        distance = self.distance(synset1, synset2)
        max_depth = 0
        for syn in self.synsets:
            max_depth = max(max_depth, max([len(path) for path in self.paths_to_root(self.synsets[syn])]))
        if distance is None or distance<0 or max_depth == 0:# if hierachy is 0
            return None
        return -log((distance+1) / (2.0*max_depth))

    def noun_lowest_common_hypernyms(self, noun1, noun2):
        # find each synset using noun
        # and find each synset paths to root
        # and find lowest path length
        # and find common path in paths
        synsets1 = self.get_synsets(noun1)
        synsets2 = self.get_synsets(noun2)
        lowest_depth = 10**0
        ret_set = set()
        # find lowest path length
        for synset1 in synsets1:
            paths1 = self.paths_to_root(synset1)
            set_paths1 = set()
            for path1 in paths1:
                for syn in path1:
                    set_paths1.add(int(syn.pos))
            for synset2 in synsets2:
                paths2 = self.paths_to_root(synset2)
                set_paths2 = set()
                for path2 in paths2:
                    for syn in path2:
                        set_paths2.add(int(syn.pos))
                common_paths = list(set_paths1 & set_paths2)
                for common_path in common_paths:
                    common_path = self.synsets[common_path]
                    for path1 in paths1:
                        try:
                            path1_index = path1.index(common_path)
                            for path2 in paths2:
                                try:
                                    path2_index = path2.index(common_path)
                                    lowest_depth = max(lowest_depth, min(len(path1) - path1_index, len(path2) - path2_index))
                                except:
                                    pass
                        except:
                            pass
        # find common path in paths
        for synset1 in synsets1:
            paths1 = self.paths_to_root(synset1)
            set_paths1 = set()
            for path1 in paths1:
                for syn in path1:
                    set_paths1.add(int(syn.pos))
            for synset2 in synsets2:
                paths2 = self.paths_to_root(synset2)
                set_paths2 = set()
                for path2 in paths2:
                    for syn in path2:
                        set_paths2.add(int(syn.pos))
                common_paths = list(set_paths1 & set_paths2)
                for common_path in common_paths:
                    common_path = self.synsets[common_path]
                    for path1 in paths1:
                        try:
                            path1_index = path1.index(common_path)
                            for path2 in paths2:
                                try:
                                    path2_index = path2.index(common_path)
                                    if min(len(path1) - path1_index, len(path2) - path2_index) == lowest_depth:
                                        ret_set.add(common_path)
                                except:
                                    pass
                        except:
                            pass
        return ret_set

# class for synset, relation, path
class Synset:
    def __init__(self, name, pos, gloss):
        self.name = name
        self.pos = pos
        self.gloss = gloss
        self.index = int(pos)
    def __iter__(self):
        for lemma in self.name:
            yield lemma
        return

class Relation:
    def __init__(self, hypo, hyper):
        self.hypo = hypo
        self.hyper = hyper

class Path:
    def __init__(self, synset):
        self.edges = self.hypernyms[synset.pos].hyper
        self.vertices = len(self.edges)

if __name__ == "__main__":
    from nltk.corpus import wordnet

    print(max(max(len(hyp_path) for hyp_path in ss.hypernym_paths()) for ss in wordnet.all_synsets()))
    dog = wordnet.synset('dog.n.01')
    print(dog.hypernym_paths())
    print(dog.max_depth())
    print([len(path) for path in dog.hypernym_paths()])
    horse = wordnet.synset('cat.n.01')
    print(horse.hypernym_paths())
    print(horse.max_depth())
    print([len(path) for path in horse.hypernym_paths()])
    print(wordnet.lch_similarity(dog, horse))