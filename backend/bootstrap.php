<?php

/**
 * BOOTSTRAP: Responsabilidade de configurações
 * Concentra todas as definições feitas no autoload e configurações
 * de dependências da API.
 */
 
require __DIR__.'/vendor/autoload.php';

use Slim\App;
use Slim\Container;
use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;
use Doctrine\ORM\Mapping\Driver\AnnotationDriver;
use Doctrine\Common\Annotations\AnnotationReader;
use Doctrine\Common\Cache\FilesystemCache;
use Monolog\Handler\FingersCrossedHandler;
use Monolog\Handler\StreamHandler;
use App\Controller\BaseController;
use Monolog\Logger;
use Awurth\SlimValidation\Validator;

/**
 * Container Resources adiciona as definições
 */
$container = new Container(require __DIR__ . "/config/settings.php");

/**
 * Validator as a service
 */
$container['validator'] = function () {
    return new Validator();
};

/**
 * Handler logs with Monolog em arquivo
 */
$container['logger'] = function($container)
{
    $logger = new Logger($container['settings']['logger']['name']);
    $logFile = $container['settings']['logger']['logfile'];
    
    $stream = new StreamHandler($logFile, Logger::DEBUG);
    $fingersCrossed = new FingersCrossedHandler($stream, Logger::INFO);
    $logger->pushHandler($fingersCrossed);

    return $logger;
};

/**
 * Erros 404 - Not Fount
 * Handler Exceptions with errors 404
 */
$container['notFoundHandler'] = function ($c) 
{
    return function ($request, $response) use ($c) {
        return $c['response']->withStatus(404)
                             ->withHeader('Content-Type', 'application/json')
                             ->withJson(
                                 ['message' => 'Page not found'],
                                 404,
                                 JSON_PRETTY_PRINT
                             );
    };
};

/**
 * Error Handling returns status code 405 Method Not Allowed
 */
$container['notAllowedHandler'] = function ($c) 
{
    return function ($request, $response, $methods) use ($c) {
        return $c['response']->withStatus(405)
                             ->withHeader('Allow', implode(', ', $methods))
                             ->withHeader('Content-Type', 'application/json')
                             ->withHeader('Access-control-Allow-Methods', implode(', ', $methods))
                             ->withJson([
                                    'status' => 405,
                                    'message' => "Method not allowed; Method must be one of: ".implode(', ', $methods)
                                ], 
                                405,
                                JSON_PRETTY_PRINT);
    };
};

/**
 * Handler de exceções
 * Retorna as exceções e codigos de status via JSON
 */
$container['errorHandler'] = function ($c) 
{
    return function ($request, $response, $exception) use ($c) {
        $statusCode = $exception->getCode() ? $exception->getCode() : 500;
        return $c['response']->withStatus($statusCode)
                             ->withHeader('Content-Type', 'application/json')
                             ->withJson(
                                    ['error' => $exception->getMessage()], 
                                    $statusCode,
                                    JSON_PRETTY_PRINT
                                );
    };
};

/**
 * Diretório de entidades e metadata do doctrine.
 */
$container[EntityManager::class] = function (Container $container): EntityManager 
{
    $config = Setup::createAnnotationMetadataConfiguration(
        $container['settings']['doctrine']['metadata_dirs'],
        $container['settings']['doctrine']['dev_mode']
    );

    $config->setMetadataDriverImpl(
        new AnnotationDriver(
            new AnnotationReader,
            $container['settings']['doctrine']['metadata_dirs']
        )
    );

    $config->setMetadataCacheImpl(
        new FilesystemCache(
            $container['settings']['doctrine']['cache_dir']
        )
    );

    return EntityManager::create(
        $container['settings']['doctrine']['connection'],
        $config
    );
};

/**
 * My UserRepository
 */
// $container[ResitryYourRepositoryHerer::class] = function ($container) 
// {
//     return new ResitryYourRepositoryHerer($container[EntityManager::class]);
// };

/**
 * AUTH Middleware
 */
$container['Auth'] = function ($c) {
    return new BaseController($c->get('router'));
};

/**
 * Instancia GLOBAL da APP (Singleton)
 * Gerenciamento de toda aplicação através de um ponto de acesso global
 * realizando a injeção de dependências dentro de um container.
 */
$app = new App($container);