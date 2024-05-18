from models.settings import *
from models.dependency import Dependency

class Relation:
    def __init__(self, type: str, left: str, right: str):
        self.type = type   
        self.left = left    
        self.right = right  
    
    def __str__(self) -> str:
        return f"({self.left} {self.type} {self.right})"

class SEM:
    
    def __init__(self, predicate: str, variable, relations=None):
        self.predicate = predicate
        self.variable = variable
        self.relations = relations if relations else []
    
    def __str__(self) -> str:
        return f"({self.predicate} {self.variable} {', '.join([str(r) for r in self.relations])})"

def construct_semantic(dependencies: "list[Dependency]") -> SEM:

    subjects = {}
    objects = {}

    for dep in dependencies:
        if "subj" in dep.relation:
            subjects[dep.head] = dep.dependent
        elif "obj" in dep.relation:
            objects[dep.head] = dep.dependent

    for dep in dependencies:
        if dep.head in subjects and dep.dependent in objects:
            return SEM("query", objects[dep.dependent], [Relation(dep.relation, subjects[dep.head], dep.dependent)])

    return None