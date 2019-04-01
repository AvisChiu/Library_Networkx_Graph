import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time

def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act

def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act,1))
    return next_action

def update(current_state, action, gamma):
    
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]
    Q[current_state, action] = R[current_state, action] + gamma * max_value
    print('max_value', R[current_state, action] + gamma * max_value)
    if (np.max(Q) > 0):
        return(np.sum(Q/np.max(Q)*100))
    else:
        return (0)
        
def map(map_data):

    points_list = map_data
    G.add_edges_from(points_list)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    plt.show()

def reward_martrix():

    for point in points_list:
        print(point) 
        if point[1] == terminal:
            R[point] = 100
        else:
            R[point] = 0
        if point[0] == terminal:
            R[point[::-1]] = 100
        else:
            R[point[::-1]]= 0
    R[terminal,terminal]= 100
    print(R)


# def q_table_tranning():


if __name__ == "__main__":
    
    # start = time.clock()
    # end = time.clock()
    # print(end-start)


    G=nx.Graph()
    points_list = data = [(0, 1), (0, 2), (0, 3), 
                        (1, 0),(1, 3),(1, 4),
                        (2, 0),(2, 3),(2, 5),
                        (3, 0),(3, 1),(3, 2),(3, 4),(3, 5),(3, 6),
                        (4, 1),(4, 3),(4, 6),
                        (5, 2),(5, 3),(5, 6),
                        (6, 3),(6, 4),(6, 5)]

    terminal = 6
    map(points_list)

    MATRIX_SIZE = 7
    R = np.matrix(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
    R *= -1
    reward_martrix()

    Q = np.matrix(np.zeros([MATRIX_SIZE,MATRIX_SIZE]))
    gamma = 0.9                                                 # learning parameter / learning rate
    initial_state = 1

    # available_act = available_actions(initial_state)
    # action = sample_next_action(available_act)
    # update(initial_state, action, gamma)




    """
    ==================================== Trainning ==========================================
    """
    scores = []
    for i in range(1000):
        current_state = np.random.randint(0, int(Q.shape[0]))
        available_act = available_actions(current_state)
        action = sample_next_action(available_act)
        score = update(current_state,action,gamma)
        scores.append(score)
        print ('Score:', str(score))
    
    print("Trained Q matrix:")
    print(Q/np.max(Q)*100)



    """
    ==================================== Testing ============================================
    """
    current_state = 0
    steps = [current_state]
    while current_state != 6:
        next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]
        if next_step_index.shape[0] > 1:
            next_step_index = int(np.random.choice(next_step_index, size = 1))
        else:
            next_step_index = int(next_step_index)
        steps.append(next_step_index)
        current_state = next_step_index

    print("Most efficient path:")
    print(steps)
    plt.plot(scores)
    plt.show()


    