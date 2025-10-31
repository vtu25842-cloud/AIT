import numpy as np
from numpy import inf

# given values for the problems
d = np.array([[0, 10, 12, 11, 14],
              [10, 0, 13, 15, 8],
              [12, 13, 0, 9, 14],
              [11, 15, 9, 0, 16],
              [14, 8, 14, 16, 0]])

iteration = 100
n_ants = 5
n_citys = 5

# initialization part
m = n_ants
n = n_citys
e = 0.5      # evaporation rate
alpha = 1    # pheromone factor
beta = 2     # visibility factor

# calculating the visibility of the next city visibility(i,j)=1/d(i,j)
visibility = 1 / d
visibility[visibility == inf] = 0  # Set visibility to self as 0

# initializing pheromone present at the paths (n x n matrix)
pheromne = 0.1 * np.ones((n, n)) # CHANGED: Was (m, n), needs to be (n, n) for paths

# initializing the route of the ants with size rute(n_ants, n_citys+1)
# note adding 1 because we want to come back to the source city
rute = np.ones((m, n + 1))

# Store the all-time best route
all_time_best_route = np.zeros(n + 1)
all_time_min_cost = inf

for ite in range(iteration):

    rute[:, 0] = 1  # initial starting position of every ant is '1' i.e city '1'
    # The last element is already 1 from np.ones, representing the return

    for i in range(m):
        
        temp_visibility = np.array(visibility)  # creating a copy of visibility
        
        for j in range(n - 1): # Loop to visit n-1 cities (city 2 to city n)
            
            combine_feature = np.zeros(5)  # initializing combine_feature array to zero
            cum_prob = np.zeros(5)         # initializing cumulative probability array to zeros
            
            cur_loc = int(rute[i, j] - 1)  # current city of the ant (0-indexed)
            
            temp_visibility[:, cur_loc] = 0  # making visibility of the current city as zero
            
            # CHANGED: Swapped alpha and beta to match the standard formula
            # (pheromone^alpha) * (visibility^beta)
            p_feature = np.power(pheromne[cur_loc, :], alpha)  # calculating pheromone feature
            v_feature = np.power(temp_visibility[cur_loc, :], beta)  # calculating visibility feature
            
            # Note: The .newaxis lines were not necessary as p_feature and v_feature are already 1D arrays
            
            combine_feature = np.multiply(p_feature, v_feature)  # calculating the combine feature
                                          
            total = np.sum(combine_feature)  # sum of all the features
            
            # Handle division by zero if all paths are blocked
            if total == 0:
                probs = np.zeros(n)
            else:
                probs = combine_feature / total  # finding probability
            
            cum_prob = np.cumsum(probs)  # calculating cumulative sum
            
            r = np.random.random_sample()  # random no in [0,1)
            
            # finding the next city
            try:
                city = np.nonzero(cum_prob > r)[0][0] + 1
            except IndexError:
                # Fallback if 'r' is too large (e.g., due to rounding)
                city = np.argmax(cum_prob) + 1 

            rute[i, j + 1] = city  # adding city to route
            
        # The two lines for 'left' were logically incorrect and have been removed.
        # The loop (n-1) times correctly fills all n cities.
        # rute[i, -1] is already 1, completing the tour back to the start.

    rute_opt = np.array(rute)  # initializing optimal route
    
    dist_cost = np.zeros((m, 1))  # initializing total_distance_of_tour with zero
    
    for i in range(m):
        
        s = 0
        # CHANGED: Loop n times to calculate all n segments of the path
        for j in range(n): 
            s = s + d[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1]  # calculating total tour distance
            
        dist_cost[i] = s  # storing distance of tour for 'i'th ant
        
    dist_min_loc = np.argmin(dist_cost)  # finding location of minimum of dist_cost
    dist_min_cost = dist_cost[dist_min_loc]  # finding min of dist_cost
    
    # Check if this iteration's best is the all-time best
    if dist_min_cost < all_time_min_cost:
        all_time_min_cost = dist_min_cost
        all_time_best_route = rute_opt[dist_min_loc, :].copy()

    best_route_current_iter = rute_opt[dist_min_loc, :]
    pheromne = (1 - e) * pheromne  # evaporation of pheromone
    
    for i in range(m):
        # CHANGED: Loop n times to update pheromones for all n segments
        for j in range(n):
            dt = 1 / dist_cost[i]
            pheromne[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1] = pheromne[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1] + dt
            # updating the pheromone

print('Route of all ants at the end:')
print(rute_opt)
print()
print('Best path found:', all_time_best_route.astype(int))
print('Cost of the best path:', int(all_time_min_cost[0]))