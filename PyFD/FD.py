import pythoncom, win32com.client as client
from collections.abc import Iterable
from PyFD.Setting_class_lib import *
from PyFD.FD_Geo import *

#Initialize the connection
class FdEventHandler:
    
    calculating = True
    
    def OnSolverEnd(self,solvertype):
        print("Solver {0} finished!".format(solvertype))
        FdEventHandler.calculating = False


connector = client.DispatchWithEvents("AklModeler.CommandControl",FdEventHandler)


def execute(command):
    connector.SendInstruction(command)

    
def select_obj(index=None):

    execute("obj unselect all")

    re_val = None

    if index is None:
        re_val = execute("obj select all")

    elif isinstance(index, Iterable):
        re_val = []
        for i in index:
            _i = int(i)
            command = "obj select {}".format(_i)
            re_val.append(execute(command))

    else:
        re_val = execute("obj select {}".format(int(index)))

    return re_val


def UnselectObj(index=None):

    re_val = None

    if index is None:
        re_val = execute("obj unselect all")

    elif isinstance(index, Iterable):
        re_val = []
        for i in index:
            _i = int(i)
            command = "obj unselect {}".format(_i)
            re_val.append(execute(command))

    else:
        re_val = execute("obj unselect {}".format(int(index)))

    return re_val


def trigger_solver(wait_until_done = True):
    
    FdEventHandler.calculating = True
    execute("menu analysis forward")
    
    if wait_until_done:
        while FdEventHandler.calculating:
            pythoncom.PumpWaitingMessages()

            
def preprocess(para_list=None):
    return None


def postprocess(para_list=None):
    return False


def loop_start(iter_count=None):

    goon = True
    counter = 0

    while goon:
        preprocess()
        trigger_solver()
        counter += 1

        if iter_count is None:
            goon = postprocess()
        else:
            goon = postprocess() and counter < iter_count

        print('iteration {} done\r\n '.format(counter))