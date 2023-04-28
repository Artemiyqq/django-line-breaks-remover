from abc import ABC, abstractmethod
from io import BytesIO
from tempfile import TemporaryFile
from zipfile import BadZipFile

import charset_normalizer
import docx


class FileProcessor(ABC):
    @abstractmethod
    def get_text(file_content: bytes) -> str:
        pass


class WordProcessor(FileProcessor):
    @staticmethod
    def get_text(file_content: bytes) -> str:
        try:
            doc = docx.Document(BytesIO(file_content))
            return ' '.join([paragraph.text for paragraph in doc.paragraphs])
        except (BadZipFile, ValueError):
            return StandartProcessor.get_text(file_content)


class StandartProcessor(FileProcessor):
    @staticmethod
    def get_text(file_content: bytes):
        encoding = get_encoding(file_content)
        if encoding:
            return file_content.decode(encoding)
        return False


def get_encoding(file_content: bytes) -> str:
    return charset_normalizer.detect(file_content)['encoding']


def determine_suitable_processor(file_name: str) -> object:
    extension = file_name.split('.')[-1].lower()
    if extension == 'docx' or extension == 'doc':
        return WordProcessor()
    elif extension == 'txt' or extension == 'rtf':
        return StandartProcessor()
    else:
        raise TypeError('Invalid file type')


def get_file_content(file):
    with TemporaryFile() as tmp:
        for chunk in file.chunks():
            tmp.write(chunk)
            tmp.seek(0)
        return tmp.read()


def get_text_from_file(file, file_name: str) -> str:
    unprocessed_content = get_file_content(file)
    file_processor = determine_suitable_processor(file_name)
    return file_processor.get_text(unprocessed_content)
