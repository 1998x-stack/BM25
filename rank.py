from math import log

K1 = 1.2
K2 = 100
B = 0.75
R = 0.0

def score_BM25(n: int, f: int, qf: int, r: int, N: int, dl: int, avdl: float) -> float:
    """
    计算BM25分数。

    Args:
        n (int): 包含词项的文档数量。
        f (int): 词项在文档中的频率。
        qf (int): 查询中词项的频率。
        r (int): 与查询相关的文档数量。
        N (int): 文档总数。
        dl (int): 文档长度。
        avdl (float): 平均文档长度。

    Returns:
        float: BM25分数。
    """
    K = compute_K(dl, avdl)
    first = log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
    second = ((K1 + 1) * f) / (K + f)
    third = ((K2 + 1) * qf) / (K2 + qf)
    return first * second * third

def compute_K(dl: int, avdl: float) -> float:
    """
    计算调节参数 K。

    Args:
        dl (int): 文档长度。
        avdl (float): 平均文档长度。

    Returns:
        float: 调节参数 K。
    """
    return K1 * ((1 - B) + B * (float(dl) / float(avdl)))