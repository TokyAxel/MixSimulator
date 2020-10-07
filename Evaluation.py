#import sys
#from MixSimulator import MixSimulator
import matplotlib.pyplot as plt
#from matplotlib.ticker import StrMethodFormatter
import numpy as np
from math import ceil
from math import floor
import itertools
from typing import List
from .nevergradBased import Optimizer as opt
from . import Demand as de

class EvaluationBudget:

    def __init__(self):
        tmp = opt.Optimizer()
        self.__available_optimizers = tmp.getOptimizerList()
        self.__marker = itertools.cycle((',', '+', '.', 'o', '*','x','v','^','s')) 
        
    def moving_average(self, x, w):
        return np.convolve(x, np.ones(w), 'valid') / w

    def set_units(self,value):
        # Y units
        N=value
        if N>=1000000: 
            units=1000000
            labelY=' Millions'
        else :
            if N>=1000 and N<1000000:
                units=1000
                labelY='k'
            else :
                units=1
                labelY=''
        return [labelY,units]
                
    def plot_evaluation(self, X, Y, label_y : List['str'], label : List = ["Optimizer"], max_budgets = 0):
        #init subplot
        fig, axs = plt.subplots(1, len(label_y), figsize=(12, 4))        
        
        #set the moving average wide
        for opt_name, value in Y[label_y[0]].items():
            average_wide = ceil(len(value)/4)
            #units=self.set_units(value[0])
            break
     
        # data integration        
        for n_axs in range(0,len(axs)) :
            dict_ = Y[label_y[n_axs]]
            for opt_name, value in dict_.items():
                smooth_value = self.moving_average(value,average_wide)
                axs[n_axs].plot(X[(average_wide - 1):], smooth_value, marker = next(self.__marker), alpha=0.5, lw=2, label=str(opt_name))
        
        # plots parametrizations    
        for n_axs in range(0,len(axs)) :
            axs[n_axs].grid()
            axs[n_axs].yaxis.set_tick_params(length=0)
            axs[n_axs].xaxis.set_tick_params(length=0)
            axs[n_axs].set_xlabel('Budgets')
            #axs[n_axs].yaxis.set_major_formatter(StrMethodFormatter("{x}"+units[0]))
            axs[n_axs].set_ylabel(label_y[n_axs])
            axs[n_axs].legend()
            
        fig.tight_layout()
        plt.show()
        
    def plot_evaluation_2(self, X, Y, label_y : List['str'], label : List = ["Optimizer"], max_budgets = 0):
        #init subplot
        max_col = ceil(len(label_y)/2)
        min_col = floor(len(label_y)/2)
        fig, axs = plt.subplots(2, max_col, figsize=(10, 8))        
        
        #set the moving average wide
        for opt_name, value in Y[label_y[0]].items():
            average_wide = ceil(len(value)/4)
            #units=self.set_units(value[0])
            break
     
        # data integration
        #texts=[]        
        for n_axs in range(0,max_col) :
            dict_ = Y[label_y[n_axs]]
            for opt_name, value in dict_.items():
                smooth_value = self.moving_average(value,average_wide)
                axs[0][n_axs].plot(X[(average_wide - 1):], smooth_value, marker = next(self.__marker), alpha=0.5, lw=2, label=opt_name)
                #axs[0][n_axs].xticks(np.arrange(min(X),max(X)+1,1.0))
                #axs[0][n_axs].yticks(np.arrange(min(smooth_value),max(smooth_value)+1,1.0))
                #label_per_opt = axs[0][n_axs].text(X[-1],smooth_value[-1],opt_name+"("+str(float("{:.2f}".format(smooth_value[-1])))+")")
                #texts.append(label_per_opt)
                #axs[0][n_axs].annotate( label_per_opt,
                #              xy     = (     X[-1], smooth_value[-1]),
                #              xytext = (1.02*X[-1], smooth_value[-1]),
                #            )
        #adjust_text(texts)       
        
        for n_axs in range(0,min_col) :
            dict_ = Y[label_y[max_col+n_axs]]
            for opt_name, value in dict_.items():
                smooth_value = self.moving_average(value,average_wide)
                axs[1][n_axs].plot(X[(average_wide - 1):], smooth_value, marker = next(self.__marker), alpha=0.5, lw=2, label=opt_name)
                #axs[1][n_axs].xticks(np.arrange(min(X),max(X)+1,1.0))
                #axs[1][n_axs].yticks(np.arrange(min(smooth_value),max(smooth_value)+1,1.0))
                #axs[1][n_axs].annotate(opt_name+"("+str(float("{:.2f}".format(smooth_value[-1])))+")",
                #              xy     = (     X[-1], smooth_value[-1]),
                #              xytext = (1.02*X[-1], smooth_value[-1]),
                #            )

        
        # plots parametrizations   
        for row in range (0,2):
            if row == 0 :
                for n_axs in range(0,max_col) :
                    axs[row][n_axs].grid()
                    axs[row][n_axs].yaxis.set_tick_params(length=0)
                    axs[row][n_axs].xaxis.set_tick_params(length=0)
                    axs[row][n_axs].set_xlabel('Budgets')
                    #axs[n_axs].yaxis.set_major_formatter(StrMethodFormatter("{x}"+units[0]))
                    axs[row][n_axs].set_ylabel(label_y[n_axs])
                    axs[row][n_axs].legend()
            else :
                for n_axs in range(0,min_col) :
                    axs[row][n_axs].grid()
                    axs[row][n_axs].yaxis.set_tick_params(length=0)
                    axs[row][n_axs].xaxis.set_tick_params(length=0)
                    axs[row][n_axs].set_xlabel('Budgets')
                    #axs[n_axs].yaxis.set_major_formatter(StrMethodFormatter("{x}"+units[0]))
                    axs[row][n_axs].set_ylabel(label_y[max_col+n_axs])
                    axs[row][n_axs].legend()
            
        fig.tight_layout()
        plt.show()

    def plot_time_evolution(self, data, label_y : List['str'], label : List = ["Optimizer"], max_budgets = 0):
        #init subplot
        print(data)
        
        fig, axs = plt.subplots(1, len(label_y)-1, figsize=(12, 4))        
        
        # data integration        
        for n_axs in range(1,len(axs)) :
            dict_ = data[label_y[n_axs]]
            for opt_name, value in dict_.items():
                axs[n_axs].scatter(data["execution_time (s)"][opt_name], value, alpha=0.5, lw=2, label=str(opt_name))
        
        # plots parametrizations    
        for n_axs in range(0,len(axs)) :
            axs[n_axs].grid()
            axs[n_axs].yaxis.set_tick_params(length=0)
            axs[n_axs].xaxis.set_tick_params(length=0)
            axs[n_axs].set_xlabel('Budgets')
            #axs[n_axs].yaxis.set_major_formatter(StrMethodFormatter("{x}"+units[0]))
            axs[n_axs].set_ylabel(label_y[n_axs])
            axs[n_axs].legend()
            
        fig.tight_layout()
        plt.show()

    def check_opt_list(self,optimizer_list):
        for index in range(0, len(optimizer_list)):
            try :
                if optimizer_list[index] not in self.__available_optimizers:
                    optimizer_list.pop(index)
            except IndexError :
                self.check_opt_list(optimizer_list)


    def evaluate(self, mix, sequence, max_budgets, optimizer_list: List['str'], indicator_list: List['str'], bind=None, carbonProdLimit: float = 39500000000, time_interval : float = 1) :        
        #setting dataset
        if bind != None:
            mix.set_data_csv(str(bind))

        self.check_opt_list(optimizer_list) 
        if optimizer_list == [] :
            raise IndexError("Selected optimizers are not available.")

       #process
        y_tmp = {}
        budget = np.arange(0, max_budgets, sequence)

        ind_per_opt = {}
        for opt_name in optimizer_list:
            data = mix.optimizeMix(carbonProdLimit= carbonProdLimit,
                            time_interval = time_interval, optimize_with = [opt_name], budgets = [max_budgets], step = sequence)
            ind_per_opt.update({opt_name:data})

        for indicator in indicator_list:
            new_ind_per_opt = {}
            for opt_name, values in ind_per_opt.items():
                ind_per_budget = []
                for budget_value in values:
                    ind_per_budget.append(float(budget_value[indicator]))
                new_ind_per_opt.update({opt_name:ind_per_budget})
            y_tmp.update({indicator: new_ind_per_opt})
            
        #plotting
        self.plot_evaluation_2(X=np.array(budget),Y=y_tmp,label_y = indicator_list, label=optimizer_list, max_budgets = max_budgets)
        # self.plot_time_evolution(y_tmp,label_y = indicator_list, label=optimizer_list, max_budgets = max_budgets)    
        
    def evaluate_total_time(self, mix, sequence, max_budgets, optimizer_list: List['str'],
                            indicator_list: List['str'], bind = None, carbonProdLimit: float = 39500000000,
                            time_index: int = 24*265, time_interval : float = 1):
        #setting dataset
        
        budget = np.arange(0, max_budgets, sequence)

        if bind != None:
            mix.set_data_csv(str(bind))

        self.check_opt_list(optimizer_list) 
        if optimizer_list == [] :
            raise IndexError("Selected optimizers are not available.")
        
       #process
        data_interval = []
        current_demand=de.Demand(12,0.2,0.3)
        for time in range(0,time_index):
            mix.set_demand(current_demand.get_demand_approxima(time,time_interval))
            print(current_demand.get_demand_approxima(time,time_interval))
            ind_per_opt = {}
            for opt_name in optimizer_list:
                data = mix.optimizeMix(carbonProdLimit= carbonProdLimit,
                                time_interval = time_interval, optimize_with = [opt_name], budgets = [max_budgets], step = sequence)
                ind_per_opt.update({opt_name:data})
            data_interval.append(ind_per_opt)
        
        Y = []
        for time in range(0,time_index):
            y_tmp = {}
            for indicator in indicator_list:
                new_ind_per_opt = {}
                for opt_name, values in ind_per_opt.items():
                    ind_per_budget = []
                    for budget_value in values:
                        ind_per_budget.append(float(budget_value[indicator]))
                    new_ind_per_opt.update({opt_name:ind_per_budget})
                y_tmp.update({indicator: new_ind_per_opt})
            Y.append(y_tmp)

        result = {}
        for indicator in indicator_list:
            optimizers_dict = {}
            for opt_name in optimizer_list:
                per_budget = []
                for budget_step in range(0,len(budget)):
                    value = 0
                    for time in range (0, time_index):
                        value += Y[time][indicator][opt_name][budget_step]
                    per_budget.append(value)
                optimizers_dict.update({opt_name:per_budget})
            result.update({indicator: optimizers_dict})
        
        self.plot_evaluation_2(X=np.array(budget),Y=result,label_y = indicator_list, label=optimizer_list, max_budgets = max_budgets)
        
                