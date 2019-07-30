"""
Constants module.

This module contains any values that are widely used across the framework,
utilities, or tests that will predominantly remain unchanged.

In the event values here have to be changed it should be under careful review
and with consideration of the entire project.

"""
import os

# Directories
TOP_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
TEMPLATE_DIR = os.path.join(TOP_DIR, "ocs_ci", "templates")
TEMPLATE_DEPLOYMENT_DIR = os.path.join(TEMPLATE_DIR, "ocs-deployment")
TEMPLATE_CSI_DIR = os.path.join(TEMPLATE_DIR, "CSI")
TEMPLATE_CSI_RBD_DIR = os.path.join(TEMPLATE_CSI_DIR, "rbd")
TEMPLATE_CSI_FS_DIR = os.path.join(TEMPLATE_CSI_DIR, "cephfs")
TEMPLATE_PV_PVC_DIR = os.path.join(TEMPLATE_DIR, "pv_pvc")
TEMPLATE_APP_POD_DIR = os.path.join(TEMPLATE_DIR, "app-pods")
TEMPLATE_WORKLOAD_DIR = os.path.join(TEMPLATE_DIR, "workloads")
TEMPLATE_FIO_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "fio")
TEMPLATE_PGSQL_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "pgsql")
TEMPLATE_CONFIGURE_PVC_MONITORING_POD = os.path.join(
    TEMPLATE_DIR, "openshift-infra/monitoring/"
)

# Statuses
STATUS_PENDING = 'Pending'
STATUS_AVAILABLE = 'Available'
STATUS_RUNNING = 'Running'
STATUS_TERMINATING = 'Terminating'
STATUS_BOUND = 'Bound'
STATUS_RELEASED = 'Released'

# Resources / Kinds
CEPHFILESYSTEM = "CephFileSystem"
CEPHBLOCKPOOL = "CephBlockPool"
STORAGECLASS = "StorageClass"
PV = "PersistentVolume"
PVC = "PersistentVolumeClaim"
POD = "Pod"
ROUTE = "Route"
NODE = "Node"

# Provisioners
AWS_EFS_PROVISIONER = "openshift.org/aws-efs"

# Other
SECRET = "Secret"
NAMESPACE = 'Namespace'
IGNORE_SC_GP2 = "gp2"
IGNORE_SC_FLEX = "rook-ceph-block"


DEFAULT_BLOCKPOOL = 'rbd'
# encoded value of 'admin'
ADMIN_USER = 'admin'
GB = 1024 ** 3

# Reclaim Policy
RECLAIM_POLICY_RETAIN = 'Retain'
RECLAIM_POLICY_DELETE = 'Delete'

# Access Mode
ACCESS_MODE_RWO = 'ReadWriteOnce'
ACCESS_MODE_ROX = 'ReadOnlyMany'
ACCESS_MODE_RWX = 'ReadWriteMany'

MON_APP_LABEL = "app=rook-ceph-mon"
MDS_APP_LABEL = "app=rook-ceph-mds"
TOOL_APP_LABEL = "app=rook-ceph-tools"
MGR_APP_LABEL = "app=rook-ceph-mgr"
OSD_APP_LABEL = "app=rook-ceph-osd"

# YAML paths
TOOL_POD_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "toolbox_pod.yaml"
)

CEPHFILESYSTEM_YAML = os.path.join(
    TEMPLATE_CSI_FS_DIR, "CephFileSystem.yaml"
)

CEPHBLOCKPOOL_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "cephblockpool.yaml"
)

CSI_RBD_STORAGECLASS_YAML = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "storageclass.yaml"
)

CSI_CEPHFS_STORAGECLASS_YAML = os.path.join(
    TEMPLATE_CSI_FS_DIR, "storageclass.yaml"
)

CSI_PVC_YAML = os.path.join(
    TEMPLATE_PV_PVC_DIR, "PersistentVolumeClaim.yaml"
)

CSI_RBD_POD_YAML = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "pod.yaml"
)

CSI_CEPHFS_POD_YAML = os.path.join(
    TEMPLATE_CSI_FS_DIR, "pod.yaml"
)
CSI_RBD_SECRET_YAML = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "secret.yaml"
)

CSI_CEPHFS_SECRET_YAML = os.path.join(
    TEMPLATE_CSI_FS_DIR, "secret.yaml"
)

CSI_CEPHFS_PVC_YAML = os.path.join(
    TEMPLATE_CSI_FS_DIR, "pvc.yaml"
)

CSI_RBD_PVC_YAML = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "pvc.yaml"
)
CONFIGURE_PVC_ON_MONITORING_POD = os.path.join(
    TEMPLATE_CONFIGURE_PVC_MONITORING_POD, "configuring_pvc.yaml"
)

PGSQL_STORAGECLASS = os.path.join(
    TEMPLATE_PGSQL_DIR, "StorageClass.yaml"
)
PGSQL_BENCHMARK = os.path.join(
    TEMPLATE_PGSQL_DIR, "BenchMark.yaml"
)

NGINX_POD_YAML = os.path.join(
    TEMPLATE_APP_POD_DIR, "nginx.yaml"
)

# Workload-io yamls
FIO_IO_PARAMS_YAML = os.path.join(
    TEMPLATE_FIO_DIR, "workload_io.yaml"
)
FIO_IO_RW_PARAMS_YAML = os.path.join(
    TEMPLATE_FIO_DIR, "workload_io_rw.yaml"
)


# constants
RBD_INTERFACE = 'rbd'
CEPHFS_INTERFACE = 'cephfs'
