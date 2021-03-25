from ocs_ci.ocs.node import get_node_objs
import pytest
import logging

from ocs_ci.framework.testlib import bugzilla, ManageTest

log = logging.getLogger(__name__)


class TestNode(ManageTest):
    """
    Resiliency Tests
    """

    @bugzilla("1754287")
    @pytest.mark.polarion_id("OCS-2015")
    def test_rolling_nodes_restart(
        self, nodes, pvc_factory, pod_factory, bucket_factory, rgw_bucket_factory
    ):
        """
        Test restart nodes one after the other and check health status in between

        """
        ocp_nodes = get_node_objs()
        i = 0
        while i <= 5:
            for node in ocp_nodes:
                nodes.restart_nodes(nodes=[node], wait=False)
                self.sanity_helpers.health_check(cluster_check=False, tries=60)
            self.sanity_helpers.create_resources(
                pvc_factory, pod_factory, bucket_factory, rgw_bucket_factory
            )
            i = i + 1
