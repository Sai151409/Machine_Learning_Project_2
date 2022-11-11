from collections import namedtuple

DataIngestionArtifact = namedtuple('DataIngestion Artifact', [
    'train_file_path', 'test_file_path', 'is_ingetsed', 'message'
])