import unittest
import sys
sys.path.insert(1, "..")
from fast_docker_web.DockerComposerBuilder import DockerComposerBuilder

class test_DockerComposerBuilder(unittest.TestCase):

    def test_create_correct_string(self):
        expected_file_string = self.__get_sample_docker_compose_file_string()
        dockerComposeBuilder = DockerComposerBuilder()
        self.assertEqual(expected_file_string, dockerComposeBuilder.getDockerComposerFileString())

    def __get_sample_docker_compose_file_string(self):
        sample_file_yml = open('tests/sample_docker_compose_file.yml', 'r')
        file_string = sample_file_yml.read()
        sample_file_yml.close()
        return file_string
