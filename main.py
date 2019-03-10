print('Start', '\n')
print("There is a model of a Prisoner's Dilemma")
# choices = {1:'Betray', 0:'Collude'}
strategy_1 = input('Choose strategy for player #1 (R - Random, T - Tooth for Tooth, F - Forgiveness(THT)')
strategy_2 = input('Choose strategy for player #2 (R - Random, T - Tooth for Tooth, F - Forgiveness(THT)')

moves = []


def cycle(i=0, rounds=100, points_1=0.0, points_2=0.0, strat_1=strategy_1, strat_2=strategy_2):

    if i > rounds:
        print("There is a model of a Prisoner's Dilemma")
        # print(moves)
        print(f'1st player points - {points_1}, 2nd player points - {points_2}')

        if points_1 == points_2:
            print('Draw!')
        elif points_1 > points_2:
            number = 2
            print(f'Player #{number} wins!')
        else:
            number = 1
            print(f'Player #{number} wins!')

        print('=== END ===')
        return

    # strategies = (strat_1, strat_2)
    # for s in strategies:
    #     if s == 'r':
    #         strat_1 == Strategy(forgiveness)
    #     if s == 't':

    move_1 = forgiveness(moves)
    move_2 = tooth_for_tooth(moves)

    moves.append([move_1, move_2])

    if move_1 == 1 and move_2 == 1:
        points_1 += 0.5
        points_2 += 0.5
    elif move_1 == 0 and move_2 == 1:
        points_2 += 10
    elif move_1 == 1 and move_2 == 0:
        points_1 += 10
    else:
        points_1 += 2
        points_2 += 2
    i += 1
    cycle(i=i, points_1=points_1, points_2=points_2)


def random():
    import random
    return int(random.choice([True, False]))


def tooth_for_tooth(moves_local):
    if not moves_local:
        move = 0
    elif moves_local[-1][0] == 1:
        move = 1
    else:
        move = 0
    return move


def forgiveness(moves_local):
    if len(moves_local) < 2:
        move = tooth_for_tooth(moves_local)
    else:
        if moves_local[-2][0] == 0 and moves_local[-1][0] == 0:
            move = 0
        elif moves_local[-2][0] == 1:
            move = 1
        else:  # moves_local[-1][0] == 1 or moves_local[-1][0] == 0:
            move = 1

    return move

cycle()