import pytest
import logging
from tests import helpers
from ocs_ci.ocs import constants
from ocs_ci.utility import templating
from ocs_ci.ocs.resources.ocs import OCS
from ocs_ci.framework.testlib import E2ETest, tier1

log = logging.getLogger(__name__)

SC_OBJ = None
PG_OBJ = None


@pytest.fixture(scope='class')
def test_fixture(request):
    """
    This is a test fixture
    """
    self = request.node.cls

    def finalizer():
        teardown()
    request.addfinalizer(finalizer)
    setup(self)


@tier1
class TestPGSQLWorkload(E2ETest):
    """
    Test PGSQL application workload
    """
    def test_run_pgbench(self):
        """
        Function to run pgbench
        """
        # Deployment Ripsaw, apply permissions and operator definitions
        # TO BE ADDED

        # Deployment Postgres
        # TO BE ADDED

        # Run pgbench
        run_pgbench(pg_client=2, pg_threads=1,
                    pg_transactions=10, pg_scaling_factor=1)

        # Check pgbench logs
        # TO DO: Add logs analysis and check for regression


def setup(self):
    """
    Create name space
    Create RBD storage class
    Create PVC
    """
    # Create name space
    # new_project = self.ocp.new_project(project_name='my-ripsaw')

    # Create storage class
    log.info("Creating a Storage Class")
    self.sc_data = templating.load_yaml_to_dict(
        constants.CSI_RBD_STORAGECLASS_YAML)
    self.sc_data['metadata']['name'] = helpers.create_unique_resource_name(
        'rook-ceph-block-extented', 'csi-rbd')

    global SC_OBJ
    SC_OBJ = OCS(**self.sc_data)
    assert SC_OBJ.create()
    log.info(f"Storage class name {SC_OBJ.name} created successfully")
    log.debug(self.sc_data)


def teardown():
    """
    Teardown the environment
    """
    # Delete Storage Class
    log.info(f"Deleting Storageclass: {SC_OBJ.name}")
    SC_OBJ.delete()
    log.info(f"Storage Class: {SC_OBJ.name} deleted successfully")

    # Delete pgbench benchmark resources
    log.info(
        f"Deleting pgbench benchmark: {PG_OBJ.name}"
    )
    PG_OBJ.delete()
    log.info(f"Pgbench benchmark: {PG_OBJ.name} deleted successfully")


def run_pgbench(pg_client, pg_threads,
                pg_transactions, pg_scaling_factor):
    """ 
    Create pgbench resource file
    """
    pg_data = templating.load_yaml_to_dict(constants.PGSQL_BENCHMARK)
    pg_data['spec']['workload']['args']['clients'] = pg_client
    pg_data['spec']['workload']['args']['threads'] = pg_threads
    pg_data['spec']['workload']['args']['transactions'] = pg_transactions
    pg_data['spec']['workload']['args']['scaling_factor'] = pg_scaling_factor
    log.info(
        f"Create resource file for pgbench workload"
    )
    global PG_OBJ
    PG_OBJ = OCS(**pg_data)
    PG_OBJ.create()
    log.info(f"PGbench data resource created successfully")
    log.debug(pg_data)

