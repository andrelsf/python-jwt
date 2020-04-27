<?php

namespace App\Controller;

use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

/**
 * @author      Andre L S Ferreira
 * @email       andre.dev.linux@gmail.com
 * @date        15/03/2020
 */
class PingController
{
    /**
     * container class
     */
    private $container;

    /**
     * @method construct
     * @param [object] $container
     */
    public function __construct($container)
    {
        $this->container = $container;
    }

    public function getPing($request, $response, $args)
    {
        return $response->withJson(
            [
                'message' => 'pong'
            ], 200, JSON_PRETTY_PRINT
        )->withHeader('Content-Type', 'application/json;charset=utf-8');
    }
}