<?php

return [
    'mysql' => [
        'driver' => 'pdo_pgsql',
        'host' => '10.1.0.5',
        'port' => 3306,
        'dbname' => 'project',
        'user' => 'project',
        'password' => 'project'
    ],
    'proxy' => array(
        'checkProxyHeaders' => true,
        'trustedProxies' => array(
            'localhost', '127.0.0.1', '10.1.0.1'
        )
    )
];