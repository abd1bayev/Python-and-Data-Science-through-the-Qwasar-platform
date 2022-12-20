from sklearn.metrics import recall_score

def my_model_evaluation_journey_recall_score(param_1, param_2):
    return recall_score(param_1, param_2, average=None)

print(my_model_evaluation_journey_recall_score([2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2], [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]))