import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


def line_chart(df, x, y):
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y], marker="o")
    ax.set_title(f"{y} vs {x}")
    return fig


def scatter_chart(df, x, y):
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    ax.set_title("Scatter Plot")
    return fig


def bar_chart(df, x, y):
    fig, ax = plt.subplots()
    ax.bar(df[x], df[y])
    ax.set_title("Bar Chart")
    return fig


def histogram(df, y):
    fig, ax = plt.subplots()
    ax.hist(df[y], bins=20)
    ax.set_title("Histogram")
    return fig


def boxplot(df, y):
    fig, ax = plt.subplots()
    ax.boxplot(df[y])
    ax.set_title("Boxplot")
    return fig


def heatmap(df):
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    return fig


def scatter_3d(df, x, y, z):
    fig = plt.figure(figsize=(8, 6))

    ax = fig.add_subplot(
        111,
        projection='3d'
    )

    ax.scatter(
        df[x],
        df[y],
        df[z],
        c=df[z],
        cmap='viridis'
    )

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)

    return fig