from random import randint

def dice_game(player=1, number_of_rolls=100):
    dice_dict={1:0,2:0,3:0,4:0,5:0,6:0}
    total_score=0

    for r in range(number_of_rolls):
        n_rolled=randint(1,6)
        dice_dict[n_rolled]+=1
        total_score+=n_rolled

    line='='*9
    line="#"*9

    print("\n{} \n Player {}:\n{}\n{}".format(line ,player,line,dice_dict))
    print("\nTotal score: {}\n{}".format(total_score,"="*16))

    return total_score

def print_result(Score_1,Score_2):
    line_result="="*32
    print("\n Result: \n"+line_result)

    if Score_1>Score_2:
        print("player 1 won!")
    elif Score_1<Score_2:
        print("player 2 won!")
        
    else:
        print("Tie")

    print(line_result)

def play_one_game():
    Score_1=dice_game(player=1)
    Score_2=dice_game(player=2)

    print_result(Score_1,Score_2)

    return Score_1,Score_2



play_one_game()