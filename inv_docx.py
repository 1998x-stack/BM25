from typing import Dict, Tuple, List

class InvertedIndex:
    """
    Inverted Index 类用于构建倒排索引，记录词项在文档中的频率以及词项在整个索引中的频率。
    """

    def __init__(self):
        """
        初始化 InvertedIndex 对象。
        """
        self.index: Dict[str, Dict[str, int]] = {}

    def __contains__(self, item: str) -> bool:
        """
        检查词项是否存在于索引中。

        Args:
            item (str): 要检查的词项。

        Returns:
            bool: 如果词项存在于索引中，则返回 True，否则返回 False。
        """
        return item in self.index

    def __getitem__(self, item: str) -> Dict[str, int]:
        """
        获取指定词项的频率字典。

        Args:
            item (str): 要获取频率的词项。

        Returns:
            Dict[str, int]: 词项在各文档中的频率字典。
        """
        return self.index[item]

    def add(self, word: str, docid: str) -> None:
        """
        向倒排索引中添加词项及其在文档中的频率。

        Args:
            word (str): 要添加的词项。
            docid (str): 包含词项的文档ID。
        """
        if word in self.index:
            if docid in self.index[word]:
                self.index[word][docid] += 1
            else:
                self.index[word][docid] = 1
        else:
            self.index[word] = {docid: 1}

    def get_document_frequency(self, word: str, docid: str) -> int:
        """
        获取词项在指定文档中的频率。

        Args:
            word (str): 要查询的词项。
            docid (str): 包含词项的文档ID。

        Returns:
            int: 词项在文档中的频率。

        Raises:
            LookupError: 如果词项不存在于指定文档中或索引中。
        """
        if word in self.index:
            if docid in self.index[word]:
                return self.index[word][docid]
            else:
                raise LookupError(f'{word} 不存在于文档 {docid} 中')
        else:
            raise LookupError(f'{word} 不存在于索引中')

    def get_index_frequency(self, word: str) -> int:
        """
        获取词项在索引中的频率，即包含该词项的文档数量。

        Args:
            word (str): 要查询的词项。

        Returns:
            int: 词项在索引中的频率。

        Raises:
            LookupError: 如果词项不存在于索引中。
        """
        if word in self.index:
            return len(self.index[word])
        else:
            raise LookupError(f'{word} 不存在于索引中')


class DocumentLengthTable:
    """
    DocumentLengthTable 类用于记录每个文档的长度及平均文档长度。
    """

    def __init__(self):
        """
        初始化 DocumentLengthTable 对象。
        """
        self.table: Dict[str, int] = {}

    def __len__(self) -> int:
        """
        获取文档长度表的长度。

        Returns:
            int: 文档长度表的长度。
        """
        return len(self.table)

    def add(self, docid: str, length: int) -> None:
        """
        向文档长度表中添加文档ID及其长度。

        Args:
            docid (str): 要添加的文档ID。
            length (int): 文档的长度。
        """
        self.table[docid] = length

    def get_length(self, docid: str) -> int:
        """
        获取指定文档的长度。

        Args:
            docid (str): 要查询的文档ID。

        Returns:
            int: 指定文档的长度。

        Raises:
            LookupError: 如果指定文档ID不存在于表中。
        """
        if docid in self.table:
            return self.table[docid]
        else:
            raise LookupError(f'{docid} 未在表中找到')

    def get_average_length(self) -> float:
        """
        获取文档的平均长度。

        Returns:
            float: 文档的平均长度。
        """
        total_length = sum(self.table.values())
        return total_length / len(self.table)


def build_data_structures(corpus: Dict[str, List[str]]) -> Tuple[InvertedIndex, DocumentLengthTable]:
    """
    构建倒排索引和文档长度表。

    Args:
        corpus (Dict[str, List[str]]): 包含文档ID和对应词项列表的语料库。

    Returns:
        Tuple[InvertedIndex, DocumentLengthTable]: 倒排索引和文档长度表。
    """
    idx = InvertedIndex()
    dlt = DocumentLengthTable()

    for docid, words in corpus.items():
        # 构建倒排索引
        for word in words:
            idx.add(word, docid)

        # 构建文档长度表
        length = len(words)
        dlt.add(docid, length)

    return idx, dlt