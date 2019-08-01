"""
Module to perform IOs with several weights
"""
import logging
import pytest

from ocs_ci.framework.testlib import E2ETest, tier1
from ocs_ci.ocs import constants
from ocs_ci.utility import templating
from ocs_ci.ocs.resources.ocs import OCS
from tests import helpers

log = logging.getLogger(__name__)

SC_OBJ = None
cr_obj = None


@pytest.fixture(scope='class')
def test_fixture(request):
    """
    This fixture defines the teardown function.
    """
    request.addfinalizer(teardown)


def teardown():
    """
    Tearing down the environment

    """
    log.info(
        f"Deleting created storage class: {SC_OBJ.name}"
    )
    SC_OBJ.delete()

    log.info(
        f"Deleting created pgbench pod: {cr_obj.name}"
    )
    cr_obj.delete()


def create_storageclass(sc_name, sc_namespace):
    """
    Function to create storageclass with specific
    storageclass name and namespace

    """
    sc_data = templating.load_yaml_to_dict(constants.PGSQL_STORAGECLASS)
    sc_data['metadata']['name'] = sc_name
    sc_data['parameters']['clusterNamespace'] = sc_namespace

    global SC_OBJ
    SC_OBJ = OCS(**sc_data)
    SC_OBJ.create()
    log.info(
        f"Storage class: {SC_OBJ.name} created successfully !"
    )



def run_pqbench_workload(cr_client, cr_threads,
                         cr_transactions, cr_scaling_factor):
    """
    Function to create resource file and
    run pgbench workload
    """
    cr_data = templating.load_yaml_to_dict(constants.PGBENCH_CR)
    cr_data['spec']['workload']['arg']['clients'] = cr_client
    cr_data['spec']['workload']['arg']['threads'] = cr_threads
    cr_data['spec']['workload']['arg']['transactions'] = cr_transactions
    cr_data['spec']['workload']['arg']['scaling_factor'] = cr_scaling_factor

    log.info(
        f"Create resource file for pgbench workload"
    )
    global cr_obj
    cr_obj = OCS(**cr_data)
    cr_obj.create()
    assert helpers.wait_for_resource_state(cr_obj, constants.STATUS_BOUND)


@tier1
class TestPgSQL(E2ETest):
    """
    Test PostgreSQL Workload
    """
    def test_pgsql_workload(self):
        """
        Test PgSQL workload
        """
    # create a storageclass
        create_storageclass(sc_name='rook-ceph-block-extented',
                            sc_namespace='my-ripsaw')

    # Deploy ripsaw framework
    # pgsql_ripsaw_operator = RipSaw(crd='ripsaw_v1alpha1_ripsaw_crd.yaml')
    # check for benchmark operator is created
        log.info(
            f"Verify benchmark operator is created and running"
        )
    #    assert helpers.wait_for_resource_state(pgsql_ripsaw_operator, constants.STATUS_RUNNING)

    # deploy PostgreSQL
    # check postgres database is created
        log.info(
            f"Verify Postgres database is created and running"
        )
    #    assert helpers.wait_for_resource_state(postgres, constants.STATUS_RUNNING)

    # Run PGSQL_BENCHMARK
        run_pqbench_workload(cr_client=2, cr_threads=1,
                             cr_transactions=10, cr_scaling_factor=1)

    # Verify Logs and assert here if numbers are not accurate
