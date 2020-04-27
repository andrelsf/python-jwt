<?php

namespace App\Controller;

use Exception;
use Slim\Router;
use Psr\Http\Message\ServerRequestInterface as Request;
use Psr\Http\Message\ResponseInterface as Response;

class BaseController
{
    protected $router;
    private $bearerToken;
    private $clientAuthJWT;
    const URI_AUTH_JWT = "http://flask-jwt:5000";

    public function __construct(Router $router)
    {
        $this->router = $router;
        $this->clientAuthJWT = new \GuzzleHttp\Client([
            'base_uri' => BaseController::URI_AUTH_JWT
        ]);
    }

    /**
     * Auth middleware invokable class
     * 
     * @param ServerRequestInterface    $request    PSR7 request
     * @param ResponseInterface         $response   PSR7 response
     * @param callable                  $next       Next Middleware
     * 
     * @return ResponseInterface
     */
    public function __invoke(Request $request, Response $response, $next)
    {
        if ( !$request->hasHeader('Authorization') ) {
            return BaseController::sendResponse(
                $response, 'Unauthorized', 401
            );
        }

        try {
            $this->bearerToken = str_replace('Bearer ', '', $request->getHeader('Authorization')[0]);
            $rspAuthJWT = $this->clientAuthJWT->get(
                '/auth/verify',
                [
                    'headers' => [
                        'Content-Type' => 'application/json',
                        'Accept' => 'application/json',
                        'Authorization' => 'Bearer ' . $this->bearerToken
                    ]
                ]
            );
            
            $respController = $next($request, $response);

            return $respController;
        } catch (\GuzzleHttp\Exception\ServerException $err) {
            return BaseController::sendResponse(
                $response, $err->getMessage(), $err->getCode()
            );
        }
    }

    /**
     * Send Response
     * 
     * Responde a requisição passando response, msg e Status Code
     * 
     * @method sendResponse
     * 
     * @param Response  $response
     * @param String    $message
     * @param Integer   $code
     * 
     * @return Response
     */
    private static function sendResponse(
        Response $response, 
        String $message, 
        int $statusCode
    ) {
        return $response->withJson(
            [
                'status' => $statusCode,
                'message' => $message
            ], $statusCode, \JSON_PRETTY_PRINT
        )->withHeader('Content-Type', 'application/json;charset=utf-8');
    }
}