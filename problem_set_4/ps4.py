# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': True}
    mutProb = 0.005
    
    #difference = [300, 150, 75, 0]
    #
    #pylab.figure(1)
    #
    #for i in range(len(difference)):
    #    final_pop = []
    #    for trial in range(numTrials):
    #        patient = TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for j in range(numViruses)], maxPop)
    #        for timestep in range(difference[i]):
    #            patient.update()
    #            
    #        patient.addPrescription("guttagonol")
    #        
    #        for timestep in range(150):
    #            patient.update()
    #            
    #        final_pop.append(patient.getTotalPop())
    #    
    #    pylab.subplot(len(difference), 1, i+1)
    #    pylab.hist(final_pop, 50)
    #    pylab.title('No. of updates before prescription added = {}'.format(difference[i]))
    #    pylab.xlabel('# viruses')
    #    pylab.ylabel('Times occured')    
    #
    #pylab.legend(loc='upper right')
    #pylab.show()
    
    final_pop = []
    for trial in range(numTrials):
        patient = TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for j in range(numViruses)], maxPop)
        for timestep in range(150):
            patient.update()
            
        patient.addPrescription("guttagonol")
        
        for timestep in range(150):
            patient.update()
            
        final_pop.append(patient.getTotalPop())
    
    pylab.figure(2)
    pylab.hist(final_pop, 50)
    pylab.xlabel('# viruses')
    pylab.ylabel('Times occured')
    pylab.legend(loc='upper right')
    pylab.show()

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    
    difference = [300, 150, 75, 0]
    
    pylab.figure(1)
    
    for i in range(len(difference)):
        final_pop = []
        for trial in range(numTrials):
            patient = TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for j in range(numViruses)], maxPop)
            for timestep in range(150):
                patient.update()
                
            patient.addPrescription("guttagonol")
            
            for timestep in range(difference[i]):
                patient.update()
                
            patient.addPrescription("grimpex")
            
            for timestep in range(150):
                patient.update()
                
            final_pop.append(patient.getTotalPop())
        
        pylab.subplot(len(difference), 1, i+1)
        pylab.hist(final_pop, 50)
        variance = [sum((x - sum(final_pop) / float(len(final_pop)) ** 2)) for x in final_pop]
        pylab.title('No. of updates before prescription added = {}'.format(difference[i]))
        pylab.xlabel('# viruses, variance = ' + variance)
        pylab.ylabel('Times occured')   
 
    
    pylab.legend(loc='upper right')
    pylab.show()
