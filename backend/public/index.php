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
 * Executa a aplicação
 */
$app->run();