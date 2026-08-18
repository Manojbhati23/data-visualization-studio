from sklearn.linear_model import LinearRegression


def train_model(df, x, y):

    model = LinearRegression()

    model.fit(
        df[[x]],
        df[y]
    )

    prediction = model.predict([[10]])

    return prediction[0]