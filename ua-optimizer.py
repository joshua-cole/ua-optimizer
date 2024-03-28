import numpy as np
import random

def filter_list_items(main_list, filter_list):
    return list(filter(lambda item: item not in filter_list, main_list))

def test_randomizer(samp, PAX, perc):
    return random.sample(samp, round(PAX * perc))

# Create a list of unique values to represent total population
totalPopulationList = []
totalPAX = len(totalPopulationList)

annualResult = []

year = 0
while year < 20:
    i = 0
    yearlyTotal = 0
    testedPopulation = []
    randomSelection = []
    while i < 12:
        #Leadership Directed selection from untested population
        untestedPopulation = filter_list_items(totalPopulationList, testedPopulation)
        untestedPAX = len(untestedPopulation)
        directedPercentage = (i/(12-i))/12
        randomUntestedSelection = test_randomizer(untestedPopulation, untestedPAX, directedPercentage)

        # Random Monthly Selection
        randomPercentage = 0.10
        randomSelection = test_randomizer(totalPopulationList, totalPAX, randomPercentage)

        # Aggregate sum of both
        testedPopulation += set(filter_list_items(randomSelection, testedPopulation))
        testedPopulation += set(filter_list_items(randomUntestedSelection, testedPopulation))
        yearlyTotal += len(randomSelection) + len(randomUntestedSelection)
        i += 1

    individualsTested = len(testedPopulation)
    annualResult.append(individualsTested)
    year += 1

annAverage = np.average(annualResult)
