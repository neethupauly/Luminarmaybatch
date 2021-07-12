# importance goes to methods

class Vscode:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("execute using vscode")
    def debug(self):
        print("debug using vscode")
class Pycharm:
    def compile(self):
        print("compiling using pycharm")
    def execute(self):
        print("execute using pycharm")
    def debug(self):
        print("debug using pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=Programmer()

pyc=Pycharm()
dev.coding(pyc)

vs=Vscode()
dev.coding(vs)
