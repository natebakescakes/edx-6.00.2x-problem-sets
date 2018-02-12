import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    results = []
    for trial in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        hand = []
        
        for draw in range(3):
            hand.append(bucket.pop(random.randint(0, len(bucket)-1)))
        
        print hand
        if all(x == 'R' for x in hand) or all(y == 'G' for y in hand):
            results.append('Success')

    return len(results) / float(numTrials)            
    
        