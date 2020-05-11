<?php

use Psr7Middlewares\Middleware\TrailingSlash;

/**
 * Carrega todas as configurações
 */
require __DIR__."/../bootstrap.php";

/**
 * Rotas da API
 */
require __DIR__ . "/../config/routes.php";

/**
 * @middleware
 * Tratamento do barra(/) na request
 * true: adiciona a barra(/) no final da URL
 * false: remove a barra(/) do final da URL
 */
$app->add(new TrailingSlash(false));

/**
 * Trusted proxies
 */
$configLocal = require __DIR__ . "/../config/config.local.php";
if (array_key_exists('proxy', $configLocal)) {
    $app->add(new RKA\Middleware\IpAddress(
        $ipAddress['checkProxyHeaders'], 
        $ipAddress['trustedProxies']
    ));
}

/**
 * Executa a aplicação
 */
$app->run();