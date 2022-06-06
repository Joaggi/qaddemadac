import numpy as np
from sklearn.ensemble import IsolationForest

from calculate_metrics import calculate_metrics


def experiment_isolation(X_train, y_train, X_test, y_test, settings, mlflow, best=False):
    
    for i, setting in enumerate(settings):

        #print(f"experiment_dmkdc {i} setting {setting}")
        with mlflow.start_run(run_name=setting["z_run_name"]):

            model = IsolationForest(n_estimators=setting["z_n_estimators"], max_samples=setting["z_max_samples"], 
                                    contamination=setting["z_nu"], random_state=setting["z_random_state"])
            model.fit(X_train)
            y_test_pred = model.predict(X_test)
            y_scores = model.decision_function(X_test)

            metrics = calculate_metrics(y_test, y_test_pred)

            mlflow.log_params(setting)
            mlflow.log_metrics(metrics)

            if best:
                np.savetxt(('artifacts/'+setting["z_name_of_experiment"]+'-preds.csv'), y_test_pred, delimiter=',')
                mlflow.log_artifact(('artifacts/'+setting["z_name_of_experiment"]+'-preds.csv'))
                np.savetxt(('artifacts/'+setting["z_name_of_experiment"]+'-scores.csv'), y_scores, delimiter=',')
                mlflow.log_artifact(('artifacts/'+setting["z_name_of_experiment"]+'-scores.csv'))

            print(f"experiment_dmkdc {i} metrics {metrics}")