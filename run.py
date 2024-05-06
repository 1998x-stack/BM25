from parse import QueryParser, CorpusParser
from query_process import QueryProcessor
import operator

def main():
    """
    主函数，用于处理查询并输出与查询相关的文档的评分结果。
    """
    # 解析查询
    qp = QueryParser(filename='text/queries.txt')
    qp.parse()
    queries = qp.get_queries()

    # 解析语料库
    cp = CorpusParser(filename='text/corpus.txt')
    cp.parse()
    corpus = cp.get_corpus()

    # 处理查询
    proc = QueryProcessor(queries, corpus)
    results = proc.run()

    # 输出结果
    qid = 0
    head = ('QueryId', 'DocumentId', 'Rank', 'Score')
    print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*head))
    print('---'*25)
    for result in results:
        sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
        index = 0
        
        for i in sorted_x[:100]:
            tmp = (qid, i[0], index, i[1])
            print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
            index += 1
        qid += 1
    print('---'*25)

if __name__ == '__main__':
    main()