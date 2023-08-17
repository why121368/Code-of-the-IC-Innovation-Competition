import matplotlib.pyplot as plt
import numpy as np

def voltage():
    v = [1]*11
    v1 = [2]*11
    v3 = [3]*11
    species = ("ch1", "ch2", "ch3","ch4","ch5","ch6","ch7","ch8","ch9","ch10","ch11")
    penguin_means = {
        'True value': v,
        'Test value': v1,
        'Error value': v3,
    }

    x = np.arange(len(species))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Voltage (V)')
    ax.set_title('Voltage detection function test results')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 4)

    fig.set_figheight(4)
    fig.set_figwidth(10)
    plt.savefig('voltage.png')

def Current():
    a = 4
    a1 = 5
    a3 =  1
    species = ("True value", "Test value", "Error value")
    penguin_means = {
        'True value': (a,a1,a3)
    }

    x = np.arange(len(species))  # the label locations
    width = 0.5  # the width of the bars
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Voltage (V)')
    ax.set_title('Voltage detection function test results')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 6)

    fig.set_figheight(4)
    fig.set_figwidth(6)
    plt.savefig('current.png')
    plt.show()

def wendu():
    a = 4
    a1 = 5
    a3 =  1
    species = ("True value", "Test value", "Error value")
    penguin_means = {
        'True value': (a,a1,a3)
    }

    x = np.arange(len(species))  # the label locations
    width = 0.5  # the width of the bars
    multiplier = 0
    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in penguin_means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Voltage (V)')
    ax.set_title('Voltage detection function test results')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 6)

    fig.set_figheight(4)
    fig.set_figwidth(6)
    plt.savefig('wendu.png')
    plt.show()


wendu()


