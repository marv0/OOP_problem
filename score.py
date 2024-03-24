def calculate_score(participants):
    scores = []
    for participant in participants:
        name = participant['name']
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scores.append({'name': name, 'score': score})
    
    
    sorted_scores = sorted(scores, key=lambda x: (-x['score'], x['name']))
    
    return sorted_scores