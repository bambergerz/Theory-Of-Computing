import networkx as nx
import Alphabet


class DFA:
    def __init__(self, states, alphabet, transition_funcs, start_states, end_states):
        """

        :param states: a list of states. Each state in a DFA is unique. Can be represented with either ints or strings.
        :param alphabet: an object of type alphabet (see Alphabet module)
        :param transition_funcs: a list of tuples of the form (source, target, char) where
        char is the character in the alphabet which enables us to take this transition from
        the source to the target
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
        """

        :return: Given the already set attributes, create the graph
        through which the DFA runs via the set of transition function that define edges.
        """

        CHAR = "char"

        g = nx.DiGraph()
        for f in self.transition_funcs:
            source, target, char = f
            self._assert_trans_func(self.alphabet, self.states, source, target, char)
            g.add_edge(source, target)
            g[source][target][CHAR] = char
        return g

    @staticmethod
    def _assert_trans_func(alphabet, states, char, source, target):
        """
        Crash if char is not in the alphabet or source or target are not in the set of states.

        :param alphabet: the alphabet of this machine
        :param states: the states of this machine
        :param char: an input character which should be in the alphabet.
        If we encounter this character in the source state, we transition to the target state.
        :param source: the source state of this transition function. In the provided set of states
        :param target: the target state of this transition function. In the provided set of states.
        :return: None
        """

        # Assertion handling:
        assert char in alphabet.symbols, "the character " + str(char) + \
                                         " which defines this transition function is not in the alphabet"
        assert source in states, "the state " + str(source) + \
                                 " which is the source of this transition function is" \
                                 " not present in the set of states"
        assert target in states, "the state " + str(target) + \
                                 " which is the target of this transition function is" \
                                 " not present in the set of states"


if __name__ == "__main__":
    pass




