from typing import List, Dict
from inv_docx import build_data_structures
from rank import score_BM25

class QueryProcessor:
    """
    QueryProcessor 类用于处理查询并返回相关文档的评分结果。
    """

    def __init__(self, queries: List[List[str]], corpus: Dict[str, List[str]]):
        """
        初始化 QueryProcessor 对象。

        Args:
            queries (List[List[str]]): 查询列表。
            corpus (Dict[str, List[str]]): 语料库，包含文档ID及对应的词项列表。
        """
        self.queries = queries
        self.index, self.dlt = build_data_structures(corpus)

    def run(self) -> List[Dict[str, float]]:
        """
        运行所有查询，并返回结果列表。

        Returns:
            List[Dict[str, float]]: 包含查询结果的列表，每个查询结果是一个字典，键为文档ID，值为评分。
        """
        results = []
        for query in self.queries:
            results.append(self.run_query(query))
        return results

    def run_query(self, query: List[str]) -> Dict[str, float]:
        """
        处理单个查询，并返回与之相关的文档评分结果。

        Args:
            query (List[str]): 单个查询的词项列表。

        Returns:
            Dict[str, float]: 与查询相关的文档评分结果，键为文档ID，值为评分。
        """
        query_result = dict()
        for term in query:
            if term in self.index:
                doc_dict = self.index[term]  # 获取词项的倒排索引条目
                for docid, freq in doc_dict.items():  # 遍历每个文档及其词频
                    score = score_BM25(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
                                       dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length())  # 计算评分
                    if docid in query_result:  # 文档已被评分过
                        query_result[docid] += score
                    else:
                        query_result[docid] = score
        return query_result