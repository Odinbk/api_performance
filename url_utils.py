import os
import itertools


_csv_files_location = '{}/cases/'.format(os.path.dirname(os.path.abspath('__file__')))


class Source(object):
    file_name = None
    header = {}
    urls = None


def _urls(file_name):
    def _url_iter(param):
        with open(param, 'r') as file:
            file.readline()
            for line in file.readlines():
                yield line.strip()
    cycle_iterator = itertools.cycle(_url_iter(file_name))
    return cycle_iterator


def _get_header(file_name):
    with open(file_name, 'r') as file:
        header_str = file.readline().strip()
    header = dict([tuple(item.split(':')) for item in header_str.split(';')])
    return header


def get_sources(dir_path):
    sources = []
    if os.path.isdir(dir_path):
        for file_name in os.listdir(dir_path):
            if file_name.endswith(".txt") and ('url' in file_name):
                source = Source()
                source.file_name = file_name
                source.header = _get_header(dir_path + file_name)
                source.urls = _urls(dir_path + file_name)
                sources.append(source)
            else:
                break
    else:
        raise IOError("can not found {}".format(dir_path))

    return sources


sources = get_sources(_csv_files_location)
