class Procedure:
    def __init__(self, name: str, *args):
        self.name = name    
        self.args = args   
    
    def __str__(self) -> str:
        return f"{self.name}({', '.join([str(arg) for arg in self.args])})"