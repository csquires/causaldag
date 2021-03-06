from unittest import TestCase
import sys
sys.path.insert(1, "C:/Users/skarn/OneDrive/Documents/MIT/year_3/SuperUROP/causaldag")
import unittest
import numpy as np
import subprocess
import causaldag as cd
from causaldag.utils.scores import local_gaussian_bge_score, MemoizedDecomposableScore
from causaldag.utils.ci_tests import partial_correlation_suffstat
# import ipdb


class TestBGEScore(TestCase):
    def test_1(self):
        samples = np.load("tests/data/bge_data/samples.npy")
        dag_amat = np.load("tests/data/bge_data/dag_amat.npy")
        dag = cd.DAG.from_amat(dag_amat)
        r_score = np.load("tests/data/bge_data/r_bge.npy")[0]
        suffstat = partial_correlation_suffstat(samples, invert=False)
        scorer = MemoizedDecomposableScore(local_gaussian_bge_score, suffstat)
        score = scorer.get_score(dag)
        print(" R:", r_score)
        print("us:", score)
        self.assertTrue(np.isclose(r_score, score))


if __name__ == '__main__':
    unittest.main()
