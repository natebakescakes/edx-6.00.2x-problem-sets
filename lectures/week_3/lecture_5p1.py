

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    import random
    
    bucket = ['Red', 'Red', 'Red', 'Green', 'Green', 'Green']
    
    def pick(bucket, trial):
        # (list) -> str
        temp_list = bucket[:]
        while trial > 0:
            temp_list.remove(random.choice(temp_list))
            trial -= 1
            
        return temp_list
    
    count = 0
    for i in range(numTrials):
        if any(pick(bucket, 3) == x for x in (['Green', 'Green', 'Green'], ['Red', 'Red', 'Red'])):
            count += 1
            
    return count / float(numTrials)
        
