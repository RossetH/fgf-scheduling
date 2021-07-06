from amplpy import AMPL, Environment
from numpy import array, count_nonzero

class FGFScheduler(object):
    """docstring for """
    
    def __init__(self,amplpath,model_path,data_path):
        self.amplpath = amplpath
        self.model = model_path
        self.data = data_path
        self.ampl = AMPL(Environment(self.amplpath))
        pass

    def solve(self):
        self.ampl.read('ampl/homeawaypattern.mod')
        self.ampl.readData('ampl/slots_2021fgf.dat')
        self.ampl.setOption('solver','cbc.exe')
        self.ampl.solve()
        pass

class FGFHandler(object):
    """docstring for """
    
    def __init__(self,ampl):
        self.ampl = ampl
        self.n = self.ampl.getParameter('n').getValues().toList()[0]
        self.start =  self.ampl.getVariable('start').getValues().toDict()
        self.to_home = self.ampl.getVariable('to_home').getValues().toDict()
        self.to_away = self.ampl.getVariable('to_away').getValues().toDict()
        self.homeawaypattern = []
        self.breaks = []
        pass

    def at_home(self,i,t):
        start_i = self.start[i]
        tmp = []
        for t1 in range(1,t):
            tmp.append(self.to_home[(i,t1)]-self.to_away[(i,t1)])
        return start_i + array(tmp).sum()

    def get_homeawaypattern(self):
        for i in range(1,int(self.n)+1):
            tmp = []
            for t in range(1,int(self.n)):
                tmp.append(self.at_home(i,t))
            self.homeawaypattern.append(tmp)
        pass

    def get_breaks(self):
        for i in range(1,int(self.n)+1):
            tmp = []
            for t1 in range(1,int(self.n)-1):
                #if self.to_home[(i,t1)]+self.to_away[(i,t1)] == 0:
                tmp.append(self.to_home[(i,t1)]+self.to_away[(i,t1)])
                #else:
                #    tmp.append('')
            self.breaks.append(tmp)
        pass

    def handle(self):       
        self.get_homeawaypattern()
        self.get_breaks()

if __name__ == '__main__':
    model = FGFScheduler(amplpath=r'~/path/to/AMPL',
                        model_path = 'ampl/homeawaypattern.mod',
                        data_path = 'ampl/slots_2021fgf.dat')

    model.solve()

    schedule = FGFHandler(model.ampl)

    schedule.handle()

    home_away_agg = array([count_nonzero(array(schedule.homeawaypattern)==0,axis=1),
                            count_nonzero(array(schedule.homeawaypattern)==1,axis=1)])

    breaks_agg = count_nonzero(array(schedule.breaks)==0,axis=1)

    n_breaks = count_nonzero(array(schedule.breaks)==0)