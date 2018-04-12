def view_highscores(name=[],new_score=[]):          #Function opens the scores.txt file, takes the data in, saves it as a two-element list
    if name != []:                                  #Then it assigns a position to each element based on when they were opened, then it puts
                                                    #the elements into a list of strings containing [position] [name] [score]
        score_list = [[name,new_score]]
    else:
        score_list = []
    with open("scores.txt","r") as all_scores:
        scores = all_scores.read()
        scores = scores.split("|")
        for person in range(len(scores)):
            scores[person] = scores[person].strip("\n")
            score_list.append(scores[person].split(","))
    score_list.remove([""])
    all_scores.close
    final_scores = []
    for i in range(10):
        high_score = ["000","0"]
        for score in range(len(score_list)):
            if int(score_list[score][1]) > int(high_score[1]):
                high_score = score_list[score]
        if high_score != ["000","0"]:
            final_scores.append(high_score)
            score_list.remove(high_score)
    spot = 1
    for i in final_scores:
        i.append(str(spot))
        spot += 1
    true_final_scores = []         
    for i in final_scores:
        true_final_scores.append(i[2] +" " + i[0] + " " + i[1])
   
    return true_final_scores
        

def save_highscores(list_of_scores):
    score_to_file = ""                  #This saves all the junk the other function opened back into the scores.txt file.
    for score in list_of_scores:
        if score[1] == '0':
            score = score[3:]
        else:
            score = score[2:]

        score_to_file += (score[0:3] + "," + score[4:] + "|\n")
    with open("scores.txt","w") as all_scores:
        all_scores.write(str(score_to_file))

