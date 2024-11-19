import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import argparse
import matplot
from simdata import Dataset
from batchpa import BatchPA


class PassiveAggressiveOne(BatchPA):
    def __init__(self, c=0.1):
        self.c = c
        BatchPA.__init__(self)

    def calc_eta(self, loss, vec_x):
        l2_norm = vec_x.dot(vec_x)
        return min(self.c, loss/l2_norm)


class PassiveAggressiveTwo(BatchPA):
    def __init__(self, c=0.1):
        self.c = c
        BatchPA.__init__(self)

    def calc_eta(self, loss, vec_x):
        l2_norm = vec_x.dot(vec_x)
        return loss/(l2_norm+1/(2*self.c))



def main():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', type=int, default=0)
    args = parser.parse_args()
    is_recorded = args.record

    train_dataset = Dataset(total_num=250, is_confused=True,x=3,y=5,seed=1)
    test_dataset  = Dataset(total_num=100,is_confused=False,x=3,y=5,seed=2)

    model_PA = BatchPA()
    model_PA_one = PassiveAggressiveOne(0.05)

    fig = plt.figure(figsize=(20, 4))
    gs = gridspec.GridSpec(1,10)
    fig_left  = fig.add_subplot(gs[0,:3])
    fig_right = fig.add_subplot(gs[0,4:])

    fig_left.set_xlim([train_dataset.dataset.x1.min() - 0.1, train_dataset.dataset.x1.max() + 0.1])
    fig_left.set_ylim([train_dataset.dataset.x2.min() - 0.1, train_dataset.dataset.x2.max() + 0.1])
    fig_left.set_title("Input Data & Trained Boundary", fontsize=15)
    fig_left.tick_params(labelsize=10)

    fig_right.set_xlim([0, len(train_dataset.y)])
    fig_right.set_ylim([0,1])
    fig_right.set_title("Test Accuracy", fontsize=15)
    fig_right.tick_params(labelsize=10)
    fig_right.set_xlabel("Number of training data", fontsize=12)
    fig_right.set_ylabel("Accuracy", fontsize=12)

    line_x = np.array(range(-10, 10, 1))
    line_y = line_x*0
    line_PA,     = fig_left.plot(line_x, line_y, color="blue", label="Benchmark"  )
    line_PA_one, = fig_left.plot(line_x, line_y, color="red", label="WAPA")

    fig_left.legend(handles=[line_PA, line_PA_one], fontsize=12)
    fig_right.legend(handles=[line_PA, line_PA_one], fontsize=12)

    valid_result_sample = []
    accuracies_PA = []
    accuracies_PA_one = []
    imgs = []

    for i in range(len(train_dataset.y)):
        fig_left.scatter(x=train_dataset.dataset.x1[i], y=train_dataset.dataset.x2[i], color=cm.cool(train_dataset.dataset.label[i]), alpha=0.5)

        model_PA.fit(train_dataset.feature_vec[i], train_dataset.y[i])
        model_PA_one.fit(train_dataset.feature_vec[i], train_dataset.y[i])

        accuracies_PA.append(test_dataset.valid_training_result(model_PA))
        accuracies_PA_one.append(test_dataset.valid_training_result(model_PA_one))

        a, b, c = model_PA.w
        line_y = (a*line_x + c)/(-b)
        line_PA.set_data(line_x, line_y)

        a, b, c = model_PA_one.w
        line_y = (a*line_x + c)/(-b)
        line_PA_one.set_data(line_x, line_y)#c="#2980b9" "#e74c3c"

        fig_right.plot(accuracies_PA,color="blue", label="Benchmark"  )
        fig_right.plot(accuracies_PA_one,color="red", label="WAPA")

        plt.pause(0.005)

        if is_recorded == 1:
            matplot.save_frame()

    if is_recorded == 1:
        matplot.save_movie("results.mp4", 0.005)



if __name__ == '__main__':
    main()
