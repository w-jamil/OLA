import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt
from base import BaseModel
from sklearn.metrics import classification_report
# from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix


parser = argparse.ArgumentParser(description="Run the PAL algorithm in sequential mode")

parser.add_argument("--data-file", default='uc2.txt', type=str,
                    help="path of the data file")

class PALNT(BaseModel):
    """This class implements Online PAL with no tuning parameter. 
    """

    def __init__(self, n):
        super(PALNT, self).__init__(n)

    def delta(self, x, y):
        self.w = self.w + (1-y*np.sign(self.w.dot(x)))/x.dot(x)**.5*y*x
        return {'w': self.w}

    def predict(self, x):
        pred = np.sign(self.w.dot(x))
        return pred.item(0)

    
if __name__ == "__main__":
    args = parser.parse_args()

    array = np.loadtxt(args.data_file, delimiter=' ')
    n = len(array[0][:-1])
    f1_score = []
    model = PALNT(n)
    y_pred = np.ones(len(array))
    y_vec = np.ones(len(array))
    for i, a in enumerate(array):
        x, y = a[:-1], a[-1]
        new_y = model.predict(x)
        y_pred[i] = new_y
        y_vec[i] = y
        model.delta(x, y)
        if i>102:
            report = classification_report(pd.Series(y_vec).iloc[1:i].astype(float),pd.Series(y_pred).iloc[1:i].astype(float), output_dict=True)
            categories = list(report.keys())[:-3]
            f1_score.append([report[category]['f1-score'] for category in categories])

    loss = pd.DataFrame(f1_score)
    loss = loss.dropna(axis=0).reset_index(drop=True)
    loss.columns = ["Benign","Malicious"]
    plt.plot(loss)
    plt.show()


    report = classification_report(y_vec[1:].astype(float),pd.Series(y_pred[1:]), output_dict=True)
    # Categories for the classification
    categories = list(report.keys())[:-3]  # Exclude 'accuracy', 'macro avg', and 'weighted avg'

    # Extracting precision, recall, and f1-score
    precision = [report[category]['precision'] for category in categories]
    recall = [report[category]['recall'] for category in categories]
    f1_score = [report[category]['f1-score'] for category in categories]

    # Setting the positions and width for the bars
    pos = list(range(len(categories)))
    width = 0.25

    # Setting the positions and width for the bars
    pos = list(range(len(categories)))
    width = 0.25

    # Plotting each metric
    plt.bar(pos, precision, width, alpha=0.5, color='red', label='Precision')
    plt.bar([p + width for p in pos], recall, width, alpha=0.5, color='blue', label='Recall')
    plt.bar([p + width*2 for p in pos], f1_score, width, alpha=0.5, color='green', label='F1-Score')

    # Adding the aesthetics
    plt.xlabel('Category')
    plt.ylabel('Score')
    plt.title('Classification Report')
    plt.xticks([p + width for p in pos], categories)
    plt.xticks(pos, ["Benign","Malicious"])
    plt.legend(['Precision', 'Recall', 'F1-Score'], loc='upper left')
    plt.grid()
    plt.show()

    # cm = confusion_matrix(y_vec[1:].astype(float),pd.Series(y_pred[1:]),labels=[-1,1])
    # disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=["Benign","Malicious"])

    # print(cm)

    # disp.plot()

