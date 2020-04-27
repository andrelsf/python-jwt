<?php

/**
 * Realizando o agrupamento dos endpoints iniciados por api
 */
$app->group('/api', function()
{
    $this->get('/ping', '\App\Controller\PingController:getPing')->add('Auth');
    /**
     * Dentro de api,
     */
    // $this->group('/resourcesExamples', function()
    // {
    //     $this->post('', '\App\Controller\resourcesExamplesController:addAction');
    //     $this->get('', '\App\Controller\resourcesExamplesController:getMFTsAction');
    //     $this->get('/{id:[0-9]+}', '\App\Controller\resourcesExamplesController:getOneMFTAction');
    // });
});