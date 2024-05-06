import re
from typing import List, Dict

class CorpusParser:
    """
    CorpusParser 类用于解析语料库文件，提取文档和对应的词项列表。
    """

    def __init__(self, filename: str):
        """
        初始化 CorpusParser 对象。

        Args:
            filename (str): 语料库文件名。
        """
        self.filename = filename
        self.regex = re.compile('^#\s*\d+')
        self.corpus: Dict[str, List[str]] = {}

    def parse(self) -> None:
        """
        解析语料库文件，提取文档和对应的词项列表。
        """
        with open(self.filename) as f:
            s = ''.join(f.readlines())
        blobs = s.split('#')[1:]
        for x in blobs:
            text = x.split()
            docid = text.pop(0)
            self.corpus[docid] = text

    def get_corpus(self) -> Dict[str, List[str]]:
        """
        获取解析后的语料库。

        Returns:
            Dict[str, List[str]]: 文档ID及对应的词项列表。
        """
        return self.corpus


class QueryParser:
    """
    QueryParser 类用于解析查询文件，提取查询列表。
    """

    def __init__(self, filename: str):
        """
        初始化 QueryParser 对象。

        Args:
            filename (str): 查询文件名。
        """
        self.filename = filename
        self.queries: List[List[str]] = []

    def parse(self) -> None:
        """
        解析查询文件，提取查询列表。
        """
        with open(self.filename) as f:
            lines = ''.join(f.readlines())
        self.queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]

    def get_queries(self) -> List[List[str]]:
        """
        获取解析后的查询列表。

        Returns:
            List[List[str]]: 查询列表。
        """
        return self.queries


if __name__ == '__main__':
    qp = QueryParser('text/queries.txt')
    qp.parse()
    print(qp.get_queries())
    
    cp = CorpusParser('text/corpus.txt')
    cp.parse()
    print(cp.get_corpus())