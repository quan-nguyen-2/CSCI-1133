def make_dictionary(key_lst, value_lst):
    dict = {}
    for i in range(len(key_lst)):
        dict[key_lst[i]] = value_lst[i]
    return dict


def get_score(name, score_dict):
    if name in list(score_dict.keys()):
        return score_dict[name]
    else:
        print("The name does not exist in the dictionary")
        return -1
        

def main():
    key_lst = ['joe', 'tom', 'barb', 'sue', 'sally']
    value_lst = [10, 23, 13, 18, 12]
    score_dict = make_dictionary(key_lst, value_lst)

    print(score_dict["barb"])

    score_dict["john"] = 19

    scores = list(score_dict.values())
    scores.sort()
    print(scores)

    total_score = 0
    for score in scores:
        total_score += score
    avg_scores = total_score // (len(scores))
    print(avg_scores)

    del score_dict["tom"]
    print(score_dict)

    score_dict["sally"] = 13
    print(score_dict["sally"])

    print(get_score("sally", score_dict))
    print(get_score("amy", score_dict))

if __name__=='__main__':
    main()
                     
