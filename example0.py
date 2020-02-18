####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Turtles0'
strategy_name = 'Collude then betray upon betrayal'
strategy_description = 'eetray only if your partner betrays in the previous round.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always colludes.
    if len(my_history) < 3: #If the length of my history is less then 3 then collude.
      return "c"
    elif len(their_history) - 1 == "b": #Else if their previous move was a betrayal. 
      return "b" #Return a betrayal
    else: #If their previous move was not a betrayal then return collude.
      return "c"
    