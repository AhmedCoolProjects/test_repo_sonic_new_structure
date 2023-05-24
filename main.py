from yapsy.IMultiprocessPlugin import IMultiprocessPlugin
from multiprocessing import Pipe


class PluginOne(IMultiprocessPlugin):
    def __init__(self, p):
        IMultiprocessPlugin.__init__(self,p)
        print('inited')
    def run(self):
        data = self.parent_pipe.recv()
        print(f'Plugin 1 received: {data}')
