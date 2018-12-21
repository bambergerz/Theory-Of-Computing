import networkx as nx
import Alphabet


class DFA:
    def __init__(self, states, alphabet, transition_funcs, start_states, end_states):
        """

        :param states: a list of states. Each state in a DFA is unique. Can be represented with either ints or strings.
        :param alphabet: an object of type alphabet (see Alphabet module)
        :param transition_funcs: a list of functions which map some state q1 and a character from the alphabet to some
        new state q2. Both q1 and q2 must be in the set of states. the character must be from the alp
        :param start_states:
        :param end_states:
        """

        # Enforce preconditions regarding types
        assert isinstance(states, list)
        assert isinstance(alphabet, Alphabet.Alphabet)
        if len(states) > 0:
            assert isinstance(states[0], int) or\
                   (isinstance(states[0], str) and len(states[0] > 0)), "invalid state type"

        # Enforce non-type preconditions
        assert len(start_states) > 0, "machine must have at least one start state"
        for s in start_states:
            assert s in states, "start state " + str(s) + " is not in the set of states of this machine"
        for s in end_states:
            assert s in states, "end state " + str(s) + " is not in the set of states of this machine"

        # TODO: assertions with respect to transition functions

        self.states = states
        self.alphabet = alphabet
        self.transition_funcs = transition_funcs
        self.start_states = start_states
        self.end_states = end_states
        self.graph = self._generate_graph()


    def _generate_graph(self):
        return nx.DiGraph()



if __name__ == "__main__":
    pass




