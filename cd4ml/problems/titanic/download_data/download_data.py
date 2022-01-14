from cd4ml.filenames import get_problem_files
from cd4ml.utils.utils import download_to_file_from_url

download_params = {
                    'url': "https://www.openml.org/data/get_csv/16826755/phpMYEkMl"
                   }


def download(use_cache=False):
    url = download_params['url']
    file_names = get_problem_files("titanic")
    filename = file_names['raw_titanic_data']

    download_to_file_from_url(url, filename, use_cache=use_cache)
