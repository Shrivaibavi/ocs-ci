from ocs_ci.ocs.node import get_node_objs
import pytest
import logging

from ocs_ci.helpers.sanity_helpers import Sanity
from ocs_ci.framework.testlib import bugzilla, ManageTest

log = logging.getLogger(__name__)


class TestNode(ManageTest):
    """
    Resiliency Tests
    """

    @pytest.fixture(autouse=True)
    def init_sanity(self):
        """
        Initialize Sanity instance

        """
        self.sanity_helpers = Sanity()

    @pytest.fixture(autouse=True)
    def teardown(self, request, nodes):
        """
        Make sure all nodes are up again

        """

        def finalizer():
            nodes.restart_nodes_by_stop_and_start_teardown()

        request.addfinalizer(finalizer)

    @bugzilla("1754287")
    @pytest.mark.polarion_id("OCS-2015")
    def test_rolling_nodes_restart(self, nodes):
        """
        Test restart nodes one after the other and check health status in between

        """
        ocp_nodes = get_node_objs()
        i = 0
        while i <= 5:
            for node in ocp_nodes:
                nodes.restart_nodes(nodes=[node], wait=False)
                self.sanity_helpers.health_check(cluster_check=False, tries=60)
            i = i + 1
