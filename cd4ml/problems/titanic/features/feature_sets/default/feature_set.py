from cd4ml.feature_set import FeatureSetBase
# import cd4ml.problems.iris.features.feature_functions.feature_functions as ff
from cd4ml.utils.feature_utils import get_generic_feature_set, get_feature_params
import re


def get_feature_set_params():
    return get_feature_params(__file__)


def get_feature_set(identifier_field,
                    target_field,
                    info):

    return get_generic_feature_set(identifier_field,
                                   target_field,
                                   info,
                                   __file__,
                                   FeatureSet)


class FeatureSet(FeatureSetBase):
    def __init__(self, identifier_field,
                 target_field,
                 info,
                 feature_set_params):

        super(FeatureSet, self).__init__(identifier_field, target_field)
        self.info = info
        self.params = feature_set_params.copy()

    # actually derive the fields

    def derived_features_categorical(self, base_features):
        features = {'deck':  base_features['cabin'][0],
                    'title': re.sub('.* ([A-Za-z]+)?\\..*', '\\1', base_features.get('name',''))}
        return {k: features[k] for k in self.params['derived_categorical_n_levels_dict'].keys()}

    def derived_features_numerical(self, base_features):
        features = {'age_decades':  base_features['age'] // 10}
        return {k: features[k] for k in self.params['derived_fields_numerical']}
