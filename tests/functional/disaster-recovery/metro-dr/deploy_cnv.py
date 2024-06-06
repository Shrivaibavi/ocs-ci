import logging

from ocs_ci.deployment.cnv import CNVInstaller
from ocs_ci.framework.pytest_customization.marks import tier2
from ocs_ci.framework import config

from ocs_ci.framework.pytest_customization.marks import turquoise_squad
from ocs_ci.ocs.utils import get_non_acm_cluster_config

logger = logging.getLogger(__name__)

polarion_id_cnv_primary_up = "OCS-5413"
polarion_id_cnv_primary_down = "OCS-5414"


@tier2
@turquoise_squad
class TestCnvInstall:
    """
    Includes tests related to CNV workloads on MDR environment.
    """

    def test_install_cnv(
        self,
    ):
        for cluster in get_non_acm_cluster_config():
            config.switch_ctx(cluster.MULTICLUSTER["multicluster_index"])
            CNVInstaller().deploy_cnv()
