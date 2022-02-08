from scripts import pipeline as pipeline_script


class TestAlgorithms:

    def test_pipeline_houses_ridge(self):
        pipeline_script.main(['houses', 'default', 'minimal', 'ridge', 'default'])

    def test_pipeline_houses_lasso(self):
        pipeline_script.main(['houses', 'default', 'minimal', 'lasso', 'default'])

    def test_pipeline_houses_decision_tree(self):
        pipeline_script.main(['houses', 'default', 'minimal', 'decision_tree', 'default'])

    def test_pipeline_houses_gradient_boosting(self):
        pipeline_script.main(
            ['houses', 'default', 'minimal', 'gradient_boosting', 'default'])

    def test_pipeline_houses_random_forest(self):
        pipeline_script.main(['houses', 'default', 'minimal', 'random_forest', 'default'])

    def test_pipeline_titanic_random_forest_classifier(self):
        pipeline_script.main(['titanic', 'default', 'default', 'random_forest_classifier', 'default'])

    def test_pipeline_titanic_decision_tree_classifier(self):
        pipeline_script.main(['titanic', 'default', 'default', 'decision_tree_classifier', 'default'])

    def test_pipeline_titanic_svc_classifier(self):
        pipeline_script.main(['titanic', 'default', 'default', 'svc_classifier', 'default'])
