def rank_suit_count(cards):
    rank_dict = {}
    suit_dict = {}

    rank_list = []
    suit_list = []

    for card in cards:
        rank_list.append(card[0])
        suit_list.append(card[1])
    for card_rank in rank_list:
        if card_rank not in rank_dict:
            rank_dict[card_rank] = 0
        rank_dict[card_rank] += 1

    for card_suit in suit_list:
        if card not in suit_dict:
            suit_dict[card_suit] = 0
        suit_dict[card_suit] += 1
    return rank_dict, suit_dict

rank, suit = rank_suit_count([ 'AS', 'AD', '2C', 'TH', 'TS'])

print(rank)
print(suit)
        
