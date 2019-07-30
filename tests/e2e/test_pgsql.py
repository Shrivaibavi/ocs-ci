"""
Module to perform IOs with several weights
"""
import logging

from ocs_ci.framework.testlib import E2ETest, tier1

logger = logging.getLogger(__name__)


@tier1
class TestPgSQL(E2ETest):
    """
    Test PostgreSQL Workload
    """
    def test_workload(self):
        """
        Test PgSQL workload
        """

    # create a storageclass

    # pgsql_ripsaw_operator = RipSaw(crd='ripsaw_v1alpha1_ripsaw_crd.yaml')

    # deploy PostgreSQL

    # check Pods are Running

    # Run PGSQL_BENCHMARK

    # Verify Logs and assert here if numbers are not accurate
