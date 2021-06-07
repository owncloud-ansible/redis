import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_redis_running_and_enabled(host):
    redis = host.service("redis-server")

    assert redis.is_running
    assert redis.is_enabled


def test_redis_config(host):
    assert "127.0.0.1" in host.run("redis-cli config get bind").stdout
    assert "6379" in host.run("redis-cli config get port").stdout

    assert "300" in host.run("redis-cli config get timeout").stdout
