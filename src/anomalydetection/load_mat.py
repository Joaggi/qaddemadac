import scipy.io
from sklearn.model_selection import train_test_split
from convert_dataset import convert_dataset

def load_mat_file(path, algorithm):

    data = scipy.io.loadmat(path)
    features = data["X"]
    labels = data["y"]

    pos_label = 0

    y = convert_dataset(labels, pos_label, algorithm)

    X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.3, random_state=42, stratify=y)

    return X_train, y_train, X_test, y_test
