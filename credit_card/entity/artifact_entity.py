from collections import namedtuple

DataIngestionArtifact = namedtuple('DataIngestionArtifact', [
    'train_file_path', 'test_file_path', 'is_ingested', 'message'
])

DataValidationArtifact = namedtuple('DataValidationArtifact', [
    'validated_train_file_path', 'validated_test_file_path',
    'schema_file_path', 'report_file_path', 
    'report_page_file_path', 'is_validated', 'message'
])