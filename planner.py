from model import train_model, predict_priority

def create_schedule(subjects):
    model = train_model()   # moved inside function (important)

    result = []

    for name, difficulty, days in subjects:
        if name.strip() == "":
            continue

        priority = predict_priority(model, difficulty, days)
        result.append((name, difficulty, days, priority))

    result.sort(key=lambda x: x[3], reverse=True)
    return result