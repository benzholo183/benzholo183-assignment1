""" water.py """
# Define how to represent a state
class State:
    # Each state stores the amount of water in both bottles
    def __init__(self, x, y, z):
        self.x = x  # amount of water in bottle X
        self.y = y  # amount of water in bottle Y
        self.z = z  
    def __str__(self):
        # Convert a state into a string
        return "[%d, %d, %d]" % (self.x, self.y, self.z)

    def __repr__(self):
        # Representation of a state
        return str(self)

    def __eq__(self, s):
        return isinstance(s, self.__class__) and \
                self.x == s.x and self.y == s.y and self.z == s.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

# Define the initial state
def initial_state():
    # We start from the state where The 19-gallon jug is empty, but the others are full.
    return State(0, 13, 7)

# Define how to check if a state is a goal state
def is_goal(s):
    # It is a goal when jug X or Y contains 10 gallons.
    if (s.x == 10)or(s.y == 10):
        return True
    return False

# Define how to generate successors according to the problem
def successors(s):
    # This function returns a list of (state, cost) pairs
    # where state is a successor of s, and
    #       cost  is the cost required to generate this state
    # Case 1: Try to empty the bottle X
    if s.x > 0:
        # State(0, s.y, s.z) = a state where X is empty and 
        #                 Y remains unchanged
        #                 Z remains unchanged
        # Cost = s.x since we throw away the water in X
        yield (State(0, s.y, s.z), s.x)

    # Case 2: Try to empty the bottle Y
    if s.y > 0:
        yield (State(s.x, 0, s.z), s.y)

    # Case 3: Try to empty the bottle Z
    if s.z > 0:
        yield (State(s.x, s.y, 0), s.z)



    # Case Pour from X : Try to pour water from X to Y
    t = 13-s.y   # available space of Y
    if s.x > 0 and t > 0:
        if s.x > t:
            # Pour until Y is full
            yield (State(s.x-t, 13, s.z), t)
        else:
            # Pour until X is empty
            yield (State(0, s.y+s.x, s.z), s.x)
         
    # Case Pour from X : Try to pour water from X to Z
    t = 7-s.z   # available space of Z
    if s.x > 0 and t > 0:
        if s.x > t:
            # Pour until Z is full
            yield (State(s.x-t, s.y, 7), t)
        else:
            # Pour until X is empty
            yield (State(0, s.y, s.z+s.x), s.x)


    # Case Pour from Y: Try to pour water from Y to X
    t = 19-s.x   # available space of X
    if s.y > 0 and t > 0:
        if s.y > t:
            # Pour until X is full
            yield (State(19, s.y-t, s.z), t)
        else:
            # Pour until Y is empty
            yield (State(s.x+s.y, 0, s.z), s.y)

    # Case Pour from Y: Try to pour water from Y to Z
    t = 7-s.z   # available space of Z
    if s.y > 0 and t > 0:
        if s.y > t:
            # Pour until Z is full
            yield (State(s.x, s.y-t, 7), t)
        else:
            # Pour until Y is empty
            yield (State(s.x, 0, s.z+s.y), s.y)


    # Case Pour from Z: Try to pour water from Z to X
    t = 19-s.x   # available space of X
    if s.z > 0 and t > 0:
        if s.z > t:
            # Pour until X is full
            yield (State(19, s.y, s.z-t), t)
        else:
            # Pour until Z is empty
            yield (State(s.x+s.z, s.y, 0), s.z)

    # Case Pour from Z: Try to pour water from Z to Y
    t = 13-s.y   # available space of Y
    if s.z > 0 and t > 0:
        if s.z > t:
            # Pour until Y is full
            yield (State(s.x, 13, s.z-t), t)
        else:
            # Pour until Z is empty
            yield (State(s.x, s.z+s.y, 0), s.z)
