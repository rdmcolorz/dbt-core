import pprint


class DebugTask:
    def __init__(self, args, project):
        self.args = args
        self.project = project

    def run(self):
        print("args: {}".format(self.args))
        print("project: ")
        pprint.pprint(self.project)
        print("local config: ")
        pprint.pprint(self.project.load_local_config())
