// vim: et:ts=2:sw=2
// This Jenkinsfile is intended to be used with a companion jenkins-job-builder
// definition. Aside from the credentials it requires which are accessed in the
// 'environment' section of this pipeline, it requires the following parameters:
//   AWS_DOMAIN
//   AWS_PROFILE
//   AWS_REGION
//   CLUSTER_USER
// It may also provide these optional parameters to override the framework's
// defaults:
//   ROOK_IMAGE
//   CEPH_IMAGE
pipeline {
  agent { node { label "rhel-8-large" }}
  environment {
    AWS_SHARED_CREDENTIALS_FILE = """${sh(
      returnStdout: true,
      script: 'echo $WORKSPACE/.aws/credentials'
      )}"""
    AWS_CONFIG_FILE = """${sh(
      returnStdout: true,
      script: 'echo $WORKSPACE/.aws/config'
      )}"""
    AWS_ACCESS_KEY_ID = credentials('openshift-dev-aws-access-key-id')
    AWS_SECRET_ACCESS_KEY = credentials('openshift-dev-aws-secret-access-key')
    PULL_SECRET = credentials('openshift-pull-secret')
  }
  stages {
    stage("Setup") {
      steps {
        sh """
          python3 -V
          pip3 install --user virtualenv
          python3 -m virtualenv venv
          source ./venv/bin/activate
          pip3 install tox
          pip3 install -r requirements.txt
          python3 setup.py develop
          python3 ./.functional_ci_setup.py
          """
      }
    }
    stage("Lint") {
      steps {
        sh """
          source ./venv/bin/activate
          tox -e flake8
          """
      }
    }
    stage("Unit test") {
      steps {
        sh """
          source ./venv/bin/activate
          tox -e py36
          """
      }
    }
    stage("Deploy OCP") {
      steps {
        sh """
        source ./venv/bin/activate
        run-ci -m deployment --deploy --ocsci-conf=ocs-ci-ocp.yaml --cluster-name=${env.CLUSTER_USER}-ocs-ci-${env.BUILD_ID} --cluster-path=cluster --collect-logs
        """
      }
    }
    stage("Deploy OCS") {
      steps {
        sh """
        source ./venv/bin/activate
        run-ci -m deployment --deploy --ocsci-conf=ocs-ci-ocs.yaml --cluster-name=${env.CLUSTER_USER}-ocs-ci-${env.BUILD_ID} --cluster-path=cluster --collect-logs
        """
      }
    }
    stage("Tier 1") {
      steps {
        sh """
        source ./venv/bin/activate
        run-ci -m tier1 --ocsci-conf=ocs-ci-ocs.yaml --cluster-name=${env.CLUSTER_USER}-ocs-ci-${env.BUILD_ID} --cluster-path=cluster --self-contained-html --html=${env.WORKSPACE}/logs/report.html --junit-xml=${env.WORKSPACE}/logs/junit.xml --collect-logs
        """
      }
    }
  }
  post {
    always {
      archiveArtifacts artifacts: 'ocs-ci-*.yaml,cluster/**,logs/**', fingerprint: true
      sh """
        source ./venv/bin/activate
        run-ci -m deployment --teardown --ocsci-conf=ocs-ci-ocs.yaml --cluster-name=${env.CLUSTER_USER}-ocs-ci-${env.BUILD_ID} --cluster-path=cluster --collect-logs
        """
      junit testResults: "logs/junit.xml", keepLongStdio: false
    }
  }
}
