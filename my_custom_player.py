
from sample_players import DataPlayer
import time


class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE: 
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random
        start_time = time.time()
        if state.ply_count == 0:
          self.queue.put(57)
        elif state.ply_count == 1:
          self.queue.put(random.choice(state.actions()))
        else:
          depth_limit = 6
          for depth in range(1,depth_limit+1):
            best_move = self.alpha_beta_search(state, depth, start_time)
            if self.time_limiter(start_time):
              break
          self.queue.put(best_move)
    
    def alpha_beta_search(self, state, depth, start_time):

      def min_value(state, alpha, beta, depth, start_time):
          if state.terminal_test(): return state.utility(self.player_id)
          if depth <= 0: return self.score(state)
          value = float("inf")
          for action in state.actions():
              value = min(value, max_value(state.result(action), alpha, beta, depth - 1, start_time))
              if value <= alpha:
                return value
              beta = min(beta, value)
              if self.time_limiter(start_time):
                break
          return value

      def max_value(state, alpha, beta, depth, start_time):
          if state.terminal_test(): return state.utility(self.player_id)
          if depth <= 0: return self.score(state)
          value = float("-inf")
          for action in state.actions():
              value = max(value, min_value(state.result(action), alpha, beta, depth - 1, start_time))
              if value >= beta:
                return value
              alpha = max(alpha, value)
              if self.time_limiter(start_time):
                break
          return value

      alpha = float("-inf")
      beta = float("inf")
      best_score = float("-inf")
      best_move = None
      for action in state.actions():
        value = min_value(state.result(action), alpha, beta, depth, start_time)
        alpha = max(alpha, value)
        if value >= best_score:
          best_score = value
          best_move = action
        if self.time_limiter(start_time):
          break
      return best_move

    def score(self, state):
        own_loc = state.locs[self.player_id]
        opp_loc = state.locs[1 - self.player_id]
        own_liberties = state.liberties(own_loc)
        opp_liberties = state.liberties(opp_loc)
        remaining_own_liberties = sum(len(state.liberties(l)) for l in own_liberties)
        remaining_opp_liberties = sum(len(state.liberties(l)) for l in opp_liberties)
        return len(own_liberties) - 2*len(opp_liberties) + remaining_own_liberties - remaining_opp_liberties

    def time_limiter(self, start_time):
      time_limit = 140
      end_time = time.time()
      if end_time * 1000 - start_time * 1000 >= time_limit:
          return True
      else:
          return False