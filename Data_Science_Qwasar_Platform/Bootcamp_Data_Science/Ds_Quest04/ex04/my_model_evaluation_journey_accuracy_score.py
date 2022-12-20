from sklearn.metrics import accuracy_score

def my_model_evaluation_journey_accuracy_score(param_1, param_2):
    return accuracy_score(param_1, param_2)

print(my_model_evaluation_journey_accuracy_score([2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2], [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]))