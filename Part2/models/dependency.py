from .settings import *

ROOT = "ROOT"

LEFT_ARC = {
    N: {V: "subj", NAME: "nmod"},
    V: {},
    Q: {N: "query"},
    PP: {TIME: "timemod"},
    TIME: [],
    NAME: {V: "subj"},
    ROOT: [],
    DURATION: {V: "duration"},
    YN: [],
}

RIGHT_ARC = {
    N: {Q: "query"},
    V: {TIME: "time", PUNC: "punc", NAME: "dobj", PP: "pp", YN: "yesno"},
    Q: [],
    PP: {NAME: "pmod"},
    TIME: [],
    NAME: [],
    ROOT: {V: "root"},
    DURATION: [],
    YN: [],
}



class Dependency:
    """
    Represents a dependency relation of the dependency parser.
    E.g. subj(đến, tour) == đến -subj-> tour
    """
    
    def __init__(self, relation: str, head: str, dependent: str):
        self.relation = relation    # e.g. subj
        self.head = head            # e.g. đến
        self.dependent = dependent  # e.g. tour
    
    def __str__(self) -> str:
        return f"\"{self.head}\" --{self.relation}-> \"{self.dependent}\""

def malt_parse(tokens: "list[str]") -> "list[Dependency]":

    buffer = tokens.copy()
    stack = [ROOT]
    dependencies = []
    root_verb = None

    while buffer:
        stack_item = stack[-1]
        buffer_item = buffer[0]
        
        stack_item_type = POS.get(stack_item, None) if stack_item is not ROOT else stack_item
        buffer_item_type = POS.get(buffer_item, None)

        if buffer_item_type == V and root_verb is None:
            root_verb = buffer_item
        
        if isinstance(buffer_item_type, tuple):
            buffer_item_type = buffer_item_type[0] if root_verb == buffer_item else buffer_item_type[1]
            
        if isinstance(stack_item_type, tuple):
            stack_item_type = stack_item_type[0] if root_verb == stack_item else stack_item_type[1]

        dep = None
        # RIGHT_ARC
        if buffer_item_type in RIGHT_ARC[stack_item_type]:
            dep = Dependency(
                RIGHT_ARC[stack_item_type][buffer_item_type],
                stack_item,
                buffer_item)

            stack.append(buffer.pop(0))


        # LEFT_ARC
        elif buffer_item_type in LEFT_ARC[stack_item_type]:
            dep = Dependency(
                LEFT_ARC[stack_item_type][buffer_item_type],
                buffer_item,
                stack_item)

            stack.pop()


        # SHIFT
        else:
            stack.append(buffer.pop(0))
        if dep:
            dependencies.append(dep)

    return dependencies