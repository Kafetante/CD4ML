import pytest

from scripts import pipeline as pipeline_script


@pytest.mark.integration
class TestAlgorithms:

    def test_pipeline_houses_ridge(self):
        pipeline_script.main(['houses', 'tiny_for_testing', 'default', 'ridge', 'default'])

    def test_pipeline_houses_lasso(self):
        pipeline_script.main(['houses', 'tiny_for_testing', 'without_aggregated_prices', 'lasso', 'default'])

    def test_pipeline_houses_decision_tree(self):
        pipeline_script.main(['houses', 'tiny_for_testing', 'without_aggregated_prices', 'decision_tree', 'default'])

    def test_pipeline_houses_gradient_boosting(self):
        pipeline_script.main(
            ['houses', 'tiny_for_testing', 'without_aggregated_prices', 'gradient_boosting', 'default'])

    def test_pipeline_houses_random_forest(self):
        pipeline_script.main(['houses', 'tiny_for_testing', 'without_aggregated_prices', 'random_forest', 'default'])

    def test_pipeline_titanic_random_forest_classifier(self):
        pipeline_script.main(['titanic', 'default', 'default', 'random_forest_classifier', 'default'])
