<?php

define('APP_ROOT', __DIR__ . '/../');

$database = include(APP_ROOT . "/config/config.local.php");

return [
    'settings' => [
        'displayErrorDetails' => true,
        'determineRouteBeforeAppMiddleware' => true,
        'doctrine' => [
            // If true, metadata caching is forcelly disabled
            'dev_mode' => true,
            // Path where the compiled metadata info will be cached
            // make sure the path exists and it is writable
            'cache_dir' => APP_ROOT . '/data/doctrine/cache',
            // You should add any other path containing annotated antity classes
            'metadata_dirs' => [APP_ROOT . "/src/Entity"],
            'connection' => [
                'driver'    => $database['mysql']['driver'],
                'host'      => $database['mysql']['host'],
                'port'      => (int)$database['mysql']['port'],
                'dbname'    => $database['mysql']['dbname'],
                'user'      => $database['mysql']['user'],
                'password'  => $database['mysql']['password']
            ]
        ],
        'logger' => [
            'name' => 'api-users',
            'logfile' => APP_ROOT . "/data/logs/projectx.log"
        ]
    ]
];