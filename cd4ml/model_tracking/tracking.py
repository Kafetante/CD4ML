import json
import logging

from cd4ml.filenames import get_model_files


class Track:
    def __init__(self, model_id, specification):
        self.specification = specification
        self.model_id = model_id
        self.logger = logging.getLogger(__name__)
        self.model = None
        self.encoder = None
        self.params = dict()
        self.metrics = dict()
        self.validation_plot = None
        self.confusion_matrix_plot = None

    def save_results(self):
        filenames = get_model_files(self.model_id)
        self.logger.info("Recording run information for model %s" % self.model_id)

        if self.model is not None:
            self.model.save(filenames['full_model'])

        if self.validation_plot is not None:
            import bokeh.plotting as bokeh_saver
            bokeh_saver.save(obj=self.validation_plot,
                             filename=filenames['validation_plot'],
                             title='Validation Plot')
        if self.confusion_matrix_plot is not None:
            self.confusion_matrix_plot.savefig(filenames['confusion_matrix'])
        self._write_dictionary_to_file(self.params, filenames['ml_pipeline_params'])
        self._write_dictionary_to_file(self.metrics, filenames['model_metrics'])
        self._write_dictionary_to_file(self.specification, filenames['model_specification'])
        if self.encoder is not None:
            self.encoder.save(filenames['encoder'])

    def log_param(self, key, val):
        self.params[key] = val

    def log_algorithm_params(self, ml_params):
        for key, val in ml_params.items():
            self.log_param(key, val)

    def log_ml_pipeline_params(self, ml_pipeline_params):
        excluded_keys = ['download_data_info']
        for key, val in ml_pipeline_params.items():
            if key not in excluded_keys:
                self.log_param(key, val.__repr__())

    def log_metrics(self, metrics):
        for key, val in metrics.items():
            self.metrics[key] = val

    def log_model(self, model, encoder):
        self.model = model
        self.encoder = encoder

    def log_validation_plot(self, plot):
        self.validation_plot = plot

    def log_confusion_matrix(self, confusion_matrix):
        self.confusion_matrix_plot = confusion_matrix

    def _write_dictionary_to_file(self, dict_to_write, output_file_name):
        if len(dict_to_write) == 0:
            return
        with open(output_file_name, 'w') as file:
            json.dump(dict_to_write, file, indent=4)
