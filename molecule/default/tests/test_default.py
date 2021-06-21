def test_command(host):
    assert host.command('librenms --version').rc == 0
