import re, fire, json

ALPHA_MAP = ["A", "B", "C", "D"]
def judge_answer(text, choices, answer):
    if isinstance(answer, int):
        answer = ALPHA_MAP[answer]
    if "[Answer]" in text:
        text = text.split("ANSWER:")[-1]
    pattern = re.compile(r'\(([A-Za-z])\)')
    res = pattern.findall(text)
    if len(res) >= 1:
        pred = res[-1].upper()  # 'A', 'B', ...
    else:
        res = []
        for i, choice in enumerate(choices):
            if str(choice).lower() in text.lower():
                res.append(ALPHA_MAP[i])
        if len(res) >= 1:
            pred = res[-1]
        else:
            for i, choice in enumerate(choices):
                text = re.sub(r'[\n.,!?]', ' ', text)
                if ALPHA_MAP[i] in text.split(" "):
                    res.append(ALPHA_MAP[i])
            if len(res) >= 1:
                pred = res[-1]
            else:
                for i, choice in enumerate(choices):
                    text = re.sub(r'[\n.,!?]', ' ', text)
                    if ALPHA_MAP[i].lower() in text.split(" "):
                        res.append(ALPHA_MAP[i])
                if len(res) >= 1:
                    pred = res[-1]
                else:
                    pred = "FAILED"
    
    if pred == answer:
        return True
    else:
        return False
    
def run(data_path, metric_path):
    dataDict = {}
    with open(data_path, "r", encoding='utf-8') as f:
        for fd in f:
            d = json.loads(fd)
            dataDict[d["id"]] = d   
    metricList = []
    with open(metric_path, "r", encoding='utf-8') as f:
        for fm in f:
            metricList.append(json.loads(fm))

    sum_comt = {"creation": 0, "deletion": 0, "update": 0, "selection": 0}
    correct_comt = {"creation": 0, "deletion": 0, "update": 0, "selection": 0}
    for md in metricList:
        gt = dataDict[md["id"]]["answer"]
        choices = dataDict[md["id"]]["option"]
        response = md["response"]
        judgment = judge_answer(response, choices, gt)
        if judgment:
            correct_comt[dataDict[md["id"]]["type"]] += 1
        sum_comt[dataDict[md["id"]]["type"]] += 1

    for type in sum_comt.keys():
        print(f"Type: {type}")
        print(f'Total: {sum_comt[type]}, Correct: {(correct_comt[type]/sum_comt[type])*100.0:.2f}%')


"""
python evaluate.py -- data_path [COMT_PATH]\
                   -- metric_path [JSON_PATH]

"""
if __name__ == "__main__":
    fire.Fire(run)