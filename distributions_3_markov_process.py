#!/usr/bin/env python3
import sys
import numpy as np
import random
import scipy as sp
import sklearn as skl
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# MARKOV PROCESS

class state_machine:
    def __init__(self):
        self.transition_probabilities={
            'A':[0.88,0.05,0.02,0.05],
            'C':[0.06,0.82,0.06,0.06],
            'G':[0.01,0.04,0.92,0.03],
            'T':[0.07,0.04,0.03,0.86],
        }
        self.states=list(self.transition_probabilities.keys())
        self.current_state=random.choice(self.states)
        self.sequence=self.current_state
    
    def step(self):
        rd=random.random()
        t_prob=self.transition_probabilities[self.current_state]
        cutoffs=[0.0]+[sum(t_prob[:n+1]) for n in range(len(t_prob))]
        for i in range(len(self.states)):
            if rd >= cutoffs[i] and rd <= cutoffs[i+1]:
                self.current_state=self.states[i]
                break
        return self.current_state
        
    def gen_sequence(self,n):
        self.sequence=self.current_state
        for i in range(n):
            self.sequence+=self.step()
        return self.sequence






sm=state_machine()
sequences=[]
for i in range(1000):
    sequences.append(sm.gen_sequence(250))
print(sequences)

def count_agct(seq):
    counts={'A':0,'C':0,'G':0,'T':0}
    for i in range(len(seq)):
        counts[seq[i]]+=1
    return counts

aggregate_counts={'A':0,'C':0,'G':0,'T':0}
indiv_probabilities=[]
for s in sequences:
    count=count_agct(s)
    prob=[]
    for n in count:
        aggregate_counts[n]+=count[n]
        prob.append(count[n]/len(s))
    indiv_probabilities.append(prob)

indiv_probabilities=np.array(indiv_probabilities)
print('A',np.mean(indiv_probabilities[:,0]),np.std(indiv_probabilities[:,0]))
print('C',np.mean(indiv_probabilities[:,1]),np.std(indiv_probabilities[:,1]))
print('G',np.mean(indiv_probabilities[:,2]),np.std(indiv_probabilities[:,2]))
print('T',np.mean(indiv_probabilities[:,3]),np.std(indiv_probabilities[:,3]))


sum_counts=len(sequences[0])*len(sequences)
aggregate_probabilities={}
for n in aggregate_counts:
    aggregate_probabilities[n]=aggregate_counts[n]/sum_counts
print(aggregate_probabilities)
cdf_in=[
    aggregate_probabilities['A'],
    aggregate_probabilities['C'],
    aggregate_probabilities['G'],
    aggregate_probabilities['T'],
]

cumulative_probabilities=[0.0]+[sum(cdf_in[:n]) for n in range(1,len(aggregate_probabilities)+1)]

def gen_seq(cumulative_probabilities):
    bases=['A','C','G','T']
    sequence=""
    for i in range(250):
        rd=random.random()
        for n in range(len(cumulative_probabilities)-1):
            if rd >= cumulative_probabilities[n] and rd <= cumulative_probabilities[n+1]:
                sequence+=bases[n]
    return sequence

print(gen_seq(cumulative_probabilities))