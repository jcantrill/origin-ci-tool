import config


def default_config():
    """
    Generate a default configuration.

    :return: the default configuration dictionary
    """
    return dict(
        config_path=config._config_path,
        host_list=config._inventory_path,
        # hosts are the hosts we want to run plays on
        hosts='vms',
        connection='ssh',
        verbosity=1,
        module_path=None,
        forks=5,
        vm_hostname='openshiftdevel',
        # TODO: are these valid defaults? how do we determine what is useful for local testing versus the tool itself?
        become=True,
        become_method='sudo',
        become_user='root',
        check=False
    )


def default_inventory():
    """
    Generate a default inventory, formatted for serialization.

    :return: the default inventory
    """
    return """
localhost

[vms]
"""